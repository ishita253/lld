import java.io.*;
public class head {
    public static void main(String args[]){
        String filename = "example.txt";
        int linesToRead = 10;
        try(BufferedReader reader = new BufferedReader(new FileReader(filename))){
            String line;
        int count =0;
        while((line=reader.readLine())!= null && count<linesToRead){
            System.out.println(line);
            count++;
        }
        }catch(IOException e){
            System.out.println("An error occurred while reading the file: " + e.getMessage());
        } 
        
}
}
