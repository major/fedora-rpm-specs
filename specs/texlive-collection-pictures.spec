%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-pictures
Epoch:          12
Version:        svn77389
Release:        1%{?dist}
Summary:        Graphics, pictures, diagrams

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-pictures.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adigraph.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adigraph.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aobs-tikz.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aobs-tikz.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/askmaps.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/askmaps.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asyfig.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asyfig.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asypictureb.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asypictureb.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autoarea.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autoarea.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bardiag.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bardiag.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamerswitch.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamerswitch.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/binarytree.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/binarytree.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blochsphere.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blochsphere.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bloques.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bloques.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blox.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blox.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bodegraph.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bodegraph.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bondgraph.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bondgraph.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bondgraphs.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bondgraphs.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bootstrapicons.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bootstrapicons.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/braids.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/braids.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxeepic.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxeepic.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/byo-twemojis.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/byo-twemojis.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/byrne.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/byrne.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/callouts.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/callouts.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/callouts-box.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/callouts-box.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/celtic.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/celtic.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemfig.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemfig.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/circuit-macros.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/circuit-macros.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/circuitikz.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/circuitikz.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/circularglyphs.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/circularglyphs.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coffeestains.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coffeestains.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coloredbelts.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coloredbelts.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/combinedgraphics.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/combinedgraphics.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/curve.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/curve.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/curve2e.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/curve2e.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/curves.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/curves.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dcpic.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dcpic.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/diagmac2.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/diagmac2.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ditaa.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ditaa.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doc-pictex.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doc-pictex.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dot2texi.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dot2texi.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dottex.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dottex.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dpcircling.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dpcircling.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dratex.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dratex.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drs.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drs.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/duotenzor.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/duotenzor.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dynkin-diagrams.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dynkin-diagrams.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecgdraw.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecgdraw.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eepic.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eepic.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/egpeirce.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/egpeirce.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ellipse.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ellipse.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/endofproofwd.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/endofproofwd.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epspdfconversion.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epspdfconversion.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esk.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esk.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euflag.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euflag.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fadingimage.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fadingimage.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fast-diagram.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fast-diagram.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fenetrecas.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fenetrecas.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figchild.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figchild.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figput.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figput.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fitbox.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fitbox.doc.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/flowchart.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/flowchart.doc.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forest.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forest.doc.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forest-ext.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forest-ext.doc.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/genealogytree.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/genealogytree.doc.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gincltex.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gincltex.doc.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gnuplottex.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gnuplottex.doc.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gradientframe.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gradientframe.doc.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grafcet.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grafcet.doc.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graph35.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graph35.doc.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphicxpsd.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphicxpsd.doc.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphviz.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphviz.doc.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtrlib-largetrees.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtrlib-largetrees.doc.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harveyballs.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harveyballs.doc.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/here.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/here.doc.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hf-tikz.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hf-tikz.doc.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hobby.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hobby.doc.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hvfloat.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hvfloat.doc.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/istgame.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/istgame.doc.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kblocks.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kblocks.doc.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/keisennote.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/keisennote.doc.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kinematikz.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kinematikz.doc.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knitting.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knitting.doc.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knittingpattern.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knittingpattern.doc.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ladder.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ladder.doc.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lapdf.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lapdf.doc.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-make.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-make.doc.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liftarm.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liftarm.doc.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lpic.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lpic.doc.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lroundrect.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lroundrect.doc.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-tikz3dtools.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-tikz3dtools.doc.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamesh.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamesh.doc.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luasseq.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luasseq.doc.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lucide-icons.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lucide-icons.doc.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maker.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maker.doc.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makeshape.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makeshape.doc.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maritime.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maritime.doc.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mercatormap.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mercatormap.doc.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/milsymb.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/milsymb.doc.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/miniplot.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/miniplot.doc.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modiagram.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modiagram.doc.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/neuralnetwork.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/neuralnetwork.doc.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nl-interval.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nl-interval.doc.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nndraw.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nndraw.doc.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numericplots.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numericplots.doc.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/open-everyday-symbols.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/open-everyday-symbols.doc.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/openmoji.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/openmoji.doc.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/optikz.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/optikz.doc.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/outilsgeomtikz.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/outilsgeomtikz.doc.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/papiergurvan.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/papiergurvan.doc.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pb-diagram.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pb-diagram.doc.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf.doc.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-blur.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-blur.doc.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-interference.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-interference.doc.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-periodictable.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-periodictable.doc.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-pie.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-pie.doc.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-soroban.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-soroban.doc.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-spectra.tar.xz
Source231:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-spectra.doc.tar.xz
Source232:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-umlcd.tar.xz
Source233:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-umlcd.doc.tar.xz
Source234:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-umlsd.tar.xz
Source235:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-umlsd.doc.tar.xz
Source236:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfgantt.tar.xz
Source237:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfgantt.doc.tar.xz
Source238:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfkeysearch.tar.xz
Source239:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfkeysearch.doc.tar.xz
Source240:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfkeyx.tar.xz
Source241:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfkeyx.doc.tar.xz
Source242:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfmolbio.tar.xz
Source243:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfmolbio.doc.tar.xz
Source244:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfmorepages.tar.xz
Source245:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfmorepages.doc.tar.xz
Source246:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfopts.tar.xz
Source247:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfopts.doc.tar.xz
Source248:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfornament.tar.xz
Source249:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfornament.doc.tar.xz
Source250:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfplots.tar.xz
Source251:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfplots.doc.tar.xz
Source252:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfplotsthemebeamer.tar.xz
Source253:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfplotsthemebeamer.doc.tar.xz
Source254:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/picinpar.tar.xz
Source255:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/picinpar.doc.tar.xz
Source256:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pict2e.tar.xz
Source257:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pict2e.doc.tar.xz
Source258:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pictex.tar.xz
Source259:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pictex.doc.tar.xz
Source260:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pictex2.tar.xz
Source261:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pictochrono.tar.xz
Source262:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pictochrono.doc.tar.xz
Source263:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pinlabel.tar.xz
Source264:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pinlabel.doc.tar.xz
Source265:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pixelart.tar.xz
Source266:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pixelart.doc.tar.xz
Source267:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pixelarttikz.tar.xz
Source268:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pixelarttikz.doc.tar.xz
Source269:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmgraph.tar.xz
Source270:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmgraph.doc.tar.xz
Source271:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyhedra.tar.xz
Source272:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyhedra.doc.tar.xz
Source273:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyomino.tar.xz
Source274:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyomino.doc.tar.xz
Source275:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/postage.tar.xz
Source276:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/postage.doc.tar.xz
Source277:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/postit.tar.xz
Source278:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/postit.doc.tar.xz
Source279:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prerex.tar.xz
Source280:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prerex.doc.tar.xz
Source281:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prisma-flow-diagram.tar.xz
Source282:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prisma-flow-diagram.doc.tar.xz
Source283:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/productbox.tar.xz
Source284:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/productbox.doc.tar.xz
Source285:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptolemaicastronomy.tar.xz
Source286:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptolemaicastronomy.doc.tar.xz
Source287:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/puyotikz.tar.xz
Source288:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/puyotikz.doc.tar.xz
Source289:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxpgfmark.tar.xz
Source290:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxpgfmark.doc.tar.xz
Source291:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxpic.tar.xz
Source292:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxpic.doc.tar.xz
Source293:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qcircuit.tar.xz
Source294:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qcircuit.doc.tar.xz
Source295:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qrcode.tar.xz
Source296:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qrcode.doc.tar.xz
Source297:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qrcodetikz.tar.xz
Source298:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qrcodetikz.doc.tar.xz
Source299:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/randbild.tar.xz
Source300:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/randbild.doc.tar.xz
Source301:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/randomwalk.tar.xz
Source302:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/randomwalk.doc.tar.xz
Source303:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realhats.tar.xz
Source304:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realhats.doc.tar.xz
Source305:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reotex.tar.xz
Source306:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reotex.doc.tar.xz
Source307:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/robotarm.tar.xz
Source308:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/robotarm.doc.tar.xz
Source309:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rviewport.tar.xz
Source310:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rviewport.doc.tar.xz
Source311:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sa-tikz.tar.xz
Source312:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sa-tikz.doc.tar.xz
Source313:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sacsymb.tar.xz
Source314:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sacsymb.doc.tar.xz
Source315:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schemabloc.tar.xz
Source316:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schemabloc.doc.tar.xz
Source317:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scratch.tar.xz
Source318:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scratch.doc.tar.xz
Source319:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scratch3.tar.xz
Source320:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scratch3.doc.tar.xz
Source321:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scsnowman.tar.xz
Source322:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scsnowman.doc.tar.xz
Source323:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/setdeck.tar.xz
Source324:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/setdeck.doc.tar.xz
Source325:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/signchart.tar.xz
Source326:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/signchart.doc.tar.xz
Source327:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplenodes.tar.xz
Source328:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplenodes.doc.tar.xz
Source329:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simpleoptics.tar.xz
Source330:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simpleoptics.doc.tar.xz
Source331:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/smartdiagram.tar.xz
Source332:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/smartdiagram.doc.tar.xz
Source333:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spath3.tar.xz
Source334:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spath3.doc.tar.xz
Source335:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spectralsequences.tar.xz
Source336:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spectralsequences.doc.tar.xz
Source337:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/strands.tar.xz
Source338:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/strands.doc.tar.xz
Source339:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sunpath.tar.xz
Source340:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sunpath.doc.tar.xz
Source341:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/swimgraf.tar.xz
Source342:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/swimgraf.doc.tar.xz
Source343:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/syntaxdi.tar.xz
Source344:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/syntaxdi.doc.tar.xz
Source345:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/table-fct.tar.xz
Source346:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/table-fct.doc.tar.xz
Source347:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdraw.tar.xz
Source348:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdraw.doc.tar.xz
Source349:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ticollege.tar.xz
Source350:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ticollege.doc.tar.xz
Source351:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-3dplot.tar.xz
Source352:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-3dplot.doc.tar.xz
Source353:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-among-us.tar.xz
Source354:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-among-us.doc.tar.xz
Source355:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bagua.tar.xz
Source356:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bagua.doc.tar.xz
Source357:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bayesnet.tar.xz
Source358:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bayesnet.doc.tar.xz
Source359:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bbox.tar.xz
Source360:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bbox.doc.tar.xz
Source361:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bpmn.tar.xz
Source362:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-bpmn.doc.tar.xz
Source363:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-cd.tar.xz
Source364:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-cd.doc.tar.xz
Source365:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-cookingsymbols.tar.xz
Source366:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-cookingsymbols.doc.tar.xz
Source367:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-decofonts.tar.xz
Source368:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-decofonts.doc.tar.xz
Source369:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-dependency.tar.xz
Source370:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-dependency.doc.tar.xz
Source371:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-dimline.tar.xz
Source372:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-dimline.doc.tar.xz
Source373:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-ext.tar.xz
Source374:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-ext.doc.tar.xz
Source375:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-feynhand.tar.xz
Source376:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-feynhand.doc.tar.xz
Source377:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-feynman.tar.xz
Source378:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-feynman.doc.tar.xz
Source379:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-imagelabels.tar.xz
Source380:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-imagelabels.doc.tar.xz
Source381:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-inet.tar.xz
Source382:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-inet.doc.tar.xz
Source383:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-kalender.tar.xz
Source384:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-kalender.doc.tar.xz
Source385:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-karnaugh.tar.xz
Source386:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-karnaugh.doc.tar.xz
Source387:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-ladder.tar.xz
Source388:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-ladder.doc.tar.xz
Source389:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-lake-fig.tar.xz
Source390:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-lake-fig.doc.tar.xz
Source391:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-layers.tar.xz
Source392:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-layers.doc.tar.xz
Source393:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-mirror-lens.tar.xz
Source394:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-mirror-lens.doc.tar.xz
Source395:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-nef.tar.xz
Source396:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-nef.doc.tar.xz
Source397:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-network.tar.xz
Source398:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-network.doc.tar.xz
Source399:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-nfold.tar.xz
Source400:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-nfold.doc.tar.xz
Source401:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-opm.tar.xz
Source402:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-opm.doc.tar.xz
Source403:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-optics.tar.xz
Source404:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-optics.doc.tar.xz
Source405:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-osci.tar.xz
Source406:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-osci.doc.tar.xz
Source407:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-page.tar.xz
Source408:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-page.doc.tar.xz
Source409:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-palattice.tar.xz
Source410:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-palattice.doc.tar.xz
Source411:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-planets.tar.xz
Source412:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-planets.doc.tar.xz
Source413:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-qtree.tar.xz
Source414:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-qtree.doc.tar.xz
Source415:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-relay.tar.xz
Source416:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-relay.doc.tar.xz
Source417:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-sfc.tar.xz
Source418:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-sfc.doc.tar.xz
Source419:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-shields.tar.xz
Source420:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-shields.doc.tar.xz
Source421:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-swigs.tar.xz
Source422:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-swigs.doc.tar.xz
Source423:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-timing.tar.xz
Source424:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-timing.doc.tar.xz
Source425:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-trackschematic.tar.xz
Source426:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-trackschematic.doc.tar.xz
Source427:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-truchet.tar.xz
Source428:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-truchet.doc.tar.xz
Source429:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz2d-fr.tar.xz
Source430:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz2d-fr.doc.tar.xz
Source431:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz3d-fr.tar.xz
Source432:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz3d-fr.doc.tar.xz
Source433:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzbrickfigurines.tar.xz
Source434:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzbrickfigurines.doc.tar.xz
Source435:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzbricks.tar.xz
Source436:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzbricks.doc.tar.xz
Source437:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzcalendarnotes.tar.xz
Source438:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzcalendarnotes.doc.tar.xz
Source439:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzcodeblocks.tar.xz
Source440:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzcodeblocks.doc.tar.xz
Source441:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzdotncross.tar.xz
Source442:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzdotncross.doc.tar.xz
Source443:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzducks.tar.xz
Source444:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzducks.doc.tar.xz
Source445:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzfill.tar.xz
Source446:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzfill.doc.tar.xz
Source447:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzfxgraph.tar.xz
Source448:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzfxgraph.doc.tar.xz
Source449:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzinclude.tar.xz
Source450:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzinclude.doc.tar.xz
Source451:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzlings.tar.xz
Source452:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzlings.doc.tar.xz
Source453:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzmark.tar.xz
Source454:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzmark.doc.tar.xz
Source455:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzmarmots.tar.xz
Source456:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzmarmots.doc.tar.xz
Source457:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzorbital.tar.xz
Source458:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzorbital.doc.tar.xz
Source459:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpackets.tar.xz
Source460:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpackets.doc.tar.xz
Source461:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpagenodes.tar.xz
Source462:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpagenodes.doc.tar.xz
Source463:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpeople.tar.xz
Source464:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpeople.doc.tar.xz
Source465:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpfeile.tar.xz
Source466:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpfeile.doc.tar.xz
Source467:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpingus.tar.xz
Source468:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzpingus.doc.tar.xz
Source469:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzposter.tar.xz
Source470:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzposter.doc.tar.xz
Source471:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzquads.tar.xz
Source472:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzquads.doc.tar.xz
Source473:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzquests.tar.xz
Source474:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzquests.doc.tar.xz
Source475:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzscale.tar.xz
Source476:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzscale.doc.tar.xz
Source477:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzsymbols.tar.xz
Source478:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzsymbols.doc.tar.xz
Source479:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzviolinplots.tar.xz
Source480:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikzviolinplots.doc.tar.xz
Source481:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tile-graphic.tar.xz
Source482:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tile-graphic.doc.tar.xz
Source483:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tilings.tar.xz
Source484:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tilings.doc.tar.xz
Source485:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/timechart.tar.xz
Source486:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/timechart.doc.tar.xz
Source487:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/timing-diagrams.tar.xz
Source488:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/timing-diagrams.doc.tar.xz
Source489:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipfr.tar.xz
Source490:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipfr.doc.tar.xz
Source491:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-base.tar.xz
Source492:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-base.doc.tar.xz
Source493:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-berge.tar.xz
Source494:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-berge.doc.tar.xz
Source495:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-bernoulli.tar.xz
Source496:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-bernoulli.doc.tar.xz
Source497:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-doc.tar.xz
Source498:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-doc.doc.tar.xz
Source499:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-elements.tar.xz
Source500:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-elements.doc.tar.xz
Source501:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-euclide.tar.xz
Source502:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-euclide.doc.tar.xz
Source503:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-fct.tar.xz
Source504:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-fct.doc.tar.xz
Source505:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-graph.tar.xz
Source506:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-graph.doc.tar.xz
Source507:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-grapheur.tar.xz
Source508:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-grapheur.doc.tar.xz
Source509:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-orm.tar.xz
Source510:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-orm.doc.tar.xz
Source511:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-tab.tar.xz
Source512:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-tab.doc.tar.xz
Source513:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkzexample.tar.xz
Source514:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkzexample.doc.tar.xz
Source515:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tonevalue.tar.xz
Source516:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tonevalue.doc.tar.xz
Source517:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tqft.tar.xz
Source518:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tqft.doc.tar.xz
Source519:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tsemlines.tar.xz
Source520:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tufte-latex.tar.xz
Source521:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tufte-latex.doc.tar.xz
Source522:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twemojis.tar.xz
Source523:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twemojis.doc.tar.xz
Source524:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tzplot.tar.xz
Source525:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tzplot.doc.tar.xz
Source526:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utfsym.tar.xz
Source527:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utfsym.doc.tar.xz
Source528:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vectorlogos.tar.xz
Source529:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vectorlogos.doc.tar.xz
Source530:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/venndiagram.tar.xz
Source531:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/venndiagram.doc.tar.xz
Source532:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vexillology.tar.xz
Source533:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vexillology.doc.tar.xz
Source534:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualpstricks.tar.xz
Source535:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualpstricks.doc.tar.xz
Source536:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wheelchart.tar.xz
Source537:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wheelchart.doc.tar.xz
Source538:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordcloud.tar.xz
Source539:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordcloud.doc.tar.xz
Source540:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/worldflags.tar.xz
Source541:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/worldflags.doc.tar.xz
Source542:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xistercian.tar.xz
Source543:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xistercian.doc.tar.xz
Source544:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpicture.tar.xz
Source545:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpicture.doc.tar.xz
Source546:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xypic.tar.xz
Source547:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xypic.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-adigraph
Requires:       texlive-aobs-tikz
Requires:       texlive-askmaps
Requires:       texlive-asyfig
Requires:       texlive-asypictureb
Requires:       texlive-autoarea
Requires:       texlive-bardiag
Requires:       texlive-beamerswitch
Requires:       texlive-binarytree
Requires:       texlive-blochsphere
Requires:       texlive-bloques
Requires:       texlive-blox
Requires:       texlive-bodegraph
Requires:       texlive-bondgraph
Requires:       texlive-bondgraphs
Requires:       texlive-bootstrapicons
Requires:       texlive-braids
Requires:       texlive-bxeepic
Requires:       texlive-byo-twemojis
Requires:       texlive-byrne
Requires:       texlive-cachepic
Requires:       texlive-callouts
Requires:       texlive-callouts-box
Requires:       texlive-celtic
Requires:       texlive-chemfig
Requires:       texlive-circuit-macros
Requires:       texlive-circuitikz
Requires:       texlive-circularglyphs
Requires:       texlive-coffeestains
Requires:       texlive-collection-basic
Requires:       texlive-coloredbelts
Requires:       texlive-combinedgraphics
Requires:       texlive-curve
Requires:       texlive-curve2e
Requires:       texlive-curves
Requires:       texlive-dcpic
Requires:       texlive-diagmac2
Requires:       texlive-ditaa
Requires:       texlive-doc-pictex
Requires:       texlive-dot2texi
Requires:       texlive-dottex
Requires:       texlive-dpcircling
Requires:       texlive-dratex
Requires:       texlive-drs
Requires:       texlive-duotenzor
Requires:       texlive-dynkin-diagrams
Requires:       texlive-ecgdraw
Requires:       texlive-eepic
Requires:       texlive-egpeirce
Requires:       texlive-ellipse
Requires:       texlive-endofproofwd
Requires:       texlive-epspdf
Requires:       texlive-epspdfconversion
Requires:       texlive-esk
Requires:       texlive-euflag
Requires:       texlive-fadingimage
Requires:       texlive-fast-diagram
Requires:       texlive-fenetrecas
Requires:       texlive-fig4latex
Requires:       texlive-figchild
Requires:       texlive-figput
Requires:       texlive-fitbox
Requires:       texlive-flowchart
Requires:       texlive-forest
Requires:       texlive-forest-ext
Requires:       texlive-genealogytree
Requires:       texlive-getmap
Requires:       texlive-gincltex
Requires:       texlive-gnuplottex
Requires:       texlive-gradientframe
Requires:       texlive-grafcet
Requires:       texlive-graph35
Requires:       texlive-graphicxpsd
Requires:       texlive-graphviz
Requires:       texlive-gtrlib-largetrees
Requires:       texlive-harveyballs
Requires:       texlive-here
Requires:       texlive-hf-tikz
Requires:       texlive-hobby
Requires:       texlive-hvfloat
Requires:       texlive-istgame
Requires:       texlive-kblocks
Requires:       texlive-keisennote
Requires:       texlive-kinematikz
Requires:       texlive-knitting
Requires:       texlive-knittingpattern
Requires:       texlive-ladder
Requires:       texlive-lapdf
Requires:       texlive-latex-make
Requires:       texlive-liftarm
Requires:       texlive-lpic
Requires:       texlive-lroundrect
Requires:       texlive-lua-tikz3dtools
Requires:       texlive-luamesh
Requires:       texlive-luasseq
Requires:       texlive-lucide-icons
Requires:       texlive-maker
Requires:       texlive-makeshape
Requires:       texlive-maritime
Requires:       texlive-mathspic
Requires:       texlive-memoize
Requires:       texlive-mercatormap
Requires:       texlive-milsymb
Requires:       texlive-miniplot
Requires:       texlive-mkpic
Requires:       texlive-modiagram
Requires:       texlive-neuralnetwork
Requires:       texlive-nl-interval
Requires:       texlive-nndraw
Requires:       texlive-numericplots
Requires:       texlive-open-everyday-symbols
Requires:       texlive-openmoji
Requires:       texlive-optikz
Requires:       texlive-outilsgeomtikz
Requires:       texlive-papiergurvan
Requires:       texlive-pb-diagram
Requires:       texlive-petri-nets
Requires:       texlive-pgf
Requires:       texlive-pgf-blur
Requires:       texlive-pgf-interference
Requires:       texlive-pgf-periodictable
Requires:       texlive-pgf-pie
Requires:       texlive-pgf-soroban
Requires:       texlive-pgf-spectra
Requires:       texlive-pgf-umlcd
Requires:       texlive-pgf-umlsd
Requires:       texlive-pgfgantt
Requires:       texlive-pgfkeysearch
Requires:       texlive-pgfkeyx
Requires:       texlive-pgfmolbio
Requires:       texlive-pgfmorepages
Requires:       texlive-pgfopts
Requires:       texlive-pgfornament
Requires:       texlive-pgfplots
Requires:       texlive-pgfplotsthemebeamer
Requires:       texlive-picinpar
Requires:       texlive-pict2e
Requires:       texlive-pictex
Requires:       texlive-pictex2
Requires:       texlive-pictochrono
Requires:       texlive-pinlabel
Requires:       texlive-pixelart
Requires:       texlive-pixelarttikz
Requires:       texlive-pmgraph
Requires:       texlive-polyhedra
Requires:       texlive-polyomino
Requires:       texlive-postage
Requires:       texlive-postit
Requires:       texlive-prerex
Requires:       texlive-prisma-flow-diagram
Requires:       texlive-productbox
Requires:       texlive-ptolemaicastronomy
Requires:       texlive-puyotikz
Requires:       texlive-pxpgfmark
Requires:       texlive-pxpic
Requires:       texlive-qcircuit
Requires:       texlive-qrcode
Requires:       texlive-qrcodetikz
Requires:       texlive-randbild
Requires:       texlive-randomwalk
Requires:       texlive-realhats
Requires:       texlive-reotex
Requires:       texlive-robotarm
Requires:       texlive-rviewport
Requires:       texlive-sa-tikz
Requires:       texlive-sacsymb
Requires:       texlive-schemabloc
Requires:       texlive-scratch
Requires:       texlive-scratch3
Requires:       texlive-scsnowman
Requires:       texlive-setdeck
Requires:       texlive-signchart
Requires:       texlive-simplenodes
Requires:       texlive-simpleoptics
Requires:       texlive-smartdiagram
Requires:       texlive-spath3
Requires:       texlive-spectralsequences
Requires:       texlive-strands
Requires:       texlive-sunpath
Requires:       texlive-swimgraf
Requires:       texlive-syntaxdi
Requires:       texlive-table-fct
Requires:       texlive-texdraw
Requires:       texlive-ticollege
Requires:       texlive-tikz-3dplot
Requires:       texlive-tikz-among-us
Requires:       texlive-tikz-bagua
Requires:       texlive-tikz-bayesnet
Requires:       texlive-tikz-bbox
Requires:       texlive-tikz-bpmn
Requires:       texlive-tikz-cd
Requires:       texlive-tikz-cookingsymbols
Requires:       texlive-tikz-decofonts
Requires:       texlive-tikz-dependency
Requires:       texlive-tikz-dimline
Requires:       texlive-tikz-ext
Requires:       texlive-tikz-feynhand
Requires:       texlive-tikz-feynman
Requires:       texlive-tikz-imagelabels
Requires:       texlive-tikz-inet
Requires:       texlive-tikz-kalender
Requires:       texlive-tikz-karnaugh
Requires:       texlive-tikz-ladder
Requires:       texlive-tikz-lake-fig
Requires:       texlive-tikz-layers
Requires:       texlive-tikz-mirror-lens
Requires:       texlive-tikz-nef
Requires:       texlive-tikz-network
Requires:       texlive-tikz-nfold
Requires:       texlive-tikz-opm
Requires:       texlive-tikz-optics
Requires:       texlive-tikz-osci
Requires:       texlive-tikz-page
Requires:       texlive-tikz-palattice
Requires:       texlive-tikz-planets
Requires:       texlive-tikz-qtree
Requires:       texlive-tikz-relay
Requires:       texlive-tikz-sfc
Requires:       texlive-tikz-shields
Requires:       texlive-tikz-swigs
Requires:       texlive-tikz-timing
Requires:       texlive-tikz-trackschematic
Requires:       texlive-tikz-truchet
Requires:       texlive-tikz2d-fr
Requires:       texlive-tikz3d-fr
Requires:       texlive-tikzbrickfigurines
Requires:       texlive-tikzbricks
Requires:       texlive-tikzcalendarnotes
Requires:       texlive-tikzcodeblocks
Requires:       texlive-tikzdotncross
Requires:       texlive-tikzducks
Requires:       texlive-tikzfill
Requires:       texlive-tikzfxgraph
Requires:       texlive-tikzinclude
Requires:       texlive-tikzlings
Requires:       texlive-tikzmark
Requires:       texlive-tikzmarmots
Requires:       texlive-tikzorbital
Requires:       texlive-tikzpackets
Requires:       texlive-tikzpagenodes
Requires:       texlive-tikzpeople
Requires:       texlive-tikzpfeile
Requires:       texlive-tikzpingus
Requires:       texlive-tikzposter
Requires:       texlive-tikzquads
Requires:       texlive-tikzquests
Requires:       texlive-tikzscale
Requires:       texlive-tikzsymbols
Requires:       texlive-tikztosvg
Requires:       texlive-tikzviolinplots
Requires:       texlive-tile-graphic
Requires:       texlive-tilings
Requires:       texlive-timechart
Requires:       texlive-timing-diagrams
Requires:       texlive-tipfr
Requires:       texlive-tkz-base
Requires:       texlive-tkz-berge
Requires:       texlive-tkz-bernoulli
Requires:       texlive-tkz-doc
Requires:       texlive-tkz-elements
Requires:       texlive-tkz-euclide
Requires:       texlive-tkz-fct
Requires:       texlive-tkz-graph
Requires:       texlive-tkz-grapheur
Requires:       texlive-tkz-orm
Requires:       texlive-tkz-tab
Requires:       texlive-tkzexample
Requires:       texlive-tonevalue
Requires:       texlive-tqft
Requires:       texlive-tsemlines
Requires:       texlive-tufte-latex
Requires:       texlive-twemojis
Requires:       texlive-tzplot
Requires:       texlive-utfsym
Requires:       texlive-vectorlogos
Requires:       texlive-venndiagram
Requires:       texlive-vexillology
Requires:       texlive-visualpstricks
Requires:       texlive-wheelchart
Requires:       texlive-wordcloud
Requires:       texlive-worldflags
Requires:       texlive-xistercian
Requires:       texlive-xpicture
Requires:       texlive-xypic

%description
Including TikZ, pict, etc., but MetaPost and PStricks are separate.


%package -n texlive-adigraph
Summary:        Augmenting directed graphs
Version:        svn70422
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(adigraph.sty) = %{tl_version}

%description -n texlive-adigraph
This LaTeX package provides the means to easily draw augmenting oriented
graphs, as well as cuts on them, to demonstrate steps of algorithms for solving
max-flow min-cut problems. This package requires the other LaTeX packages fp,
xparse, xstring, and TikZ (in particular the TikZ calc library).

%package -n texlive-aobs-tikz
Summary:        TikZ styles for creating overlaid pictures in beamer
Version:        svn70952
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibraryoverlay-beamer-styles.code.tex) = %{tl_version}

%description -n texlive-aobs-tikz
The package defines auxiliary TikZ styles useful for overlaying pictures'
elements in Beamer. The TikZ styles are grouped in a library,
overlay-beamer-styles which is automatically called by the package itself.
Users may either load just aobs-tikz or the library; the latter method
necessitates TikZ manual load.

%package -n texlive-askmaps
Summary:        Typeset American style Karnaugh maps
Version:        svn56730
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(askmaps.sty) = %{tl_version}

%description -n texlive-askmaps
The package provides 1, 2, 3, 4 and 5 variable Karnaugh maps, in the style used
in numerous American textbooks on digital design. The package draws K-maps
where the most significant input variables are placed on top of the columns and
the least significant variables are placed left of the rows.

