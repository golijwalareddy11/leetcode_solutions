class Solution:
    def interpret(self, command: str) -> str:
        s=[]
        i=0
        while i<len(command):
            if command[i:i+2]=="()":
                s.append("o")
                i+=2
            elif command[i:i+4]=="(al)":
                s.append("al")
                i+=4
            else:
                s.append(command[i])
                i+=1
        return "".join(s)       