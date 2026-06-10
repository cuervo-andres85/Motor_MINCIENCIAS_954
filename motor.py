# ============================================================
#  INGRESO DE DATOS — PORTAFOLIO DEL GRUPO DE INVESTIGACIÓN
# ============================================================
#  Instrucciones:
#  1. Escriba el número de productos en la ventana de
#     observación para cada código que aplique a su grupo.
#  2. Si no tiene productos de un tipo, déjelo en 0
#     o simplemente no lo incluya.
#  3. Los códigos corresponden exactamente a los que
#     aparecen en su reporte GrupLac de Minciencias.
#  4. La edad del grupo es el número de años desde su
#     fecha de creación oficial hasta diciembre de 2023.
# ============================================================

edad_grupo = 11   # ← Cambie este valor por la edad real de su grupo

mi_portafolio = {

    # ── GENERACIÓN DE NUEVO CONOCIMIENTO ─────────────────────

    # Generacion de nuevo conocimiento TOP
    'ART_OPEN_A1': 0,   # Artículo open access Q1
    'ART_OPEN_A2': 0,   # Artículo open access Q2
    'ART_A1':      0,   # Artículo Q1
    'ART_A2':      0,   # Artículo Q2
    'LIB_A1':      0,   # Libro calidad A1
    'LIB_A':       0,   # Libro calidad A
    'CAP_LIB_A1':  0,   # Capítulo calidad A1
    'CAP_LIB_A':   0,   # Capítulo calidad A
    'P_A1':        0,   # Patente obtenida internacional
    'P_A2':        0,   # Patente obtenida nacional
    'M_A1':        0,   # Modelo utilidad obtenido internacional
    'M_A2':        0,   # Modelo utilidad obtenido nacional
    'VV_A1':       0,   # Variedad vegetal A1
    'VV_A2':       0,   # Variedad vegetal A2
    'VA_A':        0,   # Nueva raza animal
    'AAD_A1':      0,   # Invest-Creación A1
    'AAD_A':       0,   # Invest-Creación A
    'RNL_A':       0,   # Regulación/norma/legislación A

    # Generacion de nuevo conocimiento A

    'ART_OPEN_B':  0,   # Artículo open access Q3
    'ART_B':       0,   # Artículo Q3
    'ART_OPEN_C':  0,   # Artículo open access Q4
    'ART_C':       0,   # Artículo Q4
    'LIB_B':       0,   # Libro Q3
    'CAP_LIB_B':   0,   # Capítulo Q3
    'P_A3':        0,   # Patente en trámite internacional
    'P_A4':        0,   # Patente en trámite nacional
    'M_A3':        0,   # Modelo utilidad trámite internacional
    'M_A4':        0,   # Modelo utilidad trámite nacional
    'VV_A3':       0,   # Variedad vegetal A3
    'VV_A4':       0,   # Variedad vegetal A4
    'VA_B':        0,   # Población mejorada razas pecuarias
    'AAD_B':       0,   # Invest-Creación B
    'DI_A':        0,   # Diseño industrial registrado
    'ECI':         0,   # Esquema de circuito integrado
    'PP':          0,   # Planta piloto
    'PI':          0,   # Prototipo industrial
    'SD':          0,   # Signo distintivo
    'SE':          0,   # Secreto empresarial
    'EBT_A':       0,   # Empresa de base tecnológica A
    'ICC_A':       0,   # Empresa creativa y cultural A
    'IG_A1':       0,   # Innovación en gestión empresarial A1
    'IG_A2':       0,   # Innovación en gestión empresarial A2
    'RNL_B':       0,   # Regulación/norma/legislación B
    'RNR':         0,   # Normatividad espectro radioeléctrico


    # Generacion de nuevo conocimiento B

    'ART_OPEN_D':  0,   # Artículo open access sin cuartil
    'ART_D':       0,   # Artículo sin cuartil
    'N_A1':        0,   # Nota científica Q1
    'N_A2':        0,   # Nota científica Q2
    'N_B':         0,   # Nota científica Q3
    'N_C':         0,   # Nota científica Q4
    'N_D':         0,   # Nota científica sin cuartil
    'LIB_C':       0,   # Libro sin cuartil
    'CAP_LIB_C':   0,   # Capítulo sin cuartil
    'LIB_FOR1':    0,   # Libro de formación Q1
    'P_B1':        0,   # Patente invención B1
    'P_B2':        0,   # Patente invención B2
    'P_B3':        0,   # Patente invención B3
    'P_B4':        0,   # Patente invención B4
    'P_B5':        0,   # Patente invención B5
    'P_C':         0,   # Patente invención C
    'M_B1':        0,   # Modelo utilidad B1
    'M_B2':        0,   # Modelo utilidad B2
    'M_B3':        0,   # Modelo utilidad B3
    'M_B4':        0,   # Modelo utilidad B4
    'M_B5':        0,   # Modelo utilidad B5
    'M_C':         0,   # Modelo utilidad C
    'VV_B1':       0,   # Variedad vegetal B1
    'VV_B2':       0,   # Variedad vegetal B2
    'VV_B3':       0,   # Variedad vegetal B3
    'VV_B4':       0,   # Variedad vegetal B4
    'AAD_C':       0,   # Invest-Creación C
    'DI_B':        0,   # Diseño industrial en trámite
    'SF':          0,   # Software registrado
    'PN':          0,   # Producto nutracéutico/fitoterapéutico
    'CC':          0,   # Colección científica
    'NRC_A':       0,   # Nuevo registro científico A
    'NRC_B':       0,   # Nuevo registro científico B
    'EBT_B':       0,   # Empresa de base tecnológica B
    'ICC_B':       0,   # Empresa creativa y cultural B
    'IG_B1':       0,   # Innovación en gestión empresarial B1
    'IG_B2':       0,   # Innovación en gestión empresarial B2
    'IPP':         0,   # Innovación en procedimientos y servicios
    'RNT':         0,   # Norma técnica
    'RNPC':        0,   # Guía de práctica clínica
    'GMCF':        0,   # Guía de manejo clínico forense
    'MADV':        0,   # Manual atención diferencial a víctimas
    'PAU':         0,   # Protocolo de atención a usuarios
    'PVE':         0,   # Protocolo de vigilancia epidemiológica
    'AL':          0,   # Acuerdo de Ley
    'RNPL':        0,   # Proyecto de Ley
    'CT':          0,   # Concepto técnico
    'MR':          0,   # Acuerdo de licencia I+C

    # ── APROPIACIÓN SOCIAL DEL CONOCIMIENTO ──────────────────

    'FIS':         0,   # Formación e ideación social
    'GPP_A':       0,   # Generación participación pública A
    'GPP_B':       0,   # Generación participación pública B
    'GPP_C':       0,   # Generación participación pública C
    'FCP_A':       0,   # Formación cadenas productivas A
    'FCP_B':       0,   # Formación cadenas productivas B
    'FCP_C':       0,   # Formación cadenas productivas C
    'TCCG_A':      0,   # Transferencia conocimiento científico A
    'TCCG_B':      0,   # Transferencia conocimiento científico B
    'TCCG_C':      0,   # Transferencia conocimiento científico C
    'TCCG_D':      0,   # Transferencia conocimiento científico D

    # ── DIVULGACIÓN PÚBLICA DE LA CIENCIA ────────────────────

    'EC_A':        0,   # Evento científico tipo A
    'EC_B':        0,   # Evento científico tipo B
    'RC_A':        0,   # Red de conocimiento A
    'RC_B':        0,   # Red de conocimiento B
    'TC_A':        0,   # Taller de creación A
    'TC_B':        0,   # Taller de creación B
    'TC_C':        0,   # Taller de creación C
    'ECA_A':       0,   # Evento artístico/arquitectura/diseño A
    'ECA_B':       0,   # Evento artístico/arquitectura/diseño B
    'WP':          0,   # Working paper
    'NSG':         0,   # Nueva secuencia genética
    'ERL':         0,   # Edición revista/libro de divulgación
    'IFI':         0,   # Informe final de investigación
    'INF':         0,   # Informe técnico
    'CON_CT':      0,   # Consultoría científico-tecnológica
    'CON_AAD':     0,   # Consultoría arte/arquitectura/diseño
    'PEE_A1':      0,   # Publicación editorial nacional A1
    'PEE_A2':      0,   # Publicación editorial nacional A2
    'PEE_B1':      0,   # Publicación editorial regional B1
    'PEE_B2':      0,   # Publicación editorial regional B2
    'PEE_C1':      0,   # Publicación editorial local C1
    'PEE_C2':      0,   # Publicación editorial local C2
    'PCD_A1':      0,   # Producción contenido digital A1
    'PCD_A2':      0,   # Producción contenido digital A2
    'PCD_B1':      0,   # Producción contenido digital B1
    'PCD_B2':      0,   # Producción contenido digital B2
    'PCD_C1':      0,   # Producción contenido digital C1
    'PCD_C2':      0,   # Producción contenido digital C2
    'TRM_A1':      0,   # Producción transmedia A1
    'TRM_A2':      0,   # Producción transmedia A2
    'TRM_B1':      0,   # Producción transmedia B1
    'TRM_B2':      0,   # Producción transmedia B2
    'TRM_C1':      0,   # Producción transmedia C1
    'TRM_C2':      0,   # Producción transmedia C2
    'DW_A1':       0,   # Desarrollo web A1
    'DW_A2':       0,   # Desarrollo web A2
    'DW_B1':       0,   # Desarrollo web B1
    'DW_B2':       0,   # Desarrollo web B2
    'DW_C1':       0,   # Desarrollo web C1
    'DW_C2':       0,   # Desarrollo web C2
    'LIB_FOR2':    0,   # Libro de formación Q2
    'LIB_FOR3':    0,   # Libro de formación Q3
    'BOL':         0,   # Boletín divulgativo
    'LIB_DIV':     0,   # Libro de divulgación
    'GC':          0,   # Generación de contenido
    'MAN_GUI':     0,   # Manual/guía especializada

    # ── FORMACIÓN DE RECURSO HUMANO ───────────────────────────

    # Tipo A — peso ×1.0 en IndGrupo (requiere doctorado propio
    # o alianza formal con otra IES)
    'TD_A':        0,   # Tesis doctoral dirigida
    'TD_B':        0,   # Tesis doctoral co-dirigida
    'AP_A':        0,   # Creacion de Doctorados
    'AP_C':        0,   # Creacion de cursos de Doctorados

    # Tipo B — peso ×0.2 en IndGrupo
    'TM_A':        0,   # Tesis de maestría Meritoria o Laureada
    'TM_B':        0,   # Tesis de maestría Aprobada
    'TP_A':        0,   # Trabajo de pregrado Meritorio o laureado
    'TP_B':        0,   # Trabajo de pregrado aprobado
    'PID_A':       0,   # Proyecto I+D con calidad A
    'PID_B':       0,   # Proyecto I+D con calidad B
    'PID_C':       0,   # Proyecto I+D con calidad C
    'PIC_A':       0,   # Proyecto I+Creación con calidad A
    'PIC_B':       0,   # Proyecto I+Creación con calidad B
    'PIC_C':       0,   # Proyecto I+Creación con calidad C
    'PF_A':        0,   # Proyecto IDI con formación A
    'PF_B':        0,   # Proyecto IDI con formación B
    'PE':          0,   # Proyecto de extensión y resp. social
    'AP_B':        0,   # Creacion de programas de maestria
    'AP_D':        0,   # Creacion de cursos de maestria
    'APO':         0,   # Asesoría programa Ondas

}

# ── Verificación rápida de entrada ───────────────────────────
productos_activos = {k: v for k, v in mi_portafolio.items() if v > 0}
print(f"Grupo registrado con {len(productos_activos)} tipos de "
      f"productos activos y {edad_grupo} años de existencia.")
print(f"Total de productos ingresados: {sum(productos_activos.values())}")
