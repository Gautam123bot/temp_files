import java.util.*;
class Demo {
    // non-static function
    void display() {
        System.out.println("A non-static function is called.");
    }

    // static function
    static void show() {
        System.out.println("The static function is called.");
    }

}

public class hello {
    public static void display1() {
        System.out.println("hii");
    }
    public static void main(String args[]) {
        // creating an object of the class A
        Scanner sc=new Scanner(System.in);
        display1();
        Demo obj = new Demo();
        // calling a the non-static function by using the object of the class
        obj.display();
        // calling a static function by using the class name
        Demo.show();

        int arr[]=new int[5];
        for(int i=0;i<5;i++){
            // arr[i]=sc.nextInt();
            arr[i]=i;
        }
        for(int val:arr){
            System.out.print(val+" ");
        }
        
       
        // int n=sizeof(arr)/sizeof(int);
        sc.close();

    }
}