public class ChatActivity extends AppCompatActivity {

    private EditText userInput;
    private RecyclerView chatRecyclerView;
    private ChatAdapter chatAdapter;
    private List<ChatMessage> chatMessages = new ArrayList<>();
    private DialogflowApi dialogflowApi;

    private static final String CLIENT_ACCESS_TOKEN = "Bearer YOUR_DIALOGFLOW_CLIENT_ACCESS_TOKEN";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat);

        userInput = findViewById(R.id.userInput);
        chatRecyclerView = findViewById(R.id.chatRecyclerView);
        chatAdapter = new ChatAdapter(chatMessages);
        chatRecyclerView.setLayoutManager(new LinearLayoutManager(this));
        chatRecyclerView.setAdapter(chatAdapter);

        dialogflowApi = RetrofitClient.getClient().create(DialogflowApi.class);

        findViewById(R.id.sendButton).setOnClickListener(v -> sendMessage());
    }

    private void sendMessage() {
        String message = userInput.getText().toString().trim();
        if (message.isEmpty()) return;

        chatMessages.add(new ChatMessage(message, true));
        chatAdapter.notifyDataSetChanged();
        chatRecyclerView.scrollToPosition(chatMessages.size() - 1);
        userInput.setText("");

        DialogflowRequest request = new DialogflowRequest(message, UUID.randomUUID().toString());

        dialogflowApi.getResponse(CLIENT_ACCESS_TOKEN, request).enqueue(new Callback<DialogflowResponse>() {
            @Override
            public void onResponse(Call<DialogflowResponse> call, Response<DialogflowResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    String reply = response.body().getResult().getFulfillment().getSpeech();
                    chatMessages.add(new ChatMessage(reply, false));
                    chatAdapter.notifyDataSetChanged();
                    chatRecyclerView.scrollToPosition(chatMessages.size() - 1);
                } else {
                    showError("No response from chatbot");
                }
            }

            @Override
            public void onFailure(Call<DialogflowResponse> call, Throwable t) {
                showError("Failed to connect: " + t.getMessage());
            }
        });
    }

    private void showError(String message) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    }
}
