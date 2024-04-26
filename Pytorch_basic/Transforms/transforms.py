from torchvision import transforms
from PIL import Image

img_path = "D:/Github/DL-learning/Pytorch_basic/The_use_of_Tensorboard/data/train/ants_image/0013035.jpg"
img = Image.open(img_path)
# print(img)
tensor_trans = transforms.ToTensor