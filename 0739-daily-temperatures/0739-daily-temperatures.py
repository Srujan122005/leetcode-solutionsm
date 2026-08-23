class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous = stack.pop()
                answer[previous] = i - previous
            stack.append(i)
        return answer