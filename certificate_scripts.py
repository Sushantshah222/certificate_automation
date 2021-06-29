from PIL import Image, ImageFont, ImageDraw 
import pandas as pd





if __name__ == "__main__":
    name = pd.read_csv("/home/celeritas/Downloads/file.csv",delimiter=',')
    # features = name.iloc[1:38,2:3]
    data = name["Name:"][0:37]





    font = ImageFont.truetype(r'/home/celeritas/Downloads/font.otf', 100) 


    
for texts in data[0:7]:
    if type(texts) == type(0.5):
        pass
    else:
        
        texts = texts.upper()
        image = Image.open(r'/home/celeritas/Downloads/Trainers.png') 

        draw = ImageDraw.Draw(image) 
        width,height = image.size

        text_width,text_height = draw.textsize(texts,font)

        draw.text(((width - text_width) / 2,1075),texts,fill= "#6f5e76",font = font) 

        image.save("{}.png".format(texts))




