class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        int p = 1;
        int max = 0;
        if(nums.length == 0)
        {
            return 0;
        }
        for(int i = 1; i < nums.length; i++)
        {
            if(nums[i] - 1 == nums[i-1])
            {
                p++;
            }
            else if(nums[i] == nums[i-1])
            {
                continue;
            }
            else
            {
                max = Math.max(p , max);
                p = 1;
            }
            
        }
        max = Math.max(p, max);
        return max;
    }
}
