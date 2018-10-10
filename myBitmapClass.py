# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:16:09 2018

@author: Wei-Hsiang Shen
"""

from struct import pack

class Bitmap():
    
    # Constructor for Bitmap
    def __init__(self, width, height):
        self.header_type = 19778 # bitmap signature "BM"
        self.header_reserved1 = 0 # application specific (unused)
        self.header_reserved2 = 0 # application specific (unused)
        self.header_offset = 26 # Offset of pixel raw data
        
        self.info_plane = 1 # 1 plane are used
        self.info_header_size = 12 # information header size
        self.info_pixel_size = 24 # number of bits per pixel
        self.info_width = width
        self.info_height = height

        # size of the whole file
        self.header_file_size = int(self.header_offset+width*height*self.info_pixel_size/8) 

        # list to store the raw data
        self.graphic_data = [(0,0,0)]*self.info_width*self.info_height        

    def Set_Pixel(self, x_coord, y_coord, color):
        if isinstance(color, tuple):
            if x_coord<0 or y_coord<0 or x_coord>self.info_width-1 or y_coord>self.info_height-1:
                raise ValueError('Coordinates out of range')
            if len(color) != 3:
                raise ValueError('Color must consist of three channels')
            self.graphic_data[y_coord*self.info_width+x_coord] = (color[2], color[1], color[0])
        else:
            raise ValueError('Color must consist of three channels')
            
    def Set_Pixel_Gray(self, x_coord, y_coord, intensity):
        if x_coord<0 or y_coord<0 or x_coord>self.info_width-1 or y_coord>self.info_height-1:
            raise ValueError('Coordinates out of range')
        if intensity>255 or intensity<0:
            raise ValueError('Intensity must be in the range of 0~255')
        self.graphic_data[y_coord*self.info_width+x_coord] = (intensity, intensity, intensity)
        

    def Write_File(self, file):
        try:
            f = open(file,'wb')
            
            # Bitmap file header
            # '<' stands for little-endian encoding
            # 'H' stands for unsigned short (2 bytes)
            # 'L' stands for unsigned long (4 bytes)
            f.write(pack('<HLHHL', 
                   self.header_type, 
                   self.header_file_size, 
                   self.header_reserved1, 
                   self.header_reserved2, 
                   self.header_offset))
            
            # Bitmap information header
            f.write(pack('<LHHHH', 
                   self.info_header_size, 
                   self.info_width, 
                   self.info_height, 
                   self.info_plane, 
                   self.info_pixel_size))
            
            # Bitmap raw data
            # 'B' stands for unsigned char (1 bytes)
            for px in self.graphic_data:
                f.write(pack('<BBB', *px))
            # padding until the file is the mutiples of 4
            for i in range (0, (self.info_width*3) % 4):
                f.write(pack('B', 0))
                
        except IOError as e:
            raise IOError("Could not read file , %s"%(e))

#def main():
#    side = 520
#    b = Bitmap(side, side)
#    for j in range(0, side):
#        b.Set_Pixel(j, j, (255, 0, 0))
#        b.Set_Pixel(j, side-j-1, (255, 0, 0))
#        b.Set_Pixel(j, 0, (255, 0, 0))
#        b.Set_Pixel(j, side-1, (255, 0, 0))
#        b.Set_Pixel(0, j, (255, 0, 0))
#        b.Set_Pixel(side-1, j, (255, 0, 0))
#    b.Write_File('file.bmp')
#
#if __name__ == '__main__':
#    main()