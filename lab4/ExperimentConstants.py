class ExperimentConstants:

    def __init__(self,
                 P_t0=None,
                 theta_0=None,
                 theta_true=None,
                 R=None,
                 Q=None,
                 m=None,
                 N=None,
                 a=None,
                 s=None,
                 ):
        self.P_t0 = P_t0
        self.theta_0 = theta_0
        self.theta_true = theta_true
        self.Q = Q
        self.U = [2 for _ in range(N)]
        self.R = R
        self.m = m  # количество параметров
        self.N = N
        self.a = a
        self.s = s

