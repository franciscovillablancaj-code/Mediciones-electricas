import streamlit as st
import pandas as pd
import os
from datetime import date

# Configuración de la página
st.set_page_config(page_title="Registro de Mediciones", layout="wide")

ARCHIVO_EXCEL = "Base_Datos_Mediciones.xlsx"

# LISTA COMPLETA DE EQUIPOS
lista_equipos = [
    "Seleccione un equipo", "10-EKR10-AP001-MO1", "10-GHA11-AP001-M01", "10-GHA12-AP001-M01", 
    "10-GHA13-AP001-M01", "10-GKB11-AP001-M01", "10-GKB12-AP001-M01", "10-GME41-AP001-M01", 
    "10-GME42-AP001-M01", "10-GRC10-AN001-M01", "10-GRC20-AN001-M01", "10-HAN11-AP001-M01", 
    "10-HAN12-AP001-M01", "10-HAN40-AP001-M01", "10-HHL10-AN001-M01", "HJQ11-AN001-M01", 
    "HJQ12-AN001-M01", "10-LAC11-AP001-M01", "10-LAC12-AP001-M01", "10-LCP21-AP001-M01", 
    "10-LCP22-AP001-M01", "MBH10-AN001-M01", "MBH10-AN002-M01", "MBH15-AN001-M01", 
    "MBH15-AN002-M01", "MBJ20-AE001-M01", "11-MBR01-AE001", "11-MBR01-AE002", 
    "11-MBR01-AE003", "1-MBR01-AE004", "11-MBR02-AE001", "MBU30-AP010-M01", 
    "MBV11-AN001-M01", "MBV11-AN002-M01", "MBV20-AP001-M01", "MBV20-AP002-M01", 
    "MBV30-AP001-M01", "MBX11-AP001-M01", "MBX12-AP001-M01", "MKA10-AN001-M01", 
    "MKA10-AN002-M01", "10-PGB10-AN001-M01", "10-PGB10-AN002-M01", "10-PGB10-AN003-M01", 
    "10-PGB10-AN004-M01", "10-PGB10-AN005-M01", "10-PGB10-AN006-M01", "10-PGB10-AN007-M01", 
    "10-PGB10-AN008-M01", "10-PGB10-AN009-M01", "10-PGB10-AN010-M01", "10-PGB10-AN011-M01", 
    "10-PGB10-AN012-M01", "10-PGB10-AN013-M01", "10-PGB10-AN014-M01", "10-PGB10-AN015-M01", 
    "10-PGB10-AN016-M01", "10-PGB10-AN017-M01", "10-PGB10-AN018-M01", "10-PGB10-AN019-M01", 
    "10-PGB10-AN020-M01", "10-PGB10-AN021-M01", "10-PGB10-AN022-M01", "10-PGB10-AN023-M01", 
    "10-PGB10-AN024-M01", "10-PGB11-AP001-M01", "10-PGB12-AP001-M01", "11-QHL01-AE001", 
    "11-QHL01-AE002", "SAE11-AN001-M01", "SAE12-AN001-M01", "SAE27-AN001-M01", 
    "SAE28-AN001-M01", "SAE41-AN001-M01", "SAE42-AN001-M01", "SAE71-AN001-M01", 
    "SAE72-AN001-M01", "SAF11-AN001-M01", "SAF12-AN001-M01", "10-SGA10-AP002-M01", 
    "10-SGA10-AP003-M01"
]

st.title("⚡ Sistema de Registro de Mediciones")

