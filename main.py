from base64 import b64encode, b64decode
from PIL import Image
from imageio import get_writer,imread


def b64_to_img(inp,n):
  im = Image.new('RGBA',(3840,2160))
  im.putdata([(ord(inp[i]),ord(inp[i+1]),ord(inp[i+2]),ord(inp[i+3])) for i in range(0,len(inp)-5,4)])
  im.save(f'image{str(n)}.png')
def img_decode_to_b64(im):
    return ''.join([chr(i) for tup in im.getdata() for i in tup])

def file_to_b64(filename):
  return b64encode(open(filename,'rb').read()).decode('ascii')

def main(file):
  counter = 0
  for i in range(0,len(file),33177600):
    b64_to_img(file[i:i+33177600],counter)
    counter += 1
  video = get_writer('encoded.mp4',fps=60)
  for i in range(counter):
    video.append_data(imread(f'image{str(i)}.png'))
  video.close()
    
    
    
  
main(file_to_b64('/Users/433MEA/Documents/iphone-unlocker-mac.dmg')) #file size 48,469,801 bytes reduced to 2,111,863








