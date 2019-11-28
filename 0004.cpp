#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double result = 0;
        int lengthNums1 = nums1.size();
        int lengthNums2 = nums2.size();
        int half = (lengthNums1 + lengthNums2) / 2;
        int i = 0;
        int j = 0;
        while(i + j < half){
            if(i < lengthNums1 && j < lengthNums2){
                if(nums1[i] < nums2[j]){
                    i++;
                }else{
                    j++;
                }    
            }else if(i < lengthNums1){
                i++;
            }else{
                j++;
            }
        }

        int remainder = (lengthNums1 + lengthNums2) % 2;
        int flag;
        if(remainder == 0){
            flag = 1;
        }else{
            flag = 0;
        }
        for(int k = 0; k <= flag; k++){
            if(i < 0){
                result += nums2[j];
                break;
            }
            if(j < 0){
                result += nums1[i];
                break;
            }

            if(i < lengthNums1 && j < lengthNums2){
                if(k == 0){
                     if(nums1[i] < nums2[j]){
                         result += nums1[i];
                     }else{
                        result += nums2[j];
                     }
                }else{
                     if(nums1[i] > nums2[j]){
                         result += nums1[i];
                     }else{
                        result += nums2[j];
                     }

                }
            }else if(i < lengthNums1){
                result += nums1[i];
            }else{
                result += nums2[j];
            }
            i -= 1;
            j -= 1;
        }
        
        if(flag){
            result = result / 2;
        }

        return result;
    }
};

int main(){
    vector<int> num1 = {1, 2};
    vector<int> num2 = {3, 4};

    Solution solu;
    cout << solu.findMedianSortedArrays(num1, num2) << endl;
    return 0;
}
