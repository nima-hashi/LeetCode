class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        # Step 1: Count the frequencies of each number
        counter = Counter(nums)
        
        # Step 2: Group numbers by their frequencies
        cntToVal = defaultdict(list)
        for val, cnt in counter.items():
            cntToVal[cnt].append(val)
        
        # Step 3: Extract the top k frequent elements
        res = []
        # Get the unique counts and sort them in descending order
        cnts = sorted(cntToVal.keys(), reverse=True)
        
        # Iterate through the counts and collect the top k elements
        for count in cnts:
            for num in cntToVal[count]:
                if len(res) == k:
                    return res
                res.append(num)
        
        return res
        
            
        

        

       