from torchvision import transforms

def Copy_and_Crop(tensor):
    crop_length = tensor.shape[3]
    transforms_crop = transforms.CenterCrop(crop_length, crop_length)