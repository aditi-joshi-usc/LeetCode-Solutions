class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        q.append((startGene, 0))

        visited = set()

        def diff_one(g1, g2):
            cnt =0 
            for i in range(len(g1)):
                if g1[i] != g2[i]:
                    cnt+=1
            if cnt ==1:
                return True
            return False



        while q:
            curr_gene, mutation_cnt = q.popleft()
            if curr_gene == endGene:
                return mutation_cnt
            

            for i in range(len(bank)):

                if diff_one(bank[i], curr_gene) and bank[i] not in visited:
                    q.append((bank[i], mutation_cnt+1))
                    visited.add(bank[i])
        return -1
            

