# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        table = {e.id : e for e in employees }
        return self.get_importance(table,id)
    def get_importance(self, table, id):
        sum = table[id].importance
        for sub in table[id].subordinates:
            sum += self.get_importance(table, sub)
        return sum

if __name__=="__main__":
    solu = Solution()
    print(solu.getImportance())