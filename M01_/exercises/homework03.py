# ### HOMEWORK 3 ###
import numpy as np
import matplotlib.pyplot as plt

# ### PART i.
def get_fibonacci(n):

    if n <= 0:
        print("n have to be a positive integer !")
        return np.array([])

    elif n == 1:
        return np.array([1])
    elif n == 2:
        return np.array([1, 1])

    # Base case
    f = [1, 1]

    # Sarting from index 2 because index 0 and 1 are alredy defined
    for i in range(2, n):
        nextFib = f[i-1] + f[i-2]
        f.append(nextFib)

    # dtype=object to avoid overflow
    return np.array(f, dtype=object)

if __name__ == "__main__":
    n = 100
    n_fib = get_fibonacci(n)
    print(f"the {n}-th element of the fibonacci sequence is : {n_fib[-1]}")

    # ### PART ii.
    # r_i = f_i+1 / f_i,    i = 1, 2, ..., 99.
    # [1:]  every element from index 1 to n
    # [:-1] every element form index 1 to n-1
    r = n_fib[1:] / n_fib[:-1]

    plt.plot(range(1, n), r)

    plt.title('Homework 3: part ii.')
    plt.xlabel("Index (i)")
    plt.ylabel("Ratio (r_i)")
    plt.grid(True)
    plt.show()
