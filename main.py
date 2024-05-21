import AgnostGame.Core as Agn

ele1=Agn.Element("truc1")
ele2=Agn.Element("truc2")
cmp2=Agn.Ensemble("ensemble_de_truc")
cmp2.add(ele1)
cmp2.add(ele2)
cmp2.dump("debug.json")
