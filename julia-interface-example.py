from multiprocessing import Pool
    
def _setup():
  from juliacall import Main as jl
  jl.include("install_script.jl")

def _call_script_internal(num_queens):
  from juliacall import Main as jl

  jl.seval(f"ARGS=[{num_queens}]")
  jl.include("n_queens.jl")

class JuliaInterface:
  def __init__(self):
    """Create the single special thread for all Julia operations, and instatiate the Julia engine."""
    self._process_pool = Pool(1)
    self._process_pool.apply(_setup)

  def call_script(self, num_queens: int):
    self._process_pool.apply(_call_script_internal, (num_queens,))


if __name__ == "__main__":
  interface = JuliaInterface()
  interface.call_script(8)