from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

#แบ่งข้อมูล 80% trainningset 20% testset
x_train, x_test, y_train, y_test = train_test_split(iris["data"], iris["target"], test_size=0.2, random_state=0)

print(x_train.shape)
print(x_test.shape)

print(y_train.shape)
print(y_test.shape)