%package -n texlive-asyfig
Summary:        Commands for using Asymptote figures
Version:        svn17512
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(catchfile.sty)
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifmtarg.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(import.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(preview.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(asyalign.sty) = %{tl_version}
Provides:       tex(asyfig.sty) = %{tl_version}
Provides:       tex(asyprocess.sty) = %{tl_version}

%description -n texlive-asyfig
The package provides a means of reading Asymptote figures from separate files,
rather than within the document, as is standard in the asymptote package, which
is provided as part of the Asymptote bundle. The asymptote way can prove
cumbersome in a large document; the present package allows the user to process
one picture at a time, in simple test documents, and then to migrate (with no
fuss) to their use in the target document.

%package -n texlive-asypictureb
Summary:        User-friendly integration of Asymptote into LaTeX
Version:        svn73611
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fancyvrb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(verbatimcopy.sty)
Provides:       tex(asypictureB.sty) = %{tl_version}

%description -n texlive-asypictureb
The package is an unofficial alternative to the package provided with the
Asymptote distribution, for including pictures within a LaTeX source file.
While it does not duplicate all the features of the official package, this
package is more user-friendly in several ways. Most notably, Asymptote errors
are repackaged as LaTeX errors, making debugging less of a pain. It also has a
more robust mechanism for identifying unchanged pictures that need not be
recompiled.

%package -n texlive-autoarea
Summary:        Automatic computation of bounding boxes with PiCTeX
Version:        svn59552
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(autoarea.sty) = %{tl_version}

%description -n texlive-autoarea
This package makes PiCTeX recognize lines and arcs in determining the "bounding
box" of a picture. (PiCTeX so far accounted for put commands only). The
"bounding box" is essential for proper placement of a picture between running
text and margins and for keeping the running text away.

%package -n texlive-bardiag
Summary:        LaTeX package for drawing bar diagrams
Version:        svn22013
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fp-snap.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listings.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pstcol.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(barddoc.sty) = %{tl_version}
Provides:       tex(bardiag.sty) = %{tl_version}
Provides:       tex(pstfp.sty) = %{tl_version}

%description -n texlive-bardiag
The main purpose of the package is to make the drawing of bar diagrams possible
and easy in LaTeX. The BarDiag package is inspired by and based on PSTricks.

%package -n texlive-beamerswitch
Summary:        Convenient mode selection in Beamer documents
Version:        svn64182
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-beamerswitch
This class is a wrapper around the beamer class to make it easier to use the
same document to generate the different forms of the presentation: the slides
themselves, an abbreviated slide set for transparencies or online reference, an
n-up handout version (various layouts are provided), and a transcript or set of
notes using the article class. The class provides a variety of handout layouts,
and allows the mode to be chosen from the command line (without changing the
document itself).

%package -n texlive-binarytree
Summary:        Drawing binary trees using TikZ
Version:        svn41777
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(binarytree.sty) = %{tl_version}

%description -n texlive-binarytree
This package provides an easy but flexible way to draw binary trees using TikZ.
A path specification and the setting of various options determine the style for
each edge of the tree. There is support for the external library of TikZ which
does not affect externalization of the rest of the TikZ figures in the
document. There is an option to use automatic file naming: useful if the trees
are often moved around.

%package -n texlive-blochsphere
Summary:        Draw pseudo-3D diagrams of Bloch spheres
Version:        svn38388
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(tikz.sty)
Provides:       tex(blochsphere.sty) = %{tl_version}

%description -n texlive-blochsphere
This package is used to draw pseudo-3D Blochsphere diagrams. It supports
various annotations, such as great and small circles, axes, rotation markings
and state vectors. It can be used in a standalone fashion, or nested within a
tikzpicture environment by setting the environment option nested to true.

%package -n texlive-bloques
Summary:        Generate control diagrams
Version:        svn22490
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(bloques.sty) = %{tl_version}

%description -n texlive-bloques
The package uses TikZ to provide commands for generating control diagrams
(specially in power electronics).

%package -n texlive-blox
Summary:        Draw block diagrams, using TikZ
Version:        svn57949
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(tikz.sty)
Provides:       tex(blox.sty) = %{tl_version}

%description -n texlive-blox
This package, along with TikZ, will typeset block diagrams for use with
programming and control theory. It is an English translation of the schemabloc
package.

%package -n texlive-bodegraph
Summary:        Draw Bode, Nyquist and Black plots with gnuplot and TikZ
Version:        svn72949
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifsym.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
Requires:       tex(tikz.sty)
Provides:       tex(bodegraph.sty) = %{tl_version}

%description -n texlive-bodegraph
The package provides facilities to draw Bode, Nyquist and Black plots using
Gnuplot and Tikz. Elementary Transfer Functions and basic correctors are
preprogrammed for use.

%package -n texlive-bondgraph
Summary:        Create bond graph figures in LaTeX documents
Version:        svn21670
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(bondgraph.sty) = %{tl_version}

%description -n texlive-bondgraph
The package draws bond graphs using PGF and TikZ.

%package -n texlive-bondgraphs
Summary:        Draws bond graphs in LaTeX, using PGF/TikZ
Version:        svn36605
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(bm.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Provides:       tex(bondgraphs.sty) = %{tl_version}

%description -n texlive-bondgraphs
The package is used to draw bond graphs in LaTeX. It uses a recent version
(3.0+) of PGF and TikZ for the drawing, hence, it is mainly a set of TikZ
styles that makes the drawing of bond graphs easier. Compared to the bondgraph
package this package relies more on TikZ styles and less on macros, to generate
the drawings. As such it can be more flexible than his, but requires more TikZ
knowledge of the user.

%package -n texlive-bootstrapicons
Summary:        Icons from the framework Bootstrap
Version:        svn76502
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(bootstrapicons.sty) = %{tl_version}

%description -n texlive-bootstrapicons
The package provides over 2,000 icons from the frontend framework Bootstrap.
Note: this is NOT an official package from Bootstrap.

%package -n texlive-braids
Summary:        Draw braid diagrams with PGF/TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(braids.sty) = %{tl_version}
Provides:       tex(tikzlibrarybraids.code.tex) = %{tl_version}

%description -n texlive-braids
The package enables drawing of braid diagrams with PGF/TikZ using a simple
syntax. The braid itself is specified by giving a word in the braid group, and
there are many options for styling the strands and for drawing "floors".

%package -n texlive-bxeepic
Summary:        Eepic facilities using pict2e
Version:        svn30559
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bxdpxp2e.def) = %{tl_version}
Provides:       tex(bxeepic.sty) = %{tl_version}

%description -n texlive-bxeepic
The package provides an eepic driver to use pict2e facilities.

%package -n texlive-byo-twemojis
Summary:        "Build Your Own Twemojis" with TikZ
Version:        svn58917
License:        CC-BY-4.0 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(byo-twemojis.sty) = %{tl_version}

%description -n texlive-byo-twemojis
This package provides the means to create your own emojis (the simple, round,
and mostly yellow ones) from elements of existing emojis. The provided command
creates a TikZ picture from the stated elements with multiple possibilities to
modify the result in color and position.

%package -n texlive-byrne
Summary:        Typeset geometric proofs in the style of Oliver Byrne's 1847 edition of Euclid's "Elements"
Version:        svn77031
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifmtarg.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(xparse.sty)
Provides:       tex(byrne.sty) = %{tl_version}

%description -n texlive-byrne
This package is a LaTeX adaptation of a set of tools developed for ConTeXt
reproduction of Oliver Byrne's 1847 edition of the first six books of Euclid's
"Elements". It consists of a MetaPost library, responsible for all the drawing,
and a set of LaTeX macros to conveniently use them. This package works with
LuaLaTeX and relies on luamplib v2.23.0 or higher.

%package -n texlive-callouts
Summary:        Put simple annotations and notes inside a picture
Version:        svn44899
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Provides:       tex(callouts.sty) = %{tl_version}

%description -n texlive-callouts
The package defines the annotation environment in which callouts, notes,
arrows, and the like can be placed to describe certain parts of a picture.

%package -n texlive-callouts-box
Summary:        Provides visually appealing callout boxes
Version:        svn74635
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tcolorbox.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(callouts-box-colors.sty) = %{tl_version}
Provides:       tex(callouts-box.sty) = %{tl_version}

%description -n texlive-callouts-box
This package provides a collection of visually appealing, structured callout
boxes for LaTeX documents. These boxes are useful for highlighting important
information such as warnings, errors, notes, and success messages. The package
is built on top of tcolorbox for highly customizable, breakable callout boxes
and xcolor for predefined color schemes.

%package -n texlive-celtic
Summary:        A TikZ library for drawing celtic knots
Version:        svn39797
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibraryceltic.code.tex) = %{tl_version}

%description -n texlive-celtic
The package provides a TikZ library for drawing celtic knots.

%package -n texlive-chemfig
Summary:        Draw molecules with easy syntax
Version:        svn76701
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(chemfig-lewis.tex) = %{tl_version}
Provides:       tex(chemfig.sty) = %{tl_version}
Provides:       tex(chemfig.tex) = %{tl_version}

%description -n texlive-chemfig
The package provides the command \chemfig{<code>}, which draws molecules using
the TikZ package. The <code> argument provides instructions for the drawing
operation. While the diagrams produced are essentially 2-dimensional, the
package supports many of the conventional notations for illustrating the
3-dimensional layout of a molecule. The package uses TikZ for its actual
drawing operations.

%package -n texlive-circuit-macros
Summary:        M4 macros for electric circuit diagrams
Version:        svn76218
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(boxdims.sty) = %{tl_version}

%description -n texlive-circuit-macros
A set of m4 macros for drawing high-quality electric circuits containing
fundamental elements, amplifiers, transistors, and basic logic gates to include
in TeX, LaTeX, or similar documents. Some tools and examples for other types of
diagrams are also included. The macros can be evaluated to drawing commands in
the pic language, which is very easy to understand and which has a good
power/complexity ratio. Pic contains elements of a simple programming language,
and is well-suited to line drawings requiring parametric or conditional
components, fine tuning, significant geometric calculations or repetition, or
that are naturally block structured or tree structured. (The m4 and pic
processors are readily available for Unix and PC machines.) Alternative output
macros can create TeX output to be read by pstricks, TikZ commands for use by
the pgf bundle, or SVG.

%package -n texlive-circuitikz
Summary:        Draw electrical networks with TikZ
Version:        svn77296
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(circuitikz-0.4-body.tex) = %{tl_version}
Provides:       tex(circuitikz-0.4.sty) = %{tl_version}
Provides:       tex(circuitikz-0.6-body.tex) = %{tl_version}
Provides:       tex(circuitikz-0.6.sty) = %{tl_version}
Provides:       tex(circuitikz-0.7-body.tex) = %{tl_version}
Provides:       tex(circuitikz-0.7.sty) = %{tl_version}
Provides:       tex(circuitikz-0.8.3-body.tex) = %{tl_version}
Provides:       tex(circuitikz-0.8.3.sty) = %{tl_version}
Provides:       tex(circuitikz-0.9.3-body.tex) = %{tl_version}
Provides:       tex(circuitikz-0.9.3.sty) = %{tl_version}
Provides:       tex(circuitikz-0.9.6-body.tex) = %{tl_version}
Provides:       tex(circuitikz-0.9.6.sty) = %{tl_version}
Provides:       tex(circuitikz-1.0-body.tex) = %{tl_version}
Provides:       tex(circuitikz-1.0.sty) = %{tl_version}
Provides:       tex(circuitikz-1.1.2-body.tex) = %{tl_version}
Provides:       tex(circuitikz-1.1.2.sty) = %{tl_version}
Provides:       tex(circuitikz-1.2.7-body.tex) = %{tl_version}
Provides:       tex(circuitikz-1.2.7.sty) = %{tl_version}
Provides:       tex(circuitikz-1.4.6-body.tex) = %{tl_version}
Provides:       tex(circuitikz-1.4.6.sty) = %{tl_version}
Provides:       tex(circuitikz-1.7.2-body.tex) = %{tl_version}
Provides:       tex(circuitikz-1.7.2.sty) = %{tl_version}
Provides:       tex(circuitikz.sty) = %{tl_version}
Provides:       tex(ctikzstyle-example.tex) = %{tl_version}
Provides:       tex(ctikzstyle-legacy.tex) = %{tl_version}
Provides:       tex(ctikzstyle-romano.tex) = %{tl_version}
Provides:       tex(pgfcirc.defines.tex) = %{tl_version}
Provides:       tex(pgfcircbipoles.tex) = %{tl_version}
Provides:       tex(pgfcirccurrent.tex) = %{tl_version}
Provides:       tex(pgfcircflow.tex) = %{tl_version}
Provides:       tex(pgfcirclabel.tex) = %{tl_version}
Provides:       tex(pgfcircmonopoles.tex) = %{tl_version}
Provides:       tex(pgfcircmultipoles.tex) = %{tl_version}
Provides:       tex(pgfcircpath.tex) = %{tl_version}
Provides:       tex(pgfcircquadpoles.tex) = %{tl_version}
Provides:       tex(pgfcircshapes.tex) = %{tl_version}
Provides:       tex(pgfcirctripoles.tex) = %{tl_version}
Provides:       tex(pgfcircutils.tex) = %{tl_version}
Provides:       tex(pgfcircvoltage.tex) = %{tl_version}
Provides:       tex(t-circuitikz-0.8.3.tex) = %{tl_version}
Provides:       tex(t-circuitikz-0.9.3.tex) = %{tl_version}
Provides:       tex(t-circuitikz-0.9.6.tex) = %{tl_version}
Provides:       tex(t-circuitikz-1.0.tex) = %{tl_version}
Provides:       tex(t-circuitikz-1.1.2.tex) = %{tl_version}
Provides:       tex(t-circuitikz-1.2.7.tex) = %{tl_version}
Provides:       tex(t-circuitikz-1.4.6.tex) = %{tl_version}
Provides:       tex(t-circuitikz-1.7.2.tex) = %{tl_version}
Provides:       tex(t-circuitikz.tex) = %{tl_version}

%description -n texlive-circuitikz
The package provides a set of macros for naturally typesetting electrical and
(somewhat less naturally, perhaps) electronic networks. It is designed as a
tool that is easy to use, with a lean syntax, native to LaTeX, and directly
supporting PDF output format. It has therefore been based on the very
impressive PGF/TikZ package.

%package -n texlive-circularglyphs
Summary:        A circular glyphs alphabet
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(circularglyphs.sty) = %{tl_version}

%description -n texlive-circularglyphs
Circular Glyphs is a graphic alphabet of substitution based on a geometric
construction using circles and arcs on a grid. The designs are all based on
circular arcs, divided into four quadrants. It is inspired by Star Trek and
used by the Bynar and Borg cultures depicted there.

%package -n texlive-coffeestains
Summary:        Add coffee stains to documents
Version:        svn59703
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Provides:       tex(coffeestains.sty) = %{tl_version}

%description -n texlive-coffeestains
This package provides an essential feature that LaTeX has been missing for too
long: It adds coffee stains to your documents. A lot of time can be saved by
printing stains directly on the page rather than adding them manually.

%package -n texlive-coloredbelts
Summary:        Insert colored belts in documents (to present skills, for example)
Version:        svn76924
License:        LPPL-1.3c AND CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Provides:       tex(coloredbelts.sty) = %{tl_version}

%description -n texlive-coloredbelts
The package provides commands (English and French version) to insert 'colored
belts' (in vectorial format) to present skills, for example.

%package -n texlive-combinedgraphics
Summary:        Include graphic (EPS or PDF)/LaTeX combinations
Version:        svn27198
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Provides:       tex(combinedgraphics.sty) = %{tl_version}

%description -n texlive-combinedgraphics
This package provides a macro (\includecombinedgraphics) for the inclusion of
combined EPS/LaTeX and PDF/LaTeX graphics (an export format of Gnuplot, Xfig,
and maybe other programs). Instead of including the graphics with a simple
\input, the \includecombinedgraphics macro has some comforts: changing the font
and color of the text of the LaTeX part; rescaling the graphics without
affecting the font of the LaTeX part; automatic inclusion of the vector
graphics part, as far as LaTeX part does not do it (e.g., for files exported
from Gnuplot before version 4.2); and rescaling and rotating of complete
graphics (similar to \includegraphics from the graphicx package).

%package -n texlive-curve
Summary:        A class for making curriculum vitae
Version:        svn20745
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-curve
CurVe is a class for writing a CV, with configuration for the language in which
you write. The class provides a set of commands to create rubrics, entries in
these rubrics etc. CurVe then format the CV (possibly splitting it onto
multiple pages, repeating the titles etc), which is usually the most painful
part of CV writing. Another nice feature of CurVe is its ability to manage
different CV 'flavours' simultaneously. It is often the case that you want to
maintain slightly divergent versions of your CV at the same time, in order to
emphasize on different aspects of your background. CurVe also comes with
support for use with AUC-TeX.

%package -n texlive-curve2e
Summary:        Extensions for package pict2e
Version:        svn72842
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xparse.sty)
Provides:       tex(curve2e-v161.sty) = %{tl_version}
Provides:       tex(curve2e.sty) = %{tl_version}

%description -n texlive-curve2e
The package extends the drawing capacities of the pict2e that serves as a
LaTeX2e replacement for picture mode. In particular, curve2e introduces new
macros for lines and vectors, new specifications for line terminations and
joins, arcs with any angular aperture, arcs with arrows at one or both ends,
generic curves specified with their nodes and the tangent direction at these
nodes.

%package -n texlive-curves
Summary:        Curves for LaTeX picture environment
Version:        svn45255
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(curves.sty) = %{tl_version}
Provides:       tex(curvesls.sty) = %{tl_version}

%description -n texlive-curves
This package draws curves in the standard LaTeX picture environment using
parabolas between data points with continuous slope at joins; for circles and
arcs, it uses up to 16 parabolas. The package can also draw symbols or dash
patterns along curves. The package provides facilities equivalent to technical
pens with compasses and French curves. Curves consist of short secants drawn by
overlapping disks or line-drawing \special commands selected by package
options.

%package -n texlive-dcpic
Summary:        Commutative diagrams in a LaTeX and TeX documents
Version:        svn30206
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dcpic.sty) = %{tl_version}

%description -n texlive-dcpic
DCpic is a package for typesetting Commutative Diagrams within a LaTeX and TeX
documents. Its distinguishing features are: a powerful graphical engine, the
PiCTeX package; an easy specification syntax in which a commutative diagram is
described in terms of its objects and its arrows (morphism), positioned in a
Cartesian coordinate system.

%package -n texlive-diagmac2
Summary:        Diagram macros, using pict2e
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(diagmac2.sty) = %{tl_version}

%description -n texlive-diagmac2
This is a development of the long-established diagmac package, using pict2e so
that the restrictions on line direction are removed.

%package -n texlive-ditaa
Summary:        Use ditaa diagrams within LaTeX documents
Version:        svn48932
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fancyvrb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(ditaa.sty) = %{tl_version}

%description -n texlive-ditaa
With this package ditaa (DIagrams Through Ascii Art) diagrams can be embedded
directly into LaTeX files.

%package -n texlive-doc-pictex
Summary:        A summary list of PicTeX documentation
Version:        svn24927
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-doc-pictex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-doc-pictex-doc <= 11:%{version}

%description -n texlive-doc-pictex
A summary of available resources providing (or merely discussing) documentation
of PicTeX.

%package -n texlive-dot2texi
Summary:        Create graphs within LaTeX using the dot2tex tool
Version:        svn26237
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(moreverb.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(dot2texi.sty) = %{tl_version}

%description -n texlive-dot2texi
The dot2texi package allows you to embed graphs in the DOT graph description
language in your LaTeX documents. The dot2tex tool is used to invoke Graphviz
for graph layout, and to transform the output from Graphviz to LaTeX code. The
generated code relies on the TikZ and PGF package or the PSTricks package. The
process is automated if shell escape is enabled.

%package -n texlive-dottex
Summary:        Use dot code in LaTeX
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(moreverb.sty)
Provides:       tex(dottex.sty) = %{tl_version}

%description -n texlive-dottex
The dottex package allows you to encapsulate 'dot' and 'neato' files in your
document (dot and neato are both part of graphviz; dot creates directed graphs,
neato undirected graphs). If you have shell-escape enabled, the package will
arrange for your files to be processed at LaTeX time; otherwise, the conversion
must be done manually as an intermediate process before a second LaTeX run.

%package -n texlive-dpcircling
Summary:        Decorated text boxes using TikZ
Version:        svn54994
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(tikz.sty)
Provides:       tex(DPcircling.sty) = %{tl_version}

%description -n texlive-dpcircling
This simple package provides four types of text decorations using TikZ. You can
frame your text with circles, rectangles, jagged rectangles, and fan-shapes.
The baseline will be adjusted properly according to the surroundings. You can
use these decorations both in text mode and in math mode. You can specify line
color, line width, width, and height using option keys. Note: The "DP" in the
package name stands for "Decorated Packets".

%package -n texlive-dratex
Summary:        General drawing macros
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(AlDraTex.sty) = %{tl_version}
Provides:       tex(DraTex.sty) = %{tl_version}
Provides:       tex(TeXProject.sty) = %{tl_version}
Provides:       tex(wotree.sty) = %{tl_version}

%description -n texlive-dratex
A low level (DraTex.sty) and a high-level (AlDraTex.sty) drawing package
written entirely in TeX.

%package -n texlive-drs
Summary:        Typeset Discourse Representation Structures (DRS)
Version:        svn19232
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(drs.sty) = %{tl_version}

%description -n texlive-drs
The package draws Discourse Representation Structures (DRSs). It can draw
embedded DRSs, if-then conditions and quantificational "duplex conditions"
(with a properly scaled connecting diamond). Formatting parameters allow the
user to control the appearance and placement of DRSs, and of DRS variables and
conditions. The package is based on DRS macros in the covington package.

%package -n texlive-duotenzor
Summary:        Drawing package for circuit and duotensor diagrams
Version:        svn76130
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xspace.sty)
Provides:       tex(duotenzor.sty) = %{tl_version}

%description -n texlive-duotenzor
This is a drawing package for circuit and duotensor diagrams within LaTeX
documents. It consists of about eighty commands, calling on TikZ for support.

%package -n texlive-dynkin-diagrams
Summary:        Draw Dynkin, Coxeter, and Satake diagrams using TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(dynkin-diagrams.sty) = %{tl_version}

%description -n texlive-dynkin-diagrams
Draws Dynkin, Coxeter, and Satake diagrams in LaTeX documents, using the TikZ
package. The package requires amsmath, amssymb, etoolbox, expl3, mathtools,
pgfkeys, pgfopts, TikZ, xparse, and xstring.

%package -n texlive-ecgdraw
Summary:        Draws electrocardiograms (ECG)
Version:        svn76130
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(ecgdraw.sty) = %{tl_version}

%description -n texlive-ecgdraw
This package provides the \ECG{<code>} command which draws electrocardiograms
(ECG). The <code> represents a series of abbreviations which allow to draw
different types of wave.

%package -n texlive-eepic
Summary:        Extensions to epic and the LaTeX drawing tools
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eepic.sty) = %{tl_version}
Provides:       tex(eepicemu.sty) = %{tl_version}
Provides:       tex(epic.sty) = %{tl_version}

%description -n texlive-eepic
Extensions to epic and the LaTeX picture drawing environment, include the
drawing of lines at any slope, the drawing of circles in any radii, and the
drawing of dotted and dashed lines much faster with much less TeX memory, and
providing several new commands for drawing ellipses, arcs, splines, and filled
circles and ellipses. The package uses tpic \special commands.

%package -n texlive-egpeirce
Summary:        Draw existential graphs invented by Charles S. Peirce
Version:        svn66924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(everypage.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-text.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(setspace.sty)
Provides:       tex(egpeirce.sty) = %{tl_version}

%description -n texlive-egpeirce
This package is for drawing existential graphs invented and developed by
philosopher and polymath Charles S. Peirce. It also contains new and unique
symbols for several types of linear logical operators Peirce invented and used
in his larger logical system.

%package -n texlive-ellipse
Summary:        Draw ellipses and elliptical arcs using the standard LaTeX2e picture environment
Version:        svn39025
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ellipse.sty) = %{tl_version}

%description -n texlive-ellipse
Draw ellipses and elliptical arcs using the standard LaTeX2e picture
environment.

%package -n texlive-endofproofwd
Summary:        An "end of proof" sign
Version:        svn55643
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(import.sty)
Provides:       tex(endofproofwd.sty) = %{tl_version}

%description -n texlive-endofproofwd
This package provides an additional "end of proof" sign. The command's name is
\wasserdicht.

%package -n texlive-epspdfconversion
Summary:        On-the-fly conversion of EPS to PDF
Version:        svn18703
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(epstopdf-base.sty)
Requires:       tex(graphics.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(epspdfconversion.sty) = %{tl_version}

%description -n texlive-epspdfconversion
The package calls the epstopdf package to convert EPS graphics to PDF, on the
fly. It servs as a vehicle for passing conversion options (such as grayscale,
prepress or pdfversion) to the epspdf converter.

%package -n texlive-esk
Summary:        Package to encapsulate Sketch files in LaTeX sources
Version:        svn18115
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvsetkeys.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(esk.sty) = %{tl_version}

%description -n texlive-esk
The ESK package allows to encapsulate Sketch files in LaTeX sources. This is
very useful for keeping illustrations in sync with the text. It also frees the
user from inventing descriptive names for new files that fit into the confines
of file system conventions. Sketch is a 3D scene description language by Eugene
K. Ressler and can generate TikZ and PSTricks code. ESK behaves in a similar
fashion to EMP (which encapsulates MetaPost files), and was in fact developed
from it.

%package -n texlive-euflag
Summary:        A command to reproduce the flag of the European Union
Version:        svn55265
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(euflag.sty) = %{tl_version}

%description -n texlive-euflag
This LaTeX package implements a command to reproduce the official flag of the
European Union (EU). The flag is reproduced at 1em high based on the current
font size, so it can be scaled arbitrarily by changing the font size.

%package -n texlive-fadingimage
Summary:        Add full width fading pictures at the top or bottom of a page
Version:        svn75447
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(fadingimage.sty) = %{tl_version}

%description -n texlive-fadingimage
This package provides commands for adding full width fading pictures at the top
or bottom of a page. It is based on TikZ with the fadings library. Welcome to
feedback bugs or ideas via email to xiamyphys@gmail.com.

%package -n texlive-fast-diagram
Summary:        Easy generation of FAST diagrams
Version:        svn29264
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xargs.sty)
Provides:       tex(fast-diagram.sty) = %{tl_version}

%description -n texlive-fast-diagram
The package provides simple means of producing FAST diagrams, using TikZ/pgf
tools. FAST diagrams are useful for functional analysis techniques in design
methods.

%package -n texlive-fenetrecas
Summary:        Commands for CAS-like windows (Xcas or Geogebra) in TikZ
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
Provides:       tex(FenetreCas.sty) = %{tl_version}

%description -n texlive-fenetrecas
This package provides some commands (in French) to display, with TikZ, windows
like Xcas or Geogebra : \begin{CalculFormelGeogebra} and \LigneCalculsGeogebra
; \begin{CalculFormelXcas} and \LigneCalculsXcas.

%package -n texlive-figchild
Summary:        Pictures for creating children's activities
Version:        svn75801
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(figchild.sty) = %{tl_version}

%description -n texlive-figchild
This package was created with the aim of facilitating the work of Elementary
School teachers who need to create colorful and attractive activities for their
students. It is a product of the Computational Mathematics discipline offered
at the Federal University of Vicosa -- Campus UFV -- Florestal by professor
Fernando de Souza Bastos. At the time, professor Fernando was a faculty member
at the UFV Florestal campus. Currently, he is a professor in the Department of
Statistics at the UFV main campus in Vicosa. The package makes use of the TikZ
and xcolor packages.

%package -n texlive-figput
Summary:        Create interactive figures in LaTeX
Version:        svn76924
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xsim.sty)
Requires:       tex(zref-abspage.sty)
Requires:       tex(zref-pagelayout.sty)
Requires:       tex(zref-savepos.sty)
Requires:       tex(zref-thepage.sty)
Requires:       tex(zref-user.sty)
Provides:       tex(figput.sty) = %{tl_version}

%description -n texlive-figput
FigPut allows figures to be specified using JavaScript. The resulting document
can be viewed as a static PDF, as usual, or the document can be viewed in a
web-browser, in which case the figures are interactive. A variety of
interactive widgets are included.

%package -n texlive-fitbox
Summary:        Fit graphics on a page
Version:        svn50088
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(fitbox.sty) = %{tl_version}

%description -n texlive-fitbox
The package allows a box (usually an \includegraphics box) to fit on the page.
It scales the box to the maximal allowed size within the user-set limits. If
there is not enough space on the page, the box is moved to the next one.

%package -n texlive-flowchart
Summary:        Shapes for drawing flowcharts, using TikZ
Version:        svn36572
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(makeshape.sty)
Requires:       tex(tikz.sty)
Provides:       tex(flowchart.sty) = %{tl_version}

%description -n texlive-flowchart
The package provides a set of 'traditional' flowchart element shapes; the
documentation shows how to build a flowchart from these elements, using
pgf/TikZ. The package also requires the makeshape package.

