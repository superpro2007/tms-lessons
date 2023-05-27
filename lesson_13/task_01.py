# import re
# def is_car_number(b):


#     a = re.fullmatch(r'\d{4}[A-Z]{2}-\d',b)
#     return a is not None


# if __name__ == '__main__':
#      assert is_car_number('12344B-5')

# 5
# def generate_squares(count):
#     for num in range(1, count + 1):
#         yield num**2


# if __name__ == "__main__":
#     for i in generate_squares(10):
#         print(i)

class SquaresIterable:
    def __init__(self,count):
        self.count = count
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.num +=1
        if self.num > self.count:
            raise StopIteration()
        return self.num ** 2
    
    
    
    
for i in SquaresIterable(10):
    print(i)