class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] p = new int[2];
        Map<Integer, Integer> hashmap = new HashMap<>(); 
        for(int i = 0; i < nums.length; i++)
        {
            if(hashmap.containsKey(target - nums[i]))
            {
                p[0] = hashmap.get(target - nums[i]);
                p[1] = i;
                return p; 
            }
            hashmap.put(nums[i], i);
        }
        return p;
    }
}
