#4) შექმენით ფუნქცია რომელსაც არგუმენტად გადავცემთ სახელს შემდეგ კი ის გვესალმება hello name, გამოიძახეთ ფუნქცია რამდენჯერმე და გადაეცით არგუმენტად სხვადასხვა სახელები
def greet(name):
    """
    იღებს სახელს და გვესალმება "Hello, name" ფორმატით.
    :param name: მისალმებისთვის განკუთვნილი სახელი
    """
    print(f"Hello, {name}!")

# ფუნქციის გამოძახება სხვადასხვა სახელებისთვის
greet("Nika")
greet("Mari")
greet("Lasha")
greet("Tamar")