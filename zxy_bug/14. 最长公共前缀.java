class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        String k ="" ;

        for(int i=0;i<strs[0].length();i++){
            char c = strs[0].charAt(i);
            for(int j=1;j<strs.length;j++){
                // 当字符串长度超出后面字符串长度或者后面一次匹配字符串对应的i位置的字符不一样时结束函数
                if(i==strs[j].length() || strs[j].charAt(i)!=c){
                    k=strs[0].substring(0,i);
                    return k;
                }
            }
        }
        // 当内层循环不执行就代表只有一个字符串，如果执行内层循环就会直接在内层循环中结束函数
        k = strs[0];
        return k;
    }
}