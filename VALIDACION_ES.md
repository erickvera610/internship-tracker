# Evidencia de validación automatizada

Se ejecutaron diez escenarios diferentes con datos ficticios o sintéticos. Este informe describe ejecuciones reales del código mediante un script automatizado. No representa tráfico de usuarios, experiencia laboral ni contribuciones realizadas manualmente por Erik.

Resultado: **10 de 10 escenarios aprobados**.

Consulta `validation-results.json` para ver cada entrada, resultado y fecha UTC de ejecución.

## Repetir las ejecuciones

Desde la carpeta del repositorio ejecuta:

```bash
python validate_scenarios.py
```

En Mercado Aprende instala primero las dependencias del README. En los otros cinco proyectos basta Python. El script utiliza almacenamiento temporal: no cambia registros personales ni realiza compras reales. Regenera el informe local; para conservar nuevos resultados en GitHub debes revisarlos y hacer un commit.

## Qué se comprobó

| Escenario | Entrada | Resultado |
|---|---|---|
| 1 | {"company": "Fictional Company 1", "role": "Software Intern", "status": "Saved", "deadline": "2027-03-01"} | Aprobado |
| 2 | {"company": "Fictional Company 2", "role": "ML Intern", "status": "Applied", "deadline": "2027-03-02"} | Aprobado |
| 3 | {"company": "Fictional Company 3", "role": "Data Intern", "status": "Interview", "deadline": "2027-03-03"} | Aprobado |
| 4 | {"company": "Fictional Company 4", "role": "Software Intern", "status": "Offer", "deadline": "2027-03-04"} | Aprobado |
| 5 | {"company": "Fictional Company 5", "role": "ML Intern", "status": "Closed", "deadline": "2027-03-05"} | Aprobado |
| 6 | {"company": "Fictional Company 6", "role": "Data Intern", "status": "Saved", "deadline": "2027-03-06"} | Aprobado |
| 7 | {"company": "Fictional Company 7", "role": "Software Intern", "status": "Applied", "deadline": "2027-03-07"} | Aprobado |
| 8 | {"company": "Fictional Company 8", "role": "ML Intern", "status": "Interview", "deadline": "2027-03-08"} | Aprobado |
| 9 | {"company": "Fictional Company 9", "role": "Data Intern", "status": "Offer", "deadline": "2027-03-09"} | Aprobado |
| 10 | {"company": "Fictional Company 10", "role": "Software Intern", "status": "Closed", "deadline": "2027-03-10"} | Aprobado |
