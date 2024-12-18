MAX = 100

def calculate_sum(arr):
   return sum(arr)

def get_integer_input(prompt):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def main():
   try:
      n = get_integer_input("Enter the number of elements (1-100): ")
      if not 1 <= n <= MAX:
         print("Invalid input. Please provide a number ranging from 1 to 100.")
         return

      arr = []
      print(f"Enter {n} integers:")
      for _ in range(n):
         arr.append(get_integer_input(""))

      total = calculate_sum(arr)
      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
   except EOFError:
      print("\nProgram terminated by user.")
   except Exception as e:
      print(f"An error occurred: {e}")
if __name__ == "__main__":
   main()
