------------------------------------------------------------------
To test mcp server use
npx @modelcontextprotocol/inspector
Note: if npx does not run in your machine please install npx using Node e.g . "brew install Node" 
------------------------------------------------------------------

------------------------------------------------------------------
urs for mcp server 

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

        