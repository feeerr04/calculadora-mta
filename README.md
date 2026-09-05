# Calculadora Básica - Mini Proyecto Ágil

## Prácticas de calidad aplicadas

1. **Coding Standards (Black):** Se utilizó el formateador automático Black para asegurar que el código siguiera un estilo consistente según el estándar PEP 8, sin depender de que cada desarrollador aplique el formato manualmente.

2. **Pull Request + Code Review:** Se creó una rama separada (`feature/calculadora-basica`) para aislar el desarrollo de la funcionalidad, y se abrió un Pull Request hacia `main`. Se realizó una auto-revisión dejando un comentario explicando la decisión de diseño de lanzar un `ValueError` en la función de división, en lugar de manejarlo de otra forma.

## Qué problema evita cada práctica

- **Coding Standards:** Evita errores de estilo inconsistente entre desarrolladores (por ejemplo, mezclar comillas simples y dobles, o indentaciones distintas), lo cual dificulta la lectura y el mantenimiento del código a largo plazo.
- **Pull Request + Code Review:** Evita que el código llegue directo a la rama principal sin ser revisado, reduciendo el riesgo de introducir errores no detectados y fomentando que exista al menos un punto de control antes de integrar cambios.

## Relación con lo visto en clase

Estas prácticas atacan directamente los antipatrones vistos en la clase de la semana. El uso de una rama separada y un Pull Request evita el antipatrón de **Integración Big Bang**, donde el desarrollo aislado por mucho tiempo termina en conflictos masivos al integrar, aquí el cambio se integró de forma controlada y en un ciclo corto. De igual forma, el Code Review evita el problema de **"cero filtros de calidad"** visto en el caso de DataSync, donde el código se subía directamente a `main` sin revisión, generando fallas en producción. Aplicar estas prácticas, incluso en un proyecto pequeño, ayuda a construir el hábito de trabajar con calidad integrada desde el principio, en lugar de dejarlo como una idea abstracta que solo se aplica en equipos grandes.