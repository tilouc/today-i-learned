class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        len_list = len(address)

        defanged_address = ""

        for i in range(len_list):
            if address[i] == ".":
                defanged_address += "[.]"
            else:
                defanged_address += address[i]

        return defanged_address