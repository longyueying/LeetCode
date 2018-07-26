class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        self.res = False
        waiting_room = [i for i in range(len(rooms))]

        def solver(rooms, waiting_room,index):
            new_waiting_room = waiting_room[:]
            new_waiting_room.remove(index)
            if len(new_waiting_room)==0:
                self.res=True
            if self.res == True:
                return
            for i in new_waiting_room:
                if i in rooms[index]:
                    solver(rooms, new_waiting_room, i)
        solver(rooms,waiting_room, 0)
        return self.res

if __name__=="__main__":
    solu = Solution()
    print(solu.canVisitAllRooms([[2,3],[],[2],[1,3,1]]))
