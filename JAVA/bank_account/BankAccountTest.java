public class BankAccountTest {
    public static void main(String[] args) {
        BankAccount bankAccount1 = new BankAccount(0.0, 0.0);
        
        System.out.println("Current Checking Balance is: $" + bankAccount1.getCheckingAccountBalance());
        System.out.println("Current Savings Balance is: $" +bankAccount1.getSavingsAccountBalance());
        System.out.println("Number of Accounts Open: " + BankAccount.numberOfAccounts);

        bankAccount1.deposit(100, 500);

        System.out.println("Current Checking Balance is: $" + bankAccount1.getCheckingAccountBalance());
        System.out.println("Current Savings Balance is: $" +bankAccount1.getSavingsAccountBalance());
        System.out.println("Number of Accounts Open: " + BankAccount.numberOfAccounts);

        bankAccount1.withdraw(50, 250);

        System.out.println("Current Checking Balance is: $" + bankAccount1.getCheckingAccountBalance());
        System.out.println("Current Savings Balance is: $" +bankAccount1.getSavingsAccountBalance());
        System.out.println("Number of Accounts Open: " + BankAccount.numberOfAccounts);

        BankAccount bankAccount2 = new BankAccount(1000, 10000);

        System.out.println("Number of Accounts Open: " + BankAccount.numberOfAccounts);

    }
    
}
