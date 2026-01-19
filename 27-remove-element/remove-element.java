public class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; 

        
        for (int i = 0; i < nums.length; i++) {
            
            if (nums[i] != val) {
                nums[k] = nums[i]; 
                k++; 
            }
        }

        return k; 
    }

    public void sort(int[] nums, int start, int end) {
        java.util.Arrays.sort(nums, start, end);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {3, 2, 2, 3};
        int val = 3;
        int k = solution.removeElement(nums, val);
        
        
        solution.sort(nums, 0, k);
        
        
        System.out.println("k = " + k);
        System.out.print("Modified array: ");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}
