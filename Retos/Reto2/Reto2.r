library(pracma)
library(readxl)

arch1 = read_excel("C:/Users/David/Downloads/DatosReto2.xls", sheet = "Itatira")
arch2 = read_excel("C:/Users/David/Downloads/DatosReto2.xls", sheet = "Santa Quitéria")

x = seq(from = 1, to = 720, by = 1)
y = arch1$`Temp. Interna (ºC)`

dias = arch1$`Dia Juliano`
horas = arch1$Hora
indicesIdeales = x

#35% de los datos
ones = rep(1, 720)
reduccion = sample.int(720,720*0.35)
for (e in reduccion) {
  ones[e] = 0
}

x2 = c()
y2 = c()
i = 1
j = 1

for (o in ones)
{
  if(o == 1)
  {
    x2[i] = x[j]
    y2[i] = y[j]
    i = i + 1
  }
  j = j +1
}

#Graficas
plot(x,y,type='l', ylab = "Temperatura interna", xlab = "Indice Ideal", col= "red")

lines(spline(x2,y2,n=200),col= "blue")

interpolacion = splinefun(x2,y2)

interpolados = c()
k = 1

error = c()

for(var in x)
{
  errorY = interpolacion(var)
  error = c(error, abs((y[k] - errorY)/y[k]))
  k = k + 1
}

print(error)
interpolados2 = c()

for (i in 1:length(arch2$`Dia Juliano`)) 
{
  dia = arch2$`Dia Juliano`[i]
  hora = arch2$Hora[i]
  
  for(j in 1:720)
  {
    if((dias[j] == dia) && (horas[j] == hora))
    {
      interpolados2 = c(interpolados2,indicesIdeales[j])
    }
  }
}

nuevosY = c()
errorEstacion = c()
z = 1

for (variable in interpolados2) 
{
  nuevosY = c(nuevosY, interpolacion(variable))
  errorEstacion = c(errorEstacion, abs((arch2$`Temp. Interna (ºC)`[z] - nuevosY[z])/arch2$`Temp. Interna (ºC)`[z]))
  z = z + 1
}

plot(interpolados2,arch2$`Temp. Interna (ºC)`, ylab = "Temperatura interna", xlab = "Indice Calculado", type = 'l', col= "blue")
lines(interpolados2, nuevosY, col= "red")
print(errorEstacion)

maximo = 0
media = 0

for (error in errorEstacion) {
  if(error > maximo)
    maximo = error
  media = media + error
}