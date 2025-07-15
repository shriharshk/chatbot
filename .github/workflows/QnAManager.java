package com.example.chatbot;

import java.util.HashMap;
import java.util.Map;

public class QnAManager {
    private Map<String, String> qnaMap = new HashMap<>();

    public QnAManager() {
        qnaMap.put("what is your name", "I'm a simple Q&A bot.");
        qnaMap.put("how do i use this app", "Type a question and tap Send.");
        qnaMap.put("what is 1+1", "1 + 1 equals 2.");
    }

    public String getAnswer(String question) {
        if (question == null) return "";
        String key = question.trim().toLowerCase();
        if (qnaMap.containsKey(key)) {
            return qnaMap.get(key);
        }
        return "I don't have an answer for that.";
    }
}
