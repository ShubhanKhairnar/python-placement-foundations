import csv

def process_transactions(input_file, output_file):
    total_successful_amount = 0.0
    
    print("--- Processing Transactions ---")
    
    # 1. READ AND CALCULATE
    try:
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                transaction_id = row.get('transaction_id', 'Unknown')
                amount_str = row.get('amount', '').strip()
                status = row.get('status', '').strip().lower()
                
                # Only process successful transactions
                if status == 'success':
                    try:
                        # Try to convert string to float
                        amount = float(amount_str)
                        total_successful_amount += amount
                    except ValueError:
                        # Handle malformed or empty strings gracefully
                        print(f"[WARNING] Malformed amount in transaction {transaction_id}: '{amount_str}'. Skipping.")
                        
    except FileNotFoundError:
        print(f"[ERROR] Could not find {input_file}. Please check the path.")
        return

    # 2. EXPORT TO SUMMARY CSV
    try:
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['status', 'total_amount']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerow({
                'status': 'success_summary',
                'total_amount': round(total_successful_amount, 2)
            })
            
        print(f"\n[SUCCESS] Summary written to {output_file}")
        print(f"Total Successful Amount: ${round(total_successful_amount, 2)}")
        
    except Exception as e:
        print(f"[ERROR] Failed to write to {output_file}: {e}")

if __name__ == "__main__":
    process_transactions('transactions.csv', 'summary.csv')