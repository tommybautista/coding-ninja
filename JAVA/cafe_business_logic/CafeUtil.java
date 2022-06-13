import java.util.ArrayList;

public class CafeUtil {


    // Get Streak Goal
    public int getStreakGoal() {
        int sum = 0;
        for(int week = 1; week <= 10; week++) {
            sum+= week;
        }
        return sum;
    }

    /*
        Given an array of prices for products purchased, lineItems,
        sum the amounts to return the order total
    */
    public double getOrderTotal(double[] lineItems) {
        double sum = 0;
        
        for (double price: lineItems) {
            sum+= price;
        }
        return sum;

    }

    // addCustomer
    public void addCustomer(ArrayList<String> customerList) {
        System.out.println("Please enter your name:");
        String userName = System.console().readLine();
        System.out.printf("Hello, %s! ", userName);
        System.out.printf("There are %s people ahead of you.\n", customerList.size());
        customerList.add(userName);
        System.out.println(customerList);
    }

    // Display Coffee Menu
    public void displayMenu(ArrayList<String> menuItems) {

        for (int id = 0; id < menuItems.size(); id++) {
            System.out.printf("%s %s \n", id, menuItems.get(id));
        }
    }

    // Price chart
    // Ninja bonus: Format for currency
    // https://docs.oracle.com/javase/tutorial/java/data/numberformat.html
    public void printPriceChart(String productName, double price, int maxQuantity) {

        System.out.printf("%s\n", productName);
        for(int quantity = 1; quantity < maxQuantity; quantity++) {
            System.out.printf("%s - $%.2f\n", quantity, quantity * price);
        }
        
        System.out.println("");
    }

    

    // Display Coffee Menu
    // https://docs.oracle.com/javase/tutorial/java/data/numberformat.html
    public boolean displayMenu(ArrayList<String> menuItems, ArrayList<Double> priceIndex) {
        if(menuItems.size() != priceIndex.size()) {
            return false;
        }
        for (int id = 0; id < menuItems.size(); id++) {
            System.out.printf("%s %s -- $%.2f \n", id, menuItems.get(id), priceIndex.get(id));
        }
        return true;
    }


    
    /* Sensei bonus:
    Make a method addCustomers where a barista can enter multiple customers. 
    Hint: You can use a while loop and ask the user to type q when they are finished entering names.
    */

    public void addCustomers(ArrayList<String> customerList) {
        boolean finished = false;
        String input;
        while (!finished) {
            System.out.println("Please enter a customer name or press Q to quit:");
            input = System.console().readLine();
            if (input.equals("Q")) {
                finished = true;
                return;
            }
            customerList.add(input);
            System.out.printf("%s was added to the list.", input);
            System.out.println(customerList);
        }
    }


}