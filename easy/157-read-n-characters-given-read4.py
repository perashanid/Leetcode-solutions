"""
Problem: Read N Characters Given Read4
Number: 157
Difficulty: Easy
Link: https://leetcode.com/problems/read-n-characters-given-read4/
Date: 2025-10-16
"""

"""
Time Complexity: O(n), where n is the number of characters to read.
Space Complexity: O(1) amortized, since we use a fixed-size buffer.
"""
def read4(buf4):
    """
    Fake read4 function for local testing. Replace with the problem's read4.
    """
    global file_content
    chars_read = min(4, len(file_content))
    for i in range(chars_read):
        buf4[i] = file_content[i]
    file_content = file_content[chars_read:]
    return chars_read

class Solution:
    def __init__(self):
        self.buffer = [''] * 4  # Buffer to store characters read from read4
        self.buffer_ptr = 0  # Pointer to the next character to be read from the buffer
        self.buffer_size = 0  # Number of valid characters in the buffer

    def read(self, buf, n):
        """
        Reads at most n characters from the file.

        Args:
            buf (list[str]): A list of strings to store the characters read.
            n (int): The maximum number of characters to read.

        Returns:
            int: The number of characters read.
        """
        read_count = 0  # Total number of characters read so far

        # While we need to read more characters and there are characters available either
        # in buffer or in the file (implicitly checked inside the while loop condition)
        while read_count < n:
            # If the buffer is empty, we need to call read4 to fill it
            if self.buffer_ptr == self.buffer_size:
                self.buffer_size = read4(self.buffer)  # Read up to 4 characters from the file
                self.buffer_ptr = 0  # Reset the buffer pointer
                if self.buffer_size == 0:  # If read4 returns 0, it means we have reached the end of the file
                    break  # Break out of the loop

            # Determine how many characters we can read from the buffer
            read_chars = min(n - read_count, self.buffer_size - self.buffer_ptr)

            # Copy characters from the buffer to the output buffer
            for i in range(read_chars):
                buf[read_count + i] = self.buffer[self.buffer_ptr + i]

            # Update the buffer pointer and the read count
            self.buffer_ptr += read_chars
            read_count += read_chars

        return read_count

# Example usage (for local testing):
if __name__ == '__main__':
    global file_content
    file_content = "abc"  # Initialize the file content

    solution = Solution()

    buf = [''] * 1
    chars_read = solution.read(buf, 1)
    print(f"Read {chars_read} characters: {buf[:chars_read]}")  # Output: Read 1 characters: ['a']

    buf = [''] * 2
    chars_read = solution.read(buf, 2)
    print(f"Read {chars_read} characters: {buf[:chars_read]}")  # Output: Read 2 characters: ['b', 'c']

    buf = [''] * 1
    chars_read = solution.read(buf, 1)
    print(f"Read {chars_read} characters: {buf[:chars_read]}")  # Output: Read 0 characters: []

    file_content = "abcdefgh"
    solution = Solution()
    buf = [''] * 5
    chars_read = solution.read(buf, 5)
    print(f"Read {chars_read} characters: {buf[:chars_read]}")

    buf = [''] * 5
    chars_read = solution.read(buf, 5)
    print(f"Read {chars_read} characters: {buf[:chars_read]}")