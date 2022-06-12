import java.util.Date;
public class AlfredQuotes {
    
    public String basicGreeting() {
        // You do not need to code here, this is an example method
        return "Hello, lovely to see you. How are you?";
    }
    
    public String guestGreeting(String name) {
        name = "Beth Kane";
        return "hello " + name;
    }
    
    public String dateAnnouncement() {
        Date date = new Date();
        return "Today's date is " + date;
    }
    
    public String respondBeforeAlexis(String conversation) {
        if(conversation.indexOf("Alexis") > -1){
            return "Sure thing sir!";
        }
        if(conversation.indexOf("Alfred") > -1) {
            return "I do not know where it is sir, but I will look for it right away!";
        }
        else {
            return "I apologize for that!";
        }
    }
    
	// NINJA BONUS
	// See the specs to overload the guessGreeting method
    // SENSEI BONUS
    // Write your own AlfredQuote method using any of the String methods you have learned!
}

