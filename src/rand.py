"""Module providing a function to generate random array values based on a given array of n size."""
import subprocess


def random_array(arr):
    """Function generating a random array."""
    shuffled_num = None
    for element in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True,check=True)
        arr[element[0]] = int(shuffled_num.stdout)
    return arr
