from imagededup.methods import PHash
phasher = PHash()

# Generate encodings for all images in an image directory
encodings = phasher.encode_images(image_dir='../Testout')

# Find duplicates using the generated encodings
duplicates = phasher.find_duplicates(encoding_map=encodings)

# from imagededup.utils import plot_duplicates
# # plot duplicates obtained for a given file using the duplicates dictionary
# plot_duplicates(image_dir='path/to/image/directory', 
#                 duplicate_map=duplicates, 
#                 filename='ukbench00120.jpg')
