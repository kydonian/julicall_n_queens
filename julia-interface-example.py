import time

if __name__ == "__main__":
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