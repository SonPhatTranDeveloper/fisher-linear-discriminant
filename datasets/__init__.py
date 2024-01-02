import numpy as np
import matplotlib.pyplot as plt


# Generate two 2d gaussian blobs
blob_1 = np.random.multivariate_normal(mean=[5, 0], cov=np.eye(2) , size=30)
blob_2 = np.random.multivariate_normal(mean=[10, 0], cov=np.eye(2), size=30)

if __name__ == "__main__":
    # Display the blobs
    plt.scatter(blob_1[:, 0], blob_1[:, 1], color='blue', label='Class 1')
    plt.scatter(blob_2[:, 0], blob_2[:, 1], color='orange', label='Class 2')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Two Gaussians')
    plt.show()



