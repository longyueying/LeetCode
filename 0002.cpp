#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(0);
        ListNode *cur = head;
        int carry = 0;
        int sum = 0;
        int val1 = 0;
        int val2 = 0;
        while(l1 || l2 || carry){
            val1 = 0;
            val2 = 0;
            if(l1){
                val1 = l1->val;
                l1 = l1->next;
            } 
            if(l2){
                val2 = l2->val;
                l2 = l2->next;
            }
            sum = val1 + val2 + carry;
            carry = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
        }
        return head->next;
    }
};

int main(){
    return 0;
}
