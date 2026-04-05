class Solution {
    public boolean isPalindrome(String s) {
       int n = 0;
       int e = s.length() - 1;

       while(n < e)
       {
          while(n < e && !Character.isLetterOrDigit(s.charAt(n)))
          {
            n++;
          }
          while(e > n && !Character.isLetterOrDigit(s.charAt(e)))
          {
            e--;
          }
          char k = Character.toLowerCase(s.charAt(n));
          char m = Character.toLowerCase(s.charAt(e));
          if(k != m)
          {
            return false;
          }
          n++;
          e--;
       }
       return true;
    }
}
