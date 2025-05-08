#Spectral smoothing with idl algorithm: https://www.l3harrisgeospatial.com/docs/smooth.htmlc
#https://archive.stsci.edu/iue/manual/dacguide/node83.html

import numpy as np

def smooth(data, w):
    
    '''
    smoothing algorithm as in IDL SMOOTH function
    https://www.l3harrisgeospatial.com/docs/smooth.htmlc
    
    input:
    data -> 1D array
    w -> window size (must be odd)
    
    output:
    smoothed array (smooth_data) -> 1D array
    '''
    
    if (w % 2) == 0: #checking w is odd 
        print("window length must be odd, {0} will be set to {1}".format(w,w+1)) 
        w = w + 1 #putting w to an odd value
    
    N = len(data)
    smooth_data = np.zeros(N)
    
    for i, sp in enumerate(data):
        
        if 0.5*(w-1) <= i <= N-0.5*(w+1): #boundary control
        
            start_index = i-int(0.5*w) #starting index
            end_index = i + w - 1 -int(0.5*w) #ending index
            smooth_data[i] = np.nanmean(data[start_index:end_index+1]) #moving average ignoring NaNs
            
        else:
            smooth_data[i] = data[i] #algorithm is not applied at boudary
            
    return smooth_data