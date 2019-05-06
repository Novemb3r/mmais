class ExperimentModel:

    def __init__(self, Psi=None, F=None, H=None, A=None, Gamma=None, Psi_grad=None, H_grad=None, F_grad=None, b=None,
                 A_grad=None, Gamma_grad=None, mu_x=None, mu_x_grad=None, P_tk_tk=None, P_tk_tk_grad=None, Q=None,
                 Q_grad=None, R=None, R_grad=None, b_grad=None):
        self.Psi = Psi
        self.H = H
        self.F = F
        self.A = A
        self.Q = Q
        self.Q_grad_mas = Q_grad
        self.R = R
        self.b = b
        self.R_grad_mas = R_grad
        self.Gamma = Gamma
        self.Psi_grad_mas = Psi_grad
        self.H_grad_mas = H_grad
        self.F_grad_mas = F_grad
        self.A_grad_mas = A_grad
        self.Gamma_grad_mas = Gamma_grad
        self.mu_x = mu_x
        self.mu_x_grad_mas = mu_x_grad
        self.P_tk_tk = P_tk_tk
        self.P_tk_tk_grad_mas = P_tk_tk_grad
        self.b_grad_mas = b_grad

    def Psi(self, theta):
        return self.Psi(theta)

    def H(self, theta):
        return self.H(theta)

    def F(self, theta):
        return self.F(theta)

    def A(self, theta):
        return self.A(theta)

    def Q(self, theta):
        return self.Q(theta)

    def R(self, theta):
        return self.R(theta)

    def b(self, theta):
        return self.b(theta)

    def Gamma(self, theta):
        return self.Gamma(theta)

    def mu_x(self, theta):
        return self.mu_x(theta)

    def P_tk_tk(self, theta):
        return self.P_tk_tk(theta)

    def Psi_grad(self, theta, ind):
        return self.Psi_grad_mas[ind](theta)

    def H_grad(self, theta, ind):
        return self.H_grad_mas[ind](theta)

    def F_grad(self, theta, ind):
        return self.F_grad_mas[ind](theta)

    def A_grad(self, theta, ind):
        return self.A_grad_mas[ind](theta)

    def Gamma_grad(self, theta, ind):
        return self.Gamma_grad_mas[ind](theta)

    def mu_x_grad(self, theta, ind):
        return self.mu_x_grad_mas[ind](theta)

    def P_tk_tk_grad(self, theta, ind):
        return self.P_tk_tk_grad_mas[ind](theta)

    def Q_grad(self, theta, ind):
        return self.Q_grad_mas[ind](theta)

    def R_grad(self, theta, ind):
        return self.R_grad_mas[ind](theta)

    def b_grad(self, theta, ind):
        return self.b_grad_mas[ind](theta)
