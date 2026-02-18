import math
import statsmodels
from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()

effect_size = float(input('Input the effect size: '))
alpha = float(input('Input the alpha value: '))
power = float(input('Input the power: '))
ratio = float(input('Input the sample size ratio: '))

sample_size = analysis.solve_power(
    effect_size = effect_size, 
    alpha = alpha, 
    power = power, 
    ratio = ratio)

print(f'Minimum sample size needed for experiment: {math.ceil(sample_size)}')