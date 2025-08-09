package com.coe.ai.mcp.oms.model;

public class Order {
    private String orderId;
    private String userId;
    private String orderDetails;

    public Order(String orderId, String userId, String orderDetails) {
        this.orderId = orderId;
        this.userId = userId;
        this.orderDetails = orderDetails;
    }

    public String getOrderId() {
        return orderId;
    }

    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getOrderDetails() {
        return orderDetails;
    }

    public void setOrderDetails(String orderDetails) {
        this.orderDetails = orderDetails;
    }

    @Override
    public String toString() {
        return " ID -> " + orderId + ", Details -> " + orderDetails+"\n\n";
    }


}
