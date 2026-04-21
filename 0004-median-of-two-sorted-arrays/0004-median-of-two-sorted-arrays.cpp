class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1); // Swap arrays if needed
        }
        int m = nums1.size(); // Length of nums1
        int n = nums2.size(); // Length of nums2
        int left = 0, right = m; // Binary search range

        while (left <= right) { // Binary search loop
            int i = (left + right) / 2; // Partition nums1
            int j = (m + n + 1) / 2 - i; // Partition nums2

            int maxLeftA = (i == 0) ? INT_MIN : nums1[i - 1]; // Left max of nums1
            int minRightA = (i == m) ? INT_MAX : nums1[i]; // Right min of nums1
            int maxLeftB = (j == 0) ? INT_MIN : nums2[j - 1]; // Left max of nums2
            int minRightB = (j == n) ? INT_MAX : nums2[j]; // Right min of nums2

            if (maxLeftA <= minRightB && maxLeftB <= minRightA) { // Correct partition
                if ((m + n) % 2 == 0) { // Even total length
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0; // Median is average
                } else { // Odd total length
                    return max(maxLeftA, maxLeftB); // Median is max of left parts
                }
            } else if (maxLeftA > minRightB) { // Too far right in nums1
                right = i - 1; // Move left
            } else { // Too far left in nums1
                left = i + 1; // Move right
            }
        }
        return 0.0; // Should not reach here
    }
};