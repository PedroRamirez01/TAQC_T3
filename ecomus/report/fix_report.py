#!/usr/bin/env python3
"""
Script para modificar el reporte HTML generado por pytest-html
para asegurar que los estilos CSS funcionen correctamente.
"""
import os
import sys

def fix_report(file_path):
    """
    Añade estilos CSS directamente al archivo HTML para evitar problemas de CSP.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Verificar si el archivo ya tiene el estilo inyectado
        if "/* CSS inyectado por fix_report.py */" in content:
            print("El reporte ya tiene estilos inyectados.")
            return
        
        # Estilos CSS básicos para mejorar la apariencia del reporte
        css_styles = """
        <style>
        /* CSS inyectado por fix_report.py */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #333;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .passed {
            color: green;
        }
        .failed {
            color: red;
        }
        .skipped {
            color: orange;
        }
        .error {
            color: darkred;
        }
        button {
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #e0e0e0;
        }
        .collapsible {
            cursor: pointer;
        }
        </style>
        """
        
        # Insertar CSS antes del cierre de la etiqueta head
        if "</head>" in content:
            modified_content = content.replace("</head>", f"{css_styles}</head>")
        else:
            # Si no hay etiqueta head, la añadimos al principio
            modified_content = f"<html><head>{css_styles}</head>{content}"
        
        # Guardar el archivo modificado
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"Se ha modificado el reporte en {file_path} correctamente.")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return False
    
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        report_path = sys.argv[1]
    else:
        report_path = os.path.join(os.path.dirname(__file__), "report.html")
    
    fix_report(report_path)
