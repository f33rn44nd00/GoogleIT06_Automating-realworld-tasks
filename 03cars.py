#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = 0
  max_sales_car = ""
  car_years_dict = {}

  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    
    #handle max sales
    if item["total_sales"] > max_sales:
      max_sales = item["total_sales"]
      max_sales_car = format_car(item["car"])
      
    #handle most popular car_year
    if item["car"]["car_year"] in car_years_dict:
      car_years_dict[item["car"]["car_year"]] += item ["total_sales"]
    else:
      car_years_dict[item["car"]["car_year"]] = item["total_sales"]
    

  most_popular_year = "{}".format(max(car_years_dict, key=car_years_dict.get))
  summary = [
    "The {} generated the most revenue: ${}.".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),"The {} had the most sales: {}.".format(max_sales_car,max_sales), "The most popular year was {} with {} sales.".format(most_popular_year,car_years_dict[most_popular_year])
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  table_data = cars_dict_to_table(data)
  email_body = '\n'.join(summary)
  print(summary)
  
  #turn this into a PDF report
  reports.generate("/tmp/cars.pdf", "Sales summary for last month", email_body, table_data)

  #send the PDF report as an email attachment
  message = emails.generate("automation@example.com", "student-03-67e2f72d2304@example.com", "Sales summary for last month", email_body, "/tmp/cars.pdf")
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)