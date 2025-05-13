def modify_content(text):
    # Example modification: convert text to uppercase
    return text.upper()

def main():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified = modify_content(content)

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except IOError:
        print("❌ Error: Could not read or write to file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
