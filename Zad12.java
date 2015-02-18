package hack_bulgaria;

import java.lang.Math;
import java.util.ArrayList;
import java.util.Collections;

public class Zad12 {

	// 1) Fill tetrahedron with water - implementation of fill_tetrahedron(int num)

	public static double fill_tetrahedron(int num) {
		if (num < 0) {
			System.out.println("Bad input for edge length");
			return -1;
		}

		double edgeDm = num / 10; // length of the edge in decimetres
		double volume = edgeDm * edgeDm * edgeDm * Math.sqrt(2) / 12; // the volume of Regular Tetrahedron in dm
		return Math.round(volume * 100.0d) / 100.0d; // rounding volume to the second sign
	}

	// 2) Tetrahedron filled with water - implementation of tetrahedron_filled(tetrahedrons, water)

	public static int tetrahedron_filled(ArrayList<Integer> tetrahedrons,
			int water) {
		if (tetrahedrons == null) {
			System.out.println("Missing list with tetrahedrons.");
			return 0;
		}

		if (tetrahedrons.isEmpty()) {
			System.out.println("The list of tetrahedrons is empty.");
			return 0;
		}

		if (water <= 0) {
			System.out.println("Invalid input for amount of water in litres");
			return 0;
		}

		int count = 0; // the number of tetrahedrons that could be filled with
						// water
		double sumVolume = 0; // the sum of volumes of tetrahedrons
		Collections.sort(tetrahedrons); // sort the list of tetrahedrons

		for (int i = 0; i < tetrahedrons.size(); i++) {
			sumVolume += fill_tetrahedron(tetrahedrons.get(i));
			if (sumVolume > water) {
				break;
			} else {
				count++;
			}
		}

		return count;

	}

	// main method

	public static void main(String[] args) {
		System.out.println(fill_tetrahedron(100));
		ArrayList<Integer> list = new ArrayList<Integer>();
		list.add(140);
		list.add(100);
		list.add(20);
		list.add(30);

		System.out.println(tetrahedron_filled(null, 60));

	}

}
