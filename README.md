# Image texture of ultrahigh carbon steel microstructures
This repo contains two files: "image_crop.py" is used to remove the black bar at the bottom of the micrograph. The jupyter notebook is the main file doing analysis.

In the notebook, the following tasks were performed:
* Preprocess the dataset and split it into train and test parts.  
* Extract features from different intermediate layers and compare their performance.
* Use the highest accurate layer to obtain features to train a group of binary SVM classifiers.
* Use voting scheme to obtain a multi-class classifier.

## Test error on test set for pairwise two-label classifiers:
|                 | spheroidite network  | spheroidite pearlite | spheroidite Widmanstatten | network pearlite | network Widmanstatten | pearlite Widmanstatten |
|-----------------|----------------------|---------------------------|------------------|-----------------------|------------------------|-------------|
| spheroidite     | 0.00729927           | 0.0036496                 | 0.13138686       |                       |                        |             |
| network         | 0.10714              |                           |                  | 0.080357              | 0.0535714              |             |
| pearlite        |                      | 0.08333                   |                  | 0                     |                        | 0           |
| Widmanstatten   |                      |                           | 0.380952         |                       | 0                      | 0.285714286 |

## Test error on test set for multi-label voting classifiers:
|                                | Multi-label voting classifiers |
|--------------------------------|-------------|
| spheroidite                    | 0.142335766 |
| network                        | 0.107142857 |
| pearlite                       | 0.083333    |
| Widmanstatten                  | 0.380952381 |

Source of dataset: http://uhcsdb.materials.cmu.edu/                                        
