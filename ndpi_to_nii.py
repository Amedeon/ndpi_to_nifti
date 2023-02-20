import os
import nibabel as nib
import tifffile
import numpy as np


# Path to the directory containing the NDPI images
ndpi_dir = '/where_ndpi'

ndpisplit_path='path_to_ndpisplit'
# Loop through each NDPI image in the directory
for filename in os.listdir(ndpi_dir):
    if filename.endswith('.ndpi'):
        # Construct the input and output file paths
        input_path = os.path.join(ndpi_dir, filename)
        tiff_path = os.path.join(nifti_dir, os.path.splitext(filename)[0] + '_x2.5_z0.tif') #change x2.5 to other magnification if more needed
        output_path = os.path.join(nifti_dir, os.path.splitext(filename)[0] + '.nii')
        # Use ndpisplit to convert the image to TIFF format
        os.system(f'ndpisplit_path+'ndpisplit' -x2.5 {input_path}')
        

# Path to the directory containing the TIF images
tif_dir =tiff_path

# Path to the directory where the NIfTI images will be saved
nifti_dir = 'where_you_want_to_store_nifti_images'

# Loop through each TIF image in the directory
for filename in os.listdir(tif_dir):
    if filename.endswith('.tif'):
        # Construct the input and output file paths
        input_path = os.path.join(tif_dir, filename)
        output_path = os.path.join(nifti_dir, os.path.splitext(filename)[0] + '.nii')
        # Load the TIF image and save it in NIfTI format
        img = tifffile.imread(input_path)
        nifti_img = nib.Nifti1Image(img, np.eye(4))
        nib.save(nifti_img, output_path)
