from Conexion import config
conn = config()
cursor = conn.getConnection()

class Estudiante:
    def __init__ (self) -> None:
        self.idAlumno = None
        self.dniAlumno = None
        self.cuilAlumno = None
        self.nombreAlumno = None
        self.apellidoAlumno = None
        self.fechaNacAlumno = None
        self.direccionAlumno = None  #modificable
        self.observacionesAlumno = None  
        self.telefono = None           #modificable
        self.secundariaAlumno = None   
        self.anioEgSecAlumno = None
        self.anioIngAlumISPP = None
        self.anioEgAlumISPP = None
        self.emailAlumno = None        #modificable

    def modificarEmail(self, email) :
        try :
            sql = 'UPDATE Alumno SET emailAlumno = %s WHERE dniAlumno = %s'
            values = (email, self.dniAlumno)
            cursor.execute(sql, values)
            conn.connection.commit()
            return print(cursor.rowcount, "Datos Guardados")
        
        except Exception as e:
            print(e) 
    
    def modificarTelefono(self, telefono) :
        try :
            sql = 'UPDATE Alumno SET telefono = %s WHERE dniAlumno = %s'
            values = (telefono, self.dniAlumno)
            cursor.execute(sql, values)
            conn.connection.commit()
            return print(cursor.rowcount, "Datos Guardados")
        
        except Exception as e:
            print(e) 
    
    def modificarDireccion(self, direccion) :
        try :
            sql = 'UPDATE Alumno SET direccionAlumno = %s WHERE dniAlumno = %s'
            values = (direccion, self.dniAlumno)
            cursor.execute(sql, values)
            conn.connection.commit()
            return print(cursor.rowcount, "Datos Guardados")
        
        except Exception as e:
            print(e) 