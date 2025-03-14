#version 330 core

in vec4 frontColor;
out vec4 fragColor;

uniform float smoothness = 25.0;

float epsilon = 1.0/128;

in vec2 vtexCoord;

uniform sampler2D heightMap;

uniform mat3 normalMatrix;

void main()
{
    vec2 epsx = vec2(vtexCoord.s + epsilon, vtexCoord.t);
    vec2 epsy = vec2(vtexCoord.s, vtexCoord.t + epsilon);
    float tex_ex = texture(heightMap, epsx).x;
    float tex_ey = texture(heightMap, epsy).y;
    vec4 tex = texture(heightMap, vtexCoord);
    float G_x = (tex_ex - tex.x)/epsilon;
    float G_y = (tex_ey - tex.y)/epsilon;
    vec2 G = vec2(G_x, G_y);
    vec3 N = normalize(vec3(-G.x, -G.y, smoothness));
    N = normalMatrix * N;
    fragColor = vec4(N.z);
}
