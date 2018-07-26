class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        length = len(stickers)
        mp = [[0]*26 for i in range(length)]
        dp = {}
        dp[''] = 0
        for i in range(length):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] +=1
        self.min_anw = len(target)

        def solver(dp, mp, target, cut):
            if cut > self.min_anw:
                return -1
            if target in dp:
                if cut + dp[target] < self.min_anw:
                    self.min_anw=cut+dp[target]
                return dp[target]

            anw = -1

            target_list = [0] * 26
            for c in target:
                target_list[ord(c) - ord('a')] += 1
            for i in range(len(mp)):
                if mp[i][ord(target[0])- ord('a')] == 0:
                    continue
                s = ''
                for j in range(len(target_list)):
                    if target_list[j] > mp[i][j]:
                        s+=(chr(ord('a')+j)*(target_list[j]-mp[i][j]))

                if cut+1+len(s) < self.min_anw:
                    self.min_anw = cut+1+len(s)

                tmp = solver(dp, mp, s, cut+1)
                if tmp != -1:
                    if anw == -1:
                        anw = 1+tmp
                    else:
                        anw = min(1+tmp, anw)

            return anw
        return solver(dp, mp, target, 0)


if __name__ == "__main__":
    stickers = ["seven","old","stream","century","energy","period","an","proper","together","sight","carry","milk","appear","winter","field","rather","caught","danger","lake","shall","machine","few","other","test","got","wing","map","finish","though","observe","log","they","foot","path","eat","glad","must","bar","did","of","clear","work","rule","quotient","produce","clean","wild","grass","example","left"]
    target = "weresurprise"
    solu = Solution()
    print(solu.minStickers(stickers, target))

