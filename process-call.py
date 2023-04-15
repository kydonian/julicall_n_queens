from multiprocessing import Pool
    
def _setup():
  from juliacall import Main as jl
  jl.include("n_queens.jl")
  jl.seval("using .NumQueensModule")

def _call_script_internal(num_queens):
  from juliacall import Main as jl
  solution = jl.NumQueensModule.solve_n_queens(num_queens)
  print(num_queens, solution)

class JuliaInterface:
  def __init__(self):
    """Create the single special thread for all Julia operations, and instatiate the Julia engine."""
    self._process_pool = Pool(1)
    self._process_pool.apply(_setup)

  def call_script(self, num_queens: int):
    self._process_pool.apply(_call_script_internal, (num_queens,))


if __name__ == "__main__":
  interface = JuliaInterface()

  if True:
    # Failure version A
    interface.call_script(8)
  else:
    # Failure version B
    for i in range(3,10):
      interface.call_script(i)
      print(i)
  print("exits")