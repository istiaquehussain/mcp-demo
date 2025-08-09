package com.coe.ai.mcp.oms;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.coe.ai.mcp.oms.service.OrderService;

@SpringBootApplication
public class OrderManagementServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(OrderManagementServiceApplication.class, args);
	}

	@Bean
	public ToolCallbackProvider orderServiceTools(){
		return MethodToolCallbackProvider.builder().toolObjects(new OrderService()).build();
	}

}
