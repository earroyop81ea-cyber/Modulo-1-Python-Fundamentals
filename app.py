import streamlit as st
import pandas as pd
import numpy as np

# --- Sección Home ---
def home():
    st.title("Proyecto Aplicado en Streamlit – Python Fundamentals")
    st.image("logo.png", width=120)
    st.write("Estudiante: Enrique Arroyo")
    st.write("Módulo 1: Python Fundamentals")
    st.subheader("Especialización en Python for Analytics")
    st.write("Año: 2026")
    st.markdown("Este proyecto integra conceptos de programación en Python aplicados en Streamlit.")
    st.markdown("**Tecnologías utilizadas:** Python, NumPy, Pandas, Streamlit")
    

# --- Ejercicio 1: Flujo de Caja con Listas ---
def ejercicio1():
    st.header("Ejercicio 1 – Flujo de Caja con Listas")
    st.markdown("Registrar movimientos financieros y calcular flujo de caja.")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=0.1)

    if st.button("Agregar movimiento"):
        st.session_state.movimientos.append({"concepto": concepto, "tipo": tipo, "valor": valor})
        st.success("Movimiento agregado")

    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df)

        ingresos = df[df["tipo"] == "Ingreso"]["valor"].sum()
        gastos = df[df["tipo"] == "Gasto"]["valor"].sum()
        saldo = ingresos - gastos

        st.metric("Ingresos", ingresos)
        st.metric("Gastos", gastos)
        st.metric("Saldo", saldo)

        if saldo >= 0:
            st.success("Flujo de caja a favor")
        else:
            st.error("Flujo de caja en contra")

# --- Ejercicio 2: Registro con NumPy y DataFrame ---
def ejercicio2():
    st.header("Ejercicio 2 – Registro con NumPy y DataFrame")
    st.markdown("Registrar productos y mostrar tabla con NumPy y Pandas.")

    if "productos" not in st.session_state:
        st.session_state.productos = []

    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Alimentos", "Electrónica", "Otros"])
    precio = st.number_input("Precio", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=1)

    if st.button("Agregar producto"):
        total = precio * cantidad
        st.session_state.productos.append([nombre, categoria, precio, cantidad, total])
        st.success("Producto agregado")

    if st.session_state.productos:
        arr = np.array(st.session_state.productos)
        df = pd.DataFrame(arr, columns=["Nombre", "Categoría", "Precio", "Cantidad", "Total"])
        st.dataframe(df)

# --- Ejercicio 3: Finanzas (Funciones externas) ---
import libreria_funciones_proyecto1 as lfp
def ejercicio3():
    st.header("Ejercicio 3 – Finanzas")
    st.markdown("Calcular la cuota mensual de un préstamo bajo el sistema francés.")

    monto = st.number_input("Monto del préstamo", min_value=0.0)
    tasa = st.number_input("Tasa anual (%)", min_value=0.0, max_value=100.0)
    plazo = st.number_input("Plazo en meses", min_value=1)

    if "resultados_finanzas" not in st.session_state:
        st.session_state.resultados_finanzas = []

    if st.button("Calcular cuota"):
        resultado = lfp.calcular_cuota_prestamo_frances(monto, tasa, plazo)
        st.write(f"Cuota mensual: {resultado['cuota_mensual']}")
        st.write(f"Total pagado: {resultado['total_pagado']}")
        st.write(f"Interés total: {resultado['interes_total']}")

        st.session_state.resultados_finanzas.append([
            monto, tasa, plazo,
            resultado['cuota_mensual'],
            resultado['total_pagado'],
            resultado['interes_total']
        ])

    if st.session_state.resultados_finanzas:
        df = pd.DataFrame(
            st.session_state.resultados_finanzas,
            columns=["Monto", "Tasa (%)", "Plazo (meses)", "Cuota mensual", "Total pagado", "Interés total"]
        )
        st.dataframe(df)

# --- Ejercicio 4: Clases con CRUD ---
import libreria_clases_proyecto1 as lcp
def ejercicio4():
    st.header("Ejercicio 4 – Administración / Recursos Humanos")
    st.markdown("Registrar empleados y calcular salario neto con base, bono y descuento.")

    if "empleados" not in st.session_state:
        st.session_state.empleados = []

    nombre = st.text_input("Nombre del empleado")
    salario_base = st.number_input("Salario base", min_value=0.0)
    porcentaje_bono = st.number_input("Porcentaje de bono (%)", min_value=0.0, max_value=100.0)
    porcentaje_descuento = st.number_input("Porcentaje de descuento (%)", min_value=0.0, max_value=100.0)

    if st.button("Agregar empleado"):
        empleado = lcp.Empleado(nombre, salario_base, porcentaje_bono, porcentaje_descuento)
        st.session_state.empleados.append(empleado)
        st.success("Empleado registrado")

    if st.session_state.empleados:
        data = [emp.resumen() for emp in st.session_state.empleados]
        df = pd.DataFrame(data)
        st.dataframe(df)

        # Actualizar
        idx = st.number_input("Índice de empleado a actualizar", min_value=0, max_value=len(st.session_state.empleados)-1, step=1)
        nuevo_salario = st.number_input("Nuevo salario base", min_value=0.0)
        nuevo_bono = st.number_input("Nuevo porcentaje de bono (%)", min_value=0.0, max_value=100.0)
        nuevo_descuento = st.number_input("Nuevo porcentaje de descuento (%)", min_value=0.0, max_value=100.0)

        if st.button("Actualizar empleado"):
            st.session_state.empleados[idx] = lcp.Empleado(
                st.session_state.empleados[idx].nombre,
                nuevo_salario,
                nuevo_bono,
                nuevo_descuento
            )
            st.success("Empleado actualizado")

        # Eliminar
        idx_del = st.number_input("Índice de empleado a eliminar", min_value=0, max_value=len(st.session_state.empleados)-1, step=1)
        if st.button("Eliminar empleado"):
            st.session_state.empleados.pop(idx_del)
            st.success("Empleado eliminado")

# --- Menú principal ---
def main():
    menu = st.sidebar.selectbox("Menú", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
    if menu == "Home":
        home()
    elif menu == "Ejercicio 1":
        ejercicio1()
    elif menu == "Ejercicio 2":
        ejercicio2()
    elif menu == "Ejercicio 3":
        ejercicio3()
    elif menu == "Ejercicio 4":
        ejercicio4()

if __name__ == "__main__":
    main()