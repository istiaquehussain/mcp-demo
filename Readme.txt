This project is setup for a demo of MCP. It includes sample implementation of 
1. Spring based MCP server UserManagementService 
2. Spring based MCP server OrderManagementService
3. Python based MCP server email-service
4. Python base MCP client 

-------------------------UserManagementService-----------------------------------------
This provides a sample spring based MCP server implemetaion . The source path location ./UserManagementService. 
It provides 4 functions (In MCP world they are called tools)

1. getUserIdForFirstName(String firstName) // Retrieves user id for a given user first name
2. getUserIdForLastName(String lastName) //Retrieves user id for a given user last name
3. getUserIdForEmail(String email)  // Retrieves user id for a given user email address or email id
4. getEmailForUserId(String userId)  // Retrieves user email address for a given user id

Sample user records serves by UserManagementService

("user1", "John", "Doe", "john@gmail.com"),
("user2", "Jane", "Smith", "jane@gmai.com"),
("user3", "Alice", "Johnson", "alice@gmail.com"),
("user4", "Bob", "Brown", "brown@gmail.com"),
("user5", "Charlie", "Davis", "chrales@gmail.com")



-------------------------OrderManagementService-----------------------------------------
This provides a sample spring based MCP server implemetaion . The source path location ./OrderManagementService. 
It provides 2 tools

1. getAllOrdersForUserId(String userId) // Retrieves all orders for a given user ID
2. getOrderDetailsForOrderId(String orderId) //Retrieves order details for a given order ID

Sample order records serves by UserManagementService

("ORD-001", "user1", "MACBook Pro 16-inch 2023 , M2 Pro, 12-Core CPU, 19-Core GPU, 16GB RAM, 1TB SSD"),
("ORD-002", "user1", "iPhone 15 Pro Max, 256GB, Space Black"),
("ORD-003", "user2", "Samsung Galaxy S23 Ultra, 512GB, Phantom Black"),
("ORD-004", "user2", "Sony WH-1000XM5 Wireless Noise Cancelling Headphones"),
("ORD-005", "user3", "Dell XPS 13, 13.4-inch FHD+ Touchscreen, Intel Core i7, 16GB RAM, 512GB SSD"),
("ORD-006", "user3", "Apple Watch Series 8, 45mm, GPS + Cellular, Midnight Aluminum Case with Midnight Sport Band"),
("ORD-007", "user4", "Google Pixel 7 Pro, 128GB, Obsidian"),
("ORD-008", "user4", "Bose QuietComfort 45 Wireless Noise Cancelling Headphones"),
("ORD-009", "user5", "Lenovo ThinkPad X1 Carbon Gen 10, 14-inch FHD, Intel Core i7, 16GB RAM, 1TB SSD"),
("ORD-0010", "user5", "Amazon Kindle Paperwhite, 11th Gen, Waterproof, 8GB Storage")

-------------------------email-service-----------------------------------------
This provides a sample Python MCP server implemetaion . The source path location ./email-service. 
It provides 1 tool

send_email(toEmailAddress: str, orderDeatils: str) // Sends an email with the specified ordersDetails to the given recipient email address


----------------Steps to run servers and client ----------------------
1. Sofrware requiremnts 
  - java 24 (if others say v 21 you need to update the ./UserManagementService/pom.xml and ./OrderManagementService/pom.xml in project->properties->java.version value)
  - maven      
  - Python 3.13 +
  - optional Node js to run universal mcp inspector
2. run OrderManagementService
    - open terminal 
    - cd ./OrderManagementService
    - ./mvnw spring-boot:run
3. run UserManagementService
    - open terminal 
    - cd ./UserManagementService
    - ./mvnw spring-boot:run
4. run mcp service in python 
    - cd ./email-service
    - python3 -m venv .venv
    - source ./.venv/bin/activate
    - pip3 install -r requiments.txt 
    - python3 ./email_service.py
5. (optional) test MCP Servers using universal MCP inspector
    - install npx using Node
    - npx @modelcontextprotocol/inspector
    - testing urls 
        a. order-service: protocol - SSE
        http://localhost:8070/os/api/v1/mcp/sse
        b. user-service: protocol - SSE
        http://localhost:8090/us/api/v1/mcp/sse
        c. email-service: protocol - streamable HTTP
        http://localhost:8000/mcp
6. run and test client 
   Note : In order to test the fucntionalityly without any cost We are using xxx model though groq intefencing . Please loging to https://groq.com/ and generate a API key 
   - cd ./client
   - edit .env file to replace with your GROQ API KEY
   - python3 -m venv .venv
   - source ./.venv/bin/activate
   - pip3 install -r requiments.txt
   - streamlit run ./chat_app.py
        





 




------------------------------------------------------------------
To test mcp server use
npx @modelcontextprotocol/inspector
Note: if npx does not run in your machine please install npx using Node e.g . "brew install Node" 
------------------------------------------------------------------

------------------------------------------------------------------
urls for mcp server 

1. order-service:
http://localhost:8070/os/api/v1/mcp/sse

2. user-service
http://localhost:8090/us/api/v1/mcp/sse

3. email-service
http://localhost:8000/mcp

update client/mcpserver_config.json file if you change any of this config files
------------------------------------------------------------------

------------------------------------------------------------------
to run mcp service in spring boot 
cd ./OrderManagementService
./mvnw spring-boot:run

cd ./UserManagementService
./mvnw spring-boot:run

to run mcp service in python 
cd ./email-service
source ./.venv/bin/activate
python ./email_service.py 
        OR
uv run ./email_service.py 

to run client application 
cd ./client
source ./.venv/bin/activate
streamlit run ./chat_app.py 
------------------------------------------------------------------

------------------------------------------------------------------
user records 
("user1", "John", "Doe", "john@gmail.com"),
("user2", "Jane", "Smith", "jane@gmai.com"),
("user3", "Alice", "Johnson", "alice@gmail.com"),
("user4", "Bob", "Brown", "brown@gmail.com"),
("user5", "Charlie", "Davis", "chrales@gmail.com")

order records
("ORD-001", "user1", "MACBook Pro 16-inch 2023 , M2 Pro, 12-Core CPU, 19-Core GPU, 16GB RAM, 1TB SSD"),
("ORD-002", "user1", "iPhone 15 Pro Max, 256GB, Space Black"),
("ORD-003", "user2", "Samsung Galaxy S23 Ultra, 512GB, Phantom Black"),
("ORD-004", "user2", "Sony WH-1000XM5 Wireless Noise Cancelling Headphones"),
("ORD-005", "user3", "Dell XPS 13, 13.4-inch FHD+ Touchscreen, Intel Core i7, 16GB RAM, 512GB SSD"),
("ORD-006", "user3", "Apple Watch Series 8, 45mm, GPS + Cellular, Midnight Aluminum Case with Midnight Sport Band"),
("ORD-007", "user4", "Google Pixel 7 Pro, 128GB, Obsidian"),
("ORD-008", "user4", "Bose QuietComfort 45 Wireless Noise Cancelling Headphones"),
("ORD-009", "user5", "Lenovo ThinkPad X1 Carbon Gen 10, 14-inch FHD, Intel Core i7, 16GB RAM, 1TB SSD"),
("ORD-0010", "user5", "Amazon Kindle Paperwhite, 11th Gen, Waterproof, 8GB Storage")

------------------------------------------------------------------
important example 

my first name is John, what is my use id

for user id user2 list all orders 

can you show deatils for order ORD-007

my first name is Bob can you list all orders 

can you email order details for user id user5
can you email details for first name Alice

        
