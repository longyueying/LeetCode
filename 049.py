import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for str in strs:
            temp = list(str)
            sorted(temp)

            k = ''.join(sorted(temp))
            res[k].append(str)

        return list(res.values())


if __name__ == '__main__':
    solu = Solution()
    print(solu.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))