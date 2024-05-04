import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import logic

game = logic.ant(1000)

fig = plt.figure()
ax = plt.axes()
ax.tick_params(left=False,
                bottom=False,
                labelleft=False,
                labelbottom=False)
im=plt.imshow(np.random.random([1000,1000]), cmap='plasma', vmin=0, vmax=len(game.rules_dic))

def init():
    im.set_data(game.board)
    return [im]

# animation function.  This is called sequentially
def animate(i):
    for i in range(10000):
        game.step()
    im.set_array(game.board)
    return [im]

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1, interval=0, blit=True)

plt.show()