class Solution {
    public boolean isValid(String s) {

        String str[] =  s.split("");

        ArrayList<String> index = new ArrayList<>();

        for(String s1 : str){

            if(index.size()==0){
                index.add(s1);
            }else{
                if(s1.equals(")") || s1.equals("]") || s1.equals("}") ){
                    
                    if( s1.charAt(0)-index.get(index.size()-1).charAt(0) == 1 || s1.charAt(0) - index.get(index.size()-1).charAt(0) == 2  ){
                        index.remove(index.size()-1);
                    }else{
                        // System.out.print(s1+"==="+index.get(index.size()-1));
                        return false;
                    }   

                }else{
                    index.add(s1);
                }
            }
        }

        if(index.size()!=0){
            return false;
        }
        return true;

    }
}