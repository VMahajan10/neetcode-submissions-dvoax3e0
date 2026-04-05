class Solution {

    public String encode(List<String> strs) {
        String b = "";
        for(int i = 0; i < strs.size(); i++)
        {
            b += strs.get(i)  + "-";
        }
        return b; 
    }

    public List<String> decode(String str) {
        ArrayList<String> b = new ArrayList<>();
        String p = "";
        for(char a: str.toCharArray())
        {
            if(a != '-')
            {
                p += a; 
            }
            else
            {
                b.add(p);   
                p = ""; 
            }
        }
        return b;
    }
}
