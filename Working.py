import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def run(deg):
    transformer = PolynomialFeatures(degree=deg, include_bias=False).fit_transform(x)
    model = LinearRegression().fit(transformer, y)
    r_sq = model.score(transformer, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_,"\n\n\n\n\n")
    return r_sq,model
# constants

#deg =2 coefficient of determination: 0.5197856438141792
# deg = 3 coefficient of determination: 0.5929112767701978
# deg = 4 coefficient of determination: 0.6063151835496412

# data set up
data = pd.read_csv("Resources/archive1/data.csv")

data.drop_duplicates()
data.dropna()

data = data.head(10000)#133485

y = data["popularity"].tolist()
y = np.array(y)

#data = data.drop(["artists", "id", "name", "release_date", "popularity","key","duration_ms","mode"], axis=1)
data = data.drop(["explicit"], axis=1)
x = np.array(data)
deg =2
# transfor data
model1 =0
while True:
    print("deg: ", deg)
    if (model1==0):
        r1, model1 = run(deg)
    r2, model2 = run(deg + 1)
    deg = deg + 1
    if r2 - r1 < .00001:
        model = model2
        r_sq = r2
        break
    r1,model1 = r2,model2
    
print("\n\n\n","-"*40,
      "deg: ", deg)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
# predict response
#y_pred = model.predict(transformer)
"""C:\Users\tirth\PycharmProjects\Spotify\venv\Scripts\python.exe C:\Users\tirth\PycharmProjects\Spotify\model2\workingimproving.py
deg:  2
coefficient of determination: 0.6722238929967068
intercept: -40196.36311035181
slope: [ 3.83034562e+02 -4.72867285e+01 -1.00729310e+03  7.08924383e+02
  7.64838987e+02  7.71557036e+02  3.49811831e+01  1.72570180e+03
 -1.77816658e+00  1.07568952e+03  4.02569951e+01 -2.01571044e+01
 -3.58042429e+00  2.10519615e+00  1.53883751e+00 -1.80766374e+00
 -7.97429243e+00 -3.55057671e-01 -2.36193838e+00  2.33722416e-04
 -3.45830699e+00 -1.90367198e-01  5.79159701e+00 -1.79548401e+00
 -2.27087785e+01  1.02628866e+01 -5.89520009e+00  5.01443879e-01
  2.09718469e+00 -1.19892976e-02 -1.07737776e+01  3.48114419e-02
  3.60150898e+00 -2.19820934e+01  7.63000871e+00  1.62120084e+00
 -3.29856485e-01  2.73738259e+01 -6.67117250e-02  2.08413488e+01
  5.12075857e-01  7.08924386e+02 -1.29603379e+01 -8.34520272e+00
  1.79155341e-01 -6.77384500e+00  3.42469685e-03 -5.79290755e+00
 -7.18553923e-01  9.03837929e+00  3.31570298e+00 -2.44792538e-01
 -7.46234560e+00  2.88059267e-02 -9.07056186e+00 -4.04486547e-01
  5.92199439e+00 -4.87537394e-02  6.14727196e+00 -4.29046900e-02
  1.57851717e+01 -3.99475828e-01  2.20486963e-03 -2.65656522e-01
  1.66134225e-03 -7.75864297e-01 -1.78221142e-02  1.47738316e+00
  3.07374254e-02 -3.43953152e+00 -9.06238660e-01  1.81121192e-04
  3.45200297e-02  9.11278640e-04 -7.84927342e+00 -5.58145067e-01
 -1.00641189e-02] 





coefficient of determination: 0.7901629210808997
intercept: 5093795.679158495
slope: [ 3.37207023e+04  1.61956456e+04 -4.13518123e+04 -2.63140738e+04
  1.64702568e+04  2.60073883e+04  2.55249975e+02  1.01823098e+04
 -1.39194327e+01 -3.55340205e+04 -7.81199118e+03 -1.21225052e+02
  5.36480782e+02  2.68303853e+02  4.10972891e+02  4.43238436e+02
 -3.10218254e+02  1.75612827e+01 -1.38446171e+03  1.39348817e+00
  3.94835904e+02 -3.46606397e+01 -5.83138907e+01 -7.14150696e+02
 -1.33576188e+02 -6.24621257e+02 -1.81923357e+03  5.92554304e+01
  6.92989806e+02 -8.50790046e+00  1.32847628e+03 -1.55857553e+01
  1.04884401e+03  2.24705311e+03  1.56796427e+03  1.62026724e+03
 -6.00205368e+01 -1.70073225e+03 -5.53821034e+00 -4.64065238e+02
  4.15429907e+01 -2.62939605e+04  2.15694952e+03 -5.84738100e+01
 -5.22995255e+00  2.16217016e+02 -2.04379056e-01  4.63009246e+02
  4.02463276e+01 -9.68687199e+02 -3.49665003e+02 -1.34818695e+01
 -5.40334520e+02 -1.06603084e+00  4.22641409e+02 -1.66854876e+01
 -2.33122272e+02 -2.28160277e+01  3.12678385e+02 -6.12349055e+00
 -1.15534588e+03 -2.55775728e+01 -1.35477989e+00  7.56533290e+01
  4.30435338e-02  3.92658812e+01 -3.03900869e-01  1.63418793e+03
  5.35852830e+00  1.09952642e+03 -1.05428471e+01  6.89682452e-03
  8.82479237e+00  1.41656431e-02 -6.83712453e+02  3.63267846e+01
  3.99246587e+00 -1.48629217e+01  1.01012025e+00  5.82584721e+01
  1.20578183e+01 -1.67830794e+01 -1.41594683e+01 -6.12717499e-01
  2.69365358e+01  5.86672692e-02 -3.25562210e+01  5.90072319e-02
 -5.73060933e+00 -5.36334751e+01  5.20957994e+00  9.54489333e+00
  5.24355568e+01  2.69966150e+00  1.12748116e+01 -2.71096459e-01
  5.95437360e+00 -2.32958771e-01  4.88145388e+01  3.55040205e+00
 -2.06303846e+00 -4.90766547e+01 -3.61803305e-01  3.16507281e+01
 -1.06687371e-01  4.09062717e+01 -1.83375842e-01  4.10904273e+02
  4.82884587e+01  7.27108924e+00  1.21741535e+00  3.19718023e+01
 -1.08158796e-02  2.19569830e+01 -4.33986690e-01  2.69396961e+01
  1.41982942e+00 -4.35041231e-01 -3.31468095e+01  1.73381019e-02
 -1.95599434e+01 -2.29033308e-01  3.10522555e+00  1.55623800e+00
 -2.22410462e+01  2.06517364e-01 -1.00759027e+01  1.64738863e-01
  3.63017681e-02 -3.61055317e+00  1.01907212e-02 -2.39432573e+00
 -8.53210748e-03 -4.26685720e+01  1.56019799e-01 -3.66150270e+01
  6.76778714e-01  4.02345519e-04  4.94476251e-03 -6.80972637e-04
  9.95476359e+00 -2.13986822e-01  8.91139801e-03 -8.22645517e+01
  5.16973558e+01  1.59153444e+01 -2.08862598e+01 -3.86405707e+01
 -9.25698362e-01 -1.76585110e+02  8.57594358e-02 -5.01662720e+01
  1.08153227e-01  4.51766877e+00  6.92713229e+01  1.18865525e+01
 -3.09024042e+01  1.09525768e-01 -2.33584767e+01 -9.46704515e-01
  9.65669264e+00  4.08586043e-01 -1.33567401e+02  6.82191288e+01
  6.75112575e+01 -3.27302504e+00  2.10906771e+01 -3.36572487e-01
  6.54836110e+00  8.94311315e-02 -1.02753774e+01  9.35360682e+00
 -1.97181666e-01  1.45707963e+00  6.03948052e-02 -1.70462878e+01
  3.31649023e-01  3.52381859e+01  1.74353503e+00 -4.28750500e+01
 -2.41095947e-02  5.39763457e+01  9.24999921e-01  5.66363424e-02
  4.34038169e+00  2.86986814e-02 -1.50105426e+00 -3.13446709e-02
 -1.90546217e+01  3.52737822e-01 -2.13783042e+01 -1.97401126e-01
 -1.42133377e-04  2.61838691e-01  4.75646553e-03  4.64420345e+01
 -7.17804448e-01  3.68959616e-03  7.27185863e+01  7.75753917e+01
 -2.06516837e+01 -6.87399671e+01 -4.82661618e+00 -6.76250637e+01
 -1.10580956e-01  1.99285348e+01 -6.15320738e-01  2.24705143e+03
  1.09052682e+02  4.54409873e+01 -2.78049637e+00  3.32269257e+01
  5.91505717e-02 -1.75469932e+01 -2.42779253e+00  1.72691870e+00
 -5.89265134e+00  9.46185076e-01 -3.86605854e+01  9.54214373e-02
 -2.85711677e+01 -7.85773184e-01  4.80427661e+00  2.07561420e+00
 -1.16935567e+02  7.25213354e-02  7.68086534e+00 -7.64364689e-01
  1.84955403e-01  1.55733159e+00  2.32789908e-02 -5.90256655e+00
  3.53503958e-02 -6.02692080e+01  1.22702416e-01 -8.34183206e+01
  9.93384210e-01 -1.63589586e-03  1.92188584e-01  3.43223002e-03
 -1.54318022e+01  1.84307614e-01 -1.04171164e-02 -2.62939600e+04
  2.15694970e+03 -5.84734552e+01 -5.22951044e+00  2.16216018e+02
 -2.04436626e-01  4.63009835e+02  4.02460763e+01  2.04672811e+01
  5.66099591e-01 -1.90657365e+00  2.05618788e+02  1.36101063e-01
 -1.28149432e+02 -2.31119134e+00  7.59311733e+00 -1.15552894e+00
 -1.00662423e+01  2.10842149e-02 -5.13387705e+00  1.55357073e-02
  1.03774753e-01 -2.26276397e+00 -2.27874974e-03  2.37271474e-01
  9.36734756e-03 -2.35213193e+01 -2.20570404e-02 -3.28466460e+01
 -2.44604050e-01  1.52030922e-04 -5.22572419e-02  2.98208644e-04
  2.39272922e+01 -4.77839951e-01 -2.04857889e-02  3.89968386e-01
 -5.77733571e+00  7.92085141e-01  6.13308223e+01 -4.20247211e-02
 -3.57407356e+00  4.99523486e-01  8.31114331e+00 -1.08622812e+00
 -1.43561012e+01  2.61235592e-02 -5.68669385e-01  1.71552433e-01
  7.21578962e-03  1.75565703e+00  1.18556687e-04 -3.56606696e-01
  6.81339234e-03  3.39450890e+01 -1.66071860e-01  6.84299951e+00
  2.89870912e-01 -9.19066740e-05 -3.97112915e-02  5.52219902e-04
  1.70968337e+01 -2.10437181e-01  4.21904711e-03  7.21745445e-01
  1.36723063e-01 -3.89585014e+00  5.58132138e-03  1.56733734e+00
  1.07822325e-01 -5.86522157e-02  8.97797269e-01  9.56297184e-03
 -1.01174781e-01  9.07941813e-03 -2.33354157e+01  2.20408308e-01
 -3.63034787e+00 -1.07001024e-01  3.81729529e-04 -6.45772075e-02
  3.09275564e-03  4.43954059e+00  5.81752378e-01  6.26558178e-03
 -2.91171429e-03  3.75992626e-02 -5.57955523e-04  6.11671574e-02
  5.77912419e-04  2.78115766e+00 -3.18656453e-03  9.65676102e-02
 -4.04705439e-02  5.09067648e-05 -9.97365426e-04 -5.24579464e-05
  5.19409439e-01 -1.72862855e-02  8.81065062e-05 -5.17893745e+01
 -1.31245090e-01 -2.85880608e+01 -7.34302410e-01  7.31208540e-04
 -1.46296310e-01 -2.99439155e-03  2.10520333e+01 -5.24641761e-01
  2.66245934e-03 -6.25339908e-07  1.46458961e-03 -3.30963303e-06
 -1.53501660e-01 -4.71098618e-03 -3.80507663e-06  1.74391272e+01
  3.28957632e-01 -9.24922651e-03 -6.79946017e-04] 





deg:  3
coefficient of determination: 0.795121612473348
intercept: 1276316.2902704934
slope: [-1.97134451e+02  1.23714070e-01  7.21307351e-01 ...  1.07407720e-03
 -1.92959675e-06 -2.48981658e-07] 





deg:  4
coefficient of determination: 0.8044678421280056
intercept: 516118.9449405503
slope: [ 2.15038707e-02  1.57330371e-05 -1.34764017e-05 ... -4.77667204e-07
  1.66861408e-10 -1.03437246e-10] 





deg:  5
coefficient of determination: 0.8155448390331509
intercept: 253129.85161916498
slope: [ 7.28125881e-05 -1.09508066e-06 -3.86898563e-06 ... -8.43190972e-12
 -1.57738375e-12 -4.36213836e-14] 





deg:  6
Traceback (most recent call last):
  File "C:\Users\tirth\PycharmProjects\Spotify\model2\workingimproving.py", line 41, in <module>
    r2, model2 = run(deg + 1)
  File "C:\Users\tirth\PycharmProjects\Spotify\model2\workingimproving.py", line 8, in run
    model = LinearRegression().fit(transformer, y)
  File "C:\Users\tirth\PycharmProjects\Spotify\venv\lib\site-packages\sklearn\linear_model\_base.py", line 569, in fit
    linalg.lstsq(X, y)
  File "C:\Users\tirth\PycharmProjects\Spotify\venv\lib\site-packages\scipy\linalg\basic.py", line 1199, in lstsq
    x, s, rank, info = lapack_func(a1, b1, lwork,
numpy.core._exceptions.MemoryError: Unable to allocate 2.37 GiB for an array with shape (10000, 31823) and data type float64

Process finished with exit code 1
"""
