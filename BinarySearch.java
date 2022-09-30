public class BinarySearch {
	int index(int arr[], int key, int low, int high) {
		while(low<=high) {
			int mid=(low+high)/2;
			if(arr[mid]==key)
				return mid;
			else if(arr[mid]>key)
				high=mid-1;
			else 
				low=mid+1;
		}
		return -1;
	}
}
