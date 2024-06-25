class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # make hashmap for every str
        # compare and add to list

        # def makeHash(s):
        #     hm = {}
        #     for i in s:
        #         if i in hm:
        #             hm[i] += 1
        #         else:
        #             hm[i] = 1
        #     return tuple(sorted(hm.items()))

        hm = {}
        for s in strs:
            key = tuple(sorted(s))

            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]

        return hm.values()


    


        