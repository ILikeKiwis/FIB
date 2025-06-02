#version 330 core

in vec4 gfrontColor;
out vec4 fragColor;

in vec2 st;

void main()
{
    fragColor = gfrontColor;
    if (st.x >= 2 && st.x <= 3 && st.y >= 1 && st.y <= 6) fragColor = vec4(0);
    if (st.x >= 2 && st.x <= 4 && st.y >= 3 && st.y <= 4) fragColor = vec4(0);
    if (st.x >= 2 && st.x <= 5 && st.y >= 5 && st.y <= 6) fragColor = vec4(0);
}
