class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> a = new HashMap<>();
        Map<Character, Integer> b = new HashMap<>();

        for(char k: s.toCharArray())
        {
            a.put(k, a.getOrDefault(k, 0) + 1);
        }
        for(char m: t.toCharArray())
        {
            b.put(m, b.getOrDefault(m, 0) + 1);
        }

        return a.equals(b);
    }
}
