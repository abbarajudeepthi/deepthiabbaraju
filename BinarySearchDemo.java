public class BinarySearchDemo {
	public static void main(String args[]) {
		BinarySearch bs=new BinarySearch();
		int arr[]= {2,6,15,43,49,57};
		int n=arr.length;
		int key=15;
		int r=bs.index(arr,key,0,n-1);
		if(r==-1)
			System.out.println("enf");
		else
			System.out.println("ef"+r);
			
		
	}

}
