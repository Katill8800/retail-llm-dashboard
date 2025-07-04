# Retail Chain Dashboard with LLM Querying

This project analyzes Supermart grocery retail store performance using Python, Streamlit, and LLMs.

## 🗃️ Dataset Attributes (simulated fields included)
- `order_id`, `customer_name`, `category`, `sub_category`, `city`, `state`, `region`
- `order_date`, `dispatch_date`, `sales`, `discount`, `profit`
- `store_id`, `store_name`, `product_id`

## 🧰 Components
1. **retail_data_pipeline.py** – Cleans and enriches data with simulated fields.
2. **dashboard_app.py** – Interactive dashboard via Streamlit.
3. **llm_query.py** – Natural language Q&A over retail dataset.

## 🚀 Instructions
1. Place original CSV under `data/` folder.
2. Run preprocessing:
```bash
python retail_data_pipeline.py
```
3. Launch dashboard:
```bash
streamlit run dashboard_app.py
```
4. Try querying data:
```bash
python llm_query.py
```

---

## 💬 Sample Queries to Ask the LLM
- "Top 5 cities by total sales"
- "Which region had the lowest average discount?"
- "What is the average profit per sub-category?"
- "List store names with revenue above $10,000"

Enjoy real-time insights powered by Python + AI! 🚀
