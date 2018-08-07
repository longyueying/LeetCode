class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def swap(row, left, right):
            tmp = row[left]
            row[left] = row[right]
            row[right] = tmp

        pos = [0]*len(row)
        for i,num in enumerate(row):
            pos[num] = i

        i = 0
        count = 0
        while i < len(row):
            if row[i]%2==0:
                expect = row[i]+1
            else:
                expect = row[i]-1

            if row[i+1] != expect:
                tmp = row[i+1]
                target_pos = pos[expect]
                pos[tmp] = target_pos
                swap(row, i+1, pos[expect])
                count+=1
            i+=2
        return count

