public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int k = 1; 

        for (int i = 1; i < nums.length; i++) {
            
            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i]; 
                k++; 
            }
        }

        return k; 
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 2}; 
        Solution solution = new Solution(); 
        int k = solution.removeDuplicates(nums); 

        
        System.out.println("Number of unique elements: " + k);
        System.out.print("Updated array: ");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}
