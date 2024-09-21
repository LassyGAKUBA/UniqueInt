#!/usr/bin/python3
import time  

class UniqueInt:
    def __init__(self):
        """
        Constructor method that initializes a boolean array to track the integers 
        from -1023 to 1023. We use an array of size 2047 to represent this range.
        Each index in this array will be set to True if the corresponding integer 
        has been encountered, otherwise it remains False.
        """
        self.seen = [False] * 2047 
    
    def readNextItemFromFile(self, line):
        """
        Method to read the next valid integer from the file line. This method handles:
        - Stripping whitespaces around the number
        - Skipping lines that are empty or contain multiple numbers
        - Handling non-integer values
        Returns:
        - A valid integer within the range if present
        - None if the line is invalid or the integer is out of range
        """
        try:

            line = line.strip()

            if line == "" or " " in line:
                return None
            number = int(line)
            if number < -1023 or number > 1023:
                return None
            return number
        except ValueError:
            return None
    
    def processFile(self, inputFilePath, outputFilePath):
        """
        This method processes the input file and writes the result to the output file.
        It:
        - Reads each line from the input file
        - Checks if the line contains a valid unique integer
        - Keeps track of integers already seen using the boolean array
        - Sorts the unique integers manually
        - Writes the sorted unique integers to the output file
        """
        unique_numbers = []  
        with open(inputFilePath, 'r') as input_file:
            for line in input_file:
                
                number = self.readNextItemFromFile(line)
                
                if number is not None and not self.seen[number + 1023]:
                    self.seen[number + 1023] = True  
                    unique_numbers.append(number)  
        
       
        for i in range(len(unique_numbers)):
            for j in range(i + 1, len(unique_numbers)):
                if unique_numbers[i] > unique_numbers[j]:
                   
                    unique_numbers[i], unique_numbers[j] = unique_numbers[j], unique_numbers[i]
        
       
        with open(outputFilePath, 'w') as output_file:
           
            for number in unique_numbers:
                output_file.write(f"{number}\n")
    
    def run(self, inputFilePath, outputFilePath):
        """
        This method acts as the entry point for processing a file. It:
        - Starts a timer to track how long the processing takes
        - Calls the `processFile` method to process the input file
        - Stops the timer and prints the elapsed time for processing the file
        """
        start_time = time.time() 
        self.processFile(inputFilePath, outputFilePath)  
        end_time = time.time()  
        print(f"Processed {inputFilePath} in {end_time - start_time:.2f} seconds")


unique_int_processor = UniqueInt()

unique_int_processor.run('../../sample_inputs/small_sample_input_02.txt', '../../sample_results/small_sample_input_02.txt_results.txt')
