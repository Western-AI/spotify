from FinalModels.Main import Main

#hi = Main()
#hi.makegraph()


class MainRunner:
    def __init__(self, model, inputdata):

        main = Main()
        # main.CreateModel(1)
        # main.PredictValues(1, inputData= 'data.csv')

        # inputdata=[64.3,  85.2,  51.7,   0.,    2.64, 45.,    8.09, 84.,    0.,    5.34, 26.,   95., 0.]
        # inputdata=[93.9,  37.7,  49.7,   0.,   94.6,   0.,   32.2,  80.,    0.,    3.32, 65.,   65.7,  4.]

  
        data_V2=[2.30e+01, 8.64e+01, 8.26e+01, 0.00e+00, 2.36e-04, 9.00e+01, 6.63e+00, 8.80e+01,
         1.00e+02, 8.14e+00, 4.10e+01, 5.96e+01, 6.10e+01]


        print(data_V2)
        print(inputdata)

            

        if model == 0:
            print("summing model guess", main.PredictValues(0, inputdata))
        else:
            print("Poly model guess", main.PredictValues(1, inputdata))