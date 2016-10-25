#!/usr/bin/python


def main():
  # Creating the data
  description = {"name": ("string", "Name"),
                 "salary": ("number", "Salary"),
                 "full_time": ("boolean", "Full Time Employee")}
  data = [{"name": "Mike", "salary": (10000, "$10,000"), "full_time": True},
          {"name": "Jim", "salary": (800, "$800"), "full_time": False},
          {"name": "Alice", "salary": (12500, "$12,500"), "full_time": True},
          {"name": "Bob", "salary": (7000, "$7,000"), "full_time": True}]

  # Loading it into gviz_api.DataTable
  data_table = gviz_api.DataTable(description)
  data_table.LoadData(data)

  # Create a JavaScript code string.
  jscode = data_table.ToJSCode("jscode_data",
                               columns_order=("username", "timestamp"),
                               order_by="timestamp")
  # Create a JSON string.
  json = data_table.ToJSon(columns_order=("username", "timestamp"),
                           order_by="timestamp")

  # Put the JS code and JSON string into the template.
  print "Content-type: text/html"
  print
  print page_template % vars()


if __name__ == '__main__':
  main()