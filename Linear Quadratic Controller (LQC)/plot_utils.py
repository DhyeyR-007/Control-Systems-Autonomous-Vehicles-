import matplotlib.pyplot as plt

def plot_traj(x_log, u_log, preview):
    plt.figure(figsize=(5, 3))

    plt.plot(x_log[:, 0], '--', label = "$x_1$")
    plt.plot(x_log[:, 1], '--', label = "$x_2$")
    plt.plot(x_log[:, 2], '--', label = "$x_3$")

    plt.title('Trajectory - preview = %d'% preview)
    plt.legend()
    plt.grid()
    plt.show()

def plot_input(x_log, u_log, preview):
    plt.figure(figsize=(5, 3))

    plt.plot(u_log[:, 0], '--', label = "$u_1$")
    plt.plot(u_log[:, 1], '--', label = "$u_2$")

    plt.title('Control Input - preview = %d'% preview)
    plt.legend()
    plt.grid()
    plt.show()


