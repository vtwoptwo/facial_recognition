

# Eigenface


# Model for the siamese network

```
Metal device set to: Apple M1

systemMemory: 16.00 GB
maxCacheSize: 5.33 G

 Layer (type)                Output Shape              Param #   
=================================================================
 input image (InputLayer)    [(None, 105, 105, 3)]     0         
                                                                 
 conv1 (Conv2D)              (None, 96, 96, 64)        19264     
                                                                 
 maxpool1 (MaxPooling2D)     (None, 48, 48, 64)        0         
                                                                 
 conv2 (Conv2D)              (None, 42, 42, 128)       401536    
                                                                 
 maxpool2 (MaxPooling2D)     (None, 21, 21, 128)       0         
                                                                 
 conv3 (Conv2D)              (None, 18, 18, 128)       262272    
                                                                 
 maxpool3 (MaxPooling2D)     (None, 9, 9, 128)         0         
                                                                 
 conv4 (Conv2D)              (None, 6, 6, 256)         524544    
                                                                 
 flatten_1 (Flatten)         (None, 9216)              0         
                                                                 
 dense1 (Dense)              (None, 4096)              37752832  
                                                                 
=================================================================
Total params: 38,960,448
Trainable params: 38,960,448
Non-trainable params: 0
_________________________________________________________________


Model: "siamese_network"
__________________________________________________________________________________________________
 Layer (type)                   Output Shape         Param #     Connected to                     
==================================================================================================
 input_image (InputLayer)       [(None, 105, 105, 3  0           []                               
                                )]                                                                
                                                                                                  
 validation_image (InputLayer)  [(None, 105, 105, 3  0           []                               
                                )]                                                                
                                                                                                  
 embedding_layer (Functional)   (None, 4096)         38960448    ['input_image[0][0]',            
                                                                  'validation_image[0][0]']       
                                                                                                  
 similarity (L1Dist)            (None, 4096)         0           ['embedding_layer[0][0]',        
                                                                  'embedding_layer[1][0]']        
                                                                                                  
 classification (Dense)         (None, 1)            4097        ['similarity[0][0]']             
                                                                                                  
==================================================================================================
Total params: 38,964,545
Trainable params: 38,964,545
Non-trainable params: 0
__________________________________________________________________________________________________

```