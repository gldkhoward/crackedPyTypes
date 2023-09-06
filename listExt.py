"""
Module to expand the list type with some useful methods for data analytics.
""" 
import numpy as np

class listExt(list):
    """
    Class to extend the list type with some useful methods for data analytics.
    """

    def mean(self):
        '''
        Function to calculate the mean of a list.

        Parameters:
            self (): list to be averaged.
        
        Returns:
            mean (): mean of the list.
        '''
        return sum(self)/len(self)
    
    def median(self):
        '''
        Function to calculate the median of a list. Will work even

        Parameters:
            self (): list to be averaged.
        
        Returns:
            median (): median of the list.
        '''
        srtd = sorted(self)
        mid = len(self)//2
        return (srtd[mid] + srtd[~mid])/2      

    def N_minMax(self, rangeArr):
        '''
        Function to normalize an array based a input array containing min and max values.

        If the input array is [0,1,2,3,4,5,6,7,8,9,10] and border array is [-1,1] the returned array would be
        [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1]

        Also converts ints to floats to avoid rounding errors.

        Parameters:
        self (): array to be normalized.
        borders (): array containing min and max values.
        
        Returns:
            nArr (): normalized array.
        '''
        newMin, newMax = rangeArr 
        aMin, aMax = np.amin(self), np.amax(self)
        return (self - aMin)*(newMax-newMin)/(aMax - aMin)+newMin

    
    def N_Zscore(self):
        '''
        Function to z an array based on z-score.

        Parameters:
            self (): array to be normalized.
        
        Returns:
            nArr (): normalized array.
        '''
        mean = np.mean(self)
        std = np.std(self)
        return (self - mean)/std