/**
 * This program allows the user to enter a quadratic equation and then the other pertinent 
 * information needed to Riemann sum then calculates and outputs the left and right Riemann sum.
 * 
 * @author Jared Schuller
 * @version 1.0 1/26/14
 */
import java.util.Scanner;
public class Reimann {
	private static int a, b, c, start, end, interval, range;
	private static double leftArea, rightArea;
	
	/**
	 * Runs the program
	 * @param args
	 */
	public static void main(String[] args) {
		input();
		LeftRiemannSum();
		System.out.println("The left riemann sum area is: " + leftArea);
		RightRiemannSum();
		System.out.println("The right riemann sum area is: " + rightArea);
	}
	
	/**
	 * Gathers all the information needed from the user in order to continue
	 */
	public static void input(){
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Reimann Sum Solver!");
		System.out.println("Please enter the quadratic formula in the form of ax^2 + bx + c");
		System.out.print("a: ");
		a = keyboard.nextInt();
		System.out.print("b: ");
		b = keyboard.nextInt();
		System.out.print("c: ");
		c = keyboard.nextInt();
		System.out.println("The quadratic formula entered is " + a + "x^2 + " + b + "x + " + c);
		System.out.println("Please enter the start and end of the integration");
		System.out.print("start: ");
		start = keyboard.nextInt();
		System.out.println("end: ");
		end = keyboard.nextInt();
		System.out.println("Please enter the number of partitions");
		interval = keyboard.nextInt();
		range = end - start;
		keyboard.close();
	}
	
	/**
	 * Calculates the value of a number using the inputted quadratic equation
	 * @param number the x-value
	 * @return the y-value
	 */
	public static double quadratic(double number){
		
			double val = a * Math.pow(number, 2) + b * number + c;
			return val;
	}
	
	/**
	 * Calculates the Left Riemann Sum using the inputted bounds and inputted quadratic equation
	 */
	public static void LeftRiemannSum(){
		double width = range/interval;
		double value = 0;
		for(int i = 0; i < interval; i++){
			double place = start + (i * width);
			value = quadratic(place);
			leftArea += value * width;
		}
	}
	
	/**
	 * Calculates the Right Riemann Sum using the inputted bounds and inputted quadratic equation
	 */
	public static void RightRiemannSum(){
		double width = range/interval;
		double value = 0;
		for(int i = 0; i < interval; i++){
			double place = end - (i*width);
			value = quadratic(place);
			rightArea += value * width;
		}
	}
}
