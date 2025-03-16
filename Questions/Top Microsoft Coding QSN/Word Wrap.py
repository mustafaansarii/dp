def Word_Wrap(words, m, n):

    cost = [[0 for x in range(n)] for y in range(n)]

    # Calculate the cost of each word
    for i in range(n):
        cost[i][i] = m - len(words[i])
        for j in range(i + 1, n):
            cost[i][j] = cost[i][j - 1] - len(words[j]) - 1

    # Create a 2D list to store the minimum cost of each word
    min_cost = [0 for x in range(n)]
    result = [0 for x in range(n)]

    # Calculate the minimum cost of each word
    for i in range(n - 1, -1, -1):
        min_cost[i] = cost[i][n - 1]
        result[i] = n
        for j in range(n - 1, i, -1):
            if cost[i][j - 1] == -1:
                continue
            if min_cost[i] > min_cost[j] + cost[i][j - 1]:
                min_cost[i] = min_cost[j] + cost[i][j - 1]
                result[i] = j

    # Create a list to store the justified text
    res = []
    i = 0
    j = result[0]

    # Construct the justified text
    while j < n:
        j = result[i]
        each_line = ""
        for k in range(i, j):
            each_line += words[k] + " "
        each_line += words[j]
        each_line = each_line.strip()
        res.append(each_line)
        i = j
        j = result[j]
    return res


if __name__ == "__main__":
    # Example test case
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    m = 16  # Maximum characters per line
    n = len(words)  # Number of words
    print(Word_Wrap(words, m, n))

    # Additional test case
    words2 = ["What","must","be","acknowledgment","shall","be"]
    m2 = 16
    n2 = len(words2)
    print(Word_Wrap(words2, m2, n2))