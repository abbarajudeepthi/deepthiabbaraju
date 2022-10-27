public class Triangle extends Shape {
	Triangle(int base,int h){
		a=base;
		b=h;
	}
	public void printArea() {
		double area=0.5*a*b;
		System.out.println(area);
	}
}
