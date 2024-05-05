import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import logic
import keyboard
import time 



def generate_binary_lists(n):
    binary_lists = []
    for i in range(((2**n)//2)//2):
        binary = bin(i)[2:].zfill(n)
        binary_lists.append([int(bit) for bit in binary])
    return binary_lists



#initialisation 
games = []
n = 12
for i in generate_binary_lists(n):
    game = logic.ant(150, i)
    games.append(game)

fig = plt.figure()
ax = plt.axes()
ax.tick_params(left=False,
                bottom=False,
                labelleft=False,
                labelbottom=False)
im=plt.imshow(np.random.random([1000,1000]), cmap='Accent', vmin=0, vmax=len(game.rules_dic))
visualed =0
def init():
    im.set_data(games[visualed].board)
    return [im]

start_a =  time.time()
start_d =  time.time()
color = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
color_i = 0
start_cp= time.time()
start_co = time.time()
# animation function.  This is called sequentially
def animate(i):
    global start_a
    global start_d 
    global color_i
    global color
    global start_cp 
    global start_co
    im.set_cmap(color[color_i])
    global visualed
    for i in range(1000):
        games[visualed].step()
    im.set_array(games[visualed].board)
    if keyboard.is_pressed('a') and time.time()-start_a > 2:
        visualed = (visualed + 1) % len(games)
        start_a = time.time()
    if keyboard.is_pressed('d') and time.time()-start_d > 2:
        visualed = (visualed - 1) % len(games)
        start_d = time.time()
    if keyboard.is_pressed('p') and time.time()-start_cp > 0.2:
        color_i = (color_i + 1) % len(color)
        start_cp = time.time()
    if keyboard.is_pressed('o') and time.time()-start_co > 2:
        color_i = (color_i - 1) % len(color)
        start_co = time.time()
    if keyboard.is_pressed('b'):
        print(games[visualed].sequence)
    if keyboard.is_pressed('e'):
        games[visualed].board = np.zeros([350,350])
        games[visualed].ant_pos = np.array([350//2, 350//2])
    return [im]

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1, interval=0, blit=True)

plt.show()