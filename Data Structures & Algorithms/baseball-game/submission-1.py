class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            try:
                records.append(int(op))
            except:
                if op == "D":
                    records.append(records[-1] * 2)
                elif op == "C":
                    records.pop()
                elif op == "+":
                    records.append(records[-1] + records[-2])
                else:
                    pass
        return sum(records)
