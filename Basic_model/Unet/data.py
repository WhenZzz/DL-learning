from torch.utils.data import Dataset
import os
from PIL import Image

from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize((572, 572)),
    transforms.ToTensor()
])

class MyDataset(Dataset):
    def __init__(self, path):
        self.path = path
        self.name_seg = os.listdir(os.path.join(path, 'seg'))
        self.name_origin = os.listdir(os.path.join(path, 'origin'))

    def __len__(self):
        return len(self.name_seg)
    
    def __getitem__(self, index):
        seg_name = self.name_seg[index] # xx.png
        seg_path = os.path.join(self.path, 'seg', seg_name)
        seg_img = Image.open(seg_path)

        origin_name = self.name_origin[index]
        origin_path = os.path.join(self.path, 'origin', origin_name)
        origin_img = Image.open(origin_path)

        return transform(origin_img), transform(seg_img)
    
if __name__ == '__main__':
    data = MyDataset(r'D:/Github/DL-learning/Basic_model/Unet/dataset')

    print(data[0][0].shape)