import numpy as np
import cv2
import SimpleITK as sitk
import torch

def spatial_transformations_Agumentation(IMG):
    '''
    Create a list representing a random (uniform) sampling of the 3D similarity transformation parameter space.
    As theSimpleITK rotation parametrization uses the vector portion of a versor we don't have an intuitive way of specifying rotations.
    We therefor use the ZYX Euler angle parametrization and convert to versor.

    :param IMG: sitk img
    :return: sitk img
    '''

def PADDing()

def predict_dataloader(image_path,batch_size):
    IMG = sitk.ReadImage(image_path)
    IMG = sitk.GetArrayFromImage(IMG)
    IMG = torch.tensor(IMG)
    IMG_sub_patches = IMG.unfold(0,64,62).unfold(1,64,62).unfold(2,64,62)
    print(IMG_sub_patches.shape)
    print(IMG_sub_patches[3,4,4,:,:,:])
    print(IMG_sub_patches[4,4,4,:,:,:])


if __name__ == '__main__':
    predict_dataloader('D:\\Renyi\\super_resolution\\data\\test_1.tif',0)
    # img = np.arange(0,350).reshape((-1,1))
    # row = np.ones_like(img).reshape(1,-1)
    # fig = np.multiply(img,row)+np.multiply(img.T,row.T)
    # print(fig.shape)
    # row = row[np.newaxis,:].reshape((-1,1,1))
    # print(row.shape)
    # fig = np.multiply(row,fig)+np.multiply(row,fig).T
    #
    # fig = sitk.GetImageFromArray(fig.astype('int16'))
    # sitk.WriteImage(fig,'D:\\Renyi\\super_resolution\\data\\test_1.tif')

