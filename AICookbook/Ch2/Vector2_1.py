from sklearn import datasets

digits = datasets.load_digits()

print(digits.DESCR)

features = digits.data

target = digits.target

print(features[0])