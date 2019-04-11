class ExperimentConstants:

    def __init__(self,
                 P_t0=None,
                 mu_x=None,
                 theta_0=None,
                 theta_true=None,
                 R=None,
                 Q=None,
                 m=None,
                 N=None,
                 ):
        self.P_t0 = P_t0
        self.mu_x = mu_x
        self.theta_0 = theta_0
        self.theta_true = theta_true
        self.Q = Q
        self.U = [2 for _ in range(N)]
        self.R = R
        self.m = m
        self.N = N
