#!/usr/bin/python3

## HW1 | Principle Component Analysis (PCA) and K-Nearest Neighbour
## Clustering
##
## AUTHOR: Zeyuan Hu <iamzeyuanhu@utexas.edu | EID: zh4378>
##
## INSTRUCTIONS
## ------------
##
##

import numpy as np
from scipy import linalg as la
import scipy.io as spio
import scipy.stats as spstats
import matplotlib.pyplot as plt
from sklearn import neighbors

## Read in the data file
mat = spio.loadmat('digits.mat')
testLabels = mat['testLabels']
testImages = mat['testImages']
trainImages = mat['trainImages']
trainLabels = mat['trainLabels']

## Number of training images we use
M = 1000

## Set nRedDim
nRedDim = 1

## Construct our data matrix with dimension 784xM. 784 is calculated by
## 784 = 28*28
data = trainImages[:,:,0,0:M].reshape(784,M).astype('float')

## We first calculate the "average face"
mu = np.mean(data,axis=1)
data -= np.tile(mu.reshape(784,1),M).astype(data.dtype)
#standard = np.std(data,axis=1)
#data_normalized = np.divide(data, (standard+0.0001).reshape(784,1))

## Now we calculate the covariance matrix
#C = np.cov(data)
C = np.dot(data, data.T)
#C = np.dot(data_normalized, np.transpose(data_normalized)) * (1/M)

## Compute the eigenvalues and eigenvectors and sort into descending order
evals, evecs = np.linalg.eig(C)
indices = np.argsort(evals) # is in ascending order
indices = indices[::-1]     # change to descending order
evecs = evecs[:,indices]
evals = evals[indices]

## Try to determine the number of principal component nRedDim
U,S,V = np.linalg.svd(C)
print('X  Rate')
for x in range(1,M):
    rate = S[:x].sum()/S.sum()
    print('{0:2d} {1:3f}'.format(x,rate))
    if rate >= 0.99:
        nRedDim = x
        break

## select the top nRedDim eigenvectors
evecs = evecs[:,:nRedDim]

## normalize eigenvectors
evecs = np.divide(evecs, np.linalg.norm(evecs, axis=0))

x = np.dot(np.transpose(evecs), data)
## Compute the original data
y = np.dot(evecs,x)+np.tile(mu.reshape(784,1),M)

plt.imshow(y[:,1].reshape(28,28).real) 
plt.show()

# Project the test data to the eigenspace
# n_neighbors = 3
# #num_testImages = testImages.shape[3]
# num_testImages = 300
# testImages_use = testImages[:,:,0,0:num_testImages].reshape(784, num_testImages)
# test_mu = np.mean(testImages_use,axis=1)
# testImages_normalize = testImages_use -  np.tile(test_mu.reshape(784,1),num_testImages).astype(testImages_use.dtype)
# testImages_es = np.dot(evecs.T,testImages_normalize)
# trainImages_es = np.dot(np.transpose(evecs), data)
# trainLabels_arr = np.squeeze(trainLabels)
# testLabels_arr = testLabels.squeeze()
# num_trainImages = data.shape[1]
# classification_result = np.zeros(testLabels.shape[1])

# for x in range(num_testImages):
#     distance = np.zeros(num_trainImages)
#     for y in range(num_trainImages):
#         distance[y] = np.linalg.norm(testImages_es[:,x] - trainImages_es[:,y])
#     classification_result[x] = spstats.mode(trainLabels_arr[distance.argsort()[-n_neighbors:]])[0].item(0)
#     print(classification_result[x])

# accuracy = np.sum(classification_result == testLabels_arr) / float(testLabels.shape[1])
# print(accuracy)

# # M = 400 11.35%
# # M = 500 11.35%
# # M = 600 11.35%