import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Array of consonants
        char[] consonants = {'b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w'};

        while (true) {
            String word = scanner.nextLine();

            // Break if the word is 'quit!'
            if (word.equals("quit!")) {
                break;
            }

            // Check if the word has more than 4 characters
            if (word.length() > 4) {
                // Check if the word ends with a consonant followed by 'or'
                char thirdLastChar = word.charAt(word.length() - 3);
                if (isConsonant(thirdLastChar, consonants) && word.endsWith("or")) {
                    // Replace the suffix with 'our'
                    word = word.substring(0, word.length() - 2) + "our";
                }
            }

            // Output the modified word
            System.out.println(word);
        }

        scanner.close();
    }

    // Helper function to check if a character is a consonant
    public static boolean isConsonant(char ch, char[] consonants) {
        for (char consonant : consonants) {
            if (ch == consonant) {
                return true;
            }
        }
        return false;
    }
}