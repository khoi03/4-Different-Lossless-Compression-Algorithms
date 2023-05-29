import numpy as np
from PIL import Image
import base64
import io
import os
import pickle
from scipy.io.wavfile import read,write
import time

class LZ77:
    def __init__(self, input, search_size, lookahead_size):
        self.input = input
        self.search_size = search_size
        self.lookahead_size = lookahead_size
        self.compressed_data = []
        self.decompressed_data = ''
        
    def compress(self):
        self.compressed_data = []
        
        i = 0
        while i < len(self.input):
            search_buffer_start = max(0, i - self.search_size)
            search_buffer = self.input[search_buffer_start:i]
            lookahead_buffer = self.input[i:i + self.lookahead_size]
            
            longest_match = ''
            next_character = lookahead_buffer[0]

            for j in range(1, len(lookahead_buffer) + 1):
                substring = lookahead_buffer[:j]

                if substring in search_buffer:
                    longest_match = substring
                    if j < len(lookahead_buffer):
                        next_character = lookahead_buffer[j]
                    elif (i + self.lookahead_size < len(self.input)):
                        next_character = self.input[i + self.lookahead_size]
                    else:
                        next_character = ''
                else:
                    break

            distance = len(search_buffer) - search_buffer.rindex(longest_match)
            length = len(longest_match)

            self.compressed_data.append((distance, length, next_character))
            i += length + 1

        return self.compressed_data
    
    def decompress(self, compressed_data):
        self.decompressed_data = ''
        for entry in compressed_data:
            distance, length, next_character = entry
            start_index = len(self.decompressed_data) - distance
            end_index = start_index + length
            substring = self.decompressed_data[start_index:end_index]
            self.decompressed_data += substring + next_character
            
        return self.decompressed_data

class Image_Compression(LZ77):
    def __init__(self, type, input, search_size, lookahead_size, input_path, output_file, output_path):
        super().__init__(input, search_size, lookahead_size)
        self.type = type
        self.input_path = input_path
        self.output_file = output_file
        self.output_path = output_path
        self.encoded_bytes = None
        
    def read_data(self):
        if (self.type == "image" or self.type == "sound"):
            with open(self.input_path, 'rb') as f:
                data = f.read()
            
            self.encoded_bytes = base64.b64encode(data).decode('utf-8')
        else:
            with open(self.input_path, 'r') as f:
                data = f.read()
                
            self.encoded_bytes = data
            
        self.input = self.encoded_bytes
        print(len(self.input))
    def write_compressed_data(self):
        compressed_data = self.compress()
        with open(self.output_file,"wb") as output:
            # output.write(str(compressed_data))
            pickle.dump(compressed_data,output)
            
    def recovery(self):
        with open(self.output_file, "rb") as cf:
            # string_list = cf.read()
            string_list = pickle.load(cf)
        
        # print(string_list)
        # temp = eval(string_list)
        decoded_string = self.decompress(string_list)
        if (self.type == "image"):
            decoded_bytes = base64.b64decode(decoded_string)
            stream = io.BytesIO(decoded_bytes)
            image = Image.open(stream)
            image = image.convert("RGB")
            image.save(self.output_path)
        elif (self.type == "sound"):
            decoded_bytes = base64.b64decode(decoded_string)
            with open(self.output_path, "wb") as f:
                f.write(decoded_bytes)
        else:
            with open(self.output_path, 'w') as f:
                f.write(decoded_string)
    

class Running_Data(Image_Compression):
    def __init__(self, type, search_size, lookahead_size, data_folder_path, output_folder_path):
        super().__init__(type, None, search_size, lookahead_size, None, None, None)
        # self.input_folder_path = "Data\PNG"
        self.output_folder_path = output_folder_path #"Compressed output"
        self.data_folder_path = data_folder_path #"Data\BMP"
    
    def save_compressed_data(self):
        for file_name in os.listdir(self.data_folder_path):
            file_path = os.path.join(self.data_folder_path, file_name) #read images via this path
            
            output_name = file_name.replace(os.path.splitext(file_name)[1], "") #Output's name, such as Compressed output/2heart
            pkl_path = output_name + ".pkl"
            output_folder = os.path.join(self.output_folder_path, output_name)
            output_pkl_path = os.path.join(output_folder, pkl_path)
            output_img_path = os.path.join(output_folder, "decompressed_"+file_name)
            os.makedirs(output_folder, exist_ok=True)
            
            self.input_path = file_path
            self.output_file = output_pkl_path
            self.output_path = output_img_path
            print("Compressed data saved at", self.output_file)
            start_time = time.time()
            self.read_data()
            self.write_compressed_data()
            self.recovery()
            end_time = time.time()
            
            self.execution_time = end_time - start_time 
    def calculate_ratio(self):
        pkl_ratio_path = self.output_folder_path + "\compression_ratio.txt"
        for file_name in os.listdir(self.data_folder_path):
            file_path = os.path.join(self.data_folder_path, file_name)
            image_size = os.path.getsize(file_path)

            name = os.path.splitext(file_name)
            output_name = file_name.replace(name[1], "") 
            
            pkl_path = output_name + ".pkl"
            output_folder = os.path.join(self.output_folder_path, output_name)
            output_pkl_path = os.path.join(output_folder, pkl_path)
            pkl_size = os.path.getsize(output_pkl_path)
            
            print("Input's size:", image_size)
            print("Compressed file's size:", pkl_size)

            with open(pkl_ratio_path, "a") as f:
                temp = name[0] + "(Search buffer: {}, Lookahead buffer: {}): ".format(self.search_size, self.lookahead_size) \
                    + str(pkl_size / image_size)
                f.write(temp + "\n")

        with open(pkl_ratio_path, "a") as f:
            f.write(str(self.execution_time) + "\n")
# print(lz77.compress())
# print(lz77.decompress())


# image_compression = Image_Compression('image',None, 100, 100, "2heart.bmp","2heart.pkl", "decompressed_2heart.bmp")
# image_compression.read_data()
# image_compression.write_compressed_data()
# image_compression.recovery()

# input = "ababcbababaa"
# test_lz77 = LZ77(input, 4, 3)
# print(test_lz77.compress())
# print(test_lz77.decompress(test_lz77.compress()))

#sound
type = "sound"
output_folder_path = "Compressed output\Sounds"
data_folder_path = "Data\Sound"
rd = Running_Data(type, 10000, 10000, data_folder_path, output_folder_path)
rd.save_compressed_data()
rd.calculate_ratio()
#image
# type = "image"
# output_folder_path = "Compressed output\Images"
# data_folder_path = "Data\BMP"
# rd = Running_Data(type, 5000, 5000, data_folder_path, output_folder_path)
# rd.save_compressed_data()
# rd.calculate_ratio()
#text
# type = "text"
# output_folder_path = "Compressed output\Texts"
# data_folder_path = "Data\Text"
# rd = Running_Data(type, 1500, 1500, data_folder_path, output_folder_path)
# rd.save_compressed_data()
# rd.calculate_ratio()