// README.md
# Electronics Retail App

This is a minimal 3-tier architecture application with frontend, multiple APIs, and database schema.

## APIs
- ProductAPI: /api/products
- CustomerAPI: /api/customers
- OrdersAPI: /api/orders

## Frontend
Open frontend/index.html in browser to interact with ProductAPI, CustomerAPI, and OrdersAPI.

## Database
Run schema.sql in your preferred SQL database engine to set up tables.

## Deployment
Use ARM templates in arm-templates/ to provision Azure infrastructure:

```bash
az group create --name retail-rg --location eastus
az deployment group create --resource-group retail-rg --template-file arm-templates/mainTemplate.json --parameters @arm-templates/parameters.json
```
