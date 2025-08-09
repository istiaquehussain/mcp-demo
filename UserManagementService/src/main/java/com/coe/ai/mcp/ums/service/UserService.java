package com.coe.ai.mcp.ums.service;

import java.util.List;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

import com.coe.ai.mcp.ums.model.User;


@Service
public class UserService {

    List<User> users=List.of(
            new User("user1", "John", "Doe", "john@gmail.com"),
            new User("user2", "Jane", "Smith", "jane@gmai.com"),
            new User("user3", "Alice", "Johnson", "alice@gmail.com"),
            new User("user4", "Bob", "Brown", "brown@gmail.com"),
            new User("user5", "Charlie", "Davis", "chrales@gmail.com")
        );

    @Tool(name = "getUserIdForFirstName", description = "Retrieves user id for a given user first name")
    public String getUserIdForFirstName(String firstName) {
        // Logic to retrieve user ID from first name
        if (users == null || users.isEmpty()) {
            return "";
        }
        User user = users.stream().filter(u -> u.getFirstName().equalsIgnoreCase(firstName)).findFirst().orElse(null);
        if (user == null) {
            return "";
        }
        return user.getUserId();
        
    }

    @Tool(name = "getUserIdForLastName", description = "Retrieves user id for a given user last name")
    public String getUserIdForLastName(String lastName) {
        if (users == null || users.isEmpty()) {
            return "";
        }
        User user = users.stream().filter(u -> u.getLastName().equalsIgnoreCase(lastName)).findFirst().orElse(null);
        if (user == null) {
            return "";
        }
        return user.getUserId();
    }

    @Tool(name = "getUserIdForEmail", description = "Retrieves user id for a given user email address or email id")
    public String getUserIdForEmail(String email) {
        if (users == null || users.isEmpty()) {
            return "";
        }
        User user = users.stream().filter(u -> u.getEmail().equalsIgnoreCase(email)).findFirst().orElse(null);
        if (user == null) {
            return "";
        }
        return user.getUserId();
    }
    
    @Tool(name = "getEmailForUserId", description = "Retrieves user email address for a given user id")
    public String getEmailForUserId(String userId) {
        if (users == null || users.isEmpty()) {
            return "";
        }
        User user = users.stream().filter(u -> u.getUserId().equalsIgnoreCase(userId)).findFirst().orElse(null);
        if (user == null) {
            return "";
        }
        return user.getEmail();
    }
}
