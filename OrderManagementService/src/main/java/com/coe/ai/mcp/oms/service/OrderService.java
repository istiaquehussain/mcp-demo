package com.coe.ai.mcp.oms.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

import com.coe.ai.mcp.oms.model.Order;


@Service
public class OrderService {
    
    List<Order> orders=List.of(
            new Order("ORD-001", "user1", "MACBook Pro 16-inch 2023 , M2 Pro, 12-Core CPU, 19-Core GPU, 16GB RAM, 1TB SSD"),
            new Order("ORD-002", "user1", "iPhone 15 Pro Max, 256GB, Space Black"),
            new Order("ORD-003", "user2", "Samsung Galaxy S23 Ultra, 512GB, Phantom Black"),
            new Order("ORD-004", "user2", "Sony WH-1000XM5 Wireless Noise Cancelling Headphones"),
            new Order("ORD-005", "user3", "Dell XPS 13, 13.4-inch FHD+ Touchscreen, Intel Core i7, 16GB RAM, 512GB SSD"),
            new Order("ORD-006", "user3", "Apple Watch Series 8, 45mm, GPS + Cellular, Midnight Aluminum Case with Midnight Sport Band"),
            new Order("ORD-007", "user4", "Google Pixel 7 Pro, 128GB, Obsidian"),
            new Order("ORD-008", "user4", "Bose QuietComfort 45 Wireless Noise Cancelling Headphones"),
            new Order("ORD-009", "user5", "Lenovo ThinkPad X1 Carbon Gen 10, 14-inch FHD, Intel Core i7, 16GB RAM, 1TB SSD"),
            new Order("ORD-0010", "user5", "Amazon Kindle Paperwhite, 11th Gen, Waterproof, 8GB Storage")
        );

    @Tool(name = "getAllOrdersForUserId", description = "Retrieves all orders for a given user ID")
    String getAllOrdersForUserId(String userId) {
        if (orders == null || orders.isEmpty()) {
            return "No orders found for user ID: " + userId;
        }
         List<String>  allOrders = orders.stream().filter(order-> order.getUserId().equalsIgnoreCase(userId)).map(order->order.toString()).toList();
        
         if (allOrders == null || allOrders.isEmpty()) {
            return "No orders found for user ID: " + userId;
        }
         return allOrders.stream().filter(order-> order!=null && !order.isEmpty()).collect(Collectors.joining("\n", "", ""));
    }

    @Tool(name = "getOrderDetailsForOrderId", description = "Retrieves order details for a given order ID")
    String getOrderDetailsForOrderId(String orderId) {
        // Logic to retrieve order details for the given order ID
        if (orders == null || orders.isEmpty()) {
            return "No orders found for order ID: " + orderId;
        }
        Order order = orders.stream().filter(o -> o.getOrderId().equalsIgnoreCase(orderId)).findFirst().orElse(null);
        if (order == null) {
            return "Order not found for order ID: " + orderId;
        }
        return order.toString();
    }
    
}
