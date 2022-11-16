import cobra
import os

_file_path = os.path.dirname(__file__)
starting_model_f_name = 'iDT1278.xml'
s_model_path = os.path.join(_file_path, starting_model_f_name)

s_model = cobra.io.read_sbml_model(s_model_path)
s_model.id = "AV"


def modify_compartments(model):
    new_model = model.copy()
    for metabolite in new_model.metabolites:
        if metabolite.id[-2:] == "_u":
            # removes last two characters, namely "_u"
            metabolite.id = metabolite.id[:-2]
            # rename compartment
            metabolite.compartment = metabolite.id[-1]
    return new_model


def modify_model():
    av = modify_compartments(s_model)
    cobra.io.write_sbml_model(av, s_model_path)



if __name__ == '__main__':

    modify_model()