class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for oper in operations:
            if oper == '+':
                sum1 = record[-1] + record[-2]
                record.append(sum1)
            elif oper == 'C':
                record.pop()
            elif oper == 'D':
                doubled = record[-1] * 2
                record.append(doubled)
            else:
                record.append(int(oper))
        return sum(record)