import numpy as np

class Model:

    @staticmethod
    def Psi(theta):
        # return 1
        # return theta[1]
        return np.array([0, theta[1]])

    @staticmethod
    def F(theta):
        # return 1
        #return theta[0]
        return np.array([[0, 1], [-1 * theta[0], theta[1]]])

    @staticmethod
    def Gamma():
        #return 1
        return np.array([1, 1])

    @staticmethod
    def H():
        #return 1
        return np.array([[1, 0], [0, 1]])

    @staticmethod
    def A():
        return 0
