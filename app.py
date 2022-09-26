import json
import pickle
from collections import abc, OrderedDict

import numpy as np
from flask import Flask, render_template, logging
from flask import Flask, request, jsonify
# from flask_cors import CORS
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
userFeatures = {}
recommendedProducts = []
recommendedProductsNames = []

if __name__ == '__main__':
    app.config['DEBUG'] = True


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/userRecommendation', methods=["POST"])
# to get the passed features of a user from the frontend and store them in userFeatures
def getUserFeatures():
    try:
        data = request.get_json(force=True)
        if "fecha_dato" and "EmployeeIndex" and "CustomerRresidence" \
                and "sexe" and "age"  \
                and "ind_nuevo" and "canal_entrada" and "indfall" \
                and "cod_prov" and "ind_actividad_cliente" \
                                   "GrossIncome" and "segmentation" in data:
            
            userFeatures["fecha_dato"] = data['fecha_dato']
            userFeatures["EmployeeIndex"] = data['EmployeeIndex']
            userFeatures["CustomerRresidence"] = data['CustomerRresidence']
            userFeatures["sexe"] = data['sexe']
            userFeatures["age"] = data['age']
            userFeatures["ind_nuevo"] = data['ind_nuevo']
            userFeatures["canal_entrada"] = data['canal_entrada']
            userFeatures["indfall"] = data['indfall']
            userFeatures["cod_prov"] = data['cod_prov']
            userFeatures["ind_actividad_cliente"] = data['ind_actividad_cliente']
            userFeatures["GrossIncome"] = data['GrossIncome']
            userFeatures["segmentation"] = data['segmentation']
            print(userFeatures)
            p = list(userFeatures.values())     
            print("---------------")
            r = ValuePredictor(p)
            
            recommendedProducts = r[0].tolist()
            print("3---------------")

            return predictedProds(recommendedProducts)
    except:
        return "bad request55", 500

def ValuePredictor(userFeature):
    print("4 after list ---------------")

    # p = list(userFeature.values())
    print(userFeature)
    to_predict = [userFeature]
    loaded_model = pickle.load(
        open("C:/Users/khadi/Desktop/PFA/flaskProject/decision_tree_classifier_20170212.pkl", "rb"))
    rr = loaded_model.predict(to_predict)
    return rr[[0]]




@app.route('/h')
def GetListofRecommendedProducts():
    # p= [897, 1, 3, 0, 88, 0, 9, 0, 8, 1, 9000, 0]
    # p = list(userFeatures.values())
    # r = ValuePredictor(p)
    # recommendedProducts = r[0].tolist()
    return "it works !!"

def predictedProds(predicts):
    t = 0
    recommendedProductsNames.clear()
    for y in predicts:
        t = t + 1
        if y == 1:
            if t == 1:
                recommendedProductsNames.append("P_SavingAccount")
                # pred += "P_SavingAccount"
            if t == 2:
                recommendedProductsNames.append("P_Garantees")

                # pred += "P_Garantees"
            if t == 3:
                recommendedProductsNames.append("P_currentAccount")

                # pred = "P_currentAccount"
            if t == 4:
                recommendedProductsNames.append("P_Derivada_Account")

                # pred = "P_Derivada_Account"
            if t == 5:
                recommendedProductsNames.append("P_PayrollAccount")

                # pred = "P_PayrollAccount"
            if t == 6:
                recommendedProductsNames.append("P_JuniorAccount")

                # pred = "P_JuniorAccount"
            if t == 7:
                recommendedProductsNames.append("P_MásParticularAccount")
                # pred = "P_MásParticularAccount"
            if t == 8:
                recommendedProductsNames.append("P_ParticularAccount")
                # pred = "P_ParticularAccount"
            if t == 9:
                recommendedProductsNames.append("P_ParticularPlusAccount")
                # pred = "P_ParticularPlusAccount"
            if t == 10:
                recommendedProductsNames.append("P_ShortTermDeposits")
                # pred = "P_ShortTermDeposits"
            if t == 11:
                recommendedProductsNames.append("P_MeduimTermDeposits")
                # pred = "P_MeduimTermDeposits"
            if t == 12:
                recommendedProductsNames.append("P_LongTermDeposits")
                # pred = "P_LongTermDeposits"
            if t == 13:
                recommendedProductsNames.append("P_eAccount")
                # pred = "P_eAccount"
            if t == 14:
                recommendedProductsNames.append("P_Funds")
                # pred = "P_Funds"
            if t == 15:
                recommendedProductsNames.append("P_Mortgage")
                # pred = "P_Mortgage"
            if t == 16:
                recommendedProductsNames.append("P_Pensions")
                # pred = "P_Pensions"
            if t == 17:
                recommendedProductsNames.append("P_Loans")
                # pred = "P_Loans"
            if t == 18:
                recommendedProductsNames.append("P_Taxes")
                # pred = "P_Taxes"
            if t == 19:
                recommendedProductsNames.append("P_CreditCard")
                # pred = "P_CreditCard"
            if t == 20:
                recommendedProductsNames.append("P_securities")
                # pred = "P_securities"
            if t == 21:
                recommendedProductsNames.append("P_HomeAccount")
                # pred = "P_HomeAccount"
            if t == 22:
                recommendedProductsNames.append("P_Payroll")
                # pred = "P_Payroll"
            if t == 23:
                recommendedProductsNames.append("P_DirectDebit")
                # pred = "P_DirectDebit"

    return recommendedProductsNames


# @app.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         to_predict_list = request.form.to_dict()
#         to_predict_list = list(to_predict_list.values())
#         to_predict_list = list(map(int, to_predict_list))
#         result = ValuePredictor(to_predict_list)
#         if int(result) == 1:
#             prediction = 'Income more than 50K'
#         else:
#             prediction = 'Income less that 50K'
#         return render_template("result.html", prediction=prediction)
