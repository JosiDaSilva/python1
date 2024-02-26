class Empleado:
    def __init__(self, dni, nombre, apellido, año_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.año_ingreso = año_ingreso

    def calcular_salario(self):
        pass

class EmpleadoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, año_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, año_ingreso)
        self.sueldo_basico = sueldo_basico

    def calcular_salario(self):
        años_en_empresa = 2024 - self.año_ingreso
        porcentaje_adicional = 0
        if años_en_empresa >= 2 and años_en_empresa <= 5:
            porcentaje_adicional = 0.05
        elif años_en_empresa > 5:
            porcentaje_adicional = 0.1
        return self.sueldo_basico * (1 + porcentaje_adicional)

class EmpleadoAComision(Empleado):
    def __init__(self, dni, nombre, apellido, año_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, año_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        return max(salario, self.salario_minimo)

def mostrarSalarios(empleados):
    for empleado in empleados:
        salario = empleado.calcular_salario()
        print(f"{empleado.nombre} {empleado.apellido}: ${salario:.2f}")

# Creación de 10 empleados de ejemplo
empleados = [
    EmpleadoFijo("12345678", "Clark", "kent", 2018, 200000),
    EmpleadoFijo("23456789", "loisa", "lane", 2020, 180000),
    EmpleadoFijo("34567890", "jimmy", "olsen", 2019, 220000),
    EmpleadoFijo("45678901", "lana", "lang", 2017, 250000),
    EmpleadoFijo("56789012", "Perry", "white", 2016, 190000),
    EmpleadoAComision("67890123", "sam", "foswell", 2021, 150000, 10, 50000),
    EmpleadoAComision("78901234", "franklin", "Stern", 2023, 1200, 8, 60000),
    EmpleadoAComision("89012345", "cat", "grant", 2022, 1300, 12, 55000),
    EmpleadoAComision("90123456", "Janice", "denton", 2020, 1400, 15, 45000),
    EmpleadoAComision("01234567", "brad", "hunter", 2019, 1600, 20, 40000)
]

mostrarSalarios(empleados)







def empleadoConMasClientes(empleados):
    max_clientes = 0
    empleado_max_clientes = None
    for empleado in empleados:
        if isinstance(empleado, EmpleadoAComision):
            if empleado.clientes_captados > max_clientes:
                max_clientes = empleado.clientes_captados
                empleado_max_clientes = empleado
    return empleado_max_clientes

empleado = empleadoConMasClientes(empleados)
print(f"El empleado con más clientes captados es {empleado.nombre} {empleado.apellido} con {empleado.clientes_captados} clientes.")
