public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        double dripCoffee = 4.1;
        double latte = 3.6;
        double cappucino = 5.2;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";
    
        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = false;
        boolean isReadyOrder4 = true;
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1 + pendingMessage); // Displays "Welcome to Cafe Java, Cindhuri"
        
        //Noah
        if(isReadyOrder4 == true) {
            System.out.println(customer4 + readyMessage + "\n" + displayTotalMessage + cappucino);
        }
        else {
            System.out.println(customer4 +  pendingMessage);
        }

        //Sam
        System.out.println(customer2 + ", " + displayTotalMessage + (latte*2));
        if(isReadyOrder2 == true) {
            System.out.println(customer2 + readyMessage);
        }
        else {
            System.out.println(pendingMessage);
        }

        //Jimmy
        System.err.println(customer3 + " " + "here is " + (dripCoffee - latte) + "back");
    }
}
