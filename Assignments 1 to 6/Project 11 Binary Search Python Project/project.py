def binary(arr,target):

     low = 0
     high = len(arr) -1



     while  low  <= high:
          mid = (low  + high)  // 2

     if arr[mid]== target:
       return mid
     elif arr[mid] > target:
         high  = mid -1

         

