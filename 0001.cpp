#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(int i = 0; i < nums.size(); i++){
            int expected = target - nums[i];
            for(int j = i + 1; j < nums.size(); j++){
                if(nums[j] == expected){
                    result.push_back(i);
                    result.push_back(j);
                }
            }
        }
        return result;
    }
};

int main(){
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = solution.twoSum(nums, target);
    cout << result[0] << endl;
    return 0;
}
