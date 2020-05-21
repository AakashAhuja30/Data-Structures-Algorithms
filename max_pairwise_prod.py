# python3
def max_pairwise_product(numbers):
    numbers.sort()
    num1=numbers[-1]
    num2=numbers[-2]
    return num1*num2

if __name__ == '__main__':
    # print("Enter how many numbers:")
    n = int(input())
    # print("Enter numbers:")
    a = [int(x) for x in input().split()]
    print(max_pairwise_product(a))