# --- FORMULARIO PRINCIPAL ---
with st.form("form_mediciones", clear_on_submit=True):
    col_head1, col_head2 = st.columns(2)
    with col_head1:
        equipo = st.selectbox("Seleccione el equipo", lista_equipos)
    with col_head2:
        fecha = st.date_input("Fecha de medición", date.today())

    st.markdown("---")
    col_izq, col_der = st.columns(2)

    with col_izq:
        st.subheader("🔹 Alimentación")
        
        alim_l1_l2 = st.text_input("L1-L2 (MΩ)")
        alim_l1_l3 = st.text_input("L1-L3 (MΩ)")
        alim_l2_l3 = st.text_input("L2-L3 (MΩ)")
        st.markdown("### Aislamientos")
        alim_l1_t = st.text_input("L1-T (MΩ)")
        alim_l2_t = st.text_input("L2-T (MΩ)")
        alim_l3_t = st.text_input("L3-T (MΩ)")
        st.write("")

        volt_l1 = st.text_input("L1-T (V)")
        volt_l2 = st.text_input("L2-T (V)")
        volt_l3 = st.text_input("L3-T (V)")
        volt_l1_l2 = st.text_input("L1-L2 (V)")
        volt_l1_l3 = st.text_input("L1-L3 (V)")
        volt_l2_l3 = st.text_input("L2-L3 (V)")

    with col_der:
        st.subheader("🔸 Motor")
        res_u = st.text_input("Res. Dev U (Ω)")
        res_v = st.text_input("Res. Dev V (Ω)")
        res_w = st.text_input("Res. Dev W (Ω)")
        st.write("")
        mot_u_v = st.text_input("Ais. Mot U-V (MΩ)")
        mot_u_w = st.text_input("Ais. Mot U-W (MΩ)")
        mot_v_w = st.text_input("Ais. Mot V-W (MΩ)")
        mot_u_t = st.text_input("Ais. Mot U-T (MΩ)")
        mot_v_t = st.text_input("Ais. Mot V-T (MΩ)")
        mot_w_t = st.text_input("Ais. Mot W-T (MΩ)")
        dar = st.text_input("DAR")
        st.write("")
        corr_p = st.text_input("Corr. P (A)")
        corr_u = st.text_input("Corr. L1 (A)")
        corr_v = st.text_input("Corr. L2 (A)")
        corr_w = st.text_input("Corr. L3 (A)")

    submitted = st.form_submit_button("💾 GUARDAR REGISTRO", use_container_width=True)

if submitted:
    if equipo == "Seleccione un equipo":
        st.error("⚠️ Debes seleccionar un equipo.")
    else:
        datos = {
            "Fecha": fecha, "Equipo": equipo,
            "Alim L1-L2": alim_l1_l2, "Alim L1-L3": alim_l1_l3, "Alim L2-L3": alim_l2_l3,
            "Alim L1-T": alim_l1_t, "Alim L2-T": alim_l2_t, "Alim L3-T": alim_l3_t,
            "Volt L1": volt_l1, "Volt L2": volt_l2, "Volt L3": volt_l3,
            "Volt L1-L2": volt_l1_l2, "Volt L1-L3": volt_l1_l3, "Volt L2-L3": volt_l2_l3,
            "Res Dev U": res_u, "Res Dev V": res_v, "Res Dev W": res_w,
            "Mot U-V": mot_u_v, "Mot U-W": mot_u_w, "Mot V-W": mot_v_w,
            "Mot U-T": mot_u_t, "Mot V-T": mot_v_t, "Mot W-T": mot_w_t,
            "DAR": dar, "Corr P": corr_p, "Corr L1": corr_u, "Corr L2": corr_v, "Corr L3": corr_w
        }
        try:
            df_nuevo = pd.DataFrame([datos])
            if os.path.exists(ARCHIVO_EXCEL):
                df_existente = pd.read_excel(ARCHIVO_EXCEL)
                df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
            else:
                df_final = df_nuevo
            df_final.to_excel(ARCHIVO_EXCEL, index=False)
            st.success(f"✅ Guardado: {equipo}")
            st.balloons()
        except Exception as e:
            st.error(f"❌ Error: {e}")

# --- SECCIÓN DE DESCARGA Y VISTA ---
st.markdown("---")
if os.path.exists(ARCHIVO_EXCEL):
    df_ver = pd.read_excel(ARCHIVO_EXCEL)
    col_btn1, col_btn2 = st.columns([1, 3])
    
    with col_btn1:
        with open(ARCHIVO_EXCEL, "rb") as file:
            st.download_button(
                label="📥 Descargar Excel",
                data=file,
                file_name=ARCHIVO_EXCEL,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    
    if st.checkbox("Ver registros históricos"):
        st.dataframe(df_ver)
