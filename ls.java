import java.io.File;

class ls{
    public static void main(String[] args){
        File currdir = new File(".");
        String files[] = currdir.list();
        if (files!=null){
            for(String file : files){
                System.out.println(file);
            }
        }
        else{
            System.out.println("No files found or unable to access the directory.");
        }
    }
}