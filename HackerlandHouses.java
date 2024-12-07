public class HackerlandHouses {

    static final int MOD = 1000000997;

    public static int countWaysToColorHouses(int n) {
        if (n % 2 != 0) {
            return 0;
        }

        int[][] prev = new int[4][4];
        int[][] curr = new int[4][4];

        for (int x = 1; x <= 3; x++) {
            for (int y = 1; y <= 3; y++) {
                if (x != y) {
                    prev[x][y] = 1;
                }
            }
        }

        for (int i = 2; i <= n / 2; i++) {
            for (int x = 1; x <= 3; x++) {
                for (int y = 1; y <= 3; y++) {
                    curr[x][y] = 0;
                }
            }

            for (int x = 1; x <= 3; x++) {
                for (int y = 1; y <= 3; y++) {
                    if (x == y) continue;
                    for (int p = 1; p <= 3; p++) {
                        for (int q = 1; q <= 3; q++) {
                            if (p != x && q != y) {
                                curr[x][y] = (curr[x][y] + prev[p][q]) % MOD;
                            }
                        }
                    }
                }
            }

            int[][] temp = prev;
            prev = curr;
            curr = temp;
        }

        int result = 0;
        for (int x = 1; x <= 3; x++) {
            for (int y = 1; y <= 3; y++) {
                result = (result + prev[x][y]) % MOD;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int n = 4;
        System.out.println(countWaysToColorHouses(n));
    }
}
