import matplotlib.pyplot as plt

def plot_counts(object_counts, signal_counts):
    object_types = list(object_counts.keys())
    object_values = list(object_counts.values())

    signal_types = []
    signal_subtypes = []
    signal_values = []
    for signal_type, subtypes in signal_counts.items():
        for subtype, count in subtypes.items():
            signal_types.append(signal_type + ': ' + subtype)
            signal_subtypes.append(subtype)
            signal_values.append(count)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    # Plot object counts
    ax1.bar(object_types, object_values, color='skyblue')
    ax1.set_xlabel('Object Types')
    ax1.set_ylabel('Count')
    ax1.set_title('Object Counts')

    # Add number indications on top of the bars
    for i, value in enumerate(object_values):
        ax1.text(i, value, str(value), ha='center', va='bottom')

    # Plot signal counts
    ax2.bar(signal_types, signal_values, color='lightgreen')
    ax2.set_xticks(range(len(signal_values)))
    ax2.set_xticklabels(signal_subtypes, rotation=90)
    ax2.set_xlabel('Signal Subtypes')
    ax2.set_ylabel('Count')
    ax2.set_title('Signal Counts')

    # Add number indications on top of the bars
    for i, value in enumerate(signal_values):
        ax2.text(i, value, str(value), ha='center', va='bottom')

    fig.tight_layout()
    plt.show()
