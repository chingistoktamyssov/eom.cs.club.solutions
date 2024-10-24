import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input question number (1 or 2)
        int question = scanner.nextInt();
        // Input number of citizens (cyclists) per country
        int n = scanner.nextInt();

        // Input and sort cyclists from both countries
        int[] c1 = new int[n];
        int[] c2 = new int[n];

        for (int i = 0; i < n; i++) {
            c1[i] = scanner.nextInt();
        }
        for (int i = 0; i < n; i++) {
            c2[i] = scanner.nextInt();
        }

        Arrays.sort(c1); // sort country 1 cyclists
        Arrays.sort(c2); // sort country 2 cyclists

        int total = 0;

        if (question == 1) {
            // Slowest possible speed: pair slowest with slowest
            for (int i = 0; i < n; i++) {
                total += Math.max(c1[i], c2[i]);
            }
        } else {
            // Fastest possible speed: pair slowest with fastest
            for (int i = 0; i < n; i++) {
                total += Math.max(c1[i], c2[n - 1 - i]);
            }
        }

        // Output the total speed
        System.out.println(total);

        scanner.close();
    }
}
