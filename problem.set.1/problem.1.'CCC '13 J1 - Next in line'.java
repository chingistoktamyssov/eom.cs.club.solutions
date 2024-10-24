import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input youngest and middle age
        int y = scanner.nextInt(); // youngest age
        int m = scanner.nextInt(); // middle age

        // Calculate and print the oldest age
        System.out.println(m * 2 - y);

        scanner.close();
    }
}