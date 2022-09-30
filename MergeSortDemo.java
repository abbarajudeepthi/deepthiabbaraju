import java.util.Arrays;

public class MergeSortDemo {
	public static void main(String args[]) {
		MergeSort ms=new MergeSort();
		interchanges ic=new interchanges();
		int a[]= {149,143,115,157,102,106};
		int n=a.length;
		ms.mergeSort(a,n);
		System.out.println(Arrays.toString(a));
		System.out.println(ic.minSwaps(a,n));
	}

}