%package -n texlive-forest
Summary:        Drawing (linguistic) trees
Version:        svn57398
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-elocalloc
Requires:       texlive-environ
Requires:       texlive-etoolbox
Requires:       texlive-inlinedef
Requires:       texlive-l3packages
Requires:       texlive-pgf
Requires:       texlive-pgfopts
Requires:       tex(dingbat.sty)
Requires:       tex(elocalloc.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(inlinedef.sty)
Requires:       tex(lstdoc.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(forest-compat.sty) = %{tl_version}
Provides:       tex(forest-doc.sty) = %{tl_version}
Provides:       tex(forest-index.sty) = %{tl_version}
Provides:       tex(forest-lib-edges.sty) = %{tl_version}
Provides:       tex(forest-lib-linguistics.sty) = %{tl_version}
Provides:       tex(forest.sty) = %{tl_version}

%description -n texlive-forest
The package provides a PGF/TikZ-based mechanism for drawing linguistic (and
other kinds of) trees. Its main features are: a packing algorithm which can
produce very compact trees; a user-friendly interface consisting of the
familiar bracket encoding of trees plus the key-value interface to
option-setting; many tree-formatting options, with control over option values
of individual nodes and mechanisms for their manipulation; the possibility to
decorate the tree using the full power of PGF/TikZ; and an externalization
mechanism sensitive to code-changes.

%package -n texlive-forest-ext
Summary:        Additional Forest libraries providing bug fixes, extensions and support for tagging
Version:        svn77412
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(forest-lib-ext.ling-debug.sty) = %{tl_version}
Provides:       tex(forest-lib-ext.ling.sty) = %{tl_version}
Provides:       tex(forest-lib-ext.multi-debug.sty) = %{tl_version}
Provides:       tex(forest-lib-ext.multi.sty) = %{tl_version}
Provides:       tex(forest-lib-ext.tagging-debug.sty) = %{tl_version}
Provides:       tex(forest-lib-ext.tagging.sty) = %{tl_version}
Provides:       tex(forest-lib-ext.utils-debug.sty) = %{tl_version}
Provides:       tex(forest-lib-ext.utils.sty) = %{tl_version}

%description -n texlive-forest-ext
forest-ext is a new package offering additional libraries for Forest:
ext.tagging supports tagging forest trees ext.multi provides styles for limited
inclusion of children with multiple parents ext.utils provides some utilities
and miscellaneous styles ext.ling provides some simple extensions for
linguistics, but currently only one is enabled Debugging versions of all
libraries are provided.

%package -n texlive-genealogytree
Summary:        Pedigree and genealogical tree diagrams
Version:        svn66513
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tcolorbox.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xparse.sty)
Provides:       tex(genealogytree.sty) = %{tl_version}
Provides:       tex(gtrcore.contour.code.tex) = %{tl_version}
Provides:       tex(gtrcore.drawing.code.tex) = %{tl_version}
Provides:       tex(gtrcore.node.code.tex) = %{tl_version}
Provides:       tex(gtrcore.options.code.tex) = %{tl_version}
Provides:       tex(gtrcore.parser.code.tex) = %{tl_version}
Provides:       tex(gtrcore.processing.code.tex) = %{tl_version}
Provides:       tex(gtrcore.symbols.code.tex) = %{tl_version}
Provides:       tex(gtrlang.catalan.code.tex) = %{tl_version}
Provides:       tex(gtrlang.chinese.code.tex) = %{tl_version}
Provides:       tex(gtrlang.danish.code.tex) = %{tl_version}
Provides:       tex(gtrlang.dutch.code.tex) = %{tl_version}
Provides:       tex(gtrlang.english.code.tex) = %{tl_version}
Provides:       tex(gtrlang.french.code.tex) = %{tl_version}
Provides:       tex(gtrlang.german.code.tex) = %{tl_version}
Provides:       tex(gtrlang.italian.code.tex) = %{tl_version}
Provides:       tex(gtrlang.portuguese.code.tex) = %{tl_version}
Provides:       tex(gtrlang.spanish.code.tex) = %{tl_version}
Provides:       tex(gtrlang.swedish.code.tex) = %{tl_version}
Provides:       tex(gtrlib.debug.code.tex) = %{tl_version}
Provides:       tex(gtrlib.fanchart.code.tex) = %{tl_version}
Provides:       tex(gtrlib.templates.code.tex) = %{tl_version}

%description -n texlive-genealogytree
Pedigree and genealogical tree diagrams are proven tools to visualize genetic
and relational connections between individuals. The naming ("tree") derives
from historical family diagrams. However, even the smallest family entity
consisting of two parents and several children is hardly a 'mathematical' tree
-- it is a more general graph. The package provides a set of tools to typeset
genealogical trees (i.e., to typeset a set of special graphs for the
description of family-like structures). The package uses an autolayout
algorithm which can be customized, e. g., to prioritize certain paths.

%package -n texlive-gincltex
Summary:        Include TeX files as graphics (.tex support for \includegraphics)
Version:        svn64967
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(svn-prov.sty)
Provides:       tex(gincltex.sty) = %{tl_version}

%description -n texlive-gincltex
The package builds on the standard LaTeX packages graphics and/or graphicx and
allows external LaTeX source files to be included, in the same way as graphic
files, by \includegraphics. In effect, then package adds support for the .tex
extension. Some of the lower level operations like clipping and trimming are
implemented using the adjustbox package which includes native pdfLaTeX support
and uses the pgf package for other output formats.

%package -n texlive-gnuplottex
Summary:        Embed Gnuplot commands in LaTeX documents
Version:        svn54758
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(catchfile.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(moreverb.sty)
Provides:       tex(gnuplottex.sty) = %{tl_version}

%description -n texlive-gnuplottex
This package allows you to include Gnuplot graphs in your LaTeX documents. The
gnuplot code is extracted from the document and written to .gnuplot files.
Then, if shell escape is used, the graph files are automatically processed to
graphics or LaTeX code files which will then be included in the document. If
shell escape isn't used, the user will have to manually convert the files by
running gnuplot on the extracted .gnuplot files.

%package -n texlive-gradientframe
Summary:        Simple gradient frames around objects
Version:        svn21387
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(keyval.sty)
Provides:       tex(gradientframe.sty) = %{tl_version}

%description -n texlive-gradientframe
The package provides a means of drawing graded frames around objects. The
gradients of the frames are drawn using the color package.

%package -n texlive-grafcet
Summary:        Draw Grafcet/SFC with TikZ
Version:        svn22509
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifsym.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(grafcet.sty) = %{tl_version}

%description -n texlive-grafcet
The package provides a library (GRAFCET) that can draw Grafcet Sequential
Function Chart (SFC) diagrams, in accordance with EN 60848, using Pgf/TikZ.
L'objectif de la librairie GRAFCET est de permettre le trace de grafcet selon
la norme EN 60848 a partir de Pgf/TikZ.

%package -n texlive-graph35
Summary:        Draw keys and screen items of several Casio calculators
Version:        svn66772
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsbsy.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(letterspace.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(sansmath.sty)
Requires:       tex(tikz.sty)
Provides:       tex(graph35-keys.sty) = %{tl_version}
Provides:       tex(graph35-pixelart.sty) = %{tl_version}
Provides:       tex(graph35.sty) = %{tl_version}

%description -n texlive-graph35
This package defines commands to draw the Casio Graph 35 / fx-9750GII
calculator (and other models). It can draw the whole calculator, or parts of it
(individual keys, part of the screen, etc.). It was written to typeset
documents instructing students how to use their calculator.

%package -n texlive-graphicxpsd
Summary:        Adobe Photoshop Data format (PSD) support for graphicx package
Version:        svn57341
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(shellesc.sty)
Provides:       tex(graphicxpsd.sty) = %{tl_version}

%description -n texlive-graphicxpsd
This package provides Adobe Photoshop Data format (PSD) support for the
graphicx package with the sips (Darwin/macOS) or convert (ImageMagick) command.

%package -n texlive-graphviz
Summary:        Write graphviz (dot+neato) inline in LaTeX documents
Version:        svn31517
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(psfrag.sty)
Provides:       tex(graphviz.sty) = %{tl_version}

%description -n texlive-graphviz
The package allows inline use of graphviz code, in a LaTeX document.

%package -n texlive-gtrlib-largetrees
Summary:        Library for genealogytree aiming at large trees
Version:        svn49062
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(genealogytree.sty)
Provides:       tex(gtrlib.largetrees.code.tex) = %{tl_version}
Provides:       tex(gtrlib.largetrees.sty) = %{tl_version}

%description -n texlive-gtrlib-largetrees
The main goal of this package is to offer additional database fields and
formats for the genealogytree package, particularly for typesetting large
trees. The package depends on genealogytree and etoolbox.

%package -n texlive-harveyballs
Summary:        Create Harvey Balls using TikZ
Version:        svn32003
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(harveyballs.sty) = %{tl_version}

%description -n texlive-harveyballs
The package provides 5 commands (giving symbols that indicate values from
"none" to "full").

%package -n texlive-here
Summary:        Emulation of obsolete package for "here" floats
Version:        svn16135
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Provides:       tex(here.sty) = %{tl_version}

%description -n texlive-here
Provides the H option for floats in LaTeX to signify that the environment is
not really a float (and should therefore be placed "here" and not float at
all). The package emulates an older package of the same name, which has long
been suppressed by its author. The job is done by nothing more than loading the
float package, which has long provided the option in an acceptable framework.

%package -n texlive-hf-tikz
Summary:        A simple way to highlight formulas and formula parts
Version:        svn34733
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(hf-tikz.sty) = %{tl_version}

%description -n texlive-hf-tikz
The package provides a way to highlight formulas and formula parts in both
documents and presentations, us TikZ.

%package -n texlive-hobby
Summary:        An implementation of Hobby's algorithm for PGF/TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hobby-l3draw.sty) = %{tl_version}
Provides:       tex(hobby.code.tex) = %{tl_version}
Provides:       tex(pgflibraryhobby.code.tex) = %{tl_version}
Provides:       tex(pml3array.sty) = %{tl_version}
Provides:       tex(tikzlibraryhobby.code.tex) = %{tl_version}

%description -n texlive-hobby
This package defines a path generation function for PGF/TikZ which implements
Hobby's algorithm for a path built out of Bezier curves which passes through a
given set of points. The path thus generated may by used as a TikZ 'to path'.
The implementation is in LaTeX3.

%package -n texlive-hvfloat
Summary:        Controlling captions, fullpage and doublepage floats
Version:        svn77209
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(afterpage.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(caption.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(multido.sty)
Requires:       tex(picture.sty)
Requires:       tex(stfloats.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(trimclip.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(zref-savepos.sty)
Provides:       tex(hvfloat-fps.sty) = %{tl_version}
Provides:       tex(hvfloat.sty) = %{tl_version}

%description -n texlive-hvfloat
This package defines a macro to place objects (tables and figures) and their
captions in different positions with different rotating angles within a float.
All objects and captions can be framed. The main command is \hvFloat{float
type}{floating object}{caption}{label}; a simple example is
\hvFloat{figure}{\includegraphics{rose}}{Caption}{fig:0}. Options are provided
to place captions to the right or left, and rotated. Setting nonFloat=true
results in placing the float here.

%package -n texlive-istgame
Summary:        Draw Game Trees with TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(istgame.sty) = %{tl_version}

%description -n texlive-istgame
This LaTeX package provides macros based on TikZ to draw a game tree. The main
idea underlying its core macros is the completion of a whole tree by using a
sequence of simple 'parent-child' tree structures, with no longer nested
relations involved (like the use of 'grandchildren' or 'great-grandchildren').
Using this package you can draw a game tree as easily as drawing a game tree
with pen and paper. This package depends on expl3, TikZ, and xparse. The 'ist'
prefix stands for "it's a simple tree" or "In-Sung's simple tree."

%package -n texlive-kblocks
Summary:        Easily typeset Control Block Diagrams and Signal Flow Graphs
Version:        svn57617
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(circuitikz.sty)
Requires:       tex(tikz.sty)
Provides:       tex(kblocks.sty) = %{tl_version}

%description -n texlive-kblocks
Kblocks defines a number of commands to make drawing control block diagrams
using TikZ/PGF more structured and easier. It reduces the learning curve
forTikZ/PGF and serves as a frontend, by focusing on the block resp. flow
diagrams only.

%package -n texlive-keisennote
Summary:        TikZ-based Japanese-style notebook ruled lines for LaTeX
Version:        svn77255
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(zref-savepos.sty)
Requires:       tex(zref.sty)
Provides:       tex(keisennote.sty) = %{tl_version}

%description -n texlive-keisennote
Typeset Japanese-style ruled notebook lines in LaTeX. It supports full-page
(\notefill) and short (\note) blocks. Spacing, dot size, and color are
adjustable. The package is compatible with multicols.

%package -n texlive-kinematikz
Summary:        Design kinematic chains and mechanisms
Version:        svn61392
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(kinematikz.sty) = %{tl_version}

%description -n texlive-kinematikz
This package provides functionalities to draw kinematic diagrams for mechanisms
using dedicate symbols (some from the ISO standard and others). The intention
is not to represent CAD mechanical drawings of mechanisms and robots, but only
to represent 2D and 3D kinematic chains. The package provides links, joints and
other symbols, mostly in the form of TikZ pic objects. These pics can be placed
in the canvas either by a central point for joints, and start and end points
for some links.

%package -n texlive-knitting
Summary:        Produce knitting charts, in Plain TeX or LaTeX
Version:        svn50782
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(knitting.sty) = %{tl_version}
Provides:       tex(knitting.tex) = %{tl_version}

%description -n texlive-knitting
The package provides symbol fonts and commands to write charted instructions
for cable and lace knitting patterns, using either plain TeX or LaTeX. The
fonts are available both as Metafont source and in Adobe Type 1 format.

%package -n texlive-knittingpattern
Summary:        Create knitting patterns
Version:        svn17205
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-knittingpattern
The class provides a simple, effective method for knitters to produce
high-quality, attractive patterns using LaTeX. It does this by providing
commands to handle as much of the layout of the document as possible, leaving
the author free to concentrate on the pattern.

%package -n texlive-ladder
Summary:        Draw simple ladder diagrams using TikZ
Version:        svn44394
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(ladder.sty) = %{tl_version}

%description -n texlive-ladder
This package permits the creation of simple ladder diagrams within LaTeX
documents. Required packages are tikz, ifthen, and calc.

%package -n texlive-lapdf
Summary:        PDF drawing directly in TeX documents
Version:        svn23806
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Provides:       tex(lapdf.sty) = %{tl_version}

%description -n texlive-lapdf
The package provides the means to use PDF drawing primitives to produce high
quality, colored graphics. It uses Bezier curves (integral and rational) from
degree one to seven, allows TeX typesetting in the graphic, offers most of the
standard math functions, allows plotting normal, parametric and polar
functions. The package has linear, logx, logy, logxy and polar grids with many
specs; it can rotate, clip and do many nice things easily it has two looping
commands for programming and many instructive example files. The package
requires pdfTeX but otherwise only depends on the calc package.

%package -n texlive-latex-make
Summary:        Easy compiling of complex (and simple) LaTeX documents
Version:        svn60874
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ae.sty)
Requires:       tex(aeguill.sty)
Requires:       tex(color.sty)
Requires:       tex(epstopdf.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(thumbpdf.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
Provides:       tex(figlatex.sty) = %{tl_version}
Provides:       tex(pdfswitch.sty) = %{tl_version}
Provides:       tex(texdepends.sty) = %{tl_version}
Provides:       tex(texgraphicx.sty) = %{tl_version}

%description -n texlive-latex-make
This package provides several tools that aim to simplify the compilation of
LaTeX documents: LaTeX.mk: a Makefile snippet to help compiling LaTeX documents
in DVI, PDF, PS, ... format. Dependencies are automatically tracked: one should
be able to compile documents with a one-line Makefile containing 'include
LaTeX.mk'. Complex documents (with multiple bibliographies, indexes,
glossaries, ...) should be correctly managed. figlatex.sty: a LaTeX package to
easily insert xfig figures (with \includegraphics{file.fig}). It can interact
with LaTeX.mk so that the latter automatically invokes transfig if needed. And
various helper tools for LaTeX.mk This package requires GNUmake (>= 3.81).

%package -n texlive-liftarm
Summary:        Geometric constructions with liftarms using TikZ and LaTeX3
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(liftarm.sty) = %{tl_version}

%description -n texlive-liftarm
This package is based on the package TikZ and can be used to draw geometric
constructions with liftarms. There are several options for the appearance of
the liftarms. It provides an environment to connect multiple liftarms using the
Newton-Raphson method and LU decomposition. It also provides a command to
describe a construction and a method to animate a construction with one or more
traces.

%package -n texlive-lpic
Summary:        Put LaTeX material over included graphics
Version:        svn20843
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(rotating.sty)
Provides:       tex(lpic.sty) = %{tl_version}

%description -n texlive-lpic
The package defines a convenient interface to put any LaTeX material on top of
included graphics. The LaTeX material may also be rotated and typeset on top of
a white box overshadowing the graphics. The coordinates of the LaTeX boxes are
given relative to the original, unscaled graphics; when the graphics is
rescaled, the LaTeX annotations stay at their right places (unless you do
something extreme). In a draft mode, the package enables you to draw a
coordinate grid over the picture for easy adjustment of positions of the
annotations.

%package -n texlive-lroundrect
Summary:        LaTeX macros for utilizing the roundrect MetaPost routines
Version:        svn39804
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lroundrect.sty) = %{tl_version}

%description -n texlive-lroundrect
This LaTeX package provides ways to use the extremely configurable rounded
rectangles of the roundrect MetaPost package with LaTeX. It is chiefly useful
for examples, but also has macros for particular types of boxes which are
useful on their own.

%package -n texlive-lua-tikz3dtools
Summary:        Not-so-experimental LuaLaTeX package for 3D illustrations in TikZ
Version:        svn77460
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(lua-tikz3dtools.sty) = %{tl_version}

%description -n texlive-lua-tikz3dtools
This package improves on existing 3D capabilities in TikZ. In particular, the
package enables z-sorting of multiple triangulated parametric objects and uses
elaborate clipping and occlusion logic. The parametric objects are defined
using pgfkeys, and endeavor to enable user customization. All of the 3D math is
handled in Lua, and the results are projected onto the 2D TikZ canvas. The user
is enabled to use linear, affine and projective transformations on their
parametric objects.

%package -n texlive-luamesh
Summary:        Computes and draws 2D Delaunay triangulation
Version:        svn63875
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luamesh.sty) = %{tl_version}

%description -n texlive-luamesh
The package allows to compute and draw 2D Delaunay triangulation. The algorithm
is written with lua, and depending upon the choice of the engine, the drawing
is done by MetaPost (with luamplib) or by TikZ. The Delaunay triangulation
algorithm is the Bowyer and Watson algorithm. Several macros are provided to
draw the global mesh, the set of points, or a particular step of the algorithm.

%package -n texlive-luasseq
Summary:        Drawing spectral sequences in LuaLaTeX
Version:        svn65511
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pifont.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luasseq.sty) = %{tl_version}

%description -n texlive-luasseq
The package is an update of the author's sseq package, for use with LuaLaTeX.
This version uses less memory, and operates faster than the original; it also
offers several enhancements.

%package -n texlive-lucide-icons
Summary:        Use lucide-icons through LaTeX commands
Version:        svn77188
License:        LPPL-1.3c AND ISC
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(xstring.sty)
Provides:       tex(lucide-icons.sty) = %{tl_version}

%description -n texlive-lucide-icons
This package provides commands like twemojis which allow to use Lucide-Icons
through LaTeX commands. The implementation relies on images (PDF from SVG) and
should work on every installation.

%package -n texlive-maker
Summary:        Include Arduino or Processing code in LaTeX documents
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(maker.sty) = %{tl_version}

%description -n texlive-maker
The first version of the package allows to include Arduino or Processing code
using three different forms: writing the code directly in the LaTeX document
writing Arduino or Processing commands in line with the text calling to Arduino
or Processing files All these options support the syntax highlighting of the
official IDE.

%package -n texlive-makeshape
Summary:        Declare new PGF shapes
Version:        svn28973
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(makeshape.sty) = %{tl_version}

%description -n texlive-makeshape
The package simplifies production of custom shapes with correct anchor borders,
in PGF/TikZ; the only requirement is a PGF path describing the anchor border.
The package also provides macros that help with the management of shape
parameters, and the definition of anchor points.

%package -n texlive-maritime
Summary:        International maritime signal flags using TikZ
Version:        svn74037
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(maritime.sty) = %{tl_version}

%description -n texlive-maritime
This package provides LaTeX commands for drawing international maritime signal
flags using TikZ (A-Z, NATO 0-9).

%package -n texlive-mercatormap
Summary:        Spherical Mercator coordinate systems and Web Mercator tile integration
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Provides:       tex(mercatormap.sty) = %{tl_version}
Provides:       tex(mercatorpy.def) = %{tl_version}
Provides:       tex(mercatorsupplier.def) = %{tl_version}

%description -n texlive-mercatormap
This package extends TikZ with tools to create map graphics. The provided
coordinate system relies on the Web Mercator projection used on the Web by
OpenStreetMap and others. The package supports the seamless integration of
graphics from public map tile servers by a Python script. Also, common map
elements like markers, geodetic networks, bar scales, routes, orthodrome
pieces, and more are part of the package.

%package -n texlive-milsymb
Summary:        LaTeX package for TikZ based drawing of military symbols as per NATO APP-6(C)
Version:        svn77463
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(acronym.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(arevmath.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Provides:       tex(milsymb.sty) = %{tl_version}

%description -n texlive-milsymb
The package offers commands to draw military symbols as per NATO APP-6(C)
https://web.archive.org/web/20150921231042/http://armawiki.zumo
rc.de/files/NATO/APP-6(C).pdf . It has a set of commands for drawing all
symbols found in the document up to the control measures, as well as support
for custom non-standard symbols. Control measures are planned to be included in
a future release.

%package -n texlive-miniplot
Summary:        A package for easy figure arrangement
Version:        svn17483
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(miniplot.sty) = %{tl_version}

%description -n texlive-miniplot
MiniPlot is a package to help the LaTeX user typeset EPS figures using an
easy-to-use interface. Figures can be arranged as one-figure-only or as a
collection of figures in columns and rows which can itself contain sub-figures
in columns and rows. Wrapped figures are also supported. This package provides
commands to display a framebox instead of the figure as the graphics package
does already but additionally it writes useful information such as the label
and scaling factor into these boxes.

%package -n texlive-modiagram
Summary:        Drawing molecular orbital diagrams
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(modiagram.sty) = %{tl_version}

%description -n texlive-modiagram
The package provides an environment MOdiagram and some commands, to create
molecular orbital diagrams using TikZ. For example, the MO diagram of
dihydrogen would be written as: \begin{MOdiagram} \atom{left}{ 1s = {0;up} }
\atom{right}{ 1s = {0;up} } \molecule{ 1sMO = {1;pair, } } \end{MOdiagram} The
package also needs the l3kernel and l3packages bundles from the LaTeX 3
experimental distribution.

%package -n texlive-neuralnetwork
Summary:        Graph-drawing for neural networks
Version:        svn31500
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithmicx.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(neuralnetwork.sty) = %{tl_version}

%description -n texlive-neuralnetwork
The package provides facilities for graph-drawing, with facilities designed for
neural network diagrams.

%package -n texlive-nl-interval
Summary:        Represent intervals on the number line
Version:        svn58328
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tkz-fct.sty)
Requires:       tex(xparse.sty)
Provides:       tex(nl-interval.sty) = %{tl_version}

%description -n texlive-nl-interval
This package provides macros to simplify the process of representing intervals
on the number line. It depends on tkz-fct, ifthen, and xparse.

%package -n texlive-nndraw
Summary:        Draw neural networks
Version:        svn59674
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(nndraw.sty) = %{tl_version}

%description -n texlive-nndraw
With this package you can create fully connected neural networks in a simple
and efficient way.

%package -n texlive-numericplots
Summary:        Plot numeric data (including Matlab export) using PSTricks
Version:        svn31729
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xkvview.sty)
Provides:       tex(NumericPlots.sty) = %{tl_version}
Provides:       tex(NumericPlots_TickLabels.tex) = %{tl_version}
Provides:       tex(NumericPlots_labels.tex) = %{tl_version}
Provides:       tex(NumericPlots_legend.tex) = %{tl_version}
Provides:       tex(NumericPlots_macros.tex) = %{tl_version}
Provides:       tex(NumericPlots_styles.tex) = %{tl_version}

%description -n texlive-numericplots
Plotting numeric data is a task which has often to be done for scientific
papers. LaTeX itself provides no facilities for drawing more than the simplest
plots from supplied data. The package will process user input, and uses
PSTricks to plot the results. The package provides Matlab functions to
transform Matlab results to plottable data.

%package -n texlive-open-everyday-symbols
Summary:        A list of "everyday" symbols, to be extended by everybody
Version:        svn75127
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(open-everyday-symbols.sty) = %{tl_version}

%description -n texlive-open-everyday-symbols
This is meant to be a community project: It's a list of symbols/icons from an
"everyday" context. It can literally be everything, and thus does not aim at
mathematical symbols or the like. It's basically an icons portfolio -- tiny at
this stage (basically merely providing the infrastructure for more symbols),
but we hope for contributions from the community. Just create some symbols and
make a pull request.

%package -n texlive-openmoji
Summary:        Use openmoji through LaTeX commands
Version:        svn77186
License:        LPPL-1.3c AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(xstring.sty)
Provides:       tex(openmoji.sty) = %{tl_version}

%description -n texlive-openmoji
This package provides commands like twemojis which allow to use OpenMoji
through LaTeX commands. This relies on images (PDF from SVG), so no fancy
unicode-font stuff is needed and it should work on every installation.

%package -n texlive-optikz
Summary:        Customizable optical components for drawing laser setups and optical systems using TikZ
Version:        svn75922
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(optikz.sty) = %{tl_version}

%description -n texlive-optikz
This package provides a collection of TikZ-based commands for drawing laser
setups and optical systems. It includes components such as lenses, mirrors,
beamsplitters, cameras, spectrometers, detectors and more. Each element is
highly customizable through optional key-value arguments (e.g. angle, width,
thickness, color). Furthermore, rainbow and single color beams can be drawn to
visualize beam size and dispersion in e.g. stretcher-compressor setups.

%package -n texlive-outilsgeomtikz
Summary:        Some geometric tools, with TikZ
Version:        svn75985
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(nicefrac.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(OutilsGeomTikz.sty) = %{tl_version}

%description -n texlive-outilsgeomtikz
This package provides some commands, with French keys, to display geometric
tools using TikZ, for example a pen, a compass, a rule, a square, a protractor,
...

%package -n texlive-papiergurvan
Summary:        Commands to work with Gurvan Paper
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(setspace.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(PapierGurvan.sty) = %{tl_version}

%description -n texlive-papiergurvan
This package provides commands to display Gurvan grids or Gurvan full pages,
and also the possibility to write on lines. The source for the design of the
paper can be found at http://www.sos-ecriture.fr/2014/10/papier-gurvan.html.

%package -n texlive-pb-diagram
Summary:        A commutative diagram package using LAMSTeX or Xy-pic fonts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lamsarrow.sty) = %{tl_version}
Provides:       tex(pb-diagram.sty) = %{tl_version}
Provides:       tex(pb-lams.sty) = %{tl_version}
Provides:       tex(pb-xy.sty) = %{tl_version}

%description -n texlive-pb-diagram
A commutative diagram package using LAMSTeX or Xy-pic fonts

%package -n texlive-pgf
Summary:        Create PostScript and PDF graphics in TeX
Version:        svn76180
License:        LPPL-1.3c AND GPL-2.0-only AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-atveryend
Requires:       texlive-fp
Requires:       texlive-graphics
Requires:       texlive-pdftexcmds
Requires:       texlive-xcolor
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(pgf.revision.tex) = %{tl_version}
Provides:       tex(pgf.sty) = %{tl_version}
Provides:       tex(pgf.tex) = %{tl_version}
Provides:       tex(pgfarrows.sty) = %{tl_version}
Provides:       tex(pgfautomata.sty) = %{tl_version}
Provides:       tex(pgfbaseimage.sty) = %{tl_version}
Provides:       tex(pgfbaseimage.tex) = %{tl_version}
Provides:       tex(pgfbaselayers.sty) = %{tl_version}
Provides:       tex(pgfbaselayers.tex) = %{tl_version}
Provides:       tex(pgfbasematrix.sty) = %{tl_version}
Provides:       tex(pgfbasematrix.tex) = %{tl_version}
Provides:       tex(pgfbasepatterns.sty) = %{tl_version}
Provides:       tex(pgfbasepatterns.tex) = %{tl_version}
Provides:       tex(pgfbaseplot.sty) = %{tl_version}
Provides:       tex(pgfbaseplot.tex) = %{tl_version}
Provides:       tex(pgfbaseshapes.sty) = %{tl_version}
Provides:       tex(pgfbaseshapes.tex) = %{tl_version}
Provides:       tex(pgfbasesnakes.sty) = %{tl_version}
Provides:       tex(pgfbasesnakes.tex) = %{tl_version}
Provides:       tex(pgfcalendar.code.tex) = %{tl_version}
Provides:       tex(pgfcalendar.sty) = %{tl_version}
Provides:       tex(pgfcalendar.tex) = %{tl_version}
Provides:       tex(pgfcomp-version-0-65.sty) = %{tl_version}
Provides:       tex(pgfcomp-version-1-18.sty) = %{tl_version}
Provides:       tex(pgfcore.code.tex) = %{tl_version}
Provides:       tex(pgfcore.sty) = %{tl_version}
Provides:       tex(pgfcore.tex) = %{tl_version}
Provides:       tex(pgfcorearrows.code.tex) = %{tl_version}
Provides:       tex(pgfcoreexternal.code.tex) = %{tl_version}
Provides:       tex(pgfcoregraphicstate.code.tex) = %{tl_version}
Provides:       tex(pgfcoreimage.code.tex) = %{tl_version}
Provides:       tex(pgfcorelayers.code.tex) = %{tl_version}
Provides:       tex(pgfcoreobjects.code.tex) = %{tl_version}
Provides:       tex(pgfcorepathconstruct.code.tex) = %{tl_version}
Provides:       tex(pgfcorepathprocessing.code.tex) = %{tl_version}
Provides:       tex(pgfcorepathusage.code.tex) = %{tl_version}
Provides:       tex(pgfcorepatterns.code.tex) = %{tl_version}
Provides:       tex(pgfcorepoints.code.tex) = %{tl_version}
Provides:       tex(pgfcorequick.code.tex) = %{tl_version}
Provides:       tex(pgfcorerdf.code.tex) = %{tl_version}
Provides:       tex(pgfcorescopes.code.tex) = %{tl_version}
Provides:       tex(pgfcoreshade.code.tex) = %{tl_version}
Provides:       tex(pgfcoretransformations.code.tex) = %{tl_version}
Provides:       tex(pgfcoretransparency.code.tex) = %{tl_version}
Provides:       tex(pgfexternal.tex) = %{tl_version}
Provides:       tex(pgfexternalwithdepth.tex) = %{tl_version}
Provides:       tex(pgffor.code.tex) = %{tl_version}
Provides:       tex(pgffor.sty) = %{tl_version}
Provides:       tex(pgffor.tex) = %{tl_version}
Provides:       tex(pgfheaps.sty) = %{tl_version}
Provides:       tex(pgfint.code.tex) = %{tl_version}
Provides:       tex(pgfkeys.code.tex) = %{tl_version}
Provides:       tex(pgfkeys.sty) = %{tl_version}
Provides:       tex(pgfkeys.tex) = %{tl_version}
Provides:       tex(pgfkeyslibraryfiltered.code.tex) = %{tl_version}
Provides:       tex(pgflibraryarrows.code.tex) = %{tl_version}
Provides:       tex(pgflibraryarrows.meta.code.tex) = %{tl_version}
Provides:       tex(pgflibraryarrows.spaced.code.tex) = %{tl_version}
Provides:       tex(pgflibraryarrows.sty) = %{tl_version}
Provides:       tex(pgflibraryautomata.sty) = %{tl_version}
Provides:       tex(pgflibrarycurvilinear.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydatavisualization.barcharts.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydatavisualization.formats.functions.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydatavisualization.polar.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.footprints.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.fractals.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.markings.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.pathmorphing.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.pathreplacing.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.shapes.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.text.code.tex) = %{tl_version}
Provides:       tex(pgflibraryfadings.code.tex) = %{tl_version}
Provides:       tex(pgflibraryfixedpointarithmetic.code.tex) = %{tl_version}
Provides:       tex(pgflibraryfpu.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.circular.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.examples.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.force.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.layered.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.trees.code.tex) = %{tl_version}
Provides:       tex(pgflibraryintersections.code.tex) = %{tl_version}
Provides:       tex(pgflibrarylindenmayersystems.code.tex) = %{tl_version}
Provides:       tex(pgflibraryluamath.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypatterns.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypatterns.meta.code.tex) = %{tl_version}
Provides:       tex(pgflibraryplothandlers.code.tex) = %{tl_version}
Provides:       tex(pgflibraryplothandlers.sty) = %{tl_version}
Provides:       tex(pgflibraryplotmarks.code.tex) = %{tl_version}
Provides:       tex(pgflibraryplotmarks.sty) = %{tl_version}
Provides:       tex(pgflibraryprofiler.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshadings.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.arrows.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.callouts.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.ee.IEC.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.ee.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.logic.IEC.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.logic.US.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.logic.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.geometric.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.misc.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.multipart.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.sty) = %{tl_version}
Provides:       tex(pgflibraryshapes.symbols.code.tex) = %{tl_version}
Provides:       tex(pgflibrarysnakes.code.tex) = %{tl_version}
Provides:       tex(pgflibrarysnakes.sty) = %{tl_version}
Provides:       tex(pgflibrarysvg.path.code.tex) = %{tl_version}
Provides:       tex(pgflibrarytikzbackgrounds.sty) = %{tl_version}
Provides:       tex(pgflibrarytikztrees.sty) = %{tl_version}
Provides:       tex(pgflibrarytimelines.code.tex) = %{tl_version}
Provides:       tex(pgfmanual-en-macros.tex) = %{tl_version}
Provides:       tex(pgfmanual.code.tex) = %{tl_version}
Provides:       tex(pgfmanual.pdflinks.code.tex) = %{tl_version}
Provides:       tex(pgfmanual.prettyprinter.code.tex) = %{tl_version}
Provides:       tex(pgfmanual.sty) = %{tl_version}
Provides:       tex(pgfmath.code.tex) = %{tl_version}
Provides:       tex(pgfmath.sty) = %{tl_version}
Provides:       tex(pgfmath.tex) = %{tl_version}
Provides:       tex(pgfmathcalc.code.tex) = %{tl_version}
Provides:       tex(pgfmathfloat.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.base.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.basic.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.comparison.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.integerarithmetics.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.misc.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.random.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.round.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.trigonometric.code.tex) = %{tl_version}
Provides:       tex(pgfmathode.code.tex) = %{tl_version}
Provides:       tex(pgfmathparser.code.tex) = %{tl_version}
Provides:       tex(pgfmathutil.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleanimations.code.tex) = %{tl_version}
Provides:       tex(pgfmodulebending.code.tex) = %{tl_version}
Provides:       tex(pgfmoduledatavisualization.code.tex) = %{tl_version}
Provides:       tex(pgfmoduledecorations.code.tex) = %{tl_version}
Provides:       tex(pgfmodulematrix.code.tex) = %{tl_version}
Provides:       tex(pgfmodulenonlineartransformations.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleoo.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleparser.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleplot.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleshapes.code.tex) = %{tl_version}
Provides:       tex(pgfmodulesnakes.code.tex) = %{tl_version}
Provides:       tex(pgfmodulesorting.code.tex) = %{tl_version}
Provides:       tex(pgfnodes.sty) = %{tl_version}
Provides:       tex(pgfpages.sty) = %{tl_version}
Provides:       tex(pgfparser.sty) = %{tl_version}
Provides:       tex(pgfpict2e.sty) = %{tl_version}
Provides:       tex(pgfrcs.code.tex) = %{tl_version}
Provides:       tex(pgfrcs.sty) = %{tl_version}
Provides:       tex(pgfrcs.tex) = %{tl_version}
Provides:       tex(pgfshade.sty) = %{tl_version}
Provides:       tex(pgfsys-common-pdf-via-dvi.def) = %{tl_version}
Provides:       tex(pgfsys-common-pdf.def) = %{tl_version}
Provides:       tex(pgfsys-common-postscript.def) = %{tl_version}
Provides:       tex(pgfsys-common-svg.def) = %{tl_version}
Provides:       tex(pgfsys-dvi.def) = %{tl_version}
Provides:       tex(pgfsys-dvipdfm.def) = %{tl_version}
Provides:       tex(pgfsys-dvipdfmx.def) = %{tl_version}
Provides:       tex(pgfsys-dvips.def) = %{tl_version}
Provides:       tex(pgfsys-dvisvgm.def) = %{tl_version}
Provides:       tex(pgfsys-dvisvgm4ht.def) = %{tl_version}
Provides:       tex(pgfsys-luatex.def) = %{tl_version}
Provides:       tex(pgfsys-pdftex.def) = %{tl_version}
Provides:       tex(pgfsys-tex4ht.def) = %{tl_version}
Provides:       tex(pgfsys-textures.def) = %{tl_version}
Provides:       tex(pgfsys-vtex.def) = %{tl_version}
Provides:       tex(pgfsys-xetex.def) = %{tl_version}
Provides:       tex(pgfsys.code.tex) = %{tl_version}
Provides:       tex(pgfsys.sty) = %{tl_version}
Provides:       tex(pgfsys.tex) = %{tl_version}
Provides:       tex(pgfsysanimations.code.tex) = %{tl_version}
Provides:       tex(pgfsysprotocol.code.tex) = %{tl_version}
Provides:       tex(pgfsyssoftpath.code.tex) = %{tl_version}
Provides:       tex(pgfutil-common-lists.tex) = %{tl_version}
Provides:       tex(pgfutil-common.tex) = %{tl_version}
Provides:       tex(pgfutil-context.def) = %{tl_version}
Provides:       tex(pgfutil-latex.def) = %{tl_version}
Provides:       tex(pgfutil-plain.def) = %{tl_version}
Provides:       tex(t-pgf.tex) = %{tl_version}
Provides:       tex(t-pgfbim.tex) = %{tl_version}
Provides:       tex(t-pgfbla.tex) = %{tl_version}
Provides:       tex(t-pgfbma.tex) = %{tl_version}
Provides:       tex(t-pgfbpl.tex) = %{tl_version}
Provides:       tex(t-pgfbpt.tex) = %{tl_version}
Provides:       tex(t-pgfbsh.tex) = %{tl_version}
Provides:       tex(t-pgfbsn.tex) = %{tl_version}
Provides:       tex(t-pgfcal.tex) = %{tl_version}
Provides:       tex(t-pgfcor.tex) = %{tl_version}
Provides:       tex(t-pgffor.tex) = %{tl_version}
Provides:       tex(t-pgfkey.tex) = %{tl_version}
Provides:       tex(t-pgfmat.tex) = %{tl_version}
Provides:       tex(t-pgfmod.tex) = %{tl_version}
Provides:       tex(t-pgfrcs.tex) = %{tl_version}
Provides:       tex(t-pgfsys.tex) = %{tl_version}
Provides:       tex(t-tikz.tex) = %{tl_version}
Provides:       tex(tikz.code.tex) = %{tl_version}
Provides:       tex(tikz.sty) = %{tl_version}
Provides:       tex(tikz.tex) = %{tl_version}
Provides:       tex(tikzexternal.sty) = %{tl_version}
Provides:       tex(tikzexternalshared.code.tex) = %{tl_version}
Provides:       tex(tikzlibrary3d.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryangles.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryanimations.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryarrows.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryautomata.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarybabel.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarybackgrounds.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarybending.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycalc.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycalendar.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarychains.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.ee.IEC.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.ee.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.CDH.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.IEC.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.US.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.3d.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.barcharts.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.formats.functions.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.polar.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.sparklines.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.footprints.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.fractals.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.markings.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.pathmorphing.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.pathreplacing.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.shapes.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.text.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryer.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryexternal.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfadings.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfit.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfixedpointarithmetic.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfolding.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfpu.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarygraphdrawing.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarygraphdrawing.evolving.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarygraphs.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarygraphs.standard.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryintersections.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarylindenmayersystems.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarymath.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarymatrix.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarymindmap.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypatterns.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypatterns.meta.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryperspective.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypetri.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryplothandlers.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryplotmarks.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypositioning.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryquotes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryrdf.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryscopes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshadings.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshadows.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.arrows.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.callouts.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.gates.logic.IEC.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.gates.logic.US.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.geometric.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.misc.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.multipart.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.symbols.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarysnakes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryspy.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarysvg.path.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarythrough.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytopaths.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrees.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryturtle.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryviews.code.tex) = %{tl_version}
Provides:       tex(xxcolor.sty) = %{tl_version}

%description -n texlive-pgf
PGF is a macro package for creating graphics. It is platform- and
format-independent and works together with the most important TeX backend
drivers, including pdfTeX and dvips. It comes with a user-friendly syntax layer
called TikZ. Its usage is similar to pstricks and the standard picture
environment. PGF works with plain (pdf-)TeX, (pdf-)LaTeX, and ConTeXt. Unlike
pstricks, it can produce either PostScript or PDF output.

%package -n texlive-pgf-blur
Summary:        PGF/TikZ package for "blurred" shadows
Version:        svn54512
License:        LPPL-1.3c AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibraryshadows.blur.code.tex) = %{tl_version}

%description -n texlive-pgf-blur
The package adds blurred/faded/fuzzy shadows to PGF/TikZ pictures. It is
configured as a TikZ/PGF library module. The method is similar to that of the
author's pst-blur package for PSTricks.

%package -n texlive-pgf-interference
Summary:        Drawing interference patterns with PGF/TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pgf-interference.sty) = %{tl_version}

%description -n texlive-pgf-interference
This LaTeX package makes it possible to simulate interference patterns
occurring on a screen if monochromatic light is diffracted at regular
structures of slits. It makes use of the PGF/TikZ graphics package.

%package -n texlive-pgf-periodictable
Summary:        Create custom periodic tables of elements
Version:        svn73886
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(silence.sty)
Requires:       tex(tikz.sty)
Requires:       tex(zhnumber.sty)
Provides:       tex(pgf-PeriodicTable.sty) = %{tl_version}
Provides:       tex(pgfPT.backcolors.keys.tex) = %{tl_version}
Provides:       tex(pgfPT.buildcell.tex) = %{tl_version}
Provides:       tex(pgfPT.coordinates.tex) = %{tl_version}
Provides:       tex(pgfPT.data.tex) = %{tl_version}
Provides:       tex(pgfPT.drawing.keys.tex) = %{tl_version}
Provides:       tex(pgfPT.formatNumbers.tex) = %{tl_version}
Provides:       tex(pgfPT.input.library.tex) = %{tl_version}
Provides:       tex(pgfPT.labels.tex) = %{tl_version}
Provides:       tex(pgfPT.lang.nl.tex) = %{tl_version}
Provides:       tex(pgfPT.lang.undefined.tex) = %{tl_version}
Provides:       tex(pgfPT.lang.zh.tex) = %{tl_version}
Provides:       tex(pgfPT.library.colorschemes.tex) = %{tl_version}
Provides:       tex(pgfPT.names.tex) = %{tl_version}
Provides:       tex(pgfPT.process.language.tex) = %{tl_version}

%description -n texlive-pgf-periodictable
The purpose of this package is to provide the Periodic Table of Elements in a
simple way. It relies on PGF/TikZ to offer a full or partial periodic table
with a variety of options and displaying the desired data for all the 118
elements. It can be done in different languages: English, French, German,
Portuguese (from Portugal and from Brazil), Spanish, Italian and translations
provided by user contributions -- currently in Dutch and Chinese. Compatible
with pdfLaTeX, LuaLaTeX and XeLaTeX engines.

%package -n texlive-pgf-pie
Summary:        Draw pie charts, using PGF
Version:        svn63603
License:        GPL-2.0-only AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-carlisle
Requires:       texlive-latex
Requires:       texlive-pgf
Requires:       tex(tikz.sty)
Provides:       tex(pgf-pie.sty) = %{tl_version}
Provides:       tex(tikzlibrarypie.code.tex) = %{tl_version}

%description -n texlive-pgf-pie
The package provides the means to draw pie (and variant) charts, using
PGF/TikZ.

%package -n texlive-pgf-soroban
Summary:        Create images of the soroban using TikZ/PGF
Version:        svn32269
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pgf-soroban.sty) = %{tl_version}

%description -n texlive-pgf-soroban
The package makes it possible to create pictures of the soroban (Japanese
abacus) using PGF/TikZ

%package -n texlive-pgf-spectra
Summary:        Draw continuous or discrete spectra using PGF/TikZ
Version:        svn75535
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(pgf-spectra.data.LSE.tex) = %{tl_version}
Provides:       tex(pgf-spectra.data.NIST.tex) = %{tl_version}
Provides:       tex(pgf-spectra.input.library.tex) = %{tl_version}
Provides:       tex(pgf-spectra.library.data.tex) = %{tl_version}
Provides:       tex(pgf-spectra.library.pgfplots.tex) = %{tl_version}
Provides:       tex(pgf-spectra.library.rainbow.tex) = %{tl_version}
Provides:       tex(pgf-spectra.library.tempercolor.tex) = %{tl_version}
Provides:       tex(pgf-spectra.sty) = %{tl_version}

%description -n texlive-pgf-spectra
The purpose of this package is to draw the spectrum of elements in a simple
way. It relies on PGF/TikZ to draw the desired spectrum, continuous or
discrete. Data for the spectra of 98 elements and their ions are available
(from the NASA database and from NIST). Lines data ranges from Extreme UV to
Near IR (from 10 to 4000 nanometers). It also allows the user to draw spectra
using their own data. It is possible to redshift the lines of a spectrum, by
directly entering the redshift value or the velocity and the angle to compute
the redshift value. Spectral lines data can be presented in a table or exported
to a file. The package also provides color conversion (correlated color
temperature), shadings for use with TikZ and/or pgfplots and color maps for use
with pgfplots.

%package -n texlive-pgf-umlcd
Summary:        Some LaTeX macros for UML Class Diagrams
Version:        svn63386
License:        GPL-2.0-only AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-latex
Requires:       texlive-pgf
Requires:       tex(tikz.sty)
Provides:       tex(pgf-umlcd.sty) = %{tl_version}
Provides:       tex(tikzlibraryumlcd.code.tex) = %{tl_version}

%description -n texlive-pgf-umlcd
Some LaTeX macros for UML Class Diagrams.

%package -n texlive-pgf-umlsd
Summary:        Draw UML Sequence Diagrams
Version:        svn55342
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-latex
Requires:       texlive-pgf
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pgf-umlsd.sty) = %{tl_version}

%description -n texlive-pgf-umlsd
LaTeX macros to draw UML diagrams using pgf

%package -n texlive-pgfgantt
Summary:        Draw Gantt charts with TikZ
Version:        svn71565
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-pgf
Requires:       tex(pgfcalendar.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pgfgantt.sty) = %{tl_version}

%description -n texlive-pgfgantt
The package provides an environment for drawing Gantt charts that contain
various elements (titles, bars, milestones, groups and links). Several keys
customize the appearance of the chart elements.

%package -n texlive-pgfkeysearch
Summary:        Find keys in a given path 'recursively'
Version:        svn77050
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pgfkeysearch.sty) = %{tl_version}

