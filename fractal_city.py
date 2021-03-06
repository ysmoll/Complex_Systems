import matplotlib.pyplot as plt
import numpy as np
import os
from dla_model_final import get_fractal_dim
from networks import get_city_network, get_fractal_from_network

def network_frac_dim(city = "Berlin", country = "Germany"):
    """Creates a network of chosen city and country and returns the grid-version and fractal dimension"""

    # get the city network and convert it to a grid
    city_network = get_city_network(f'{city}, {country}')
    grid_city = get_fractal_from_network(city_network, bins=200, threshold=0)

    # reduce and save the graph so we can use it for fractal dimension calculation
    grid_reduced = grid_city[~np.all(grid_city == 0, axis=1)]
    grid_reduced = grid_reduced[:, ~np.all(grid_reduced == 0, axis=0)]
    fig = plt.figure()
    ax = fig.add_subplot()
    cax = ax.matshow(grid_reduced, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.axis('off')
    fig.subplots_adjust(bottom = 0)
    fig.subplots_adjust(top = 1)
    fig.subplots_adjust(right = 1)
    fig.subplots_adjust(left = 0)
    plt.savefig('interim_fractal.png', dpi=1000)
    plt.close()

    # get the fractal dimension through box counting
    frac_dim, std = get_fractal_dim('interim_fractal')
    os.remove('interim_fractal.png')
    print(f'Found fractal dimension of {frac_dim} with standard deviation {std}.')

if __name__ == '__main__':

    # choose city and country
    city = 'Berlin'
    country = 'Germany'

    # print the fractal dimension
    network_frac_dim(city, country)