
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# =========================================================================
# CONFIGURACIÓN DE LA PÁGINA (debe ser el primer comando de Streamlit)
# =========================================================================
st.set_page_config(
    page_title="LYGRAV Pro | Gravity Dam Modeler",
    page_icon="🏞️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================================
# PALETA Y ESTILOS GLOBALES
# =========================================================================
NAVY = "#0B1D3A"
NAVY_2 = "#123C69"
GOLD = "#E3B23C"
TEAL = "#54B8B0"
CREAM = "#F4F1EA"
MUTED = "#93A2B8"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

h1, h2, h3 {{
    font-family: 'Space Grotesk', sans-serif !important;
    color: {NAVY} !important;
}}

.stApp {{
    background-color: {CREAM} !important;
}}
.stApp {{
    color: {NAVY} !important;
}}
[data-testid="stAppViewContainer"] {{
    background-color: {CREAM} !important;
}}
[data-testid="stHeader"] {{
    background-color: {CREAM} !important;
}}

section[data-testid="stSidebar"] [data-testid="stExpander"] {{
    background-color: {NAVY_2} !important;
    border: 1px solid rgba(227,178,60,0.35) !important;
    border-radius: 10px !important;
    overflow: hidden;
}}
section[data-testid="stSidebar"] [data-testid="stExpander"] summary,
section[data-testid="stSidebar"] [data-testid="stExpander"] > details > summary {{
    background-color: {NAVY_2} !important;
}}
section[data-testid="stSidebar"] [data-testid="stExpander"] summary * {{
    color: {CREAM} !important;
    fill: {CREAM} !important;
}}
section[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] {{
    background-color: {NAVY} !important;
}}

section[data-testid="stSidebar"] {{
    background-color: {NAVY};
}}
section[data-testid="stSidebar"] * {{
    color: {CREAM} !important;
}}
section[data-testid="stSidebar"] hr {{
    border-color: {NAVY_2};
}}

section[data-testid="stSidebar"] input,
section[data-testid="stSidebar"] textarea,
section[data-testid="stSidebar"] [data-baseweb="select"] *,
section[data-testid="stSidebar"] [data-baseweb="input"],
.stApp input,
.stApp textarea {{
    color: {NAVY} !important;
    background-color: #FFFFFF !important;
    -webkit-text-fill-color: {NAVY} !important;
}}
section[data-testid="stSidebar"] [data-baseweb="input"],
section[data-testid="stSidebar"] [data-baseweb="select"] > div {{
    background-color: #FFFFFF !important;
    border-radius: 6px;
}}
section[data-testid="stSidebar"] button svg,
section[data-testid="stSidebar"] [data-baseweb="select"] svg {{
    fill: {NAVY} !important;
    color: {NAVY} !important;
}}
.stApp [data-testid="stDataFrame"] *,
.stApp [data-testid="stDataEditor"] * {{
    color: {NAVY} !important;
}}

[data-testid="stDataFrame"],
[data-testid="stDataEditor"] {{
    background-color: #FFFFFF !important;
    border: 1px solid #E4E1D6 !important;
    border-radius: 10px !important;
    overflow: hidden;
}}
[data-testid="stDataFrame"] div,
[data-testid="stDataEditor"] div {{
    background-color: #FFFFFF !important;
}}
[data-testid="stDataFrame"] [role="columnheader"],
[data-testid="stDataEditor"] [role="columnheader"] {{
    background-color: {CREAM} !important;
    color: {NAVY} !important;
    font-weight: 600 !important;
}}
[data-testid="stDataFrame"] [role="gridcell"],
[data-testid="stDataEditor"] [role="gridcell"] {{
    background-color: #FFFFFF !important;
    color: {NAVY} !important;
}}
[data-testid="stDataFrame"] [role="row"]:hover [role="gridcell"],
[data-testid="stDataEditor"] [role="row"]:hover [role="gridcell"] {{
    background-color: {CREAM} !important;
}}
section[data-testid="stSidebar"] [data-testid="stDataFrame"],
section[data-testid="stSidebar"] [data-testid="stDataEditor"] {{
    background-color: #FFFFFF !important;
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 4px;
    border-bottom: 2px solid {CREAM};
}}
.stTabs [data-baseweb="tab"] {{
    background-color: transparent;
    border-radius: 8px 8px 0 0;
    color: {NAVY_2};
    font-weight: 600;
    padding: 8px 18px;
}}
.stTabs [aria-selected="true"] {{
    background-color: {NAVY} !important;
    color: {GOLD} !important;
}}

.lg-card {{
    background-color: #FFFFFF;
    border: 1px solid #E4E1D6;
    border-left: 5px solid {GOLD};
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 10px;
}}
.lg-card h4 {{
    margin: 0 0 4px 0;
    font-size: 13px;
    color: {NAVY_2};
    text-transform: uppercase;
    letter-spacing: 0.04em;
}}
.lg-card .lg-val {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 24px;
    font-weight: 600;
    color: {NAVY};
}}
.lg-ok {{ border-left-color: {TEAL} !important; }}
.lg-ok .lg-val {{ color: #0F6E56; }}
.lg-bad {{ border-left-color: #D85A30 !important; }}
.lg-bad .lg-val {{ color: #993C1D; }}

.lg-banner {{
    background: linear-gradient(90deg, {NAVY} 0%, {NAVY_2} 100%);
    color: {CREAM};
    padding: 10px 18px;
    border-radius: 10px;
    margin-bottom: 14px;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    letter-spacing: 0.02em;
}}

.stButton>button {{
    background-color: {NAVY};
    color: {CREAM};
    border: 1px solid {GOLD};
    border-radius: 8px;
    font-weight: 600;
    padding: 0.5em 1.4em;
}}
.stButton>button:hover {{
    background-color: {GOLD};
    color: {NAVY};
    border-color: {NAVY};
}}
</style>
""", unsafe_allow_html=True)

# =========================================================================
# PORTADA / SPLASH SCREEN
# =========================================================================
if "entrar" not in st.session_state:
    st.session_state.entrar = False


def mostrar_portada():
    st.markdown(f"""
    <style>
    header[data-testid="stHeader"] {{ display: none; }}
    section[data-testid="stSidebar"] {{ display: none; }}
    div.block-container {{ padding-top: 2rem; }}
    .lg-hero {{
        background: radial-gradient(circle at 30% 20%, {NAVY_2} 0%, {NAVY} 65%);
        border-radius: 18px;
        padding: 60px 40px 40px 40px;
        text-align: center;
        color: {CREAM};
        position: relative;
        overflow: hidden;
    }}
    .lg-hero .eyebrow {{
        letter-spacing: 0.3em;
        font-size: 12px;
        color: {GOLD};
        text-transform: uppercase;
        margin-bottom: 18px;
    }}
    .lg-hero h1 {{
        font-family: 'Space Grotesk', sans-serif;
        color: {CREAM} !important;
        font-size: 58px;
        font-weight: 700;
        margin: 0;
        letter-spacing: 0.02em;
    }}
    .lg-hero h1 span {{ color: {GOLD}; }}
    .lg-hero p.subtitle {{
        font-size: 17px;
        color: {MUTED};
        margin-top: 14px;
        max-width: 520px;
        margin-left: auto;
        margin-right: auto;
    }}
    .lg-hero .credit {{
        margin-top: 34px;
        font-size: 13px;
        color: {MUTED};
        letter-spacing: 0.04em;
    }}
    .lg-hero .credit b {{ color: {TEAL}; }}
    .wave-rule {{
        width: 140px;
        height: 4px;
        margin: 22px auto 0 auto;
        background: linear-gradient(90deg, {GOLD}, {TEAL});
        border-radius: 4px;
    }}
    </style>

    <div class="lg-hero">
        <div class="eyebrow" style="color:{GOLD} !important;">Análisis y diseño de presas de gravedad</div>
        <svg width="220" height="120" viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
            <polygon points="40,100 40,55 70,15 95,15 130,100" fill="#1f3a5f" stroke="{GOLD}" stroke-width="2"/>
            <rect x="0" y="100" width="220" height="6" fill="{GOLD}" opacity="0.7"/>
            <path d="M0,70 Q15,62 30,70 T60,70" stroke="{TEAL}" stroke-width="2.5" fill="none" opacity="0.85"/>
            <path d="M0,80 Q15,72 30,80 T60,80" stroke="{TEAL}" stroke-width="2" fill="none" opacity="0.55"/>
            <path d="M130,90 Q160,84 190,90 T220,90" stroke="{TEAL}" stroke-width="2" fill="none" opacity="0.55"/>
        </svg>
        <h1 style="color:{CREAM} !important;">LY<span style="color:{GOLD} !important;">GRAV</span> PRO</h1>
        <div class="wave-rule"></div>
        <p class="subtitle" style="color:{MUTED} !important;">Modelamiento geométrico, estabilidad a presa vacía y presa llena, y verificación de esfuerzos para presas de gravedad.</p>
        <div class="credit" style="color:{MUTED} !important;">Desarrollado por <b style="color:{TEAL} !important;">Lucero Yamile Silva de la Cruz</b></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 0.6, 1])
    with c2:
        st.write("")
        if st.button("Ingresar al sistema →", use_container_width=True):
            st.session_state.entrar = True
            st.rerun()


if not st.session_state.entrar:
    mostrar_portada()
    st.stop()

# =========================================================================
# FUNCIONES DE CÁLCULO DE ESTABILIDAD
#
# CONVENCIÓN UNIFICADA:
#   • Talón = lado aguas arriba  (x_min en el gráfico, eje Y del cuaderno)
#   • Punta = lado aguas abajo   (x_max en el gráfico)
#   • Excentricidad, brazos y momentos SIEMPRE referenciados a la PUNTA
#     (pie de la presa, el caso más crítico para el volteo):
#         e = x̄_punta − b/2      (e>0 → centroide se acerca al talón)
#   • Fórmulas de esfuerzos estándar (referencia PUNTA, talón "+"):
#       σ_talón = W/A + M_e·(b/2)/I
#       σ_punta = W/A − M_e·(b/2)/I
#   • Tabla y visualización muestran brazos medidos desde la PUNTA.
#   • Área y centroide calculados con FÓRMULA DE SHOELACE → exacta para
#     cualquier polígono simple, independientemente de su forma.
#   • EMPUJE HIDROSTÁTICO SOBRE CARA INCLINADA: se descompone en
#     componente horizontal (F, la de siempre, con el prisma de presión)
#     y componente VERTICAL (Fv = peso del agua apoyada sobre el talud,
#     entre la cara y la vertical trazada desde el pie de esa cara). Si
#     la cara es vertical, Fv=0 automáticamente.
# =========================================================================

def _shoelace(px, py):
    """Devuelve (área, x_centroide_global) para cualquier polígono simple."""
    n = len(px)
    S, Cx = 0.0, 0.0
    for i in range(n):
        j = (i + 1) % n
        c = px[i] * py[j] - px[j] * py[i]
        S  += c
        Cx += (px[i] + px[j]) * c
    area = abs(S) / 2.0
    x_cg = Cx / (3.0 * S) if abs(S) > 1e-12 else sum(px) / n
    return area, x_cg


def _obtener_cadenas(px, py):
    """
    Divide el contorno de la presa en la cadena aguas arriba (talón→cresta)
    y aguas abajo (cresta→punta), asumiendo un único vértice de cresta (el
    de mayor Y). Es la misma lógica que usan la vista "Perfil Geométrico"
    y la descomposición en rectángulos/triángulos.
    """
    idx_cresta = py.index(max(py))
    chain_izq_x = px[:idx_cresta + 1]
    chain_izq_y = py[:idx_cresta + 1]
    chain_der_x = px[idx_cresta:]
    chain_der_y = py[idx_cresta:]
    return chain_izq_x, chain_izq_y, chain_der_x, chain_der_y, px[idx_cresta]


def _decomponer_rectangulos_triangulos(px, py, gamma_c, L):
    """
    Descompone el perfil de la presa en franjas verticales (rectángulo +
    triángulo) entre cada par de vértices consecutivos en X — la misma
    lógica que se enseña a mano: se identifican los tramos verticales
    (rectángulos) y las transiciones de talud (triángulos), en vez de
    una triangulación en abanico sin significado físico.
    """
    y_base = min(py)
    chain_izq_x, chain_izq_y, chain_der_x, chain_der_y, x_cresta = _obtener_cadenas(px, py)

    if len(chain_izq_x) > 1:
        orden = np.argsort(chain_izq_x)
        chain_izq_x = np.array(chain_izq_x)[orden]
        chain_izq_y = np.array(chain_izq_y)[orden]
    if len(chain_der_x) > 1:
        orden = np.argsort(chain_der_x)
        chain_der_x = np.array(chain_der_x)[orden]
        chain_der_y = np.array(chain_der_y)[orden]

    breakpoints = sorted(set(round(v, 9) for v in px))

    def _y_top(x):
        if x <= x_cresta + 1e-9 and len(chain_izq_x) > 1:
            return float(np.interp(x, chain_izq_x, chain_izq_y))
        elif len(chain_der_x) > 1:
            return float(np.interp(x, chain_der_x, chain_der_y))
        else:
            return float(np.interp(x, chain_izq_x, chain_izq_y))

    filas = []
    for k in range(len(breakpoints) - 1):
        xi, xj = breakpoints[k], breakpoints[k + 1]
        dx = xj - xi
        if dx < 1e-9:
            continue

        hi = _y_top(xi) - y_base
        hj = _y_top(xj) - y_base
        h_min = min(hi, hj)

        if h_min > 1e-9:
            area_r = dx * h_min
            peso_r = area_r * L * gamma_c
            cx_r   = (xi + xj) / 2.0
            filas.append({
                "Área (m²)": area_r, "Peso (kgf)": peso_r,
                "cx_global": cx_r,
            })

        dh = hi - hj
        if abs(dh) > 1e-9:
            area_t = 0.5 * dx * abs(dh)
            peso_t = area_t * L * gamma_c
            if dh > 0:
                cx_t = xi + dx / 3.0
            else:
                cx_t = xi + 2.0 * dx / 3.0
            filas.append({
                "Área (m²)": area_t, "Peso (kgf)": peso_t,
                "cx_global": cx_t,
            })

    return filas


def _cuna_agua(chain_x, chain_y, x_ref, h, gamma_w, L):
    """
    Peso del agua que se apoya sobre una cara inclinada de la presa, en la
    región comprendida entre la cara y la vertical x=x_ref (la vertical
    trazada desde el pie de esa cara), hasta la altura h.

    Es exactamente la componente VERTICAL del empuje hidrostático sobre
    un talud: si la cara es vertical (x constante), la cuña tiene ancho
    cero y Fv=0 automáticamente — coherente con la teoría clásica, donde
    una cara vertical solo genera empuje horizontal.

    Devuelve (Fv, x_centroide_global_de_la_cuña).
    """
    if h <= 1e-9 or len(chain_x) < 2:
        return 0.0, x_ref

    orden = np.argsort(chain_y)
    xs = np.array(chain_x)[orden]
    ys = np.array(chain_y)[orden]

    if h > ys.max() + 1e-9:
        h = float(ys.max())

    x_en_h = float(np.interp(h, ys, xs))
    pts_x, pts_y = [], []
    for x, y in zip(xs, ys):
        if y <= h + 1e-9:
            pts_x.append(float(x)); pts_y.append(float(y))
        else:
            break
    if not pts_y or pts_y[-1] < h - 1e-9:
        pts_x.append(x_en_h); pts_y.append(h)

    if len(pts_x) < 2:
        return 0.0, x_ref

    poly_x = pts_x + [x_ref, x_ref]
    poly_y = pts_y + [h, 0.0]
    area, cx = _shoelace(poly_x, poly_y)
    if area < 1e-9:
        return 0.0, x_ref
    return area * L * gamma_w, cx


def calcular_presa_vacia(puntos_x, puntos_y, gamma_c=2300.0, L=1.0):
    px = list(puntos_x)
    py = list(puntos_y)
    if len(px) > 2 and abs(px[-1] - px[0]) < 1e-9 and abs(py[-1] - py[0]) < 1e-9:
        px.pop(); py.pop()

    n = len(px)
    x_min, x_max = min(px), max(px)
    b_base = x_max - x_min

    A_total, x_cg_global = _shoelace(px, py)
    W_T = A_total * L * gamma_c

    x_cg_talon = x_cg_global - x_min
    x_cg_punta = x_max   - x_cg_global

    e    = x_cg_punta - (b_base / 2.0)
    M_e  = W_T * e

    A_base  = b_base * L
    I_base  = L * (b_base ** 3) / 12.0

    sigma_talon = (W_T / A_base) + (M_e * (b_base / 2.0) / I_base)
    sigma_punta = (W_T / A_base) - (M_e * (b_base / 2.0) / I_base)

    piezas = _decomponer_rectangulos_triangulos(px, py, gamma_c, L)
    filas_tabla = []
    for i, p in enumerate(piezas, start=1):
        filas_tabla.append({
            "Figura":     str(i),
            "Área (m²)":  round(p["Área (m²)"], 4),
            "Peso (kgf)": round(p["Peso (kgf)"], 2),
        })

    filas_tabla.append({
        "Figura":     "TOTAL",
        "Área (m²)":  round(A_total, 4),
        "Peso (kgf)": round(W_T, 2),
    })

    chain_izq_x, chain_izq_y, chain_der_x, chain_der_y, x_cresta = _obtener_cadenas(px, py)

    return {
        "df":          pd.DataFrame(filas_tabla),
        "W_T":         W_T,
        "x_cg_punta":  x_cg_punta,
        "x_cg_talon":  x_cg_talon,
        "e":           e,
        "M_e":         M_e,
        "sigma_talon": sigma_talon,
        "sigma_punta": sigma_punta,
        "b_base":      b_base,
        "x_min":       x_min,
        "x_max":       x_max,
        "A_base":      A_base,
        "I_base":      I_base,
        "chain_izq_x": chain_izq_x, "chain_izq_y": chain_izq_y,
        "chain_der_x": chain_der_x, "chain_der_y": chain_der_y,
    }


def calcular_presa_llena(res_v, h_up, h_down, gamma_w=1000.0, mu=0.75, L=1.0):
    W_T        = res_v["W_T"]
    x_cg_punta = res_v["x_cg_punta"]
    b_base     = res_v["b_base"]
    x_min      = res_v["x_min"]
    x_max      = res_v["x_max"]

    M_R = W_T * x_cg_punta

    # 1. Empuje hidrostático aguas arriba — componente HORIZONTAL
    F_up, M_v_up, h_cp_up = 0.0, 0.0, 0.0
    if h_up > 0:
        h_cg_up  = h_up / 2.0
        A_up     = h_up * L
        I_cg_up  = (h_up ** 3) / 12.0
        h_cp_up  = (I_cg_up / (h_cg_up * h_up)) + h_cg_up
        F_up     = gamma_w * h_cg_up * A_up
        M_v_up   = F_up * (h_up - h_cp_up)

    # 1b. Empuje hidrostático aguas arriba — componente VERTICAL
    Fv_up, cx_Fv_up = _cuna_agua(res_v["chain_izq_x"], res_v["chain_izq_y"],
                                  x_ref=x_min, h=h_up, gamma_w=gamma_w, L=L)
    M_Fv_up = Fv_up * (x_max - cx_Fv_up)

    # 2. Empuje hidrostático aguas abajo — componente HORIZONTAL
    F_down, M_e_down, h_cp_down = 0.0, 0.0, 0.0
    if h_down > 0:
        h_cg_down  = h_down / 2.0
        A_down     = h_down * L
        I_cg_down  = (h_down ** 3) / 12.0
        h_cp_down  = (I_cg_down / (h_cg_down * h_down)) + h_cg_down
        F_down     = gamma_w * h_cg_down * A_down
        M_e_down   = F_down * (h_down - h_cp_down)

    # 2b. Empuje hidrostático aguas abajo — componente VERTICAL
    Fv_down, cx_Fv_down = _cuna_agua(res_v["chain_der_x"], res_v["chain_der_y"],
                                      x_ref=x_max, h=h_down, gamma_w=gamma_w, L=L)
    M_Fv_down = Fv_down * (x_max - cx_Fv_down)

    # 3. Subpresión trapezoidal
    p_up, p_down = gamma_w * h_up, gamma_w * h_down
    U_rect  = min(p_up, p_down) * b_base * L
    U_tri   = (abs(p_up - p_down) * b_base * L) / 2.0
    U_total = U_rect + U_tri

    if U_total > 0:
        br_rect = b_base / 2.0
        if p_up >= p_down:
            br_tri = (2.0 / 3.0) * b_base
        else:
            br_tri = b_base / 3.0
        x_u     = (U_rect * br_rect + U_tri * br_tri) / U_total
        M_v_sub = U_total * x_u
    else:
        x_u, M_v_sub = 0.0, 0.0

    Sum_M_Volteo          = M_v_up + M_v_sub
    Sum_M_Estabilizadores = M_R + M_e_down + M_Fv_up + M_Fv_down

    # Resultante vertical: ahora incluye Fv_up y Fv_down
    R_v = W_T + Fv_up + Fv_down - U_total

    Fsv    = Sum_M_Estabilizadores / Sum_M_Volteo if Sum_M_Volteo > 0 else float('inf')
    F_H_n  = F_up - F_down
    Fsd    = (mu * R_v) / F_H_n if F_H_n > 0 else float('inf')

    # x'' usa solo fuerzas VERTICALES (peso + Fv_up + Fv_down - subpresión)
    x_segundo = (M_R + M_Fv_up + M_Fv_down - M_v_sub) / R_v if R_v != 0 else 0.0

    e_llena   = x_segundo - (b_base / 2.0)
    M_e_llena = R_v * e_llena

    I_base = b_base ** 3 / 12.0
    sigma_talon_l = (R_v / b_base) + (M_e_llena * (b_base / 2.0) / I_base)
    sigma_punta_l = (R_v / b_base) - (M_e_llena * (b_base / 2.0) / I_base)

    return {
        "F_up": F_up, "F_down": F_down, "h_cp_up": h_cp_up, "h_cp_down": h_cp_down,
        "Fv_up": Fv_up, "Fv_down": Fv_down,
        "cx_Fv_up": cx_Fv_up, "cx_Fv_down": cx_Fv_down,
        "M_Fv_up": M_Fv_up, "M_Fv_down": M_Fv_down,
        "U": U_total, "x_u": x_u,
        "M_R": M_R, "M_v_up": M_v_up, "M_e_down": M_e_down, "M_v_sub": M_v_sub,
        "Sum_M_Volteo": Sum_M_Volteo, "Sum_M_Estabilizadores": Sum_M_Estabilizadores,
        "R_v": R_v, "Fsv": Fsv, "Fsd": Fsd,
        "x_segundo": x_segundo, "e_llena": e_llena,
        "sigma_talon_l": sigma_talon_l, "sigma_punta_l": sigma_punta_l,
    }


# =========================================================================
# DIAGRAMA DE ESFUERZOS (TALÓN - PUNTA) — ESTILO CLÁSICO "PEINE DE FLECHAS"
# =========================================================================
def dibujar_diagrama_esfuerzos(sigma_talon, sigma_punta, b_base, titulo,
                                puntos_x, puntos_y):
    color_comp = "#1D9E75"
    color_trac = "#D85A30"
    color_talon = color_comp if sigma_talon >= 0 else color_trac
    color_punta = color_comp if sigma_punta >= 0 else color_trac

    px = list(puntos_x)
    py = list(puntos_y)
    if len(px) > 2 and px[-1] == px[0] and py[-1] == py[0]:
        px.pop(); py.pop()
    x_min_p, x_max_p = min(px), max(px)
    y_base = min(py)

    fig, ax = plt.subplots(figsize=(7.5, 6.5))

    ax.fill(px, py, color="#E4E1D6", alpha=1.0, zorder=3)
    ax.plot(px + [px[0]], py + [py[0]], color=NAVY, linewidth=2.2, zorder=4)

    max_abs = max(abs(sigma_talon), abs(sigma_punta), 1.0)
    alt_max = (max(py) - y_base) * 0.55

    long_talon = (abs(sigma_talon) / max_abs) * alt_max
    long_punta = (abs(sigma_punta) / max_abs) * alt_max
    sign_t = -1 if sigma_talon >= 0 else +1
    sign_p = -1 if sigma_punta >= 0 else +1
    y_tip_talon = y_base + sign_t * long_talon
    y_tip_punta = y_base + sign_p * long_punta

    n_flechas = int(np.clip(round(b_base / 1.0), 12, 26))
    fracs = np.linspace(0.0, 1.0, n_flechas)
    xs = x_min_p + fracs * (x_max_p - x_min_p)

    for x, frac in zip(xs, fracs):
        sigma_local = sigma_talon + (sigma_punta - sigma_talon) * frac
        longitud    = (abs(sigma_local) / max_abs) * alt_max
        color       = color_comp if sigma_local >= 0 else color_trac
        signo       = -1 if sigma_local >= 0 else +1

        if longitud < alt_max * 0.02:
            ax.plot(x, y_base, marker='o', markersize=3, color=NAVY_2, zorder=7)
            continue

        y_tip = y_base + signo * longitud
        ax.annotate("", xy=(x, y_tip), xytext=(x, y_base),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, mutation_scale=10), zorder=6)

    ax.plot([x_min_p, x_max_p], [y_tip_talon, y_tip_punta],
            color=MUTED, linewidth=1.4, zorder=6)

    if (sigma_talon >= 0) != (sigma_punta >= 0) and (sigma_punta - sigma_talon) != 0:
        frac_zero = min(max(-sigma_talon / (sigma_punta - sigma_talon), 0.0), 1.0)
        x_zero = x_min_p + frac_zero * (x_max_p - x_min_p)
        ax.plot(x_zero, y_base, marker='o', markersize=4, color=NAVY_2, zorder=7)

    ax.plot([x_min_p, x_max_p], [y_base, y_base], color=NAVY, linewidth=1.6, zorder=6)

    va_t = "top" if sigma_talon >= 0 else "bottom"
    va_p = "top" if sigma_punta >= 0 else "bottom"
    off  = alt_max * 0.12

    ax.text(x_min_p - (x_max_p - x_min_p) * 0.02,
            y_tip_talon + sign_t * off,
            f"TALÓN\nσ = {sigma_talon:,.1f} kgf/m²",
            ha="right", va=va_t, fontsize=11, fontweight="bold", color=color_talon, zorder=7)
    ax.text(x_max_p + (x_max_p - x_min_p) * 0.02,
            y_tip_punta + sign_p * off,
            f"PUNTA\nσ = {sigma_punta:,.1f} kgf/m²",
            ha="left",  va=va_p, fontsize=11, fontweight="bold", color=color_punta, zorder=7)

    ax.set_title(titulo, fontsize=15, fontweight="bold", color=NAVY, pad=14)
    ax.set_xlim(x_min_p - (x_max_p - x_min_p) * 0.30, x_max_p + (x_max_p - x_min_p) * 0.30)
    y_lo = min(y_tip_talon, y_tip_punta, y_base) - alt_max * 0.25
    y_hi = max(y_tip_talon, y_tip_punta, max(py), y_base + alt_max * 0.1) + 2
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    fig.tight_layout()
    return fig


def dibujar_diagrama_fuerzas(puntos_x, puntos_y, h_up, h_down, x_centroide_abs,
                              W_T, F_up, F_down, U_total,
                              Fv_up=0.0, Fv_down=0.0, cx_Fv_up=None, cx_Fv_down=None):
    px = list(puntos_x)
    py = list(puntos_y)
    if len(px) > 2 and px[-1] == px[0] and py[-1] == py[0]:
        px.pop(); py.pop()
    x_min, x_max = min(px), max(px)
    y_max = max(py)
    ancho = x_max - x_min

    fig, ax = plt.subplots(figsize=(7.5, 5.8))
    ax.fill(px, py, color="#8C8C82", alpha=1.0, zorder=3)
    ax.plot(px + [px[0]], py + [py[0]], color="#1f1f1f", linewidth=2.2, zorder=4)

    if h_up > 0:
        y_arrow = h_up / 2.0
        ax.annotate("", xy=(x_min + ancho * 0.05, y_arrow), xytext=(x_min - ancho * 0.12, y_arrow),
                     arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.6), zorder=5)
        ax.text(x_min - ancho * 0.13, y_arrow + y_max * 0.04, f"F_H↑ = {F_up:,.0f} kgf",
                color="#0F6E56", fontsize=10.5, fontweight="bold", ha="left", va="bottom")

    if h_down > 0:
        y_arrow2 = h_down / 2.0
        ax.annotate("", xy=(x_max - ancho * 0.05, y_arrow2), xytext=(x_max + ancho * 0.12, y_arrow2),
                     arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.6), zorder=5)
        ax.text(x_max + ancho * 0.13, y_arrow2 + y_max * 0.04, f"F_H↓ = {F_down:,.0f} kgf",
                color="#0F6E56", fontsize=10.5, fontweight="bold", ha="right", va="bottom")

    # Fv_up: componente VERTICAL del empuje aguas arriba (solo si la cara
    # está inclinada y Fv_up>0) — flecha hacia ABAJO, apoyada en el punto
    # de la cresta/talud donde actúa la cuña de agua.
    if Fv_up > 1e-6 and cx_Fv_up is not None:
        y_top_fv = float(np.interp(cx_Fv_up, px, py)) if len(px) >= 2 else y_max
        ax.annotate("", xy=(cx_Fv_up, y_top_fv + y_max * 0.02), xytext=(cx_Fv_up, y_top_fv + y_max * 0.22),
                     arrowprops=dict(arrowstyle="-|>", color="#7A4FB5", lw=2.6), zorder=6)
        ax.text(cx_Fv_up, y_top_fv + y_max * 0.25, f"Fv↑ = {Fv_up:,.0f} kgf",
                color="#5A3A8A", fontsize=10.5, fontweight="bold", ha="center", va="bottom", zorder=6)

    # Fv_down: componente VERTICAL del empuje aguas abajo
    if Fv_down > 1e-6 and cx_Fv_down is not None:
        y_top_fv2 = float(np.interp(cx_Fv_down, px, py)) if len(px) >= 2 else y_max
        ax.annotate("", xy=(cx_Fv_down, y_top_fv2 + y_max * 0.02), xytext=(cx_Fv_down, y_top_fv2 + y_max * 0.22),
                     arrowprops=dict(arrowstyle="-|>", color="#7A4FB5", lw=2.6), zorder=6)
        ax.text(cx_Fv_down, y_top_fv2 + y_max * 0.25, f"Fv↓ = {Fv_down:,.0f} kgf",
                color="#5A3A8A", fontsize=10.5, fontweight="bold", ha="center", va="bottom", zorder=6)

    y_base = min(py)
    if h_up > 0 or h_down > 0:
        ax.annotate("", xy=(x_centroide_abs, y_base + y_max * 0.20), xytext=(x_centroide_abs, y_base - y_max * 0.14),
                     arrowprops=dict(arrowstyle="-|>", color="#D85A30", lw=2.8), zorder=5)
        ax.text(x_centroide_abs, y_base - y_max * 0.18, f"Fs = {U_total:,.0f} kgf",
                color="#993C1D", fontsize=10.5, fontweight="bold", ha="center", va="top")

    ax.annotate("", xy=(x_centroide_abs, y_max * 0.32), xytext=(x_centroide_abs, y_max * 0.62),
                 arrowprops=dict(arrowstyle="-|>", color="#1f1f1f", lw=2.6), zorder=5)
    ax.text(x_centroide_abs, y_max * 0.65, f"W_T = {W_T:,.0f} kgf",
            color="#1f1f1f", fontsize=10.5, fontweight="bold", ha="center", va="bottom")

    ax.set_title("Diagrama de Fuerzas Actuantes — Presa Llena", fontsize=14, fontweight="bold", color=NAVY)
    margen = ancho * 0.38
    ax.set_xlim(x_min - margen, x_max + margen)
    y_hi_total = max(y_max * 1.35, y_max + y_max * 0.35)
    ax.set_ylim(y_base - y_max * 0.32, y_hi_total + 2)
    ax.set_aspect('equal')
    ax.axis("off")
    fig.patch.set_facecolor("white")
    fig.tight_layout()
    return fig


# =========================================================================
# TABLA DE SOLO LECTURA EN HTML
# =========================================================================
def tabla_html(df):
    filas_html = ""
    for _, fila in df.iterrows():
        celdas = "".join(f"<td style='padding:8px 14px; border-bottom:1px solid #E4E1D6;'>{v}</td>" for v in fila)
        filas_html += f"<tr>{celdas}</tr>"

    encabezados = "".join(
        f"<th style='padding:9px 14px; text-align:left; background-color:{NAVY}; "
        f"color:{CREAM}; font-family:\"Space Grotesk\",sans-serif; font-size:13px; "
        f"text-transform:uppercase; letter-spacing:0.03em;'>{col}</th>"
        for col in df.columns
    )

    html = f"""
    <div style="overflow-x:auto; border:1px solid #E4E1D6; border-radius:10px; margin-bottom:14px;">
    <table style="width:100%; border-collapse:collapse; background-color:#FFFFFF;
                   color:{NAVY}; font-family:'Inter',sans-serif; font-size:14px;">
        <thead><tr>{encabezados}</tr></thead>
        <tbody>{filas_html}</tbody>
    </table>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


# =========================================================================
# ENCABEZADO PRINCIPAL
# =========================================================================
col_logo, col_title = st.columns([0.07, 0.93])
with col_logo:
    st.markdown(f"<div style='font-size:38px;'>🏞️</div>", unsafe_allow_html=True)
with col_title:
    st.markdown(f"<h1 style='margin-bottom:0;'>LY<span style='color:{GOLD}'>GRAV</span> PRO</h1>"
                f"<p style='color:{NAVY_2}; margin-top:0;'>Gravity Dam Modeler · Lucero Yamile Silva de la Cruz</p>",
                unsafe_allow_html=True)
st.markdown("---")

st.sidebar.markdown(f"<h3 style='color:{GOLD};'>⚙️ Configuración de Entrada</h3>", unsafe_allow_html=True)

modo_entrada = st.sidebar.radio(
    "Selecciona cómo deseas ingresar la geometría:",
    ("Por Ángulos y Tramos", "Por Coordenadas (Tabla X, Y)")
)

puntos_x = []
puntos_y = []

# =========================================================================
# MODO 1: ÁNGULOS Y TRAMOS ENCADENADOS
# =========================================================================
if modo_entrada == "Por Ángulos y Tramos":
    st.sidebar.subheader("📐 Diseño por Componentes")

    b = st.sidebar.number_input("Ancho de la Cresta, b (m)", min_value=0.5, value=2.4, step=0.1)

    with st.sidebar.expander("⬅️ Talud Aguas Arriba (Izq)", expanded=True):
        num_tramos_izq = st.number_input("N° de tramos (subiendo)", min_value=1, max_value=4, value=2, step=1)
        tramos_izq = []

        for i in range(int(num_tramos_izq)):
            st.markdown(f"**Tramo {i+1}** (De abajo hacia arriba)")
            h_tramo = st.number_input(f"Altura Tramo {i+1} (m)", min_value=0.1, value=8.4 if i == 0 else 9.6, step=0.1, key=f"h_izq_{i}")
            ang_tramo = st.slider(f"Ángulo Tramo {i+1} (°)", min_value=0.1, max_value=90.0,
                                   value=90.0 if i == 0 else 70.0, step=0.1, key=f"ang_izq_{i}")
            tramos_izq.append((h_tramo, ang_tramo))

    with st.sidebar.expander("➡️ Talud Aguas Abajo (Der)", expanded=True):
        num_tramos_der = st.number_input("N° de tramos (bajando)", min_value=1, max_value=4, value=1, step=1)
        tramos_der = []

        for i in range(int(num_tramos_der)):
            st.markdown(f"**Tramo {i+1}** (De arriba hacia abajo)")
            h_tramo = st.number_input(f"Altura Tramo {i+1} (m)", min_value=0.1, value=18.0, step=0.1, key=f"h_der_{i}")
            ang_tramo = st.slider(f"Ángulo Tramo {i+1} (°)", min_value=0.1, max_value=90.0,
                                   value=50.0, step=0.1, key=f"ang_der_{i}")
            tramos_der.append((h_tramo, ang_tramo))

    x_act, y_act = 0.0, 0.0
    puntos_x.append(x_act)
    puntos_y.append(y_act)

    for h_t, ang_t in tramos_izq:
        if ang_t == 90.0:
            y_act += h_t
        else:
            y_act += h_t
            x_act += h_t / np.tan(np.radians(ang_t))
        puntos_x.append(x_act)
        puntos_y.append(y_act)

    x_act += b
    puntos_x.append(x_act)
    puntos_y.append(y_act)

    for h_t, ang_t in tramos_der:
        if ang_t == 90.0:
            y_act -= h_t
        else:
            y_act -= h_t
            x_act += h_t / np.tan(np.radians(ang_t))
        puntos_x.append(x_act)
        puntos_y.append(y_act)

    puntos_x.append(0.0)
    puntos_y.append(0.0)

# =========================================================================
# MODO 2: COORDENADAS MANUALES
# =========================================================================
else:
    st.sidebar.subheader("📊 Tabla de Coordenadas")
    st.info("Ingresa los vértices en sentido horario empezando desde el origen (0,0).")
    st.caption("Cada fila es un vértice. Usá **+ Agregar vértice** para sumar filas y 🗑 para quitar una.")

    if "vertices" not in st.session_state:
        _datos_iniciales = [
            (0.0, 0.0), (0.0, 18.0), (2.4, 18.0), (15.0, 0.0), (0.0, 0.0),
        ]
        st.session_state.vertices = [
            {"id": i, "x": x, "y": y} for i, (x, y) in enumerate(_datos_iniciales)
        ]
        st.session_state.vertices_next_id = len(_datos_iniciales)

    st.sidebar.markdown(
        f"<div style='display:flex; gap:8px; font-size:12px; color:{MUTED}; "
        f"padding:0 4px; margin-bottom:2px;'><div style='flex:1;'>X (m)</div>"
        f"<div style='flex:1;'>Y (m)</div><div style='width:34px;'></div></div>",
        unsafe_allow_html=True,
    )

    _id_a_borrar = None
    for v in st.session_state.vertices:
        c1, c2, c3 = st.sidebar.columns([1, 1, 0.4])
        with c1:
            v["x"] = st.number_input(
                f"X vértice {v['id']}", value=float(v["x"]), step=0.1,
                key=f"vx_{v['id']}", label_visibility="collapsed",
            )
        with c2:
            v["y"] = st.number_input(
                f"Y vértice {v['id']}", value=float(v["y"]), step=0.1,
                key=f"vy_{v['id']}", label_visibility="collapsed",
            )
        with c3:
            if st.button("🗑", key=f"del_{v['id']}", help="Quitar este vértice"):
                _id_a_borrar = v["id"]

    if _id_a_borrar is not None:
        st.session_state.vertices = [v for v in st.session_state.vertices if v["id"] != _id_a_borrar]
        st.rerun()

    if st.sidebar.button("➕ Agregar vértice", use_container_width=True):
        nuevo_id = st.session_state.vertices_next_id
        st.session_state.vertices.append({"id": nuevo_id, "x": 0.0, "y": 0.0})
        st.session_state.vertices_next_id += 1
        st.rerun()

    df_editado = pd.DataFrame(
        {"X (m)": [v["x"] for v in st.session_state.vertices],
         "Y (m)": [v["y"] for v in st.session_state.vertices]}
    )
    df_limpio = df_editado.dropna(subset=["X (m)", "Y (m)"])

    puntos_x = df_limpio["X (m)"].tolist()
    puntos_y = df_limpio["Y (m)"].tolist()

# ==========================================================
# PARÁMETROS HIDRÁULICOS Y DE MATERIALES
# ==========================================================
H_max = float(max(puntos_y)) if puntos_y else 10.0

with st.sidebar.expander("💧 Hidráulica", expanded=True):
    h_up = st.slider("Nivel aguas arriba (m)", min_value=0.0, max_value=H_max,
                      value=H_max - 2.0 if H_max > 2 else 0.0)
    h_down = st.slider("Nivel aguas abajo (m)", min_value=0.0, max_value=H_max,
                        value=2.0 if H_max > 2 else 0.0)

with st.sidebar.expander("🧱 Materiales y Coeficientes", expanded=False):
    gamma_c = st.number_input("Peso específico del concreto γc (kgf/m³)", min_value=1000.0, value=2300.0, step=50.0)
    gamma_w = st.number_input("Peso específico del agua γw (kgf/m³)", min_value=900.0, value=1000.0, step=10.0)
    mu = st.number_input("Coeficiente de fricción μ", min_value=0.1, max_value=1.0, value=0.75, step=0.05)
    L_presa = st.number_input("Longitud de análisis L (m)", min_value=0.5, value=1.0, step=0.5)

mostrar_fuerzas = st.sidebar.checkbox("Mostrar diagrama de fuerzas actuantes en Presa Llena", value=False)

# =========================================================================
# PESTAÑAS
# =========================================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Perfil Geométrico", "📋 Coordenadas", "🟦 Presa Vacía", "🌊 Presa Llena"
])

with tab1:
    st.caption("🔍 Usa la rueda del mouse para hacer zoom, arrastra para desplazarte, "
               "y doble clic para restablecer la vista — igual que en GeoGebra.")

    x_min = float(min(puntos_x) - 5) if puntos_x else -5.0
    x_max = float(max(puntos_x) + 5) if puntos_x else 15.0
    y_max_presa = float(max(puntos_y)) if puntos_y else 10.0

    px_perfil = puntos_x.copy()
    py_perfil = puntos_y.copy()

    if len(px_perfil) > 2 and px_perfil[-1] == px_perfil[0] and py_perfil[-1] == py_perfil[0]:
        px_perfil.pop()
        py_perfil.pop()

    fig_plotly = go.Figure()

    if len(px_perfil) >= 3:
        idx_cresta = py_perfil.index(max(py_perfil))
        puntos_x_izq = px_perfil[:idx_cresta + 1]
        puntos_y_izq = py_perfil[:idx_cresta + 1]
        puntos_x_der = px_perfil[idx_cresta:]
        puntos_y_der = py_perfil[idx_cresta:]

        idx_izq_ordenado = np.argsort(puntos_y_izq)
        puntos_x_izq_interp = np.array(puntos_x_izq)[idx_izq_ordenado]
        puntos_y_izq_interp = np.array(puntos_y_izq)[idx_izq_ordenado]

        idx_der_ordenado = np.argsort(puntos_y_der)
        puntos_x_der_interp = np.array(puntos_x_der)[idx_der_ordenado]
        puntos_y_der_interp = np.array(puntos_y_der)[idx_der_ordenado]

        if h_up > 0 and len(puntos_x_izq_interp) > 0:
            x_linea_up = float(np.interp(h_up, puntos_y_izq_interp, puntos_x_izq_interp))
            x_talud_up = [x for x, y in zip(puntos_x_izq, puntos_y_izq) if y <= h_up]
            y_talud_up = [y for x, y in zip(puntos_x_izq, puntos_y_izq) if y <= h_up]

            x_agua_up = [x_min, x_min, x_linea_up] + x_talud_up[::-1] + [x_min]
            y_agua_up = [0.0, h_up, h_up] + y_talud_up[::-1] + [0.0]

            fig_plotly.add_trace(go.Scatter(
                x=x_agua_up, y=y_agua_up, fill="toself",
                fillcolor="rgba(84,184,176,0.30)",
                line=dict(color=TEAL, width=2),
                mode="lines", name="Agua aguas arriba", hoverinfo="skip",
            ))

        if h_down > 0 and len(puntos_x_der_interp) > 0:
            x_linea_down = float(np.interp(h_down, puntos_y_der_interp, puntos_x_der_interp))
            x_talud_down = [x for x, y in zip(puntos_x_der, puntos_y_der) if y <= h_down]
            y_talud_down = [y for x, y in zip(puntos_x_der, puntos_y_der) if y <= h_down]

            x_agua_down = [x_linea_down] + x_talud_down + [x_max, x_max, x_linea_down]
            y_agua_down = [h_down] + y_talud_down + [0.0, h_down, h_down]

            fig_plotly.add_trace(go.Scatter(
                x=x_agua_down, y=y_agua_down, fill="toself",
                fillcolor="rgba(147,162,184,0.30)",
                line=dict(color=MUTED, width=2),
                mode="lines", name="Agua aguas abajo", hoverinfo="skip",
            ))

    if len(puntos_x) >= 3:
        fig_plotly.add_trace(go.Scatter(
            x=puntos_x + [puntos_x[0]], y=puntos_y + [puntos_y[0]],
            fill="toself", fillcolor="#E4E1D6",
            line=dict(color=NAVY, width=2.5),
            mode="lines+markers", marker=dict(size=6, color=NAVY_2),
            name="Presa de Concreto",
        ))

    fig_plotly.update_layout(
        title="Visualización Dinámica de Presa Flexible",
        xaxis_title="Distancia Horizontal / Ancho (m)",
        yaxis_title="Elevación / Altura (m)",
        template="plotly_white",
        showlegend=False,
        height=620,
        margin=dict(l=40, r=20, t=60, b=40),
        dragmode="pan",
        paper_bgcolor=CREAM,
        plot_bgcolor="#FFFFFF",
        font=dict(color=NAVY),
        title_font=dict(color=NAVY),
    )
    fig_plotly.update_xaxes(scaleanchor="y", scaleratio=1, gridcolor="rgba(11,29,58,0.08)",
                             color=NAVY, zerolinecolor="rgba(11,29,58,0.15)")
    fig_plotly.update_yaxes(gridcolor="rgba(11,29,58,0.08)", color=NAVY,
                             zerolinecolor="rgba(11,29,58,0.15)")

    st.plotly_chart(
        fig_plotly, use_container_width=True, theme=None,
        config={"scrollZoom": True, "displaylogo": False,
                "modeBarButtonsToAdd": ["drawline"], "doubleClick": "reset"},
    )

with tab2:
    if modo_entrada != "Por Ángulos y Tramos":
        tabla_html(df_editado)
    else:
        df_visual = pd.DataFrame({"X (m)": puntos_x, "Y (m)": puntos_y})
        tabla_html(df_visual)


# =========================================================================
# CÁLCULOS DE ESTABILIDAD
# =========================================================================
puntos_x_calc = puntos_x.copy()
puntos_y_calc = puntos_y.copy()
if len(puntos_x_calc) > 2 and puntos_x_calc[-1] == puntos_x_calc[0] and puntos_y_calc[-1] == puntos_y_calc[0]:
    puntos_x_calc.pop()
    puntos_y_calc.pop()

try:
    if len(puntos_x_calc) < 3:
        raise ValueError("Se necesitan al menos 3 vértices para definir la geometría de la presa.")
    res_vacia = calcular_presa_vacia(puntos_x_calc, puntos_y_calc, gamma_c=gamma_c, L=L_presa)
    res_llena = calcular_presa_llena(res_vacia, h_up, h_down, gamma_w=gamma_w, mu=mu, L=L_presa)
    error_calculo = None
except Exception as e:
    res_vacia, res_llena = None, None
    error_calculo = str(e)

with tab3:
    st.markdown("<div class='lg-banner'>① ANÁLISIS A PRESA VACÍA</div>", unsafe_allow_html=True)

    if error_calculo:
        st.error(f"No se pudo calcular: {error_calculo}")
    else:
        st.markdown("**Descomposición en figuras geométricas**")
        tabla_html(res_vacia["df"])

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"<div class='lg-card'><h4>Peso total Wт</h4><div class='lg-val'>{res_vacia['W_T']:,.0f} kgf</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='lg-card'><h4>Centroide (desde punta)</h4><div class='lg-val'>{res_vacia['x_cg_punta']:.5f} m</div></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='lg-card'><h4>Excentricidad e</h4><div class='lg-val'>{res_vacia['e']:.5f} m</div></div>", unsafe_allow_html=True)
        with c4:
            st.markdown(f"<div class='lg-card'><h4>Momento Me</h4><div class='lg-val'>{res_vacia['M_e']:,.2f} kgf·m</div></div>", unsafe_allow_html=True)

        st.markdown("**Esfuerzos en la base** &nbsp;·&nbsp; (−) tracción &nbsp;·&nbsp; (+) compresión")
        c1, c2 = st.columns(2)
        cls_talon = "lg-bad" if res_vacia['sigma_talon'] < 0 else "lg-ok"
        cls_punta = "lg-bad" if res_vacia['sigma_punta'] < 0 else "lg-ok"
        with c1:
            st.markdown(f"<div class='lg-card {cls_talon}'><h4>σ Talón</h4><div class='lg-val'>{res_vacia['sigma_talon']:,.1f} kgf/m²</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='lg-card {cls_punta}'><h4>σ Punta</h4><div class='lg-val'>{res_vacia['sigma_punta']:,.1f} kgf/m²</div></div>", unsafe_allow_html=True)

        fig_v = dibujar_diagrama_esfuerzos(res_vacia['sigma_talon'], res_vacia['sigma_punta'],
                                            res_vacia['b_base'], "Diagrama de Esfuerzos — Presa Vacía",
                                            puntos_x=puntos_x_calc, puntos_y=puntos_y_calc)
        st.pyplot(fig_v)

with tab4:
    st.markdown("<div class='lg-banner'>② ANÁLISIS A PRESA LLENA</div>", unsafe_allow_html=True)

    if error_calculo:
        st.error(f"No se pudo calcular: {error_calculo}")
    else:
        st.markdown("**Empuje hidrostático — componente HORIZONTAL**")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='lg-card'><h4>F↑ Horizontal aguas arriba</h4><div class='lg-val'>{res_llena['F_up']:,.0f} kgf</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='lg-card'><h4>F↓ Horizontal aguas abajo</h4><div class='lg-val'>{res_llena['F_down']:,.0f} kgf</div></div>", unsafe_allow_html=True)

        st.markdown("**Empuje hidrostático — componente VERTICAL** &nbsp;·&nbsp; "
                     "*(peso del agua apoyada sobre el talud; es 0 si la cara es vertical)*")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"<div class='lg-card'><h4>Fv↑ Vertical aguas arriba</h4><div class='lg-val'>{res_llena['Fv_up']:,.0f} kgf</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='lg-card'><h4>Fv↓ Vertical aguas abajo</h4><div class='lg-val'>{res_llena['Fv_down']:,.0f} kgf</div></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='lg-card'><h4>Subpresión U</h4><div class='lg-val'>{res_llena['U']:,.0f} kgf</div></div>", unsafe_allow_html=True)

        st.markdown("**Momentos respecto a la punta**")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"<div class='lg-card'><h4>ΣM estabilizadores</h4><div class='lg-val'>{res_llena['Sum_M_Estabilizadores']:,.0f} kgf·m</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='lg-card'><h4>ΣM de volteo</h4><div class='lg-val'>{res_llena['Sum_M_Volteo']:,.0f} kgf·m</div></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='lg-card'><h4>Resultante vertical Rv</h4><div class='lg-val'>{res_llena['R_v']:,.0f} kgf</div></div>", unsafe_allow_html=True)
        st.caption("Rv = Peso propio (Wт) + Fv↑ + Fv↓ − Subpresión (U). "
                   "ΣM estabilizadores incluye el peso propio, los momentos de Fv↑ y Fv↓, "
                   "y el empuje horizontal aguas abajo (si existe).")

        st.markdown("**Factores de seguridad**")
        c1, c2 = st.columns(2)
        cls_v = "lg-ok" if res_llena['Fsv'] >= 1.5 else "lg-bad"
        cls_d = "lg-ok" if res_llena['Fsd'] >= 1.5 else "lg-bad"
        with c1:
            estado_v = "✓ Estable" if res_llena['Fsv'] >= 1.5 else "✗ Revisar"
            st.markdown(f"<div class='lg-card {cls_v}'><h4>Fsv (volteo) — {estado_v}</h4><div class='lg-val'>{res_llena['Fsv']:.2f}</div></div>", unsafe_allow_html=True)
        with c2:
            estado_d = "✓ Estable" if res_llena['Fsd'] >= 1.5 else "✗ Revisar"
            st.markdown(f"<div class='lg-card {cls_d}'><h4>Fsd (deslizamiento) — {estado_d}</h4><div class='lg-val'>{res_llena['Fsd']:.2f}</div></div>", unsafe_allow_html=True)

        st.markdown("**Posición de la resultante y esfuerzos finales**")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='lg-card'><h4>x'' (desde punta)</h4><div class='lg-val'>{res_llena['x_segundo']:.5f} m</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='lg-card'><h4>Excentricidad e</h4><div class='lg-val'>{res_llena['e_llena']:.5f} m</div></div>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        cls_talon_l = "lg-bad" if res_llena['sigma_talon_l'] < 0 else "lg-ok"
        cls_punta_l = "lg-bad" if res_llena['sigma_punta_l'] < 0 else "lg-ok"
        with c1:
            st.markdown(f"<div class='lg-card {cls_talon_l}'><h4>σ Talón</h4><div class='lg-val'>{res_llena['sigma_talon_l']:,.1f} kgf/m²</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='lg-card {cls_punta_l}'><h4>σ Punta</h4><div class='lg-val'>{res_llena['sigma_punta_l']:,.1f} kgf/m²</div></div>", unsafe_allow_html=True)

        fig_l = dibujar_diagrama_esfuerzos(res_llena['sigma_talon_l'], res_llena['sigma_punta_l'],
                                            res_vacia['b_base'], "Diagrama de Esfuerzos — Presa Llena",
                                            puntos_x=puntos_x_calc, puntos_y=puntos_y_calc)
        st.pyplot(fig_l)

        if mostrar_fuerzas:
            x_centroide_abs = res_vacia['x_max'] - res_vacia['x_cg_punta']
            fig_f = dibujar_diagrama_fuerzas(
                puntos_x_calc, puntos_y_calc, h_up, h_down,
                x_centroide_abs, res_vacia['W_T'],
                res_llena['F_up'], res_llena['F_down'], res_llena['U'],
                Fv_up=res_llena['Fv_up'], Fv_down=res_llena['Fv_down'],
                cx_Fv_up=res_llena['cx_Fv_up'], cx_Fv_down=res_llena['cx_Fv_down'],
            )
            st.pyplot(fig_f)
            

