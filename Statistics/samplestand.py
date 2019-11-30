from Calculator.subtraction import subtraction

from Calculator.division import division

from Statistics.sampledata import sampledata

from Calculator.squareroot import squareroot

from Calculator.square import square

from Statistics.mean import mean

from Calculator.addition import addition





def samplestand(data, sample_size):

    dev = 0

    sample = sampledata(data, sample_size)

    sample_values = len(sample)

    x_bar = mean()

    x = sample_values

    n = subtraction(sample_values, 1)

    for dev in sample:

        dev = subtraction(x, x_bar)

        square_x_bar = square(dev)

        add = addition(square_x_bar, square_x_bar)

        result = division(add, n)

    return squareroot(result)