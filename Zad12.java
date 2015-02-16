package regularTetrahedron;

import java.lang.Math;
import java.util.ArrayList;
import java.util.Collections;

public class Zad12 {
	
	// Fill tetrahedron with water - implementation of fill_tetrahedron(int num)
	
	public static double fill_tetrahedron(int num){
		if (num < 0){
			System.out.println("Bad input for edge length");
			return -1;
		}
		
		double edgeDm = num / 10;
		double volume=edgeDm*edgeDm*edgeDm*Math.sqrt(2)/12;
		return Math.round(volume*100.0d)/100.0d;
	}
	
	//	Tetrahedron filled with water - implementation of  tetrahedron_filled(tetrahedrons, water) 
	
    public static int tetrahedron_filled(ArrayList<Integer> tetrahedrons, int water){
    	
		if (tetrahedrons.isEmpty()){
			System.out.println("Invalid input for tetrahedrons.");
			return 0;
		}
		
		if (water <= 0){
			System.out.println("Invalid input for amount of water in liters");
			return 0;			
		}
		
		int count=0;
	    double volumeMax=0;
	    Collections.sort(tetrahedrons);
		
		for (int i=0; i<tetrahedrons.size(); i++){
			volumeMax+=fill_tetrahedron(tetrahedrons.get(i));
			if (volumeMax > water){
				break;
			} 
			else {
				count ++;	
			}
		}
		
		return count;	
		
	}
    
    // main method
	
	public static void main (String [] args){
		System.out.println(fill_tetrahedron(100));
		ArrayList<Integer> list=new ArrayList<Integer>();
		list.add(140);
		list.add(100);
		list.add(20);
		list.add(30);

//		Collections.sort(list);
//		for (int i=0; i<list.size(); i++){
//			System.out.println(fill_tetrahedron(list.get(i)));
//		}
		
	System.out.println(tetrahedron_filled(list, 129));
		
	}
  

}

