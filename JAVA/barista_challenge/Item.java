public class Item {

    // Set the member variables to private instead of  public.
    private String name;
    private double price;

    public Item(){}

    // Add a constructor to your Item class that takes a String name and  double price as arguments to set the name and price for that object on instantiation.

    public Item(String name, double price) {
        this.name = name;
        this.price = price;
    }

    // Create getters and setters for all the member variables.
    public String getName(){
        return this.name;
    }

    public double getPrice(){
        return this.price;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}