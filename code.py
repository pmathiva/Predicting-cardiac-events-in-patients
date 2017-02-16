
import pandas as pd
from sklearn import tree

def my_decision_tree():
    
        #Import the data from the csv file      
        training = pd.read_csv("C:\Users\priya.cse2009\.spyder2\Mydata\cardiac_training.csv")
        testing = pd.read_csv("C:\Users\priya.cse2009\.spyder2\Mydata\mytest.csv")

        cols_to_fit =[ 'bhr', 'basebp','basedp','pkhr','sbp',
              'dp','dose', 'maxhr', 'mphr', 'mbp', 
             'dpmaxdo','dobdose', 'age', 'gender', 'baseEF',
             'dobEF', 'chestpain','posECG', 'equivecg','restwma',
             'posSE','hxofHT', 'hxofdm','hxofcig', 'hxofMI',
             'hxofPTCA', 'hxofCABG']

        #CART
        cart = tree.DecisionTreeClassifier(criterion = 'gini')
        cart = cart.fit(training[cols_to_fit],training['any event'])
        cart_results = cart.predict(testing[cols_to_fit])
        return cart_results[0]

def my_decision_tree_newMI():
    
        #Import the data from the csv file      
        training = pd.read_csv("newMI_training.csv")
        testing = pd.read_csv("C:\Users\priya.cse2009\.spyder2\Mydata\mytest.csv")

        cols_to_fit =[ 'bhr', 'basebp','basedp','pkhr','sbp',
              'dp','dose', 'maxhr', 'mphr', 'mbp', 
             'dpmaxdo','dobdose', 'age', 'gender', 'baseEF',
             'dobEF', 'chestpain','posECG', 'equivecg','restwma',
             'posSE','hxofHT', 'hxofdm','hxofcig', 'hxofMI',
             'hxofPTCA', 'hxofCABG']

        #CART
        cart = tree.DecisionTreeClassifier(criterion = 'gini')
        cart = cart.fit(training[cols_to_fit],training['newMI'])
        cart_results = cart.predict(testing[cols_to_fit])
        return cart_results[0]
        
def my_decision_tree_newPTCA():
    
        training = pd.read_csv("newPTCA_training.csv")
        testing = pd.read_csv("C:\Users\priya.cse2009\.spyder2\Mydata\mytest.csv")

        cols_to_fit =[ 'bhr', 'basebp','basedp','pkhr','sbp',
              'dp','dose', 'maxhr', 'mphr', 'mbp', 
             'dpmaxdo','dobdose', 'age', 'gender', 'baseEF',
             'dobEF', 'chestpain','posECG', 'equivecg','restwma',
             'posSE','hxofHT', 'hxofdm','hxofcig', 'hxofMI',
             'hxofPTCA', 'hxofCABG']

    #CART
        cart = tree.DecisionTreeClassifier(criterion = 'gini')
        cart = cart.fit(training[cols_to_fit],training['newPTCA'])
        cart_results = cart.predict(testing[cols_to_fit])
        return cart_results[0]

def my_decision_tree_newCABG():
    
        #Import the data from the csv file      
        training = pd.read_csv("newCABG_training.csv")
        testing = pd.read_csv("C:\Users\priya.cse2009\.spyder2\Mydata\mytest.csv")

        cols_to_fit =[ 'bhr', 'basebp','basedp','pkhr','sbp',
              'dp','dose', 'maxhr', 'mphr', 'mbp', 
             'dpmaxdo','dobdose', 'age', 'gender', 'baseEF',
             'dobEF', 'chestpain','posECG', 'equivecg','restwma',
             'posSE','hxofHT', 'hxofdm','hxofcig', 'hxofMI',
             'hxofPTCA', 'hxofCABG']

        #CART
        cart = tree.DecisionTreeClassifier(criterion = 'gini')
        cart = cart.fit(training[cols_to_fit],training['newCABG'])
        cart_results = cart.predict(testing[cols_to_fit])
        return cart_results[0]

def my_decision_tree_death():
    
        #Import the data from the csv file      
        training = pd.read_csv("death_training.csv")
        testing = pd.read_csv("C:\Users\priya.cse2009\.spyder2\Mydata\mytest.csv")

        cols_to_fit =[ 'bhr', 'basebp','basedp','pkhr','sbp',
              'dp','dose', 'maxhr', 'mphr', 'mbp', 
             'dpmaxdo','dobdose', 'age', 'gender', 'baseEF',
             'dobEF', 'chestpain','posECG', 'equivecg','restwma',
             'posSE','hxofHT', 'hxofdm','hxofcig', 'hxofMI',
             'hxofPTCA', 'hxofCABG']

        #CART
        cart = tree.DecisionTreeClassifier(criterion = 'gini')
        cart = cart.fit(training[cols_to_fit],training['death'])
        cart_results = cart.predict(testing[cols_to_fit])
        return cart_results[0]

import web
urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('C:\\Users\\priya.cse2009\\Anaconda2\\Lib\\site-packages\\web\\templates\\')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(bhr = 0, basebp = 0,basedp = 0,pkhr = 0,sbp = 0,
              dp = 0,dose = 0, maxhr = 0, mphr = 0, mbp = 0, 
             dpmaxdo = 0,dobdose = 0, age = 0, gender = 0, baseEF = 0,
             dobEF = 0, chestpain = 0,posECG = 0, equivecg = 0,restwma = 0,
             posSE = 0,hxofHT = 0, hxofdm = 0,hxofcig = 0, hxofMI = 0,
             hxofPTCA = 0, hxofCABG = 0)

        header ="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"  % ('bhr', 'basebp','basedp','pkhr','sbp',
              'dp','dose', 'maxhr', 'mphr', 'mbp', 
             'dpmaxdo','dobdose', 'age', 'gender', 'baseEF',
             'dobEF', 'chestpain','posECG', 'equivecg','restwma',
             'posSE','hxofHT', 'hxofdm','hxofcig', 'hxofMI',
             'hxofPTCA', 'hxofCABG')
             
        check = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"  % (form.bhr, form.basebp,form.basedp,form.pkhr,form.sbp,
                 form.dp,form.dose, form.maxhr, form.mphr, form.mbp, 
                 form.dpmaxdo,form.dobdose, form.age, form.gender, form.baseEF,
                 form.dobEF, form.chestpain,form.posECG, form.equivecg,form.restwma,
                 form.posSE,form.hxofHT, form.hxofdm,form.hxofcig, form.hxofMI,
                 form.hxofPTCA, form.hxofCABG)
        
        text_file = open("C:\Users\priya.cse2009\.spyder2\Mydata\mytest.csv", "w")
        text_file.write(header)
        text_file.write(check)
        text_file.close()
        
        output = my_decision_tree()
        outputMI = my_decision_tree_newMI()
        outputPTCA = my_decision_tree_newPTCA()
        outputCABG = my_decision_tree_newCABG()
        outputdeath = my_decision_tree_death()
        g1 = "Event %s " % output
        g2 = "Myocardial Infarction %s " % outputMI
        g3 = "Coronary Angioplasty %s " % outputPTCA
        g4 = "Coronary Artery Bypass Grafting %s " % outputCABG
        g5 = "Death %s " % outputdeath
        return render.index(greeting1 = g1,greeting2 = g2,greeting3 = g3,greeting4 = g4,greeting5 = g5)

if __name__ == "__main__":
    app.run()