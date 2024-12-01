## Part 1

1. **Reading the File**: The script opens the file `day1/input.txt` in read mode.
2. **Initializing Lists**: Two lists, `leftID` and `rightID`, are initialized to store integer values from the file.
3. **Reading and Storing Data**: For each line in the file, the script splits the line into two numbers, converts them to integers, and appends them to `leftID` and `rightID` respectively.
4. **Sorting Lists**: Both `leftID` and `rightID` lists are sorted.
5. **Calculating Difference**: The script calculates the sum of absolute differences between corresponding elements in `leftID` and `rightID`.

## Part 2

1. **Reading the File**: The script reopens the file `day1/input.txt` in read mode.
2. **Initializing Data Structures**: An empty list `IDs` and a `defaultdict` named `scores` are initialized.
3. **Reading and Storing Data**: For each line in the file, the script splits the line into two numbers, converts them to integers, appends the first number to `IDs`, and increments the count of the second number in `scores`.
4. **Calculating Score**: The script calculates a score by multiplying each ID in `IDs` by its corresponding count in `scores` and summing the results.
