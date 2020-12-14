# Termformat

The package allows you to format terminal output:

- background color
- foreground color
- bold
- dim

Example:

    f = Formatter()
    print(f('Hello World!').bg('#fff').fg('#FAA500').bold().bake())

More details:

To apply formatting use a chain notation:

    f('Hello World!').bg('#fff').dim(). ...

To complete formatting ang get a string to print use `bake()`:

    result = f('Hello World!').bg('#fff').bake()
    print(result)