%description -n texlive-pgfkeysearch
The command \pgfkeysvalueof, unlike \pgfkeys, does not use the .unknown
handler, but raises an error if a key is not defined in the given path. It
neither offers an option to search for the key in other paths. This package
defines commands that allow to retrieve the value of a key, recursively
searching for it in a list of paths.

%package -n texlive-pgfkeyx
Summary:        Extended and more robust version of pgfkeys
Version:        svn26093
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pdftexcmds.sty)
Provides:       tex(pgfkeyx.sty) = %{tl_version}

%description -n texlive-pgfkeyx
The package extends and improves the robustness of the pgfkeys package. In
particular, it can deal with active comma, equality sign, and slash in key
parsing. The difficulty with active characters has long been a problem with the
pgfkeys package. The package also introduces handlers beyond those that pgfkeys
can offer.

%package -n texlive-pgfmolbio
Summary:        Draw graphs typically found in molecular biology texts
Version:        svn71551
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase-modutils.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(pgfmolbio.chromatogram.tex) = %{tl_version}
Provides:       tex(pgfmolbio.convert.tex) = %{tl_version}
Provides:       tex(pgfmolbio.domains.tex) = %{tl_version}
Provides:       tex(pgfmolbio.sty) = %{tl_version}

%description -n texlive-pgfmolbio
The package draws graphs typically found in molecular biology texts. Currently,
the package contains modules for drawing DNA sequencing chromatograms and
protein domain diagrams.

%package -n texlive-pgfmorepages
Summary:        Assemble multiple logical pages onto a physical page
Version:        svn54770
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(pgfcore.sty)
Provides:       tex(pgfmorepages.sty) = %{tl_version}
Provides:       tex(pgfmorepageslayouts.code.tex) = %{tl_version}

%description -n texlive-pgfmorepages
This package replaces and extends the pgfpages sub-package of the PGF system.
It provides the capability to arrange multiple "logical" pages on multiple
"physical" pages, for example as for arranging pages to make booklets.

%package -n texlive-pgfopts
Summary:        LaTeX package options with pgfkeys
Version:        svn56615
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-pgf
Requires:       tex(pgfkeys.sty)
Provides:       tex(pgfopts.sty) = %{tl_version}

%description -n texlive-pgfopts
The pgfkeys package (part of the pgf distribution) is a well-designed way of
defining and using large numbers of keys for key-value syntaxes. However,
pgfkeys itself does not offer means of handling LaTeX class and package
options. This package adds such option handling to pgfkeys, in the same way
that kvoptions adds the same facility to the LaTeX standard keyval package.

%package -n texlive-pgfornament
Summary:        Drawing of Vectorian ornaments with PGF/TikZ
Version:        svn72029
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pgflibraryam.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypgfhan.code.tex) = %{tl_version}
Provides:       tex(pgflibraryvectorian.code.tex) = %{tl_version}
Provides:       tex(pgfornament.sty) = %{tl_version}
Provides:       tex(tikzrput.sty) = %{tl_version}

%description -n texlive-pgfornament
This package allows the drawing of Vectorian ornaments (196) with PGF/TikZ. The
documentation presents the syntax and parameters of the macro "pgfornament".

%package -n texlive-pgfplots
Summary:        Create normal/logarithmic plots in two and three dimensions
Version:        svn76111
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-pgf
Requires:       tex(array.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(listings.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(tikz.sty)
Provides:       tex(bugtracker.sty) = %{tl_version}
Provides:       tex(pgflibraryfillbetween.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.colorbrewer.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.colortol.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-dvipdfmx.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-dvips.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-luatex.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-luatexpatch.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-pdftex.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-xetex.def) = %{tl_version}
Provides:       tex(pgfplots.assert.code.tex) = %{tl_version}
Provides:       tex(pgfplots.assert.sty) = %{tl_version}
Provides:       tex(pgfplots.code.tex) = %{tl_version}
Provides:       tex(pgfplots.errorbars.code.tex) = %{tl_version}
Provides:       tex(pgfplots.markers.code.tex) = %{tl_version}
Provides:       tex(pgfplots.paths.code.tex) = %{tl_version}
Provides:       tex(pgfplots.revision.tex) = %{tl_version}
Provides:       tex(pgfplots.scaling.code.tex) = %{tl_version}
Provides:       tex(pgfplots.sty) = %{tl_version}
Provides:       tex(pgfplots.tex) = %{tl_version}
Provides:       tex(pgfplotsarray.code.tex) = %{tl_version}
Provides:       tex(pgfplotsbinary.code.tex) = %{tl_version}
Provides:       tex(pgfplotsbinary.data.code.tex) = %{tl_version}
Provides:       tex(pgfplotscolor.code.tex) = %{tl_version}
Provides:       tex(pgfplotscolormap.code.tex) = %{tl_version}
Provides:       tex(pgfplotscoordprocessing.code.tex) = %{tl_version}
Provides:       tex(pgfplotscore.code.tex) = %{tl_version}
Provides:       tex(pgfplotsdeque.code.tex) = %{tl_version}
Provides:       tex(pgfplotslibrary.code.tex) = %{tl_version}
Provides:       tex(pgfplotsliststructure.code.tex) = %{tl_version}
Provides:       tex(pgfplotsliststructureext.code.tex) = %{tl_version}
Provides:       tex(pgfplotsmatrix.code.tex) = %{tl_version}
Provides:       tex(pgfplotsmeshplothandler.code.tex) = %{tl_version}
Provides:       tex(pgfplotsmeshplotimage.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_leq.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_loader.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_misc.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcoreexternal.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcoreimage.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcorelayers.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcorescopes.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfkeys.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfkeysfiltered.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryfpu.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryintersections.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryluamath.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryplothandlers.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.pdflinks.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.prettyprinter.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmathfloat.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfutil-common-lists.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_tikzexternal.sty) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_tikzexternalshared.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_tikzlibraryexternal.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_trig_format.code.tex) = %{tl_version}
Provides:       tex(pgfplotsplothandlers.code.tex) = %{tl_version}
Provides:       tex(pgfplotsstackedplots.code.tex) = %{tl_version}
Provides:       tex(pgfplotssysgeneric.code.tex) = %{tl_version}
Provides:       tex(pgfplotstable.code.tex) = %{tl_version}
Provides:       tex(pgfplotstable.coltype.code.tex) = %{tl_version}
Provides:       tex(pgfplotstable.sty) = %{tl_version}
Provides:       tex(pgfplotstable.tex) = %{tl_version}
Provides:       tex(pgfplotstableshared.code.tex) = %{tl_version}
Provides:       tex(pgfplotsticks.code.tex) = %{tl_version}
Provides:       tex(pgfplotsutil.code.tex) = %{tl_version}
Provides:       tex(pgfplotsutil.verb.code.tex) = %{tl_version}
Provides:       tex(pgfregressiontest.sty) = %{tl_version}
Provides:       tex(pgfsys-luatexpatch.def) = %{tl_version}
Provides:       tex(t-pgfplots.tex) = %{tl_version}
Provides:       tex(t-pgfplotstable.tex) = %{tl_version}
Provides:       tex(tikzlibrarycolorbrewer.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycolortol.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydateplot.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.softclip.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfillbetween.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.clickable.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.colormaps.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.contourlua.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.dateplot.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.decorations.softclip.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.external.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.fillbetween.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.groupplots.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.patchplots.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.polar.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.smithchart.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.statistics.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.ternary.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.units.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplotsclickable.code.tex) = %{tl_version}

%description -n texlive-pgfplots
PGFPlots draws high-quality function plots in normal or logarithmic scaling
with a user-friendly interface directly in TeX. The user supplies axis labels,
legend entries and the plot coordinates for one or more plots and PGFPlots
applies axis scaling, computes any logarithms and axis ticks and draws the
plots, supporting line plots, scatter plots, piecewise constant plots, bar
plots, area plots, mesh-- and surface plots and some more. Pgfplots is based on
PGF/TikZ (PGF); it runs equally for LaTeX/TeX/ConTeXt.

%package -n texlive-pgfplotsthemebeamer
Summary:        Use colours from the current beamer theme in pgfplots
Version:        svn71954
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-beamer
Requires:       texlive-pgfopts
Requires:       texlive-pgfplots
Requires:       texlive-tools
Requires:       tex(pgfplots.sty)
Provides:       tex(pgfplotsthemebeamer.sty) = %{tl_version}

%description -n texlive-pgfplotsthemebeamer
A LaTeX package for using colours from the current beamer theme in pgfplots
diagrams.

%package -n texlive-picinpar
Summary:        Insert pictures into paragraphs
Version:        svn76726
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(picinpar.sty) = %{tl_version}

%description -n texlive-picinpar
A legacy package for creating 'windows' in paragraphs, for inserting graphics,
etc. (including "dropped capitals"). Users should note that Pieter van Oostrum
(in a published review of packages of this sort) does not recommend this
package; Picins is recommended instead.

%package -n texlive-pict2e
Summary:        New implementation of picture commands
Version:        svn56504
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(trig.sty)
Provides:       tex(p2e-dvipdfm.def) = %{tl_version}
Provides:       tex(p2e-dvipdfmx.def) = %{tl_version}
Provides:       tex(p2e-dvips.def) = %{tl_version}
Provides:       tex(p2e-luatex.def) = %{tl_version}
Provides:       tex(p2e-pctex32.def) = %{tl_version}
Provides:       tex(p2e-pctexps.def) = %{tl_version}
Provides:       tex(p2e-pdftex.def) = %{tl_version}
Provides:       tex(p2e-textures.def) = %{tl_version}
Provides:       tex(p2e-vtex.def) = %{tl_version}
Provides:       tex(p2e-xetex.def) = %{tl_version}
Provides:       tex(pict2e.sty) = %{tl_version}

%description -n texlive-pict2e
This package was described in the 2nd edition of 'LaTeX: A Document Preparation
System', but the LaTeX project team declined to produce the package. For a long
time, LaTeX included a 'pict2e package' that merely produced an apologetic
error message. The new package extends the existing LaTeX picture environment,
using the familiar technique (cf. the graphics and color packages) of driver
files (at present, drivers for dvips, pdfTeX, LuaTeX, XeTeX, VTeX, dvipdfm, and
dvipdfmx are available). The package documentation has a fair number of
examples of use, showing where things are improved by comparison with the LaTeX
picture environment.

%package -n texlive-pictex
Summary:        Picture drawing macros for TeX and LaTeX
Version:        svn59551
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(errorbars.tex) = %{tl_version}
Provides:       tex(latexpicobjs.tex) = %{tl_version}
Provides:       tex(piccorr.sty) = %{tl_version}
Provides:       tex(picmore.tex) = %{tl_version}
Provides:       tex(pictex.sty) = %{tl_version}
Provides:       tex(pictex.tex) = %{tl_version}
Provides:       tex(pictexwd.sty) = %{tl_version}
Provides:       tex(pictexwd.tex) = %{tl_version}
Provides:       tex(pointers.tex) = %{tl_version}
Provides:       tex(postpictex.tex) = %{tl_version}
Provides:       tex(prepictex.tex) = %{tl_version}
Provides:       tex(texpictex.tex) = %{tl_version}
Provides:       tex(tree.sty) = %{tl_version}

%description -n texlive-pictex
PicTeX is an early and very comprehensive drawing package that mostly draws by
placing myriads of small dots to make up pictures. It has a tendency to run out
of space; packages m-pictex and pictexwd deal with the problems in different
ways.

%package -n texlive-pictex2
Summary:        Adds relative coordinates and improves the \plot command
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pictex.sty)
Provides:       tex(pictex2.sty) = %{tl_version}

%description -n texlive-pictex2
Adds two user commands to standard PiCTeX. One command uses relative
coordinates, thus eliminating the need to calculate the coordinate of every
point manually as in standard PiCTeX. The other command modifies \plot to use a
rule instead of dots if the line segment is horizontal or vertical.

%package -n texlive-pictochrono
Summary:        Insert "chronometer pictograms" with a duration
Version:        svn75622
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(pictochrono.sty) = %{tl_version}

%description -n texlive-pictochrono
Small package to insert, inline with automatic height and vertical offset,
small "pictogram chronometers" to indicate a duration.

%package -n texlive-pinlabel
Summary:        A TeX labelling package
Version:        svn24769
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(pinlabel.sty) = %{tl_version}

%description -n texlive-pinlabel
Pinlabel is a labelling package for attaching perfectly formatted TeX labels to
figures and diagrams in both eps and pdf formats. It is suitable both for
labelling a new diagram and for relabelling an existing diagram. The package
uses coordinates derived from GhostView (or gv) and labels are placed with
automatic and consistent spacing relative to the object labelled.

%package -n texlive-pixelart
Summary:        Draw pixel-art pictures
Version:        svn66012
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(iftex.sty)
Requires:       tex(luacode.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pixelart.sty) = %{tl_version}
Provides:       tex(pixelart0.sty) = %{tl_version}

%description -n texlive-pixelart
A LuaLaTeX package to draw pixel-art pictures using TikZ.

%package -n texlive-pixelarttikz
Summary:        Work with PixelArts, with TikZ
Version:        svn77054
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(csvsimple.sty)
Requires:       tex(datatool.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(multicol.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xstring.sty)
Provides:       tex(PixelArtTikz.sty) = %{tl_version}
Provides:       tex(pixelarttikz-l3.sty) = %{tl_version}

%description -n texlive-pixelarttikz
The package defines commands and an environment for displaying pixel arts.

%package -n texlive-pmgraph
Summary:        "Poor man's" graphics
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pmgraph.sty) = %{tl_version}

%description -n texlive-pmgraph
A set of extensions to LaTeX picture environment, including a wider range of
vectors, and a lot more box frame styles.

%package -n texlive-polyhedra
Summary:        A TikZ package for drawing polyhedra
Version:        svn68770
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor-solarized.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(polyhedra.sty) = %{tl_version}

%description -n texlive-polyhedra
This package provides macros for creating polyhedral objects in 2D and 3D. It
requires TikZ and tikz-3dplot. The macros provided can be used for drawing
vertices, edges, rays, polygons and cones.

%package -n texlive-polyomino
Summary:        Polyominoes using TikZ and LaTeX3
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(polyomino.sty) = %{tl_version}

%description -n texlive-polyomino
This package is based on the package TikZ and can be used to draw polyominoes.
It is possible to define custom styles, pics and grids.

%package -n texlive-postage
Summary:        Stamp letters with >>Deutsche Post<<'s service >>Internetmarke<<
Version:        svn55920
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(tikz.sty)
Provides:       tex(postage.sty) = %{tl_version}

%description -n texlive-postage
The postage package is used for franking letters with >>Deutsche Post<<'s
online postage service >>Internetmarke<<. Note that in order to print valid
stamps you must point to a valid PDF of >>Deutsche Post<<'s >>Ausdruck
4-spaltig (DIN A4)<<.

%package -n texlive-postit
Summary:        A LaTeX package for displaying Post-it notes
Version:        svn75925
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xstring.sty)
Provides:       tex(postit.sty) = %{tl_version}

%description -n texlive-postit
This package provides some commands and options for creating Post-it-like boxes
with tcolorbox: an environment PostIt with customizations; a command
\MiniPostIt to display a simple Post-It.

%package -n texlive-prerex
Summary:        Interactive editor and macro support for prerequisite charts
Version:        svn54512
License:        GPL-2.0-only AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pgf.sty)
Requires:       tex(relsize.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(prerex.sty) = %{tl_version}

%description -n texlive-prerex
This package consists of prerex.sty, a LaTeX package for producing charts of
course nodes linked by arrows representing pre- and co-requisites, and prerex,
an interactive program for creating and editing chart descriptions. The
implementation of prerex.sty uses PGF, so that it may be used equally happily
with LaTeX or pdfLaTeX; prerex itself is written in C. The package includes
source code for a previewer application, a lightweight Qt-4 and poppler-based
prerex-enabled PDF viewer.

%package -n texlive-prisma-flow-diagram
Summary:        An abstraction for creating PRISMA 2009 flow diagrams with TikZ
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Provides:       tex(prisma-flow-diagram.sty) = %{tl_version}

%description -n texlive-prisma-flow-diagram
This package provides an abstraction for creating PRISMA 2009 flow diagrams in
LaTeX. It simplifies the process of building these diagrams by providing
intuitive commands while maintaining full compatibility with TikZ.

%package -n texlive-productbox
Summary:        Typeset a three-dimensional product box
Version:        svn20886
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(tikz.sty)
Provides:       tex(productbox.sty) = %{tl_version}

%description -n texlive-productbox
The package enables typesetting of a three-dimensional product box. This
product box can be rendered as it is standing on a surface and some light is
shed onto it. Alternatively it can be typeset as a wireframe to be cut out and
glued together. This will lead to a physical product box. The package requires
pgf and TikZ.

%package -n texlive-ptolemaicastronomy
Summary:        Diagrams of sphere models for variably strict conditionals (Lewis counterfactuals)
Version:        svn50810
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(ptolemaicastronomy.sty) = %{tl_version}

%description -n texlive-ptolemaicastronomy
David K. Lewis (Counterfactuals, Blackwell 1973) introduced a sphere semantics
for counterfactual conditionals. He jokingly referred to the diagrams depicting
such sphere models as Ptolemaic astronomy, hence the name of this package. The
macros provided in this package aid in the construction of sphere model
diagrams in the style of Lewis. The macros all make use of TikZ.

%package -n texlive-puyotikz
Summary:        Quickly typeset board states of Puyo Puyo games
Version:        svn57254
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(pythontex.sty)
Requires:       tex(tikz.sty)
Provides:       tex(puyotikz.sty) = %{tl_version}

%description -n texlive-puyotikz
This LaTeX package permits to quickly typeset board states of Puyo Puyo games.
It supports large and small boards with arbitrary shape, hidden rows, current
and next puyos, labels and move planning markers. The package requires Python3
in support of scripts driven by PythonTeX.

%package -n texlive-pxpgfmark
Summary:        E-pTeX driver for PGF inter-picture connections
Version:        svn30212
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pxpgfmark.sty) = %{tl_version}

%description -n texlive-pxpgfmark
The distributed drivers do not support the PGF feature of "inter-picture
connections" under e-pTeX and dvipdfmx. The package uses existing features of
dvipdfmx to fix this problem

%package -n texlive-pxpic
Summary:        Draw pixel pictures
Version:        svn67955
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(expkv.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(pxpic.sty) = %{tl_version}

%description -n texlive-pxpic
With pxpic you draw pictures pixel by pixel. It was inspired by a lovely post
by Paulo Cereda, among other things (most notably a beautiful duck) showcasing
the use of characters from the Mario video games by Nintendo in LaTeX.

%package -n texlive-qcircuit
Summary:        Macros to generate quantum ciruits
Version:        svn48400
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifpdf.sty)
Requires:       tex(xy.sty)
Provides:       tex(qcircuit.sty) = %{tl_version}

%description -n texlive-qcircuit
The package supports those within the quantum information community who typeset
quantum circuits, using xy-pic package, offering macros designed to help users
generate circuits.

%package -n texlive-qrcode
Summary:        Generate QR codes in LaTeX
Version:        svn36065
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(qrcode.sty) = %{tl_version}

%description -n texlive-qrcode
The package generates QR (Quick Response) codes in LaTeX, without the need for
PSTricks or any other graphical package.

%package -n texlive-qrcodetikz
Summary:        Prettier QR codes
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(qrcode.sty)
Requires:       tex(tikz.sty)
Provides:       tex(qrcodetikz.sty) = %{tl_version}

%description -n texlive-qrcodetikz
This package improves the display of QR codes provided by qrcode. The Quick
Response (QR) codes provided by package qrcode show white borders on each
square (from little to very prominent, depending on the pdf viewer). This is
because the QR code is printed square by square, not the connected regions of
squares as such, and pdf screen viewers show these undesired borders. This
package overwrites the qrcode printing functions to fill connected regions of
the QR code using TikZ, allowing prettier qrcodes on screen visualization, with
possibility of customization.

%package -n texlive-randbild
Summary:        Marginal pictures
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-plot.sty)
Provides:       tex(randbild.sty) = %{tl_version}

%description -n texlive-randbild
Provides environments randbild to draw small marginal plots (using the packages
pstricks and pst-plot), and randbildbasis (the same, only without the
automatically drawn coordinate system).

%package -n texlive-randomwalk
Summary:        Random walks using TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfcore.sty)
Requires:       tex(xparse.sty)
Provides:       tex(randomwalk.sty) = %{tl_version}

%description -n texlive-randomwalk
The randomwalk package provides a user command, \RandomWalk, to draw random
walks with a given number of steps. Lengths and angles of the steps can be
customized in various ways. The package uses lcg for its 'random' numbers and
PGF/TikZ for its graphical output.

%package -n texlive-realhats
Summary:        Put real hats on symbols instead of ^
Version:        svn66924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lcg.sty)
Requires:       tex(stackengine.sty)
Provides:       tex(realhats.sty) = %{tl_version}

%description -n texlive-realhats
This LaTeX package makes \hat put real hats on symbols. The package depends on
amsmath, calc, graphicx, ifthen, lcg, and stackengine.

%package -n texlive-reotex
Summary:        Draw Reo Channels and Circuits
Version:        svn34924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(reotex.sty) = %{tl_version}

%description -n texlive-reotex
The package defines macros and other utilities to design Reo Circuits. The
package requires PGF/TikZ support.

%package -n texlive-robotarm
Summary:        TikZ powered LaTeX package to draw parameterized 2D robot arms
Version:        svn63116
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(robotarm.sty) = %{tl_version}

%description -n texlive-robotarm
This LaTeX package uses TikZ to draw parameterized 2D robot arms, for example
to be used in educational material.

%package -n texlive-rviewport
Summary:        Relative Viewport for Graphics Inclusion
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(rviewport.sty) = %{tl_version}

%description -n texlive-rviewport
Package graphicx provides a useful keyword viewport which allows to show just a
part of an image. However, one needs to put there the actual coordinates of the
viewport window. Sometimes it is useful to have relative coordinates as
fractions of natural size. For example, one may want to print a large image on
a spread, putting a half on a verso page, and another half on the next recto
page. For this one would need a viewport occupying exactly one half of the
file's bounding box, whatever the actual width of the image may be. This
package adds a new keyword rviewport to the graphicx package specifying
Relative Viewport for graphics inclusion: a window defined by the given
fractions of the natural width and height of the image.

%package -n texlive-sa-tikz
Summary:        TikZ library to draw switching architectures
Version:        svn32815
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(sa-tikz.sty) = %{tl_version}
Provides:       tex(tikzlibraryswitching-architectures.code.tex) = %{tl_version}

%description -n texlive-sa-tikz
The package provides a library that offers an easy way to draw switching
architectures and to customize their aspect.

%package -n texlive-sacsymb
Summary:        "Sacred Symbols" prepared with TikZ
Version:        svn65768
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(sacsymb.sty) = %{tl_version}

%description -n texlive-sacsymb
The author tells us: This is "a package with symbols prepared with TikZ. These
symbols are the variables used in the space of the collapse of the wave
function of a quantum field associated with the micro-tubule while exploring an
Orchestrated, objective reduction (Orch OR) theory of consciousness as applied
to the three brains model of psychological experience."

%package -n texlive-schemabloc
Summary:        Draw block diagrams, using TikZ
Version:        svn68445
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(schemabloc.sty) = %{tl_version}

