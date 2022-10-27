
public class Circle extends Shape {
	Circle(int r){
		a=r;
	}
	
	public  void printArea() {
		double area=a*a*3.14;
		System.out.println(area);
	}
}
