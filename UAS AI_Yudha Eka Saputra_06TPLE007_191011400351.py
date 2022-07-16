#Mengimpor Library
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#Menentukan variabel kasus
permintaan = np.arange(0,6000,1)
persediaan = np.arangen(0,700,1)
produksi = np.arange(0,9000,1)

#Menentukan range himpunan fuzzy
permintaan_sd = fuzz.trapmf(permintaan,[0,0,1000,5000])
permintaan_by = fuzz.trapmf(permintaan,[1000,5000,6000,6000])

persediaan_sd = fuzz.trapmf(persediaan,[0,0,100,600])
persediaan_by = fuzz.trapmf(persediaan,[100,600,700,700])

produksi_kr = fuzz.trapmf(produksi,[0,0,2000,7000])
produksi_tb = fuzz.trapmf(produksi,[2000,7000,9000,9000])


#Membuat grafik himpunan fuzzy
fig, (ax0, ax1 ax2) = plt.subplots(nrows =3, figsize =(8,9))

ax0.plot(permintaan,permintaan_sd, 'b',linewordth =1.5, label'sedikit')
ax0.plot(permintaan,permintaan_by, 'g',linewordth =1.5, label'banyak')

ax0.set_titile('permintaan')
ax0.legend()

ax1.plot(persediaan, persediaan_sd, 'b',linewidth =1.5, label'sedikit')
ax1.plot(persediaan, persediaan_by, 'g',linewidth =1.5, label'banyak')

ax1.set_title('persediaan')
ax1.legend()

ax2.plot(produksi, produksi_kr, 'b',linewidth =1.5, label'berkurang')
ax2.plot(produksi, produksi_tb, 'g',linewidth =1.5, label'bertambah')

ax2.set_title('produksi')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
     ax.spines['right'].set_visible(False)
     ax.get_xaxis()tick.bottom()
     ax.get_yaxis()tick.left()
     
     plt.tight_layout()
     
#Menentukan Input
Minta = 4000
Sedia = 300

#Menentukan Rule Base Kasus
"""
1. R1, Jika Permintaan Banyak AND Persediaan Banyak Maka Produksi Bertambah
2. R2, Jika Permintaan Sedikit AND Persediaan Sedikit Maka Produksi Berkurang
3. R3, Jika Permintaan sedikit AND Persediaan Banyak Maka Produksi Berkurang
4. R4, R1, Jika Permintaan Banyak AND Persediaan Sedikit Maka Produksi Bertambah
5. R5, Jika Permintaan Banyak AND Persediaan Banyak Maka Produksi Bertambah
6. R6, Jika Permintaan Sedikit AND Persediaan Sedikit Maka Produksi Berkurang
7. R7, Jika Permintaan sedikit AND Persediaan Banyak Maka Produksi Berkurang
8. R8, Jika Permintaan Banyak AND Persediaan Sedikit Maka Produksi Bertambah
9. R9, Jika Permintaan Banyak AND Persediaan Banyak Maka Produksi Bertambah
10. R10, Jika Permintaan Sedikit AND Persediaan Sedikit Maka Produksi Berkurang

Domain Jumlah Produksi
Berkurang ---> (7000 - z) / (7000 - 2000) = fmin; apred[i] = fmin; (7000 - z) = 5000 * apred[i]; z = 7000 - (5000 * apred [i])
Bertambah ===> (z - 2000) / (7000 - 2000) = fmin; apred[i] = fmin; (z - 2000)= 5000 * apred[i]; z = (5000 * apred [i])+ 2000 """;

#Menentukan Derajat Keanggotaan
x = []
x.append(fuzz.interp_membership(permintaan, permintaan_sd, minta)
x.append(fuzz.interp_membership(permintaan, permintaan_by, minta)

y = []
y.append(fuzz.interp_membership(persediaan, persediaan_sd, sedia)
y.append(fuzz.interp_membership(persediaan, persediaan_by, sedia)

print("Derajat Keanggotaan Permintaan")
if x[0] > 0;
    printf ("Sedikit : "+str(x[0]))
if x[1] > 0;
    printf ("Banyak : "+str(x[1]))
    
printf("Derajat Keanggotaan Persediaan")
if y[0] > 0;
    printf ("Sedikit : "+str(y[0]))
if y[1] > 0;
    printf ("Banyak : "+str(y[1]))
    
#Memodelkan Rule Base dan Inferensi Tsukomoto
apred1= np.fmin(x[1], y[1])
printf ("Bertambah, Nilai apred1 = "apred1)
z1 = (apred1 * 5000) + 2000
printf("Nilai z1 =  ",z1)

apred2= np.fmin(x[0], y[0])
printf ("Bertambah, Nilai apred2 = "apred2)
z2 = 7000 - (apred2 * 5000) 
printf("Nilai z2 =  ",z2)

apred3= np.fmin(x[0], y[1])
printf ("Bertambah, Nilai apred3 = "apred3)
z3 = 7000 - (apred3 * 5000) 
printf("Nilai z3 =  ",z3)

apred4= np.fmin(x[1], y[0])
printf ("Bertambah, Nilai apred4 = "apred4)
z4 = (apred4 * 5000) + 2000
printf("Nilai z4 =  ",z4)

apred5= np.fmin(x[1], y[1])
printf ("Bertambah, Nilai apred5 = "apred5)
z5 = (apred5 * 5000) + 2000
printf("Nilai z5 =  ",z5)

apred6= np.fmin(x[0], y[0])
printf ("Bertambah, Nilai apred6 = "apred6)
z6 = 7000 - (apred6 * 5000) 
printf("Nilai z6 =  ",z6)

apred7= np.fmin(x[0], y[1])
printf ("Bertambah, Nilai apred7 = "apred7)
z7 = 7000 - (apred7 * 5000) 
printf("Nilai z7 =  ",z7)

apred8= np.fmin(x[1], y[0])
printf ("Bertambah, Nilai apred8 = "apred8)
z8 = (apred8 * 5000) + 2000
printf("Nilai z8 =  ",z8)

apred9= np.fmin(x[1], y[1])
printf ("Bertambah, Nilai apred9 = "apred9)
z9 = (apred9 * 5000) + 2000
printf("Nilai z9 =  ",z9)

apred10= np.fmin(x[0], y[0])
printf ("Bertambah, Nilai apred10 = "apred10)
z10 = 7000 - (apred2 * 5000) 
printf("Nilai z10 =  ",z10)

#Defuzzifikasi
z = (apred*z1 + apred*z2 + apred*z3 + apred*z4 + apred*z5 + apred*z6 + apred*z7 + apred*z8 + apred*z9 + apred*z10 / apred1 + apred2 + apred3 + apred4 + apred5 + apred6 + apred7 + apred8 + apred9 + apred10)

printf("Jumlah Produksi Perusahaan =  ", z)