def main():
    for _  in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Try all possible permutations of size N
        found = False
        for perm in range(1, n+1):
            # Check if we can construct array B such that A[i] + B[i] = perm
            valid = True
            for i in range(n):
                if arr[i] > perm:
                    valid = False
                    break
            if valid:
                found = True
                break
                
        print("YES" if found else "NO")