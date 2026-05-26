'''Sequential Search'''
# def Sequential_Search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return None

# arr = [1,2,3,4,5,6,7,8,9]

# while True:
#     t = int(input("Aradiginiz sayiyi giriniz: "))
#     result = Sequential_Search(arr, t)
    
#     if result is not None:
#         print("Bulundu, index: ", result)
#     else:
#         print("Bulunmadi!")




'''Sequential Search-2'''
# def sequential_search(arr, target):
#     index = 0
#     found = False

#     while index <= len(arr) and  not found:
#         if arr[index] == target:
#             found = True
#         else:
#             index += 1
#     return (index, found)

# arr = [1,2,3,4,5,6,7,8,9]

# while True:
#     t = int(input("Aradiginiz sayiyi giriniz: "))
#     result = sequential_search(arr, t)
    
#     if result is not None:
#         print("Bulundu, index: ", result)
#     else:
#         print("Bulunmadi!")


'''Sequential Search with ordered list'''

# def sequential_search(arr, target):
#     index = 0
#     found = False
#     stop = 0

#     while index <= len(arr) and  not found and not stop:
#         if arr[index] == target:
#             found = True
#         else:
#             if arr[index] == target:
#                 stop = True
#             else:
#                 index += 1
#     return (index, found)

# arr = [1,2,3,4,5,6,7,8,9]

# while True:
#     t = int(input("Aradiginiz sayiyi giriniz: "))
#     result = sequential_search(arr, t)
    
#     if result is not None:
#         print("Bulundu, index: ", result)
#     else:
#         print("Bulunmadi!")

'''binary search'''
# def binary_search(arr, target):
#     left = 0
#     right = (len(arr)-1)
#     found = False

#     while left <= right and not found:
#         middle = int(left+right)//2

#         if arr[middle] == target:
#             return found, True
        
#         if arr[middle] > target:
#             right = middle - 1
#         else:
#             left = middle + 1
#     return found

# arr = [1,2,3,4,5,6,7,8]

# while True: 
#     n = int(input("Sayi giriniz: "))
#     result = binary_search(arr,n)
    
#     if result:
#         print("Bulundu")
#     else:
#         print("bulunmadi")



"""KAYAN PENCERE PROBLEMI"""
# from collections import deque

# def kayak_pencere(liste, k):
#     n = len(liste)
#     sonuclar = []
#     pencere = deque()

#     # ilk pencere
#     for i in range(k):
#         while pencere and liste[i] >= liste[pencere[-1]]:
#             pencere.pop()
#         pencere.append(i)

#     # diğer pencereler
#     for i in range(k, n):

#         sonuclar.append(liste[pencere[0]])

#         # pencere dışındaki elemanları sil
#         while pencere and pencere[0] <= i - k:
#             pencere.popleft()

#         # küçük elemanları sil
#         while pencere and liste[i] >= liste[pencere[-1]]:
#             pencere.pop()

#         pencere.append(i)

#     sonuclar.append(liste[pencere[0]])

#     return sonuclar

# liste = [1,3,-1, -3, 5, 3, 6,7]
# k=5
# print(kayak_pencere(liste, k))




"""PARANTEZ ESLESME KONTROLU"""
# def parantez_eslesme_kontrolu(ifade):
#     stack = []
#     eslesme = {
#         ')' : '(',
#         ']' : '[',
#         '}' : '{'
#     }

#     for karakter in ifade:
#         if karakter in "{([":
#             stack.append(karakter)
#         elif karakter in "})]":
#             if not stack:
#                 return False
#             ust = stack.pop()
#             if eslesme[karakter] != ust:
#                 return False
    
#     if not stack:
#         return True
#     else:
#         return False

# ifade = "{}"
# print(parantez_eslesme_kontrolu(ifade))

#mergesort
# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])

#     return merge(left, right)


# def merge(left, right):
#     result = []
#     i = 0 
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result   


# arr = [3,2,13,4,6,5,7,8,1,20]
# print(mergesort(arr))


#insertion sort
# def insertionsort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr
# arr=[2,3,4,2,7,11,1,0,13]
# print(insertionsort(arr))     

# def selectionsort(arr):
#     for i in range(len(arr) -1, 0, -1):
#         positionofMax = 0 
#         for location in range(1, i+1):
#             if arr[location] > arr[positionofMax]:
#                 positionofMax = location 
#         print(positionofMax)
#         temp = arr[i]
#         arr[i] = arr[positionofMax]
#         arr[positionofMax]=temp
#         print(arr)
#     return arr

# arr = [3,2,13,4,6,5,7,8,1,20]
# selectionsort(arr)




