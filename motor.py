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


"""
motor_minciencias.py  —  v2.0  (COMPLETO 169 productos)
========================================================
Motor del modelo de medición de grupos de investigación
Minciencias 2024 — Convocatoria 954 / Modelo M601PR04G01
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

CALIDAD_PESO = {
    'TOP':  3.7,
    'A':    2.3,
    'B':    0.4,
    'ASC':  1.5,
    'DPC':  0.5,
    'FRHA': 1.0,
    'FRHB': 0.2,
}

PRODUCTOS = pd.DataFrame([
    # GNC — Artículos open access
    ('ART_OPEN_A1','Artículo open access Q1',          'GNC','TOP', 10,  100,7),
    ('ART_OPEN_A2','Artículo open access Q2',          'GNC','TOP',  6,  100,7),
    ('ART_OPEN_B', 'Artículo open access Q3',          'GNC','A',   3.5, 100,7),
    ('ART_OPEN_C', 'Artículo open access Q4',          'GNC','A',   2.0, 100,7),
    ('ART_OPEN_D', 'Artículo open access sin cuartil', 'GNC','B',  10,     5,7),
    # GNC — Artículos de investigación
    ('ART_A1',     'Artículo de investigación Q1',     'GNC','TOP', 9.5, 100,7),
    ('ART_A2',     'Artículo de investigación Q2',     'GNC','TOP', 5.5, 100,7),
    ('ART_B',      'Artículo de investigación Q3',     'GNC','A',   3.0, 100,7),
    ('ART_C',      'Artículo de investigación Q4',     'GNC','A',   1.5, 100,7),
    ('ART_D',      'Artículo de investigación sin Q',  'GNC','B',   9.0,   5,7),
    # GNC — Notas científicas (siempre Tipo B)
    ('N_A1',       'Nota científica Q1',               'GNC','B',  10,    5,7),
    ('N_A2',       'Nota científica Q2',               'GNC','B',   8.5,  5,7),
    ('N_B',        'Nota científica Q3',               'GNC','B',   6.0,  5,7),
    ('N_C',        'Nota científica Q4',               'GNC','B',   4.0,  5,7),
    ('N_D',        'Nota científica sin cuartil',      'GNC','B',   2.0,  5,5),
    # GNC — Libros resultado de investigación (categoría dinámica)
    ('LIB_A1',     'Libro resultado investigación Q1', 'GNC','TOP',10,   300,7),
    ('LIB_A',      'Libro resultado investigación Q2', 'GNC','TOP', 9,   300,7),
    ('LIB_B',      'Libro resultado investigación Q3', 'GNC','A',   8,   300,7),
    ('LIB_C',      'Libro resultado investigación s/Q','GNC','B',  10,    15,7),
    # GNC — Capítulos de libro
    ('CAP_LIB_A1', 'Capítulo de libro Q1',             'GNC','TOP',10,    60,5),
    ('CAP_LIB_A',  'Capítulo de libro Q2',             'GNC','TOP', 9,    60,5),
    ('CAP_LIB_B',  'Capítulo de libro Q3',             'GNC','A',   8,    60,5),
    ('CAP_LIB_C',  'Capítulo de libro sin cuartil',    'GNC','B',  10,     3,5),
    # GNC — Libro de formación
    ('LIB_FOR1',   'Libro de formación Q1',            'GNC','B',  10,    60,7),
    # GNC — Patentes de invención
    ('P_A1',       'Patente invención obtenida intl.', 'GNC','TOP',10,   500,10),
    ('P_A2',       'Patente invención obtenida nac.',  'GNC','TOP', 7,   500,10),
    ('P_A3',       'Patente invención trámite intl.',  'GNC','A',   6,   500,10),
    ('P_A4',       'Patente invención trámite nac.',   'GNC','A',   5.5, 500,10),
    ('P_B1',       'Patente invención B1',             'GNC','B',   5.0, 500,10),
    ('P_B2',       'Patente invención B2',             'GNC','B',   3.5, 500,10),
    ('P_B3',       'Patente invención B3',             'GNC','B',   3.0, 500,10),
    ('P_B4',       'Patente invención B4',             'GNC','B',   2.6, 500,10),
    ('P_B5',       'Patente invención B5',             'GNC','B',   2.5, 500,10),
    ('P_C',        'Patente invención C',              'GNC','B',   1.8, 500,10),
    # GNC — Modelos de utilidad
    ('M_A1',       'Modelo utilidad obtenido intl.',   'GNC','TOP', 6,   500,10),
    ('M_A2',       'Modelo utilidad obtenido nac.',    'GNC','TOP', 4.2, 500,10),
    ('M_A3',       'Modelo utilidad trámite intl.',    'GNC','A',   3.6, 500,10),
    ('M_A4',       'Modelo utilidad trámite nac.',     'GNC','A',   3.33,500,10),
    ('M_B1',       'Modelo utilidad B1',               'GNC','B',   3.0, 500,10),
    ('M_B2',       'Modelo utilidad B2',               'GNC','B',   2.1, 500,10),
    ('M_B3',       'Modelo utilidad B3',               'GNC','B',   1.8, 500,10),
    ('M_B4',       'Modelo utilidad B4',               'GNC','B',   1.7, 500,10),
    ('M_B5',       'Modelo utilidad B5',               'GNC','B',   1.5, 500,10),
    ('M_C',        'Modelo utilidad C',                'GNC','B',   1.1, 500,10),
    # GNC — Variedades vegetales
    ('VV_A1',      'Variedad vegetal A1',              'GNC','TOP',10,   300,10),
    ('VV_A2',      'Variedad vegetal A2',              'GNC','TOP', 8,   300,10),
    ('VV_A3',      'Variedad vegetal A3',              'GNC','A',   5.0, 300,10),
    ('VV_A4',      'Variedad vegetal A4',              'GNC','A',   2.5, 300,10),
    ('VV_B1',      'Variedad vegetal B1',              'GNC','B',   5.0, 300,10),
    ('VV_B2',      'Variedad vegetal B2',              'GNC','B',   4.0, 300,10),
    ('VV_B3',      'Variedad vegetal B3',              'GNC','B',   2.5, 300,10),
    ('VV_B4',      'Variedad vegetal B4',              'GNC','B',   1.0, 300,10),
    # GNC — Variedades animales
    ('VA_A',       'Nueva raza animal',                'GNC','TOP',10,   300,10),
    ('VA_B',       'Población mejorada razas pecuarias','GNC','A',  5.0, 300,10),
    # GNC — Investigación-Creación
    ('AAD_A1',     'Invest-Creación AAD A1',           'GNC','TOP',10,   100,10),
    ('AAD_A',      'Invest-Creación AAD A',            'GNC','TOP', 8,   100,10),
    ('AAD_B',      'Invest-Creación AAD B',            'GNC','A',   6,   100,10),
    ('AAD_C',      'Invest-Creación AAD C',            'GNC','B',   4,   100,10),
    # DTI
    ('DI_A',       'Diseño industrial registrado',     'DTI','A',  10,    35,5),
    ('DI_B',       'Diseño industrial en trámite',     'DTI','B',   5,    35,5),
    ('ECI',        'Esquema circuito integrado',       'DTI','A',   4,    35,5),
    ('SF',         'Software registrado',              'DTI','B',   8,    35,5),
    ('PP',         'Planta piloto',                    'DTI','A',   4,    35,5),
    ('PI',         'Prototipo industrial',             'DTI','A',   4,    35,5),
    ('SD',         'Signo distintivo',                 'DTI','A',   4,    35,5),
    ('PN',         'Producto nutracéutico',            'DTI','B',   6,    35,5),
    ('CC',         'Colección científica',             'DTI','B',  10,    35,5),
    ('NRC_A',      'Nuevo registro científico A',      'DTI','B',   8,    35,5),
    ('NRC_B',      'Nuevo registro científico B',      'DTI','B',   5,    35,5),
    ('SE',         'Secreto empresarial',              'DTI','A',   5,   100,5),
    ('EBT_A',      'Empresa base tecnológica A',       'DTI','A',  10,   100,5),
    ('EBT_B',      'Empresa base tecnológica B',       'DTI','B',   8,   100,5),
    ('ICC_A',      'Empresa creativa y cultural A',    'DTI','A',  10,   100,5),
    ('ICC_B',      'Empresa creativa y cultural B',    'DTI','B',   4,   100,5),
    ('IG_A1',      'Innovación gestión empresarial A1','DTI','A',  10,   100,5),
    ('IG_A2',      'Innovación gestión empresarial A2','DTI','A',   6,   100,5),
    ('IG_B1',      'Innovación gestión empresarial B1','DTI','B',   5,   100,5),
    ('IG_B2',      'Innovación gestión empresarial B2','DTI','B',   3,   100,5),
    ('IPP',        'Innovación procedimientos/serv.',  'DTI','B',   5,   100,5),
    ('RNL_A',      'Regulación/norma/legislación A',   'DTI','TOP',10,   100,5),
    ('RNL_B',      'Regulación/norma/legislación B',   'DTI','A',   8,   100,5),
    ('RNR',        'Normatividad espectro radioeléct.','DTI','A',   8,   100,5),
    ('RNT',        'Norma técnica',                    'DTI','B',   7,   100,5),
    ('RNPC',       'Guía práctica clínica',            'DTI','B',   7,   100,5),
    ('GMCF',       'Guía manejo clínico forense',      'DTI','B',   7,   100,5),
    ('MADV',       'Manual atención víctimas',         'DTI','B',   7,   100,5),
    ('PAU',        'Protocolo atención usuarios',      'DTI','B',   7,   100,5),
    ('PVE',        'Protocolo vigilancia epidemiol.',  'DTI','B',   7,   100,5),
    ('AL',         'Acuerdo de Ley',                   'DTI','B',   8,   100,5),
    ('RNPL',       'Proyecto de Ley',                  'DTI','B',   6,   100,5),
    ('CT',         'Concepto técnico',                 'DTI','B',  10,    15,5),
    ('MR',         'Acuerdo licencia I+C',             'DTI','B',  10,    14,5),
    # ASC
    ('FIS',        'Formación e ideación social',      'ASC','ASC',10,   200,5),
    ('GPP_A',      'Gen. participación pública A',     'ASC','ASC',10,   200,5),
    ('GPP_B',      'Gen. participación pública B',     'ASC','ASC', 7,   200,5),
    ('GPP_C',      'Gen. participación pública C',     'ASC','ASC', 5,   200,5),
    ('FCP_A',      'Form. cadenas productivas A',      'ASC','ASC',10,   200,5),
    ('FCP_B',      'Form. cadenas productivas B',      'ASC','ASC', 5,   200,5),
    ('FCP_C',      'Form. cadenas productivas C',      'ASC','ASC', 3,   200,5),
    ('TCCG_A',     'Transfer. conocim. científico A',  'ASC','ASC',10,   200,5),
    ('TCCG_B',     'Transfer. conocim. científico B',  'ASC','ASC', 7,   200,5),
    ('TCCG_C',     'Transfer. conocim. científico C',  'ASC','ASC', 4,   200,5),
    ('TCCG_D',     'Transfer. conocim. científico D',  'ASC','ASC', 1,   200,5),
    # DPC — Eventos y redes
    ('EC_A',       'Evento científico tipo A',         'DPC','DPC',10,   100,5),
    ('EC_B',       'Evento científico tipo B',         'DPC','DPC', 6,   100,5),
    ('RC_A',       'Red de conocimiento A',            'DPC','DPC',10,   100,5),
    ('RC_B',       'Red de conocimiento B',            'DPC','DPC', 6,   100,5),
    ('TC_A',       'Taller de creación A',             'DPC','DPC',10,   100,5),
    ('TC_B',       'Taller de creación B',             'DPC','DPC', 8,   100,5),
    ('TC_C',       'Taller de creación C',             'DPC','DPC', 6,   100,5),
    ('ECA_A',      'Evento artístico/arq./diseño A',   'DPC','DPC', 8,   100,5),
    ('ECA_B',      'Evento artístico/arq./diseño B',   'DPC','DPC', 6,   100,5),
    # DPC — Documentos
    ('WP',         'Working paper',                    'DPC','DPC',10,   100,5),
    ('NSG',        'Nueva secuencia genética',         'DPC','DPC',10,   100,5),
    ('ERL',        'Edición revista/libro divulgación','DPC','DPC', 6,   100,5),
    ('IFI',        'Informe final de investigación',   'DPC','DPC', 2,   100,5),
    ('INF',        'Informe técnico',                  'DPC','DPC', 5,   100,5),
    ('CON_CT',     'Consultoría científico-tecnológ.', 'DPC','DPC', 7.5, 100,5),
    ('CON_AAD',    'Consultoría arte/arq./diseño',     'DPC','DPC', 7.5, 100,5),
    # DPC — Publicaciones editoriales
    ('PEE_A1',     'Publicación editorial nac. A1',    'DPC','DPC',10,   100,5),
    ('PEE_A2',     'Publicación editorial nac. A2',    'DPC','DPC', 8,   100,5),
    ('PEE_B1',     'Publicación editorial reg. B1',    'DPC','DPC', 7,   100,5),
    ('PEE_B2',     'Publicación editorial reg. B2',    'DPC','DPC', 5,   100,5),
    ('PEE_C1',     'Publicación editorial loc. C1',    'DPC','DPC', 5,   100,5),
    ('PEE_C2',     'Publicación editorial loc. C2',    'DPC','DPC', 3,   100,5),
    # DPC — Contenido digital
    ('PCD_A1',     'Producción contenido digital A1',  'DPC','DPC',10,   100,5),
    ('PCD_A2',     'Producción contenido digital A2',  'DPC','DPC', 8,   100,5),
    ('PCD_B1',     'Producción contenido digital B1',  'DPC','DPC', 7,   100,5),
    ('PCD_B2',     'Producción contenido digital B2',  'DPC','DPC', 5,   100,5),
    ('PCD_C1',     'Producción contenido digital C1',  'DPC','DPC', 5,   100,5),
    ('PCD_C2',     'Producción contenido digital C2',  'DPC','DPC', 3,   100,5),
    # DPC — Transmedia
    ('TRM_A1',     'Producción transmedia A1',         'DPC','DPC',10,   100,5),
    ('TRM_A2',     'Producción transmedia A2',         'DPC','DPC', 8,   100,5),
    ('TRM_B1',     'Producción transmedia B1',         'DPC','DPC', 7,   100,5),
    ('TRM_B2',     'Producción transmedia B2',         'DPC','DPC', 5,   100,5),
    ('TRM_C1',     'Producción transmedia C1',         'DPC','DPC', 5,   100,5),
    ('TRM_C2',     'Producción transmedia C2',         'DPC','DPC', 3,   100,5),
    # DPC — Desarrollos web
    ('DW_A1',      'Desarrollo web A1',                'DPC','DPC',10,   100,5),
    ('DW_A2',      'Desarrollo web A2',                'DPC','DPC', 8,   100,5),
    ('DW_B1',      'Desarrollo web B1',                'DPC','DPC', 7,   100,5),
    ('DW_B2',      'Desarrollo web B2',                'DPC','DPC', 5,   100,5),
    ('DW_C1',      'Desarrollo web C1',                'DPC','DPC', 5,   100,5),
    ('DW_C2',      'Desarrollo web C2',                'DPC','DPC', 3,   100,5),
    # DPC — Libros y otros
    ('LIB_FOR2',   'Libro de formación Q2',            'DPC','DPC',10,   100,5),
    ('LIB_FOR3',   'Libro de formación Q3',            'DPC','DPC', 8,   100,5),
    ('BOL',        'Boletín divulgativo',               'DPC','DPC', 3,   100,5),
    ('LIB_DIV',    'Libro de divulgación',              'DPC','DPC',10,   100,5),
    ('GC',         'Generación de contenido',           'DPC','DPC', 4,   100,5),
    ('MAN_GUI',    'Manual/guía especializada',         'DPC','DPC', 2,   100,5),
    # FRH — Tipo A (peso ×1.0)
    ('TD_A',       'Tesis doctoral dirigida',           'FRH','FRHA',10,  160,5),
    ('TD_B',       'Tesis doctoral co-dirigida',        'FRH','FRHA', 5,  160,5),
    ('AP_A',       'Asesoría posdoctoral A',            'FRH','FRHA',10,  100,5),
    ('AP_C',       'Asesoría posdoctoral C',            'FRH','FRHA', 5,  100,5),
    # FRH — Tipo B (peso ×0.2)
    ('TM_A',       'Tesis de maestría Meritorio',       'FRH','FRHB',10,   70,5),
    ('TM_B',       'Tesis de maestría',                 'FRH','FRHB', 5,   70,5),
    ('TP_A',       'Trabajo de pregrado Meritorio',     'FRH','FRHB',10,   20,5),
    ('TP_B',       'Trabajo de pregrado',               'FRH','FRHB', 5,   20,5),
    ('PID_A',      'Proyecto I+D con formación A',      'FRH','FRHB',10,   50,5),
    ('PID_B',      'Proyecto I+D con formación B',      'FRH','FRHB', 6,   50,5),
    ('PID_C',      'Proyecto I+D con formación C',      'FRH','FRHB', 2,   50,5),
    ('PIC_A',      'Proyecto I+Creación formación A',   'FRH','FRHB',10,   50,5),
    ('PIC_B',      'Proyecto I+Creación formación B',   'FRH','FRHB', 6,   50,5),
    ('PIC_C',      'Proyecto I+Creación formación C',   'FRH','FRHB', 2,   50,5),
    ('PF_A',       'Proyecto IDI con formación A',      'FRH','FRHB',10,   50,5),
    ('PF_B',       'Proyecto IDI con formación B',      'FRH','FRHB', 8,   50,5),
    ('PE',         'Proyecto extensión resp. social',   'FRH','FRHB',10,  100,5),
    ('AP_B',       'Creacion programas de Maestría',    'FRH','FRHB', 8,  100,5),
    ('AP_D',       'Creación de cursos de Maestría',    'FRH','FRHB',10,   30,5),
    ('APO',        'Asesoría programa Ondas',           'FRH','FRHB',10,   30,5),
],
columns=['codigo','nombre','clase','calidad','peso_relativo',
         'peso_alta_calidad','ventana_obs'])

PRODUCTOS['peso_global'] = (PRODUCTOS['peso_alta_calidad'] *
                             PRODUCTOS['peso_relativo'])


def calcular_lambda(n_productos, edad_grupo, ventana_obs):
    periodo = min(edad_grupo, ventana_obs)
    if periodo <= 0:
        return 0.0
    return np.log((n_productos / periodo) + 1)


def calcular_contribucion(codigo, n_productos, edad_grupo):
    prod = PRODUCTOS[PRODUCTOS['codigo'] == codigo]
    if prod.empty:
        raise ValueError(f"Producto '{codigo}' no encontrado.")
    prod = prod.iloc[0]
    lam = calcular_lambda(n_productos, edad_grupo, prod['ventana_obs'])
    contrib = lam * prod['peso_global']
    return {
        'codigo': codigo, 'nombre': prod['nombre'],
        'clase': prod['clase'], 'calidad': prod['calidad'],
        'peso_calidad': CALIDAD_PESO[prod['calidad']],
        'peso_relativo': prod['peso_relativo'],
        'peso_alta_calidad': prod['peso_alta_calidad'],
        'peso_global': prod['peso_global'],
        'n_productos': n_productos, 'ventana_obs': prod['ventana_obs'],
        'lambda': lam, 'contribucion_ind_grupo': contrib,
    }


def calcular_indicador_grupo(portafolio, edad_grupo):
    resultados = [calcular_contribucion(c, n, edad_grupo)
                  for c, n in portafolio.items() if n > 0]
    if not resultados:
        return {'IndGrupo': 0, 'detalle': pd.DataFrame()}
    df = pd.DataFrame(resultados)
    ind_top  = df[df['calidad']=='TOP']['contribucion_ind_grupo'].sum()
    ind_a    = df[df['calidad']=='A']['contribucion_ind_grupo'].sum()
    ind_b    = df[df['calidad']=='B']['contribucion_ind_grupo'].sum()
    ind_asc  = df[df['calidad']=='ASC']['contribucion_ind_grupo'].sum()
    ind_dpc  = df[df['calidad']=='DPC']['contribucion_ind_grupo'].sum()
    ind_frha = df[df['calidad']=='FRHA']['contribucion_ind_grupo'].sum()
    ind_frhb = df[df['calidad']=='FRHB']['contribucion_ind_grupo'].sum()
    ind_grupo = (3.7*ind_top + 2.3*ind_a + 0.4*ind_b +
                 1.5*ind_asc + 0.5*ind_dpc +
                 1.0*ind_frha + 0.2*ind_frhb)
    return {'detalle': df, 'Nc_TOP': ind_top, 'Nc_A': ind_a,
            'Nc_B': ind_b, 'ASC': ind_asc, 'DPC': ind_dpc,
            'FRH_A': ind_frha, 'FRH_B': ind_frhb, 'IndGrupo': ind_grupo}


def delta_marginal(codigo, n_base, edad_grupo, delta=1.0):
    antes   = calcular_contribucion(codigo, n_base,         edad_grupo)
    despues = calcular_contribucion(codigo, n_base + delta, edad_grupo)
    peso_cal = CALIDAD_PESO[antes['calidad']]
    dc = despues['contribucion_ind_grupo'] - antes['contribucion_ind_grupo']
    return {
        'codigo': codigo, 'n_base': n_base,
        'lambda_antes': antes['lambda'], 'lambda_despues': despues['lambda'],
        'delta_lambda': despues['lambda'] - antes['lambda'],
        'delta_ind_grupo': dc * peso_cal,
        'contribucion_acumulada': despues['contribucion_ind_grupo'] * peso_cal,
    }


def mapa_valor(edad_grupo=10, n=1):
    filas = []
    for _, row in PRODUCTOS.iterrows():
        r = calcular_contribucion(row['codigo'], n, edad_grupo)
        filas.append({'codigo': r['codigo'], 'nombre': r['nombre'],
                      'clase': r['clase'], 'calidad': r['calidad'],
                      'delta_ind': r['contribucion_ind_grupo'] * r['peso_calidad']})
    return pd.DataFrame(filas).sort_values('delta_ind', ascending=False)


if __name__ == '__main__':
    total = len(PRODUCTOS)
    print(f"Motor v2.0 — {total} productos cargados")
    por_clase = PRODUCTOS.groupby('clase').size()
    for clase, n in por_clase.items():
        print(f"  {clase}: {n}")
    top5 = mapa_valor().head(5)
    print("\nTop 5 por contribución marginal:")
    print(top5[['codigo','calidad','delta_ind']].to_string(index=False))
    print(f"\n✓ Motor v2.0 verificado — {total}/169 productos activos.")

