class Variaveis:
    def __init___(self):
        self.tec_funcao = lambda:  1
        self.tes_funcao = lambda:  1
    
    def set_tec(self, f):
        """
            params: 
                f: (func) função de aridade 0 de retorno inteiro
        """
        self.tec_funcao = f
        
    def get_tec(self):
        return self.tec_funcao()
    
    def set_tes(self, f):
        """
            params:
                f: (func) função de aridade 0 de retorno inteiro
        """
        self.tes_funcao = f
        
    def get_tes(self):
        return  self.tes_funcao()