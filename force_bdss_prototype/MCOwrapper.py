import numpy as np
from .objectives import Objectives
from .constraints import Constraints
from .initializer import Initializer
from .MCOsolver import MCOsolver
from .pareto_process_db import Pareto_process_db


class MCOwrapper:
    # default constructor
    def __init__(self, R, C):
        # mco setup: trasform to impl. data structures.
        self.R = R
        self.C = C
        self.obj = Objectives(self.R, self.C)
        self.constraints = Constraints(self.R)
        self.ini = Initializer()
        constr = self.constraints.get_linear_constraints()
        obj_f = lambda y: self.obj.obj_calc(y)[0]
        obj_jac = lambda y: self.obj.obj_calc(y)[1]
        X0 = self.ini.get_init_data_kin_model(self.R)
        # X0 structure:
        # 0: A concentration
        # 1: 0.5. B concentration
        # 2: 0. P concentration
        # 3: 0. S concentration
        # 4: 0.505. C concentration
        # 5: 335. Temperature
        # 6: 360. Reaction time
        y0 = self.obj.x_to_y(X0)
        self.mcosolver = MCOsolver(y0, constr, obj_f, obj_jac)

    def solve(self):
        results = self.mcosolver.solve()
        res = np.empty((results.shape[0], results.shape[1] + 3))
        for i in range(results.shape[0]):
            y = results[i, :]
            O, _ = self.obj.obj_calc(y)
            res[i, :results.shape[1]] = results[i, :]
            res[i, results.shape[1]:] = O
        self.pp_db = Pareto_process_db(res)
        self.pp_db.write_csv()
        return res
