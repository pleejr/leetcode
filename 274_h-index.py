class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        l = len(citations)
        h = citations[0]
        count = 0

        if l == 1:
            if h >= 1:
                return 1
            else:
                return 0

        for i in range(l):
            h = citations[i]
            if h >= l:
                print("increment")
                count += 1
            elif h > 0:
                # how many papers have at least h citations?
                has_citations = i + 1
                remaining_papers = citations[has_citations:]
                for paper in remaining_papers:
                    if paper == h:
                        has_citations += 1
                    else:
                        break
                # are there at least h citations?
                if has_citations >= h:
                    print("returning h")
                    print(f"count={count}")
                    return max(h, count)
                else:
                    count += 1
        print("returning count")
        return count