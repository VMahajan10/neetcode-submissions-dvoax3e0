class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str: strs)
        {
            sb.append(str.length()).append('#').append(str);
        }
        return sb.toString(); 
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0; 
        int j = 0;
        while(i < str.length())
        {
            String l = "";
            while(str.charAt(i) != '#')
            {
                l += str.substring(i, i+1);
                i++;
            }
            int m = Integer.parseInt(l);
            j = i + m;
            i = i + 1;
            res.add(str.substring(i, j+1));
            i = j + 1;
            

        }
        return res;
    }
}
