public class multiplication {
public static void multiplication(int n) {
    for(int i = 1;i<=10;i++){
        System.out.println(n + " x " + i + " = " + (n*i)); 
    }
}
public static void main(String[] args) {
    int n = 5;
    multiplication(n);
}
}