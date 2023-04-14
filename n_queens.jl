# Solve N-Queens, source largely from
# https://github.com/jump-dev/JuMP.jl/blob/master/docs/src/tutorials/linear/n-queens.jl
# usage: julia --project n_queens.jl NUM_QUEENS

using JuMP
import HiGHS
import LinearAlgebra

function solve_n_queens(N::Int64)
    model = Model(HiGHS.Optimizer)
    set_silent(model)
    @variable(model, x[1:N, 1:N], Bin);
    for i in 1:N
        @constraint(model, sum(x[i, :]) == 1)
        @constraint(model, sum(x[:, i]) == 1)
    end
    for i in -(N-1):(N-1)
        @constraint(model, sum(LinearAlgebra.diag(x, i)) <= 1)
        @constraint(model, sum(LinearAlgebra.diag(reverse(x; dims = 1), i)) <= 1)
    end
    optimize!(model)
    return round.(Int, value.(x))
end

num_queens= ARGS[1]
solution = solve_n_queens(num_queens)
println(solution)