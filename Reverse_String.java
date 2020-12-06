//Time complexity : \mathcal{O}(N)O(N) to swap N/2N/2 element.

//Space complexity : \mathcal{O}(1)O(1), it's a constant space solution.

class Solution {
    public void reverseString(char[] s) {
        char temp;
        int size = s.length;
        for(int i=0; i < size/2; i++){
            temp = s[i];
            s[i] = s[size - 1 - i];
            s[size - 1 - i] = temp;
        }
    }
}
