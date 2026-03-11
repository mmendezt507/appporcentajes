import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Calculadora de porcentajes",
    page_icon="💰",
    layout="centered"
)

# Inicializar historial
if "historial" not in st.session_state:
    st.session_state.historial = []

# Estilos compatibles con modo oscuro
st.markdown("""
<style>

.main-title{
    font-size:36px;
    font-weight:bold;
    text-align:center;
}

.subtitle{
    text-align:center;
    opacity:0.8;
    margin-bottom:25px;
}

.calc-card{
    padding:25px;
    border-radius:12px;
    border:1px solid rgba(128,128,128,0.3);
}

.result-box{
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    border:1px solid rgba(128,128,128,0.4);
    margin-top:20px;
}

.history-card{
    padding:20px;
    border-radius:10px;
    border:1px solid rgba(128,128,128,0.3);
}

</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="main-title">Calculadora de porcentajes</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Calcula porcentajes y guarda el historial</p>', unsafe_allow_html=True)

# Calculadora
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

        # Guardar historial
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