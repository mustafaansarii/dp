import java.util.Arrays;

public class coin_change {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Arrays.fill(dp,amount+1);
        dp[0] = 0;
        for(int i=1;i<=amount;i++){
            for(int j=0;j<coins.length;j++){
                if(coins[j]<=i){
                    dp[i] = Math.min(dp[i],dp[i-coins[j]]+1);
                }
            }
        }
        return dp[amount]==amount+1?-1:dp[amount];
    }
    public static void main(String[] args) {
        coin_change cc = new coin_change();
        int[] coins = {1,2,5};
        int amount = 11;
        System.out.println(cc.coinChange(coins,amount));
    }
}
