def interpolate(x, y, x_test):
    # Zip all into dic
    kv = dict(zip(x, y))

    # I assume it not been sorted, then sort it!
    sorted_keys = sorted(kv.keys())

    for key_index in range(len(sorted_keys) - 1):
        # loop in x value to get proper range
        current_x = sorted_keys[key_index]
        next_x = sorted_keys[key_index + 1]

        current_y = kv[sorted_keys[key_index]]
        next_y = kv[sorted_keys[key_index + 1]]

        if current_x <= x_test <= next_x:
            # As we had range, calculate the change rate.
            # Apply the change rate to difference_y
            change_rate = (x_test - current_x) / (next_x - current_x)
            res = current_y + change_rate * (next_y - current_y)
            return res
