class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> hashmap = new HashMap<>();
        hashmap.put(')', '(');
        hashmap.put('}', '{');
        hashmap.put(']', '[');
        Stack<Character> stack = new Stack<>();

        for(char c: s.toCharArray())
        {
            if(stack.isEmpty())
            {
                
                stack.push(c);
                
            }
            else
            {
                if(c == '[' || c == '{' || c == '[')
                {
                    stack.push(c);
                }
                else if(c == ']' || c == '}' || c == ')')
                {
                    if(stack.peek() == hashmap.get(c))
                    {
                        stack.pop();
                    }
                    else
                    {
                        stack.push(c);
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}
