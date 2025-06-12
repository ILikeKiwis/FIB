#version 330 core

in vec3 vertex;
in vec3 color;
out vec4 f_color;

void main()  {
    gl_Position = vec4 (vertex, 1.0);
    f_color = vec4(color, 1);
}