%description -n texlive-schemabloc
The package provides a set of macros for constructing block diagrams, using
TikZ. (The blox package is an "English translation" of this package.)

%package -n texlive-scratch
Summary:        Draw programs like "scratch"
Version:        svn66655
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(scratch.sty) = %{tl_version}

%description -n texlive-scratch
This package is now obsolete. From now on, scratch at scratch.mit.edu is now
version3 with a new design. Please, use the "scratch3" package to draw blocks
with the new design. This package permits to draw program charts in the style
of the scatch project (scratch.mit.edu). It depends on the other LaTeX packages
TikZ and simplekv.

%package -n texlive-scratch3
Summary:        Draw programs like "scratch"
Version:        svn61921
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(scratch3.sty) = %{tl_version}

%description -n texlive-scratch3
This package permits to draw program charts in the style of the scatch project
(scratch.mit.edu). It depends on the other LaTeX packages TikZ and simplekv.

%package -n texlive-scsnowman
Summary:        Snowman variants using TikZ
Version:        svn66115
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(pxeveryshi.sty)
Requires:       tex(tikz.sty)
Provides:       tex(scsnowman-normal.def) = %{tl_version}
Provides:       tex(scsnowman.sty) = %{tl_version}
Provides:       tex(sctkzsym-base.sty) = %{tl_version}

%description -n texlive-scsnowman
This LaTeX package provides a command \scsnowman which can display many
variants of "snowman" ("yukidaruma" in Japanese). TikZ is required for drawing
these snowmen.

%package -n texlive-setdeck
Summary:        Typeset cards for Set
Version:        svn40613
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(setdeck.sty) = %{tl_version}

%description -n texlive-setdeck
The package will typeset cards for use in a game of Set.

%package -n texlive-signchart
Summary:        Create beautifully typeset sign charts
Version:        svn39707
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(signchart.sty) = %{tl_version}

%description -n texlive-signchart
The package allows users to easily typeset beautiful looking sign charts
directly into their (La)TeX document.

%package -n texlive-simplenodes
Summary:        Simple nodes in four colors written in TikZ for LaTeX
Version:        svn62888
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Provides:       tex(simplenodes.sty) = %{tl_version}

%description -n texlive-simplenodes
This is a LaTeX macro package for generating simple node-based flow graphs or
diagrams built upon the TikZ package. The package provides two basic commands,
one to generate a node and one to create links between nodes. The positioning
of the nodes is not handled by the package itself but is preferably done in a
tabular environment. In total, four simple node types are defined, loosely
based on the nomenclature and color patterns of the popular Java script
Bootstrap.

%package -n texlive-simpleoptics
Summary:        Drawing lenses and mirrors for optical diagrams
Version:        svn62977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(simpleoptics.sty) = %{tl_version}

%description -n texlive-simpleoptics
This package provides some of macros for drawing simple lenses and mirrors for
use in optical diagrams.

%package -n texlive-smartdiagram
Summary:        Generate diagrams from lists
Version:        svn42781
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(smartdiagram.sty) = %{tl_version}
Provides:       tex(smartdiagramlibraryadditions.code.tex) = %{tl_version}
Provides:       tex(smartdiagramlibrarycore.commands.code.tex) = %{tl_version}
Provides:       tex(smartdiagramlibrarycore.definitions.code.tex) = %{tl_version}
Provides:       tex(smartdiagramlibrarycore.styles.code.tex) = %{tl_version}

%description -n texlive-smartdiagram
The package will create 'smart' diagrams from lists of items, for simple
documents and for presentations.

%package -n texlive-spath3
Summary:        Manipulate "soft paths" in PGF
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgf.sty)
Requires:       tex(xparse.sty)
Provides:       tex(spath3.sty) = %{tl_version}
Provides:       tex(tikzlibrarycalligraphy.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryknots.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryspath3.code.tex) = %{tl_version}

%description -n texlive-spath3
The spath3 library provides methods for manipulating the "soft paths" of
TikZ/PGF. Packaged with it are two TikZ libraries that make use of the methods
provided. These are libraries for drawing calligraphic paths and for drawing
knot diagrams.

%package -n texlive-spectralsequences
Summary:        Print spectral sequence diagrams using PGF/TikZ
Version:        svn65667
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(pdfcomment.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xparse.sty)
Provides:       tex(spectralsequences.sty) = %{tl_version}
Provides:       tex(sseqcheckdefinitions.code.tex) = %{tl_version}
Provides:       tex(sseqdrawing.code.tex) = %{tl_version}
Provides:       tex(sseqforeach.code.tex) = %{tl_version}
Provides:       tex(sseqkeys.code.tex) = %{tl_version}
Provides:       tex(sseqloadstore.code.tex) = %{tl_version}
Provides:       tex(sseqmacromakers.code.tex) = %{tl_version}
Provides:       tex(sseqmain.code.tex) = %{tl_version}
Provides:       tex(sseqmessages.code.tex) = %{tl_version}
Provides:       tex(sseqparsers.code.tex) = %{tl_version}

%description -n texlive-spectralsequences
The package is a specialized tool built on top of PGF/TikZ for drawing spectral
sequences. It provides a powerful, concise syntax for specifying the data of a
spectral sequence, and then allows the user to print various pages of spectral
sequences, automatically choosing which subset of the classes, differentials,
and structure lines to display on each page. It also handles most of the
details of the layout. At the same time, it is extremely flexible.
spectralsequences is closely integrated with TikZ to ensure that users can take
advantage of as much as possible of its expressive power. It is possible to
turn off most of the automated layout features and draw replacements using TikZ
commands. The package also provides a carefully designed error reporting system
intended to ensure that it is as clear as possible what is going wrong.

%package -n texlive-strands
Summary:        Draw objects constructed from strands
Version:        svn59906
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(forarray.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(strands.sty) = %{tl_version}

%description -n texlive-strands
This package permits to draw objects constructed from strands, like set
partitions, permutations, braids, etc. It depends on forarray, ifthen, TikZ,
xfp, xstring, and xkeyval.

%package -n texlive-sunpath
Summary:        Draw sun path charts
Version:        svn72604
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(sunpath.sty) = %{tl_version}

%description -n texlive-sunpath
This package can help to draw sun path charts using a polar coordinate system.

%package -n texlive-swimgraf
Summary:        Graphical/textual representations of swimming performances
Version:        svn25446
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstcol.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(swimgraf.sty) = %{tl_version}

%description -n texlive-swimgraf
The package provides two macros that produce representations of a swimmer's
performances. The user records data in a text file and specifies as arguments
of the macros the date range of interest. The macros extract the relevant
information from the file and process it: \swimgraph produces a graph of the
times in a single swimming event (specified as an argument), plotting long
course and short course times in separate lines. Records and qualifying times,
stored in text files, may optionally be included on the graph. \swimtext
produces a written record of the times in all events. Files of current world
and Canadian records are included. The package requires the PSTricks and keyval
packages. For attractive output it also requires a colour output device.

%package -n texlive-syntaxdi
Summary:        Create "railroad" syntax diagrams
Version:        svn56685
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(syntaxdi.sty) = %{tl_version}

%description -n texlive-syntaxdi
This package provides TikZ styles for creating special syntax diagrams known as
"railroad" diagrams. The package was originally distributed as part of the
schule bundle.

%package -n texlive-table-fct
Summary:        Draw a variations table of functions and a convexity table of its graph
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(table-fct.sty) = %{tl_version}

%description -n texlive-table-fct
Draw a variations table of functions and a convexity table of its graph This
version offers two environments, to draw a variations table of a function and a
convexity table of its graph.

%package -n texlive-texdraw
Summary:        Graphical macros, using embedded PostScript
Version:        svn64477
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(blockdiagram.tex) = %{tl_version}
Provides:       tex(texdraw.sty) = %{tl_version}
Provides:       tex(texdraw.tex) = %{tl_version}
Provides:       tex(txdps.tex) = %{tl_version}
Provides:       tex(txdtools.tex) = %{tl_version}

%description -n texlive-texdraw
TeXdraw is a set of macro definitions for TeX, which allow the user to produce
PostScript drawings from within TeX and LaTeX. TeXdraw has been designed to be
extensible. Drawing 'segments' are relocatable, self-contained units. Using a
combination of TeX's grouping mechanism and the gsave/grestore mechanism in
PostScript, drawing segments allow for local changes to the scaling and line
parameters. Using TeX's macro definition capability, new drawing commands can
be constructed from drawing segments.

%package -n texlive-ticollege
Summary:        Graphical representation of keys on a standard scientific calculator
Version:        svn36306
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multido.sty)
Requires:       tex(multirow.sty)
Requires:       tex(newtxtt.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(ticollege.sty) = %{tl_version}

%description -n texlive-ticollege
This package provides commands to draw scientific calculator keys with the help
of TikZ. It also provides commands to draw the content of screens and of menu
items.

%package -n texlive-tikz-3dplot
Summary:        Coordinate transformation styles for 3d plotting in TikZ
Version:        svn25087
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(pgf.sty)
Provides:       tex(tikz-3dplot.sty) = %{tl_version}

%description -n texlive-tikz-3dplot
The package provides straightforward ways to define three-dimensional
coordinate frames through which to plot in TikZ. The user can specify the
orientation of the main coordinate frame, and use standard TikZ commands and
coordinates to render their tikzfigure. A secondary coordinate frame is
provided to allow rotations and translations with respect to the main
coordinate frame. In addition, the package can also handle plotting
user-specified functions in spherical polar coordinates, where both the radius
and fill color can be expressed as parametric functions of polar angles.

%package -n texlive-tikz-among-us
Summary:        Create some AmongUs characters in TikZ environments
Version:        svn60880
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(eso-pic.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Provides:       tex(tikz-among-us-fancyhdr.sty) = %{tl_version}
Provides:       tex(tikz-among-us-watermark-eso-pic.sty) = %{tl_version}
Provides:       tex(tikz-among-us.sty) = %{tl_version}

%description -n texlive-tikz-among-us
This package recreates some AmongUs characters in TikZ environments. Some
interesting uses alongside other packages are also supported.

%package -n texlive-tikz-bagua
Summary:        Draw Bagua symbols in Yijing
Version:        svn64103
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bitset.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikz-bagua.sty) = %{tl_version}

%description -n texlive-tikz-bagua
This package provides commands for drawing symbols in Yijing (I Ching) or
Zhouyi using TikZ. There is no need for extra special fonts for showing these
symbols. The package relies on TikZ, bitset, xintexpr, xparse, and xstring.

%package -n texlive-tikz-bayesnet
Summary:        Draw Bayesian networks, graphical models and directed factor graphs
Version:        svn38295
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarybayesnet.code.tex) = %{tl_version}

%description -n texlive-tikz-bayesnet
The package provides a library supporting the display of Bayesian networks,
graphical models and (directed) factor graphs in LaTeX.

%package -n texlive-tikz-bbox
Summary:        Precise determination of bounding boxes in TikZ
Version:        svn57444
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pgflibrarybbox.code.tex) = %{tl_version}

%description -n texlive-tikz-bbox
The built-in determination of the bounding box in TikZ is not entirely
accurate. This is because, for Bezier curves, it is the smallest box that
contains all control points, which is in general larger than the box that just
contains the curve. This library determines the exact bounding box of the
curve.

%package -n texlive-tikz-bpmn
Summary:        A TikZ library for creating BPMN models
Version:        svn73368
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarybpmn.code.tex) = %{tl_version}

%description -n texlive-tikz-bpmn
This package provides primitives for drawing Business Process Modelling and
Notation (BPMN) models. It includes tasks, subprocesses, events, task markers
and gateways. The symbols aim to follow the BPMN standard as closely as
possible. Please refer to the documentation for further information.

%package -n texlive-tikz-cd
Summary:        Create commutative diagrams with TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(tikz-cd.sty) = %{tl_version}
Provides:       tex(tikzlibrarycd.code.tex) = %{tl_version}

%description -n texlive-tikz-cd
The general-purpose drawing package TikZ can be used to typeset commutative
diagrams and other kinds of mathematical pictures, generating high-quality
results. The purpose of this package is to make the process of creation of such
diagrams easier by providing a convenient set of macros and reasonable default
settings. This package also includes an arrow tip library that match closely
the arrows present in the Computer Modern typeface.

%package -n texlive-tikz-cookingsymbols
Summary:        Draw cooking symbols
Version:        svn75636
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-cookingsymbols.sty) = %{tl_version}

%description -n texlive-tikz-cookingsymbols
The package uses TikZ for drawing cooking symbols like top heat, airfryer and
so on. The commands are provided in English and German. The size of the symbol
is based on the font size and grabbed with \settoheight and \settodepth.

%package -n texlive-tikz-decofonts
Summary:        Simple decoration fonts, made with TikZ, for short texts
Version:        svn77388
License:        LPPL-1.3c AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikz-decofonts.sty) = %{tl_version}

%description -n texlive-tikz-decofonts
Some simple "decoration" fonts made with TikZ, for short texts: paint brush;
ink brush; pixelart brush; bicolor texts; 'surround' or 'underline' effect;
block of letters texts.

%package -n texlive-tikz-dependency
Summary:        A library for drawing dependency graphs
Version:        svn54512
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pgfmanual.code.tex) = %{tl_version}
Provides:       tex(pgfmanual.pdflinks.code.tex) = %{tl_version}
Provides:       tex(pgfmanual.prettyprinter.code.tex) = %{tl_version}
Provides:       tex(tikz-dependency.sty) = %{tl_version}

%description -n texlive-tikz-dependency
The package provides a library that draws together existing TikZ facilities to
make a comfortable environment for drawing dependency graphs. Basic facilities
of the package include a lot of styling facilities, to let you personalize the
look and feel of the graphs.

%package -n texlive-tikz-dimline
Summary:        Technical dimension lines using PGF/TikZ
Version:        svn35805
License:        WTFPL
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-dimline.sty) = %{tl_version}

%description -n texlive-tikz-dimline
tikz-dimline helps drawing technical dimension lines in TikZ picture
environments. Its usage is similar to some contributions posted on
stackexchange.

%package -n texlive-tikz-ext
Summary:        A collection of libraries for PGF/TikZ
Version:        svn75014
License:        GFDL-1.3-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfcalendar.sty)
Requires:       tex(pgffor.sty)
Provides:       tex(pgfcalendar-ext.code.tex) = %{tl_version}
Provides:       tex(pgfcalendar-ext.sty) = %{tl_version}
Provides:       tex(pgfcalendar-ext.tex) = %{tl_version}
Provides:       tex(pgffor-ext.code.tex) = %{tl_version}
Provides:       tex(pgffor-ext.sty) = %{tl_version}
Provides:       tex(pgffor-ext.tex) = %{tl_version}
Provides:       tex(pgfkeyslibraryext.pgfkeys-plus.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.arrows.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.shapes.circlearrow.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.shapes.circlecrosssplit.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.shapes.heatmark.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.shapes.rectangleroundedcorners.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.shapes.superellipse.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.shapes.uncenteredrectangle.code.tex) = %{tl_version}
Provides:       tex(pgflibraryext.transformations.mirror.code.tex) = %{tl_version}
Provides:       tex(tikzext-util.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.arrows-plus.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.beamer.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.calendar-plus.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.layers.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.misc.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.node-families.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.node-families.shapes.geometric.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.nodes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.paths.arcto.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.paths.ortho.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.paths.timer.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.patterns.images.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.positioning-plus.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.scalepicture.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.shapes.uncenteredrectangle.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.topaths.arcthrough.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.topaths.autobend.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryext.transformations.mirror.code.tex) = %{tl_version}

%description -n texlive-tikz-ext
This is a collection of PGF and TikZ libraries which were developed in response
to questions on tex.stackexchange.com or texwelt.de. These libraries can be
loaded by either \usepgflibrary or \usetikzlibrary.

%package -n texlive-tikz-feynhand
Summary:        Feynman diagrams with TikZ
Version:        svn76924
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-feynhand.sty) = %{tl_version}
Provides:       tex(tikzfeynhand.keys.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfeynhand.code.tex) = %{tl_version}

%description -n texlive-tikz-feynhand
This package lets you draw Feynman diagrams using TikZ. It is a low-end
modification of the TikZ-Feynman package, one of whose principal advantages is
the automatic generation of diagrams, for which it needs LuaTeX. TikZ-FeynHand
only provides the manual mode and hence runs in LaTeX without any reference to
LuaTeX. In addition it provides some new styles for vertices and propagators,
alternative shorter keywords in addition to TikZ-Feynman's longer ones, some
shortcut commands for quickly customizing the diagrams' look, and the new
feature of putting one propagator "on top" of another. It also includes a quick
user guide for getting started, with many examples and a 5-minute introduction
to TikZ.

%package -n texlive-tikz-feynman
Summary:        Feynman diagrams with TikZ
Version:        svn56615
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-iftex
Requires:       texlive-pgfopts
Requires:       tex(ifluatex.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-feynman.sty) = %{tl_version}
Provides:       tex(tikzfeynman.keys.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfeynman.code.tex) = %{tl_version}

%description -n texlive-tikz-feynman
This is a LaTeX package allowing Feynman diagrams to be easily generated within
LaTeX with minimal user instructions and without the need of external programs.
It builds upon the TikZ package and leverages the graph placement algorithms
from TikZ in order to automate the placement of many vertices. tikz-feynman
allows fine-tuned placement of vertices so that even complex diagrams can still
be generated with ease.

%package -n texlive-tikz-imagelabels
Summary:        Put labels on images using TikZ
Version:        svn51490
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Provides:       tex(tikz-imagelabels.sty) = %{tl_version}

%description -n texlive-tikz-imagelabels
This package allows to add label texts to an existing image with the aid of
TikZ. This may be used to label certain features in an image.

%package -n texlive-tikz-inet
Summary:        Draw interaction nets with TikZ
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-inet.sty) = %{tl_version}

%description -n texlive-tikz-inet
The package extends TikZ with macros to draw interaction nets.

%package -n texlive-tikz-kalender
Summary:        A LaTeX based calendar using TikZ
Version:        svn77508
License:        LicenseRef-Unknown
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tikz-kalender
For usage see the example files tikz-kalender-example1.tex,
tikz-kalender-example2.tex, and *.events. The Code is inspired by this document
and is subject to the >>Creative Commons attribution license (CC-BY-SA)<<. The
class tikz-kalender requires the package TikZ and the TikZ libraries calc and
calendar.

%package -n texlive-tikz-karnaugh
Summary:        Typeset Karnaugh maps using TikZ
Version:        svn62040
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarykarnaugh.code.tex) = %{tl_version}

%description -n texlive-tikz-karnaugh
The tikz-karnaugh package is a LaTeX package used to draw Karnaugh maps. It
uses TikZ to produce high quality graph from 1 to 12 variables, but this upper
limit depends on the TeX memory usage and can be different for you. It is very
good for presentation since TikZ allows for a better control over the final
appearance of the map. You can control colour, styles and distances. It can be
considered as an upgrade and extension of Andreas W. Wieland's karnaugh package
towards TikZ supporting. Upgrade because uses TikZ for more option on
typesetting and overall higher quality. Extension because it also supports
American style and inputting the values as they would appear in the map or in
the truth table. Complex maps with solution (implicants) pointed out can be
generated with external java software (see documentation for details). It
supports both American and traditional (simplified labels) styles and from
version 1.3 on American style is natively supported, therefore, no more
addition work is required to typeset Gray coded labels, variable names etc.
From version 1.4, two new macros allow typesetting a map much more similarly as
it should appear. Original order, as the values appear in the truth table,
still being supported.

%package -n texlive-tikz-ladder
Summary:        Draw ladder diagrams using TikZ
Version:        svn62992
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarycircuits.plc.ladder.code.tex) = %{tl_version}

%description -n texlive-tikz-ladder
The tikz-ladder package contains a collection of symbols for typesetting ladder
diagrams (PLC program) in agreement with the international standard
IEC-61131-3/2013. It includes blocks (for representing functions and function
blocks) besides contacts and coils. It extends the circuit library of TikZ and
allows you to draw a ladder diagram in the same way as you would draw any other
circuit.

%package -n texlive-tikz-lake-fig
Summary:        Schematic diagrams of lakes
Version:        svn55288
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(multirow.sty)
Requires:       tex(pbox.sty)
Requires:       tex(relsize.sty)
Requires:       tex(subfiles.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-lake-fig.sty) = %{tl_version}

%description -n texlive-tikz-lake-fig
This package contains a collection of schematic diagrams of lakes for use in
LaTeX documents. Diagrams include representations of material budgets, fluxes,
and connectivity arrangements.

%package -n texlive-tikz-layers
Summary:        TikZ provides graphical layers on TikZ: "behind", "above" and "glass"
Version:        svn46660
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(tikz-layers.sty) = %{tl_version}

%description -n texlive-tikz-layers
TikZ-layers is a tiny package that provides, along side "background", typical
graphical layers on TikZ: "behind", "above" and "glass". The layers may be
selected with one of the styles "on behind layer", "on above layer", "on glass
layer" as an option to a {scope} environment.

%package -n texlive-tikz-mirror-lens
Summary:        Spherical mirrors and lenses in TikZ
Version:        svn65500
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-mirror-lens.sty) = %{tl_version}

%description -n texlive-tikz-mirror-lens
This package allows the automatic drawing of the image of objects in spherical
mirrors and lenses from the data of the focus, from the position and height of
the object. It calculates the position and height of the image, and also
displays the notable rays.

%package -n texlive-tikz-nef
Summary:        Create diagrams for neural networks constructed with the methods of the Neural Engineering Framework (NEF)
Version:        svn55920
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarynef.code.tex) = %{tl_version}

%description -n texlive-tikz-nef
The nef TikZ library provides predefined styles and shapes to create diagrams
for neural networks constructed with the methods of the Neural Engineering
Framework (NEF). The following styles are supported: ea: ensemble array ens:
ensemble ext: external input or output inhibt: inhibitory connection net:
network pnode: pass-through node rect: rectification ensemble recurrent:
recurrent connection

%package -n texlive-tikz-network
Summary:        Draw networks with TikZ
Version:        svn51884
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(datatool.sty)
Requires:       tex(etex.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tikz-network.sty) = %{tl_version}

%description -n texlive-tikz-network
This package allows the creation of images of complex networks that are
seamlessly integrated into the underlying LaTeX files. The package requires
datatool, etex, graphicx, tikz, trimspaces, xifthen, and xkeyval.

%package -n texlive-tikz-nfold
Summary:        Triple, quadruple, and n-fold paths with TikZ
Version:        svn67718
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pgflibrarybezieroffset.code.tex) = %{tl_version}
Provides:       tex(pgflibrarynfold.code.tex) = %{tl_version}
Provides:       tex(pgflibraryoffsetpath.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarynfold.code.tex) = %{tl_version}

%description -n texlive-tikz-nfold
This library adds higher-order paths to TikZ and also fixes some graphical
issues with TikZ' double paths, used e.g. in arrows with an Implies tip. It is
also compatible with tikz-cd, adding support for triple and higher arrows.
Macros to offset arbitrary paths are included as well.

%package -n texlive-tikz-opm
Summary:        Typeset OPM diagrams
Version:        svn32769
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(makeshape.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-opm.sty) = %{tl_version}

%description -n texlive-tikz-opm
Typeset OPM (Object-Process Methodology) diagrams using LaTeX and PGF/TikZ.

%package -n texlive-tikz-optics
Summary:        A library for drawing optical setups with TikZ
Version:        svn62977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibraryoptics.code.tex) = %{tl_version}

%description -n texlive-tikz-optics
This package provides a new TikZ library designed to easily draw optical setups
with TikZ. It provides shapes for lens, mirror, etc. The geometrically
(in)correct computation of light rays through the setup is left to the user.

%package -n texlive-tikz-osci
Summary:        Produce oscilloscope "screen shots"
Version:        svn68636
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(tikz-osci.sty) = %{tl_version}

%description -n texlive-tikz-osci
This package enables you to produce oscilloscope "screen shots".

%package -n texlive-tikz-page
Summary:        Small macro to help building nice and complex layout materials
Version:        svn42039
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-page.sty) = %{tl_version}

%description -n texlive-tikz-page
The package provides a small macro to help building nice and complex layout
materials.

%package -n texlive-tikz-palattice
Summary:        Draw particle accelerator lattices with TikZ
Version:        svn43442
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xargs.sty)
Provides:       tex(tikz-palattice.sty) = %{tl_version}

%description -n texlive-tikz-palattice
This package allows for drawing a map of a particle accelerator just by giving
a list of elements -- similar to lattice files for simulation software. The
package includes 12 common element types like dipoles, quadrupoles, cavities,
or screens, as well as automatic labels with element names, a legend, a rule,
and an environment to fade out parts of the accelerator. The coordinate of any
element can be saved and used for custom TikZ drawings or annotations. Thereby,
lattices can be connected to draw injection/extraction or even a complete
accelerator facility.

%package -n texlive-tikz-planets
Summary:        Illustrate celestial mechanics and the solar system
Version:        svn75210
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfkeys.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
Provides:       tex(planets.sty) = %{tl_version}

%description -n texlive-tikz-planets
This TikZ-package makes it easy to illustrate celestial mechanics and the solar
system. You can use it to draw sketches of the eclipses, the phases of the
Moon, etc. The package requires the standard packages TikZ, xcolor, xstring,
and pgfkeys.

%package -n texlive-tikz-qtree
Summary:        Use existing qtree syntax for trees in TikZ
Version:        svn26108
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pgfsubpic.sty) = %{tl_version}
Provides:       tex(pgfsubpic.tex) = %{tl_version}
Provides:       tex(pgftree.sty) = %{tl_version}
Provides:       tex(pgftree.tex) = %{tl_version}
Provides:       tex(tikz-qtree-compat.sty) = %{tl_version}
Provides:       tex(tikz-qtree.sty) = %{tl_version}
Provides:       tex(tikz-qtree.tex) = %{tl_version}

%description -n texlive-tikz-qtree
The package provides a macro for drawing trees with TikZ using the easy syntax
of Alexis Dimitriadis' Qtree. It improves on TikZ's standard tree-drawing
facility by laying out tree nodes without collisions; it improves on Qtree by
adding lots of features from TikZ (for example, edge labels, arrows between
nodes); and it improves on pst-qtree in being usable with pdfTeX and XeTeX.

%package -n texlive-tikz-relay
Summary:        TikZ library for typesetting electrical diagrams
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarycircuits.ee.IEC.relay.code.tex) = %{tl_version}

%description -n texlive-tikz-relay
This package contains a collection of symbols for typesetting electrical wiring
diagrams for relay control systems. The symbols are meant to be in agreement
with the international standard IEC-60617 which has been adopted worldwide,
with perhaps the exception of the USA. It extends and modifies, when needed,
the TikZ-library circuits.ee.IEC. A few non-standard symbols are also included
mainly to be used in presentations, particularly with the beamer package.

%package -n texlive-tikz-sfc
Summary:        Symbols collection for typesetting Sequential Function Chart (SFC) diagrams (PLC programs)
Version:        svn49424
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarycircuits.plc.sfc.code.tex) = %{tl_version}

%description -n texlive-tikz-sfc
This package contains a collection of symbols for typesetting Sequential
Function Chart (SFC) diagrams in agreement with the international standard
IEC-61131-3/2013. It includes steps (normal and initial), transitions, actions
and actions qualifiers (with and without time duration). It extends the circuit
library of TikZ and allows you to draw an SFC diagram in same way you would
draw any other circuit.

%package -n texlive-tikz-shields
Summary:        Badges as in shields.io, but in LaTeX
Version:        svn76593
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontawesome.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tikz-shields.sty) = %{tl_version}

%description -n texlive-tikz-shields
A small package that allows to include in a LaTeX document shields badges, as
in shields.io. Various styles of badges and other features are available,
including clickable links, logos, and color customization options.

%package -n texlive-tikz-swigs
Summary:        Horizontally and vertically split elliptical nodes
Version:        svn59889
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibraryswigs.code.tex) = %{tl_version}

%description -n texlive-tikz-swigs
This package provides horizontally and vertically split elliptical (pairs of)
nodes in TikZ. The package name derives from the fact that split ellipses of
this type are used to represent Single-World Intervention Graph (SWIG) models
which are used in counterfactual causal inference.

%package -n texlive-tikz-timing
Summary:        Easy generation of timing diagrams as TikZ pictures
Version:        svn64967
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-svn-prov
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(environ.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-timing-advnodes.sty) = %{tl_version}
Provides:       tex(tikz-timing-arrows.sty) = %{tl_version}
Provides:       tex(tikz-timing-beamer.sty) = %{tl_version}
Provides:       tex(tikz-timing-clockarrows.sty) = %{tl_version}
Provides:       tex(tikz-timing-columntype.sty) = %{tl_version}
Provides:       tex(tikz-timing-counters.sty) = %{tl_version}
Provides:       tex(tikz-timing-either.sty) = %{tl_version}
Provides:       tex(tikz-timing-ifsym.sty) = %{tl_version}
Provides:       tex(tikz-timing-interval.sty) = %{tl_version}
Provides:       tex(tikz-timing-nicetabs.sty) = %{tl_version}
Provides:       tex(tikz-timing-overlays.sty) = %{tl_version}
Provides:       tex(tikz-timing.sty) = %{tl_version}

%description -n texlive-tikz-timing
This package provides macros and an environment to generate timing diagrams
(digital waveforms) without much effort. The TikZ package is used to produce
the graphics. The diagrams may be inserted into text (paragraphs, \hbox, etc.)
and into tikzpictures. A tabular-like environment is provided to produce larger
timing diagrams.

%package -n texlive-tikz-trackschematic
Summary:        A TikZ library for creating track diagrams in railways
Version:        svn63480
License:        ISC
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tikz-trackschematic.sty) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.constructions.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.electrics.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.measures.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.symbology.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.topology.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.trafficcontrol.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrackschematic.vehicles.code.tex) = %{tl_version}

%description -n texlive-tikz-trackschematic
This TikZ library is a toolbox of symbols geared primarily towards creating
track schematic for either research or educational purposes. It provides a TikZ
frontend to some of the symbols which may be needed to describe situations and
layouts in railway operation. The library is divided into sublibraries:
topology, trafficcontrol, vehicles, constructions, electrics, symbology, and
measures.

%package -n texlive-tikz-truchet
Summary:        Draw Truchet tiles
Version:        svn50020
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikz-truchet.sty) = %{tl_version}

%description -n texlive-tikz-truchet
This is a package for LaTeX that draws Truchet tiles, as used in Colin
Beveridge's article Too good to be Truchet in issue 08 of Chalkdust.

%package -n texlive-tikz2d-fr
Summary:        Work with some 2D TikZ commands (French)
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listofitems.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikz2d-fr.sty) = %{tl_version}

%description -n texlive-tikz2d-fr
This is a small package to work with some (French) 2D commands for TikZ:
"freehand style" mainlevee define and mark points \DefinirPoints,
\MarquerPoints draw colored segments \TracerSegments

%package -n texlive-tikz3d-fr
Summary:        Work with some 3D figures
Version:        svn75291
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listofitems.sty)
Requires:       tex(randomlist.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikz3d-fr.sty) = %{tl_version}

%description -n texlive-tikz3d-fr
This is a package for working with some 3D figures.

%package -n texlive-tikzbrickfigurines
Summary:        Draw brick figurines with TikZ
Version:        svn76088
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikzbrickfigurines.sty) = %{tl_version}

%description -n texlive-tikzbrickfigurines
A small LaTeX package to draw (2D) brick-figurines with TikZ. The user can
modify colors and/or elements.

%package -n texlive-tikzbricks
Summary:        Drawing bricks with TikZ
Version:        svn73140
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf-pkg
Requires:       texlive-iftex
Requires:       texlive-pgf
Requires:       texlive-tikz-3dplot
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tikzbricks.sty) = %{tl_version}

%description -n texlive-tikzbricks
A small LaTeX package to draw bricks with TikZ. The user can modify color,
shape, and viewpoint.

%package -n texlive-tikzcalendarnotes
Summary:        Highlighting, marking and annotating dates in a TikZ calendar
Version:        svn77050
License:        LPPL-1.3c AND GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzcalendarnotes.sty) = %{tl_version}

%description -n texlive-tikzcalendarnotes
This package offers a "calendar arrangement" (atop of the TikZ calendar
library) and provides a set of commands to highlight, mark, and annotate dates
in a calendar.

