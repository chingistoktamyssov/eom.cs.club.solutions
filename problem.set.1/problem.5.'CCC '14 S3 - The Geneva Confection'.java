import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input number of test cases
        int t = scanner.nextInt();

        // Loop over each test case
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();  // Number of cars

            Stack<Integer> train = new Stack<>();  // Stack for the train
            for (int j = 0; j < n; j++) {
                int car = scanner.nextInt();
                train.push(car);  // Add cars to train
            }
            Stack<Integer> branch = new Stack<>();  // Stack for the branch
            int expect = 1;  // Start expecting car 1

            while (!train.isEmpty()) {
                branch.push(train.pop());  // Send the cars from the train to the branch
                while (!branch.isEmpty() && branch.peek() == expect) {  // Check if the top of the branch is the expected car
                    branch.pop();  // Move the car to the lake
                    expect++;  // Now expect the next car number
                }
            }

            // If all cars are successfully moved from the branch to the lake
            if (branch.isEmpty()) {
                System.out.println("Y");
            } else {
                System.out.println("N");  // Impossible case
            }
        }

        scanner.close();
    }
}