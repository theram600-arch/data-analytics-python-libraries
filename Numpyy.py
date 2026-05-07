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



                                                                    #  zeros and ones
# tw = np.array([[0,1,2,3,5], 
#                 [3,4,5,6,8],                                    
#                 [6,7,8,8,9]])
# # Numpy Zeroes
# numpy_ones = np.zeros((3,3),dtype=int,order='C')

# numpy_ones = np.ones((3,3),dtype=int,order='C')
# print(numpy_ones)





                                                                        #    reshape
# tw = np.array([[0,1,2,3], 
#                 [3,4,5,6],                                    
#                 [6,7,8,8]])

# tt=tw.reshape(6,2)
# print(tt)




# tw = np.array([[0,1,2,3], 
#                 [3,4,5,6],                                    
#                 [6,7,8,8]])
# flattened = tw.flatten()
# print(flattened)







                                                                             ## Horitzontal Stack
# np_list_one = np.array([1,2,3])
# np_list_two = np.array([4,5,6])

# print(np_list_one + np_list_two)

# print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))





                                                                                #   random number genration
# rano=np.random.randint(2,8,size=(3,3))
# print(rano)





# tw = np.array([[0,1,2,3], 
#                 [3,4,5,6],                                    
#                 [6,7,8,8]])
# arr = np.array([10, 20, 30, 40, 50])
# print(sum(tw))
# print(np.max(tw))
# print(np.mean(arr))
# print(np.min(arr))