%package -n texlive-tikzcodeblocks
Summary:        Helps to draw codeblocks like scratch, NEPO and PXT in TikZ
Version:        svn54758
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(fontawesome.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(tikz.sty)
Requires:       tex(translations.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xspace.sty)
Provides:       tex(tikzcodeblocks.sty) = %{tl_version}

%description -n texlive-tikzcodeblocks
tikzcodeblocks is a LaTeX package for typesetting blockwise graphic programming
languages like scratch, nepo or pxt.

%package -n texlive-tikzdotncross
Summary:        Marking coordinates and crossing paths
Version:        svn77050
License:        LPPL-1.3c AND GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(tikzdotncross.sty) = %{tl_version}

%description -n texlive-tikzdotncross
This package offers a few alternative ways for declaring and marking
coordinates and drawing a line with "jumps" over an already existent path,
which is quite a common issue when drawing, for instance, electronic circuits
(like with CircuiTikZ).

%package -n texlive-tikzducks
Summary:        A little fun package for using rubber ducks in TikZ
Version:        svn77080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf-pkg
Requires:       texlive-iftex
Requires:       texlive-pgf
Requires:       tex(tikz.sty)
Provides:       tex(tikzducks.sty) = %{tl_version}
Provides:       tex(tikzlibraryducks.code.tex) = %{tl_version}

%description -n texlive-tikzducks
The package is a LaTeX package for ducks to be used in TikZ pictures. This
project is a continuation of an answer at StackExchange How we can draw a duck?

%package -n texlive-tikzfill
Summary:        TikZ libraries for filling with images and patterns
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(tikzfill-common.sty) = %{tl_version}
Provides:       tex(tikzfill.hexagon.sty) = %{tl_version}
Provides:       tex(tikzfill.image.sty) = %{tl_version}
Provides:       tex(tikzfill.rhombus.sty) = %{tl_version}
Provides:       tex(tikzfill.sty) = %{tl_version}
Provides:       tex(tikzlibraryfill.hexagon.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfill.image.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfill.rhombus.code.tex) = %{tl_version}

%description -n texlive-tikzfill
This is a collection of TikZ libraries which add further options to fill TikZ
paths with images and patterns. The libraries comprise fillings with images
from files and from TikZ pictures. Also, patterns of hexagons and of rhombi are
provided.

%package -n texlive-tikzfxgraph
Summary:        Plotting functions in a simplified way
Version:        svn77050
License:        LPPL-1.3c AND GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzfxgraph.sty) = %{tl_version}

%description -n texlive-tikzfxgraph
This package is mostly a wrap around pgfplots and Gnuplot, hiding most of their
inherent complexity.

%package -n texlive-tikzinclude
Summary:        Import TikZ images from colletions
Version:        svn28715
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikzinclude.sty) = %{tl_version}

%description -n texlive-tikzinclude
The package addresses the problem of importing only one TikZ-image from a file
holding multiple images.

%package -n texlive-tikzlings
Summary:        A collection of cute little animals and similar creatures
Version:        svn77079
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf-pkg
Requires:       texlive-iftex
Requires:       texlive-pgf
Requires:       texlive-pgf-blur
Requires:       tex(tikz.sty)
Provides:       tex(tikzlibrarytikzlings.code.tex) = %{tl_version}
Provides:       tex(tikzlings-addons.sty) = %{tl_version}
Provides:       tex(tikzlings-anteaters.sty) = %{tl_version}
Provides:       tex(tikzlings-apes.sty) = %{tl_version}
Provides:       tex(tikzlings-bats.sty) = %{tl_version}
Provides:       tex(tikzlings-bears.sty) = %{tl_version}
Provides:       tex(tikzlings-bees.sty) = %{tl_version}
Provides:       tex(tikzlings-bugs.sty) = %{tl_version}
Provides:       tex(tikzlings-cats.sty) = %{tl_version}
Provides:       tex(tikzlings-chickens.sty) = %{tl_version}
Provides:       tex(tikzlings-coatis.sty) = %{tl_version}
Provides:       tex(tikzlings-dogs.sty) = %{tl_version}
Provides:       tex(tikzlings-elephants.sty) = %{tl_version}
Provides:       tex(tikzlings-hippos.sty) = %{tl_version}
Provides:       tex(tikzlings-koalas.sty) = %{tl_version}
Provides:       tex(tikzlings-list.sty) = %{tl_version}
Provides:       tex(tikzlings-marmots.sty) = %{tl_version}
Provides:       tex(tikzlings-meerkats.sty) = %{tl_version}
Provides:       tex(tikzlings-mice.sty) = %{tl_version}
Provides:       tex(tikzlings-moles.sty) = %{tl_version}
Provides:       tex(tikzlings-owls.sty) = %{tl_version}
Provides:       tex(tikzlings-pandas.sty) = %{tl_version}
Provides:       tex(tikzlings-penguins.sty) = %{tl_version}
Provides:       tex(tikzlings-pigs.sty) = %{tl_version}
Provides:       tex(tikzlings-rhinos.sty) = %{tl_version}
Provides:       tex(tikzlings-sheep.sty) = %{tl_version}
Provides:       tex(tikzlings-sloths.sty) = %{tl_version}
Provides:       tex(tikzlings-snowmen.sty) = %{tl_version}
Provides:       tex(tikzlings-squirrels.sty) = %{tl_version}
Provides:       tex(tikzlings-turkeys.sty) = %{tl_version}
Provides:       tex(tikzlings-wolves.sty) = %{tl_version}
Provides:       tex(tikzlings.sty) = %{tl_version}

%description -n texlive-tikzlings
A collection of LaTeX packages for drawing cute little animals and similar
creatures using TikZ. Currently, the following TikZlings are included: anteater
ape bat bear bee bug cat chicken coati dog elephant hippo koala marmot meerkat
mole mouse owl panda penguin pig rhino sheep sloth snowman squirrel turkey wolf
These little drawings can be customized in many ways.

%package -n texlive-tikzmark
Summary:        Use TikZ's method of remembering a position on a page
Version:        svn64819
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarytikzmark.code.tex) = %{tl_version}
Provides:       tex(tikzmarklibraryams.code.tex) = %{tl_version}
Provides:       tex(tikzmarklibraryhighlighting.code.tex) = %{tl_version}
Provides:       tex(tikzmarklibrarylistings.code.tex) = %{tl_version}

%description -n texlive-tikzmark
The tikzmark package defines a command to "remember" a position on a page for
later (or earlier) use, primarily (but not exclusively) with TikZ.

%package -n texlive-tikzmarmots
Summary:        Drawing little marmots in TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-tikzlings
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tikzlings-marmots.sty)
Provides:       tex(tikzlibrarymarmots.code.tex) = %{tl_version}
Provides:       tex(tikzmarmots-v1.sty) = %{tl_version}
Provides:       tex(tikzmarmots.sty) = %{tl_version}

%description -n texlive-tikzmarmots
This is a LaTeX package for marmots to be used in TikZ pictures. These little
figures are constructed in such a way that they may even "borrow" some
accessories and other attributes from the TikZlings package.

%package -n texlive-tikzorbital
Summary:        Atomic and molecular orbitals using TikZ
Version:        svn36439
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikzorbital.sty) = %{tl_version}

%description -n texlive-tikzorbital
Atomic s, p and d orbitals may be drawn, as well as molecular orbital diagrams.

%package -n texlive-tikzpackets
Summary:        Display network packets
Version:        svn55827
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pbox.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(tikzPackets.sty) = %{tl_version}

%description -n texlive-tikzpackets
This package allows you to easily display network packets graphically.

%package -n texlive-tikzpagenodes
Summary:        A single TikZ node for the whole page
Version:        svn64967
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifoddpage.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikzpagenodes.sty) = %{tl_version}

%description -n texlive-tikzpagenodes
The package provides special PGF/TikZ nodes for the text, marginpar, footer and
header area of the current page. They are inspired by the 'current page' node
defined by PGF/TikZ itself.

%package -n texlive-tikzpeople
Summary:        Draw people-shaped nodes in TikZ
Version:        svn67840
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(capt-of.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Provides:       tex(tikzpeople.shape.alice.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.bob.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.bride.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.builder.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.businessman.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.charlie.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.chef.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.conductor.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.cowboy.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.criminal.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.dave.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.devil.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.duck.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.graduate.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.groom.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.guard.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.jester.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.judge.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.maninblack.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.mexican.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.nun.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.nurse.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.physician.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.pilot.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.police.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.priest.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.sailor.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.santa.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.surgeon.sty) = %{tl_version}
Provides:       tex(tikzpeople.sty) = %{tl_version}

%description -n texlive-tikzpeople
This package provides people-shaped nodes in the style of Microsoft Visio clip
art, to be used with TikZ. The available, highly customizable, node shapes are:
alice, bob, bride, builder, businessman, charlie, chef, conductor, cowboy,
criminal, dave, devil, duck, graduate, groom, guard, jester, judge,
maininblack, mexican, nun, nurse, physician, pilot, police, priest, sailor,
santa, surgeon.

%package -n texlive-tikzpfeile
Summary:        Draw arrows using PGF/TikZ
Version:        svn25777
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikzpfeile.sty) = %{tl_version}

%description -n texlive-tikzpfeile
In a document with a lot of diagrams created with PGF/TikZ, there is a
possibility of the reader being distracted by different sorts of arrowheads in
the diagrams and in the text (as, e.g., in \rightarrow). The package defines
macros to create all arrows using PGF/TikZ, so as to avoid the problem.

%package -n texlive-tikzpingus
Summary:        Penguins with TikZ
Version:        svn75543
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikzpingus.sty) = %{tl_version}

%description -n texlive-tikzpingus
tikzpingus is a package similar to TikZducks but with penguins and a vast set
of gadgets and extras (capable of changing the wing-positions, body-types, and
more).

%package -n texlive-tikzposter
Summary:        Create scientific posters using TikZ
Version:        svn32732
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzposterBackgroundstyles.tex) = %{tl_version}
Provides:       tex(tikzposterBlockstyles.tex) = %{tl_version}
Provides:       tex(tikzposterColorpalettes.tex) = %{tl_version}
Provides:       tex(tikzposterColorstyles.tex) = %{tl_version}
Provides:       tex(tikzposterInnerblockstyles.tex) = %{tl_version}
Provides:       tex(tikzposterLayoutthemes.tex) = %{tl_version}
Provides:       tex(tikzposterNotestyles.tex) = %{tl_version}
Provides:       tex(tikzposterTitlestyles.tex) = %{tl_version}

%description -n texlive-tikzposter
A document class provides a simple way of using TikZ for generating posters.
Several formatting options are available, and spacing and layout of the poster
is to a large extent automated.

%package -n texlive-tikzquads
Summary:        A few shapes designed to be used with CircuiTikZ
Version:        svn77050
License:        LPPL-1.3c OR AGPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfkeysearch.sty)
Requires:       tex(tikzdotncross.sty)
Provides:       tex(tikzquads.sty) = %{tl_version}

%description -n texlive-tikzquads
This package defines a few extra shapes, Quadripoles and single port, which can
be used 'standalone', but are mainly meant to be used with CircuiTikZ.

%package -n texlive-tikzquests
Summary:        A parametric questions' repositories framework
Version:        svn77050
License:        LPPL-1.3c AND GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzquests.sty) = %{tl_version}

%description -n texlive-tikzquests
This is a framework for building parametric questions' repositories, which can
be further used to construct parametric questions for exams. Unlike other
packages of the kind this does not try to enforce any pre-defined presentation
format, focusing only on how to set a repository of questions and use them.

%package -n texlive-tikzscale
Summary:        Resize pictures while respecting text size
Version:        svn30637
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikzscale.sty) = %{tl_version}

%description -n texlive-tikzscale
The package extends the \includegraphics command to support tikzpictures. It
allows scaling of TikZ images and PGFPlots to a given width or height without
changing the text size.

%package -n texlive-tikzsymbols
Summary:        Some symbols created using TikZ
Version:        svn61300
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(tikzsymbols.sty) = %{tl_version}

%description -n texlive-tikzsymbols
The package provides various emoticons, cooking symbols and trees.

%package -n texlive-tikzviolinplots
Summary:        Draws violin plots from data
Version:        svn76451
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(pgfplotstable.sty)
Requires:       tex(stringstrings.sty)
Provides:       tex(tikzviolinplots.sty) = %{tl_version}

%description -n texlive-tikzviolinplots
This package enables the user to draw violin plots, calculating the kernel
density estimation from the data and plotting the resulting curve inside a
tikzpicture environment. It supports different kernels, and allows the user to
either set the bandwidth value for each plot or use a default value.

%package -n texlive-tile-graphic
Summary:        Create tiles of a graphical file
Version:        svn55325
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(multido.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(web.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tile-graphic.sty) = %{tl_version}

%description -n texlive-tile-graphic
This package breaks a given graphical file into n rows and m columns of
subgraphics, which are called tiles. The tiles can be written separately to
individual PDF files, or packaged into a single PDF file.

%package -n texlive-tilings
Summary:        A TikZ library for drawing tiles and tilings
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibrarypenrose.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytilings.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytilings.penrose.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytilings.polykite.code.tex) = %{tl_version}

%description -n texlive-tilings
This package provides a TikZ library for working with tiles, tilings, and
tessellations. Using it, one can define tiles, place tiles, deform tiles, and
-- in some cases -- apply replacement rules to generate tessellations. It has
pre-defined tiles for most of the Penrose tile sets and the aperiodical
polykite tiles. This is a replacement for the penrose package, renamed as it
now deals with more extensive tiles than just the Penrose tile sets.

%package -n texlive-timechart
Summary:        A package for drawing chronological charts
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(timechart.sty) = %{tl_version}

%description -n texlive-timechart
This package provides for the easy creation of chronological charts which show
visually the relative historical positions of people and events. Each event or
period can be specified by a single line of LaTeX code comprising (possibly
uncertain) start and finish dates and a label, and the package takes care of
indicating the uncertainties and whether intervals extend beyond the specified
bounds of the chart.

%package -n texlive-timing-diagrams
Summary:        Draw timing diagrams
Version:        svn31491
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(timing-diagrams.sty) = %{tl_version}

%description -n texlive-timing-diagrams
The package provides commands to draw and annotate various kinds of timing
diagrams, using Tikz. Documentation is sparse, but the source and the examples
file should be of some use.

%package -n texlive-tipfr
Summary:        Produces calculator's keys with the help of TikZ
Version:        svn38646
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multido.sty)
Requires:       tex(newtxtt.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tipfr.sty) = %{tl_version}

%description -n texlive-tipfr
The package provides commands to draw calculator keys with the help of TikZ. It
also provides commands to draw the content of screens and of menu items.

%package -n texlive-tkz-base
Summary:        Tools for drawing with a cartesian coordinate system
Version:        svn69460
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(numprint.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfp.sty)
Provides:       tex(tkz-base.sty) = %{tl_version}
Provides:       tex(tkz-lib-marks.tex) = %{tl_version}
Provides:       tex(tkz-lib-shape.tex) = %{tl_version}
Provides:       tex(tkz-obj-axes.tex) = %{tl_version}
Provides:       tex(tkz-obj-grids.tex) = %{tl_version}
Provides:       tex(tkz-obj-marks.tex) = %{tl_version}
Provides:       tex(tkz-obj-points.tex) = %{tl_version}
Provides:       tex(tkz-obj-rep.tex) = %{tl_version}
Provides:       tex(tkz-tools-BB.tex) = %{tl_version}
Provides:       tex(tkz-tools-arith.tex) = %{tl_version}
Provides:       tex(tkz-tools-base.tex) = %{tl_version}
Provides:       tex(tkz-tools-colors.tex) = %{tl_version}
Provides:       tex(tkz-tools-misc.tex) = %{tl_version}
Provides:       tex(tkz-tools-modules.tex) = %{tl_version}
Provides:       tex(tkz-tools-print.tex) = %{tl_version}
Provides:       tex(tkz-tools-text.tex) = %{tl_version}
Provides:       tex(tkz-tools-utilities.tex) = %{tl_version}

%description -n texlive-tkz-base
The bundle is a set of packages, designed to give mathematics teachers (and
students) easy access to programming of drawings with TikZ.

%package -n texlive-tkz-berge
Summary:        Macros for drawing graphs of graph theory
Version:        svn57485
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tkz-graph.sty)
Provides:       tex(tkz-berge.sty) = %{tl_version}

%description -n texlive-tkz-berge
The package provides a collection of useful macros for drawing classic graphs
of graph theory, or to make other graphs. This package has been taken
temporarily out of circulation to give the author time to investigate some
problems.

%package -n texlive-tkz-bernoulli
Summary:        Draw Bernoulli trees with TikZ
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgffor.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintbinhex.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tkz-bernoulli.sty) = %{tl_version}

%description -n texlive-tkz-bernoulli
This is a package for representing Bernoulli trees with PGF/TikZ.

%package -n texlive-tkz-doc
Summary:        Documentation macros for the TKZ series of packages
Version:        svn68665
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tkz-doc
This bundle offers a documentation class (tkz-doc) and a package (tkzexample).
These files are used in the documentation of the author's packages tkz-base,
tkz-euclide, tkz-fct, tkz-linknodes, and tkz-tab.

%package -n texlive-tkz-elements
Summary:        A Lua library for drawing Euclidean geometry with TikZ or tkz-euclide
Version:        svn77479
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(tkz-elements.sty) = %{tl_version}

%description -n texlive-tkz-elements
This package provides a library written in Lua, allowing to make all the
necessary calculations to define the objects of a Euclidean geometry figure.
You need to compile with LuaLaTeX. The definitions and calculations are only
done with Lua. The main possibility of programming proposed is oriented "object
programming" with object classes like point, line, triangle, circle and now,
conic. For the moment, once the calculations are done, it is tkz-euclide or
TikZ which allows the drawings.

%package -n texlive-tkz-euclide
Summary:        Tools for drawing Euclidean geometry
Version:        svn77515
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(tkz-draw-eu-angles.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-arcs.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-circles.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-compass.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-ellipses.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-lines.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-points.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-polygons.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-protractor.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-sectors.tex) = %{tl_version}
Provides:       tex(tkz-draw-eu-show.tex) = %{tl_version}
Provides:       tex(tkz-euclide.sty) = %{tl_version}
Provides:       tex(tkz-lib-eu-marks.tex) = %{tl_version}
Provides:       tex(tkz-lib-eu-shape.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-axesmin.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-circles-by.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-circles.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-grids.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-lines.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-lua-circles-by.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-lua-circles.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-lua-points-by.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-lua-points-spc.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-lua-points-with.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-lua-points.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-points-by.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-points-rnd.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-points-spc.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-points-with.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-points.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-polygons.tex) = %{tl_version}
Provides:       tex(tkz-obj-eu-triangles.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-BB.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-angles.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-base.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-colors.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-intersections.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-lua-angles.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-lua-base.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-lua-intersections.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-lua-math.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-math.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-modules.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-text.tex) = %{tl_version}
Provides:       tex(tkz-tools-eu-utilities.tex) = %{tl_version}

%description -n texlive-tkz-euclide
The tkz-euclide package is a set of files designed to give math teachers and
students easy access to the programming of Euclidean geometry with TikZ.

%package -n texlive-tkz-fct
Summary:        Tools for drawing graphs of functions
Version:        svn61949
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(tkz-base.sty)
Provides:       tex(tkz-fct.sty) = %{tl_version}

%description -n texlive-tkz-fct
The tkz-fct package is designed to give math teachers (and students) easy
access to programming graphs of functions with TikZ and gnuplot.

%package -n texlive-tkz-graph
Summary:        Draw graph-theory graphs
Version:        svn57484
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tkz-graph.sty) = %{tl_version}

%description -n texlive-tkz-graph
The package is designed to create graph diagrams as simply as possible, using
TikZ.

%package -n texlive-tkz-grapheur
Summary:        A LaTeX package with tools for graph plotting (and TikZ)
Version:        svn77346
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xint-regression.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tkz-grapheur.sty) = %{tl_version}

%description -n texlive-tkz-grapheur
This package provides some commands to help French mathematics teachers for
15-18 years olds, with graphs of functions: define and draw functions and
interpolations curves work with integrals, tangents, intersections get
coordinates of points ... The syntax is rather explicit, like \DefinirCourbe,
\RecupererCoordonnees,\TrouverIntersections, etc.

%package -n texlive-tkz-orm
Summary:        Create Object-Role Model (ORM) diagrams
Version:        svn61719
License:        GPL-2.0-only AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(tkz-orm.sty) = %{tl_version}

%description -n texlive-tkz-orm
The package provides styles for drawing Object-Role Model (ORM) diagrams in TeX
based on the PGF and TikZ picture environment.

%package -n texlive-tkz-tab
Summary:        Tables of signs and variations using PGF/TikZ
Version:        svn66115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tkz-tab.sty) = %{tl_version}

%description -n texlive-tkz-tab
The package provides comprehensive facilities for preparing lists of signs and
variations, using PGF. The package documentation requires the tkz-doc bundle.
This package has been taken temporarily out of circulation to give the author
time to investigate some problems.

%package -n texlive-tkzexample
Summary:        Package for the documentation of all tkz-* packages
Version:        svn63908
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(mdframed.sty)
Provides:       tex(tkzexample.sty) = %{tl_version}

%description -n texlive-tkzexample
This package is needed to compile the documentation of all tkz-* packages (like
tkz-euclide).

%package -n texlive-tonevalue
Summary:        Tool for linguists and phoneticians to visualize tone value patterns
Version:        svn60058
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(contour.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tonevalue.sty) = %{tl_version}

%description -n texlive-tonevalue
This package provides a TikZ-based solution to typeset visualisations of tone
values. Currently, unt's model is implemented. Support for more models is
planned.

%package -n texlive-tqft
Summary:        Drawing TQFT diagrams with TikZ/PGF
Version:        svn71401
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgf.sty)
Requires:       tex(pgfkeys.sty)
Provides:       tex(tikzlibrarytqft.code.tex) = %{tl_version}
Provides:       tex(tqft.sty) = %{tl_version}

%description -n texlive-tqft
The package defines some node shapes useful for drawing TQFT diagrams with
TikZ/PGF. That is, it defines highly customisable shapes that look like
cobordisms between circles, such as those used in TQFT and other mathematical
diagrams.

%package -n texlive-tsemlines
Summary:        Support for the ancient \emline macro
Version:        svn23440
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tsemlines.sty) = %{tl_version}

%description -n texlive-tsemlines
Occasional Documents appear, that use graphics generated by texcad from the
emtex distribution. These documents often use the \emline macro, which produced
lines at an arbitrary orientation. The present package emulates the macro,
using TikZ.

%package -n texlive-tufte-latex
Summary:        Document classes inspired by the work of Edward Tufte
Version:        svn37649
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-xifthen
Requires:       texlive-ifmtarg
Requires:       texlive-changepage
Requires:       texlive-paralist
Requires:       texlive-sauerj
Requires:       texlive-placeins
Provides:       tex(tufte-common.def) = %{tl_version}

%description -n texlive-tufte-latex
Provided are two classes inspired, respectively, by handouts and books created
by Edward Tufte.

%package -n texlive-twemojis
Summary:        Use Twitter's open source emojis through LaTeX commands
Version:        svn62930
License:        LPPL-1.3c AND CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(twemojis.sty) = %{tl_version}

%description -n texlive-twemojis
This package provides a simple wrapper which allows to use Twitter's open
source emojis through LaTeX commands. This relies on images, so no fancy
unicode-font stuff is needed and it should work on every installation.

%package -n texlive-tzplot
Summary:        Plot graphs with TikZ abbreviations
Version:        svn77181
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(tzplot.sty) = %{tl_version}

%description -n texlive-tzplot
This is a LaTeX package that provides TikZ-based macros to make it easy to draw
graphs. The macros provided in this package are just abbreviations for TikZ
codes, which can be complicated; but using the package will hopefully make
drawing easier, especially when drawing repeatedly. The macros were chosen and
developed with an emphasis on drawing graphs in economics. The package depends
on TikZ, xparse, and expl3.

%package -n texlive-utfsym
Summary:        Provides various Unicode symbols
Version:        svn63076
License:        CC0-1.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(utfsym.sty) = %{tl_version}

%description -n texlive-utfsym
This package provides various symbols from the Unicode in order to be able to
use them originally in a school setting such as on worksheets.

%package -n texlive-vectorlogos
Summary:        Vectorial logos (GeoGebra, Emacs, Scratch, ...) with 'inline' support
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(xstring.sty)
Provides:       tex(vectorlogos.sty) = %{tl_version}

%description -n texlive-vectorlogos
With this package you can insert vectorial logos of some 'classic' software.
The format of the logos is pdf. The package provides macros to insert them
inline, with automatic height and alignment.

%package -n texlive-venndiagram
Summary:        Creating Venn diagrams with TikZ
Version:        svn47952
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(venndiagram.sty) = %{tl_version}

%description -n texlive-venndiagram
The package assists generation of simple two- and three-set Venn diagrams for
lectures or assignment sheets. The package requires the TikZ package.

%package -n texlive-vexillology
Summary:        Vexillogical symbols
Version:        svn77381
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(vexillology.sty) = %{tl_version}

%description -n texlive-vexillology
This package implements symbols used by vexillologists (people who study flags)
to indicate certain aspects of flags, such as where they are used, who uses
them, and what they look like. The package uses TikZ to draw the symbols, whose
heights scale with the font size.

%package -n texlive-visualpstricks
Summary:        Visual help for PSTricks based on images with minimum text
Version:        svn39799
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-visualpstricks-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-visualpstricks-doc <= 11:%{version}

%description -n texlive-visualpstricks
Visual help for PSTricks based on images with minimum text. One image per
command or per parameter.

%package -n texlive-wheelchart
Summary:        Diagrams with circular or other shapes using TikZ and LaTeX3
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(wheelchart.sty) = %{tl_version}

%description -n texlive-wheelchart
This package is based on the package TikZ and can be used to draw various kinds
of diagrams such as bar charts, doughnut charts, infographics, pie charts, ring
charts, square charts, sunburst charts, waffle charts and wheel charts. It
provides several options to customize the diagrams. It is also possible to
specify a plot for the shape of the chart. Furthermore a legend can be added
and the table of contents can be displayed as one of these diagrams.

%package -n texlive-wordcloud
Summary:        Drawing wordclouds with MetaPost and Lua
Version:        svn76890
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luamplib.sty)
Provides:       tex(wordcloud.sty) = %{tl_version}

%description -n texlive-wordcloud
This MetaPost and LuaLaTeX package allows drawing wordclouds from a list of
words and weights. The algorithm is implemented with MetaPost whereas Lua is
used to parse LaTeX commands, to build the list of words and weights from a
text file and to generate MetaPost code interpreted by luamplib.

