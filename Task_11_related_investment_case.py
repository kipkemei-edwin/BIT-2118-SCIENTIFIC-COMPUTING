from scipy.optimize import root_scalar

# Alternative investment project: initial cost followed by four annual returns
cash_flows = [-15000, 5000, 5500, 6000, 4000]

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows) if t > 0
    )

solution = root_scalar(
    npv, fprime=d_npv, x0=0.10,
    method="newton", xtol=1e-12
)

print(f"Estimated project IRR: {solution.root:.6%}")
print(f"NPV at estimated IRR: {npv(solution.root):.8f}")
