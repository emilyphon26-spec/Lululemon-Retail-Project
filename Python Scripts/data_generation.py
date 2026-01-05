import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

def generate_stores():
    """Generate stores data"""
    cities = [
        {'name': 'Vancouver', 'region': 'West'},
        {'name': 'Seattle', 'region': 'West'},
        {'name': 'Los Angeles', 'region': 'West'},
        {'name': 'San Francisco', 'region': 'West'},
        {'name': 'New York', 'region': 'East'},
        {'name': 'Boston', 'region': 'East'},
        {'name': 'Miami', 'region': 'East'},
        {'name': 'Chicago', 'region': 'Central'},
        {'name': 'Denver', 'region': 'Central'},
        {'name': 'Austin', 'region': 'Central'}
    ]
    
    stores = []
    for i, city in enumerate(cities, 1):
        stores.append({
            'store_id': i,
            'store_name': f"Lululemon {city['name']}",
            'region': city['region']
        })
    
    return pd.DataFrame(stores)

def generate_products():
    """Generate products data"""
    categories = {
        'Leggings': [
            {'name': 'Align High-Rise Pant', 'price': 98},
            {'name': 'Wunder Under High-Rise', 'price': 98},
            {'name': 'Fast and Free High-Rise', 'price': 128},
            {'name': 'Invigorate High-Rise', 'price': 118},
            {'name': 'Train Times Pant', 'price': 98},
            {'name': 'Pace Rival Skirt', 'price': 68},
            {'name': 'All The Right Places Pant', 'price': 118},
            {'name': 'Align Jogger', 'price': 118},
            {'name': 'Dance Studio Pant', 'price': 108},
            {'name': 'On The Fly Pant', 'price': 98}
        ],
        'Tops': [
            {'name': 'Swiftly Tech Long Sleeve', 'price': 68},
            {'name': 'Define Jacket', 'price': 118},
            {'name': 'Scuba Hoodie', 'price': 118},
            {'name': 'Energy Bra', 'price': 52},
            {'name': 'Align Tank', 'price': 58},
            {'name': 'Back In Action Long Sleeve', 'price': 78},
            {'name': 'Swiftly Tech Short Sleeve', 'price': 58},
            {'name': 'Cool Racerback', 'price': 48},
            {'name': 'Flow Y Bra', 'price': 52},
            {'name': 'Free To Be Serene Bra', 'price': 52}
        ],
        'Shorts': [
            {'name': 'Hotty Hot Short', 'price': 58},
            {'name': 'Speed Up Short', 'price': 58},
            {'name': 'Track That Short', 'price': 58},
            {'name': 'Align Short', 'price': 58},
            {'name': 'Find Your Pace Short', 'price': 68},
            {'name': 'Fast and Free Short', 'price': 68},
            {'name': 'Pace Breaker Short', 'price': 68},
            {'name': 'T.H.E. Short', 'price': 68},
            {'name': 'License To Train Short', 'price': 68},
            {'name': 'Surge Short', 'price': 68}
        ],
        'Accessories': [
            {'name': 'Reversible Mat', 'price': 78},
            {'name': 'The Towel', 'price': 38},
            {'name': 'Loop It Up Mat Strap', 'price': 18},
            {'name': 'Everywhere Belt Bag', 'price': 38},
            {'name': 'Fast and Free Run Hat', 'price': 38},
            {'name': 'Light Locks Scrunchie', 'price': 18},
            {'name': 'Festival Bag', 'price': 68},
            {'name': 'City Adventurer Backpack', 'price': 98},
            {'name': 'On My Level Bag', 'price': 88},
            {'name': 'Go Lightly Backpack', 'price': 58}
        ],
        'Outerwear': [
            {'name': 'Down For It All Jacket', 'price': 228},
            {'name': 'Another Mile Jacket', 'price': 148},
            {'name': 'Always Effortless Jacket', 'price': 128},
            {'name': 'Rain Rebel Jacket', 'price': 148},
            {'name': 'Glyde Along Softshell', 'price': 168},
            {'name': 'Pack It Up Jacket', 'price': 128},
            {'name': 'Nulu Cropped Define Jacket', 'price': 128},
            {'name': 'Hooded Define Jacket', 'price': 138},
            {'name': 'Wunder Puff Jacket', 'price': 248},
            {'name': 'Always There Vest', 'price': 108}
        ]
    }
    
    products = []
    product_id = 1
    
    for category, items in categories.items():
        for item in items:
            products.append({
                'product_id': product_id,
                'product_name': item['name'],
                'category': category,
                'base_price': item['price']
            })
            product_id += 1
    
    return pd.DataFrame(products)

def generate_promotions(products_df):
    """Generate promotions data"""
    promotions = []
    promo_id = 1
    discounts = [10, 20, 30]
    
    # Generate promotions throughout the year
    for month in range(12):
        # 3-5 promotions per month
        num_promos = random.randint(3, 5)
        
        for _ in range(num_promos):
            product = products_df.sample(1).iloc[0]
            discount = random.choice(discounts)
            
            # Random start date within the month
            promo_start = datetime(2024, month + 1, random.randint(1, 28))
            # Duration between 7-21 days
            duration = random.randint(7, 21)
            promo_end = promo_start + timedelta(days=duration)
            
            promotions.append({
                'promo_id': promo_id,
                'product_id': product['product_id'],
                'discount_pct': discount,
                'start_date': promo_start.strftime('%Y-%m-%d'),
                'end_date': promo_end.strftime('%Y-%m-%d')
            })
            promo_id += 1
    
    return pd.DataFrame(promotions)