%package -n texlive-worldflags
Summary:        Drawing flags with TikZ
Version:        svn68827
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(worldflag_0.tex) = %{tl_version}
Provides:       tex(worldflag_1.tex) = %{tl_version}
Provides:       tex(worldflag_2.tex) = %{tl_version}
Provides:       tex(worldflag_3.tex) = %{tl_version}
Provides:       tex(worldflag_4.tex) = %{tl_version}
Provides:       tex(worldflag_5.tex) = %{tl_version}
Provides:       tex(worldflag_6.tex) = %{tl_version}
Provides:       tex(worldflag_7.tex) = %{tl_version}
Provides:       tex(worldflag_8.tex) = %{tl_version}
Provides:       tex(worldflag_9.tex) = %{tl_version}
Provides:       tex(worldflag_A.tex) = %{tl_version}
Provides:       tex(worldflag_AD.tex) = %{tl_version}
Provides:       tex(worldflag_AE.tex) = %{tl_version}
Provides:       tex(worldflag_AF.tex) = %{tl_version}
Provides:       tex(worldflag_AG.tex) = %{tl_version}
Provides:       tex(worldflag_AL.tex) = %{tl_version}
Provides:       tex(worldflag_AM.tex) = %{tl_version}
Provides:       tex(worldflag_AO.tex) = %{tl_version}
Provides:       tex(worldflag_AQ.tex) = %{tl_version}
Provides:       tex(worldflag_AR.tex) = %{tl_version}
Provides:       tex(worldflag_AT-B.tex) = %{tl_version}
Provides:       tex(worldflag_AT-K.tex) = %{tl_version}
Provides:       tex(worldflag_AT-N.tex) = %{tl_version}
Provides:       tex(worldflag_AT-O.tex) = %{tl_version}
Provides:       tex(worldflag_AT-S.tex) = %{tl_version}
Provides:       tex(worldflag_AT-St.tex) = %{tl_version}
Provides:       tex(worldflag_AT-T.tex) = %{tl_version}
Provides:       tex(worldflag_AT-V.tex) = %{tl_version}
Provides:       tex(worldflag_AT-W.tex) = %{tl_version}
Provides:       tex(worldflag_AT.tex) = %{tl_version}
Provides:       tex(worldflag_AU.tex) = %{tl_version}
Provides:       tex(worldflag_AX.tex) = %{tl_version}
Provides:       tex(worldflag_AZ.tex) = %{tl_version}
Provides:       tex(worldflag_Abkhazia.tex) = %{tl_version}
Provides:       tex(worldflag_Artsakh.tex) = %{tl_version}
Provides:       tex(worldflag_B.tex) = %{tl_version}
Provides:       tex(worldflag_BA.tex) = %{tl_version}
Provides:       tex(worldflag_BB.tex) = %{tl_version}
Provides:       tex(worldflag_BD.tex) = %{tl_version}
Provides:       tex(worldflag_BE.tex) = %{tl_version}
Provides:       tex(worldflag_BF.tex) = %{tl_version}
Provides:       tex(worldflag_BG.tex) = %{tl_version}
Provides:       tex(worldflag_BH.tex) = %{tl_version}
Provides:       tex(worldflag_BI.tex) = %{tl_version}
Provides:       tex(worldflag_BJ.tex) = %{tl_version}
Provides:       tex(worldflag_BN.tex) = %{tl_version}
Provides:       tex(worldflag_BO.tex) = %{tl_version}
Provides:       tex(worldflag_BR.tex) = %{tl_version}
Provides:       tex(worldflag_BS.tex) = %{tl_version}
Provides:       tex(worldflag_BT.tex) = %{tl_version}
Provides:       tex(worldflag_BW.tex) = %{tl_version}
Provides:       tex(worldflag_BY.tex) = %{tl_version}
Provides:       tex(worldflag_BZ.tex) = %{tl_version}
Provides:       tex(worldflag_Bonaire.tex) = %{tl_version}
Provides:       tex(worldflag_Buddhism.tex) = %{tl_version}
Provides:       tex(worldflag_C.tex) = %{tl_version}
Provides:       tex(worldflag_CA.tex) = %{tl_version}
Provides:       tex(worldflag_CD.tex) = %{tl_version}
Provides:       tex(worldflag_CF.tex) = %{tl_version}
Provides:       tex(worldflag_CG.tex) = %{tl_version}
Provides:       tex(worldflag_CH.tex) = %{tl_version}
Provides:       tex(worldflag_CI.tex) = %{tl_version}
Provides:       tex(worldflag_CK.tex) = %{tl_version}
Provides:       tex(worldflag_CL.tex) = %{tl_version}
Provides:       tex(worldflag_CM.tex) = %{tl_version}
Provides:       tex(worldflag_CN.tex) = %{tl_version}
Provides:       tex(worldflag_CO.tex) = %{tl_version}
Provides:       tex(worldflag_CR.tex) = %{tl_version}
Provides:       tex(worldflag_CU.tex) = %{tl_version}
Provides:       tex(worldflag_CV.tex) = %{tl_version}
Provides:       tex(worldflag_CY.tex) = %{tl_version}
Provides:       tex(worldflag_CZ.tex) = %{tl_version}
Provides:       tex(worldflag_Christian.tex) = %{tl_version}
Provides:       tex(worldflag_D.tex) = %{tl_version}
Provides:       tex(worldflag_DE-BY.tex) = %{tl_version}
Provides:       tex(worldflag_DE.tex) = %{tl_version}
Provides:       tex(worldflag_DJ.tex) = %{tl_version}
Provides:       tex(worldflag_DK.tex) = %{tl_version}
Provides:       tex(worldflag_DM.tex) = %{tl_version}
Provides:       tex(worldflag_DO.tex) = %{tl_version}
Provides:       tex(worldflag_DZ.tex) = %{tl_version}
Provides:       tex(worldflag_E.tex) = %{tl_version}
Provides:       tex(worldflag_EC.tex) = %{tl_version}
Provides:       tex(worldflag_EE.tex) = %{tl_version}
Provides:       tex(worldflag_EG.tex) = %{tl_version}
Provides:       tex(worldflag_EH.tex) = %{tl_version}
Provides:       tex(worldflag_ER.tex) = %{tl_version}
Provides:       tex(worldflag_ES.tex) = %{tl_version}
Provides:       tex(worldflag_ET.tex) = %{tl_version}
Provides:       tex(worldflag_EU.tex) = %{tl_version}
Provides:       tex(worldflag_Esperanto.tex) = %{tl_version}
Provides:       tex(worldflag_F.tex) = %{tl_version}
Provides:       tex(worldflag_FI.tex) = %{tl_version}
Provides:       tex(worldflag_FJ.tex) = %{tl_version}
Provides:       tex(worldflag_FM.tex) = %{tl_version}
Provides:       tex(worldflag_FO.tex) = %{tl_version}
Provides:       tex(worldflag_FR.tex) = %{tl_version}
Provides:       tex(worldflag_G.tex) = %{tl_version}
Provides:       tex(worldflag_GA.tex) = %{tl_version}
Provides:       tex(worldflag_GB-ENG.tex) = %{tl_version}
Provides:       tex(worldflag_GB-RAF.tex) = %{tl_version}
Provides:       tex(worldflag_GB-RED.tex) = %{tl_version}
Provides:       tex(worldflag_GB-RN.tex) = %{tl_version}
Provides:       tex(worldflag_GB-SCT.tex) = %{tl_version}
Provides:       tex(worldflag_GB.tex) = %{tl_version}
Provides:       tex(worldflag_GD.tex) = %{tl_version}
Provides:       tex(worldflag_GE.tex) = %{tl_version}
Provides:       tex(worldflag_GF.tex) = %{tl_version}
Provides:       tex(worldflag_GG.tex) = %{tl_version}
Provides:       tex(worldflag_GH.tex) = %{tl_version}
Provides:       tex(worldflag_GI.tex) = %{tl_version}
Provides:       tex(worldflag_GL.tex) = %{tl_version}
Provides:       tex(worldflag_GM.tex) = %{tl_version}
Provides:       tex(worldflag_GN.tex) = %{tl_version}
Provides:       tex(worldflag_GQ.tex) = %{tl_version}
Provides:       tex(worldflag_GR.tex) = %{tl_version}
Provides:       tex(worldflag_GT.tex) = %{tl_version}
Provides:       tex(worldflag_GW.tex) = %{tl_version}
Provides:       tex(worldflag_GY.tex) = %{tl_version}
Provides:       tex(worldflag_H.tex) = %{tl_version}
Provides:       tex(worldflag_HN.tex) = %{tl_version}
Provides:       tex(worldflag_HR.tex) = %{tl_version}
Provides:       tex(worldflag_HT.tex) = %{tl_version}
Provides:       tex(worldflag_HU.tex) = %{tl_version}
Provides:       tex(worldflag_I.tex) = %{tl_version}
Provides:       tex(worldflag_ID.tex) = %{tl_version}
Provides:       tex(worldflag_IE.tex) = %{tl_version}
Provides:       tex(worldflag_IL.tex) = %{tl_version}
Provides:       tex(worldflag_IM.tex) = %{tl_version}
Provides:       tex(worldflag_IN.tex) = %{tl_version}
Provides:       tex(worldflag_IQ.tex) = %{tl_version}
Provides:       tex(worldflag_IR.tex) = %{tl_version}
Provides:       tex(worldflag_IS.tex) = %{tl_version}
Provides:       tex(worldflag_IT-AA.tex) = %{tl_version}
Provides:       tex(worldflag_IT-AB.tex) = %{tl_version}
Provides:       tex(worldflag_IT-AO.tex) = %{tl_version}
Provides:       tex(worldflag_IT-BA.tex) = %{tl_version}
Provides:       tex(worldflag_IT-CL.tex) = %{tl_version}
Provides:       tex(worldflag_IT-CM.tex) = %{tl_version}
Provides:       tex(worldflag_IT-EM.tex) = %{tl_version}
Provides:       tex(worldflag_IT-FR.tex) = %{tl_version}
Provides:       tex(worldflag_IT-LA.tex) = %{tl_version}
Provides:       tex(worldflag_IT-LI.tex) = %{tl_version}
Provides:       tex(worldflag_IT-LO.tex) = %{tl_version}
Provides:       tex(worldflag_IT-MA.tex) = %{tl_version}
Provides:       tex(worldflag_IT-MO.tex) = %{tl_version}
Provides:       tex(worldflag_IT-PI.tex) = %{tl_version}
Provides:       tex(worldflag_IT-PU.tex) = %{tl_version}
Provides:       tex(worldflag_IT-SA.tex) = %{tl_version}
Provides:       tex(worldflag_IT-SI.tex) = %{tl_version}
Provides:       tex(worldflag_IT-TA.tex) = %{tl_version}
Provides:       tex(worldflag_IT-TN.tex) = %{tl_version}
Provides:       tex(worldflag_IT-TO.tex) = %{tl_version}
Provides:       tex(worldflag_IT-UM.tex) = %{tl_version}
Provides:       tex(worldflag_IT-VE.tex) = %{tl_version}
Provides:       tex(worldflag_IT.tex) = %{tl_version}
Provides:       tex(worldflag_J.tex) = %{tl_version}
Provides:       tex(worldflag_JE.tex) = %{tl_version}
Provides:       tex(worldflag_JM.tex) = %{tl_version}
Provides:       tex(worldflag_JO.tex) = %{tl_version}
Provides:       tex(worldflag_JP.tex) = %{tl_version}
Provides:       tex(worldflag_JollyRoger.tex) = %{tl_version}
Provides:       tex(worldflag_K.tex) = %{tl_version}
Provides:       tex(worldflag_KE.tex) = %{tl_version}
Provides:       tex(worldflag_KG.tex) = %{tl_version}
Provides:       tex(worldflag_KH.tex) = %{tl_version}
Provides:       tex(worldflag_KI.tex) = %{tl_version}
Provides:       tex(worldflag_KM.tex) = %{tl_version}
Provides:       tex(worldflag_KN.tex) = %{tl_version}
Provides:       tex(worldflag_KO.tex) = %{tl_version}
Provides:       tex(worldflag_KP.tex) = %{tl_version}
Provides:       tex(worldflag_KR.tex) = %{tl_version}
Provides:       tex(worldflag_KW.tex) = %{tl_version}
Provides:       tex(worldflag_KZ.tex) = %{tl_version}
Provides:       tex(worldflag_L.tex) = %{tl_version}
Provides:       tex(worldflag_LA.tex) = %{tl_version}
Provides:       tex(worldflag_LB.tex) = %{tl_version}
Provides:       tex(worldflag_LC.tex) = %{tl_version}
Provides:       tex(worldflag_LI.tex) = %{tl_version}
Provides:       tex(worldflag_LK.tex) = %{tl_version}
Provides:       tex(worldflag_LR.tex) = %{tl_version}
Provides:       tex(worldflag_LS.tex) = %{tl_version}
Provides:       tex(worldflag_LT.tex) = %{tl_version}
Provides:       tex(worldflag_LU.tex) = %{tl_version}
Provides:       tex(worldflag_LV.tex) = %{tl_version}
Provides:       tex(worldflag_LY.tex) = %{tl_version}
Provides:       tex(worldflag_M.tex) = %{tl_version}
Provides:       tex(worldflag_MA.tex) = %{tl_version}
Provides:       tex(worldflag_MC.tex) = %{tl_version}
Provides:       tex(worldflag_MD.tex) = %{tl_version}
Provides:       tex(worldflag_ME.tex) = %{tl_version}
Provides:       tex(worldflag_MG.tex) = %{tl_version}
Provides:       tex(worldflag_MH.tex) = %{tl_version}
Provides:       tex(worldflag_MK.tex) = %{tl_version}
Provides:       tex(worldflag_ML.tex) = %{tl_version}
Provides:       tex(worldflag_MM.tex) = %{tl_version}
Provides:       tex(worldflag_MN.tex) = %{tl_version}
Provides:       tex(worldflag_MR.tex) = %{tl_version}
Provides:       tex(worldflag_MT.tex) = %{tl_version}
Provides:       tex(worldflag_MU.tex) = %{tl_version}
Provides:       tex(worldflag_MV.tex) = %{tl_version}
Provides:       tex(worldflag_MW.tex) = %{tl_version}
Provides:       tex(worldflag_MX.tex) = %{tl_version}
Provides:       tex(worldflag_MY.tex) = %{tl_version}
Provides:       tex(worldflag_MZ.tex) = %{tl_version}
Provides:       tex(worldflag_N.tex) = %{tl_version}
Provides:       tex(worldflag_NA.tex) = %{tl_version}
Provides:       tex(worldflag_NATO.tex) = %{tl_version}
Provides:       tex(worldflag_NE.tex) = %{tl_version}
Provides:       tex(worldflag_NG.tex) = %{tl_version}
Provides:       tex(worldflag_NI.tex) = %{tl_version}
Provides:       tex(worldflag_NL.tex) = %{tl_version}
Provides:       tex(worldflag_NO.tex) = %{tl_version}
Provides:       tex(worldflag_NP.tex) = %{tl_version}
Provides:       tex(worldflag_NR.tex) = %{tl_version}
Provides:       tex(worldflag_NU.tex) = %{tl_version}
Provides:       tex(worldflag_NZ.tex) = %{tl_version}
Provides:       tex(worldflag_O.tex) = %{tl_version}
Provides:       tex(worldflag_OM.tex) = %{tl_version}
Provides:       tex(worldflag_Olympics.tex) = %{tl_version}
Provides:       tex(worldflag_P.tex) = %{tl_version}
Provides:       tex(worldflag_PA.tex) = %{tl_version}
Provides:       tex(worldflag_PE.tex) = %{tl_version}
Provides:       tex(worldflag_PG.tex) = %{tl_version}
Provides:       tex(worldflag_PH.tex) = %{tl_version}
Provides:       tex(worldflag_PK.tex) = %{tl_version}
Provides:       tex(worldflag_PL.tex) = %{tl_version}
Provides:       tex(worldflag_PR.tex) = %{tl_version}
Provides:       tex(worldflag_PS.tex) = %{tl_version}
Provides:       tex(worldflag_PT.tex) = %{tl_version}
Provides:       tex(worldflag_PW.tex) = %{tl_version}
Provides:       tex(worldflag_PY.tex) = %{tl_version}
Provides:       tex(worldflag_Q.tex) = %{tl_version}
Provides:       tex(worldflag_QA.tex) = %{tl_version}
Provides:       tex(worldflag_R.tex) = %{tl_version}
Provides:       tex(worldflag_RE.tex) = %{tl_version}
Provides:       tex(worldflag_RO.tex) = %{tl_version}
Provides:       tex(worldflag_RS.tex) = %{tl_version}
Provides:       tex(worldflag_RU.tex) = %{tl_version}
Provides:       tex(worldflag_RW.tex) = %{tl_version}
Provides:       tex(worldflag_Rainbow.tex) = %{tl_version}
Provides:       tex(worldflag_RedCrescent.tex) = %{tl_version}
Provides:       tex(worldflag_RedCross.tex) = %{tl_version}
Provides:       tex(worldflag_RedCrystal.tex) = %{tl_version}
Provides:       tex(worldflag_S.tex) = %{tl_version}
Provides:       tex(worldflag_SA.tex) = %{tl_version}
Provides:       tex(worldflag_SB.tex) = %{tl_version}
Provides:       tex(worldflag_SC.tex) = %{tl_version}
Provides:       tex(worldflag_SD.tex) = %{tl_version}
Provides:       tex(worldflag_SE.tex) = %{tl_version}
Provides:       tex(worldflag_SG.tex) = %{tl_version}
Provides:       tex(worldflag_SI.tex) = %{tl_version}
Provides:       tex(worldflag_SK.tex) = %{tl_version}
Provides:       tex(worldflag_SL.tex) = %{tl_version}
Provides:       tex(worldflag_SM.tex) = %{tl_version}
Provides:       tex(worldflag_SN.tex) = %{tl_version}
Provides:       tex(worldflag_SO.tex) = %{tl_version}
Provides:       tex(worldflag_SR.tex) = %{tl_version}
Provides:       tex(worldflag_SS.tex) = %{tl_version}
Provides:       tex(worldflag_ST.tex) = %{tl_version}
Provides:       tex(worldflag_SU.tex) = %{tl_version}
Provides:       tex(worldflag_SV.tex) = %{tl_version}
Provides:       tex(worldflag_SY.tex) = %{tl_version}
Provides:       tex(worldflag_SZ.tex) = %{tl_version}
Provides:       tex(worldflag_Saba.tex) = %{tl_version}
Provides:       tex(worldflag_Somaliland.tex) = %{tl_version}
Provides:       tex(worldflag_StEustasius.tex) = %{tl_version}
Provides:       tex(worldflag_T.tex) = %{tl_version}
Provides:       tex(worldflag_TD.tex) = %{tl_version}
Provides:       tex(worldflag_TG.tex) = %{tl_version}
Provides:       tex(worldflag_TH.tex) = %{tl_version}
Provides:       tex(worldflag_TJ.tex) = %{tl_version}
Provides:       tex(worldflag_TL.tex) = %{tl_version}
Provides:       tex(worldflag_TM.tex) = %{tl_version}
Provides:       tex(worldflag_TN.tex) = %{tl_version}
Provides:       tex(worldflag_TO.tex) = %{tl_version}
Provides:       tex(worldflag_TR.tex) = %{tl_version}
Provides:       tex(worldflag_TT.tex) = %{tl_version}
Provides:       tex(worldflag_TV.tex) = %{tl_version}
Provides:       tex(worldflag_TW.tex) = %{tl_version}
Provides:       tex(worldflag_TZ.tex) = %{tl_version}
Provides:       tex(worldflag_Tibet.tex) = %{tl_version}
Provides:       tex(worldflag_Transnistria.tex) = %{tl_version}
Provides:       tex(worldflag_U.tex) = %{tl_version}
Provides:       tex(worldflag_UA.tex) = %{tl_version}
Provides:       tex(worldflag_UG.tex) = %{tl_version}
Provides:       tex(worldflag_UNESCO.tex) = %{tl_version}
Provides:       tex(worldflag_UNO.tex) = %{tl_version}
Provides:       tex(worldflag_US.tex) = %{tl_version}
Provides:       tex(worldflag_UY.tex) = %{tl_version}
Provides:       tex(worldflag_UZ.tex) = %{tl_version}
Provides:       tex(worldflag_V.tex) = %{tl_version}
Provides:       tex(worldflag_VA.tex) = %{tl_version}
Provides:       tex(worldflag_VC.tex) = %{tl_version}
Provides:       tex(worldflag_VE.tex) = %{tl_version}
Provides:       tex(worldflag_VN.tex) = %{tl_version}
Provides:       tex(worldflag_VU.tex) = %{tl_version}
Provides:       tex(worldflag_W.tex) = %{tl_version}
Provides:       tex(worldflag_WB.tex) = %{tl_version}
Provides:       tex(worldflag_WHO.tex) = %{tl_version}
Provides:       tex(worldflag_WS.tex) = %{tl_version}
Provides:       tex(worldflag_X.tex) = %{tl_version}
Provides:       tex(worldflag_Y.tex) = %{tl_version}
Provides:       tex(worldflag_YE.tex) = %{tl_version}
Provides:       tex(worldflag_Z.tex) = %{tl_version}
Provides:       tex(worldflag_ZA.tex) = %{tl_version}
Provides:       tex(worldflag_ZM.tex) = %{tl_version}
Provides:       tex(worldflag_ZW.tex) = %{tl_version}
Provides:       tex(worldflags.sty) = %{tl_version}

%description -n texlive-worldflags
This is a package for drawing flags using TikZ. Currently the national flags of
all independent nations are included, additionally some other flags of various
organizations. A flag can be drawn ... as a single TikZ-picture within ordinary
text, as a picture element within a TikZ-picture. The appearance of a flag
(size, frame etc.) can be adapted using optional parameters.

%package -n texlive-xistercian
Summary:        Cistercian numerals in LaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(expkv-opt.sty)
Requires:       tex(pgf.sty)
Provides:       tex(xistercian.sty) = %{tl_version}

%description -n texlive-xistercian
This package allows you to use Cistercian numerals in LaTeX. The glyphs are
created using PGF and to a certain degree configurable. You can use Cistercian
numerals as page numbers using \pagenumbering{cistercian}. The two main macros
are: \cistercian{<counter>} formats the LaTeX2e counter as a Cistercian
numeral, \cisterciannum{<integer>} formats the integer (given as a string) as a
Cistercian numeral.

%package -n texlive-xpicture
Summary:        Extensions of LaTeX picture drawing
Version:        svn28770
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calculus.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(xpicture.sty) = %{tl_version}

%description -n texlive-xpicture
The package extends the facilities of the pict2e and the curve2e packages,
providing extra reference frames, conic section curves, graphs of elementary
functions and other parametric curves.

%package -n texlive-xypic
Summary:        Flexible diagramming macros
Version:        svn61719
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifpdf.sty)
Provides:       tex(xy.sty) = %{tl_version}
Provides:       tex(xy.tex) = %{tl_version}
Provides:       tex(xy16textures.tex) = %{tl_version}
Provides:       tex(xy17oztex.tex) = %{tl_version}
Provides:       tex(xy2cell.tex) = %{tl_version}
Provides:       tex(xyall.tex) = %{tl_version}
Provides:       tex(xyarc.tex) = %{tl_version}
Provides:       tex(xyarrow.tex) = %{tl_version}
Provides:       tex(xybarr.tex) = %{tl_version}
Provides:       tex(xycmactex.tex) = %{tl_version}
Provides:       tex(xycmtip.tex) = %{tl_version}
Provides:       tex(xycolor.tex) = %{tl_version}
Provides:       tex(xycrayon.tex) = %{tl_version}
Provides:       tex(xycurve.tex) = %{tl_version}
Provides:       tex(xydummy.tex) = %{tl_version}
Provides:       tex(xydvidrv.tex) = %{tl_version}
Provides:       tex(xydvips.tex) = %{tl_version}
Provides:       tex(xydvitops.tex) = %{tl_version}
Provides:       tex(xyemtex.tex) = %{tl_version}
Provides:       tex(xyframe.tex) = %{tl_version}
Provides:       tex(xygraph.tex) = %{tl_version}
Provides:       tex(xyidioms.tex) = %{tl_version}
Provides:       tex(xyimport.tex) = %{tl_version}
Provides:       tex(xyknot.tex) = %{tl_version}
Provides:       tex(xyline.tex) = %{tl_version}
Provides:       tex(xymatrix.tex) = %{tl_version}
Provides:       tex(xymovie.tex) = %{tl_version}
Provides:       tex(xynecula.tex) = %{tl_version}
Provides:       tex(xyoztex.tex) = %{tl_version}
Provides:       tex(xypdf-co.tex) = %{tl_version}
Provides:       tex(xypdf-cu.tex) = %{tl_version}
Provides:       tex(xypdf-fr.tex) = %{tl_version}
Provides:       tex(xypdf-li.tex) = %{tl_version}
Provides:       tex(xypdf-ro.tex) = %{tl_version}
Provides:       tex(xypdf.tex) = %{tl_version}
Provides:       tex(xypic.sty) = %{tl_version}
Provides:       tex(xypic.tex) = %{tl_version}
Provides:       tex(xypicture.tex) = %{tl_version}
Provides:       tex(xypoly.tex) = %{tl_version}
Provides:       tex(xyps-c.tex) = %{tl_version}
Provides:       tex(xyps-col.tex) = %{tl_version}
Provides:       tex(xyps-f.tex) = %{tl_version}
Provides:       tex(xyps-l.tex) = %{tl_version}
Provides:       tex(xyps-pro.tex) = %{tl_version}
Provides:       tex(xyps-ps.tex) = %{tl_version}
Provides:       tex(xyps-r.tex) = %{tl_version}
Provides:       tex(xyps-s.tex) = %{tl_version}
Provides:       tex(xyps-t.tex) = %{tl_version}
Provides:       tex(xyps.tex) = %{tl_version}
Provides:       tex(xypsdict.tex) = %{tl_version}
Provides:       tex(xypspatt.tex) = %{tl_version}
Provides:       tex(xyrecat.tex) = %{tl_version}
Provides:       tex(xyrotate.tex) = %{tl_version}
Provides:       tex(xysmart.tex) = %{tl_version}
Provides:       tex(xytextures.tex) = %{tl_version}
Provides:       tex(xytile.tex) = %{tl_version}
Provides:       tex(xytips.tex) = %{tl_version}
Provides:       tex(xytp-f.tex) = %{tl_version}
Provides:       tex(xytpic.tex) = %{tl_version}
Provides:       tex(xyv2.tex) = %{tl_version}
Provides:       tex(xyweb.tex) = %{tl_version}
Provides:       tex(xyxdvi.tex) = %{tl_version}

%description -n texlive-xypic
A package for typesetting a variety of graphs and diagrams with TeX. Xy-pic
works with most formats (including LaTeX, AMS-LaTeX, AMS-TeX, and plain TeX).
The distribution includes Michael Barr's diag package, which was previously
distributed stand-alone.


%prep
# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE2} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE3} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE4} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE5} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE6} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE7} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE8} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE9} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE10} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE11} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE12} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE13} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE14} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE15} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE16} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE17} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE18} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE19} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE20} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE21} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE22} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE23} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE24} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE25} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE26} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE27} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE28} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE29} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE30} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE31} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE32} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE33} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE34} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE35} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE36} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE37} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE38} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE39} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE41} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE42} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE43} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE44} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE45} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE46} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE47} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE48} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE49} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE50} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE51} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE52} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE53} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE54} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE55} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE56} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE57} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE58} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE59} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE60} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE61} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE62} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE63} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE64} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE65} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE66} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE67} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE68} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE69} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE70} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE71} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE72} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE73} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE74} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE75} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE76} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE77} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE78} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE79} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE80} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE81} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE82} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE83} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE84} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE85} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE86} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE87} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE88} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE89} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE90} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE91} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE92} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE93} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE94} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE95} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE96} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE97} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE98} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE99} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE100} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE101} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE102} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE103} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE104} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE105} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE106} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE107} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE108} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE109} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE110} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE111} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE112} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE113} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE114} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE115} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE116} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE117} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE118} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE119} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE120} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE121} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE122} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE123} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE124} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE125} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE126} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE127} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE128} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE129} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE130} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE131} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE132} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE133} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE134} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE135} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE136} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE137} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE138} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE139} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE140} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE141} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE142} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE143} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE144} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE145} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE146} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE147} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE148} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE149} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE150} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE151} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE152} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE153} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE154} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE155} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE156} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE157} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE158} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE159} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE160} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE161} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE162} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE163} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE164} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE165} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE166} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE167} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE168} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE169} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE170} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE171} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE172} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE173} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE174} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE175} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE176} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE177} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE178} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE179} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE180} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE181} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE182} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE183} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE184} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE185} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE186} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE187} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE188} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE189} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE190} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE191} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE192} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE193} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE194} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE195} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE196} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE197} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE198} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE199} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE200} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE201} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE202} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE203} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE204} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE205} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE206} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE207} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE208} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE209} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE210} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE211} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE212} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE213} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE214} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE215} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE216} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE217} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE218} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE219} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE220} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE221} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE222} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE223} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE224} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE225} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE226} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE227} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE228} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE229} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE230} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE231} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE232} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE233} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE234} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE235} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE236} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE237} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE238} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE239} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE240} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE241} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE242} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE243} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE244} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE245} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE246} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE247} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE248} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE249} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE250} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE251} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE252} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE253} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE254} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE255} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE256} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE257} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE258} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE259} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE260} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE261} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE262} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE263} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE264} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE265} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE266} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE267} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE268} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE269} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE270} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE271} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE272} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE273} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE274} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE275} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE276} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE277} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE278} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE279} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE280} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE281} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE282} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE283} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE284} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE285} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE286} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE287} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE288} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE289} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE290} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE291} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE292} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE293} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE294} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE295} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE296} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE297} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE298} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE299} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE300} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE301} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE302} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE303} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE304} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE305} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE306} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE307} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE308} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE309} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE310} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE311} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE312} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE313} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE314} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE315} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE316} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE317} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE318} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE319} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE320} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE321} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE322} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE323} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE324} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE325} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE326} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE327} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE328} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE329} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE330} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE331} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE332} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE333} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE334} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE335} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE336} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE337} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE338} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE339} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE340} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE341} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE342} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE343} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE344} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE345} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE346} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE347} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE348} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE349} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE350} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE351} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE352} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE353} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE354} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE355} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE356} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE357} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE358} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE359} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE360} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE361} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE362} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE363} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE364} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE365} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE366} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE367} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE368} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE369} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE370} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE371} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE372} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE373} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE374} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE375} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE376} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE377} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE378} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE379} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE380} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE381} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE382} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE383} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE384} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE385} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE386} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE387} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE388} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE389} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE390} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE391} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE392} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE393} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE394} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE395} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE396} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE397} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE398} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE399} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE400} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE401} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE402} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE403} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE404} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE405} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE406} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE407} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE408} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE409} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE410} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE411} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE412} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE413} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE414} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE415} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE416} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE417} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE418} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE419} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE420} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE421} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE422} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE423} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE424} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE425} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE426} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE427} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE428} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE429} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE430} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE431} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE432} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE433} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE434} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE435} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE436} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE437} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE438} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE439} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE440} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE441} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE442} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE443} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE444} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE445} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE446} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE447} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE448} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE449} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE450} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE451} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE452} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE453} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE454} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE455} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE456} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE457} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE458} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE459} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE460} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE461} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE462} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE463} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE464} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE465} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE466} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE467} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE468} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE469} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE470} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE471} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE472} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE473} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE474} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE475} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE476} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE477} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE478} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE479} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE480} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE481} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE482} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE483} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE484} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE485} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE486} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE487} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE488} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE489} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE490} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE491} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE492} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE493} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE494} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE495} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE496} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE497} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE498} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE499} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE500} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE501} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE502} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE503} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE504} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE505} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE506} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE507} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE508} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE509} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE510} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE511} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE512} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE513} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE514} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE515} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE516} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE517} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE518} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE519} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE520} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE521} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE522} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE523} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE524} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE525} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE526} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE527} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE528} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE529} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE530} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE531} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE532} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE533} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE534} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE535} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE536} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE537} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE538} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE539} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE540} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE541} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE542} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE543} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE544} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE545} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE546} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE547} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Compile Python bytecode
%py_byte_compile %{python3} %{buildroot}%{_texmf_main}/scripts/latex-make
%py_byte_compile %{python3} %{buildroot}%{_texmf_main}/scripts/pgfplots

# Main collection metapackage (empty)
%files

%files -n texlive-adigraph
%license mit.txt
%{_texmf_main}/tex/latex/adigraph/
%doc %{_texmf_main}/doc/latex/adigraph/

%files -n texlive-aobs-tikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/aobs-tikz/
%doc %{_texmf_main}/doc/latex/aobs-tikz/

%files -n texlive-askmaps
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/askmaps/
%doc %{_texmf_main}/doc/latex/askmaps/

%files -n texlive-asyfig
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/asyfig/
%doc %{_texmf_main}/doc/latex/asyfig/

%files -n texlive-asypictureb
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/asypictureb/
%doc %{_texmf_main}/doc/latex/asypictureb/

%files -n texlive-autoarea
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/autoarea/
%doc %{_texmf_main}/doc/latex/autoarea/

%files -n texlive-bardiag
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bardiag/
%doc %{_texmf_main}/doc/latex/bardiag/

%files -n texlive-beamerswitch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/beamerswitch/
%doc %{_texmf_main}/doc/latex/beamerswitch/

%files -n texlive-binarytree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/binarytree/
%doc %{_texmf_main}/doc/latex/binarytree/

%files -n texlive-blochsphere
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/blochsphere/
%doc %{_texmf_main}/doc/latex/blochsphere/

%files -n texlive-bloques
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bloques/
%doc %{_texmf_main}/doc/latex/bloques/

%files -n texlive-blox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/blox/
%doc %{_texmf_main}/doc/latex/blox/

%files -n texlive-bodegraph
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bodegraph/
%doc %{_texmf_main}/doc/latex/bodegraph/

%files -n texlive-bondgraph
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bondgraph/
%doc %{_texmf_main}/doc/latex/bondgraph/

%files -n texlive-bondgraphs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bondgraphs/
%doc %{_texmf_main}/doc/latex/bondgraphs/

%files -n texlive-bootstrapicons
%license mit.txt
%{_texmf_main}/tex/latex/bootstrapicons/
%doc %{_texmf_main}/doc/latex/bootstrapicons/

%files -n texlive-braids
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/braids/
%doc %{_texmf_main}/doc/latex/braids/

%files -n texlive-bxeepic
%license mit.txt
%{_texmf_main}/tex/latex/bxeepic/
%doc %{_texmf_main}/doc/latex/bxeepic/

%files -n texlive-byo-twemojis
%license cc-by-4.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/byo-twemojis/
%doc %{_texmf_main}/doc/latex/byo-twemojis/

%files -n texlive-byrne
%license gpl3.txt
%{_texmf_main}/metapost/byrne/
%{_texmf_main}/tex/latex/byrne/
%doc %{_texmf_main}/doc/metapost/byrne/

%files -n texlive-callouts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/callouts/
%doc %{_texmf_main}/doc/latex/callouts/

%files -n texlive-callouts-box
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/callouts-box/
%doc %{_texmf_main}/doc/latex/callouts-box/

%files -n texlive-celtic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/celtic/
%doc %{_texmf_main}/doc/latex/celtic/

%files -n texlive-chemfig
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/chemfig/
%doc %{_texmf_main}/doc/generic/chemfig/

%files -n texlive-circuit-macros
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/circuit-macros/
%doc %{_texmf_main}/doc/latex/circuit-macros/

%files -n texlive-circuitikz
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/circuitikz/
%{_texmf_main}/tex/latex/circuitikz/
%doc %{_texmf_main}/doc/context/third/
%doc %{_texmf_main}/doc/generic/circuitikz/
%doc %{_texmf_main}/doc/latex/circuitikz/

%files -n texlive-circularglyphs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/circularglyphs/
%doc %{_texmf_main}/doc/latex/circularglyphs/

%files -n texlive-coffeestains
%license pd.txt
%{_texmf_main}/tex/latex/coffeestains/
%doc %{_texmf_main}/doc/latex/coffeestains/

%files -n texlive-coloredbelts
%license lppl1.3c.txt
%license other-free.txt
%{_texmf_main}/tex/latex/coloredbelts/
%doc %{_texmf_main}/doc/latex/coloredbelts/

%files -n texlive-combinedgraphics
%license gpl2.txt
%{_texmf_main}/tex/latex/combinedgraphics/
%doc %{_texmf_main}/doc/latex/combinedgraphics/

%files -n texlive-curve
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/curve/
%doc %{_texmf_main}/doc/latex/curve/

%files -n texlive-curve2e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/curve2e/
%doc %{_texmf_main}/doc/latex/curve2e/

%files -n texlive-curves
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/curves/
%doc %{_texmf_main}/doc/latex/curves/

%files -n texlive-dcpic
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/dcpic/
%doc %{_texmf_main}/doc/generic/dcpic/

%files -n texlive-diagmac2
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/diagmac2/
%doc %{_texmf_main}/doc/latex/diagmac2/

%files -n texlive-ditaa
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ditaa/
%doc %{_texmf_main}/doc/latex/ditaa/

%files -n texlive-doc-pictex
%doc %{_texmf_main}/doc/generic/doc-pictex/

%files -n texlive-dot2texi
%license gpl2.txt
%{_texmf_main}/tex/latex/dot2texi/
%doc %{_texmf_main}/doc/latex/dot2texi/

%files -n texlive-dottex
%license gpl2.txt
%{_texmf_main}/tex/latex/dottex/
%doc %{_texmf_main}/doc/latex/dottex/

%files -n texlive-dpcircling
%license mit.txt
%{_texmf_main}/tex/latex/dpcircling/
%doc %{_texmf_main}/doc/latex/dpcircling/

%files -n texlive-dratex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/dratex/
%doc %{_texmf_main}/doc/generic/dratex/

%files -n texlive-drs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/drs/
%doc %{_texmf_main}/doc/latex/drs/

%files -n texlive-duotenzor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/duotenzor/
%doc %{_texmf_main}/doc/latex/duotenzor/

%files -n texlive-dynkin-diagrams
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dynkin-diagrams/
%doc %{_texmf_main}/doc/latex/dynkin-diagrams/

%files -n texlive-ecgdraw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ecgdraw/
%doc %{_texmf_main}/doc/latex/ecgdraw/

%files -n texlive-eepic
%license pd.txt
%{_texmf_main}/tex/latex/eepic/
%doc %{_texmf_main}/doc/latex/eepic/

%files -n texlive-egpeirce
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/egpeirce/
%doc %{_texmf_main}/doc/latex/egpeirce/

%files -n texlive-ellipse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ellipse/
%doc %{_texmf_main}/doc/latex/ellipse/

