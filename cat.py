filename = 'example.txt'

with open(filename, 'r') as f:
    print(f.read())

'''
import java.nio.file.*;

public class SimpleCat {
    public static void main(String[] args) throws Exception {
        String content = Files.readString(Path.of("example.txt"));
        System.out.print(content);
    }
}
'''