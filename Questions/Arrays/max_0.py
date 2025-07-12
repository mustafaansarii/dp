def calculateMaxZeroes(n, sequenceData):
    zero_count = 0

    while True:
        # Find the longest prefix without any zero
        prefix_end = 0
        while prefix_end < n and sequenceData[prefix_end] != 0:
            prefix_end += 1

        if prefix_end == 0:
            # No valid prefix found
            break

        # Find the minimum value in this prefix
        min_val = min(sequenceData[:prefix_end])

        # Subtract min_val from all elements in the prefix
        for i in range(prefix_end):
            sequenceData[i] -= min_val
            if sequenceData[i] == 0:
                zero_count += 1

    return zero_count
