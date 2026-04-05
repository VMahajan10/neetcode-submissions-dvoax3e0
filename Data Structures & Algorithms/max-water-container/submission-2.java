class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length - 1; 
        int max = 0; 
        while(l < r)
        {
            int j = Math.min(heights[l], heights[r]);
            int relMax = (r - l)*(j);
            max = Math.max(relMax, max);
            if(j == heights[l])
            {
                l++;
            }
            else if(j == heights[r])
            {
                r--;
            }
        }
        return max; 
    }
}
