from OpenGL.GL import *

# métodos estáticos para carregar e compilar shaders OpenGL e vincular para criar programas
class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):

        # especifica a versão necessária do OpenGL/GLSL
        shaderCode = '#version 330\n' + shaderCode

        # cria um objeto de shader vazio e retorna o valor de referência
        shaderRef = glCreateShader(shaderType)

        # armazena o código-fonte no shader
        glShaderSource(shaderRef, shaderCode)

        # compila o código-fonte previamente armazenado no objeto shader
        glCompileShader(shaderRef)

        # verifica se a compilação do shader foi bem-sucedida
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)

        if not compileSuccess:
            # recupera a mensagem de erro
            errorMessage = glGetShaderInfoLog(shaderRef)

            # libera a memória usada para armazenar o programa do shader
            glDeleteShader(shaderRef)

            # converte string de bytes em string de caracteres
            errorMessage = '\n' + errorMessage.decode('utf-8')

            # lança uma exceção: interrompe o programa e imprime a mensagem de erro
            raise Exception(errorMessage)

        # a compilação foi bem-sucedida; retorna o valor de referência do shader    
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        
        vertexShaderRef = OpenGLUtils.initializeShader(
                    vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(
                    fragmentShaderCode, GL_FRAGMENT_SHADER)
        
        # cria um objeto de programa vazio e armazena a referência a ele
        programRef = glCreateProgram()

        # anexa os programas de shader previamente compilados
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)
        
        # vincula o vertex shader ao fragment shader
        glLinkProgram(programRef)

        # verifica se o link do programa foi bem-sucedido
        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)

        if not linkSuccess:
            # recupera a mensagem de erro
            errorMessage = glGetProgramInfoLog(programRef)
            
            # libera a memória usada para armazenar o programa
            glDeleteShader(programRef)
            
            # converte string de bytes em string de caracteres
            errorMessage = '\n' + errorMessage.decode('utf-8')
            
            # lança uma exceção: interrompe a aplicação e imprime a mensagem de erro
            raise Exception(errorMessage)
        
        # o link foi bem-sucedido; retorna o valor de referência do programa
        return programRef
    
    @staticmethod
    def printSystemInfo():
        print("  Vendor: " + glGetString(GL_VENDOR).decode('utf-8') )
        print("Renderer: " + glGetString(GL_RENDERER).decode('utf-8') )
        print("Versão do OpenGL suportada: " + glGetString(GL_VERSION).decode('utf-8') )
        print("Versão do GLSL suportada: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8') )
