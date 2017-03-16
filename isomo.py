class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            if s == t == '':
                return True
            
            else:
                containerDict = {}
                sList = list(s)
                tList = list(t)
                while 0 < len(sList):
                    popElement = sList.pop()
                    if not containerDict.has_key(popElement):
                        containerDict[popElement] = tList.pop()
                    elif containerDict.has_key(popElement):
                        if containerDict[popElement] != tList.pop():
                            return False
            return True
