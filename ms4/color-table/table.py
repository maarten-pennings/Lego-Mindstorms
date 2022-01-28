#!/usr/bin/python3


# table.py - Script creating a color table for a LEGO 3x3 color LED matrix
# 2022 jan 28  v1  Maarten Pennings  Created
version = "v1"


import os
import io
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


div_grid_hlen      = 50  # width of a cell in the table
div_grid_vlen      = 60  # height of a cell in the table
div_grid_hsep      = 1   # (horizontal) border thickness in the table
div_grid_vsep      = 1   # (vertical) border thickness in the  table
div_grid_title     = 28  # height for title at bottom in the table
                   
div_grid_xcount    = 16
div_grid_ycount    = 16
          
div_colorbox_width = 40
div_colorbox_height= 20
          
div_mainfont_name  ="consolab.ttf"
div_mainfont_size  = 20

div_smallfont_name ="consolab.ttf"
div_smallfont_size = 14

div_grid_linecol   = "black"
div_grid_bgcol     = "white"
div_hitext_color   = "black"
div_lotext_color   = "silver"
                   
# Converts integer `val` to an 2 char long hexadecimal string 
def hex2(val) :
  return ("00"+hex(val)[2:])[-2:]

# Convert integer ascii value to character (but makes some unprintable ones readable)
def chrr(ascii) :
  if   ascii <0x20 : return f"\{ascii:02X}";
  elif ascii==0x20 : return "□"
  elif ascii>=0x7F : return f"\{ascii:02X}";
  return chr(ascii)


div_palette = [
 (0,0,0), #  0 black
 (215,0,154), #  1 magenta
 (163,74,198), #  2 violet
 (24,145,242), #  3 blue
 (21,180,160), #  4 turquoise
 (32,189,124), #  5 mint
 (15,168,73), #  6 green
 (249,212,84), #  7 yellow
 (253,162,51), #  8 orange
 (253,0,30), #  9 red
 (255,255,255), # 10 white
]

def palette_scaleup() :
  palette = []
  for r,g,b in div_palette :
    m = max(r,g,b)
    f = 255/m if m>0 else 1
    n = ( int(r*f), int(g*f), int(b*f) )
    palette.append(n) 
  return palette

full_palette = palette_scaleup()

def darken( color, percent ) :
  r,g,b = color
  percent = 10*percent**0.5 # non-linear to get some color for low brightness
  return int(r*percent/100), int(g*percent/100), int(b*percent/100)


def draw_colorbox(draw,x,y,brightnesspercent,colorindex) :
  if colorindex>=len(full_palette) : return
  if brightnesspercent==0 : return
  if brightnesspercent>100 : return
  draw.rectangle([x,y,x+div_colorbox_width-1,y+div_colorbox_height-1], darken(full_palette[colorindex],brightnesspercent) )
  draw.rectangle([x,y,x+div_colorbox_width-1,y+div_colorbox_height-1], outline="black", width=1 )


def table() :
  # Compute size for image to generate
  width  = div_grid_xcount*div_grid_hlen + (div_grid_xcount+1)*div_grid_hsep
  height = div_grid_ycount*div_grid_vlen + (div_grid_ycount+1)*div_grid_vsep       + div_grid_title + div_grid_vsep
  # Create image of computed size
  image = Image.new("RGBA", (width,height), div_grid_linecol ) 
  draw = ImageDraw.Draw(image)
  mainfont = ImageFont.truetype(div_mainfont_name, div_mainfont_size)
  smallfont = ImageFont.truetype(div_smallfont_name, div_smallfont_size)
  # Create the grid
  for yy in range(div_grid_ycount) :
    y0 = yy*(div_grid_vlen+div_grid_vsep) + div_grid_vsep
    y1 = y0+div_grid_vlen-1
    for xx in range(div_grid_xcount) :
      y = y0+1 # vertical cursor in cell
      ascii = yy*div_grid_xcount+xx
      # Draw the grid cell
      x0 = xx*(div_grid_hlen+div_grid_hsep) + div_grid_hsep
      x1 = x0+div_grid_hlen-1
      draw.rectangle([x0,y0,x1,y1],fill=div_grid_bgcol)
      # Draw the hex ASCII value
      label = f"{ascii:02X}"
      sizex,sizey = draw.textsize( label, font=smallfont)
      draw.text( (x0+1,y), label, div_lotext_color, font=smallfont)
      # Draw the dec ASCII value
      label = f"{ascii}"
      sizex,sizey= draw.textsize( label, font=smallfont)
      draw.text( (x1-sizex-1,y), label, div_lotext_color, font=smallfont)
      y += div_smallfont_size
      # Draw the ASCII character
      label = chrr(ascii)
      sizex,sizey= draw.textsize( label, font=mainfont)
      draw.text( (x0+(x1-x0-sizex)/2,y), label, div_hitext_color, font=mainfont)
      y += div_mainfont_size
      # Draw color box
      draw_colorbox( draw, x0+(div_grid_hlen-div_colorbox_width)//2, y, yy*10, xx )
  # Draw title cell
  x0 = div_grid_hsep
  y0 = div_grid_ycount*(div_grid_vlen+div_grid_vsep) + div_grid_vsep
  draw.rectangle([x0,y0,x0+width-2*div_grid_hsep-1,y0+div_grid_title-1],fill=div_grid_bgcol)
  # Draw the title
  label = f"LEGO 45608: 3x3 Color Light Matrix"
  sizex,sizey= draw.textsize( label, font=mainfont)
  draw.text( ((width-sizex)/2,y0+(div_grid_title-sizey)/2+2), label, div_hitext_color, font=mainfont)
  return image


def main() :
  image = table()
  filename = f"table.png"
  image.save(filename)
  print( f"  saving {filename}")


# The entry point for command line test
if __name__ == "__main__":
  print( f"tables.py {version}")
  main()
