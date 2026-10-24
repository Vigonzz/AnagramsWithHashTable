# task 2:
# Read and parse each word from the file pride-and-prejudice.txtDownload pride-and-prejudice.txt. 
# Read the text line by line, and split it into words. 


from hashtable import HashTable
import re

# Got through the provided file and separate each word. Ensure things such as spaces, commas, etc. are not
# getting included in the count 
def count_anagram_roots(filename):
    table = HashTable()
    with open(filename, "r", encoding = "utf-8") as file:
        # Go through each line, lowercase clean it up and store it in our table
        for line in file:
            words = re.findall("[a-zA-Z0-9]+", line)
            for word in words:
                lower_word = word.lower()
                root = "".join(sorted(lower_word))
                table.insert(root)

    # Get the size of out text
    return table.size()


if __name__ == "__main__":
    print(count_anagram_roots("pride-and-prejudice.txt"))

