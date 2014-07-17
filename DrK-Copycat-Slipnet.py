import pygraphviz


N = ['Bush', 'Rumsfeld']

G = AGraph (strict='false', directed = 'true', landscape='false',ranksep='2.5', splines = 'true', overlap='scalexy', nodesep='0.6', elenght=1.0, eweight=0.5)



for node in N:
    Node_Names.append(node.get_name())
    G.add_node(node.get_name())
    


filename = 'Bush' 
program = 'neato'
G.layout(program, args='-Gepsilon=0.000001; overlap="false"')
file_name = program+"_"+filename
G.write(file_name+"_output.xdot")
G.draw(file_name+".svg")
