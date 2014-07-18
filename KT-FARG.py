import pygraphviz as pgv 

N = ['Bush', 'Rumsfeld', 'Cheney', 'Libby', 'Wolfowitz', 'Myers', 'Powell', 'Armitage', 'Ashcroft', 'Rice', 'Whitman', 'Card', 'Feith']

G = pgv.AGraph (strict='false', directed = 'true', landscape='false',ranksep='2.5', splines = 'true', overlap='scalexy', nodesep='2.5', elenght=2.0, eweight=2.5)

for node in N:
    G.add_node(node)

bush_node = G.get_node('Bush')

bush_node.pos ='4.0!, 1.0!'
#bush_node.attr['pos']=bush_node.attr['pos']+"!"


filename = 'Bush-step0' 
program = 'dot'
G.layout(program, args='-Gepsilon=0.000001; overlap="false"; -n')
file_name = program+"_"+filename
G.write(file_name+"_output.xdot")
G.draw(file_name+".svg")



G.add_edge('Libby', 'Bush', elength='2.0', length = "2.0")


filename = 'Bush-step1' 
G.layout(program, args='-Gepsilon=0.000001; overlap="false"; -Kfdp -n -Tpng -o')
file_name = program+"_"+filename
G.write(file_name+"_output.xdot")
G.draw(file_name+".svg")


################################################################################################################################################

G.add_edge('Bush', 'Cheney', elength='1.0')
G.add_edge('Cheney', 'Libby', elength='1.0')


G.add_edge('Rumsfeld', 'Myers', elength='4.0')


filename = 'Bush-step2' 
G.layout(program, args='-Gepsilon=0.000001; overlap="false"')
file_name = program+"_"+filename
G.write(file_name+"_output.xdot")
G.draw(file_name+".svg")

################################################################################################################################################

G.remove_edge ('Libby', 'Bush')

G.add_edge('Powell', 'Armitage')


filename = 'Bush-step3' 
G.layout(program, args='-Gepsilon=0.000001; overlap="false"')
file_name = program+"_"+filename
G.write(file_name+"_output.xdot")
G.draw(file_name+".svg")



################################################################################################################################################

G.add_edge('Bush', 'Wolfowitz')
G.add_edge('Bush', 'Rice')
G.add_edge('Bush', 'Ashcroft')
G.add_edge('Rumsfeld', 'Feith')



filename = 'Bush-step4' 

G.layout(program, args='-Gepsilon=0.000001; overlap="false"')
file_name = program+"_"+filename
G.write(file_name+"_output.xdot")
G.draw(file_name+".svg")





################################################################################################################################################

G.add_edge('Bush', 'Card')
G.add_edge('Bush', 'Rumsfeld')
G.add_edge('Bush', 'Powell')
G.add_edge('Bush', 'Whitman')



filename = 'Bush-step5' 
G.layout(program, args='-Gepsilon=0.000001; overlap="false"')
file_name = program+"_"+filename
G.write(file_name+"_output.xdot")
G.draw(file_name+".svg")