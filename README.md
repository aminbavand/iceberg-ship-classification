# Kaggle Competition: Statoil/C-CORE Iceberg Classifier Challenge in Kaggle.


## Data desciption

### `train.json`, `test.json`

The data (`train.json`, `test.json`) is presented in json format. The files consist of a list of images, and for each image, you can find the following fields:

- `id` - the id of the image
- `band_1`, `band_2` - the flattened image data. Each band has 75x75 pixel values in the list, so the list has 5625 elements. Note that these values are not the normal non-negative integers in image files since they have physical meanings - these are float numbers with unit being dB. Band 1 and Band 2 are signals characterized by radar backscatter produced from different polarizations at a particular incidence angle. The polarizations correspond to HH (transmit/receive horizontally) and HV (transmit horizontally and receive vertically). More background on the satellite imagery can be found here.
- `inc_angle` - the incidence angle of which the image was taken. Note that this field has missing data marked as "na", and those images with "na" incidence angles are all in the training data to prevent leakage.
- `is_iceberg` - the target variable, set to 1 if it is an iceberg, and 0 if it is a ship. This field only exists in `train.json`.


## Running the Project
This project was run with gpu in google colab notebook. Also, the data is not included in this repository as it would take a long time to be uploaded. To run the project:

1. Clone the repository
```
$ git clone git@github.com:aminbavand/iceberg-ship-classification.git
```

2. Check into the cloned repository
```
$ cd iceberg-ship-classification
```

3. Create a Data folder in the repository
```
$ mkdir Data
```

4. Download the data from [Kaggle](https://www.kaggle.com/c/statoil-iceberg-classifier-challenge/data)

5. Unzip and copy the data and paste it into the Data folder in the project directory

6. Run main_cnn.py file
```
$ python3 main_cnn.py
```


