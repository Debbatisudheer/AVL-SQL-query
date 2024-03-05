from tabulate import tabulate

class Employee:
    def __init__(self, id, name, age, email, area, country):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.area = area
        self.country = country

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Email: {self.email}, Area: {self.area}, Country: {self.country}"


class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def search_by_age(self, age):
        return self._search_by_age(self.root, age)

    def _search_by_age(self, node, age):
        if node is None:
            return None
        if node.value.age == age:
            return node.value
        elif age < node.value.age:
            return self._search_by_age(node.left, age)
        else:
            return self._search_by_age(node.right, age)

    def search_by_id(self, id):
        return self._search_by_id(self.root, id)

    def _search_by_id(self, node, id):
        if node is None:
            return None
        if node.value.id == id:
            return node.value
        elif id < node.value.id:
            return self._search_by_id(node.left, id)
        else:
            return self._search_by_id(node.right, id)


class Database:
    def __init__(self):
        self.employee_table = []
        self.id_index = AVLTree()

    def insert_employee(self, employee):
        self.employee_table.append(employee)
        self.id_index.insert(employee.id, employee)

    def execute_query(self, sql_query):
        if sql_query == "SELECT * FROM employees":
            return [[employee.id, employee.name, employee.age, employee.email, employee.area, employee.country]
                    for employee in self.employee_table]
        elif sql_query.startswith("SELECT * FROM employees WHERE id = "):
            try:
                id = int(sql_query.split("id = ")[1])
                employee = self.id_index.search_by_id(id)
                if employee:
                    return [[employee.id, employee.name, employee.age, employee.email, employee.area, employee.country]]
                else:
                    return "No employee found with the specified ID."
            except ValueError:
                return "Invalid ID specified in the query."
        else:
            return "Invalid SQL query"


# Create an instance of the database
db = Database()

# Insert some sample employees into the database
db.insert_employee(Employee(1, "Alice", 30, "alice@example.com", "Area1", "Country1"))
db.insert_employee(Employee(2, "Bob", 35, "bob@example.com", "Area2", "Country2"))
db.insert_employee(Employee(3, "Charlie", 28, "charlie@example.com", "Area3", "Country3"))
db.insert_employee(Employee(4, "David", 40, "david@example.com", "Area4", "Country4"))

# Interface for the user to enter SQL-like queries
while True:
    query = input("Enter an SQL-like query (e.g., SELECT * FROM employees): ")
    if query.lower() == "exit":
        break
    result = db.execute_query(query)
    print("Query Result:")
    if isinstance(result, str):
        print(result)
    else:
        headers = ["ID", "Name", "Age", "Email", "Area", "Country"]
        print(tabulate(result, headers=headers, tablefmt="grid"))