import streamlit as st

st.set_page_config(page_title="Sistema de Gestión Bibliotecaria", page_icon="📚", layout="wide")

if "registrado" not in st.session_state:
    st.session_state.registrado = False
    st.session_state.usuario = ""

if "inventario" not in st.session_state:
    st.session_state.inventario = [
        {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "genero": "Realismo Mágico", "disponible": True, "devolucion": "-"},
        {"id": 2, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "genero": "Infantil / Filosofía", "disponible": True, "devolucion": "-"},
        {"id": 3, "titulo": "1984", "autor": "George Orwell", "genero": "Distopía", "disponible": False, "devolucion": "Hoy"},
        {"id": 4, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "genero": "Clásico", "disponible": False, "devolucion": "En 2 días"},
        {"id": 5, "titulo": "El Hobbit", "autor": "J.R.R. Tolkien", "genero": "Fantasía", "disponible": True, "devolucion": "-"},
        {"id": 6, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "genero": "Drama", "disponible": True, "devolucion": "-"},
        {"id": 7, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "genero": "Ciencia Ficción", "disponible": False, "devolucion": "En 5 días"},
        {"id": 8, "titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "genero": "Romance Clásico", "disponible": True, "devolucion": "-"}
    ]

for libro in st.session_state.inventario:
    if "devolucion" not in libro:
        libro["devolucion"] = "-"

st.markdown("""
    <style>
    /* Fondo degradado llamativo cyberpunk-cyberpunk oscuro */
    .stApp { 
        background: radial-gradient(circle at top right, #1e1b4b, #0f172a 60%, #020617);
        color: #f8fafc; 
    }
    
    /* Contenedor del logotipo e interfaz */
    .logo-container { text-align: center; margin-bottom: 25px; animation: glow 2s ease-in-out infinite alternate; }
    
    /* Tarjetas de Libros Estilo Vidrio Esmerilado (Glassmorphism) */
    .card-biblioteca {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(8px);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 12px;
    }
    
    .badge-disponible { background-color: #10b981; color: white; padding: 5px 12px; border-radius: 30px; font-size: 11px; font-weight: bold; display: inline-block; }
    .badge-prestado { background-color: #ef4444; color: white; padding: 5px 12px; border-radius: 30px; font-size: 11px; font-weight: bold; display: inline-block; }
    
    /* Contenedores de avisos de la app */
    .alerta-contenedor { background: rgba(245, 158, 11, 0.1); border-left: 5px solid #f59e0b; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
    .alerta-critica { background: rgba(239, 68, 68, 0.1); border-left: 5px solid #ef4444; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

logo_libros_svg = """
<div class="logo-container">
    <svg width="140" height="140" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4 18H18C19.1046 18 20 17.1046 20 16V15H4V18Z" fill="#a855f7" opacity="0.8"/>
        <path d="M4 15H20V12H5.5C4.67157 12 4 12.6716 4 13.5V15Z" fill="#c084fc"/>
        <path d="M6 12H18C19.1046 12 20 11.1046 20 10V9H6V12Z" fill="#0284c7" opacity="0.8"/>
        <path d="M6 9H20V6H7.5C6.67157 6 6 6.67157 6 7.5V9Z" fill="#38bdf8"/>
        <path d="M4 18C2.89543 18 2 18.8954 2 20C2 21.1046 2.89543 22 4 22H20" stroke="#f43f5e" stroke-width="2" stroke-linecap="round"/>
    </svg>
</div>
"""

if not st.session_state.registrado:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(logo_libros_svg, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #ffffff; font-family: system-ui; font-weight: 800; letter-spacing: -0.5px;'>Sistema de Gestión Bibliotecaria</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 15px;'>Módulo de Autenticación de Operadores y Alumnos</p>", unsafe_allow_html=True)
    
    _, col_center, _ = st.columns([1, 1.6, 1])
    with col_center:
        with st.form("login_sistema"):
            st.markdown("<p style='color: #cbd5e1; margin-bottom:4px; font-weight:500;'>Código de Operador / Usuario</p>", unsafe_allow_html=True)
            user_input = st.text_input("Usuario", label_visibility="collapsed")
            
            st.markdown("<p style='color: #cbd5e1; margin-bottom:4px; font-weight:500;'>Clave de Acceso</p>", unsafe_allow_html=True)
            pass_input = st.text_input("Contraseña", type="password", label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            bot_entrar = st.form_submit_button("Ingresar al Sistema →", use_container_width=True)
            
            if bot_entrar:
                if user_input and pass_input:
                    st.session_state.registrado = True
                    st.session_state.usuario = user_input
                    st.rerun()
                else:
                    st.error("Campos obligatorios vacíos. Por favor complete sus datos.")

else:
    # Barra lateral de administración
    st.sidebar.markdown(logo_libros_svg, unsafe_allow_html=True)
    st.sidebar.markdown(f"<h3 style='text-align:center; color:#ffffff;'>Sesión: {st.session_state.usuario}</h3>", unsafe_allow_html=True)
    st.sidebar.divider()
    if st.sidebar.button(" Desconectar Operador", use_container_width=True):
        st.session_state.registrado = False
        st.rerun()

    st.title("Tablero de Control Bibliotecario")
    st.markdown("---")
    
    st.subheader(" Panel de Alertas Operativas")
    c_alert1, c_alert2 = st.columns(2)
    with c_alert1:
        st.markdown("""
        <div class="alerta-contenedor">
            <span style='color:#f59e0b; font-weight:bold;'> SEGUIMIENTO DE RETORNO</span><br>
            El ejemplar <b>'Don Quijote de la Mancha'</b> tiene un tiempo límite estimado de entrega de 2 días.
        </div>
        """, unsafe_allow_html=True)
    with c_alert2:
        st.markdown("""
        <div class="alerta-critica">
            <span style='color:#ef4444; font-weight:bold;'> PLAZO EXPIRED</span><br>
            La orden para el ejemplar de lectura <b>'1984'</b> vence de manera inapelable el día de hoy.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(" Localizador de Libros e Inventario")
    busqueda = st.text_input("Buscar por título, autor o categoría indexada:", placeholder="Escribe el nombre del libro...").lower()

    # Algoritmo de filtrado
    libros_filtrados = [
        l for l in st.session_state.inventario 
        if busqueda in l["titulo"].lower() or busqueda in l["autor"].lower() or busqueda in l["genero"].lower()
    ]

    disponibles = [l for l in libros_filtrados if l["disponible"]]
    no_disponibles = [l for l in libros_filtrados if not l["disponible"]]

    st.markdown("<br>##  Copias en Estantería (Listas para Asignar)", unsafe_allow_html=True)
    if disponibles:
        for lib in disponibles:
            st.markdown(f"""
            <div class="card-biblioteca">
                <span class="badge-disponible">EJEMPLAR DISPONIBLE</span>
                <h3 style="margin: 8px 0 4px 0; color:#ffffff;"> {lib['titulo']}</h3>
                <p style="margin:0; color:#94a3b8; font-size:14px;"><b>Autor:</b> {lib['autor']} | <b>Género:</b> {lib['genero']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"📥 Conceder Préstamo: {lib['titulo']}", key=f"btn_disp_{lib['id']}"):
                lib["disponible"] = False
                lib["devolucion"] = "En 7 días"
                st.balloons()
                st.rerun()
    else:
        st.info("Ningún ejemplar coincide con el criterio del motor de búsqueda.")

    st.markdown("<br>##  Registro Activo de Préstamos Externos", unsafe_allow_html=True)
    if no_disponibles:
        for lib in no_disponibles:
            st.markdown(f"""
            <div class="card-biblioteca" style="border-left: 4px solid #ef4444;">
                <span class="badge-prestado">EN LECTURA EXTERNA</span>
                <h3 style="margin: 8px 0 4px 0; color:#cbd5e1;"> {lib['titulo']}</h3>
                <p style="margin:0; color:#94a3b8; font-size:14px;"><b>Autor:</b> {lib['autor']} | <b>Límite de Entrega:</b> <span style="color:#fca5a5; font-weight:bold;">{lib['devolucion']}</span></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No se registran transacciones externas pendientes en este momento.")