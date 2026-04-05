class Solution {
    public boolean isPalindrome(String s) {
       
       String b = s.toLowerCase(); 
       int l = 0;
       int r = s.length() - 1; 
       while(l < r)
       {
            if(!(Character.isLetterOrDigit(b.charAt(l))))
            {
                l++;
            }
            else if(!(Character.isLetterOrDigit(b.charAt(r))))
            {
                r--; 
            }
            else
            {
                char a = b.charAt(l);
                char c = b.charAt(r);
                if(a != c)
                {
                    return false;
                }
                l++;
                r--;
            }
            
       }
       return true; 
    }
}
