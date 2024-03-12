# def LengthofCycle(nums):
#     count = 0
#     num = str(nums)
#     while True:
#         if len(num) == 1:
#             num = '0' + num
#         num = num[-1] + str(int(num[0])+int(num[1]))[-1]
#         count += 1
#         if num == str(nums):
#             break
#     return count

def LengthofCycle(nums):
    count = 0
    num = nums
    while True:
        num = (num%10)*10 + (num//10 + num%10)%10
        count += 1
        if num == nums:
            break
    return count

def main():
    nums = int(input())
    print(LengthofCycle(nums))

if __name__ == "__main__":
    main()