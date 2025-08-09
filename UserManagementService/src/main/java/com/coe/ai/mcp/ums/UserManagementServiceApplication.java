package com.coe.ai.mcp.ums;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.coe.ai.mcp.ums.service.UserService;

@SpringBootApplication
public class UserManagementServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(UserManagementServiceApplication.class, args);
	}
	@Bean
	public ToolCallbackProvider userServiceTools(){
		return MethodToolCallbackProvider.builder().toolObjects(new UserService()).build();
	}

}
