class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> l1=new ArrayList<>();
        List<Integer> l2=new ArrayList<>();
        help(0,nums,l1,l2);
        return l1;
        
    }
    void help(int i,int a[],List<List<Integer>> l1,List<Integer> l2){
        if(i==a.length){
            l1.add(new ArrayList<>(l2));
            return;    
        }
        l2.add(a[i]);
        help(i+1,a,l1,l2);
        l2.remove(Integer.valueOf(a[i]));
        help(i+1,a,l1,l2);
    }
}
