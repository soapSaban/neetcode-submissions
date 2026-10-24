class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                record.append(record[len(record)-1]+record[len(record)-2])
            if operations[i]=="C":
                 record.pop()
            if operations[i]=="D":
                record.append(record[-1]*2)
            if operations[i] not in ["+", "C", "D"]:
                record.append(int(operations[i]))
        return sum(record)
            