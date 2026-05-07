import numpy as np
import random



# arr=np.array([1,2,3,4,5])
# print(type(arr))

# print(np.__version__)



# two_dimensional_list = np.array([[0,1,2], [3,4,5], [6,7,8]])
# print(type(two_dimensional_list))



                                                                                        #  tolist:  convert array onto list
# two_dimensional_list = np.array([[0,1,2], [3,4,5], [6,7,8]],dtype=float)
# print(two_dimensional_list)

# convert=two_dimensional_list.tolist()
# print(type(convert))
# print(convert)





                                                                                        #   shape: show how many rows and column in it , first show rows and second columns                                         
# two_dimensional_list = np.array([[0,1,2], [3,4,5], [6,7,8]])
# print(two_dimensional_list.shape)
# tw = np.array([[0,1,2,3,5], 
#                 [3,4,5,6,8],                                    
#                 [6,7,8,8,9]])
# print(tw.shape)





                                                                                #  size: show how many elements in array
# tw = np.array([[0,1,2,3,5], 
#                 [3,4,5,6,8],                                    
#                 [6,7,8,8,9]])
# print(tw.size)






                                                                        #  we can perform operation like addition, subtraction, mutiplacation, division on it
# tw = np.array([[0,1,2,3,5], 
#                 [3,4,5,6,8],                                    
#                 [6,7,8,8,9]])
# oo=tw+10
# print(oo)




                                                                    #    indexing
# tw = np.array([[0,1,2,3,5], 
#                 [3,4,5,6,8],                                    
#                 [6,7,8,8,9]])
# fore=tw[1]
# print(fore)





                                                                        # slicing
# tw = np.array([[0,1,2,3,5], 
#                 [3,4,5,6,8],                                    
#                 [6,7,8,8,9]])
# # array[start:end:step]
# print(tw[0,1])
# print(tw[0:1,1:2])
# print(tw[0:1,1:2]).item()




# tw = np.array([[0,1,2,3,5], 
#                 [3,4,5,6,8],                                    
#                 [6,7,8,8,9]])
# tw[1,2]=33
# print(tw)