%files -n texlive-endofproofwd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/endofproofwd/
%doc %{_texmf_main}/doc/latex/endofproofwd/

%files -n texlive-epspdfconversion
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/epspdfconversion/
%doc %{_texmf_main}/doc/latex/epspdfconversion/

%files -n texlive-esk
%license gpl2.txt
%{_texmf_main}/tex/latex/esk/
%doc %{_texmf_main}/doc/latex/esk/

%files -n texlive-euflag
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/euflag/
%doc %{_texmf_main}/doc/latex/euflag/

%files -n texlive-fadingimage
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fadingimage/
%doc %{_texmf_main}/doc/latex/fadingimage/

%files -n texlive-fast-diagram
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fast-diagram/
%doc %{_texmf_main}/doc/latex/fast-diagram/

%files -n texlive-fenetrecas
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fenetrecas/
%doc %{_texmf_main}/doc/latex/fenetrecas/

%files -n texlive-figchild
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/figchild/
%doc %{_texmf_main}/doc/latex/figchild/

%files -n texlive-figput
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/figput/
%doc %{_texmf_main}/doc/latex/figput/

%files -n texlive-fitbox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fitbox/
%doc %{_texmf_main}/doc/latex/fitbox/

%files -n texlive-flowchart
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/flowchart/
%doc %{_texmf_main}/doc/latex/flowchart/

%files -n texlive-forest
%license lppl1.3c.txt
%{_texmf_main}/makeindex/forest/
%{_texmf_main}/tex/latex/forest/
%doc %{_texmf_main}/doc/latex/forest/

%files -n texlive-forest-ext
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/forest-ext/
%doc %{_texmf_main}/doc/latex/forest-ext/

%files -n texlive-genealogytree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/genealogytree/
%doc %{_texmf_main}/doc/latex/genealogytree/

%files -n texlive-gincltex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gincltex/
%doc %{_texmf_main}/doc/latex/gincltex/

%files -n texlive-gnuplottex
%license gpl2.txt
%{_texmf_main}/tex/latex/gnuplottex/
%doc %{_texmf_main}/doc/latex/gnuplottex/

%files -n texlive-gradientframe
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gradientframe/
%doc %{_texmf_main}/doc/latex/gradientframe/

%files -n texlive-grafcet
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/grafcet/
%doc %{_texmf_main}/doc/latex/grafcet/

%files -n texlive-graph35
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/graph35/
%doc %{_texmf_main}/doc/latex/graph35/

%files -n texlive-graphicxpsd
%license mit.txt
%{_texmf_main}/tex/latex/graphicxpsd/
%doc %{_texmf_main}/doc/latex/graphicxpsd/

%files -n texlive-graphviz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/graphviz/
%doc %{_texmf_main}/doc/latex/graphviz/

%files -n texlive-gtrlib-largetrees
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gtrlib-largetrees/
%doc %{_texmf_main}/doc/latex/gtrlib-largetrees/

%files -n texlive-harveyballs
%license gpl3.txt
%{_texmf_main}/tex/latex/harveyballs/
%doc %{_texmf_main}/doc/latex/harveyballs/

%files -n texlive-here
%license pd.txt
%{_texmf_main}/tex/latex/here/
%doc %{_texmf_main}/doc/latex/here/

%files -n texlive-hf-tikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hf-tikz/
%doc %{_texmf_main}/doc/latex/hf-tikz/

%files -n texlive-hobby
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hobby/
%doc %{_texmf_main}/doc/latex/hobby/

%files -n texlive-hvfloat
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hvfloat/
%doc %{_texmf_main}/doc/latex/hvfloat/

%files -n texlive-istgame
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/istgame/
%doc %{_texmf_main}/doc/latex/istgame/

%files -n texlive-kblocks
%license mit.txt
%{_texmf_main}/tex/latex/kblocks/
%doc %{_texmf_main}/doc/latex/kblocks/

%files -n texlive-keisennote
%license mit.txt
%{_texmf_main}/tex/latex/keisennote/
%doc %{_texmf_main}/doc/latex/keisennote/

%files -n texlive-kinematikz
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/tex/latex/kinematikz/
%doc %{_texmf_main}/doc/latex/kinematikz/

%files -n texlive-knitting
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/knitting/
%{_texmf_main}/fonts/map/dvips/knitting/
%{_texmf_main}/fonts/source/public/knitting/
%{_texmf_main}/fonts/tfm/public/knitting/
%{_texmf_main}/fonts/type1/public/knitting/
%{_texmf_main}/tex/latex/knitting/
%{_texmf_main}/tex/plain/knitting/
%doc %{_texmf_main}/doc/fonts/knitting/

%files -n texlive-knittingpattern
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/knittingpattern/
%doc %{_texmf_main}/doc/latex/knittingpattern/

%files -n texlive-ladder
%license mit.txt
%{_texmf_main}/tex/latex/ladder/
%doc %{_texmf_main}/doc/latex/ladder/

%files -n texlive-lapdf
%license gpl2.txt
%{_texmf_main}/tex/latex/lapdf/
%doc %{_texmf_main}/doc/latex/lapdf/

%files -n texlive-latex-make
%license gpl2.txt
%{_texmf_main}/scripts/latex-make/
%{_texmf_main}/tex/latex/latex-make/
%doc %{_texmf_main}/doc/support/latex-make/

%files -n texlive-liftarm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/liftarm/
%doc %{_texmf_main}/doc/latex/liftarm/

%files -n texlive-lpic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lpic/
%doc %{_texmf_main}/doc/latex/lpic/

%files -n texlive-lroundrect
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lroundrect/
%doc %{_texmf_main}/doc/latex/lroundrect/

%files -n texlive-lua-tikz3dtools
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lua-tikz3dtools/
%doc %{_texmf_main}/doc/latex/lua-tikz3dtools/

%files -n texlive-luamesh
%license lppl1.3c.txt
%{_texmf_main}/metapost/luamesh/
%{_texmf_main}/scripts/luamesh/
%{_texmf_main}/tex/lualatex/luamesh/
%doc %{_texmf_main}/doc/lualatex/luamesh/

%files -n texlive-luasseq
%license lppl1.3c.txt
%{_texmf_main}/scripts/luasseq/
%{_texmf_main}/tex/lualatex/luasseq/
%doc %{_texmf_main}/doc/lualatex/luasseq/

%files -n texlive-lucide-icons
%license lppl1.3c.txt
%license other-free.txt
%{_texmf_main}/tex/latex/lucide-icons/
%doc %{_texmf_main}/doc/latex/lucide-icons/

%files -n texlive-maker
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/maker/
%doc %{_texmf_main}/doc/latex/maker/

%files -n texlive-makeshape
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/makeshape/
%doc %{_texmf_main}/doc/latex/makeshape/

%files -n texlive-maritime
%license mit.txt
%{_texmf_main}/tex/latex/maritime/
%doc %{_texmf_main}/doc/latex/maritime/

%files -n texlive-mercatormap
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mercatormap/
%doc %{_texmf_main}/doc/latex/mercatormap/

%files -n texlive-milsymb
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/milsymb/
%doc %{_texmf_main}/doc/latex/milsymb/

%files -n texlive-miniplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/miniplot/
%doc %{_texmf_main}/doc/latex/miniplot/

%files -n texlive-modiagram
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/modiagram/
%doc %{_texmf_main}/doc/latex/modiagram/

%files -n texlive-neuralnetwork
%license gpl2.txt
%{_texmf_main}/tex/latex/neuralnetwork/
%doc %{_texmf_main}/doc/latex/neuralnetwork/

%files -n texlive-nl-interval
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nl-interval/
%doc %{_texmf_main}/doc/latex/nl-interval/

%files -n texlive-nndraw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nndraw/
%doc %{_texmf_main}/doc/latex/nndraw/

%files -n texlive-numericplots
%license gpl3.txt
%{_texmf_main}/tex/latex/numericplots/
%doc %{_texmf_main}/doc/latex/numericplots/

%files -n texlive-open-everyday-symbols
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/open-everyday-symbols/
%doc %{_texmf_main}/doc/latex/open-everyday-symbols/

%files -n texlive-openmoji
%license lppl1.3c.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/openmoji/
%doc %{_texmf_main}/doc/latex/openmoji/

%files -n texlive-optikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/optikz/
%doc %{_texmf_main}/doc/latex/optikz/

%files -n texlive-outilsgeomtikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/outilsgeomtikz/
%doc %{_texmf_main}/doc/latex/outilsgeomtikz/

%files -n texlive-papiergurvan
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/papiergurvan/
%doc %{_texmf_main}/doc/latex/papiergurvan/

%files -n texlive-pb-diagram
%license gpl2.txt
%{_texmf_main}/tex/latex/pb-diagram/
%doc %{_texmf_main}/doc/latex/pb-diagram/

%files -n texlive-pgf
%license lppl1.3c.txt
%license gpl2.txt
%license fdl.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/pgf/
%{_texmf_main}/tex/latex/pgf/
%{_texmf_main}/tex/plain/pgf/
%doc %{_texmf_main}/doc/generic/pgf/

%files -n texlive-pgf-blur
%license lppl1.3c.txt
%license pd.txt
%{_texmf_main}/tex/latex/pgf-blur/
%doc %{_texmf_main}/doc/latex/pgf-blur/

%files -n texlive-pgf-interference
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-interference/
%doc %{_texmf_main}/doc/latex/pgf-interference/

%files -n texlive-pgf-periodictable
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-periodictable/
%doc %{_texmf_main}/doc/latex/pgf-periodictable/

%files -n texlive-pgf-pie
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-pie/
%doc %{_texmf_main}/doc/latex/pgf-pie/

%files -n texlive-pgf-soroban
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-soroban/
%doc %{_texmf_main}/doc/latex/pgf-soroban/

%files -n texlive-pgf-spectra
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-spectra/
%doc %{_texmf_main}/doc/latex/pgf-spectra/

%files -n texlive-pgf-umlcd
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-umlcd/
%doc %{_texmf_main}/doc/latex/pgf-umlcd/

%files -n texlive-pgf-umlsd
%license gpl2.txt
%{_texmf_main}/tex/latex/pgf-umlsd/
%doc %{_texmf_main}/doc/latex/pgf-umlsd/

%files -n texlive-pgfgantt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgfgantt/
%doc %{_texmf_main}/doc/latex/pgfgantt/

%files -n texlive-pgfkeysearch
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/tex/latex/pgfkeysearch/
%doc %{_texmf_main}/doc/latex/pgfkeysearch/

%files -n texlive-pgfkeyx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgfkeyx/
%doc %{_texmf_main}/doc/latex/pgfkeyx/

%files -n texlive-pgfmolbio
%license lppl1.3c.txt
%{_texmf_main}/scripts/pgfmolbio/
%{_texmf_main}/tex/lualatex/pgfmolbio/
%doc %{_texmf_main}/doc/lualatex/pgfmolbio/

%files -n texlive-pgfmorepages
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgfmorepages/
%doc %{_texmf_main}/doc/latex/pgfmorepages/

%files -n texlive-pgfopts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgfopts/
%doc %{_texmf_main}/doc/latex/pgfopts/

%files -n texlive-pgfornament
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pgfornament/
%{_texmf_main}/tex/latex/pgfornament/
%doc %{_texmf_main}/doc/latex/pgfornament/

%files -n texlive-pgfplots
%license gpl3.txt
%{_texmf_main}/scripts/pgfplots/
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/pgfplots/
%{_texmf_main}/tex/latex/pgfplots/
%{_texmf_main}/tex/plain/pgfplots/
%doc %{_texmf_main}/doc/context/third/
%doc %{_texmf_main}/doc/generic/pgfplots/
%doc %{_texmf_main}/doc/latex/pgfplots/
%doc %{_texmf_main}/doc/plain/pgfplots/

%files -n texlive-pgfplotsthemebeamer
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgfplotsthemebeamer/
%doc %{_texmf_main}/doc/latex/pgfplotsthemebeamer/

%files -n texlive-picinpar
%license gpl2.txt
%{_texmf_main}/tex/latex/picinpar/
%doc %{_texmf_main}/doc/latex/picinpar/

%files -n texlive-pict2e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pict2e/
%doc %{_texmf_main}/doc/latex/pict2e/

%files -n texlive-pictex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pictex/
%doc %{_texmf_main}/doc/generic/pictex/

%files -n texlive-pictex2
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pictex2/

%files -n texlive-pictochrono
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pictochrono/
%doc %{_texmf_main}/doc/latex/pictochrono/

%files -n texlive-pinlabel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pinlabel/
%doc %{_texmf_main}/doc/latex/pinlabel/

%files -n texlive-pixelart
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pixelart/
%doc %{_texmf_main}/doc/latex/pixelart/

%files -n texlive-pixelarttikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pixelarttikz/
%doc %{_texmf_main}/doc/latex/pixelarttikz/

%files -n texlive-pmgraph
%license gpl2.txt
%{_texmf_main}/tex/latex/pmgraph/
%doc %{_texmf_main}/doc/latex/pmgraph/

%files -n texlive-polyhedra
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/polyhedra/
%doc %{_texmf_main}/doc/latex/polyhedra/

%files -n texlive-polyomino
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/polyomino/
%doc %{_texmf_main}/doc/latex/polyomino/

%files -n texlive-postage
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/postage/
%doc %{_texmf_main}/doc/latex/postage/

%files -n texlive-postit
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/postit/
%doc %{_texmf_main}/doc/latex/postit/

%files -n texlive-prerex
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/prerex/
%doc %{_texmf_main}/doc/latex/prerex/
%doc %{_texmf_main}/doc/man/man5/

%files -n texlive-prisma-flow-diagram
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/prisma-flow-diagram/
%doc %{_texmf_main}/doc/latex/prisma-flow-diagram/

%files -n texlive-productbox
%{_texmf_main}/tex/latex/productbox/
%doc %{_texmf_main}/doc/latex/productbox/

%files -n texlive-ptolemaicastronomy
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ptolemaicastronomy/
%doc %{_texmf_main}/doc/latex/ptolemaicastronomy/

%files -n texlive-puyotikz
%license mit.txt
%{_texmf_main}/scripts/puyotikz/
%{_texmf_main}/tex/latex/puyotikz/
%doc %{_texmf_main}/doc/latex/puyotikz/

%files -n texlive-pxpgfmark
%license mit.txt
%{_texmf_main}/tex/latex/pxpgfmark/
%doc %{_texmf_main}/doc/latex/pxpgfmark/

%files -n texlive-pxpic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pxpic/
%doc %{_texmf_main}/doc/latex/pxpic/

%files -n texlive-qcircuit
%license gpl2.txt
%{_texmf_main}/tex/latex/qcircuit/
%doc %{_texmf_main}/doc/latex/qcircuit/

%files -n texlive-qrcode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qrcode/
%doc %{_texmf_main}/doc/latex/qrcode/

%files -n texlive-qrcodetikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qrcodetikz/
%doc %{_texmf_main}/doc/latex/qrcodetikz/

%files -n texlive-randbild
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/randbild/
%doc %{_texmf_main}/doc/latex/randbild/

%files -n texlive-randomwalk
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/randomwalk/
%doc %{_texmf_main}/doc/latex/randomwalk/

%files -n texlive-realhats
%license mit.txt
%{_texmf_main}/tex/latex/realhats/
%doc %{_texmf_main}/doc/latex/realhats/

%files -n texlive-reotex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/reotex/
%doc %{_texmf_main}/doc/latex/reotex/

%files -n texlive-robotarm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/robotarm/
%doc %{_texmf_main}/doc/latex/robotarm/

%files -n texlive-rviewport
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rviewport/
%doc %{_texmf_main}/doc/latex/rviewport/

%files -n texlive-sa-tikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sa-tikz/
%doc %{_texmf_main}/doc/latex/sa-tikz/

%files -n texlive-sacsymb
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sacsymb/
%doc %{_texmf_main}/doc/latex/sacsymb/

%files -n texlive-schemabloc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/schemabloc/
%doc %{_texmf_main}/doc/latex/schemabloc/

%files -n texlive-scratch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scratch/
%doc %{_texmf_main}/doc/latex/scratch/

%files -n texlive-scratch3
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scratch3/
%doc %{_texmf_main}/doc/latex/scratch3/

%files -n texlive-scsnowman
%license bsd2.txt
%{_texmf_main}/tex/latex/scsnowman/
%doc %{_texmf_main}/doc/latex/scsnowman/

%files -n texlive-setdeck
%license gpl3.txt
%{_texmf_main}/tex/latex/setdeck/
%doc %{_texmf_main}/doc/latex/setdeck/

%files -n texlive-signchart
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/signchart/
%doc %{_texmf_main}/doc/latex/signchart/

%files -n texlive-simplenodes
%license mit.txt
%{_texmf_main}/tex/latex/simplenodes/
%doc %{_texmf_main}/doc/latex/simplenodes/

%files -n texlive-simpleoptics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/simpleoptics/
%doc %{_texmf_main}/doc/latex/simpleoptics/

%files -n texlive-smartdiagram
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/smartdiagram/
%doc %{_texmf_main}/doc/latex/smartdiagram/

%files -n texlive-spath3
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/spath3/
%doc %{_texmf_main}/doc/latex/spath3/

%files -n texlive-spectralsequences
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/spectralsequences/
%doc %{_texmf_main}/doc/latex/spectralsequences/

%files -n texlive-strands
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/strands/
%doc %{_texmf_main}/doc/latex/strands/

%files -n texlive-sunpath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sunpath/
%doc %{_texmf_main}/doc/latex/sunpath/

%files -n texlive-swimgraf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/swimgraf/
%doc %{_texmf_main}/doc/latex/swimgraf/

%files -n texlive-syntaxdi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/syntaxdi/
%doc %{_texmf_main}/doc/latex/syntaxdi/

%files -n texlive-table-fct
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/table-fct/
%doc %{_texmf_main}/doc/latex/table-fct/

%files -n texlive-texdraw
%license cc-by-4.txt
%{_texmf_main}/tex/generic/texdraw/
%doc %{_texmf_main}/doc/info/
%doc %{_texmf_main}/doc/support/texdraw/

%files -n texlive-ticollege
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ticollege/
%doc %{_texmf_main}/doc/latex/ticollege/

%files -n texlive-tikz-3dplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-3dplot/
%doc %{_texmf_main}/doc/latex/tikz-3dplot/

%files -n texlive-tikz-among-us
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-among-us/
%doc %{_texmf_main}/doc/latex/tikz-among-us/

%files -n texlive-tikz-bagua
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-bagua/
%doc %{_texmf_main}/doc/latex/tikz-bagua/

%files -n texlive-tikz-bayesnet
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-bayesnet/
%doc %{_texmf_main}/doc/latex/tikz-bayesnet/

%files -n texlive-tikz-bbox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-bbox/
%doc %{_texmf_main}/doc/latex/tikz-bbox/

%files -n texlive-tikz-bpmn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-bpmn/
%doc %{_texmf_main}/doc/latex/tikz-bpmn/

%files -n texlive-tikz-cd
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/tikz-cd/
%{_texmf_main}/tex/latex/tikz-cd/
%doc %{_texmf_main}/doc/latex/tikz-cd/

%files -n texlive-tikz-cookingsymbols
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-cookingsymbols/
%doc %{_texmf_main}/doc/latex/tikz-cookingsymbols/

%files -n texlive-tikz-decofonts
%license lppl1.3c.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/tikz-decofonts/
%doc %{_texmf_main}/doc/latex/tikz-decofonts/

%files -n texlive-tikz-dependency
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/tex/latex/tikz-dependency/
%doc %{_texmf_main}/doc/latex/tikz-dependency/

%files -n texlive-tikz-dimline
%license other-free.txt
%{_texmf_main}/tex/latex/tikz-dimline/
%doc %{_texmf_main}/doc/latex/tikz-dimline/

%files -n texlive-tikz-ext
%license fdl.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/tikz-ext/
%{_texmf_main}/tex/latex/tikz-ext/
%{_texmf_main}/tex/plain/tikz-ext/
%doc %{_texmf_main}/doc/latex/tikz-ext/

%files -n texlive-tikz-feynhand
%license gpl3.txt
%{_texmf_main}/tex/latex/tikz-feynhand/
%doc %{_texmf_main}/doc/latex/tikz-feynhand/

%files -n texlive-tikz-feynman
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-feynman/
%doc %{_texmf_main}/doc/latex/tikz-feynman/

%files -n texlive-tikz-imagelabels
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-imagelabels/
%doc %{_texmf_main}/doc/latex/tikz-imagelabels/

%files -n texlive-tikz-inet
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-inet/
%doc %{_texmf_main}/doc/latex/tikz-inet/

%files -n texlive-tikz-kalender
%{_texmf_main}/tex/latex/tikz-kalender/
%doc %{_texmf_main}/doc/latex/tikz-kalender/

%files -n texlive-tikz-karnaugh
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-karnaugh/
%doc %{_texmf_main}/doc/latex/tikz-karnaugh/

%files -n texlive-tikz-ladder
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-ladder/
%doc %{_texmf_main}/doc/latex/tikz-ladder/

%files -n texlive-tikz-lake-fig
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-lake-fig/
%doc %{_texmf_main}/doc/latex/tikz-lake-fig/

%files -n texlive-tikz-layers
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-layers/
%doc %{_texmf_main}/doc/latex/tikz-layers/

%files -n texlive-tikz-mirror-lens
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-mirror-lens/
%doc %{_texmf_main}/doc/latex/tikz-mirror-lens/

%files -n texlive-tikz-nef
%license mit.txt
%{_texmf_main}/tex/latex/tikz-nef/
%doc %{_texmf_main}/doc/latex/tikz-nef/

%files -n texlive-tikz-network
%license gpl3.txt
%{_texmf_main}/tex/latex/tikz-network/
%doc %{_texmf_main}/doc/latex/tikz-network/

%files -n texlive-tikz-nfold
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-nfold/
%doc %{_texmf_main}/doc/latex/tikz-nfold/

%files -n texlive-tikz-opm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-opm/
%doc %{_texmf_main}/doc/latex/tikz-opm/

%files -n texlive-tikz-optics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-optics/
%doc %{_texmf_main}/doc/latex/tikz-optics/

%files -n texlive-tikz-osci
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-osci/
%doc %{_texmf_main}/doc/latex/tikz-osci/

%files -n texlive-tikz-page
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-page/
%doc %{_texmf_main}/doc/latex/tikz-page/

%files -n texlive-tikz-palattice
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-palattice/
%doc %{_texmf_main}/doc/latex/tikz-palattice/

%files -n texlive-tikz-planets
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/tikz-planets/
%doc %{_texmf_main}/doc/latex/tikz-planets/

%files -n texlive-tikz-qtree
%license gpl2.txt
%{_texmf_main}/tex/latex/tikz-qtree/
%doc %{_texmf_main}/doc/latex/tikz-qtree/

%files -n texlive-tikz-relay
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-relay/
%doc %{_texmf_main}/doc/latex/tikz-relay/

%files -n texlive-tikz-sfc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-sfc/
%doc %{_texmf_main}/doc/latex/tikz-sfc/

%files -n texlive-tikz-shields
%license gpl3.txt
%{_texmf_main}/tex/latex/tikz-shields/
%doc %{_texmf_main}/doc/latex/tikz-shields/

%files -n texlive-tikz-swigs
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/tex/latex/tikz-swigs/
%doc %{_texmf_main}/doc/latex/tikz-swigs/

%files -n texlive-tikz-timing
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-timing/
%doc %{_texmf_main}/doc/latex/tikz-timing/

%files -n texlive-tikz-trackschematic
%license other-free.txt
%{_texmf_main}/tex/latex/tikz-trackschematic/
%doc %{_texmf_main}/doc/latex/tikz-trackschematic/

%files -n texlive-tikz-truchet
%license mit.txt
%{_texmf_main}/tex/latex/tikz-truchet/
%doc %{_texmf_main}/doc/latex/tikz-truchet/

%files -n texlive-tikz2d-fr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz2d-fr/
%doc %{_texmf_main}/doc/latex/tikz2d-fr/

%files -n texlive-tikz3d-fr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz3d-fr/
%doc %{_texmf_main}/doc/latex/tikz3d-fr/

%files -n texlive-tikzbrickfigurines
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzbrickfigurines/
%doc %{_texmf_main}/doc/latex/tikzbrickfigurines/

%files -n texlive-tikzbricks
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzbricks/
%doc %{_texmf_main}/doc/latex/tikzbricks/

%files -n texlive-tikzcalendarnotes
%license lppl1.3c.txt
%license gpl3.txt
%{_texmf_main}/tex/latex/tikzcalendarnotes/
%doc %{_texmf_main}/doc/latex/tikzcalendarnotes/

%files -n texlive-tikzcodeblocks
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzcodeblocks/
%doc %{_texmf_main}/doc/latex/tikzcodeblocks/

%files -n texlive-tikzdotncross
%license lppl1.3c.txt
%license gpl3.txt
%{_texmf_main}/tex/latex/tikzdotncross/
%doc %{_texmf_main}/doc/latex/tikzdotncross/

%files -n texlive-tikzducks
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzducks/
%doc %{_texmf_main}/doc/latex/tikzducks/

%files -n texlive-tikzfill
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzfill/
%doc %{_texmf_main}/doc/latex/tikzfill/

%files -n texlive-tikzfxgraph
%license lppl1.3c.txt
%license gpl3.txt
%{_texmf_main}/tex/latex/tikzfxgraph/
%doc %{_texmf_main}/doc/latex/tikzfxgraph/

%files -n texlive-tikzinclude
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzinclude/
%doc %{_texmf_main}/doc/latex/tikzinclude/

%files -n texlive-tikzlings
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzlings/
%doc %{_texmf_main}/doc/latex/tikzlings/

%files -n texlive-tikzmark
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzmark/
%doc %{_texmf_main}/doc/latex/tikzmark/

%files -n texlive-tikzmarmots
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzmarmots/
%doc %{_texmf_main}/doc/latex/tikzmarmots/

%files -n texlive-tikzorbital
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzorbital/
%doc %{_texmf_main}/doc/latex/tikzorbital/

%files -n texlive-tikzpackets
%license mit.txt
%{_texmf_main}/tex/latex/tikzpackets/
%doc %{_texmf_main}/doc/latex/tikzpackets/

%files -n texlive-tikzpagenodes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzpagenodes/
%doc %{_texmf_main}/doc/latex/tikzpagenodes/

%files -n texlive-tikzpeople
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzpeople/
%doc %{_texmf_main}/doc/latex/tikzpeople/

%files -n texlive-tikzpfeile
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzpfeile/
%doc %{_texmf_main}/doc/latex/tikzpfeile/

%files -n texlive-tikzpingus
%license gpl3.txt
%{_texmf_main}/tex/latex/tikzpingus/
%doc %{_texmf_main}/doc/latex/tikzpingus/

%files -n texlive-tikzposter
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzposter/
%doc %{_texmf_main}/doc/latex/tikzposter/

%files -n texlive-tikzquads
%license lppl1.3c.txt
%license other-free.txt
%{_texmf_main}/tex/latex/tikzquads/
%doc %{_texmf_main}/doc/latex/tikzquads/

%files -n texlive-tikzquests
%license lppl1.3c.txt
%license gpl3.txt
%{_texmf_main}/tex/latex/tikzquests/
%doc %{_texmf_main}/doc/latex/tikzquests/

%files -n texlive-tikzscale
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzscale/
%doc %{_texmf_main}/doc/latex/tikzscale/

%files -n texlive-tikzsymbols
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzsymbols/
%doc %{_texmf_main}/doc/latex/tikzsymbols/

%files -n texlive-tikzviolinplots
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikzviolinplots/
%doc %{_texmf_main}/doc/latex/tikzviolinplots/

%files -n texlive-tile-graphic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tile-graphic/
%doc %{_texmf_main}/doc/latex/tile-graphic/

%files -n texlive-tilings
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tilings/
%doc %{_texmf_main}/doc/latex/tilings/

%files -n texlive-timechart
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/timechart/
%doc %{_texmf_main}/doc/latex/timechart/

%files -n texlive-timing-diagrams
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/timing-diagrams/
%doc %{_texmf_main}/doc/latex/timing-diagrams/

%files -n texlive-tipfr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tipfr/
%doc %{_texmf_main}/doc/latex/tipfr/

%files -n texlive-tkz-base
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-base/
%doc %{_texmf_main}/doc/latex/tkz-base/

%files -n texlive-tkz-berge
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-berge/
%doc %{_texmf_main}/doc/latex/tkz-berge/

%files -n texlive-tkz-bernoulli
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-bernoulli/
%doc %{_texmf_main}/doc/latex/tkz-bernoulli/

%files -n texlive-tkz-doc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-doc/
%doc %{_texmf_main}/doc/latex/tkz-doc/

%files -n texlive-tkz-elements
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-elements/
%doc %{_texmf_main}/doc/latex/tkz-elements/

%files -n texlive-tkz-euclide
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-euclide/
%doc %{_texmf_main}/doc/latex/tkz-euclide/

%files -n texlive-tkz-fct
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-fct/
%doc %{_texmf_main}/doc/latex/tkz-fct/

%files -n texlive-tkz-graph
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-graph/
%doc %{_texmf_main}/doc/latex/tkz-graph/

%files -n texlive-tkz-grapheur
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-grapheur/
%doc %{_texmf_main}/doc/latex/tkz-grapheur/

%files -n texlive-tkz-orm
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-orm/
%doc %{_texmf_main}/doc/latex/tkz-orm/

%files -n texlive-tkz-tab
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-tab/
%doc %{_texmf_main}/doc/latex/tkz-tab/

%files -n texlive-tkzexample
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkzexample/
%doc %{_texmf_main}/doc/latex/tkzexample/

%files -n texlive-tonevalue
%license apache2.txt
%{_texmf_main}/tex/latex/tonevalue/
%doc %{_texmf_main}/doc/latex/tonevalue/

%files -n texlive-tqft
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tqft/
%doc %{_texmf_main}/doc/latex/tqft/

%files -n texlive-tsemlines
%license pd.txt
%{_texmf_main}/tex/latex/tsemlines/

%files -n texlive-tufte-latex
%license apache2.txt
%{_texmf_main}/bibtex/bst/tufte-latex/
%{_texmf_main}/tex/latex/tufte-latex/
%doc %{_texmf_main}/doc/latex/tufte-latex/

%files -n texlive-twemojis
%license lppl1.3c.txt
%license cc-by-4.txt
%{_texmf_main}/tex/latex/twemojis/
%doc %{_texmf_main}/doc/latex/twemojis/

%files -n texlive-tzplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tzplot/
%doc %{_texmf_main}/doc/latex/tzplot/

%files -n texlive-utfsym
%license cc-zero-1.txt
%{_texmf_main}/tex/latex/utfsym/
%doc %{_texmf_main}/doc/latex/utfsym/

%files -n texlive-vectorlogos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/vectorlogos/
%doc %{_texmf_main}/doc/latex/vectorlogos/

%files -n texlive-venndiagram
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/venndiagram/
%doc %{_texmf_main}/doc/latex/venndiagram/

%files -n texlive-vexillology
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/vexillology/
%doc %{_texmf_main}/doc/latex/vexillology/

%files -n texlive-visualpstricks
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/visualpstricks/

%files -n texlive-wheelchart
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/wheelchart/
%doc %{_texmf_main}/doc/latex/wheelchart/

%files -n texlive-wordcloud
%license lppl1.3c.txt
%{_texmf_main}/metapost/wordcloud/
%{_texmf_main}/tex/latex/wordcloud/
%doc %{_texmf_main}/doc/metapost/wordcloud/

%files -n texlive-worldflags
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/worldflags/
%doc %{_texmf_main}/doc/latex/worldflags/

%files -n texlive-xistercian
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xistercian/
%doc %{_texmf_main}/doc/latex/xistercian/

%files -n texlive-xpicture
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xpicture/
%doc %{_texmf_main}/doc/latex/xpicture/

%files -n texlive-xypic
%license gpl2.txt
%{_texmf_main}/dvips/xypic/
%{_texmf_main}/fonts/afm/public/xypic/
%{_texmf_main}/fonts/enc/dvips/xypic/
%{_texmf_main}/fonts/map/dvips/xypic/
%{_texmf_main}/fonts/source/public/xypic/
%{_texmf_main}/fonts/tfm/public/xypic/
%{_texmf_main}/fonts/type1/public/xypic/
%{_texmf_main}/tex/generic/xypic/
%doc %{_texmf_main}/doc/generic/xypic/

%changelog
* Wed Feb 04 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77389-1
- Update to svn77389, fix descriptions, licensing

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75936-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75936-1
- Update to TeX Live 2025
