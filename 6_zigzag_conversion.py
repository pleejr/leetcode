class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        matrix = []
        s_list = list(s)

        while len(s_list) != 0:
            col = [""] * numRows
            for i in range(len(col)):
                col[i] = s_list.pop(0) if s_list else ""
            print(col)
            matrix.append(col)
            col = [""] * numRows
            for i in range(len(col) - 2):
                col[i + 1] = s_list.pop(0) if s_list else ""
            col.reverse()
            print(col)
            matrix.append(col)

        for row in range(numRows):
            for col in matrix:
                result += col[row]
        
        return result