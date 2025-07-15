public class DialogflowRequest {
    private String lang;
    private String query;
    private String sessionId;
    private String timezone;

    public DialogflowRequest(String query, String sessionId) {
        this.lang = "en";
        this.query = query;
        this.sessionId = sessionId;
        this.timezone = "Asia/Kolkata"; // set your timezone
    }

    // Getters and setters
}
