import matplotlib.pyplot as plt
from sklearn import datasets


digit_datasets = datasets.load_digits()
print(digit_datasets.target_names[:10])


# import pylab
# for i in range(0, 10):
#     pylab.imshow(digit_datasets.images[i], cmap=pylab.cm.gray_r)
#     pylab.show()
    
plt.imshow(digit_datasets.images[3], cmap=plt.get_cmap('gray'))
plt.show()