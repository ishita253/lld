filename = "example.txt"

lines = 0
words = 0
chars = 0

with open(filename, 'r') as file:
    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)

print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {chars}")

'''import java.io.*;

public class WC {
    public static void main(String[] args) {
        String filename = "example.txt";
        int lines = 0, words = 0, chars = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines++;
                words += line.split("\\s+").length;
                chars += line.length();
            }
            System.out.println("Lines: " + lines);
            System.out.println("Words: " + words);
            System.out.println("Characters: " + chars);
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}
'''