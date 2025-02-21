#version 330 core

#define ROJO vec4(1, 0, 0, 1)
#define AZUL vec4(0, 0, 1, 1)
#define VERDE   vec4(0, 1, 0, 1) 
#define AMARILLO    vec4(1, 1, 0, 1)

out vec4 FragColor;

void main() {
    if (int(gl_FragCoord.y) % 28 <= 13) discard;
    FragColor = ROJO;
    if (gl_FragCoord.x > 356){
        if (gl_FragCoord.y > 354) {
            FragColor = AZUL;
        }
        else FragColor = VERDE;
    }
    else if (gl_FragCoord.y > 354){
        FragColor = ROJO;
    }
    else FragColor = AMARILLO;
}

