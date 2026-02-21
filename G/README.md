# G — Gráficos

Prácticas de la asignatura de Gráficos en la FIB (UPC).

## 🛠️ Tecnologías
- C++ / OpenGL 3.3
- GLSL (shaders de vértice, geometría y fragmento)
- Qt (mediante el framework GLarena)

## 📁 Contenido

### GLarena Viewer
Framework OpenGL basado en plugins utilizado como base para los ejercicios de gráficos.
Soporta carga de shaders, pipeline de renderizado por plugins y controles de cámara interactivos.

### Deferred Shading
Implementación de un pipeline de deferred shading con G-buffer completo:
- Buffer de posición
- Buffer de normales
- Buffer de color + especular

El paso final de iluminación combina todas las texturas del G-buffer para calcular la iluminación de la escena.

### Shaders
Colección de shaders GLSL (`.vert` / `.frag`) desarrollados a lo largo de los ejercicios de la asignatura.
