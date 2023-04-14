import time

# from multiprocessing import Pool
    
# def _setup():
#   from juliacall import Main as jl
#   jl.include("n_queens.jl")
#   jl.seval("using .NumQueensModule")

# def _call_script_internal(num_queens):
#   from juliacall import Main as jl
#   solution = jl.NumQueensModule.solve_n_queens(num_queens)
#   print(solution)

# class JuliaInterface:
#   def __init__(self):
#     """Create the single special thread for all Julia operations, and instatiate the Julia engine."""
#     self._process_pool = Pool(1)
#     self._process_pool.apply(_setup)

#   def call_script(self, num_queens: int):
#     self._process_pool.apply(_call_script_internal, (num_queens,))


if __name__ == "__main__":
#   interface = JuliaInterface()
#   interface.call_script(8)

  from juliacall import Main as jl
  jl.include("n_queens.jl")
  jl.seval("using .NumQueensModule")
  for i in range (3, 20):
    t0 = time.time()
    solution = jl.NumQueensModule.solve_n_queens(i+1)
    dt = time.time() - t0
    print("solve time", dt)
    t0 = time.time()
    sol_numpy = solution.to_numpy()
    dt = time.time() - t0
    print("conversion time", dt)
    print(i, sol_numpy)