from os import listdir
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    filename_list = listdir(image_dir)
    results_dic = dict()

    for filename in filename_list:
        if results_dic.get(filename) is None:
            filename_labels = get_filename_labels(filename)
            results_dic[filename] = filename_labels
        else:
            print(f'key ={filename} already exists in results_dic')
            print(f'\nthe values = {results_dic[filename]}')

    return results_dic

#get_pet_labels('./pet_images/')
def get_filename_labels(filename: str)-> list:
    return [label for label in filename.lower().strip().split('_') if label.isalpha()]

dic = get_pet_labels('./pet_images/')
print(dic)