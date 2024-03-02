class LowPassFilter:
    def __init__(self, alpha):
        self.alpha = alpha
        self.filtered_value = None

    def apply(self, new_value):
        if self.filtered_value is None:
            self.filtered_value = new_value
        else:
            self.filtered_value = self.alpha * new_value + (1 - self.alpha) * self.filtered_value
        return self.filtered_value

# Example usage
if __name__ == "__main__":
    # Define the filter parameters
    alpha = 0.1  # Smoothing factor (0 < alpha < 1)

    # Initialize the low-pass filter
    low_pass_filter = LowPassFilter(alpha)

    # Simulate incoming data (replace this with actual data acquisition)
    incoming_data = [10, 20, 15, 25, 30, 20, 25, 35]

    # Apply the filter to each data point
    filtered_data = []
    for data_point in incoming_data:
        filtered_value = low_pass_filter.apply(data_point)
        filtered_data.append(filtered_value)

    # Print the filtered data
    print("Filtered Data:", filtered_data)
