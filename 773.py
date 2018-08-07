class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        move = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        used = []
        cnt = 0

        s = ''.join([str(c) for row in board for c in row])
        status_list = [(s, s.index('0'))]

        while len(status_list) > 0:

            new_status_list = []

            for status, position in status_list:
                if status == '123450':
                    return cnt
                used.append(status)
                for move_target in move[position]:
                    tmp = list(status)
                    mid = tmp[position]
                    tmp[position] = tmp[move_target]
                    tmp[move_target] = mid
                    tmp = ''.join(tmp)
                    print(tmp)
                    if tmp not in used:
                        new_status_list.append((tmp,tmp.index('0')))
            status_list = new_status_list
            cnt+=1
        return -1

if __name__=="__main__":
    solu = Solution()
    print(solu.slidingPuzzle([[1,2,3],[4,0,5]]))




