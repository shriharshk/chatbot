import java.util.List;

public class DialogflowResponse {
    private Result result;

    public Result getResult() {
        return result;
    }

    public class Result {
        private Fulfillment fulfillment;

        public Fulfillment getFulfillment() {
            return fulfillment;
        }
    }

    public class Fulfillment {
        private String speech;

        public String getSpeech() {
            return speech;
        }
    }
}
