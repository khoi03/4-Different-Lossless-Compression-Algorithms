# 4 Different Lossless Compression Algorithms

## Introduction:
There are numerous lossless compression algorithms utilized for various types of data. In this GitHub repository, we conduct experiments to compare four different lossless compression algorithms—**Arithmetic Coding, LZ77, LZW, and Deflate (PNG)**—sorted in ascending order based on their performance. We evaluate their effectiveness across three data types: **images, text, and sound.**

## Table of contents:
1. [Compressed ratios of each algorithm](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#1-compressed-ratios-of-each-algorithm)

    a.  [Arithmetic Coding](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#a-arithmetic-coding)
  
    b.  [LZ77](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#b-lz77)
  
    c.  [LZW](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#c-lzw)
  
    d.  [Deflate(PNG)](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#d-deflate-png)
  
2.  [Statistic table](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#2--statistic-table)

    a.  [Image](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#a--image)
  
    b.  [Sound](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#b--sound)
  
    c.  [Text](https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms#c--text)
    
    
## 1. Compressed ratios of each algorithm:

**The compressed ratio is calculated as:**  $$\frac{Compressed  File}{Original  File}$$

### a. Arithmetic Coding
-   **Image:**
    
|       Name      |   Ratio   |       Name      |   Ratio   |                    
| :-------------: | :------: | :-------------: | :------: |
| <pre>2heart</pre> |   0.38   | <pre>heart</pre> |   15.61   |
| <pre>background</pre> |   7.69   | <pre>people</pre> |   10.47   |
| <pre>beach</pre> |   6.87   | <pre>pikachu</pre> |      |
| <pre>cartoon</pre> |      | <pre>planet</pre> |   6.57   |
| <pre>hanamichi</pre> |   3.06   | <pre>rukawa</pre> |   11.07   |
| <pre>harrypotter</pre> |   6.24   | <pre>spiderman</pre> |      |
| <pre>todolist</pre> |   23.05   |

-   **Sound:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>00ae03f6</pre> |   11.06   | <pre>0a5cbf90</pre> |   9.39   |
| <pre>00eac343</pre> |   7.86   | <pre>sound</pre> |    5.68    |


-   **Text:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>sample3</pre> |   4.63   | <pre>Text1</pre> |   3.09   |
| <pre>Text</pre> |   4.08   | <pre>Text2</pre> |   2.04   |


### b. LZ77
-   **Image:**
    
|       Name      |   Ratio   |       Name      |   Ratio   |                    
| :-------------: | :------: | :-------------: | :------: |
| <pre>2heart</pre> |   0.03   | <pre>heart</pre> |   0.05   |
| <pre>background</pre> |   3.19   | <pre>people</pre> |   3.45   |
| <pre>beach</pre> |   1.82   | <pre>pikachu</pre> |   0.98   |
| <pre>cartoon</pre> |   2.05   | <pre>planet</pre> |   1.56   |
| <pre>hanamichi</pre> |   0.36   | <pre>rukawa</pre> |   2.90   |
| <pre>harrypotter</pre> |   2.30   | <pre>spiderman</pre> |   1.89   |
| <pre>todolist</pre> |   2.33   |

-   **Sound:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>00ae03f6</pre> |   3.63   | <pre>0a5cbf90</pre> |   2.78   |
| <pre>00eac343</pre> |   3.11   | <pre>sound</pre> |    2.17    |


-   **Text:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>sample3</pre> |   2.25   | <pre>Text1</pre> |   2.11   |
| <pre>Text</pre> |   2.10   | <pre>Text2</pre> |   2.08   |

  
### c. LZW
-   **Image:**
    
|       Name      |   Ratio   |       Name      |   Ratio   |                    
| :-------------: | :------: | :-------------: | :------: |
| <pre>2heart</pre> |   0.01   | <pre>heart</pre> |   0.07   |
| <pre>background</pre> |   1.19   | <pre>people</pre> |   1.32   |
| <pre>beach</pre> |   0.91   | <pre>pikachu</pre> |   0.55   |
| <pre>cartoon</pre> |   0.99   | <pre>planet</pre> |   0.60   |
| <pre>hanamichi</pre> |   0.09   | <pre>rukawa</pre> |   1.10   |
| <pre>harrypotter</pre> |   0.84   | <pre>spiderman</pre> |   0.89   |
| <pre>todolist</pre> |   1.11   |

-   **Sound:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>00ae03f6</pre> |   1.57   | <pre>0a5cbf90</pre> |   1.43   |
| <pre>00eac343</pre> |   1.29   | <pre>sound</pre> |    0.85    |

-   **Text:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>sample3</pre> |   1.63   | <pre>Text1</pre> |   1.08   |
| <pre>Text</pre> |   1.45   | <pre>Text2</pre> |   0.80   |


### d. Deflate (PNG)
-   **Image:**
    
|       Name      |   Ratio   |       Name      |   Ratio   |                    
| :-------------: | :------: | :-------------: | :------: |
| <pre>2heart</pre> |   0.005   | <pre>heart</pre> |   0.009   |
| <pre>background</pre> |   0.66   | <pre>people</pre> |   0.77   |
| <pre>beach</pre> |   0.38   | <pre>pikachu</pre> |   0.16   |
| <pre>cartoon</pre> |   0.44   | <pre>planet</pre> |   0.30   |
| <pre>hanamichi</pre> |   0.06   | <pre>rukawa</pre> |   0.64   |
| <pre>harrypotter</pre> |   0.45   | <pre>spiderman</pre> |   0.42   |
| <pre>todolist</pre> |   0.51   |

-   **Sound:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>00ae03f6</pre> |   0.86   | <pre>0a5cbf90</pre> |   0.66   |
| <pre>00eac343</pre> |   0.67   | <pre>sound</pre> |    0.52    |

-   **Text:**
    
|      Name       |   Ratio   |      Name       |   Ratio   |
| :-------------: | :------: | :-------------: | :------: |
| <pre>sample3</pre> |   0.51   | <pre>Text1</pre> |   0.47   |
| <pre>Text</pre> |   0.48   | <pre>Text2</pre> |   0.47   |
    

## 2.  Statistic table

### a.  Image:

    
    
<p align="center">
    <img src="https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms/assets/80579165/f996e5da-aec8-4770-9b71-b828875f53ee" width=200 height=200>
    &nbsp; &nbsp; &nbsp; &nbsp;
    <img src="https://github.com/khoi03/4-Different-Lossless-Compression-Algorithms/assets/80579165/cb2f78b3-7fc7-4492-a83e-1033d54d11f9" width=200 height=200>
</p>

                                 2heart(Best case)               people(Worst case)
        
    
<table>
  <tr>
    <th>Algorithm</th>
    <th></th>
    <th>Name</th>
    <th>Ratio</th>
  </tr>
  <tr>
    <td rowspan="2"> <pre> AC </pre></td>
    <td>Worst</td>
    <td>todolist</td>
    <td>23.05</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>2heart</td>
    <td>0.38</td>
  </tr>
  <tr>
    <td rowspan="2"> <pre> LZ77 </pre></td>
    <td>Worst</td>
    <td>people</td>
    <td>3.45</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>2heart</td>
    <td>0.03</td>
  </tr>
  <tr>
    <td rowspan="2"> <pre> LZW </pre></td>
    <td>Worst</td>
    <td>people</td>
    <td>1.32</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>2heart</td>
    <td>0.01</td>
  </tr>
  <tr>    
    <td rowspan="2"> <pre> PNG </pre></td>
    <td>Worst</td>
    <td>people</td>
    <td>0.77</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>2heart</td>
    <td>0.005</td>
  </tr>
</table>
    
</sub>


### b.  Sound:

<table>
  <tr>
    <th>Algorithm</th>
    <th></th>
    <th>Name</th>
    <th>Ratio</th>
  </tr>
  <tr>
    <td rowspan="2"> <pre> AC </pre></td>
    <td>Worst</td>
    <td>00ae03f6</td>
    <td>11.06</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>sound</td>
    <td>5.68</td>
  </tr>
  <tr>
    <td rowspan="2"> <pre> LZ77 </pre></td>
    <td>Worst</td>
    <td>00ae03f6</td>
    <td>3.63</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>sound</td>
    <td>2.17</td>
  </tr>
  <tr>
    <td rowspan="2"> <pre> LZW </pre></td>
    <td>Worst</td>
    <td>00ae03f6</td>
    <td>1.57</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>sound</td>
    <td>0.85</td>
  </tr>
  <tr>    
    <td rowspan="2"> <pre> PNG </pre></td>
    <td>Worst</td>
    <td>00ae03f6</td>
    <td>0.86</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>sound</td>
    <td>0.52</td>
  </tr>
</table>
    
</sub>

### c.  Text:

<table>
  <tr>
    <th>Algorithm</th>
    <th></th>
    <th>Name</th>
    <th>Ratio</th>
  </tr>
  <tr>
    <td rowspan="2"> <pre> AC </pre></td>
    <td>Worst</td>
    <td>sample3</td>
    <td>4.63</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>Text2</td>
    <td>2.04</td>
  </tr>
  <tr>
    <td rowspan="2"> <pre> LZ77 </pre></td>
    <td>Worst</td>
    <td>sample3</td>
    <td>2.25</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>Text2</td>
    <td>2.08</td>
  </tr>
  <tr>
    <td rowspan="2"> <pre> LZW </pre></td>
    <td>Worst</td>
    <td>sample3</td>
    <td>1.63</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>Text2</td>
    <td>0.80</td>
  </tr>
  <tr>    
    <td rowspan="2"> <pre> PNG </pre></td>
    <td>Worst</td>
    <td>sample3</td>
    <td>0.51</td>
  </tr>
  <tr>
    <td>Best</td>
    <td>Text2</td>
    <td>0.47</td>
  </tr>
</table>

## Conclusion
In conclusion, based on our experiments, **Deflate (PNG)** consistently demonstrated the best performance across all types of data. Moreover, it exhibits excellent capability in handling complex data. Conversely, **Arithmetic Coding, LZ77, and LZW algorithms** are more suited for simple and regular data, displaying comparatively lower effectiveness.
