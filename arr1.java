import java.util.Arrays;
import java.util.Scanner;
public class arr1{
    public static void main(String[] args){
        
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        int maxm=Integer.MIN_VALUE;
        int minm=Integer.MAX_VALUE;
        int s_maxm=arr[0];
        for(int i=0; i<n; i++){
            arr[i]=sc.nextInt();
        }
        for(int i=0; i<n; i++){
            System.out.println(arr[i]);
        }
        for(int i=0; i<n; i++){
            if (arr[i]>maxm){
                maxm=arr[i];
            }
            if (arr[i]<minm){
                minm=arr[i];
            }
        }
        System.out.println(maxm);
        System.out.println(minm);
        Arrays.sort(arr);
        System.out.println(arr[n-2]);
        for(int i=0; i<n; i++){
            if (arr[i]!=maxm){
                if (arr[i]>maxm){
                s_maxm=arr[i];
            }

            }
            
        }
}
}