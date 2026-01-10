class solution:
    def find_missing_element(self,arr):
        for i in range(1,len(arr)+1):
            if i not in arr:
                return i 
            
if __name__ == "__main__":
    arr = [1,2,4,5,6]
    obj = solution()
    missing_element = obj.find_missing_element(arr)
    print(f"The missing element is: {missing_element}")