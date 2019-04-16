class ExperimentModel:

    def __init__(self, Psi=None, F=None, H=None, A=None):
        self.Psi = Psi
        self.H = H
        self.F = F
        self.A = A

    def Psi(self, theta):
        return self.Psi(theta)

    def H(self, theta):
        return self.H(theta)

    def F(self, theta):
        return self.F(theta)

    def A(self, theta):
        return self.A(theta)

    def Gamma(self, theta):
        return self.Gamma(theta)

    def Psi_grad(self, theta):
        return self.Psi_grad(theta)

    def H_grad(self, theta):
        return self.H_grad(theta)

    def F_grad(self, theta):
        return self.F_grad(theta)

    def A_grad(self, theta):
        return self.A_grad(theta)

    def Gamma_grad(self, theta):
        return self.Gamma_grad(theta)

