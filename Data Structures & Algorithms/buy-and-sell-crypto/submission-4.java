class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1; 
        int priceProfit = 0;
        while(r < prices.length)
        {
            if(prices[l] >= prices[r])
            {
                l = r;
            }
            //r++;
            else
            {
                
                priceProfit = Math.max(priceProfit, prices[r] - prices[l]);
            }
            r++;
        }
        return priceProfit;


    }
}
