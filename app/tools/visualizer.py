import matplotlib.pyplot as plt

def plot_data(df):
    df.hist(figsize=(10, 8))
    plt.savefig("outputs/plot.png")