#addition of two lists using lambda
nums1 = [7, 4, 6, 5]
nums2 = [8, 3, 9, 2]

result = map(lambda x, y: x+y, nums1, nums2)
print("\nAddition of two given lists:")
print(list(result),'\n')



#map func practice:
nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Squared nums in given list:")
print(square)

double_chars = [c*2 for c in "hello"]
print(double_chars)