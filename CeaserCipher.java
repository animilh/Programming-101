package CeaserCipher;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class CeaserCipher {

    // implementation of caesar_encrypt(str, n)
	
	public static String caesar_encrypt(String text, int n) {
		if ("".equals(text)) {
			System.out.println("Bad input for text");
			return "";
		}
		String encText = "";
		Map<Character, Integer> alphabet = new HashMap<Character, Integer>(26);
		for (int i = 65; i <= 90; i++) {
			alphabet.put((char) i, i - 65);
		}

		char[] a = text.toCharArray();
		char currentChar;
		int asciiChar;
		for (int i = 0; i < a.length; i++) {
			currentChar = a[i];
			if (alphabet.containsKey(Character.toUpperCase(a[i]))) {
				asciiChar = ((int) alphabet.get(Character.toUpperCase(a[i])) + n) % 26;
				for (Entry<Character, Integer> entry : alphabet.entrySet()) {
					if (entry.getValue().equals(asciiChar)) {
						a[i] = entry.getKey();
						
					}
				}

			}
			if (Character.isLowerCase(currentChar)) {
				a[i] += 32;
			}

			encText += a[i];
		}

		return encText;
	}

	// main method
	
	public static void main(String[] args) {

		System.out.println(caesar_encrypt("abXYZ", 2));

	}

}
