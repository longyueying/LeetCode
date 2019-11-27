#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length()== 0){
            return 0;
        }
        int result = 1;
        int currentLength = 1;
        int stringLength = s.length();
        int begin = 0;
        for(int i = 1; i < stringLength; i++){
            int j;
            for(j = begin; j < i; j++){
                if(s[j] == s[i]){
                    break;                
                }
            }
            if(i == j){
                currentLength += 1;
            }else{
               begin = j + 1;
               if(currentLength > result){
                   result = currentLength;
               }
               currentLength = i - begin + 1;
            }
        }
        if(currentLength > result){
            result = currentLength;
        }        
        return result;
    }
};

int main(){
    Solution solution;
    int length = solution.lengthOfLongestSubstring("dvdf");
    cout << length << endl;
    return 0;
}
