import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Calculadora Financiera de Porcentajes",
    page_icon="💰",
    layout="centered"
)

# Inicializar historial
if "historial" not in st.session_state:
    st.session_state.historial = []

# Estilos
st.markdown("""
<style>

.main-title{
    font-size:38px;
    font-weight:bold;
    text-align:center;
    color:#1f4e79;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.calc-card{
    background-color:#f7f9fc;
    padding:25px;
    border-radius:12px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}

.result-box{
    background-color:#e8f4ff;
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    margin-top:20px;
}

.history-card{
    background-color:#ffffff;
    padding:20px;
    border-radius:10px;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="main-title">Calculadora Financiera</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Calcula porcentajes y guarda el historial de operaciones</p>', unsafe_allow_html=True)

# Tarjeta calculadora
with st.container():

    st.markdown('<div class="calc-card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        numero = st.number_input(
            "Cantidad",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

    with col2:
        porcentaje = st.number_input(
            "Porcentaje (%)",
            min_value=0.0,
            step=1.0,
            value=16.0
        )

    calcular = st.button("Calcular", use_container_width=True)

    if calcular:
        resultado = numero * (porcentaje / 100)

        # Guardar en historial
        st.session_state.historial.insert(
            0,
            f"{porcentaje}% de {numero:.2f} = {resultado:.2f}"
        )

        st.markdown(
            f"""
            <div class="result-box">
            Resultado: {resultado:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

# Historial
st.markdown("### Historial de cálculos")

with st.container():

    st.markdown('<div class="history-card">', unsafe_allow_html=True)

    if st.session_state.historial:

        for item in st.session_state.historial:
            st.write("• ", item)

        if st.button("Limpiar historial"):
            st.session_state.historial = []
            st.rerun()

    else:
        st.info("Aún no hay cálculos realizados.")

    st.markdown("</div>", unsafe_allow_html=True)