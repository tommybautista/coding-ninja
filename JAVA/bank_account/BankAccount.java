public class BankAccount {

    // The class should have the following attributes: (double) checking balance, (double) savings balance.
    private double checkingBalance;
    private double savingsBalance;


    // Create a class member (static) that has the number of accounts created thus far.
    public static int numberOfAccounts = 0;

    // Create a class member (static) that tracks the total amount of money stored in every account created.
    public static int totalAmountOfMoney = 0;

    // In the constructor, be sure to increment the account count.
    public BankAccount(double checkingParam, double savingsParam) {
        checkingBalance = checkingParam;
        savingsBalance = savingsParam;
        numberOfAccounts++;
    }

    // Create a getter method for the user's checking account balance.
    public double getCheckingAccountBalance() {
        return this.checkingBalance;
    }

    // Create a getter method for the user's saving account balance.
    public double getSavingsAccountBalance() {
        return this.savingsBalance;
    }

    // Create a method that will allow a user to deposit money into either the checking or saving, be sure to add to total amount stored.
    public void deposit(double checkingDeposit, double savingsDeposit) {
        checkingBalance += checkingDeposit;
        savingsBalance += savingsDeposit;
    }

    // Create a method to withdraw money from one balance. Do not allow them to withdraw money if there are insufficient funds.
    public void withdraw(double checkingWithdraw, double savingsWithdraw) {
        checkingBalance -= checkingWithdraw;
        savingsBalance -= savingsWithdraw;
    }


}