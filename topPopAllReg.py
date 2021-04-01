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
data = pd.read_csv("Resources/archive1/data2.csv")

data.drop_duplicates()
data.dropna()

data = data.head(10000)#133485

y = data["popularity"].tolist()
y = np.array(y)

data = data.drop(["artists", "id", "name", "release_date", "popularity","key","duration_ms","mode"], axis=1)

x = np.array(data)
deg =2
# transfor data
model1 =0
while True:
    print("deg: ", deg)
    if (model1==0):
        r1, model1 = run(deg)
    r2, model2 = run(deg + 1)
    if r2 - r1 < .00001:
        model = model2
        r_sq = r2
        break
    r1,model1 = r2,model2
    deg = deg + 1
print("\n\n\n","-"*40,
      "deg: ", deg)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
# predict response
#y_pred = model.predict(transformer)
"""
C:\Users\tirth\PycharmProjects\Spotify\venv\Scripts\python.exe C:\Users\tirth\PycharmProjects\Spotify\model2\workingimproving.py
deg:  2
coefficient of determination: 0.1449115524431408
intercept: 20949.163176372393
slope: [-1.53083768e+02 -2.27245752e+02  2.89322939e+02 -4.94689420e+01
 -8.84195482e+01 -6.48057612e+01 -1.14888639e+01 -1.20746627e+02
 -1.59869115e-01  1.44514417e+01 -2.10156873e+01  4.16036972e-01
  1.02479750e+00 -5.57849371e-01 -9.96010092e-02  7.65256406e-01
  1.78970913e+00 -2.51868664e-02 -8.09624488e-01 -1.48227798e-04
 -1.47287587e+00  7.59979719e-02 -1.06036795e+00 -6.21409930e+00
 -2.44329452e+00  8.18203822e-01 -2.33994337e+00  5.00693976e-01
  1.06328516e+00  3.88248656e-03  6.16600076e+00  1.17831206e-01
 -1.02049674e+01  1.72763490e+00  5.03751437e+00  3.73737733e+00
  4.28178395e-01  2.64325175e+00 -1.52945311e-02  7.15163655e+00
 -1.35904498e-01 -4.94689414e+01 -1.09380239e+00  2.33201923e+00
 -2.10972707e-01 -6.44157637e+00  5.01997425e-03  1.69391910e+00
  4.80827403e-02  3.88222268e-01 -2.69905519e+00 -1.95534599e-01
  1.78294794e+00  1.60634203e-02  6.23443161e-01  3.90598520e-02
 -1.10330823e-01 -2.45843221e-01 -7.53240719e+00  2.32536606e-02
  1.07714554e+00  2.87233694e-02 -6.32464013e-03  1.72538198e-01
  5.71890049e-04 -3.20730752e-01  5.53303328e-03 -1.16864671e+00
  5.88909475e-03 -7.52625086e-01  6.08061068e-02  1.37064781e-04
  5.77437105e-04  6.35295322e-05 -2.50701826e+00 -1.18421504e-02
  5.28637479e-03] 





coefficient of determination: 0.20848758400517287
intercept: -1730610.267974654
slope: [ 1.99965593e+04  3.63649138e+04 -2.11366690e+04  2.22463090e+04
  4.51394864e+03  9.91709114e+02  2.00642216e+03  2.84267478e+04
  2.44045977e+01 -1.90049802e+04  2.61876758e+03 -1.56150083e+02
 -4.96680757e+02 -5.99738948e+02  1.37335880e+02 -2.48024478e+01
  1.28745617e+02  1.36928843e+01  6.02995594e+02 -6.50545934e-01
  3.67115884e+02 -1.97733139e+01 -1.06900410e+02  2.93035042e+01
  1.08528337e+02  3.83449765e+02 -1.06423929e+03  5.42971059e+00
  8.18696719e+02 -1.95566654e+00 -4.00115490e+02 -3.60704852e+01
  5.34529476e+02 -3.24428615e+02 -8.18824809e+02 -3.91876383e+02
  2.33940555e+00  1.79207999e+03  1.77844212e-01 -2.24763961e+02
  2.10684260e+01  2.22261352e+04 -2.30818287e+02 -9.29142373e+01
  3.74766623e+01  6.12088106e+02 -3.38505383e-01 -2.06736750e+01
 -3.30009868e+01 -6.63391824e+02  4.26615796e+02  9.84317496e+00
  1.47391550e+03  2.95562670e-01 -1.09004897e+02 -4.20882928e+00
  9.04144724e+01  6.02646767e+01 -3.42300896e+00 -2.05209904e+00
  6.86929761e+02 -4.69712318e-01  2.92226576e-01 -1.18249307e+02
  6.92023884e-02 -1.97231452e+01 -2.01646335e+00  1.97028149e+03
  4.86465805e-02 -5.30515898e+02 -3.01471320e+01 -3.28920474e-03
 -2.16404300e+00 -2.21296214e-02  5.62992077e+02  1.88537928e+01
 -1.32089132e+00 -1.84366384e+00 -1.22118567e+01  7.07960810e+00
 -1.52988518e+00  8.94943610e-01 -8.10470735e+00  2.87305400e-01
  1.05855028e+01  5.70830718e-02 -2.61939482e+00  7.97890127e-02
 -2.91471951e+01 -2.34151928e+01 -4.35017737e+00  9.48667299e+00
 -1.96687798e+01  1.17149398e+00  5.88163297e+01  6.37943433e-02
  1.77036848e+01  2.71277993e-01  1.50540526e+01  5.20433261e+00
  1.58444205e+01 -1.42820843e+01  6.22902525e-02 -3.95120565e+01
  1.17172926e-01  2.39175339e+01  2.82686490e-01  1.37263167e+02
 -1.71096091e+00  2.69420124e-01  2.22455128e-01  1.65033536e+00
  3.79993882e-03 -7.59842569e-01 -1.35323095e-01  1.03734339e+01
  9.46558671e+00  2.90931650e-01  1.70514241e+01 -1.03662315e-02
 -8.08014460e+00  4.61698875e-03 -6.03376358e+00  4.86518616e-01
  2.91117243e+01 -8.70508644e-02  7.21964172e+00 -4.46799685e-02
  1.10066698e-02  8.08430917e-01 -3.36784797e-03 -1.31059403e+00
 -6.78424179e-03 -1.21566450e+00 -1.15820654e-01 -1.51573126e+01
 -3.00200308e-01 -1.28117073e-06 -3.24173199e-02  2.60903940e-04
 -6.90849715e+00 -1.93738308e-01  4.88857391e-03 -3.02066829e+01
 -2.75236798e+01 -5.91022836e+00  2.53663971e+01  9.99200366e+00
 -4.82896199e-01  4.66915031e+01 -7.77081213e-02  4.25672761e+01
  8.13846195e-02 -2.57093369e+01 -1.76921600e+01  1.04620141e+01
 -1.15435804e+01  2.19419691e+00  6.38692184e+01 -2.28523959e-03
  1.03338381e+01  2.27657066e-02  1.08523356e+02  6.25370931e+00
 -2.74305070e+00  1.43245625e-01 -6.46921664e+00 -1.37510071e-02
 -1.67886987e+00 -9.69087675e-02  3.28914765e+00  6.16724319e+00
 -7.81067121e-01 -1.47972637e+01  6.21799447e-02 -1.03722714e+01
 -2.13879708e-01  6.48641799e+00 -3.00615021e+00  1.92559531e+01
  8.94803576e-02  1.57535310e+01  5.06186659e-01 -1.35534988e-02
  1.07019462e+00 -1.61731298e-03  7.78263231e-01 -2.92741135e-03
  4.56989504e+01 -6.52627511e-02 -6.25086163e+01 -4.50136398e-01
 -6.86166383e-05  6.60693518e-02  9.95755336e-04 -1.33889493e+01
  1.77961831e-01  8.93392379e-03  2.89129666e+00  2.50989386e+00
  2.26117054e+01 -1.38353172e+01  4.04525029e-01 -3.31532981e+01
 -4.10615480e-02  1.38304965e+01 -2.68523823e-01 -3.24427317e+02
  1.33717262e+01  9.40868301e+00  1.26282830e+00 -1.93343895e+01
 -2.33638859e-02  3.76511324e+00  3.31155809e-01  8.00803183e+00
  1.70340729e+01 -5.37331360e-01 -1.88059720e+01 -1.50403874e-02
  1.56687270e+01  3.81496449e-01 -5.35748084e-01  1.41791687e+00
  3.31700520e+01  1.26095302e-01  3.60338447e+00  2.06358395e-01
 -1.86797131e-02 -5.44558056e-01  3.10459591e-03  7.36316735e-02
 -2.18920166e-03  2.99011910e+01 -3.54871921e-02 -2.22410110e+01
 -8.82394549e-01 -2.91083621e-04 -4.68910113e-04 -4.09709883e-05
 -6.38134846e+00  1.04616393e-01 -5.25367687e-03  2.22261347e+04
 -2.30818284e+02 -9.29141360e+01  3.74765837e+01  6.12087992e+02
 -3.38300330e-01 -2.06743284e+01 -3.30010694e+01 -7.85597358e+00
  1.04014209e+00 -6.53647573e-01  1.37725369e+01 -2.55435123e-02
  2.59911665e+00  2.23212531e-01 -2.05977717e+00 -6.26398791e-02
  1.07826243e+01 -7.89983178e-02 -2.02486207e+00  9.60831528e-02
 -4.75562875e-02  5.76990497e-01  9.91088697e-05 -4.41843457e-02
 -3.81207775e-02  7.36043832e-01  6.49563329e-02 -4.62039063e+00
 -6.05055736e-01  1.63177377e-04  4.87897204e-03  3.33014983e-04
  1.97337208e-02  2.03058658e-02  1.63227692e-02 -7.14007401e+00
  1.13030690e+01 -1.47088467e-01 -7.32235569e+01 -7.17755747e-02
  2.07390434e+01  3.31950341e-01 -1.18965897e+01  5.68262995e-02
 -7.52644655e+00 -9.07366386e-02 -1.52744895e+01 -2.11980513e-01
  3.05994503e-02 -7.19091166e-01 -8.85786492e-04  1.42792077e-01
 -4.22137034e-03  1.47675757e+01  1.82713636e-01  3.13507529e+01
 -7.24387580e-01 -4.53951439e-04 -6.88952785e-03 -6.04349732e-05
 -6.30302144e+00  5.10618661e-02  9.81138333e-04 -5.81739186e+00
 -1.27219393e+00  5.58503122e+00 -8.79728875e-02  8.74281829e+00
 -4.39141905e-02  1.48127000e-02 -5.73276817e-01 -1.17593458e-02
  4.47980041e-01 -2.87175774e-02  5.10248082e+00  1.05453619e-01
  4.13178786e+00 -3.85725179e-02 -3.82712905e-04  2.11072174e-02
  1.01245484e-03 -6.75716239e+00 -3.47546213e-01 -8.96162601e-06
  6.45680743e-04  7.13843799e-02 -8.51655837e-05 -2.06292915e-02
 -1.28387253e-04 -3.12528699e+00  1.71296189e-03  8.15630259e-01
  5.93592659e-02 -2.04710511e-05 -1.12972711e-03 -3.11198384e-05
  2.28969274e-01  9.32859428e-03  5.06672546e-04  4.66856033e+00
  7.05719916e-02 -8.46159838e+00 -1.01848318e+00 -2.72297746e-04
  1.63677536e-02  1.57267368e-05 -1.38418100e+01  3.03947945e-01
  7.96756424e-03  2.12103078e-06  4.72364976e-04  1.20699406e-06
  7.26451760e-03  9.93394991e-04  5.00209535e-06 -3.79909103e+00
 -2.69434465e-01 -4.67399144e-03  2.22088209e-04] 





deg:  3
coefficient of determination: 0.24291970621804937
intercept: -420270.55259255396
slope: [-2.17239274e+02  9.81141551e-02  8.96976169e-01 ... -2.84839828e-05
 -1.19011384e-06  8.24930682e-08] 





deg:  4
coefficient of determination: 0.29534022303076646
intercept: -165313.0453502522
slope: [ 2.51836253e-02  3.40441267e-05  6.55138213e-05 ... -6.27138311e-07
 -1.94434374e-09  2.96236888e-11] 





deg:  5

Process finished with exit code -1
"""

