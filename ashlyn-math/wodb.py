from PIL import Image, ImageDraw, ImageFont
import os

def mkWODB(a="1",b="2",c="3",d="4",fn="wodb"):
    l = 800
    w = 800
    lw = 10

    cwd = os.getcwd()
    fpPDF = cwd + '/image/'+fn+".pdf"
    fpSVG = cwd + '/image/'+fn+".svg"
    pdf2svgCMD = 'pdf2svg ' + fpPDF + ' ' + fpSVG

    img = Image.new('RGB', (l, w), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # draw the four boxes
    draw.rectangle([(0, 0), (w/2, l/2)], outline=(0, 0, 0), width=lw)
    draw.rectangle([(w/2, l/2), (w, l)], outline=(0, 0, 0), width=lw)
    draw.rectangle([(w/2, 0), (w, l/2)], outline=(0, 0, 0), width=lw)
    draw.rectangle([(0, l/2), (w/2, l)], outline=(0, 0, 0), width=lw)
    
    # draw the numbers inside the boxes
    #font = ImageFont.truetype("/home/ryan/.fonts/NewCM10-Regular.otf", size=200)
    font = ImageFont.truetype("/usr/share/fonts/tex/cmunss.ttf", size=200)
    draw.text((w/4, l/4), a, fill=(0,0,0), anchor="mm", font=font)
    draw.text((3*w/4, l/4), b, fill=(0,0,0), anchor="mm", font=font)
    draw.text((w/4,3*l/4), c, fill=(0,0,0), anchor="mm", font=font)
    draw.text((3*w/4,3*l/4), d, fill=(0,0,0), anchor="mm", font=font)
    
    # save the image as a PDF file
    img.save(fpPDF, "PDF", resolution=100.0)
    os.system(pdf2svgCMD)
