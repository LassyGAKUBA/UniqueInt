import os

inputFilePath = 'dsa/hw01/sample_inputs/sample_input_02.txt'
if not os.path.exists(inputFilePath):
    print(f"Error: {inputFilePath} not found!")
else:

    unique_int_processor.run(inputFilePath, 'dsa/hw01/sample_results/sample_input_02_results.txt')
