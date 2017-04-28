def is_palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

def largest_product_palindrome():
    max_product = 0
    for i in range(100,1000):
        for j in range(100,1000):
            product = i * j
            if product > max_product and is_palindrome(product):
                max_product = product
    return max_product

if __name__=="__main__":
    print(largest_product_palindrome())