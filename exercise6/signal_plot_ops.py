import matplotlib.pyplot as plt

def load_signal_from_txt(path):
    with open(path, mode="r") as file:
        values = []
        for line in file:
            new_line = line.strip()
            nnew_line = float(new_line)
            values.append(nnew_line)
        return values


def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values)/len(values)


def plot_signal(values):
    plt.plot(values)
    plt.show()


if __name__ == "__main__":
    load_signal_from_txt("ekg_signal.txt")
    print(signal_min(load_signal_from_txt("ekg_signal.txt")))
    print(signal_max(load_signal_from_txt("ekg_signal.txt")))
    print(signal_avg(load_signal_from_txt("ekg_signal.txt")))
    plot_signal(load_signal_from_txt("ekg_signal.txt"))









