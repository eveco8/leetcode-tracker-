/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let majority = nums.length / 2
    let freq = {}
    for (let i = 0; i < nums.length; i++) {
    let num = nums[i]
        if (freq[num]) {
            freq[num]++
        } else {
            freq[num] = 1
        }
    }
    for (let num in freq) {
    if (freq[num] > majority) { 
        return Number(num)
    }
    }
};
