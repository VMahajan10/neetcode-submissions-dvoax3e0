class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        for(int num: nums)
        {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }
        for(int i = 0; i < nums.length; i++)
        {
            if(hashmap.get(nums[i]) == 1)
            {
                return nums[i];
            }
        }
        return 0;
    }
}
