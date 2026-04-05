class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> hashset = new HashSet<>();
        int count = 0; 
        int maxCount = 0; 
        for(int num: nums)
        {
            hashset.add(num);
        }
        for(int i = 0; i < nums.length; i++)
        {
            if(!hashset.contains(nums[i] - 1))
            {
                count = 1; 
                int k = 1;
                while(hashset.contains(nums[i] + k))
                {
                    count++;
                    k++;
                }
                maxCount = Math.max(count, maxCount);

            }
        }
        return maxCount; 
    }
}
