
public class main {
    public static void main(String args[]) {
      int a = 10;
      int b = 0;
      try{
        System.out.println("a = "  + a + ",b =" + b );  
        System.out.println("a/b = " + a/b);
      }catch(ArithmeticException e){
          System.out.println("Divisão por 0 invalida!");
          System.out.println("Para b = 1 ");
          b = 1;
          System.out.println("a/b = " + a/b);
          
      }
      
      
    }
}