
import csv
import math
from datetime import datetime

def main():
    KEY_COLUMN_INDEX = 0
    try:
        products_dict = read_dictionary("products.csv", KEY_COLUMN_INDEX)
    except FileNotFoundError:
        print("Error: The file 'products.csv' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    print()
    shop_name = "Kaakyire and Mom's ventures"
    print(shop_name)
    num_of_items = 0
    subtotal = 0
    accumulated_discount = 0

    try:
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            print()
            for line in reader:
                product_num = line[0]
                ordered_qty = int(line[1])
                try:
                    product_name = products_dict[product_num][1]
                    price = float(products_dict[product_num][2])
                except KeyError:
                    print(f"Error: Product number '{product_num}' was not found in the products dictionary.")
                    continue

                print(f"{product_name}: {ordered_qty} @ ${price}")
                num_of_items += ordered_qty
                subtotal += ordered_qty * price
                if product_num == "D083" and ordered_qty > 1:
                    item_discountable = math.floor(ordered_qty / 2)
                    buy_two_get_one_half = (item_discountable * price) * 0.5
                    accumulated_discount += buy_two_get_one_half
    except FileNotFoundError:
        print("Error: The file 'request.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        current_date = datetime.now()
        formatted_date = current_date.strftime("%a %b %e %H:%M:%S %Y")
        today = datetime.today()
        new_year_sale = datetime(today.year + 1, 1, 1)
        days_until_sale = (new_year_sale - today).days

        print(f"Number of Items: {num_of_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print(f"Discounted Price: {accumulated_discount}")
        print(f"Thank you for shopping at the {shop_name}.")
        print(formatted_date)
        print(f"There are {days_until_sale} days until the New Year's sale begins.")
        print()

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.

    Return: a compound dictionary that contains the contents of the CSV file.
    """
    products_dict = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    products_dict[key] = row_list
    except Exception as e:
        print(f"An error occurred: {e}")
    return products_dict

if __name__ == "__main__":

    main()
    
