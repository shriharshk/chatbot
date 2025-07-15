public interface DialogflowApi {
    @POST("query?v=20150910")
    Call<DialogflowResponse> getResponse(
        @Header("Authorization") String authToken,
        @Body DialogflowRequest request
    );
}
