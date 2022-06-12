import java.util.ArrayList;

public class CafeUtil {

    // TestCafe testCafe = new TestCafe();
    // do


    public int getStreakGoal() {
        int sum = 0;
        for (int i = 0; i < (10+1); i++) {
            sum = sum + i;
        }
        return sum;
    }

    public double getOrderTotal() {
        double[] lineItems = {3.5, 1.5, 4.0, 4.5};
        double sum = 0;
        for (double i: lineItems) {
            sum += i; 
        }
        return sum;
    }

    public void displayMenu () {
        ArrayList<String> menu = new ArrayList<String>();
            menu.add("drip coffee");
            menu.add("cappuccino");
            menu.add("latte");
            menu.add("mocha");
        for (String i: menu) {
            System.out.println(i);
        }
    }
    
    public void addCustomer() {

            System.out.println("Please enter your name:");
            String userName = System.console().readLine();
            System.out.println("Hello " + userName + "!");
    
            ArrayList<String> customers = new ArrayList<String>();
                customers.add(userName);
                
                for (String i: customers) {
                    int count = customers.size();

                    System.out.println( "There are " + (count-1) + " people in front of you!");
                    System.out.println(customers);
                }
        }
}
