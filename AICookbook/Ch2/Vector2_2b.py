from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

features, target = make_classification(
    n_samples=100,
    n_features=3,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    weights=[0.25, 0.75],
    random_state=1,
)

# View feature matrix and target vector
print("Feature Matrix\n", features[:3])
print("Target Vector\n", target[:3])

plt.scatter(features[:,0], features[:,1], c = target)
plt.show()
