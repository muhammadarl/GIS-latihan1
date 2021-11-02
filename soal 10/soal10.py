import shapefile
w=shapefile.Writer('./soal10',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")


w.record("ngek","satu")
w.record("crit","dua")




w.poly([[[24,24],[27,24], [27,21],[24,21]]])
w.poly([[[20,23],[23,23], [23,20],[20,20]]])