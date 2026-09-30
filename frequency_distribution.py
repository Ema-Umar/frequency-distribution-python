import math


def frequency_distribution(data, number_of_classes=None):
    # Basic calculations
    minimum = min(data)
    maximum = max(data)
    data_range = maximum - minimum

    # If number of classes is not provided,
    # use Sturges' formula
    if number_of_classes is None:
        number_of_classes = math.ceil(
            1 + 3.322 * math.log10(len(data))
        )

    # Calculate class width
    class_width = math.ceil(data_range / number_of_classes)

    # Create frequency table
    frequency = [0] * number_of_classes

    intervals = []

    lower = minimum

    for i in range(number_of_classes):
        upper = lower + class_width - 1

        intervals.append((lower, upper))

        # Count values in this interval
        for value in data:
            if lower <= value <= upper:
                frequency[i] += 1

        lower = upper + 1

    # Calculate cumulative frequency
    cumulative_frequency = []
    total = 0

    for freq in frequency:
        total += freq
        cumulative_frequency.append(total)

    # Display results
    print("\n========== FREQUENCY DISTRIBUTION ==========")

    print(f"Number of observations : {len(data)}")
    print(f"Minimum value          : {minimum}")
    print(f"Maximum value          : {maximum}")
    print(f"Range                  : {data_range}")
    print(f"Number of classes      : {number_of_classes}")
    print(f"Class width            : {class_width}")

    print("\nFrequency Distribution Table")
    print("-" * 55)
    print(f"{'Class Interval':<20}{'Frequency':<15}{'Cumulative Freq.':<20}")
    print("-" * 55)

    for i in range(number_of_classes):
        lower, upper = intervals[i]

        print(
            f"{str(lower) + ' - ' + str(upper):<20}"
            f"{frequency[i]:<15}"
            f"{cumulative_frequency[i]:<20}"
        )

    print("-" * 55)
    print(
        f"{'Total':<20}"
        f"{sum(frequency):<15}"
        f"{cumulative_frequency[-1]:<20}"
    )


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

print("FREQUENCY DISTRIBUTION PROGRAM")

data_input = input(
    "\nEnter the data values separated by spaces: "
)

data = list(map(float, data_input.split()))

# Convert whole-number floats to integers
data = [
    int(x) if x.is_integer() else x
    for x in data
]

frequency_distribution(data)