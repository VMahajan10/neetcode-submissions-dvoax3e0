class Solution {
    public int maxArea(int[] heights) {
      int l = 0;
      int r = heights.length-1; 
      int j = 0;
      while(l < r)
      {
        j = Math.max(j, ((Math.min(heights[l], heights[r]))*Math.abs(r-l)));
        if(heights[l] > heights[r])
        {
            r--;
        }
        else
        {
            l++;
        }
      }
      return j;
    }
}
