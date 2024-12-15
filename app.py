def read_and_write_with_error_handling():
    try:
        
        input_filename = input("Enter the name of the file to read from: ")
        
        
        with open(input_filename, "r") as infile:
            content = infile.readlines()
        
        
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        
        output_filename = input("Enter the name of the file to write to: ")
        
        
        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except PermissionError:
        print("Error: Permission denied. Unable to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_write_with_error_handling()
