package com.example.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jms.core.JmsTemplate;

import org.springframework.stereotype.Component;

@Component
public class MessageService {
    @JmsListener(destination = "exampleQueue")
    public void receiveMessage(String message) {
        System.out.println("Received message: " + message);
    }
}

/*
 * private final JmsTemplate jmsTemplate;
 * 
 * @Autowired
 * public MessageService(JmsTemplate jmsTemplate) {
 * this.jmsTemplate = jmsTemplate;
 * }
 * 
 * public void sendMessage(String message) {
 * jmsTemplate.convertAndSend("yourQueueName", message);
 * }
 * 
 */
