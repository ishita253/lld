def tail(filename, n=10):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line, end='')

# Example usage
tail('example.txt', 10)  # Prints last 10 lines of example.txt

'''
java version
import java.io.*;
import java.util.*;

public class Tail {
    public static void main(String[] args) throws IOException {
        String filename = "example.txt"; // Replace with your file
        int n = 10; // Number of lines to show from the end

        List<String> lines = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;

            // Read all lines into the list
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
        }

        // Calculate the starting index to print last n lines
        int start = Math.max(lines.size() - n, 0);

        for (int i = start; i < lines.size(); i++) {
            System.out.println(lines.get(i));
        }
    }
}
'''