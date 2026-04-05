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
       int i = 0;
       int j = 0;
       List<String> res = new ArrayList<>();
       String k = "";
       while(i < str.length())
       {
            
            if(str.charAt(j) != '#')
            {
                k += str.charAt(j);
                i++;
                j++;
            }
            else
            {
                int l = Integer.parseInt(k);
                i = i + 1; 
                j = i + l;
                String f = str.substring(i, j);
                res.add(f);
                k = "";
                i = j;
            }
       }
       return res;
    }
      
 }
       
