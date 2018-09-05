class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic_1 = {}
        dic_2 = {}
        for i, restaurant in enumerate(list1):
            dic_1[restaurant] = i
        for i, restaurant in enumerate(list2):
            if restaurant in dic_1.keys():
                dic_2[restaurant] = i+dic_1[restaurant]
        res = []
        m = min(dic_2.values())
        for restaurant in dic_2:
            if dic_2[restaurant] == m:
                res.append(restaurant)
        return res