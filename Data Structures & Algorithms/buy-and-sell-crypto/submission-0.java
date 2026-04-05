class Solution {
    public int maxProfit(int[] prices) {
        Stack<Integer> stack = new Stack<>();
        int max = 0;
        for(int price: prices)
        {
            if(stack.isEmpty())
            {
                stack.push(price);
            }
            else
            {
                if(price < stack.peek())
                {
                    stack.pop();
                    stack.push(price);
                }
                else if(price > stack.peek())
                {
                    int b = price - stack.peek();
                    max = Math.max(max, b);
                }
            }
        }
        return max;
    }
}