def generate_transactions(stores_df, products_df, promotions_df):
    """Generate transactions with realistic patterns"""
    transactions = []
    txn_id = 1
    
    # Create promotion lookup
    promo_lookup = {}
    for _, promo in promotions_df.iterrows():
        start = datetime.strptime(promo['start_date'], '%Y-%m-%d')
        end = datetime.strptime(promo['end_date'], '%Y-%m-%d')
        
        current = start
        while current <= end:
            date_key = current.strftime('%Y-%m-%d')
            if date_key not in promo_lookup:
                promo_lookup[date_key] = {}
            promo_lookup[date_key][promo['product_id']] = promo
            current += timedelta(days=1)
    
    # Category weights for product selection
    category_weights = {
        'Leggings': 0.35,
        'Tops': 0.30,
        'Shorts': 0.15,
        'Accessories': 0.12,
        'Outerwear': 0.08
    }
    
    # Generate transactions for each day
    start_date = datetime(2024, 1, 1)
    
    print("Generating transactions...")
    for day in range(365):
        if day % 50 == 0:
            print(f"Progress: {day}/365 days")
        
        current_date = start_date + timedelta(days=day)
        date_str = current_date.strftime('%Y-%m-%d')
        day_of_week = current_date.weekday()
        
        # Weekend boost (Saturday=5, Sunday=6)
        weekend_multiplier = 1.4 if day_of_week in [5, 6] else 1.0
        
        # Seasonal patterns (summer boost)
        month = current_date.month
        seasonal_multiplier = 1.2 if 5 <= month <= 8 else 1.0
        
        # Generate transactions for each store
        for _, store in stores_df.iterrows():
            # Base traffic per store per day
            store_traffic = random.randint(15, 30)
            num_txns = int(store_traffic * weekend_multiplier * seasonal_multiplier * 
                          random.uniform(0.8, 1.2))
            
            for _ in range(num_txns):
                # Select product based on category weights
                rand = random.random()
                cumulative = 0
                selected_product = None
                
                for category, weight in category_weights.items():
                    cumulative += weight
                    if rand < cumulative:
                        cat_products = products_df[products_df['category'] == category]
                        selected_product = cat_products.sample(1).iloc[0]
                        break
                
                if selected_product is None:
                    selected_product = products_df.sample(1).iloc[0]
                
                # Check for promotion
                promo = promo_lookup.get(date_str, {}).get(selected_product['product_id'])
                
                # Quantity (base: 1, 15% chance of 2)
                quantity = 2 if random.random() < 0.15 else 1
                
                # Promotion boost
                if promo is not None:
                    promo_boost = 1.0 + (promo['discount_pct'] / 100) * 2.5
                    # Increase chance of multiple items during promotion
                    if random.random() < 0.25:
                        quantity += 1
                else:
                    promo_boost = 1.0
                
                # Only create transaction if it passes probability check
                if random.random() < promo_boost / (promo_boost + 0.5):
                    base_price = selected_product['base_price']
                    discount = promo['discount_pct'] / 100 if promo is not None else 0
                    price_paid = round(base_price * (1 - discount), 2)
                    
                    transactions.append({
                        'transaction_id': txn_id,
                        'date': date_str,
                        'store_id': store['store_id'],
                        'product_id': selected_product['product_id'],
                        'quantity': quantity,
                        'price_paid': price_paid
                    })
                    txn_id += 1
    
    print(f"Generated {len(transactions)} transactions")
    return pd.DataFrame(transactions)

def main():
    """Main function to generate all datasets and save as CSV"""
    print("="*60)
    print("Lululemon Retail Dataset Generator")
    print("="*60)
    
    # Generate all datasets
    print("\n1. Generating stores...")
    stores_df = generate_stores()
    print(f"   Created {len(stores_df)} stores")
    
    print("\n2. Generating products...")
    products_df = generate_products()
    print(f"   Created {len(products_df)} products")
    
    print("\n3. Generating promotions...")
    promotions_df = generate_promotions(products_df)
    print(f"   Created {len(promotions_df)} promotions")
    
    print("\n4. Generating transactions (this may take a minute)...")
    transactions_df = generate_transactions(stores_df, products_df, promotions_df)
    
    # Save to CSV files
    print("\n5. Saving CSV files...")
    stores_df.to_csv('stores.csv', index=False)
    print("   ✓ stores.csv")
    
    products_df.to_csv('products.csv', index=False)
    print("   ✓ products.csv")
    
    promotions_df.to_csv('promotions.csv', index=False)
    print("   ✓ promotions.csv")
    
    transactions_df.to_csv('transactions.csv', index=False)
    print("   ✓ transactions.csv")
    
    # Summary statistics
    print("\n" + "="*60)
    print("DATASET SUMMARY")
    print("="*60)
    print(f"Stores:          {len(stores_df)}")
    print(f"Products:        {len(products_df)}")
    print(f"Promotions:      {len(promotions_df)}")
    print(f"Transactions:    {len(transactions_df):,}")
    print(f"Date Range:      2024-01-01 to 2024-12-31")
    print(f"Total Revenue:   ${transactions_df['price_paid'].sum() * transactions_df['quantity'].sum():,.2f}")
    print("="*60)
    
    # Quick data preview
    print("\nSample Transaction Data:")
    print(transactions_df.head(10))
    
    print("\n✓ All CSV files generated successfully!")

if __name__ == "__main__":
    main()