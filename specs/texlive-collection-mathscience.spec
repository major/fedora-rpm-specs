%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-mathscience
Epoch:          12
Version:        svn77507
Release:        1%{?dist}
Summary:        Mathematics, natural sciences, computer science packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-mathscience.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/12many.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/12many.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/accents.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/accents.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aiplans.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aiplans.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alg.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alg.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algobox.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algobox.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithm2e.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithm2e.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithmicx.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithmicx.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithms.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algorithms.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algpseudocodex.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algpseudocodex.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algxpar.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algxpar.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aligned-overset.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aligned-overset.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscdx.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscdx.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/annotate-equations.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/annotate-equations.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apxproof.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apxproof.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aspen.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aspen.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atableau.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atableau.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autobreak.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autobreak.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/backnaur.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/backnaur.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/begriff.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/begriff.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/binomexp.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/binomexp.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biocon.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biocon.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitpattern.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitpattern.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bodeplot.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bodeplot.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bohr.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bohr.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/boldtensors.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/boldtensors.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bosisio.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bosisio.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bpchem.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bpchem.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bracealign.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bracealign.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bropd.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bropd.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/broydensolve.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/broydensolve.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bussproofs.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bussproofs.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bussproofs-colorful.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bussproofs-colorful.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bussproofs-extra.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bussproofs-extra.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bytefield.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bytefield.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calculation.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calculation.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cartonaugh.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cartonaugh.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascade.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascade.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/causets.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/causets.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ccfonts.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ccfonts.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ccool.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ccool.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemarrow.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemarrow.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemcompounds.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemcompounds.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemcono.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemcono.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemexec.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemexec.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemformula.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemformula.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemformula-ru.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemformula-ru.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemgreek.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemgreek.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemmacros.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemmacros.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemnum.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemnum.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemobabel.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemobabel.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemplants.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemplants.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemschemex.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemschemex.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemsec.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemsec.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemstyle.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chemstyle.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clrscode.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clrscode.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clrscode3e.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clrscode3e.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/codeanatomy.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/codeanatomy.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coloredtheorem.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coloredtheorem.doc.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/commath.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/commath.doc.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/commutative-diagrams.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/commutative-diagrams.doc.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/complexity.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/complexity.doc.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/complexpolylongdiv.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/complexpolylongdiv.doc.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/computational-complexity.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/computational-complexity.doc.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concmath.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concmath.doc.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concrete.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concrete.doc.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/conteq.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/conteq.doc.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cora-macs.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cora-macs.doc.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/correctmathalign.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/correctmathalign.doc.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cryptocode.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cryptocode.doc.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cs-techrep.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cs-techrep.doc.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csassignments.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csassignments.doc.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csthm.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csthm.doc.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cvss.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cvss.doc.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/decision-table.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/decision-table.doc.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/delim.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/delim.doc.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/delimseasy.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/delimseasy.doc.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/delimset.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/delimset.doc.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/derivative.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/derivative.doc.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/diffcoeff.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/diffcoeff.doc.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/digiconfigs.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/digiconfigs.doc.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dijkstra.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dijkstra.doc.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/domaincoloring.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/domaincoloring.doc.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drawmatrix.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drawmatrix.doc.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drawstack.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drawstack.doc.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dyntree.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dyntree.doc.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/easing.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/easing.doc.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebproof.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebproof.doc.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/econometrics.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/econometrics.doc.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eltex.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eltex.doc.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emf.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emf.doc.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/endiagram.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/endiagram.doc.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/engtlc.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/engtlc.doc.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqexpl.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqexpl.doc.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqnarray.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqnarray.doc.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqnlines.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqnlines.doc.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqnnumwarn.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eqnnumwarn.doc.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euclidean-lattice.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euclidean-lattice.doc.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euclideangeometry.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euclideangeometry.doc.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/extarrows.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/extarrows.doc.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/extpfeil.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/extpfeil.doc.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/faktor.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/faktor.doc.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fascicules.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fascicules.doc.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fitch.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fitch.doc.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixdif.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixdif.doc.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixmath.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixmath.doc.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fnspe.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fnspe.doc.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fodot.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fodot.doc.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/formal-grammar.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/formal-grammar.doc.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fouridx.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fouridx.doc.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/freealign.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/freealign.doc.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/freemath.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/freemath.doc.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/functan.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/functan.doc.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/galois.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/galois.doc.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gastex.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gastex.doc.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gene-logic.tar.xz
Source231:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gene-logic.doc.tar.xz
Source232:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ghsystem.tar.xz
Source233:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ghsystem.doc.tar.xz
Source234:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/glosmathtools.tar.xz
Source235:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/glosmathtools.doc.tar.xz
Source236:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gotoh.tar.xz
Source237:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gotoh.doc.tar.xz
Source238:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grundgesetze.tar.xz
Source239:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grundgesetze.doc.tar.xz
Source240:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gu.tar.xz
Source241:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gu.doc.tar.xz
Source242:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.tar.xz
Source243:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.doc.tar.xz
Source244:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-graphic.tar.xz
Source245:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-graphic.doc.tar.xz
Source246:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-reference.tar.xz
Source247:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-reference.doc.tar.xz
Source248:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepnames.tar.xz
Source249:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepnames.doc.tar.xz
Source250:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepparticles.tar.xz
Source251:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepparticles.doc.tar.xz
Source252:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepthesis.tar.xz
Source253:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepthesis.doc.tar.xz
Source254:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepunits.tar.xz
Source255:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hepunits.doc.tar.xz
Source256:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hideproofs.tar.xz
Source257:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hideproofs.doc.tar.xz
Source258:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibrackets.tar.xz
Source259:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibrackets.doc.tar.xz
Source260:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/includernw.tar.xz
Source261:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/includernw.doc.tar.xz
Source262:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interval.tar.xz
Source263:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interval.doc.tar.xz
Source264:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intexgral.tar.xz
Source265:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intexgral.doc.tar.xz
Source266:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ionumbers.tar.xz
Source267:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ionumbers.doc.tar.xz
Source268:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/isomath.tar.xz
Source269:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/isomath.doc.tar.xz
Source270:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/isphysicalmath.tar.xz
Source271:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/isphysicalmath.doc.tar.xz
Source272:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jkmath.tar.xz
Source273:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jkmath.doc.tar.xz
Source274:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jupynotex.tar.xz
Source275:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jupynotex.doc.tar.xz
Source276:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/karnaugh.tar.xz
Source277:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/karnaugh.doc.tar.xz
Source278:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/karnaugh-map.tar.xz
Source279:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/karnaugh-map.doc.tar.xz
Source280:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/karnaughmap.tar.xz
Source281:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/karnaughmap.doc.tar.xz
Source282:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/keytheorems.tar.xz
Source283:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/keytheorems.doc.tar.xz
Source284:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvmap.tar.xz
Source285:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvmap.doc.tar.xz
Source286:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letterswitharrows.tar.xz
Source287:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letterswitharrows.doc.tar.xz
Source288:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lie-hasse.tar.xz
Source289:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lie-hasse.doc.tar.xz
Source290:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linearregression.tar.xz
Source291:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linearregression.doc.tar.xz
Source292:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linkedthm.tar.xz
Source293:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linkedthm.doc.tar.xz
Source294:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logicproof.tar.xz
Source295:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logicproof.doc.tar.xz
Source296:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logictools.tar.xz
Source297:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logictools.doc.tar.xz
Source298:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/longdivision.tar.xz
Source299:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/longdivision.doc.tar.xz
Source300:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lpform.tar.xz
Source301:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lpform.doc.tar.xz
Source302:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lplfitch.tar.xz
Source303:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lplfitch.doc.tar.xz
Source304:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lstbayes.tar.xz
Source305:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lstbayes.doc.tar.xz
Source306:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-regression.tar.xz
Source307:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-regression.doc.tar.xz
Source308:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luanumint.tar.xz
Source309:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luanumint.doc.tar.xz
Source310:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/math-operator.tar.xz
Source311:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/math-operator.doc.tar.xz
Source312:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathcommand.tar.xz
Source313:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathcommand.doc.tar.xz
Source314:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathcomp.tar.xz
Source315:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathcomp.doc.tar.xz
Source316:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathfixs.tar.xz
Source317:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathfixs.doc.tar.xz
Source318:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathlig.tar.xz
Source319:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpartir.tar.xz
Source320:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpartir.doc.tar.xz
Source321:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpunctspace.tar.xz
Source322:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpunctspace.doc.tar.xz
Source323:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathsemantics.tar.xz
Source324:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathsemantics.doc.tar.xz
Source325:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matlab-prettifier.tar.xz
Source326:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matlab-prettifier.doc.tar.xz
Source327:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matrix-skeleton.tar.xz
Source328:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matrix-skeleton.doc.tar.xz
Source329:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mattens.tar.xz
Source330:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mattens.doc.tar.xz
Source331:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mecaso.tar.xz
Source332:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mecaso.doc.tar.xz
Source333:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/medmath.tar.xz
Source334:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/medmath.doc.tar.xz
Source335:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/membranecomputing.tar.xz
Source336:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/membranecomputing.doc.tar.xz
Source337:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memorygraphs.tar.xz
Source338:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memorygraphs.doc.tar.xz
Source339:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/messagepassing.tar.xz
Source340:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/messagepassing.doc.tar.xz
Source341:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mgltex.tar.xz
Source342:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mgltex.doc.tar.xz
Source343:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mhchem.tar.xz
Source344:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mhchem.doc.tar.xz
Source345:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mhequ.tar.xz
Source346:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mhequ.doc.tar.xz
Source347:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/miller.tar.xz
Source348:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/miller.doc.tar.xz
Source349:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mismath.tar.xz
Source350:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mismath.doc.tar.xz
Source351:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/moremath.tar.xz
Source352:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/moremath.doc.tar.xz
Source353:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multiobjective.tar.xz
Source354:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multiobjective.doc.tar.xz
Source355:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/naive-ebnf.tar.xz
Source356:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/naive-ebnf.doc.tar.xz
Source357:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/namedtensor.tar.xz
Source358:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/namedtensor.doc.tar.xz
Source359:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/natded.tar.xz
Source360:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/natded.doc.tar.xz
Source361:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nath.tar.xz
Source362:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nath.doc.tar.xz
Source363:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nchairx.tar.xz
Source364:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nchairx.doc.tar.xz
Source365:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nicematrix.tar.xz
Source366:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nicematrix.doc.tar.xz
Source367:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nuc.tar.xz
Source368:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nuc.doc.tar.xz
Source369:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nucleardata.tar.xz
Source370:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nucleardata.doc.tar.xz
Source371:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numbersets.tar.xz
Source372:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numbersets.doc.tar.xz
Source373:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numerica.tar.xz
Source374:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numerica.doc.tar.xz
Source375:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numerica-plus.tar.xz
Source376:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numerica-plus.doc.tar.xz
Source377:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numerica-tables.tar.xz
Source378:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numerica-tables.doc.tar.xz
Source379:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/objectz.tar.xz
Source380:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/objectz.doc.tar.xz
Source381:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/odesandpdes.tar.xz
Source382:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/odesandpdes.doc.tar.xz
Source383:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oplotsymbl.tar.xz
Source384:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oplotsymbl.doc.tar.xz
Source385:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ot-tableau.tar.xz
Source386:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ot-tableau.doc.tar.xz
Source387:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oubraces.tar.xz
Source388:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oubraces.doc.tar.xz
Source389:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overarrows.tar.xz
Source390:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overarrows.doc.tar.xz
Source391:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pascaltriangle.tar.xz
Source392:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pascaltriangle.doc.tar.xz
Source393:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/perfectcut.tar.xz
Source394:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/perfectcut.doc.tar.xz
Source395:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pfdicons.tar.xz
Source396:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pfdicons.doc.tar.xz
Source397:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physconst.tar.xz
Source398:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physconst.doc.tar.xz
Source399:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics.tar.xz
Source400:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics.doc.tar.xz
Source401:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics-patch.tar.xz
Source402:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics-patch.doc.tar.xz
Source403:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics2.tar.xz
Source404:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics2.doc.tar.xz
Source405:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics3.tar.xz
Source406:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physics3.doc.tar.xz
Source407:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physunits.tar.xz
Source408:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/physunits.doc.tar.xz
Source409:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pinoutikz.tar.xz
Source410:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pinoutikz.doc.tar.xz
Source411:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pm-isomath.tar.xz
Source412:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pm-isomath.doc.tar.xz
Source413:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmdraw.tar.xz
Source414:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmdraw.doc.tar.xz
Source415:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polexpr.tar.xz
Source416:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polexpr.doc.tar.xz
Source417:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prftree.tar.xz
Source418:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prftree.doc.tar.xz
Source419:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/principia.tar.xz
Source420:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/principia.doc.tar.xz
Source421:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proba.tar.xz
Source422:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proba.doc.tar.xz
Source423:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proof-at-the-end.tar.xz
Source424:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proof-at-the-end.doc.tar.xz
Source425:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prooftrees.tar.xz
Source426:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prooftrees.doc.tar.xz
Source427:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pseudo.tar.xz
Source428:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pseudo.doc.tar.xz
Source429:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pseudocode.tar.xz
Source430:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pseudocode.doc.tar.xz
Source431:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pythonhighlight.tar.xz
Source432:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pythonhighlight.doc.tar.xz
Source433:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qsharp.tar.xz
Source434:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qsharp.doc.tar.xz
Source435:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantikz.tar.xz
Source436:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantikz.doc.tar.xz
Source437:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantum-chemistry-bonn.tar.xz
Source438:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantum-chemistry-bonn.doc.tar.xz
Source439:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantumcubemodel.tar.xz
Source440:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantumcubemodel.doc.tar.xz
Source441:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quickreaction.tar.xz
Source442:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quickreaction.doc.tar.xz
Source443:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quiver.tar.xz
Source444:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quiver.doc.tar.xz
Source445:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qworld.tar.xz
Source446:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qworld.doc.tar.xz
Source447:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rank-2-roots.tar.xz
Source448:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rank-2-roots.doc.tar.xz
Source449:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rbt-mathnotes.tar.xz
Source450:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rbt-mathnotes.doc.tar.xz
Source451:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rec-thy.tar.xz
Source452:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rec-thy.doc.tar.xz
Source453:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reptheorem.tar.xz
Source454:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reptheorem.doc.tar.xz
Source455:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resolsysteme.tar.xz
Source456:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resolsysteme.doc.tar.xz
Source457:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rest-api.tar.xz
Source458:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rest-api.doc.tar.xz
Source459:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revquantum.tar.xz
Source460:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revquantum.doc.tar.xz
Source461:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ribbonproofs.tar.xz
Source462:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ribbonproofs.doc.tar.xz
Source463:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rigidnotation.tar.xz
Source464:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rigidnotation.doc.tar.xz
Source465:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rmathbr.tar.xz
Source466:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rmathbr.doc.tar.xz
Source467:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sankey.tar.xz
Source468:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sankey.doc.tar.xz
Source469:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sasnrdisplay.tar.xz
Source470:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sasnrdisplay.doc.tar.xz
Source471:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sciposter.tar.xz
Source472:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sciposter.doc.tar.xz
Source473:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sclang-prettifier.tar.xz
Source474:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sclang-prettifier.doc.tar.xz
Source475:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scratchx.tar.xz
Source476:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scratchx.doc.tar.xz
Source477:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sesamanuel.tar.xz
Source478:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sesamanuel.doc.tar.xz
Source479:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sfg.tar.xz
Source480:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sfg.doc.tar.xz
Source481:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shuffle.tar.xz
Source482:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shuffle.doc.tar.xz
Source483:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplebnf.tar.xz
Source484:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplebnf.doc.tar.xz
Source485:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simpler-wick.tar.xz
Source486:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simpler-wick.doc.tar.xz
Source487:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simples-matrices.tar.xz
Source488:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simples-matrices.doc.tar.xz
Source489:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplewick.tar.xz
Source490:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplewick.doc.tar.xz
Source491:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sistyle.tar.xz
Source492:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sistyle.doc.tar.xz
Source493:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/siunits.tar.xz
Source494:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/siunits.doc.tar.xz
Source495:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/siunitx.tar.xz
Source496:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/siunitx.doc.tar.xz
Source497:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skmath.tar.xz
Source498:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skmath.doc.tar.xz
Source499:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spalign.tar.xz
Source500:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spalign.doc.tar.xz
Source501:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spbmark.tar.xz
Source502:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spbmark.doc.tar.xz
Source503:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stanli.tar.xz
Source504:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stanli.doc.tar.xz
Source505:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statex.tar.xz
Source506:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statex.doc.tar.xz
Source507:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statex2.tar.xz
Source508:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statex2.doc.tar.xz
Source509:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statistics.tar.xz
Source510:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statistics.doc.tar.xz
Source511:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statistik.tar.xz
Source512:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statistik.doc.tar.xz
Source513:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statmath.tar.xz
Source514:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/statmath.doc.tar.xz
Source515:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/steinmetz.tar.xz
Source516:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/steinmetz.doc.tar.xz
Source517:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stmaryrd.tar.xz
Source518:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stmaryrd.doc.tar.xz
Source519:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/string-diagrams.tar.xz
Source520:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/string-diagrams.doc.tar.xz
Source521:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/structmech.tar.xz
Source522:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/structmech.doc.tar.xz
Source523:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/struktex.tar.xz
Source524:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/struktex.doc.tar.xz
Source525:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/substances.tar.xz
Source526:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/substances.doc.tar.xz
Source527:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subsupscripts.tar.xz
Source528:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subsupscripts.doc.tar.xz
Source529:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subtext.tar.xz
Source530:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subtext.doc.tar.xz
Source531:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/susy.tar.xz
Source532:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/susy.doc.tar.xz
Source533:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/syllogism.tar.xz
Source534:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/syllogism.doc.tar.xz
Source535:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sympytexpackage.tar.xz
Source536:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sympytexpackage.doc.tar.xz
Source537:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/synproof.tar.xz
Source538:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/synproof.doc.tar.xz
Source539:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t-angles.tar.xz
Source540:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t-angles.doc.tar.xz
Source541:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tablor.tar.xz
Source542:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tablor.doc.tar.xz
Source543:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/temporal-logic.tar.xz
Source544:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/temporal-logic.doc.tar.xz
Source545:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tensind.tar.xz
Source546:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tensind.doc.tar.xz
Source547:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tensor.tar.xz
Source548:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tensor.doc.tar.xz
Source549:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tensormatrix.tar.xz
Source550:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tensormatrix.doc.tar.xz
Source551:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-ewd.tar.xz
Source552:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-ewd.doc.tar.xz
Source553:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textgreek.tar.xz
Source554:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textgreek.doc.tar.xz
Source555:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textopo.tar.xz
Source556:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textopo.doc.tar.xz
Source557:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thermodynamics.tar.xz
Source558:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thermodynamics.doc.tar.xz
Source559:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thmbox.tar.xz
Source560:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thmbox.doc.tar.xz
Source561:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thmtools.tar.xz
Source562:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thmtools.doc.tar.xz
Source563:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tiscreen.tar.xz
Source564:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tiscreen.doc.tar.xz
Source565:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-interval.tar.xz
Source566:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tkz-interval.doc.tar.xz
Source567:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turnstile.tar.xz
Source568:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turnstile.doc.tar.xz
Source569:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unitsdef.tar.xz
Source570:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unitsdef.doc.tar.xz
Source571:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/venn.tar.xz
Source572:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/venn.doc.tar.xz
Source573:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/witharrows.tar.xz
Source574:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/witharrows.doc.tar.xz
Source575:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xymtex.tar.xz
Source576:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xymtex.doc.tar.xz
Source577:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yhmath.tar.xz
Source578:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yhmath.doc.tar.xz
Source579:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/youngtab.tar.xz
Source580:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/youngtab.doc.tar.xz
Source581:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yquant.tar.xz
Source582:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yquant.doc.tar.xz
Source583:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ytableau.tar.xz
Source584:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ytableau.doc.tar.xz
Source585:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zeckendorf.tar.xz
Source586:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zeckendorf.doc.tar.xz
Source587:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zx-calculus.tar.xz
Source588:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zx-calculus.doc.tar.xz

# Patches
Patch0:         texlive-bz#1442706-python-path.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-12many
Requires:       texlive-accents
Requires:       texlive-aiplans
Requires:       texlive-alg
Requires:       texlive-algobox
Requires:       texlive-algorithm2e
Requires:       texlive-algorithmicx
Requires:       texlive-algorithms
Requires:       texlive-algpseudocodex
Requires:       texlive-algxpar
Requires:       texlive-aligned-overset
Requires:       texlive-amscdx
Requires:       texlive-amstex
Requires:       texlive-annotate-equations
Requires:       texlive-apxproof
Requires:       texlive-aspen
Requires:       texlive-atableau
Requires:       texlive-autobreak
Requires:       texlive-axodraw2
Requires:       texlive-backnaur
Requires:       texlive-begriff
Requires:       texlive-binomexp
Requires:       texlive-biocon
Requires:       texlive-bitpattern
Requires:       texlive-bodeplot
Requires:       texlive-bohr
Requires:       texlive-boldtensors
Requires:       texlive-bosisio
Requires:       texlive-bpchem
Requires:       texlive-bracealign
Requires:       texlive-bropd
Requires:       texlive-broydensolve
Requires:       texlive-bussproofs
Requires:       texlive-bussproofs-colorful
Requires:       texlive-bussproofs-extra
Requires:       texlive-bytefield
Requires:       texlive-calculation
Requires:       texlive-cartonaugh
Requires:       texlive-cascade
Requires:       texlive-causets
Requires:       texlive-ccfonts
Requires:       texlive-ccool
Requires:       texlive-chemarrow
Requires:       texlive-chemcompounds
Requires:       texlive-chemcono
Requires:       texlive-chemexec
Requires:       texlive-chemformula
Requires:       texlive-chemformula-ru
Requires:       texlive-chemgreek
Requires:       texlive-chemmacros
Requires:       texlive-chemnum
Requires:       texlive-chemobabel
Requires:       texlive-chemplants
Requires:       texlive-chemschemex
Requires:       texlive-chemsec
Requires:       texlive-chemstyle
Requires:       texlive-clrscode
Requires:       texlive-clrscode3e
Requires:       texlive-codeanatomy
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-collection-latex
Requires:       texlive-coloredtheorem
Requires:       texlive-commath
Requires:       texlive-commutative-diagrams
Requires:       texlive-complexity
Requires:       texlive-complexpolylongdiv
Requires:       texlive-computational-complexity
Requires:       texlive-concmath
Requires:       texlive-concrete
Requires:       texlive-conteq
Requires:       texlive-cora-macs
Requires:       texlive-correctmathalign
Requires:       texlive-cryptocode
Requires:       texlive-cs-techrep
Requires:       texlive-csassignments
Requires:       texlive-csthm
Requires:       texlive-cvss
Requires:       texlive-decision-table
Requires:       texlive-delim
Requires:       texlive-delimseasy
Requires:       texlive-delimset
Requires:       texlive-derivative
Requires:       texlive-diffcoeff
Requires:       texlive-digiconfigs
Requires:       texlive-dijkstra
Requires:       texlive-domaincoloring
Requires:       texlive-drawmatrix
Requires:       texlive-drawstack
Requires:       texlive-dyntree
Requires:       texlive-easing
Requires:       texlive-ebproof
Requires:       texlive-econometrics
Requires:       texlive-eltex
Requires:       texlive-emf
Requires:       texlive-endiagram
Requires:       texlive-engtlc
Requires:       texlive-eolang
Requires:       texlive-eqexpl
Requires:       texlive-eqnarray
Requires:       texlive-eqnlines
Requires:       texlive-eqnnumwarn
Requires:       texlive-euclidean-lattice
Requires:       texlive-euclideangeometry
Requires:       texlive-extarrows
Requires:       texlive-extpfeil
Requires:       texlive-faktor
Requires:       texlive-fascicules
Requires:       texlive-fitch
Requires:       texlive-fixdif
Requires:       texlive-fixmath
Requires:       texlive-fnspe
Requires:       texlive-fodot
Requires:       texlive-formal-grammar
Requires:       texlive-fouridx
Requires:       texlive-freealign
Requires:       texlive-freemath
Requires:       texlive-functan
Requires:       texlive-galois
Requires:       texlive-gastex
Requires:       texlive-gene-logic
Requires:       texlive-ghsystem
Requires:       texlive-glosmathtools
Requires:       texlive-gotoh
Requires:       texlive-grundgesetze
Requires:       texlive-gu
Requires:       texlive-helmholtz-ellis-ji-notation
# hep depends on axodraw, which is not open source. As a result, it has been omitted.
Requires:       texlive-hep-graphic
Requires:       texlive-hep-reference
Requires:       texlive-hepnames
Requires:       texlive-hepparticles
Requires:       texlive-hepthesis
Requires:       texlive-hepunits
Requires:       texlive-hideproofs
Requires:       texlive-ibrackets
Requires:       texlive-includernw
Requires:       texlive-interval
Requires:       texlive-intexgral
Requires:       texlive-ionumbers
Requires:       texlive-isomath
Requires:       texlive-isphysicalmath
Requires:       texlive-jkmath
Requires:       texlive-jupynotex
Requires:       texlive-karnaugh
Requires:       texlive-karnaugh-map
Requires:       texlive-karnaughmap
Requires:       texlive-keytheorems
Requires:       texlive-kvmap
Requires:       texlive-letterswitharrows
Requires:       texlive-lie-hasse
Requires:       texlive-linearregression
Requires:       texlive-linkedthm
Requires:       texlive-logicproof
Requires:       texlive-logictools
Requires:       texlive-longdivision
Requires:       texlive-lpform
Requires:       texlive-lplfitch
Requires:       texlive-lstbayes
Requires:       texlive-lua-regression
Requires:       texlive-luanumint
Requires:       texlive-math-operator
Requires:       texlive-mathcommand
Requires:       texlive-mathcomp
Requires:       texlive-mathfixs
Requires:       texlive-mathlig
Requires:       texlive-mathpartir
Requires:       texlive-mathpunctspace
Requires:       texlive-mathsemantics
Requires:       texlive-matlab-prettifier
Requires:       texlive-matrix-skeleton
Requires:       texlive-mattens
Requires:       texlive-mecaso
Requires:       texlive-medmath
Requires:       texlive-membranecomputing
Requires:       texlive-memorygraphs
Requires:       texlive-messagepassing
Requires:       texlive-mgltex
Requires:       texlive-mhchem
Requires:       texlive-mhequ
Requires:       texlive-miller
Requires:       texlive-mismath
Requires:       texlive-moremath
Requires:       texlive-multiobjective
Requires:       texlive-naive-ebnf
Requires:       texlive-namedtensor
Requires:       texlive-natded
Requires:       texlive-nath
Requires:       texlive-nchairx
Requires:       texlive-nicematrix
Requires:       texlive-nuc
Requires:       texlive-nucleardata
Requires:       texlive-numbersets
Requires:       texlive-numerica
Requires:       texlive-numerica-plus
Requires:       texlive-numerica-tables
Requires:       texlive-objectz
Requires:       texlive-odesandpdes
Requires:       texlive-oplotsymbl
Requires:       texlive-ot-tableau
Requires:       texlive-oubraces
Requires:       texlive-overarrows
Requires:       texlive-pascaltriangle
Requires:       texlive-perfectcut
Requires:       texlive-pfdicons
Requires:       texlive-physconst
Requires:       texlive-physics
Requires:       texlive-physics-patch
Requires:       texlive-physics2
Requires:       texlive-physics3
Requires:       texlive-physunits
Requires:       texlive-pinoutikz
Requires:       texlive-pm-isomath
Requires:       texlive-pmdraw
Requires:       texlive-polexpr
Requires:       texlive-prftree
Requires:       texlive-principia
Requires:       texlive-proba
Requires:       texlive-proof-at-the-end
Requires:       texlive-prooftrees
Requires:       texlive-pseudo
Requires:       texlive-pseudocode
Requires:       texlive-pythonhighlight
Requires:       texlive-qsharp
Requires:       texlive-quantikz
Requires:       texlive-quantum-chemistry-bonn
Requires:       texlive-quantumcubemodel
Requires:       texlive-quickreaction
Requires:       texlive-quiver
Requires:       texlive-qworld
Requires:       texlive-rank-2-roots
Requires:       texlive-rbt-mathnotes
Requires:       texlive-rec-thy
Requires:       texlive-reptheorem
Requires:       texlive-resolsysteme
Requires:       texlive-rest-api
Requires:       texlive-revquantum
Requires:       texlive-ribbonproofs
Requires:       texlive-rigidnotation
Requires:       texlive-rmathbr
Requires:       texlive-sankey
Requires:       texlive-sasnrdisplay
Requires:       texlive-sciposter
Requires:       texlive-sclang-prettifier
Requires:       texlive-scratchx
Requires:       texlive-sesamanuel
Requires:       texlive-sfg
Requires:       texlive-shuffle
Requires:       texlive-simplebnf
Requires:       texlive-simpler-wick
Requires:       texlive-simples-matrices
Requires:       texlive-simplewick
Requires:       texlive-sistyle
Requires:       texlive-siunits
Requires:       texlive-siunitx
Requires:       texlive-skmath
Requires:       texlive-spalign
Requires:       texlive-spbmark
Requires:       texlive-stanli
Requires:       texlive-statex
Requires:       texlive-statex2
Requires:       texlive-statistics
Requires:       texlive-statistik
Requires:       texlive-statmath
Requires:       texlive-steinmetz
Requires:       texlive-stmaryrd
Requires:       texlive-string-diagrams
Requires:       texlive-structmech
Requires:       texlive-struktex
Requires:       texlive-substances
Requires:       texlive-subsupscripts
Requires:       texlive-subtext
Requires:       texlive-susy
Requires:       texlive-syllogism
Requires:       texlive-sympytexpackage
Requires:       texlive-synproof
Requires:       texlive-t-angles
Requires:       texlive-tablor
Requires:       texlive-temporal-logic
Requires:       texlive-tensind
Requires:       texlive-tensor
Requires:       texlive-tensormatrix
Requires:       texlive-tex-ewd
Requires:       texlive-textgreek
Requires:       texlive-textopo
Requires:       texlive-thermodynamics
Requires:       texlive-thmbox
Requires:       texlive-thmtools
Requires:       texlive-tiscreen
Requires:       texlive-tkz-interval
Requires:       texlive-turnstile
Requires:       texlive-ulqda
Requires:       texlive-unitsdef
Requires:       texlive-venn
Requires:       texlive-witharrows
Requires:       texlive-xymtex
Requires:       texlive-yhmath
Requires:       texlive-youngtab
Requires:       texlive-yquant
Requires:       texlive-ytableau
Requires:       texlive-zeckendorf
Requires:       texlive-zx-calculus

%description
Mathematics, natural sciences, computer science packages


%package -n texlive-12many
Summary:        Generalising mathematical index sets
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(keyval.sty)
Provides:       tex(12many.sty) = %{tl_version}

%description -n texlive-12many
In the discrete branches of mathematics and the computer sciences, it will only
take some seconds before you're faced with a set like {1,...,m}. Some people
write $1\ldotp\ldotp m$, others $\{j:1\leq j\leq m\}$, and the journal you're
submitting to might want something else entirely. The 12many package provides
an interface that makes changing from one to another a one-line change.

%package -n texlive-accents
Summary:        Multiple mathematical accents
Version:        svn51497
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(accents.sty) = %{tl_version}

%description -n texlive-accents
A package for multiple accents in mathematics, with nice features concerning
the creation of accents and placement of scripts.

%package -n texlive-aiplans
Summary:        A TikZ-based library for drawing POCL plans
Version:        svn74462
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tikzlibraryaiplans.code.tex) = %{tl_version}

%description -n texlive-aiplans
This TikZ library is designed for generating diagrams related to Automated
Planning, a subdiscipline of Artificial Intelligence. It allows users to define
a "domain model" for actions, similar to PDDL and HDDL used in hierarchical
planning. The package is useful for researchers and students to create diagrams
that represent sequential action sequences or partially ordered plans,
including causal links and ordering constraints (e.g., POCL plans). It is
particularly suited for presentations and scientific publications.

%package -n texlive-alg
Summary:        LaTeX environments for typesetting algorithms
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(alg.sty) = %{tl_version}

%description -n texlive-alg
Defines two environments for typesetting algorithms in LaTeX2e. The algtab
environment is used to typeset an algorithm with automatically numbered lines.
The algorithm environment can be used to encapsulate the algtab environment
algorithm in a floating body together with a header, a caption, etc.
\listofalgorithms is defined.

%package -n texlive-algobox
Summary:        Typeset Algobox programs
Version:        svn67201
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(algobox.sty) = %{tl_version}

%description -n texlive-algobox
This LaTeX package can typeset Algobox programs almost exactly as displayed
when editing with Algobox itself, using an input syntax very similar to the
actual Algobox program text. It gives better results than Algobox's own LaTeX
export which does not look like the editor rendition, produces standalone
documents cumbersome to customize, and has arbitrary and inconsistent
differences between the input syntax and the program text. This package depends
upon the following other LaTeX packages: expl3, TikZ, environ, xparse, and
xcolor.

%package -n texlive-algorithm2e
Summary:        Floating algorithm environment with algorithmic keywords
Version:        svn44846
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(endfloat.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
Requires:       tex(tocbibind.sty)
Requires:       tex(xspace.sty)
Provides:       tex(algorithm2e.sty) = %{tl_version}

%description -n texlive-algorithm2e
Algorithm2e is an environment for writing algorithms. An algorithm becomes a
floating object (like figure, table, etc.). The package provides macros that
allow you to create different keywords, and a set of predefined key words is
provided; you can change the typography of the keywords. The package allows
vertical lines delimiting a block of instructions in an algorithm, and defines
different sorts of algorithms such as Procedure or Function; the name of these
functions may be reused in the text or in other algorithms.

%package -n texlive-algorithmicx
Summary:        The algorithmic style you always wanted
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(algc.sty) = %{tl_version}
Provides:       tex(algcompatible.sty) = %{tl_version}
Provides:       tex(algmatlab.sty) = %{tl_version}
Provides:       tex(algorithmicx.sty) = %{tl_version}
Provides:       tex(algpascal.sty) = %{tl_version}
Provides:       tex(algpseudocode.sty) = %{tl_version}

%description -n texlive-algorithmicx
Algorithmicx provides a flexible, yet easy to use, way for inserting good
looking pseudocode or source code in your papers. It has built in support for
Pseudocode, Pascal and C, and offers powerful means to create definitions for
any programming language. The user can adapt a Pseudocode style to his native
language.

%package -n texlive-algorithms
Summary:        A suite of tools for typesetting algorithms in pseudo-code
Version:        svn76389
License:        LGPL-2.1-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Provides:       tex(algorithm.sty) = %{tl_version}
Provides:       tex(algorithmic.sty) = %{tl_version}

%description -n texlive-algorithms
Consists of two environments: algorithm and algorithmic. The algorithm package
defines a floating algorithm environment designed to work with the algorithmic
style. Within an algorithmic environment a number of commands for typesetting
popular algorithmic constructs are available.

%package -n texlive-algpseudocodex
Summary:        Package for typesetting pseudocode
Version:        svn74973
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithmicx.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fifo-stack.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tabto.sty)
Requires:       tex(tikz.sty)
Requires:       tex(totcount.sty)
Requires:       tex(varwidth.sty)
Provides:       tex(algpseudocodex.sty) = %{tl_version}

%description -n texlive-algpseudocodex
This package allows typesetting pseudocode in LaTeX. It is based on
algpseudocode from the algorithmicx package and uses the same syntax, but adds
several new features and improvements. Notable features include customizable
indent guide lines and the ability to draw boxes around parts of the code for
highlighting differences. This package also has better support for long code
lines spanning several lines and improved comments.

%package -n texlive-algxpar
Summary:        Support multiple lines of pseudocode
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-algorithmicx
Requires:       texlive-algorithmicx
Requires:       texlive-amsfonts
Requires:       texlive-etoolbox
Requires:       texlive-pgf
Requires:       texlive-pgf
Requires:       texlive-pgfopts
Requires:       texlive-ragged2e
Requires:       texlive-varwidth
Requires:       texlive-xcolor
Requires:       tex(algorithmicx.sty)
Requires:       tex(algpseudocode.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(algxpar-brazilian.kw.tex) = %{tl_version}
Provides:       tex(algxpar-english.kw.tex) = %{tl_version}
Provides:       tex(algxpar.sty) = %{tl_version}

%description -n texlive-algxpar
This package extends the package algorithmicx to support long text which spans
over multiple lines.

%package -n texlive-aligned-overset
Summary:        Fix alignment at \overset or \underset
Version:        svn47290
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(xparse.sty)
Provides:       tex(aligned-overset.sty) = %{tl_version}

%description -n texlive-aligned-overset
This package allows the base character of \underset or \overset to be used as
the alignment position for the amsmath aligned math environments.

%package -n texlive-amscdx
Summary:        Enhanced commutative diagrams
Version:        svn51532
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsgen.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(amscdx.sty) = %{tl_version}

%description -n texlive-amscdx
The original amscd package provides a CD environment that emulates the
commutative diagram capabilities of AMS-TeX version 2.x. This means that only
simple rectangular diagrams are supported, with no diagonal arrows or more
exotic features. This enhancement package implements double ("fat"), dashed,
and bidirectional arrows (left-right and up-down), and color attributes for
arrows and their annotations. The restriction to rectangular geometry remains.
This nevertheless allows the drawing of a much broader class of
"commutative-diagram-like" diagrams. This update, 2.2x of 2019-07-02, fixes the
dashed-arrows parts placement bug, and adds the package option 'lyx', for use
with lyx to prevent conflict with the already loaded amscd. The packages xcolor
and graphicx are made required.

%package -n texlive-annotate-equations
Summary:        Easily annotate math equations using TikZ
Version:        svn67044
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(annotate-equations.sty) = %{tl_version}

%description -n texlive-annotate-equations
This package provides commands that make it easy to highlight terms in
equations and add annotation labels using TikZ. It should work with pdfLaTeX as
well as LuaLaTeX.

%package -n texlive-apxproof
Summary:        Proofs in appendix
Version:        svn76507
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsthm.sty)
Requires:       tex(bibunits.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(apxproof.sty) = %{tl_version}

%description -n texlive-apxproof
The package makes it easier to write articles where proofs and other material
are deferred to the appendix. The appendix material is written in the LaTeX
code along with the main text which it naturally complements, and it is
automatically deferred. The package can automatically send proofs to the
appendix, can repeat in the appendix the theorem environments stated in the
main text, can section the appendix automatically based on the sectioning of
the main text, and supports a separate bibliography for the appendix material.
It depends on the following other packages: amsthm, bibunits (if the
bibliography option is set to separate), environ, etoolbox, fancyvrb, ifthen,
and kvoptions.

%package -n texlive-aspen
Summary:        Simple crypto notation in LaTeX
Version:        svn77463
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(rcs.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(aspen.sty) = %{tl_version}

%description -n texlive-aspen
The Aspen package implements LaTeX commands closely related to what is often
called security protocol notation, standard protocol engineering notation,
standard protocol notation, or protocol narrations. Optionally, the Aspen
package also implements LaTeX commands for Burrows-Abadi-Needham logic (BAN
logic). The name Aspen can be an abbreviation for A Security Protocol
Engineering Notation, but another possible abbreviation is Anderson-inspired
Standard Protocol Engineering Notation, in memory of the late Professor Ross J.
Anderson who has meant so much for the fields of computer security, distributed
systems, and, in particular, security engineering.

%package -n texlive-atableau
Summary:        A LaTeX package for symmetric group combinatorics
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(atableau.sty) = %{tl_version}

%description -n texlive-atableau
A LaTeX package for symmetric group combinatorics, with commands for Young
diagrams, tableaux, tabloids, skew tableaux, shifted tableaux, ribbon tableaux,
multitableaux, abacuses. These commands are intended to be easy to use and easy
to customise. In particular, TikZ styling can be added to the components of
these diagrams and common conventions and idioms are supported using a
key-value interface. All diagrams can be used as standalone commands or as part
of tikzpicture environments.

%package -n texlive-autobreak
Summary:        Simple line breaking of long formulae
Version:        svn43337
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(catchfile.sty)
Provides:       tex(autobreak.sty) = %{tl_version}

%description -n texlive-autobreak
This package implements a simple mechanism of line/page breaking within the
align environment of the amsmath package; new line characters are considered as
possible candidates for the breaks and the package tries to put breaks at
adequate places. It is suitable for computer-generated long formulae with many
terms.

%package -n texlive-backnaur
Summary:        Typeset Backus Naur Form definitions
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(backnaur.sty) = %{tl_version}

%description -n texlive-backnaur
The package typesets Backus-Naur Form (BNF) definitions. It prints formatted
lists of productions, with numbers if required. It can also print in-line BNF
expressions using math mode.

%package -n texlive-begriff
Summary:        Typeset Begriffschrift
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(begriff.sty) = %{tl_version}

%description -n texlive-begriff
The package defines maths mode commands for typesetting Frege's Begriffschrift.

%package -n texlive-binomexp
Summary:        Calculate Pascal's triangle
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(binomexp.sty) = %{tl_version}

%description -n texlive-binomexp
The package calculates and prints rows of Pascal's triangle. It may be used:
simply to print successive rows of the triangle, or to print the rows inside an
array or tabular.

%package -n texlive-biocon
Summary:        Typesetting biological species names
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Provides:       tex(biocon-old.sty) = %{tl_version}
Provides:       tex(biocon.sty) = %{tl_version}

%description -n texlive-biocon
The biocon--biological conventions--package aids the typesetting of some
biological conventions. At the moment, it makes a good job of typesetting
species names (and ranks below the species level). A distinction is made
between the Plant, Fungi, Animalia and Bacteria kingdoms. There are default
settings for the way species names are typeset, but they can be customized.
Different default styles are used in different situations.

%package -n texlive-bitpattern
Summary:        Typeset bit pattern diagrams
Version:        svn39073
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(multido.sty)
Provides:       tex(bitpattern.sty) = %{tl_version}

%description -n texlive-bitpattern
A package to typeset bit pattern diagrams such as those used to describe
hardware, data format or protocols.

%package -n texlive-bodeplot
Summary:        Draw Bode, Nyquist and Nichols plots with gnuplot or pgfplots
Version:        svn77390
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifplatform.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(xparse.sty)
Provides:       tex(bodeplot-2024-02-06.sty) = %{tl_version}
Provides:       tex(bodeplot.sty) = %{tl_version}

%description -n texlive-bodeplot
This is a LaTeX package to plot Bode, Nichols, and Nyquist diagrams. It
provides added functionality over the similar bodegraph package: New \BodeZPK
and \BodeTF commands to generate Bode plots of any transfer function given
either poles, zeros, gain, and delay, or numerator and denominator coefficients
and delay Support for unstable poles and zeros. Support for complex poles and
zeros. Support for general stable and unstable second order transfer functions.
Support for both Gnuplot (default) and pgfplots (package option pgf). Support
for linear and asymptotic approximation of magnitude and phase plots of any
transfer function given poles, zeros, and gain.

%package -n texlive-bohr
Summary:        Simple atom representation according to the Bohr model
Version:        svn62977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(elements.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(bohr.sty) = %{tl_version}

%description -n texlive-bohr
The package provides means for the creation of simple Bohr models of atoms up
to the atomic number 112. In addition, commands are provided to convert atomic
numbers to element symbols or element names and vice versa.

%package -n texlive-boldtensors
Summary:        Bold latin and greek characters through simple prefix characters
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(boldtensors.sty) = %{tl_version}

%description -n texlive-boldtensors
This package provides bold latin and greek characters within
\mathversion{normal}, by using ~ and " as prefix characters.

%package -n texlive-bosisio
Summary:        A collection of packages by Francesco Bosisio
Version:        svn16989
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Requires:       tex(graphics.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(xspace.sty)
Provides:       tex(accenti.sty) = %{tl_version}
Provides:       tex(dblfont.sty) = %{tl_version}
Provides:       tex(envmath.sty) = %{tl_version}
Provides:       tex(evenpage.sty) = %{tl_version}
Provides:       tex(graphfig.sty) = %{tl_version}
Provides:       tex(mathcmd.sty) = %{tl_version}
Provides:       tex(quotes.sty) = %{tl_version}
Provides:       tex(sobolev.sty) = %{tl_version}

%description -n texlive-bosisio
A collection of packages containing: accenti dblfont; envmath; evenpage;
graphfig; mathcmd; quotes; and sobolev.

%package -n texlive-bpchem
Summary:        Typeset chemical names, formulae, etc.
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(bpchem.sty) = %{tl_version}

%description -n texlive-bpchem
The package provides support for typesetting simple chemical formulae, those
long IUPAC compound names, and some chemical idioms. It also supports the
labelling of compounds and reference to labelled compounds.

%package -n texlive-bracealign
Summary:        Align braces under and over math expressions
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bracealign.sty) = %{tl_version}

%description -n texlive-bracealign
A LaTeX package to align braces under and over math expressions. A new
environment called bracealign is provided, inside which braces and brackets
drawn with the commands \underbrace, \overbrace, \underbracket, \overbracket,
\underparen or \overparenare vertically aligned. The package also allows adding
support for new commands.

%package -n texlive-bropd
Summary:        Simplified brackets and differentials in LaTeX
Version:        svn35383
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bropd.sty) = %{tl_version}

%description -n texlive-bropd
The package simplifies the process of writing differential operators and
brackets in LaTeX. The commands facilitate the easy manipulation of equations
involving brackets and allow partial differentials to be expressed in an
alternate form.

%package -n texlive-broydensolve
Summary:        Solve a system of equations with Broyden's good method
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(broydensolve.sty) = %{tl_version}

%description -n texlive-broydensolve
This package implements Broyden's good method to solve a system of equations.
It is also possible to use coordinates defined by TikZ as known and unknown
variables.

%package -n texlive-bussproofs
Summary:        Proof trees in the style of the sequent calculus
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bussproofs.sty) = %{tl_version}

%description -n texlive-bussproofs
The package allows the construction of proof trees in the style of the sequent
calculus and many other proof systems. One novel feature of the macros is they
support the horizontal alignment according to some centre point specified with
the command \fCenter. This is the style often used in sequent calculus proofs.
The package works in a Plain TeX document, as well as in LaTeX; an exposition
of the commands available is given in the package file itself.

%package -n texlive-bussproofs-colorful
Summary:        Color extension for the bussproofs package
Version:        svn77507
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bussproofs.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(bussproofs-colorful.sty) = %{tl_version}

%description -n texlive-bussproofs-colorful
This is a small extension to the bussproofs package that adds color control for
proof trees. It allows users to customize the colors of nodes (formulas),
inference lines, and labels via package options and runtime commands, while
preserving the original layout and spacing of bussproofs.

%package -n texlive-bussproofs-extra
Summary:        Extra commands for bussproofs.sty
Version:        svn51299
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bussproofs.sty)
Requires:       tex(tikz.sty)
Provides:       tex(bussproofs-extra.sty) = %{tl_version}

%description -n texlive-bussproofs-extra
This package provides additional functionality for bussproofs.sty;
specifically, it allows for typesetting of entire (sub)deductions.

%package -n texlive-bytefield
Summary:        Create illustrations for network protocol specifications
Version:        svn74416
License:        LPPL-1.3a
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(keyval.sty)
Provides:       tex(bytefield.sty) = %{tl_version}

%description -n texlive-bytefield
The bytefield package helps the user create illustrations for network protocol
specifications and anything else that utilizes fields of data. These
illustrations show how the bits and bytes are laid out in a packet or in
memory.

%package -n texlive-calculation
Summary:        Typesetting reasoned calculations, also called calculational proofs
Version:        svn35973
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(delarray.sty)
Provides:       tex(calculation.sty) = %{tl_version}

%description -n texlive-calculation
The calculation environment formats reasoned calculations, also called
calculational proofs. The notion of reasoned calculations or calculational
proofs was originally advocated by Wim Feijen and Edsger Dijkstra. The package
accepts options fleqn and leqno (with the same effect as the LaTeX options
fleqn and leqno, or may inherit the options from the document class). It allows
steps and expressions to be numbered (by LaTeX equation numbers, obeying the
LaTeX \label command to refer to these numbers), and a step doesn't take
vertical space if its hint is empty. An expression in a calculation can be
given a comment; it is placed at the side opposite to the equation numbers.
Calculations are allowed inside hints although numbering and commenting is then
disabled.

%package -n texlive-cartonaugh
Summary:        A LuaLaTeX package for drawing karnaugh maps with up to 6 variables
Version:        svn59938
License:        CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cartonaugh.sty) = %{tl_version}

%description -n texlive-cartonaugh
This package, a fork of 2pi's karnaugh-map package, draws karnaugh maps with 2,
3, 4, 5, and 6 variables. It also contains commands for filling the karnaugh
map with terms semi-automatically or manually. Last but not least it contains
commands for drawing implicants on top of the map. The name "cartonaugh" is a
portmanteau of "cartographer" and "karnaugh". The package needs LuaLaTeX and
depends on TikZ, xparse, and xstring.

%package -n texlive-cascade
Summary:        Constructions with braces to present mathematical demonstrations
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cascade.sty) = %{tl_version}

%description -n texlive-cascade
The LaTeX package cascade provides a command \Cascade to do constructions to
present mathematical demonstrations with successive braces for the deductions.

%package -n texlive-causets
Summary:        Draw causal set (Hasse) diagrams
Version:        svn74247
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(causets.sty) = %{tl_version}

%description -n texlive-causets
This LaTeX package uses TikZ to generate (Hasse) diagrams for causal sets
(causets) to be used inline with text or in mathematical expressions. The
macros can also be used in the tikzpicture environment to annotate or modify a
diagram, as shown with some examples in the documentation.

%package -n texlive-ccfonts
Summary:        Support for Concrete text and math fonts in LaTeX
Version:        svn61431
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ccfonts.sty) = %{tl_version}

%description -n texlive-ccfonts
LaTeX font definition files for the Concrete fonts and a LaTeX package for
typesetting documents using Concrete as the default font family. The files
support OT1, T1, TS1, and Concrete mathematics including AMS fonts (Ulrik
Vieth's concmath).

%package -n texlive-ccool
Summary:        A key-value document command parser
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(lambdax.sty)
Requires:       tex(xparse.sty)
Provides:       tex(ccool.sty) = %{tl_version}

%description -n texlive-ccool
This package provides a key-value interface, \Ccool, on top of xparse's
document command parser. Global options control input processing and its
expansion. By default, they are set to meet likely requirements, depending on
context: the selected language, and which of text and math mode is active.
These options can be overridden inline. This versatility could find its use,
for example, to encode notational conventions (such as \Real - \mathbb{R}) at
the point where they are introduced in the document ("Let R denote real
numbers"). Polymorphic commands can be generated by parameterizing the keys
(for instance, one parameter value for style, another for a property). User
input to \Ccool can optionally be serialized. This can useful for typesetting
documents sharing the same notation.

%package -n texlive-chemarrow
Summary:        Arrows for use in chemistry
Version:        svn17146
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chemarrow.sty) = %{tl_version}

%description -n texlive-chemarrow
This bundle consists of a font (available as Metafont source, MetaPost source,
and generated type 1 versions), and a package to use it. The arrows in the font
are designed to look more like those in chemistry text-books than do Knuth's
originals.

%package -n texlive-chemcompounds
Summary:        Simple consecutive numbering of chemical compounds
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chemcompounds.sty) = %{tl_version}

%description -n texlive-chemcompounds
The chemcompounds package allows for a simple consecutive numbering of chemical
compounds. Optionally, it is possible to supply a custom name for each
compound. The package differs from the chemcono package by not generating an
odd-looking list of compounds inside the text.

%package -n texlive-chemcono
Summary:        Support for compound numbers in chemistry documents
Version:        svn17119
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(chemcono.sty) = %{tl_version}
Provides:       tex(drftcono.sty) = %{tl_version}
Provides:       tex(showkeysff.sty) = %{tl_version}

%description -n texlive-chemcono
A LaTeX package for using compound numbers in chemistry documents. It works
like \cite and the \thebibliography, using \fcite and \theffbibliography
instead. It allows compound names in documents to be numbered and does not
affect the normal citation routines.

%package -n texlive-chemexec
Summary:        Creating (chemical) exercise sheets
Version:        svn21632
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accents.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(framed.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mhchem.sty)
Requires:       tex(tikz.sty)
Requires:       tex(ulem.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(chemexec.sty) = %{tl_version}

%description -n texlive-chemexec
The package provides environments and commands that the author needed when
preparing exercise sheets and other teaching material. In particular, the
package supports the creation of exercise sheets, with separating printing of
solutions

%package -n texlive-chemformula
Summary:        Command for typesetting chemical formulas and reactions
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-units
Requires:       tex(amsmath.sty)
Requires:       tex(nicefrac.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfrac.sty)
Provides:       tex(chemformula.sty) = %{tl_version}

%description -n texlive-chemformula
The package provides a command to typeset chemical formulas and reactions in
support of other chemistry packages (such as chemmacros). The package used to
be distributed as a part of chemmacros.

%package -n texlive-chemformula-ru
Summary:        Using the chemformula package with babel-russian settings
Version:        svn71883
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(chemformula.sty)
Provides:       tex(chemformula-ru.sty) = %{tl_version}

%description -n texlive-chemformula-ru
The chemformula package and babel-russian settings (russian.ldf) both define
macros named "\ch". The package chemformula-ru undefines babel's macro to
prevent an error when both packages are loaded together. Optionally it
redefines the \cosh macro to print the hyperbolic cosine in Russian notation
and/or defines a new macro \Ch for that purpose.

%package -n texlive-chemgreek
Summary:        Upright Greek letters in chemistry
Version:        svn53437
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Requires:       tex(xparse.sty)
Provides:       tex(chemgreek.sty) = %{tl_version}

%description -n texlive-chemgreek
The package provides upright Greek letters in support of other chemistry
packages (such as chemmacros). The package used to be distributed as a part of
chemmacros.

%package -n texlive-chemmacros
Summary:        A collection of macros to support typesetting chemistry documents
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Requires:       tex(bm.sty)
Requires:       tex(chemgreek.sty)
Requires:       tex(elements.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(relsize.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(translations.sty)
Requires:       tex(xfrac.sty)
Requires:       tex(xparse.sty)
Provides:       tex(chemmacros-2015-02-08.sty) = %{tl_version}
Provides:       tex(chemmacros-2020-03-07.sty) = %{tl_version}
Provides:       tex(chemmacros.sty) = %{tl_version}

%description -n texlive-chemmacros
The bundle offers a collection of macros and commands which are intended to
make typesetting chemistry documents faster and more convenient. Coverage
includes some nomenclature commands, oxidation numbers, thermodynamic data,
newman projections, etc. The package relies on the following supporting
packages: chemformula, providing a command for typesetting chemical formulae
and reactions (doing a similar task to that of mhchem); chemgreek, offering
support for use of greek letters; and ghsystem, providing for the UN globally
harmonised chemical notation. The packages are written using current versions
of the experimental LaTeX 3 coding conventions and the LaTeX 3 support
packages.

%package -n texlive-chemnum
Summary:        A method for numbering chemical compounds
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(chemgreek.sty)
Requires:       tex(psfrag.sty)
Requires:       tex(translations.sty)
Requires:       tex(xparse.sty)
Provides:       tex(chemnum.sty) = %{tl_version}

%description -n texlive-chemnum
The package defines a \label- and \ref-like commands for compound numbers. The
package requires LaTeX3 packages expl3 (from the l3kernel bundle) as well as
xparse and l3keys2e (from the l3packages bundle).

%package -n texlive-chemobabel
Summary:        Convert chemical structures from ChemDraw, MDL molfile or SMILES using Open Babel
Version:        svn64778
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(chemobabel.sty) = %{tl_version}

%description -n texlive-chemobabel
This package provides a way to convert and include chemical structure graphics
from various chemical formats, such as ChemDraw files, MDL molfile or SMILES
notations using Open Babel. To use this LaTeX package, it is necessary to
enable execution of the following external commands via latex -shell-escape.
obabel (Open Babel) inkscape or rsvg-convert (for SVG -> PDF/EPS conversion)
pdfcrop or ps2eps (optional; for cropping large margins of PDF/EPS)

%package -n texlive-chemplants
Summary:        Symbology to draw chemical plants with TikZ
Version:        svn60606
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(chemplants.sty) = %{tl_version}

%description -n texlive-chemplants
This package offers tools to draw simple or barely complex schemes of chemical
processes. The package defines several standard symbols and styles to draw
process units and streams. The guiding light of the package is the UNICHIM
regulation. All of the symbols and styles are defined using tools of the TikZ
package, thus a basic knowledge of the logic of this powerful tool is required
to profitably use chemplants.

%package -n texlive-chemschemex
Summary:        Typeset and cross-reference chemical schemes based on TikZ code
Version:        svn46723
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fancylabel.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(chemschemex.sty) = %{tl_version}

%description -n texlive-chemschemex
The package provides a comfortable means of typesetting chemical schemes, and
also offers automatic structure referencing.

%package -n texlive-chemsec
Summary:        Automated creation of numeric entity labels
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(chemsec.sty) = %{tl_version}

%description -n texlive-chemsec
Packages provides creation of sequential numeric labels for entities in a
document. The motivating example is chemical structures in a scientific
document. The package can automatically output a full object name and label on
the first occurrence in the document and just labels only on subsequent
references.

%package -n texlive-chemstyle
Summary:        Writing chemistry with style
Version:        svn31096
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(SIunits.sty)
Requires:       tex(amstext.sty)
Requires:       tex(bpchem.sty)
Requires:       tex(caption.sty)
Requires:       tex(chemcompounds.sty)
Requires:       tex(float.sty)
Requires:       tex(floatrow.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(psfrag.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xspace.sty)
Provides:       tex(chemscheme.sty) = %{tl_version}
Provides:       tex(chemstyle.sty) = %{tl_version}

%description -n texlive-chemstyle
Chemstyle has been developed as a successor to the LaTeX package provided by
the rsc bundle. The package provides an extensible system for formatting
chemistry documents according to the conventions of a number of leading
journals. It also provides some handy chemistry-related macros. Chemstyle is
much enhanced compared to its predecessor, and users of rsc are strongly
encouraged to migrate (all of the additional macros in the rsc LaTeX package
are present in chemstyle). The package chemscheme is distributed with
chemstyle; chemstyle itself incorporates ideas that come from the trivfloat
package; the documentation uses the auto-pst-pdf package.

%package -n texlive-clrscode
Summary:        Typesets pseudocode as in Introduction to Algorithms
Version:        svn51136
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(latexsym.sty)
Provides:       tex(clrscode.sty) = %{tl_version}

%description -n texlive-clrscode
This package allows you to typeset pseudocode in the style of Introduction to
Algorithms, Second edition, by Cormen, Leiserson, Rivest, and Stein. The
package was written by the authors. You use the commands the same way the
package's author did when writing the book, and your output will look just like
the pseudocode in the text.

%package -n texlive-clrscode3e
Summary:        Typesets pseudocode as in Introduction to Algorithms
Version:        svn51137
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(clrscode3e.sty) = %{tl_version}

%description -n texlive-clrscode3e
This package allows you to typeset pseudocode in the style of Introduction to
Algorithms, Third edition, by Cormen, Leiserson, Rivest, and Stein. The package
was written by the authors. Use the commands the same way the package's author
did when writing the book, and your output will look just like the pseudocode
in the text.

%package -n texlive-codeanatomy
Summary:        Typeset code with annotations
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(codeanatomy.sty) = %{tl_version}

%description -n texlive-codeanatomy
The idea of this Package is to typeset illustrations of pieces of code with
annotations on each single part of code (Code Anatomy). The origin of this idea
are code illustrations from the book "Computer Science: An Interdisciplinary
Approach" from Robert Sedgewick and Kevin Wayne. The package depends on expl3,
xparse, and TikZ.

%package -n texlive-coloredtheorem
Summary:        A colourful boxed theorem environment
Version:        svn74812
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tcolorbox.sty)
Provides:       tex(coloredtheorem.sty) = %{tl_version}

%description -n texlive-coloredtheorem
This packages provides a colourful boxed theorem environment, combining
tcolorbox and breakable boxes.

%package -n texlive-commath
Summary:        Mathematics typesetting support
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(commath.sty) = %{tl_version}

%description -n texlive-commath
Provides a range of differential, partial differential and delimiter commands,
together with a \fullfunction (function, with both domain and range, and
function operation) and various reference commands.

%package -n texlive-commutative-diagrams
Summary:        CoDi: Commutative Diagrams for TeX
Version:        svn71053
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(commutative-diagrams.sty) = %{tl_version}
Provides:       tex(commutative-diagrams.tex) = %{tl_version}
Provides:       tex(kodi.sty) = %{tl_version}
Provides:       tex(t-commutative-diagrams.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.bapto.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.diorthono.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.ektropi.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.katharizo.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.koinos.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.mandyas.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.mitra.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.ozos.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.ramma.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycommutative-diagrams.velos.code.tex) = %{tl_version}

%description -n texlive-commutative-diagrams
This package provides a TikZ library for making commutative diagrams easy to
design, parse and tweak.

%package -n texlive-complexity
Summary:        Computational complexity class names
Version:        svn45322
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(complexity.sty) = %{tl_version}
Provides:       tex(mycomplexity.sty) = %{tl_version}

%description -n texlive-complexity
Complexity is a LaTeX package that defines commands to typeset Computational
Complexity Classes such as $\P$ and $\NP$ (as well as hundreds of others). It
also offers several options including which font classes are typeset in and how
many are defined (all of them or just the basic, most commonly used ones). The
package has no dependencies other than the standard ifthen package.

%package -n texlive-complexpolylongdiv
Summary:        Typesetting (complex) polynomial long division
Version:        svn76639
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(complexpolylongdiv.sty) = %{tl_version}

%description -n texlive-complexpolylongdiv
This package provides a simple interface for typesetting (complex) polynomial
long division.

%package -n texlive-computational-complexity
Summary:        Class for the journal Computational Complexity
Version:        svn44847
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(breakcites.sty)
Requires:       tex(breakurl.sty)
Requires:       tex(draftcopy.sty)
Requires:       tex(environ.sty)
Requires:       tex(graphics.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(lineno.sty)
Requires:       tex(natbib.sty)
Requires:       tex(theorem.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(cc-cls.sty) = %{tl_version}
Provides:       tex(cc2cite.sty) = %{tl_version}
Provides:       tex(cc4amsart.sty) = %{tl_version}
Provides:       tex(cc4apjrnl.sty) = %{tl_version}
Provides:       tex(cc4elsart.sty) = %{tl_version}
Provides:       tex(cc4jT.sty) = %{tl_version}
Provides:       tex(cc4llncs.sty) = %{tl_version}
Provides:       tex(cc4siamltex.sty) = %{tl_version}
Provides:       tex(cc4svjour.sty) = %{tl_version}
Provides:       tex(ccalgo.sty) = %{tl_version}
Provides:       tex(ccaux.sty) = %{tl_version}
Provides:       tex(cccite.sty) = %{tl_version}
Provides:       tex(ccdbs.sty) = %{tl_version}
Provides:       tex(cclayout.sty) = %{tl_version}
Provides:       tex(ccproof.sty) = %{tl_version}
Provides:       tex(ccqed.sty) = %{tl_version}
Provides:       tex(ccref.sty) = %{tl_version}
Provides:       tex(ccreltx.sty) = %{tl_version}
Provides:       tex(ccthm.sty) = %{tl_version}
Provides:       tex(relabel.sty) = %{tl_version}
Provides:       tex(thcc.sty) = %{tl_version}

%description -n texlive-computational-complexity
The LaTeX2e class cc was written for the journal Computational Complexity, and
it can also be used for a lot of other articles. You may like it since it
contains a lot of features such as more intelligent references, a set of
theorem definitions, an algorithm environment, and more. The class requires
natbib.

%package -n texlive-concmath
Summary:        Concrete Math fonts
Version:        svn17219
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(exscale.sty)
Provides:       tex(concmath.sty) = %{tl_version}

%description -n texlive-concmath
A LaTeX package and font definition files to access the Concrete mathematics
fonts, which were derived from Computer Modern math fonts using parameters from
Concrete Roman text fonts.

%package -n texlive-concrete
Summary:        Concrete Roman fonts
Version:        svn57963
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-concrete
Concrete Roman fonts, designed by Donald E. Knuth, originally for use with
Euler mathematics fonts. Alternative mathematics fonts, based on the concrete
'parameter set' are available as the concmath fonts bundle. LaTeX support is
offered by the beton, concmath and ccfonts packages. T1- and TS1-encoded
versions of the fonts are available in the ecc bundle, and Adobe Type 1
versions of the ecc fonts are part of the cm-super bundle.

%package -n texlive-conteq
Summary:        Typeset multiline continued equalities
Version:        svn37868
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(environ.sty)
Provides:       tex(conteq.sty) = %{tl_version}

%description -n texlive-conteq
The package provides an environment conteq, which will lay out systems of
continued equalities (or inequalities). Several variant layouts of the
equalities are provided, and the user may define their own. The package is
written using LaTeX 3 macros.

%package -n texlive-cora-macs
Summary:        Macros for continuous sets and neural networks in the context of cyber-physical systems
Version:        svn76540
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(graphics.sty)
Requires:       tex(keyval.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikzscale.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cora-macs.sty) = %{tl_version}

%description -n texlive-cora-macs
This LaTeX package has been designed to assist in the representation and
manipulation of continuous sets, operations, neural networks, and color schemes
tailored for use in the context of cyber-physical systems. It provides a
comprehensive set of macros that streamline the process of documenting complex
mathematical objects and operations.

%package -n texlive-correctmathalign
Summary:        Correct spacing of the alignment in expressions
Version:        svn44131
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(correctmathalign.sty) = %{tl_version}

%description -n texlive-correctmathalign
This package realigns the horizontal spacing of the alignments in some
mathematical environments.

%package -n texlive-cryptocode
Summary:        Typesetting pseudocode, protocols, game-based proofs and black-box reductions in cryptography
Version:        svn60249
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(centernot.sty)
Requires:       tex(environ.sty)
Requires:       tex(etex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(forloop.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pbox.sty)
Requires:       tex(pgf.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(cryptocode-2018-11-11.sty) = %{tl_version}
Provides:       tex(cryptocode-2020-04-24.sty) = %{tl_version}
Provides:       tex(cryptocode.sty) = %{tl_version}

%description -n texlive-cryptocode
The cryptocode package provides a set of macros to ease the typesetting of
pseudocode, algorithms and protocols. In addition it comes with a wide range of
tools to typeset cryptographic papers. This includes simple predefined commands
for concepts such as a security parameter or advantage terms but also flexible
and powerful environments to layout game-based proofs or black-box reductions.

%package -n texlive-cs-techrep
Summary:        Technical Reports in Computer Science and Software Engineering
Version:        svn77506
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cs-techrep
This package provides a class for the creation of technical reports in computer
science and software engineering. The style is a two-column format similar to
IEEE. It is intended for lab reports and provides a beginner-friendly template
example.

%package -n texlive-csassignments
Summary:        A wrapper for article with macros and customizations for computer science assignments
Version:        svn77161
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-csassignments
This class wraps the default article and extends it for a homogeneous look of
hand-in assignments at university (RWTH Aachen University, Computer Science
Department), specifically in the field of computer science, but easily
extensible to other fields. It provides macros for structuring exercises,
aggregating points, and displaying a grading table, as well as several macros
for easier math mode usage.

%package -n texlive-csthm
Summary:        Customized theorem environments for computer science documents
Version:        svn73506
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(thmtools.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(csthm.sty) = %{tl_version}

%description -n texlive-csthm
This package provides customized theorem-like environments specifically
designed for computer science documents. It offers a set of pre-defined theorem
styles and environments to streamline the creation of theorems, definitions,
remarks, and other common structures in computer science papers and documents.
Features: Predefined theorem styles tailored for computer science Environments
for theorems, lemmas, definitions, examples, remarks, and more Special
environments for cases and axioms Customizable accent color Optional cleveref
support for enhanced cross-referencing The package requires the following
packages to be installed: amsmath, amssymb, amsthm, enumitem, and thmtools. If
using the cleveref option, hyperref and cleveref are also required.

%package -n texlive-cvss
Summary:        Compute and display CVSS base scores
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cvss.sty) = %{tl_version}

%description -n texlive-cvss
The Common Vulnerability Scoring System (CVSS) is an open framework for
communicating the characteristics and severity of software vulnerabilities.
CVSS consists of three metric groups: Base, Temporal, and Environmental. This
package allows the user to compute CVSS3.1 base scores and use them in
documents, i.e. it only deals with the Base score. Temporal and Environmental
scores will be part of a future release. More information can be found at
https://www.first.org/cvss/specification-document.

%package -n texlive-decision-table
Summary:        An easy way to create Decision Model and Notation decision tables
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(decision-table.sty) = %{tl_version}

%description -n texlive-decision-table
The decision-table package allows for an easy way to generate decision tables
in the Decision Model and Notation (DMN) format. This package ensures
consistency in the tables (i.e. fontsize), and is thus a better alternative to
inserting tables via images. The decision-table package adds the \dmntable
command, with which tables can be created. This command expands into a tabular,
so it can be used within a table or figure environment. Furthermore, this
allows labels and captions to be added seamlessly. It is also possible to place
multiple DMN tables in one table/figure environment. The package relies on
nicematrix and l3keys2e.

%package -n texlive-delim
Summary:        Simplify typesetting mathematical delimiters
Version:        svn23974
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(delim.sty) = %{tl_version}

%description -n texlive-delim
The package permits simpler control of delimiters without excessive use of
\big... commands (and the like).

%package -n texlive-delimseasy
Summary:        Delimiter commands that are easy to use and resize
Version:        svn77161
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(delimseasy.sty) = %{tl_version}

%description -n texlive-delimseasy
This package provides commands to give a consistent, easy-to-remember, easy to
edit way to control the size and blackness of delimiters: append 1-4 "b"s to
command for larger sizes; prepend "B" for boldface. These commands reduce the
likelihood of incomplete delimiter pairs and typically use fewer characters
than the LaTeX default.

%package -n texlive-delimset
Summary:        Typeset and declare sets of delimiters with convenient size control
Version:        svn74779
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(delimset.sty) = %{tl_version}

%description -n texlive-delimset
delimset is a LaTeX2e package to typeset and declare sets of delimiters in math
mode whose size can be adjusted conveniently.

%package -n texlive-derivative
Summary:        Nice and easy derivatives
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(derivative.sty) = %{tl_version}

%description -n texlive-derivative
Typesetting derivatives and differentials in a consistent way are clumsy and
require care to ensure the preferred formatting. Several packages have been
developed for this purpose, each with its own features and drawbacks, with the
most ambitious one being diffcoeff. While this package is comparable to
diffcoeff in terms of features, it takes a different approach. One difference
is this package provides more options to tweak the format of the derivatives
and differentials. However, the automatic calculation of the total order isn't
as developed as the one in diffcoeff. This package makes it easy to write
derivatives and differentials consistently with its predefined commands. It
also provides a set of commands that can define custom derivatives and
differential operators. The options follow a consistent naming scheme making
them easy to use and understand.

%package -n texlive-diffcoeff
Summary:        Write differential coefficients easily and consistently
Version:        svn77136
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(mleftright.sty)
Requires:       tex(xparse.sty)
Provides:       tex(diffcoeff-doc.def) = %{tl_version}
Provides:       tex(diffcoeff.sty) = %{tl_version}
Provides:       tex(diffcoeff4.sty) = %{tl_version}
Provides:       tex(diffcoeff5.def) = %{tl_version}

%description -n texlive-diffcoeff
This package allows the easy and consistent writing of ordinary, partial and
other derivatives of arbitrary (algebraic or numeric) order. For mixed partial
derivatives, the total order of differentiation is calculated by the package.
Optional arguments allow specification of points of evaluation (ordinary
derivatives), or variables held constant (partial derivatives), and the
placement of the differentiand (numerator or appended). The package is built on
xtemplate and the configurability it enables, extending to differentials
(including simple line elements) and jacobians.

%package -n texlive-digiconfigs
Summary:        Writing "configurations"
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Provides:       tex(digiconfigs.sty) = %{tl_version}

%description -n texlive-digiconfigs
In Stochastic Geometry and Digital Image Analysis some problems can be solved
in terms of so-called "configurations". A configuration is basically a square
matrix of \circ and \bullet symbols. This package provides a convenient and
compact mechanism for displaying these configurations.

%package -n texlive-dijkstra
Summary:        Dijkstra algorithm for LaTeX
Version:        svn64580
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(simplekv.sty)
Provides:       tex(dijkstra.sty) = %{tl_version}

%description -n texlive-dijkstra
This small package uses the Dijkstra algorithm for weighted graphs,directed or
not: the search table of the shortest path can be displayed, the minimum
distance between two vertices and the corresponding path are stored in macros.
This packages depends on simplekv.

%package -n texlive-domaincoloring
Summary:        Draw colored represenations of complex functions
Version:        svn72176
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(domaincoloring.sty) = %{tl_version}

%description -n texlive-domaincoloring
Domain coloring is a technique to visualize complex functions by assigning a
color to each point of the complex plane z=x+iy. This package calculates with
the help of Lua any complex function to visualize its behaviour. The value of
the complex function(z) can be described by radius and angle which can be two
values of the hsv-color model, which then defines the color of each point in
the complex plane z=x+iy.

%package -n texlive-drawmatrix
Summary:        Draw visual representations of matrices in LaTeX
Version:        svn44471
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(drawmatrix.sty) = %{tl_version}

%description -n texlive-drawmatrix
The package provides macros to visually represent matrices. Various options
allow to change the visualizations, e.g., drawing rectangular, triangular, or
banded matrices.

%package -n texlive-drawstack
Summary:        Draw execution stacks
Version:        svn28582
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(drawstack.sty) = %{tl_version}

%description -n texlive-drawstack
This simple LaTeX package provides support for drawing execution stack
(typically to illustrate assembly language notions). The code is written on top
of TikZ.

%package -n texlive-dyntree
Summary:        Construct Dynkin tree diagrams
Version:        svn67016
License:        LGPL-2.1-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(calc.sty)
Requires:       tex(coollist.sty)
Requires:       tex(eepic.sty)
Requires:       tex(epic.sty)
Provides:       tex(dyntree.sty) = %{tl_version}

%description -n texlive-dyntree
The package is intended for users needing to typeset a Dynkin Tree Diagram--a
group theoretical construct consisting of cartan coefficients in boxes
connected by a series of lines. Such a diagram is a tool for working out the
states and their weights in terms of the fundamental weights and the simple
roots. The package makes use of the author's coollist package.

%package -n texlive-easing
Summary:        Easing functions for pgfmath
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pgflibraryeasing.code.tex) = %{tl_version}

%description -n texlive-easing
This library implements a collection of easing functions and adds them to the
PGF mathematical engine.

%package -n texlive-ebproof
Summary:        Formal proofs in the style of sequent calculus
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(ebproof.sty) = %{tl_version}

%description -n texlive-ebproof
This package provides commands to typeset proof trees in the style of sequent
calculus and related systems. The commands allow for writing inferences with
any number of premises and alignment of successive formulas on an arbitrary
point. Various options allow complete control over spacing, styles of inference
rules, placement of labels, etc. The package requires expl3 and xparse.

%package -n texlive-econometrics
Summary:        Simplify mathematic notation in economic and econometric writing
Version:        svn39396
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(econometrics.sty) = %{tl_version}

%description -n texlive-econometrics
Econometrics is a package that defines some commands that simplify mathematic
notation in economic and econometrics writing. The commands are related to the
notation of vectors, matrices, sets, calligraphic and roman letters statistical
distributions constants and symbols matrix operators and statistical operators.
The package is based on "Notation in Econometrics: a proposal for a standard"
by Karim Abadir and Jan R. Magnus, The Econometrics Journal (2002), 5, 76-90.

%package -n texlive-eltex
Summary:        Simple circuit diagrams in LaTeX picture mode
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eltex1.tex) = %{tl_version}
Provides:       tex(eltex2.tex) = %{tl_version}
Provides:       tex(eltex3.tex) = %{tl_version}
Provides:       tex(eltex4.tex) = %{tl_version}
Provides:       tex(eltex5.tex) = %{tl_version}
Provides:       tex(eltex6.tex) = %{tl_version}
Provides:       tex(eltex7.tex) = %{tl_version}

%description -n texlive-eltex
The macros enable the user to draw simple circuit diagrams in the picture
environment, with no need of special resources. The macros are appropriate for
drawing for school materials. The circuit symbols accord to the various parts
of the standard IEC 617.

%package -n texlive-emf
Summary:        Support for the EMF symbol
Version:        svn76790
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(emf.sty) = %{tl_version}

%description -n texlive-emf
This package provides LaTeX support for the symbol for the EMF in electric
circuits and electrodynamics. It provides support for multiple symbols but does
not provide any fonts; the fonts are part of a normal TeX Live installation.

%package -n texlive-endiagram
Summary:        Easy creation of potential energy curve diagrams
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(endiagram.sty) = %{tl_version}

%description -n texlive-endiagram
The package provides the facility of drawing potential energy curve diagrams
with just a few simple commands. The package cannot (yet) be considered stable.

%package -n texlive-engtlc
Summary:        Support for users in Telecommunications Engineering
Version:        svn28571
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(engtlc.sty) = %{tl_version}

%description -n texlive-engtlc
The package provides a wide range of abbreviations for terms used in
Telecommunications Engineering.

%package -n texlive-eqexpl
Summary:        Align explanations for formulas
Version:        svn63629
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xparse.sty)
Provides:       tex(eqexpl.sty) = %{tl_version}

%description -n texlive-eqexpl
This package was developed in response to a question on
https://tex.stackexchange.com. Its purpose is to enable a perfectly formatted
explanation of components of a formula. The package depends on calc, etoolbox,
and xparse.

%package -n texlive-eqnarray
Summary:        More generalised equation arrays with numbering
Version:        svn20641
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Provides:       tex(eqnarray.sty) = %{tl_version}

%description -n texlive-eqnarray
Defines an equationarray environment, that allows more than three columns, but
otherwise behaves like LaTeX's eqnarray environment. This environment is
similar, in some ways, to the align environment of amsmath. The package
requires the array package.

%package -n texlive-eqnlines
Summary:        Single- and multiline equations
Version:        svn77363
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(eqnlines.sty) = %{tl_version}

%description -n texlive-eqnlines
This LaTeX2e package provides a framework for typesetting single- and multiline
equations which extends the established equation environments of LaTeX and the
amsmath package with many options for convenient adjustment of the intended
layout. In particular, the package adds flexible schemes for numbering,
horizontal alignment and semi-automatic punctuation, and it improves upon the
horizontal and vertical spacing options. The extensions can be used and
adjusted through optional arguments and modifiers to the equation environments
as well as global settings.

%package -n texlive-eqnnumwarn
Summary:        Modifies the amsmath equation environments to warn for a displaced equation number
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(eqnnumwarn.sty) = %{tl_version}

%description -n texlive-eqnnumwarn
Sometimes an equation is too long that an equation number will be typeset below
the equation itself, but yet not long enough to yield an overfull \hbox
warning. The eqnnumwarn package modifies the standard amsmath numbered equation
environments to throw a warning whenever this occurs.

%package -n texlive-euclidean-lattice
Summary:        Draw two-dimensional Euclidean lattices with TikZ
Version:        svn72985
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(euclidean-lattice.sty) = %{tl_version}

%description -n texlive-euclidean-lattice
This package provides a simple, efficient and easily configurable way to draw
two-dimensional Euclidean lattices using TikZ.

%package -n texlive-euclideangeometry
Summary:        Draw geometrical constructions
Version:        svn67608
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(euclideangeometry.sty) = %{tl_version}

%description -n texlive-euclideangeometry
This package provides tools to draw most of the geometrical constructions that
a high school instructor or bachelor degree professor might need to teach
geometry. The connection to Euclide depends on the fact that in his times
calculations were made with ruler, compass and also with ellipsograph. This
package extends the functionalities of the curve2e package.

%package -n texlive-extarrows
Summary:        Extra Arrows beyond those provided in amsmath
Version:        svn54400
License:        LGPL-2.1-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Provides:       tex(extarrows.sty) = %{tl_version}

%description -n texlive-extarrows
Arrows are provided to supplement \xleftarrow and \xrightarrow of the amsath
package: \xlongequal, \xLongleftarrow, \xLongrightarrow, \xLongleftrightarrow,
\xLeftrightarrow. \xlongleftrightarrow, \xleftrightarrow, \xlongleftarrow and
\xlongrightarrow.

%package -n texlive-extpfeil
Summary:        Extensible arrows in mathematics
Version:        svn16243
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(stmaryrd.sty)
Provides:       tex(extpfeil.sty) = %{tl_version}

%description -n texlive-extpfeil
The package provides some more extensible arrows (usable in the same way as
\xleftarrow from amsmath), and a simple command to create new ones.

%package -n texlive-faktor
Summary:        Typeset quotient structures with LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(faktor.sty) = %{tl_version}

%description -n texlive-faktor
The package provides the means to typeset factor structures, as are used in
many areas of algebraic notation. The structure is similar to the 'A/B' that is
provided by the nicefrac package (part of the units distribution), and by the
xfrac package; the most obvious difference is that the numerator and
denominator's sizes do not change in the \faktor command.

%package -n texlive-fascicules
Summary:        Create mathematical manuals for schools
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsthm.sty)
Requires:       tex(answers.sty)
Requires:       tex(beamerarticle.sty)
Requires:       tex(calc.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(comment.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(tagging.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xcomment.sty)
Provides:       tex(fascicules.sty) = %{tl_version}

%description -n texlive-fascicules
This package enables LaTeX users to create math books for middle and high
schools. It provides commands to create the front page of the manual and the
chapters. Each chapter can consist of three sections: the lesson, the exercises
and the activities.

%package -n texlive-fitch
Summary:        LaTeX macros for Fitch-style natural deduction
Version:        svn69160
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(fitch.sty) = %{tl_version}

%description -n texlive-fitch
The package provides macros for typesetting natural deduction proofs in Fitch
style, with subproofs indented and offset by scope lines.

%package -n texlive-fixdif
Summary:        Macros for typesetting differential operators
Version:        svn66606
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fixdif.sty) = %{tl_version}

%description -n texlive-fixdif
This package redefines the \d command in LaTeX and provides an interface to
define new commands for differential operators. It is compatible with pdfTeX,
XeTeX and LuaTeX, and can also be used with the unicode-math package.

%package -n texlive-fixmath
Summary:        Make maths comply with ISO 31-0:1992 to ISO 31-13:1992
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fixmath.sty) = %{tl_version}

%description -n texlive-fixmath
LaTeX's default style of typesetting mathematics does not comply with the
International Standards ISO 31-0:1992 to ISO 31-13:1992 which require that
uppercase Greek letters always be typeset upright, as opposed to italic (even
though they usually represent variables) and allow for typesetting of variables
in a boldface italic style (even though the required fonts are available). This
package ensures that uppercase Greek be typeset in italic style, that upright
$\Delta$ and $\Omega$ symbols are available through the commands \upDelta and
\upOmega; and provides a new math alphabet \mathbold for boldface italic
letters, including Greek. This package used to be part of the was bundle, but
has now become a package in its own right.

%package -n texlive-fnspe
Summary:        Macros for supporting mainly students of FNSPE CTU in Prague
Version:        svn45360
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(physics.sty)
Requires:       tex(substr.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
Provides:       tex(fnspe.sty) = %{tl_version}

%description -n texlive-fnspe
This package is primary intended for students of FNSPE CTU in Prague but many
other students or scientists can found this package as useful. This package
implements different standards of tensor notation, interval notation and
complex notation. Further many macros and shortcuts are added, e.q. for spaces,
operators, physics unit, etc.

%package -n texlive-fodot
Summary:        Helpful commands to work with the FODOT
Version:        svn76255
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(listings.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xspace.sty)
Provides:       tex(fodot.sty) = %{tl_version}

%description -n texlive-fodot
This package provides helpful commands to work with the fodot language in LaTeX
including syntax highlighting in listings. The fodot language itself is not
introduced. Instead, please refer to the official documentation: Official
documentation of fodot: https://fo-dot.readthedocs.io/en/latest/FO-dot.html
Technical implementation of fodot:
https://docs.idp-z3.be/en/stable/introduction.html Reasoning engine IDP-Z3
(using fodot): https://idp-z3.be/.

%package -n texlive-formal-grammar
Summary:        Typeset formal grammars
Version:        svn61955
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(newfloat.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(formal-grammar.sty) = %{tl_version}

%description -n texlive-formal-grammar
This package provides a new environment and associated commands to typeset BNF
grammars. It allows to easily write formal grammars. Its original motivation
was to typeset grammars for beamer presentations, therefore, there are macros
to emphasize or downplay some parts of the grammar (which is the main novelty
compared to other BNF packages).

%package -n texlive-fouridx
Summary:        Left sub- and superscripts in maths mode
Version:        svn32214
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fouridx.sty) = %{tl_version}

%description -n texlive-fouridx
The package enables left subscripts and superscripts in maths mode. The sub-
and superscripts are raised for optimum fitting to the symbol indexed, in such
a way that left and right sub- and superscripts are set on the same level, as
appropriate. The package provides an alternative to the use of the \sideset
command in the amsmath package.

%package -n texlive-freealign
Summary:        Align math formulas in different lines
Version:        svn69267
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(zref-savepos.sty)
Provides:       tex(freealign.sty) = %{tl_version}

%description -n texlive-freealign
This package provides several commands for aligning math formulas in different
lines.

%package -n texlive-freemath
Summary:        LaTeX maths without backslashes
Version:        svn76930
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(freemath.sty) = %{tl_version}

%description -n texlive-freemath
This package allows for the omission of backslashes from most math mode
commands. Specifically, any consecutive string of at least two (Latin) letters
appearing in math mode will automatically be turned into the control sequence
with the same name, if it exists. The package provides the \freemathon and
\freemathoff commands which respectively activate and deactivate this
behaviour. It is disabled by default upon loading. Regular commands initiated
by a backslash may of course still be used when freemath is active, and can
furthermore be freely mixed with backslash-free commands.

%package -n texlive-functan
Summary:        Macros for functional analysis and PDE theory
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Provides:       tex(functan.sty) = %{tl_version}

%description -n texlive-functan
This package provides a convenient and coherent way to deal with name of
functional spaces (mainly Sobolev spaces) in functional analysis and PDE
theory. It also provides a set of macros for dealing with norms, scalar
products and convergence with some object oriented flavor (it gives the
possibility to override the standard behavior of norms, ...).

%package -n texlive-galois
Summary:        Typeset Galois connections
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(galois.sty) = %{tl_version}

%description -n texlive-galois
The package deals with connections in two-dimensional style, optionally in
colour.

%package -n texlive-gastex
Summary:        Graphs and Automata Simplified in TeX
Version:        svn69842
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(auto-pst-pdf.sty)
Requires:       tex(calc.sty)
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(pst-pdf.sty)
Requires:       tex(trig.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(gastex.sty) = %{tl_version}

%description -n texlive-gastex
GasTeX is a set of LaTeX macros which enable the user to draw graphs, automata,
nets, diagrams, etc., very easily, in the LaTeX picture environment.

%package -n texlive-gene-logic
Summary:        Typeset logic formulae, etc.
Version:        svn75878
License:        Crossword
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gn-logic14.sty) = %{tl_version}

%description -n texlive-gene-logic
The package provides a facility to typeset certain logic formulae. It provides
an environment like eqnarray, a newtheorem-like environment (NewTheorem), and
several macros.

%package -n texlive-ghsystem
Summary:        Globally harmonised system of chemical (etc) naming
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(chemmacros.sty)
Requires:       tex(xparse.sty)
Provides:       tex(ghsystem.sty) = %{tl_version}
Provides:       tex(ghsystem_acid-8.tex) = %{tl_version}
Provides:       tex(ghsystem_acid.tex) = %{tl_version}
Provides:       tex(ghsystem_aqpol.tex) = %{tl_version}
Provides:       tex(ghsystem_bottle-2-black.tex) = %{tl_version}
Provides:       tex(ghsystem_bottle-2-white.tex) = %{tl_version}
Provides:       tex(ghsystem_bottle.tex) = %{tl_version}
Provides:       tex(ghsystem_english.def) = %{tl_version}
Provides:       tex(ghsystem_exclam.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-1.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-2.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-3.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-4.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-5.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-6.tex) = %{tl_version}
Provides:       tex(ghsystem_explos.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-2-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-2-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-3-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-3-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-1.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-2.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-3-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-3-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-5-2-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-5-2-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-O-5-1.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-O.tex) = %{tl_version}
Provides:       tex(ghsystem_flame.tex) = %{tl_version}
Provides:       tex(ghsystem_french.def) = %{tl_version}
Provides:       tex(ghsystem_german.def) = %{tl_version}
Provides:       tex(ghsystem_health.tex) = %{tl_version}
Provides:       tex(ghsystem_italian.def) = %{tl_version}
Provides:       tex(ghsystem_langtemplate.def) = %{tl_version}
Provides:       tex(ghsystem_skull-2.tex) = %{tl_version}
Provides:       tex(ghsystem_skull-6.tex) = %{tl_version}
Provides:       tex(ghsystem_skull.tex) = %{tl_version}
Provides:       tex(ghsystem_spanish.def) = %{tl_version}

%description -n texlive-ghsystem
The package provides the means to typeset all the hazard and precautionary
statements and pictograms in a straightforward way. The statements are taken
from EU regulation 1272/2008.

%package -n texlive-glosmathtools
Summary:        Mathematical nomenclature tools based on the glossaries package
Version:        svn55920
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(glossaries.sty)
Provides:       tex(glosmathtools.sty) = %{tl_version}

%description -n texlive-glosmathtools
This package can be used to generate a mathematical nomenclature (also called
"list of symbols" or "notation"). It is based on the glossaries package. Its
main features are: symbol categories (e.g.: latin, greek) automatic but
customizable symbol sorting easy subscript management easy accentuation
management abbreviation support (with first use definition) bilingual
nomenclatures (for bilingual documents) bilingual abbreviations The
documentation is based on the ulthese class. The package itself depends on
glossaries, amsmath, amsfonts, and etoolbox.

%package -n texlive-gotoh
Summary:        An implementation of the Gotoh sequence alignment algorithm
Version:        svn44764
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(gotoh.sty) = %{tl_version}

%description -n texlive-gotoh
This package calculates biological sequence alignment with the Gotoh algorithm.
The package also provides an interface to control various settings including
algorithm parameters.

%package -n texlive-grundgesetze
Summary:        Typeset Frege's Grundgesetze der Arithmetik
Version:        svn58997
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bguq.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(grundgesetze.sty) = %{tl_version}

%description -n texlive-grundgesetze
The package defines maths mode commands for typesetting Gottlob Frege's
concept-script in the style of his "Grundgesetze der Arithmetik" (Basic Laws of
Arithmetic).

%package -n texlive-gu
Summary:        Typeset crystallographic group-subgroup-schemes
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tabularx.sty)
Provides:       tex(gu.sty) = %{tl_version}

%description -n texlive-gu
The package simplifies typesetting of simple crystallographic
group-subgroup-schemes in the Barnighausen formalism. It defines a new
environment stammbaum, wherein all elements of the scheme are defined.
Afterwards all necessary dimensions are calculated and the scheme is drawn.
Currently two steps of symmetry reduction are supported.

%package -n texlive-helmholtz-ellis-ji-notation
Summary:        Beautiful in-line microtonal just intonation accidentals
Version:        svn55213
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(helmholtz-ellis-ji-notation.sty) = %{tl_version}

%description -n texlive-helmholtz-ellis-ji-notation
The Helmholtz-Ellis JI Pitch Notation (HEJI), devised in the early 2000s by
Marc Sabat and Wolfgang von Schweinitz, explicitly notates the raising and
lowering of the untempered diatonic Pythagorean notes by specific microtonal
ratios defined for each prime. It provides visually distinctive "logos"
distinguishing families of justly tuned intervals that relate to the harmonic
series. These take the form of strings of additional accidental symbols based
on historical precedents, extending the traditional sharps and flats. Since its
2020 update, HEJI ver. 2 ("HEJI2") provides unique microtonal symbols through
the 47-limit. This package is a simple LaTeX implementation of HEJI2 that
allows for in-line typesetting of microtonal accidentals for use within
theoretical texts, program notes, symbol legends, etc. Documents must be
compiled using XeLaTeX.

%package -n texlive-hep-graphic
Summary:        Extensions for graphics, plots and feynman graphs in high energy physics
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz-feynman.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tikzscale.sty)
Requires:       tex(xparse.sty)
Provides:       tex(hep-feynman.sty) = %{tl_version}
Provides:       tex(hep-graphic.sty) = %{tl_version}
Provides:       tex(hep-plot.sty) = %{tl_version}

%description -n texlive-hep-graphic
The hep-graphic package collects convenience macros that modify the behaviour
of the TikZ, pgfplots, and TikZ-Feynman packages and ensure that the generated
graphics look consistent.

%package -n texlive-hep-reference
Summary:        Adjustments for publications in High Energy Physics
Version:        svn76220
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cleveref.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(footnotebackref.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(hep-reference.sty) = %{tl_version}

%description -n texlive-hep-reference
This package makes some changes to the reference, citation and footnote macros
to improve the default behavior of LaTeX for High Energy Physics publications.

%package -n texlive-hepnames
Summary:        Pre-defined high energy particle names
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(hepparticles.sty)
Requires:       tex(xspace.sty)
Provides:       tex(hepnames.sty) = %{tl_version}
Provides:       tex(hepnicenames.sty) = %{tl_version}
Provides:       tex(heppennames.sty) = %{tl_version}

%description -n texlive-hepnames
Hepnames provides a pair of LaTeX packages, heppennames and hepnicenames,
providing a large set of pre-defined high energy physics particle names built
with the hepparticles package. The packages are based on pennames.sty by Michel
Goossens and Eric van Herwijnen. Heppennames re-implements the particle names
in pennames.sty, with some additions and alterations and greater flexibility
and robustness due to the hepparticles structures, which were written for this
purpose. Hepnicenames provides the main non-resonant particle names from
heppennames with more "friendly" names.

%package -n texlive-hepparticles
Summary:        Macros for typesetting high energy physics particle names
Version:        svn35723
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(subdepth.sty)
Provides:       tex(hepparticles.sty) = %{tl_version}

%description -n texlive-hepparticles
HEPparticles is a set of macros for typesetting high energy particle names, to
meet the following criteria: 1. The main particle name is a Roman or Greek
symbol, to be typeset in upright font in normal contexts. 2. Additionally a
superscript and/or subscript may follow the main symbol. 3. Particle resonances
may also have a resonance specifier which is typeset in parentheses following
the main symbol. In general the parentheses may also be followed by sub- and
superscripts. 4. The particle names are expected to be used both in and out of
mathematical contexts. 5. If the surrounding text is bold or italic then the
particle name should adapt to that context as best as possible (this may not be
possible for Greek symbols). A consequence of point 5 is that the well-known
problems with boldness of particle names in section titles, headers and tables
of contents automatically disappear if these macros are used.

%package -n texlive-hepthesis
Summary:        A class for academic reports, especially PhD theses
Version:        svn46054
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hepthesis
Hepthesis is a LaTeX class for typesetting large academic reports, in
particular PhD theses. It was originally developed for typesetting the author's
high-energy physics PhD thesis and includes some features specifically tailored
to such an application. In particular, hepthesis offers: Attractive semantic
environments for various rubric sections; Extensive options for draft
production, screen viewing and binding-ready output; Helpful extensions of
existing environments, including equation and tabular; and Support for
quotations at the start of the thesis and each chapter. The class is based on
scrbook, from the KOMA-Script bundle.

%package -n texlive-hepunits
Summary:        A set of units useful in high energy physics applications
Version:        svn54758
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(siunitx.sty)
Provides:       tex(hepunits.sty) = %{tl_version}

%description -n texlive-hepunits
Hepunits is a LaTeX package built on the SIunits package which adds a
collection of useful HEP units to the existing SIunits set. These include the
energy units \MeV, \GeV, \TeV and the derived momentum and mass units
\MeVoverc, \MeVovercsq and so on.

%package -n texlive-hideproofs
Summary:        Defines a starred proof environment that hides proofs in draft mode
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsthm.sty)
Requires:       tex(environ.sty)
Requires:       tex(ifdraft.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(hideproofs.sty) = %{tl_version}

%description -n texlive-hideproofs
This package introduces an alternate proof environment, proof*, which
conditionally hides or shows its contents based on the document mode (draft,
final, or default). This is useful for omitting formal proofs from draft
versions while retaining them in final documents. The motivation for this
package is to reduce the clutter in large files by omitting long proofs,
allowing authors to focus their attention on results or proofs that are
currently works in progress.

%package -n texlive-ibrackets
Summary:        Intelligent brackets
Version:        svn67736
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ibrackets.sty) = %{tl_version}

%description -n texlive-ibrackets
This small package provides a new definition of brackets [ and ] as active
characters to get correct blank spaces in mathematical mode when using for open
intervals. Instead of parenthesis: ]-\infty, 0[ is equivalent to (-\infty, 0).

%package -n texlive-includernw
Summary:        Include .Rnw inside .tex
Version:        svn47557
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Provides:       tex(includeRnw.sty) = %{tl_version}

%description -n texlive-includernw
This package is for including .Rnw (knitr/sweave)-files inside .tex-files. It
requires that you have R and the R-package knitr installed. Note: This package
will probably not work on Windows. It is tested only on OS X, and will probably
also work on standard Linux distros.

%package -n texlive-interval
Summary:        Format mathematical intervals, ensuring proper spacing
Version:        svn50265
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfkeys.sty)
Provides:       tex(interval.sty) = %{tl_version}

%description -n texlive-interval
When typing an open interval as $]a,b[$, a closing bracket is being used in
place of an opening fence and vice versa. This leads to the wrong spacing in,
say, $]-a,b[$ or $A\in]a,b[=B$. The package attempts to solve this using:
\interval{a}{b} -> [a,b] \interval[open]{a}{b} -> ]a,b[ \interval[open
left]{a}{b} -> ]a,b] The package also supports fence scaling and ensures that
the enclosing fences will end up having the proper closing and opening types.
TeX maths does not do this job properly. The package depends on pgfkeys.

%package -n texlive-intexgral
Summary:        A LaTeX package for typesetting integrals
Version:        svn77252
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(derivative.sty)
Provides:       tex(intexgral.sty) = %{tl_version}

%description -n texlive-intexgral
Typesetting integrals, although common in LaTeX, is not particularly practical.
The way in which the different parts are managed often generates unreadable
source code, making modifications laborious. The package therefore follows a
simple philosophy: focus on the essential element of an integral, the
integrand. Everything else (limits, differentials, symbols) can be modified
using keys. These keys are designed to allow you to easily and quickly change
the style of an integral. Additionally, the package provides various auxiliary
macros to support some keys which can have lengthy inputs.

%package -n texlive-ionumbers
Summary:        Restyle numbers in maths mode
Version:        svn76924
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(ionumbers.sty) = %{tl_version}

%description -n texlive-ionumbers
'ionumbers' stands for 'input/output numbers'. The package restyles numbers in
maths mode. If a number in the input file is written, e.g., as $3,231.44$ as
commonly used in English texts, the package is able to restyle it to be output
as $3\,231{,}44$ as commonly used in German texts (and vice versa). This may be
useful, for example, if you have a large table and want to include it in texts
with different output conventions without the need to change the table. The
package can also automatically group digits left of the decimal separator
(thousands) and right of the decimal separator (thousandths) in triplets
without the need of specifying commas (English) or points (German) as
separators. E.g., the input $1234.567890$ can be output as $1\,234.\,567\,890$.
Finally, an e starts the exponent of the number. For example, $21e6$ may be
output as $26\times10\,^{6}$.

%package -n texlive-isomath
Summary:        Mathematics style for science and technology
Version:        svn27654
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fixmath.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(isomath.sty) = %{tl_version}

%description -n texlive-isomath
The package provides tools for a mathematical style that conforms to the
International Standard ISO 80000-2 and is common in science and technology. It
changes the default shape of capital Greek letters to italic, sets up bold
italic and sans-serif bold italic math alphabets with Latin and Greek
characters, and defines macros for markup of vector, matrix and tensor symbols.

%package -n texlive-isphysicalmath
Summary:        Simple way to write nice formulas
Version:        svn73239
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xstring.sty)
Provides:       tex(isphysicalmath.sty) = %{tl_version}

%description -n texlive-isphysicalmath
This package helps users to write mathematical and physical contents according
to scientific notation (international mainly), in an elegant way. It deals with
the notation and formatting of formulas, quantities, numerical values, factors,
dimensions, measurement units and also performs its activities in complex
mathematical environments.

%package -n texlive-jkmath
Summary:        Macros for mathematics that make the code more readable
Version:        svn47109
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(physics.sty)
Requires:       tex(xparse.sty)
Provides:       tex(jkmath.sty) = %{tl_version}

%description -n texlive-jkmath
Inspired by the physicspackage on CTAN, the package defines some simple macros
for mathematical notation which make the code more readable and/or allow
flexibility in typesetting material.

%package -n texlive-jupynotex
Summary:        Include whole or partial Jupyter notebooks in LaTeX documents
Version:        svn75037
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfopts.sty)
Requires:       tex(tcolorbox.sty)
Provides:       tex(jupynotex.sty) = %{tl_version}

%description -n texlive-jupynotex
This package provides a python3 script and a LaTeX .sty file which can be used
together to include Jupyter Notebooks (all of them, or some specific cells) as
part of a LaTeX document. It will convert the Jupyter Notebook format to proper
LaTeX so it gets included seamlessly, supporting text, LaTeX, images, etc.

%package -n texlive-karnaugh
Summary:        Typeset Karnaugh-Veitch-maps
Version:        svn21338
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(kvmacros.tex) = %{tl_version}

%description -n texlive-karnaugh
The package provides macros for typesetting Karnaugh-Maps and Veitch-Charts in
a simple and user-friendly way. Karnaugh-Maps and Veitch-Charts are used to
display and simplify logic functions "manually". These macros can typeset
Karnaugh-Maps and Veitch-Charts with up to ten variables (=1024 entries).

%package -n texlive-karnaugh-map
Summary:        LaTeX package for drawing karnaugh maps with up to 6 variables
Version:        svn61614
License:        CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(karnaugh-map.sty) = %{tl_version}

%description -n texlive-karnaugh-map
This package draws karnaugh maps with 2, 3, 4, 5, and 6 variables. It also
contains commands for filling the karnaugh map with terms semi-automatically or
manually. Last but not least it contains commands for drawing implicants on top
of the map. This package depends on the keyval, kvoptions, TikZ, xparse, and
xstring packages.

%package -n texlive-karnaughmap
Summary:        Typeset Karnaugh maps
Version:        svn36989
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(karnaughmap.sty) = %{tl_version}

%description -n texlive-karnaughmap
This package provides an easy to use interface to typeset Karnaugh maps using
TikZ. Though similar to the karnaugh macros, it provides a key-value system to
customize karnaughmaps and a proper LaTeX package.

%package -n texlive-keytheorems
Summary:        An l3keys interface to amsthm
Version:        svn77073
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(aliascnt.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(refcount.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(thmtools.sty)
Requires:       tex(translations.sty)
Requires:       tex(unique.sty)
Provides:       tex(keytheorems.sty) = %{tl_version}
Provides:       tex(keythms-IEEEtran-support.tex) = %{tl_version}
Provides:       tex(keythms-amsart-support.tex) = %{tl_version}
Provides:       tex(keythms-amsbook-support.tex) = %{tl_version}
Provides:       tex(keythms-amsproc-support.tex) = %{tl_version}
Provides:       tex(keythms-beamer-support.tex) = %{tl_version}
Provides:       tex(keythms-jlreq-support.tex) = %{tl_version}
Provides:       tex(keythms-ltx-talk-support.tex) = %{tl_version}
Provides:       tex(keythms-memoir-support.tex) = %{tl_version}

%description -n texlive-keytheorems
An expl3-implementation of a key-value interface to amsthm, implementing most
of the functionality provided by thmtools. Several issues encountered with
thmtools are avoided (see the README for a list) and a few new features are
added.

%package -n texlive-kvmap
Summary:        Create Karnaugh maps with LaTeX
Version:        svn67201
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-amsmath
Requires:       texlive-l3experimental
Requires:       texlive-pgf
Requires:       tex(amsmath.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(kvmap.sty) = %{tl_version}

%description -n texlive-kvmap
This LaTeX package allows the creation of (even large) Karnaugh maps. It
provides a tabular-like input syntax and support for drawing bundles
(implicants) around adjacent values. It is based on an answer at StackExchange.

%package -n texlive-letterswitharrows
Summary:        Draw arrows over math letters
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(mathtools.sty)
Requires:       tex(pgf.sty)
Requires:       tex(xparse.sty)
Provides:       tex(letterswitharrows.sty) = %{tl_version}

%description -n texlive-letterswitharrows
This package provides LaTeX math-mode commands for setting left and right
arrows over mathematical symbols so that the arrows dynamically scale with the
symbols. While it is possible to set arrows over longer strings of symbols, the
focus lies on single characters.

%package -n texlive-lie-hasse
Summary:        Draw Hasse diagrams
Version:        svn75301
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(contour.sty)
Requires:       tex(dynkin-diagrams.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(lie-hasse.sty) = %{tl_version}

%description -n texlive-lie-hasse
This package draws Hasse diagrams of the partially ordered sets of the simple
roots of any complex simple Lie algebra. It uses the Dynkin diagrams package
dynkin-diagrams.

%package -n texlive-linearregression
Summary:        Calculate and display linear regressions
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(linearregression.sty) = %{tl_version}

%description -n texlive-linearregression
This package provides the definition of some document-level commands (and some
auxiliary functions) that perform the linear regression on a set of data and
present the data and the results in tabular and in graphic form.

%package -n texlive-linkedthm
Summary:        Hyperlinked theorem-proof environments for LaTeX
Version:        svn75860
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsthm.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(xparse.sty)
Provides:       tex(linkedthm.sty) = %{tl_version}

%description -n texlive-linkedthm
This package provides lightweight infrastructure for bidirectional linking
between theorem-like environments and their corresponding proofs. It
automatically adds a [Proof] hyperlink at the end of a theorem and a restated
version with a [Return] link inside the proof. You can declare any number of
custom linked environments (e.g., linkeddefinition, linkedexample) using
\DeclareLinkedTheorem, and base them on any amsthm-compatible environment. This
is useful for mathematical writing and documentation, where proof navigation is
essential. The package uses amsthm, xparse, and hyperref, and is compatible
with all standard LaTeX engines.

%package -n texlive-logicproof
Summary:        Box proofs for propositional and predicate logic
Version:        svn33254
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(logicproof.sty) = %{tl_version}

%description -n texlive-logicproof
A common style of proof used in propositional and predicate logic is Fitch
proofs, in which each line of the proof has a statement and a justification,
and subproofs within a larger proof have boxes around them. The package
provides environments for typesetting such proofs and boxes. It creates proofs
in a style similar to that used in "Logic in Computer Science" by Huth and
Ryan.

%package -n texlive-logictools
Summary:        Additional tools for typesetting formal logic
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(bussproofs.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(xfrac.sty)
Provides:       tex(logictools.sty) = %{tl_version}

%description -n texlive-logictools
Adds various tools for typesetting formal logic, including: An environment that
makes it easier to produce good looking formal logic. A few macros that would
be of interest to people studying logic at Oxford (or other places with similar
notational conventions).

%package -n texlive-longdivision
Summary:        Typesets long division
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(longdivision.sty) = %{tl_version}

%description -n texlive-longdivision
This package executes the long division algorithm and typesets the solutions.
The dividend must be a positive decimal number and the divisor must be a
positive integer. Repeating decimals is handled correctly, putting a bar over
the repeated part of the decimal. Dividends up to 20 digits long are handled
gracefully (though the typeset result will take up about a page), and dividends
between 20 and 60 digits long slightly less gracefully. The package defines two
macros, \longdivision and \intlongdivision. Each takes two arguments, a
dividend and a divisor. \longdivision keeps dividing until the remainder is
zero, or it encounters a repeated remainder. \intlongdivision stops when the
dividend stops (though the dividend doesn't have to be an integer). This
package depends on the xparse package from the l3packages bundle.

%package -n texlive-lpform
Summary:        Typesetting linear programming formulations and sets of equations
Version:        svn36918
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xifthen.sty)
Provides:       tex(lpform.sty) = %{tl_version}

%description -n texlive-lpform
The package is designed to aid the author writing linear programming
formulations, one restriction at a time. With the package, one can easily label
equations, formulations can span multiple pages and several elements of the
layout (such as spacing, texts and equation tags) are also customizable.
Besides linear programming formulations, this package can also be used to
display any series of aligned equations with easy labeling/referencing and
other customization options.

%package -n texlive-lplfitch
Summary:        Fitch-style natural deduction proofs
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lplfitch.sty) = %{tl_version}

%description -n texlive-lplfitch
The package provides macros for typesetting natural deduction proofs in "Fitch"
style, with subproofs indented and offset by scope lines. The proofs from use
of the package are in the format used in the textbook "Language, Proof, and
Logic" by Dave Barker-Plummer, Jon Barwise, and John Etchemendy. (In fact, the
prefix "lpl" in the package name stands for "Language, Proof, and Logic".)

%package -n texlive-lstbayes
Summary:        Listings language driver for Bayesian modeling languages
Version:        svn48160
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Provides:       tex(lstbayes.sty) = %{tl_version}

%description -n texlive-lstbayes
The package provides language drivers for the listings package for several
languages not included in that package: BUGS, JAGS, and Stan.

%package -n texlive-lua-regression
Summary:        Add polynomial regressions to graphs
Version:        svn74969
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(luacode.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfplots.sty)
Provides:       tex(lua-regression.sty) = %{tl_version}

%description -n texlive-lua-regression
This LuaLaTeX package provides a simple interface for performing polynomial
regression on data sets. It allows users to specify the order of the polynomial
regression, the columns of the data set to use, and whether to plot the
results. The package also includes options for confidence intervals and error
bands.

%package -n texlive-luanumint
Summary:        Numerical integration using Lua inside LaTeX documents
Version:        svn68918
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(breqn.sty)
Requires:       tex(luacode.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luanumint.sty) = %{tl_version}

%description -n texlive-luanumint
This package uses Lua to calculate the numerical integral value of real-valued
functions of a real variable over closed and bounded intervals. The package
provides commands to perform numerical integration using the mid-point,
trapezoidal, and Simpson's one-third and three-eighth rules. The loadstring
command is used to load and evaluate functions at different points in the
mathematics environment of Lua. The package also provides commands to perform
numerical integration using step-by-step calculations. The package's commands
have an optional argument to round off the numbers to the desired number of
decimal places. The breqn package is loaded to display and align step-by-step
calculations properly. Advanced users can customize the code to achieve the
desired formatting of step-by-step computations. The package can assist in
creating various problems on numerical integration with their solutions. The
results obtained using different methods of numerical integration can be
compared. It can save users' efforts of doing computations involving numerical
integration in external software and copying them inside LaTeX documents.

%package -n texlive-math-operator
Summary:        Predefined and new math operators
Version:        svn76273
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(math-operator.sty) = %{tl_version}

%description -n texlive-math-operator
This package defines control sequences for roughly one hundred and fifty math
operators, including special functions, probability distributions, pure
mathematical constructions, and a variant of \overline. The package also
provides an interface for users to define new math operators similar to the
amsopn package. New operators can be medium or bold weight, and they may be
declared as \mathord or \mathop subformulas.

%package -n texlive-mathcommand
Summary:        \newcommand-like commands for defining math macros
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(xparse.sty)
Provides:       tex(mathcommand.sty) = %{tl_version}

%description -n texlive-mathcommand
This package provides functionalities for defining macros that have different
behaviors depending on whether in math or text mode, that absorb Primes,
Indices and Exponents (PIE) as extra parameters usable in the code; and it
offers some iteration facilities for defining macros with similar code. The
primary objective of this package is to be used together with the knowledge
package for a proper handling of mathematical notations.

%package -n texlive-mathcomp
Summary:        Text symbols in maths mode
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(textcomp.sty)
Provides:       tex(mathcomp.sty) = %{tl_version}

%description -n texlive-mathcomp
A package which provides access to some interesting characters of the Text
Companion fonts (TS1 encoding) in maths mode.

%package -n texlive-mathfixs
Summary:        Fix various layout issues in math mode
Version:        svn74752
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(mathfixs.sty) = %{tl_version}

%description -n texlive-mathfixs
This is a LaTeX2e package to fix some odd behaviour in math mode such as
spacing around fractions and roots, math symbols within bold text as well as
capital Greek letters. It also adds some related macros.

%package -n texlive-mathlig
Summary:        Define maths "ligatures"
Version:        svn54244
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mathlig.tex) = %{tl_version}

%description -n texlive-mathlig
The package defines character sequences that "behave like" ligatures, in maths
mode. Example definitions (chosen to show the package's flexibility, are:
\mathlig{->}{\rightarrow} \mathlig{<-}{\leftarrow}
\mathlig{<->}{\leftrightarrow}

%package -n texlive-mathpartir
Summary:        Typesetting sequences of math formulas, e.g. type inference rules
Version:        svn76924
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mathpartir.sty) = %{tl_version}

%description -n texlive-mathpartir
The package provides macros for typesetting math formulas in mixed horizontal
and vertical mode, automatically as best fit. It provides an environment
mathpar that behaves much as a loose centered paragraph where words are math
formulas, and spaces between them are larger and adjustable. It also provides a
macro \inferrule for typesetting fractions where both the numerator and
denominator may be sequences of formulas that will be also typeset in a similar
way. It can typically be used for typesetting sets of type inference rules or
typing derivations. A macro inferrule for typesetting type inference rules.

%package -n texlive-mathpunctspace
Summary:        Control the space after punctuation in math expressions
Version:        svn46754
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(mathpunctspace.sty) = %{tl_version}

%description -n texlive-mathpunctspace
This package provides a mechanism to control the space after commas and
semicolons in mathematical expressions.

%package -n texlive-mathsemantics
Summary:        Semantic math commands in LaTeX
Version:        svn63241
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Provides:       tex(mathsemantics-abbreviations.sty) = %{tl_version}
Provides:       tex(mathsemantics-commons.sty) = %{tl_version}
Provides:       tex(mathsemantics-manifolds.sty) = %{tl_version}
Provides:       tex(mathsemantics-names.sty) = %{tl_version}
Provides:       tex(mathsemantics-optimization.sty) = %{tl_version}
Provides:       tex(mathsemantics-semantic.sty) = %{tl_version}
Provides:       tex(mathsemantics-syntax.sty) = %{tl_version}
Provides:       tex(mathsemantics.sty) = %{tl_version}

%description -n texlive-mathsemantics
This LaTeX package provides both syntactic and semantic helpers to typeset
mathematics in LaTeX. The syntactic layer eases typesetting of formulae in
general, while the semantic layer provides commands like \inner{x}{y} to unify
typesetting of inner products. These not only unify typesetting of math
formulae but also allow to easily adapt notation if a user prefers to. The
semantic layer is split into topics.

%package -n texlive-matlab-prettifier
Summary:        Pretty-print Matlab source code
Version:        svn34323
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(matlab-prettifier.sty) = %{tl_version}

%description -n texlive-matlab-prettifier
The package extends the facilities of the listings package, to pretty-print
Matlab and Octave source code. (Note that support of Octave syntax is not
complete.)

%package -n texlive-matrix-skeleton
Summary:        A PGF/TikZ library that simplifies working with multiple matrix nodes
Version:        svn65013
License:        ISC
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pgflibrarymatrix.skeleton.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarymatrix.skeleton.code.tex) = %{tl_version}

%description -n texlive-matrix-skeleton
The package provides a PGF/TikZ library that simplifies working with multiple
matrix nodes. To do so, it correctly aligns groups of nodes with the content of
the whole matrix. Furthermore, matrix.skeleton provides rows and columns for
easy styling.

%package -n texlive-mattens
Summary:        Matrices/tensor typesetting
Version:        svn62326
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Provides:       tex(mattens.sty) = %{tl_version}

%description -n texlive-mattens
The mattens package contains the definitions to typeset matrices, vectors and
tensors as used in the engineering community for the representation of common
vectors and tensors such as forces, velocities, moments of inertia, etc.

%package -n texlive-mecaso
Summary:        Formulas frequently used in rigid body mechanics
Version:        svn60346
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(mathrsfs.sty)
Provides:       tex(mecaso.sty) = %{tl_version}

%description -n texlive-mecaso
This package provides a number of formulas frequently used in rigid body
mechanics. Since most of these formulas are long and tedious to write, this
package wraps them up in short commands.

%package -n texlive-medmath
Summary:        Better medium-size math commands
Version:        svn74208
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(etoolbox.sty)
Provides:       tex(medmath.sty) = %{tl_version}

%description -n texlive-medmath
This package started as a fork of the mediummath code of the nccmath package,
aiming to provide more stable and flexible medium-size math commands. This
concerns sizes of operators and infinite loops caused by definite integrals.

%package -n texlive-membranecomputing
Summary:        Membrane Computing notation
Version:        svn64627
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(xstring.sty)
Provides:       tex(membranecomputing.sty) = %{tl_version}

%description -n texlive-membranecomputing
This is a LaTeX package for the Membrane Computing community. It comprises the
definition of P systems, rules and some concepts related to languages and
computational complexity usually needed for Membrane Computing research. The
package depends on ifthen and xstring.

%package -n texlive-memorygraphs
Summary:        TikZ styles to typeset graphs of program memory
Version:        svn49631
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(memorygraphs.sty) = %{tl_version}

%description -n texlive-memorygraphs
This package defines some TikZ styles and adds anchors to existing styles that
ease the declaration of "memory graphs". It is intended for graphs that
represent the memory of a computer program during its execution.

%package -n texlive-messagepassing
Summary:        Draw diagrams to represent communication protocols
Version:        svn69123
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(messagepassing.sty) = %{tl_version}

%description -n texlive-messagepassing
This package provides an environment to easily draw diagrams to represent
communication protocols using message passing among processes. Processes are
represented as horizontal or vertical lines, and communications as arrows
between lines. The package also provides multiple macros to decorate those
diagrams, for instance to annotate the diagram, to add crashes to the
processes, checkpoints, ...

%package -n texlive-mgltex
Summary:        High-quality graphics from MGL scripts embedded in LaTeX documents
Version:        svn63255
License:        GPL-3.0-only AND CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(mgltex.sty) = %{tl_version}

%description -n texlive-mgltex
This package allows you to create high-quality publication-ready graphics
directly from MGL scripts embedded into your LaTeX document, using the MathGL
library. Besides following the LaTeX philosophy of allowing you to concentrate
on content rather than output (mglTeX takes care of producing the output),
mglTeX facilitates the maintenance of your document, since both code for text
and code for plots are contained in a single file. MathGL. is a fast and
efficient library by Alexey Balakin for the creation of high-quality
publication-ready scientific graphics. Although it defines interfaces for many
programming languages, it also implements its own scripting language, called
MGL, which can be used independently.

%package -n texlive-mhchem
Summary:        Typeset chemical formulae/equations and H and P statements
Version:        svn69639
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-amsmath
Requires:       texlive-chemgreek
Requires:       texlive-graphics
Requires:       texlive-l3kernel
Requires:       texlive-l3packages
Requires:       texlive-tools
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(chemgreek.sty)
Requires:       tex(graphics.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgf.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(hpstatement-bg.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-cs.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-da.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-de.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-el.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-en.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-es.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-et.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-fi.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-fr.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-ga.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-hr.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-hu.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-it.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-lt.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-lv.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-mt.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-nl.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-pl.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-pt.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-ro.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-sk.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-sl.inc.sty) = %{tl_version}
Provides:       tex(hpstatement-sv.inc.sty) = %{tl_version}
Provides:       tex(hpstatement.sty) = %{tl_version}
Provides:       tex(mhchem.sty) = %{tl_version}
Provides:       tex(rsphrase.sty) = %{tl_version}

%description -n texlive-mhchem
The bundle provides three packages: The mhchem package provides commands for
typesetting chemical molecular formulae and equations. The hpstatement package
provides commands for the official hazard statements and precautionary
statements (H and P statements) that are used to label chemicals. The rsphrase
package provides commands for the official Risk and Safety (R and S) Phrases
that are used to label chemicals. The package requires the expl3 bundle.

%package -n texlive-mhequ
Summary:        Multicolumn equations, tags, labels, sub-numbering
Version:        svn64978
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mhequ.sty) = %{tl_version}

%description -n texlive-mhequ
The mhequ style file simplifies creating multi-column equation environments and
tagging equations therein. It supports sub-numbering of blocks of equations
(like (1.2a), (1.2b), etc) and references to each equation individually (1.2a)
or to the whole block (1.2). The labels can be shown in draft mode. The default
behaviour is to show an equation number if and only if the equation actually
has a label, which reduces visual clutter. Comments in the package itself
describe its usage, which should also be self-evident from the provided example
file.

%package -n texlive-miller
Summary:        Typeset miller indices
Version:        svn18789
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(miller.sty) = %{tl_version}

%description -n texlive-miller
Typeset miller indices, e.g., <1-20>, that are used in material science with an
easy syntax. Minus signs are printed as bar above the corresponding number.

%package -n texlive-mismath
Summary:        Miscellaneous mathematical macros
Version:        svn76547
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(decimalcomma.sty)
Requires:       tex(esvect.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ibrackets.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(mleftright.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Provides:       tex(mismath.sty) = %{tl_version}

%description -n texlive-mismath
The package provides some mathematical macros to typeset: mathematical
constants e, i, p in upright shape (automatically) as recommended by ISO
80000-2, vectors with nice arrows and adjusted norm (and tensors), tensors in
sans serif bold italic shape, some standard operator names, improved spacings
in mathematical formulas, systems of equations and small matrices, displaymath
in double columns for lengthy calculations.

%package -n texlive-moremath
Summary:        Additional commands for typesetting maths
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(mathtools.sty)
Provides:       tex(moremath.sty) = %{tl_version}

%description -n texlive-moremath
This package provides several document level commands to ease typesetting of
maths with LaTeX. This package provides complementary commands to all operators
defined by amsmath which typeset the operators together with delimiters (which
can be scaled manually, automatically or not at all). These commands also
accept optional sub- and superscripts. Additionally, this package provides
several commands to typeset gradient, divergence, curl, Laplace, and d'Alembert
operators. Those commands also accept an optional subscript and their
appearance can be modified using key-value options. Furthermore several
commands for producing row and column vectors, as well as (anti-)diagonal
matrices and identity matrices, utilizing mathtools' matrix* family of
environments, are provided. Most of the document level commands defined by this
package can also be disabled using a package load-time option to avoid clashes
with commands defined by other packages. The package depends on mathtools, bm
(optional), and amssymb.

%package -n texlive-multiobjective
Summary:        Symbols for multiobjective optimisation etc.
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Provides:       tex(multiobjective.sty) = %{tl_version}

%description -n texlive-multiobjective
The package provides a series of operators commonly used in papers related to
multiobjective optimisation, multiobjective evolutionary algorithms,
multicriteria decision making and similar fields.

%package -n texlive-naive-ebnf
Summary:        EBNF in plain text
Version:        svn72843
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-filecontentsdef
Requires:       texlive-l3kernel
Requires:       texlive-pgfopts
Requires:       tex(pgfopts.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(naive-ebnf.sty) = %{tl_version}

%description -n texlive-naive-ebnf
With the help of this LaTeX package a context-free grammar (CFG) may be
rendered in a plain-text mode using a simplified Extended Backus-Naur Form
(EBNF) notation.

%package -n texlive-namedtensor
Summary:        Macros for named tensor notation
Version:        svn65346
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Provides:       tex(namedtensor.sty) = %{tl_version}

%description -n texlive-namedtensor
This style file provides macros for named tensor notation. Please see the paper
'Named Tensor Notation' for background on this notation.

%package -n texlive-natded
Summary:        Typeset natural deduction proofs
Version:        svn32693
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Provides:       tex(natded.sty) = %{tl_version}

%description -n texlive-natded
The package provides commands to typeset proofs in the style used by Jaskowski,
or that of Kalish and Montague.

%package -n texlive-nath
Summary:        Natural mathematics notation
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(nath.sty) = %{tl_version}

%description -n texlive-nath
Nath is a LaTeX (both 2e and 2.09) style to separate presentation and content
in mathematical typography. The style delivers a particular context-dependent
presentation on the basis of a rather coarse context-independent notation.
Highlighted features: depending on the context, the command \frac produces
either built-up or case or solidus fractions, with parentheses added whenever
required for preservation of the mathematical meaning; delimiters adapt their
size to the material enclosed, rendering \left and \right almost obsolete.

%package -n texlive-nchairx
Summary:        Maths macros from chair X of Wurzburg University
Version:        svn60196
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(aliascnt.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tensor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(chairxmath.sty) = %{tl_version}
Provides:       tex(nchairx.sty) = %{tl_version}

%description -n texlive-nchairx
This package was developed by members of the chair for mathematical physics at
the University of Wurzburg as a collection of macros and predefined
environments for quickly creating nice mathematical documents. (Note concerning
the package name: the "n" stands for "new", the "X" is a roman 10.)

%package -n texlive-nicematrix
Summary:        Improve the typesetting of mathematical matrices with PGF
Version:        svn77270
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(pgfcore.sty)
Provides:       tex(nicematrix.sty) = %{tl_version}

%description -n texlive-nicematrix
This package is based on the package array. It creates PGF/TikZ nodes under the
cells of the array and uses these nodes to provide functionalities to construct
tabulars, arrays and matrices. Among the features : continuous dotted lines for
the mathematical matrices; exterior rows and columns (so-called border
matrices); control of the width of the columns; tools to color rows and columns
with a good PDF result; blocks of cells; tabular notes; etc. The package
requires and loads array, amsmath, pgfcore, and the module shapes of PGF.

%package -n texlive-nuc
Summary:        Notation for nuclear isotopes
Version:        svn22256
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(nuc.sty) = %{tl_version}

%description -n texlive-nuc
A simple package providing nuclear sub- and superscripts as commonly used in
radiochemistry, radiation science, and nuclear physics and engineering
applications. Isotopes which have Z with more digits than A require special
spacing to appear properly; this spacing is supported in the package.

%package -n texlive-nucleardata
Summary:        Provides data about atomic nuclides for documents
Version:        svn47307
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pythontex.sty)
Requires:       tex(siunitx.sty)
Provides:       tex(nucleardata.sty) = %{tl_version}

%description -n texlive-nucleardata
The package provides data and commands for including nuclear and atomic mass
and energy data in LaTeX documents. It uses the PythonTeX package and requires
pythontex.exe to be called with the TeX file as the argument.

%package -n texlive-numbersets
Summary:        Display number sets with customizable typefaces
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(numbersets.sty) = %{tl_version}

%description -n texlive-numbersets
This package allows users to express mathematical concepts related to sets of
numbers using meaningful commands rather than relying on visual
representations. Key Features: Command to specify typefaces for number sets.
Interface for defining typeface rules. Interface for creating commands that
represent number sets. Several predefined presets for common number sets.

%package -n texlive-numerica
Summary:        Numerically evaluate mathematical expressions in LaTeX form
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(mathtools.sty)
Provides:       tex(numerica.sty) = %{tl_version}

%description -n texlive-numerica
This package defines a command to wrap around a mathematical expression in its
LaTeX form and, once values are assigned to variables, numerically evaluate it.
The intent is to avoid the need to modify the LaTeX form of the expression
being evaluated. For programs with a preview facility like LyX, or
compile-as-you-go systems, interactive back-of-envelope calculations and
numerical exploration are possible within the document being worked on. The
package requires the bundles l3kernel and l3packages, and the amsmath and
mathtools packages.

%package -n texlive-numerica-plus
Summary:        Iteration and recurrence relations: finding fixed points, zeros and extrema of functions
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(numerica-plus.sty) = %{tl_version}

%description -n texlive-numerica-plus
The package defines commands to iterate functions of a single variable, find
fixed points, zeros and extrema of such functions, and calculate the terms of
recurrence relations. numerica-plus requires the package numerica, which in
turn requires l3kernel , l3packages, and the amsmath and mathtools packages.

%package -n texlive-numerica-tables
Summary:        Create multi-column tables of mathematical functions
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(booktabs.sty)
Provides:       tex(numerica-tables.sty) = %{tl_version}

%description -n texlive-numerica-tables
The package defines a command to create possibly multi-column tables of
mathematical function values. Key = value settings produce a wide variety of
table styles consistent with the booktabs package (required). Also required are
the packages numerica, l3kernel, l3packages, amsmath and mathtools.

%package -n texlive-objectz
Summary:        Macros for typesetting Object Z
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Provides:       tex(oz.sty) = %{tl_version}

%description -n texlive-objectz
The package will typeset both Z and Object-Z specifications; it develops the
original zed package

%package -n texlive-odesandpdes
Summary:        Optimizing workflow involving odes and pdes
Version:        svn69485
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(odesandpdes.sty) = %{tl_version}

%description -n texlive-odesandpdes
This package is the solution no one asked for, to a problem nobody had. Have
you ever thought to yourself "wow, I sure do dislike having to remember
multiple macros for my odes and pdes" and the author of this package has to
agree, wholeheartedly. In the modern world of "tik-toking" and "family guy
surfing" our brains have rotted beyond salvage for even basic levels of
cognitive recall. This package aims to fix this, through two macros that have
been set to each have an identical form and function with an emphasis on
intuitive use. Through setting options, the multiple common notational style
are easily swapped between, all by a single option. You're Welcome.

%package -n texlive-oplotsymbl
Summary:        Some symbols which are not easily available
Version:        svn44951
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(oplotsymbl.sty) = %{tl_version}

%description -n texlive-oplotsymbl
This package is named oPlotSymbl and it includes symbols, which are not easily
available. Especially, these symbols are used in scientific plots, but the
potential user is allowed to use them in other ways. This package uses TikZ and
xcolor.

%package -n texlive-ot-tableau
Summary:        Optimality Theory tableaux in LaTeX
Version:        svn67813
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(arydshln.sty)
Requires:       tex(bbding.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(hhline.sty)
Requires:       tex(rotating.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tipa.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ot-tableau.sty) = %{tl_version}

%description -n texlive-ot-tableau
The package makes it easy to create beautiful optimality-theoretic tableaux.
The LaTeX source is visually very similar to a formatted tableau, which makes
working with the source code painless (well, less painful). A variety of
stylistic variants are available to suit personal taste. The package requires
xstring, amssymb, bbding, suffix, colortbl, rotating, hhline (optionally),
arydshln, and tipa (optionally).

%package -n texlive-oubraces
Summary:        Braces over and under a formula
Version:        svn21833
License:        BSD-1-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(oubraces.sty) = %{tl_version}

%description -n texlive-oubraces
Provides a means to interleave \overbrace and \underbrace in the same formula.

%package -n texlive-overarrows
Summary:        Custom extensible arrows over math expressions
Version:        svn76641
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(esvect.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(old-arrows.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(tikz.sty)
Provides:       tex(overarrows.sty) = %{tl_version}

%description -n texlive-overarrows
A LaTeX package to create custom arrows over math expressions, mainly for
vectors (but arrows can as well be drawn below). Arrows stretch with content,
scale with math styles, and have a correct kerning when a subscript follows.
Some predefined commands are also provided.

%package -n texlive-pascaltriangle
Summary:        Draw beautiful Pascal (Yanghui) triangles
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(pascaltriangle.sty) = %{tl_version}

%description -n texlive-pascaltriangle
This LaTeX3 package based on TikZ helps to generate beautiful Pascal (Yanghui)
triangles. It provides a unique drawing macro \pascal which can generate
isosceles or right-angle triangles customized by means of different \pascal
macro options or the \pascalset macro.

%package -n texlive-perfectcut
Summary:        Nested delimiters that consistently grow regardless of the contents
Version:        svn67201
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(mathstyle.sty)
Requires:       tex(scalerel.sty)
Provides:       tex(perfectcut.sty) = %{tl_version}

%description -n texlive-perfectcut
This package defines the command \perfectcut#1#2 which displays a bracket
<#1||#2>. Various other delimiters are similarly defined (parentheses, square
brackets ...). The effect of these commands is to let the delimiters grow
according to the number of nested \perfectcommands (regardless of the size of
the contents). The package was originally intended for solving a notational
issue for direct-style continuation calculi in proof theory. For general use,
the package also defines commands for defining other sorts of delimiters which
will behave in the same way (see example in the documentation). The package
also offers a robust reimplementation of \big, \bigg, etc.

%package -n texlive-pfdicons
Summary:        Draw process flow diagrams in chemical engineering
Version:        svn60089
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Provides:       tex(pfdicons.sty) = %{tl_version}

%description -n texlive-pfdicons
This package provides TikZ shapes to represent commonly encountered unit
operations for depiction in process flow diagrams (PFDs) and, to a lesser
extent, process and instrumentation diagrams (PIDs). The package was designed
with undergraduate chemical engineering students and faculty in mind, and the
number of units provided should cover--in Turton's estimate--about 90 percent
of all fluid processing operations.

%package -n texlive-physconst
Summary:        Macros for commonly used physical constants
Version:        svn58727
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(physunits.sty)
Provides:       tex(physconst.sty) = %{tl_version}

%description -n texlive-physconst
This package consists of several macros that are shorthand for a variety of
physical constants, e.g. the speed of light. The package developed out of
physics and astronomy classes that the author has taught and wanted to ensure
that he had correct values for each constant and did not wish to retype them
every time he uses them. The constants can be used in two forms, the most
accurate available values, or versions that are rounded to 3 significant digits
for use in typical classroom settings, homework assignments, etc. Most
constants are taken from CODATA 2018, with the exception of the astronomical
objects, whose values are taken from International Astronomical Union specified
values. Constants that are derived from true constants, e.g. the fine structure
constant, have been calculated using the accepted values of the fundamental
constants.

%package -n texlive-physics
Summary:        Macros supporting the Mathematics of Physics
Version:        svn74247
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(xparse.sty)
Provides:       tex(physics.sty) = %{tl_version}

%description -n texlive-physics
The package defines simple and flexible macros for typesetting equations in the
languages of vector calculus and linear algebra, using Dirac notation.

%package -n texlive-physics-patch
Summary:        Improved version of the physics package
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(physics-patch.sty) = %{tl_version}

%description -n texlive-physics-patch
This package requires the amsmath, etoolbox, xcolor, xparse, and xstring
packages. Commands that have different definitions come with PT in the
beginning of their name (e.g. \PTmqty). physics-patch has covered all commands
in physics since version 2.0, so there's no need to load physics. It is ok to
load physics before this package. This package will silently override macros in
physics with an improved version. To use the original version provided by
physics, load physics before this package and use the nooverride option (not
recommended). This package pretends that the physics package is loaded so that
this package won't be overridden if loading physics is called afterwards and
packages loaded afterwards that check whether physics is loaded to determine
their behavior (e.g. siunitx) work correctly. To disable this, use the
nopretend option (not recommended). If siunitx is loaded before this package,
this package will define \ITquantity and \ITqty as the integration of the
improved definition of physics's \qty (in \PHquantity and \PHqty) and siuitx's
\SI. You can optionally set the siintegrate option to override \PTquantity and
\PTqty with \ITqty (not recommended). If two opposite options -- one of them
with the name of the other prefixed with a no -- are loaded at the same time,
the one without the no in the name will be used. If two opposite options which
have the same suffix and different prefixes are loaded at the same time, the
default one will be used.

%package -n texlive-physics2
Summary:        Macros for typesetting maths faster and more simply
Version:        svn69369
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Requires:       tex(fixdif.sty)
Requires:       tex(keyval.sty)
Provides:       tex(phy-ab.braket.sty) = %{tl_version}
Provides:       tex(phy-ab.legacy.sty) = %{tl_version}
Provides:       tex(phy-ab.sty) = %{tl_version}
Provides:       tex(phy-bm-um.legacy.sty) = %{tl_version}
Provides:       tex(phy-braket.sty) = %{tl_version}
Provides:       tex(phy-diagmat.sty) = %{tl_version}
Provides:       tex(phy-doubleprod.sty) = %{tl_version}
Provides:       tex(phy-nabla.legacy.sty) = %{tl_version}
Provides:       tex(phy-op.legacy.sty) = %{tl_version}
Provides:       tex(phy-qtext.legacy.sty) = %{tl_version}
Provides:       tex(phy-xmat.sty) = %{tl_version}
Provides:       tex(physics2.sty) = %{tl_version}

%description -n texlive-physics2
The physics2 package defines commands for typesetting maths formulae faster and
more simply. physics2 is a modularized package, each module provides its own
function. You can load modules separately after loading physics2. Modules of
physics provide the following support: Automatic braces; Dirac bra-ket
notation; Easy way to typeset diagonal matrices and matrices with similar
entries; Double cross and double dot (binary) operators for tensors.

%package -n texlive-physics3
Summary:        Modularized package for easy setting of physical formulas
Version:        svn77503
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Requires:       tex(fixdif.sty)
Requires:       tex(keyval.sty)
Provides:       tex(phx-ab.braket.sty) = %{tl_version}
Provides:       tex(phx-ab.legacy.sty) = %{tl_version}
Provides:       tex(phx-ab.sty) = %{tl_version}
Provides:       tex(phx-bm-um.sty) = %{tl_version}
Provides:       tex(phx-braket.sty) = %{tl_version}
Provides:       tex(phx-diagmat.sty) = %{tl_version}
Provides:       tex(phx-doubleprod.sty) = %{tl_version}
Provides:       tex(phx-operator.sty) = %{tl_version}
Provides:       tex(phx-qtext.legacy.sty) = %{tl_version}
Provides:       tex(phx-xmat.sty) = %{tl_version}
Provides:       tex(physics3.sty) = %{tl_version}

%description -n texlive-physics3
This package defines commands for typesetting math formulae faster and more
simply. physics3 is a modularized package, that currently provides modules for:
Automatic braces Dirac bra-ket notation Easy way to typeset diagonal matrices
and matrices with similar entries Double cross and double dot (binary)
operators for tensors

%package -n texlive-physunits
Summary:        Macros for commonly used physical units
Version:        svn58728
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(physunits.sty) = %{tl_version}

%description -n texlive-physunits
This package provides a collection of macros to simplify using physical units
(e.g. m for meters, J for joules, etc.), especially in math mode. All major SI
units are included, as well as some cgs units used in astronomy.

%package -n texlive-pinoutikz
Summary:        Draw chip pinouts with TikZ
Version:        svn55966
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(arrayjob.sty)
Requires:       tex(forarray.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       tex(upquote.sty)
Requires:       tex(xstring.sty)
Provides:       tex(pinoutikz.sty) = %{tl_version}

%description -n texlive-pinoutikz
The package provides a set of macros for typesetting electronic chip pinouts.
It is designed as a tool that is easy to use, with a lean syntax, native to
LaTeX, and directly supporting PDF output format. It has therefore been based
on the very impressive TikZ package.

%package -n texlive-pm-isomath
Summary:        Poor man ISO math for pdfLaTeX users
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xparse.sty)
Provides:       tex(pm-isomath.sty) = %{tl_version}

%description -n texlive-pm-isomath
This small package realizes a poor man approximation of the ISO regulations for
physical sciences and technology. Contrary to other more elegant solutions, it
does not load any math alphabet, since pdfLaTeX can use only a maximum of such
alphabets. The necessary user macros are defined for typesetting common math
symbols that require special ISO treatment.

%package -n texlive-pmdraw
Summary:        Draw elements of the diagram monoids
Version:        svn77509
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(pmdraw.sty) = %{tl_version}

%description -n texlive-pmdraw
This package allows you to draw elements of the diagram monoids, commonly
referred to as diagrams. The package provides a lot of flexibility to draw most
diagrams and can be customised as needed. It makes use of the TikZ and keyval
packages.

%package -n texlive-polexpr
Summary:        A parser for polynomial expressions
Version:        svn63337
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xintexpr.sty)
Provides:       tex(polexpr-examples.tex) = %{tl_version}
Provides:       tex(polexpr.sty) = %{tl_version}
Provides:       tex(polexprcore.tex) = %{tl_version}
Provides:       tex(polexprexpr.tex) = %{tl_version}
Provides:       tex(polexprsturm.tex) = %{tl_version}

%description -n texlive-polexpr
The package provides a parser \poldef of algebraic polynomial expressions. As
it is based on xintexpr, the coefficients are allowed to be arbitrary rational
numbers. Once defined, a polynomial is usable by its name either as a numerical
function in \xintexpr/\xinteval, or for additional polynomial definitions, or
as argument to the package macros. The localization of real roots to arbitrary
precision as well as the determination of all rational roots is implemented via
such macros. Since release 0.8, polexpr extends the xintexpr syntax to
recognize polynomials as a new variable type (and not only as functions).
Functionality which previously was implemented via macros such as the
computation of a greatest common divisor is now available directly in
\xintexpr, \xinteval or \poldef via infix or functional syntax.

%package -n texlive-prftree
Summary:        Macros for building proof trees
Version:        svn54080
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(prftree.sty) = %{tl_version}

%description -n texlive-prftree
A package to typeset proof trees for natural deduction calculi, sequent-like
calculi, and similar.

%package -n texlive-principia
Summary:        Notations for typesetting the "Principia Mathematica"
Version:        svn74710
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(pifont.sty)
Provides:       tex(principia.sty) = %{tl_version}

%description -n texlive-principia
This package supports typesetting the Peanese notation in Volumes I-III of
Whitehead and Russell's 1910 "Principia Mathematica".

%package -n texlive-proba
Summary:        Shortcuts commands to symbols used in probability texts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Provides:       tex(proba.sty) = %{tl_version}

%description -n texlive-proba
This package includes some of the most often used commands in probability
texts, e.g. probability, expectation, variance, etc. It also includes some
short commands for set (blackboard) or filtrations (calligraphic). It requires
LaTeX2e and the amsfonts package.

%package -n texlive-proof-at-the-end
Summary:        A package to move proofs to appendix
Version:        svn77355
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(catchfile.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(thm-restate.sty)
Requires:       tex(thmtools.sty)
Requires:       tex(xparse.sty)
Provides:       tex(proof-at-the-end.sty) = %{tl_version}

%description -n texlive-proof-at-the-end
This package aims to provide a way to easily move proofs to the appendix. You
can (among other things) move proofs to different places/sections, create links
from theorems to proofs, restate theorems, add comments in appendix...

%package -n texlive-prooftrees
Summary:        Forest-based proof trees (symbolic logic)
Version:        svn77411
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(forest.sty)
Requires:       tex(svn-prov.sty)
Provides:       tex(prooftrees-debug.sty) = %{tl_version}
Provides:       tex(prooftrees.sty) = %{tl_version}

%description -n texlive-prooftrees
The package supports drawing proof trees of the kind often used in introductory
logic classes, especially those aimed at students without strong mathematical
backgrounds. Hodges (1991) is one example of a text which uses this system.
When teaching such a system it is especially useful to annotate the tree with
line numbers, justifications and explanations of branch closures. prooftrees
provides a single environment, prooftree, and a variety of tools for
annotating, customising and highlighting such trees. A cross-referencing system
is provided for trees which cite line numbers in justifications for proof lines
or branch closures. prooftrees is based on forest and, hence, TikZ. The package
requires version 2.0.2 of Forest for expected results and will not work with
version 1. Out-of-the-box support for memoization is based on forest version
2.1.

%package -n texlive-pseudo
Summary:        Straightforward pseudocode
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(aliascnt.sty)
Requires:       tex(array.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(pseudo.sty) = %{tl_version}

%description -n texlive-pseudo
The package permits writing pseudocode without much fuss and with quite a bit
of configurability. Its main environment combines aspects of enumeration,
tabbing and tabular for nonintrusive line numbering, indentation and
highlighting, and there is functionality for typesetting common syntactic
elements such as keywords, identifiers, and comments. The package relies on
aliascnt, array, colortbl, expl3, l3keys2e, xcolor, and xparse.

%package -n texlive-pseudocode
Summary:        LaTeX environment for specifying algorithms in a natural way
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fancybox.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(pseudocode.sty) = %{tl_version}

%description -n texlive-pseudocode
This package provides the environment "pseudocode" for describing algorithms in
a natural manner.

%package -n texlive-pythonhighlight
Summary:        Highlighting of Python code, based on the listings package
Version:        svn70698
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(pythonhighlight.sty) = %{tl_version}

%description -n texlive-pythonhighlight
Highlighting of Python code, based on the listings package.

%package -n texlive-qsharp
Summary:        Syntax highlighting for the Q# language
Version:        svn49722
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(qsharp.sty) = %{tl_version}

%description -n texlive-qsharp
The package provides syntax highlighting for the Q# language, a domain-specific
language for quantum programming.

%package -n texlive-quantikz
Summary:        Draw quantum circuit diagrams
Version:        svn67206
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(quantikz.sty) = %{tl_version}
Provides:       tex(tikzlibraryquantikz.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryquantikz2.code.tex) = %{tl_version}

%description -n texlive-quantikz
The purpose of this package is to extend TikZ with the functionality for
drawing quantum circuit diagrams.

%package -n texlive-quantum-chemistry-bonn
Summary:        Use consistent typesetting for quantum chemistry related software
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(siunitx.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(quantum-chemistry-bonn.sty) = %{tl_version}

%description -n texlive-quantum-chemistry-bonn
This package gives access to several commands related to quantum chemistry.
This includes consistent formatting of names of QC programs, as well as methods
such as density functionals. Furthermore, units of energy are set, and
easy-to-use commands are provided. Lastly, the corporate design colors of the
University of Bonn are defined.

%package -n texlive-quantumcubemodel
Summary:        Representation of quantum states in the quantum cube model
Version:        svn77308
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(braket.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(quantumcubemodel.sty) = %{tl_version}

%description -n texlive-quantumcubemodel
This package provides simple LaTeX commands to draw intuitive cube-based
diagrams for quantum states of one, two, or three qubits. Inspired by Prof. B.
Just's educational framework, it supports amplitude-phase notation, gate
transition visualizations (Hadamard, Pauli, CNOT, Toffoli). The package is
ideal for teaching and documenting small quantum circuits.

%package -n texlive-quickreaction
Summary:        A simple and fast way to typeset chemical reactions
Version:        svn66867
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(quickreaction.sty) = %{tl_version}

%description -n texlive-quickreaction
This package provides the quickreaction environment and the \quickarrow command
to simplify the typesetting of chemical reactions. It is based on the TikZ
matrix of nodes and aligns all the reactants and products at the center of the
TikZ box in which they are contained.

%package -n texlive-quiver
Summary:        Draw commutative diagrams exported from https://q.uiver.app
Version:        svn75606
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(tikz-cd.sty)
Provides:       tex(quiver.sty) = %{tl_version}

%description -n texlive-quiver
quiver is a modern graphical editor for commutative and pasting diagrams,
capable of rendering high-quality diagrams for screen viewing, and exporting to
LaTeX. This LaTeX package is intended to be used in conjunction with the
editor, and provides the packages and styles that are used by diagrams exported
from the editor.

%package -n texlive-qworld
Summary:        Drawing string diagrams for monoidal categories and quantum theory in TeX
Version:        svn75910
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(qworld.sty) = %{tl_version}

%description -n texlive-qworld
This LaTeX package has been designed for the typesetting of graphical languages
grounded in monoidal category theory and its extensions. It provides a
declarative, LaTeX-native interface for rendering string diagrams, eliminating
the need for any external graphics software or manual image management. The
package supports a wide spectrum of categorical structures frequently
encountered in categorical quantum mechanics, algebraic structures, and
diagrammatic reasoning, including but not limited to: Monoidal and symmetric
monoidal categories Dual objects and pivotal / rigid categories Dagger
categories Frobenius algebras and Hopf algebras Braided, balanced, and ribbon
categories Internally, QWorld builds upon the TikZ graphics framework, but
introduces a domain-specific layer of abstraction that aligns diagram syntax
closely with categorical semantics. This design facilitates accurate and
transparent visual representations of morphisms, tensor products, and
composition, thereby supporting both formal exposition and pedagogical use.
QWorld is intended for researchers and educators working in categorical logic,
quantum foundations, topological quantum field theory (TQFT), and related
domains where graphical calculi constitute an essential mode of reasoning.

%package -n texlive-rank-2-roots
Summary:        Draw (mathematical) rank 2 root systems
Version:        svn75301
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(rank-2-roots.sty) = %{tl_version}

%description -n texlive-rank-2-roots
This package concerns mathematical drawings arising in representation theory.
The purpose of this package is to ease drawing of rank 2 root systems, with
Weyl chambers, weight lattices, and parabolic subgroups. Required packages are
tikz, etoolbox, expl3, pgfkeys, pgfopts, xparse, and xstring.

%package -n texlive-rbt-mathnotes
Summary:        Rebecca Turner's personal macros and styles for typesetting mathematics notes
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(knowledge.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(multirow.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(tabu.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(rbt-mathnotes-messages.sty) = %{tl_version}
Provides:       tex(rbt-mathnotes-util.sty) = %{tl_version}
Provides:       tex(rbt-mathnotes.sty) = %{tl_version}

%description -n texlive-rbt-mathnotes
Styles for typesetting mathematics notes. Includes document classes for
typesetting homework assignments and "formula cheat sheets" for exams. Several
examples are included, along with rendered PDFs.

%package -n texlive-rec-thy
Summary:        Commands to typeset recursion theory papers
Version:        svn76924
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(bbm.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifmtarg.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(picture.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(rec-thy.sty) = %{tl_version}

%description -n texlive-rec-thy
This package is designed to help mathematicians publishing papers in the area
of recursion theory (aka Computability Theory) easily use standard notation.
This includes easy commands to denote Turing reductions, Turing functionals,
c.e. sets, stagewise computations, forcing and syntactic classes.

%package -n texlive-reptheorem
Summary:        Repetition of theorem environments
Version:        svn76224
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(reptheorem.sty) = %{tl_version}

%description -n texlive-reptheorem
When writing a large manuscript, it is sometimes beneficial to repeat a theorem
(or lemma or...) at an earlier or later point for didactical purposes. However,
thmtools's built-in restatable only allows replicating theorems after they have
been stated, and only in the same document. This package solves the issue by
making use of the .aux file, and also introduces its own file extension, .thm,
to replicate theorems in other files.

%package -n texlive-resolsysteme
Summary:        Work on linear systems using xint or pyluatex
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(nicefrac.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ResolSysteme.sty) = %{tl_version}

%description -n texlive-resolsysteme
This package provides some commands (in French) to perform calculations on
small (2x2 or 3x3 or 4x4) linear systems, with xint or pyluatex: \DetMatrice or
\DetMatricePY to diplay the determinant of a matrix (with formatting options);
\MatriceInverse or \MatriceInversePY to display the invers of a matrix (with
formatting options) ; \SolutionSysteme or \SolutionSystemePY to display the
solution of a linear system (with formatting options); ...

%package -n texlive-rest-api
Summary:        Describing a rest api
Version:        svn57068
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(color.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(listings.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(transparent.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xstring.sty)
Provides:       tex(rest-api.sty) = %{tl_version}

%description -n texlive-rest-api
This LaTeX package provides macros to describe rest apis for documentation
purposes. The endpoints can hold the following information: method description
path parameter request body and content type response body, content type and
status code

%package -n texlive-revquantum
Summary:        Hacks to make writing quantum papers for revtex4-1 less painful
Version:        svn43505
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithm.sty)
Requires:       tex(algpseudocode.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(braket.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(sourcecodepro.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(revquantum.sty) = %{tl_version}

%description -n texlive-revquantum
This package provides a number of useful hacks to solve common annoyances with
the revtex4-1 package, and to define notation in common use within quantum
information. In doing so, it imports and configures a number of
commonly-available and used packages, and where reasonable, provides fallbacks.
It also warns when users try to load packages which are known to be
incompatible with revtex4-1.

%package -n texlive-ribbonproofs
Summary:        Drawing ribbon proofs
Version:        svn31137
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etextools.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ribbonproofs.sty) = %{tl_version}

%description -n texlive-ribbonproofs
The package provides a way to draw "ribbon proofs" in LaTeX. A ribbon proof is
a diagrammatic representation of a mathematical proof that a computer program
meets its specification. These diagrams are more human-readable, more scalable,
and more easily modified than the corresponding textual proofs.

%package -n texlive-rigidnotation
Summary:        Typeset vectors and matrices following the RIGID notation
Version:        svn71264
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-l3packages
Requires:       texlive-mathtools
Requires:       tex(mathtools.sty)
Requires:       tex(xparse.sty)
Provides:       tex(rigidnotation.sty) = %{tl_version}

%description -n texlive-rigidnotation
This package provides LaTeX macros to easily and concisely typeset vectors and
matrices in a flexible way such as to follow the RIGID notation convention. The
package enables the user to define custom commands that can then be used in any
math-mode environment to efficiently and rigorously typeset the notational
elements commonly used in robotics research (and many other fields) for
position vectors, rotation matrices, pose matrices, etc.

%package -n texlive-rmathbr
Summary:        Repeating of math operator at the broken line and the new line in inline equations
Version:        svn57173
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifetex.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(rmathbr.sty) = %{tl_version}

%description -n texlive-rmathbr
Repeating of math operators at the broken line and the new line in inline
equations is used in Cyrillic mathematical typography (Russian for example),
but unfortunately LaTeX does not provide such an option. This package solves
the problem by extending ideas described in M. I. Grinchuk "TeX and Russian
Traditions of Typesetting", TUGboat 17(4) (1996) 385 and supports most of LaTeX
mathematical packages. See the documentation for details.

%package -n texlive-sankey
Summary:        Draw Sankey diagrams with TikZ
Version:        svn73396
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accsupp.sty)
Requires:       tex(babel.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(cmap.sty)
Requires:       tex(dtx-attach.sty)
Requires:       tex(dtxdescribe.sty)
Requires:       tex(embedfile.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(footnote.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hypdoc.sty)
Requires:       tex(inconsolata.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(microtype.sty)
Requires:       tex(parskip.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xparse.sty)
Provides:       tex(sankey-doc-preamble.sty) = %{tl_version}
Provides:       tex(sankey.sty) = %{tl_version}
Provides:       tex(tikzlibrarydubins.code.tex) = %{tl_version}

%description -n texlive-sankey
This package provides macros and an environment for creating Sankey diagrams,
i.e. flow diagrams in which the width of the arrows is proportional to the flow
rate.

%package -n texlive-sasnrdisplay
Summary:        Typeset SAS or R code or output
Version:        svn63255
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(caption.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(listings.sty)
Requires:       tex(needspace.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(SASnRdisplay.sty) = %{tl_version}

%description -n texlive-sasnrdisplay
The SASnRdisplay package serves as a front-end to listings, which permits
statisticians and others to import source code and the results of their
calculations or simulations into LaTeX projects. The package is also capable of
overloading the Sweave User Manual and SASweave packages.

%package -n texlive-sciposter
Summary:        Make posters of ISO A3 size and larger
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sciposter
This collection of files contains LaTeX packages for posters of ISO A3 size and
larger (ISO A0 is the default size). American paper sizes and custom paper are
supported. In particular, sciposter.cls defines a document class which allows
cutting and pasting most of an article to a poster without any editing (save
reducing the size) -- see the manual. Sciposter does work for LaTeX, not just
pdfLaTeX. However, xdvi produces strange results, though a recent version of
dvips does create good ps-files from the dvi files. Also note that logos must
either be put in the current working directory or in the directories of your
LaTeX distribution. For some reason graphicspath settings are ignored.

%package -n texlive-sclang-prettifier
Summary:        Prettyprinting SuperCollider source code
Version:        svn35087
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(sclang-prettifier.sty) = %{tl_version}

%description -n texlive-sclang-prettifier
Built on top of the listings package, the package allows effortless
prettyprinting of SuperCollider source code in documents typeset with LaTeX &
friends.

%package -n texlive-scratchx
Summary:        Include Scratch programs in LaTeX documents
Version:        svn44906
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifsym.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ScratchX.sty) = %{tl_version}

%description -n texlive-scratchx
This package can be used to include every kind of Scratch program in LaTeX
documents. This may be particularly useful for Math Teachers and IT
specialists. The package depends on the following other LaTeX packages: calc,
fp, ifsym, multido, tikz, xargs, and xstring.

%package -n texlive-sesamanuel
Summary:        Class and package for sesamath books or paper
Version:        svn36613
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(esvect.sty)
Requires:       tex(etex.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(helvet.sty)
Requires:       tex(ifmtarg.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multido.sty)
Requires:       tex(multirow.sty)
Requires:       tex(numprint.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pifont.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-tab.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xunicode.sty)
Provides:       tex(sesamanuel.sty) = %{tl_version}
Provides:       tex(sesamanuelTIKZ.sty) = %{tl_version}

%description -n texlive-sesamanuel
The package contains a sesamanuel class which could be used to compose a
student's classroom book with LaTeX, and also a sesamanuelTIKZ style to be used
for TikZ pictures in the sesamath book.

%package -n texlive-sfg
Summary:        Draw signal flow graphs
Version:        svn20209
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(sfg.sty) = %{tl_version}

%description -n texlive-sfg
Defines some commands to draw signal flow graphs as used by electrical and
electronics engineers and graph theorists. Requires fp and pstricks packages
(and a relatively fast machine).

%package -n texlive-shuffle
Summary:        A symbol for the shuffle product
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(shuffle.sty) = %{tl_version}

%description -n texlive-shuffle
The bundle provides a LaTeX package and a font (as Metafont source) for the
shuffle product which is used in some part of mathematics and physics.

%package -n texlive-simplebnf
Summary:        A simple package to format Backus-Naur form (BNF)
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(mathtools.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(xparse.sty)
Provides:       tex(simplebnf.sty) = %{tl_version}

%description -n texlive-simplebnf
This package provides a simple way for typesetting grammars in Backus-Naur form
(BNF). The included bnf environment parses BNF expressions (possibly
annotated), so users can write readable BNF expressions in their documents. It
features a flexible configuration system, allowing for the customization of the
domain-specific language (DSL) used in typesetting the grammar. Additionally,
the package comes with sensible defaults. The package requires expl3, xparse,
mathtools, and tabularray..

%package -n texlive-simpler-wick
Summary:        Simpler Wick contractions
Version:        svn71991
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Provides:       tex(simpler-wick.sty) = %{tl_version}

%description -n texlive-simpler-wick
In every quantum field theory course, there will be a chapter about Wick's
theorem and how it can be used to convert a very large product of many creation
and annihilation operators into something more tractable and normal ordered.
The contractions are denoted with a square bracket over the operators which are
being contracted, which used to be rather annoying to typeset in LaTeX as the
only other package available was simplewick, which is rather unwieldy. This
package provides a simpler syntax for Wick contractions.

%package -n texlive-simples-matrices
Summary:        Define matrices by given list of values
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(xparse.sty)
Provides:       tex(simples-matrices.sty) = %{tl_version}

%description -n texlive-simples-matrices
Macros to define and write matrices whose coefficients are given row by row in
a list of values separated by commas.

%package -n texlive-simplewick
Summary:        Simple Wick contractions
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(simplewick.sty) = %{tl_version}

%description -n texlive-simplewick
The package provides a simple means of drawing Wick contractions above and
below expressions.

%package -n texlive-sistyle
Summary:        Package to typeset SI units, numbers and angles
Version:        svn59682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Provides:       tex(sistyle.sty) = %{tl_version}

%description -n texlive-sistyle
This package typesets SI units, numbers and angles according to the ISO
requirements. Care is taken with font setup and requirements, and language
customisation is available. Note that this package is (in principle) superseded
by siunitx; sistyle has maintenance-only support, now.

%package -n texlive-siunits
Summary:        International System of Units
Version:        svn59702
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Provides:       tex(SIunits.sty) = %{tl_version}
Provides:       tex(binary.sty) = %{tl_version}

%description -n texlive-siunits
Typeset physical units following the rules of the International System of Units
(SI). The package requires amstext, for proper representation of some values.
Note that the package is now superseded by siunitx; siunits has
maintenance-only support, now.

%package -n texlive-siunitx
Summary:        A comprehensive (SI) units package
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Requires:       tex(array.sty)
Requires:       tex(xparse.sty)
Provides:       tex(siunitx-v2.sty) = %{tl_version}
Provides:       tex(siunitx.sty) = %{tl_version}

%description -n texlive-siunitx
Physical quantities have both numbers and units, and each physical quantity
should be expressed as the product of a number and a unit. Typesetting physical
quantities requires care to ensure that the combined mathematical meaning of
the number-unit combination is clear. In particular, the SI units system lays
down a consistent set of units with rules on how these are to be used. However,
different countries and publishers have differing conventions on the exact
appearance of numbers (and units). The siunitx package provides a set of tools
for authors to typeset quantities in a consistent way. The package has an
extended set of configuration options which make it possible to follow varying
typographic conventions with the same input syntax. The package includes
automated processing of numbers and units, and the ability to control tabular
alignment of numbers.

%package -n texlive-skmath
Summary:        Extensions to the maths command repertoir
Version:        svn52411
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(isomath.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(xfrac.sty)
Requires:       tex(xparse.sty)
Provides:       tex(skmath.sty) = %{tl_version}

%description -n texlive-skmath
The package provides a selection of new maths commands and improved
re-definitions of existing commands.

%package -n texlive-spalign
Summary:        Typeset matrices and arrays with spaces and semicolons as delimiters
Version:        svn42225
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(spalign.sty) = %{tl_version}

%description -n texlive-spalign
Typeset matrices and arrays with spaces and semicolons as delimiters. The
purpose of this package is to decrease the number of keystrokes needed to
typeset small amounts of aligned material (matrices, arrays, etc.). It provides
a facility for typing alignment environments and macros with spaces as the
alignment delimiter and semicolons (by default) as the end-of-row indicator.
For instance, typeset a matrix using \spalignmat{1 12 -3; 24 -2 2; 0 0 1}, or a
vector using \spalignvector{22 \frac{1}{2} -14}. This package also contains
utility macros for typesetting augmented matrices, vectors, arrays, systems of
equations, and more, and is easily extendable to other situations that use
alignments. People who have to typeset a large number of matrices (like linear
algebra teachers) should find this package to be a real time saver.

%package -n texlive-spbmark
Summary:        Customize superscripts and subscripts
Version:        svn76924
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(spbmark.sty) = %{tl_version}

%description -n texlive-spbmark
This package provides three commands \super, \sub and \supersub to improve the
layout of superscripts and subscripts which can be adjusted with respect to
relative position and format, and can be used in text and math mode.

%package -n texlive-stanli
Summary:        TikZ Library for Structural Analysis
Version:        svn54512
License:        GPL-2.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xargs.sty)
Provides:       tex(stanli.sty) = %{tl_version}

%description -n texlive-stanli
stanli is a STructural ANalysis LIbrary based on PGF/TikZ. Creating new
assignments and tests, at university, is usually a very time-consuming task,
especially when this includes drawing graphics. In the field of structural
engineering, those small structures are a key part for teaching. This package
permits to create such 2D and 3D structures in a very fast and simple way.

%package -n texlive-statex
Summary:        Statistics style
Version:        svn20306
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(color.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(shortvrb.sty)
Provides:       tex(statex.sty) = %{tl_version}

%description -n texlive-statex
A package defining many macros for items of significance in statistical
presentations. An updated, but incompatible, version of the package is
available: statex2.

%package -n texlive-statex2
Summary:        Statistics style
Version:        svn23961
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(color.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(shortvrb.sty)
Provides:       tex(statex2.sty) = %{tl_version}

%description -n texlive-statex2
The package defines many macros for items of significance in statistical
presentations. It represents a syntax-incompatible upgrade of statex.

%package -n texlive-statistics
Summary:        Compute and typeset statistics tables and graphics
Version:        svn67201
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(statistics.sty) = %{tl_version}

%description -n texlive-statistics
The 'statistics' package can compute and typeset statistics like frequency
tables, cumulative distribution functions (increasing or decreasing, in
frequency or absolute count domain), from the counts of individual values, or
ranges, or even the raw value list with repetitions. It can also compute and
draw a bar diagram in case of individual values, or, when the data repartition
is known from ranges, an histogram or the continuous cumulative distribution
function. You can ask 'statistics' to display no result, selective results or
all of them. Similarly 'statistics' can draw only some parts of the graphs.
Every part of the generated tables or graphics is customizable.

%package -n texlive-statistik
Summary:        Store statistics of a document
Version:        svn20334
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(keyval.sty)
Provides:       tex(statistik.sty) = %{tl_version}

%description -n texlive-statistik
The package counts the numbers of pages per chapter, and stores the results in
a separate file; the format of the file is selectable.

%package -n texlive-statmath
Summary:        A LaTeX package for simple use of statistical notation
Version:        svn46925
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(bm.sty)
Provides:       tex(statmath.sty) = %{tl_version}

%description -n texlive-statmath
The package offers anumber of notational conventions to be used in applied and
theoretical papers in statistics which are currently lacking in the popular
amsmath package. The seasoned LaTeX user will see that the provided commands
are simple, almost trivial, but will hopefully offer less cluttered preambles
as well as a welcome help for novice users.

%package -n texlive-steinmetz
Summary:        Print Steinmetz notation
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(steinmetz.sty) = %{tl_version}

%description -n texlive-steinmetz
The steinmetz package provides a command for typesetting complex numbers in the
Steinmetz notation used in electrotechnics as: <modulus>;<argument or phase
inside an angle symbol> The package makes use of pict2e.

%package -n texlive-stmaryrd
Summary:        St Mary Road symbols for theoretical computer science
Version:        svn22027
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(stmaryrd.sty) = %{tl_version}

%description -n texlive-stmaryrd
The fonts were originally distributed as Metafont sources only, but Adobe Type
1 versions are also now available. Macro support is provided for use under
LaTeX; the package supports the "only" option (provided by the somedefs
package) to restrict what is loaded, for those who don't need the whole font.

%package -n texlive-string-diagrams
Summary:        Create string diagrams with LaTeX and TikZ
Version:        svn67363
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(string-diagrams.sty) = %{tl_version}

%description -n texlive-string-diagrams
This LaTeX package has been designed for effortless and aesthetically pleasing
creation of string diagrams.

%package -n texlive-structmech
Summary:        A TikZ command set for structural mechanics drawings
Version:        svn66724
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(structmech.sty) = %{tl_version}

%description -n texlive-structmech
This package provides a collection of TikZ commands that allow users to draw
basic elements in material/structural mechanics. It is thus possible to draw
member forces, nodal forces/displacements, various boundary conditions,
internal force distributions, etc.

%package -n texlive-struktex
Summary:        Draw Nassi-Shneiderman charts
Version:        svn75565
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cleveref.sty)
Requires:       tex(color.sty)
Requires:       tex(curves.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(url.sty)
Requires:       tex(varioref.sty)
Provides:       tex(strukdoc.sty) = %{tl_version}
Provides:       tex(struktex.sty) = %{tl_version}
Provides:       tex(struktxf.sty) = %{tl_version}
Provides:       tex(struktxp.sty) = %{tl_version}

%description -n texlive-struktex
Even in the age of OOP one must develop algorithms. Nassi-Shneiderman charts
are a well known tool to describe an algorithm in a graphical way. The package
offers some macros for generating those charts in a LaTeX document. The package
provides the most important elements of a Nassi-Shneiderman charts, including
processing blocks, loops, mapping conventions for alternatives, etc. The charts
are drawn using the picture environment (using pict2e for preference).

%package -n texlive-substances
Summary:        A database of chemicals
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(chemfig.sty)
Requires:       tex(chemmacros.sty)
Requires:       tex(ghsystem.sty)
Requires:       tex(xparse.sty)
Provides:       tex(substances-default.def) = %{tl_version}
Provides:       tex(substances.sty) = %{tl_version}

%description -n texlive-substances
The package provides the means to create a database-like file that contains
data of various chemicals. These data may be retrieved in the document; an
index of the chemicals mentioned in the document can be created..

%package -n texlive-subsupscripts
Summary:        A range of sub- and superscript commands
Version:        svn16080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(subsupscripts.sty) = %{tl_version}

%description -n texlive-subsupscripts
The package provides a comprehensive and flexible set of commands for
combinations of left and right sub- and superscripts.

%package -n texlive-subtext
Summary:        Easy text-style subscripts in math mode
Version:        svn51273
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Provides:       tex(subtext.sty) = %{tl_version}

%description -n texlive-subtext
This LaTeX package gives easy access to text-style subscripts in math mode by
providing an optional argument to _. This is implemented by using the \text{}
command from the amstext package.

%package -n texlive-susy
Summary:        Macros for SuperSymmetry-related work
Version:        svn19440
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(susy.sty) = %{tl_version}

%description -n texlive-susy
The package provides abbreviations of longer expressions.

%package -n texlive-syllogism
Summary:        Typeset syllogisms in LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xspace.sty)
Provides:       tex(syllogism.sty) = %{tl_version}

%description -n texlive-syllogism
The package provides a simple, configurable, way for neatly typesetting
syllogisms and syllogistic-like arguments, composed of two premises and a
conclusion.

%package -n texlive-sympytexpackage
Summary:        Include symbolic computation (using sympy) in documents
Version:        svn57090
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(makecmds.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(sympytex.sty) = %{tl_version}

%description -n texlive-sympytexpackage
The bundle supports inclusion of symbolic-python (sympy) expressions, as well
as graphical output from the sympy plotting module (or from matplotlib).

%package -n texlive-synproof
Summary:        Easy drawing of syntactic proofs
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(synproof.sty) = %{tl_version}

%description -n texlive-synproof
The package provides a set of macros based on PSTricks that will enable you to
draw syntactic proofs easily (inspired by the Gamut books). Very few commands
are needed, however fine tuning of the various parameters (dimensions) can
still be achieved through "key=value" pairs.

%package -n texlive-t-angles
Summary:        Draw tangles, trees, Hopf algebra operations and other pictures
Version:        svn71991
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifpdf.sty)
Provides:       tex(t-angles.sty) = %{tl_version}

%description -n texlive-t-angles
A LaTeX2e package for drawing tangles, trees, Hopf algebra operations and other
pictures. It is based on emTeX or TPIC \specials. Therefore, it can be used
with the most popular drivers, including emTeX drivers, dviwin, xdvi and dvips,
and (using some code from ConTeXt) it may also be used with pdfLaTeX.

%package -n texlive-tablor
Summary:        Create tables of signs and of variations
Version:        svn31855
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(pst-eps.sty)
Provides:       tex(tablor-xetex.sty) = %{tl_version}
Provides:       tex(tablor.sty) = %{tl_version}

%description -n texlive-tablor
The package allows the user to use the computer algebra system XCAS to generate
tables of signs and of variations (the actual plotting of the tables uses the
MetaPost macro package tableauVariations). Tables with forbidden regions may be
developed using the package. A configuration file permits some configuration of
the language to be used in the diagrams. The tablor package requires that shell
escape be enabled.

%package -n texlive-temporal-logic
Summary:        Symbols for Temporal Logics
Version:        svn77281
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(temporal-logic.sty) = %{tl_version}

%description -n texlive-temporal-logic
This package defines functions for rendering temporal operators defined in
Linear Temporal Logic (LTL), Metric Temporal Logic (MTL), Metric First-order
Temporal Logic (MFOTL), and the Counting Metric First-order Temporal Binding
Logic (CMFTBL). The package defines various functions with variants in order to
include or omit optional parameters of the operators like the optional
interval.

%package -n texlive-tensind
Summary:        Typeset tensors
Version:        svn51481
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tensind.sty) = %{tl_version}

%description -n texlive-tensind
Typesets tensors with dots filling gaps and fine tuning of index placement.

%package -n texlive-tensor
Summary:        Typeset tensors
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tensor.sty) = %{tl_version}

%description -n texlive-tensor
A package which allows the user to set tensor-style super- and subscripts with
offsets between successive indices. It supports the typesetting of tensors with
mixed upper and lower indices with spacing, also typeset preposed indices. This
is a complete revision and extension of the original 'tensor' package by Mike
Piff.

%package -n texlive-tensormatrix
Summary:        Matrix representations of tensors
Version:        svn76005
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(tensormatrix.sty) = %{tl_version}

%description -n texlive-tensormatrix
This LaTeX package defines an environment tmat for visualizing the structure of
matrix representations of tensors. It requires the TikZ package.

%package -n texlive-tex-ewd
Summary:        Macros to typeset calculational proofs and programs in Dijkstra's style
Version:        svn15878
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dotnot.tex) = %{tl_version}

%description -n texlive-tex-ewd
Edsger W. Dijkstra and others suggest a unique style to present mathematical
proofs and to construct programs. This package provides macros that support
calculational proofs and Dijkstra's "guarded command language".

%package -n texlive-textgreek
Summary:        Upright greek letters in text
Version:        svn44192
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-greek-fontenc
Provides:       tex(textgreek.sty) = %{tl_version}

%description -n texlive-textgreek
Use upright greek letters as text symbols, e.g. \textbeta.

%package -n texlive-textopo
Summary:        Annotated membrane protein topology plots
Version:        svn23796
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphics.sty)
Requires:       tex(texshade.sty)
Provides:       tex(biotex.sty) = %{tl_version}
Provides:       tex(textopo.def) = %{tl_version}
Provides:       tex(textopo.sty) = %{tl_version}

%description -n texlive-textopo
A LaTeX package for setting shaded and annotated membrane protein topology
plots and helical wheels.

%package -n texlive-thermodynamics
Summary:        Macros for multicomponent thermodynamics documents
Version:        svn77280
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Provides:       tex(thermodynamics.sty) = %{tl_version}

%description -n texlive-thermodynamics
This package makes typesetting quantities found in thermodynamics texts
relatively simple. The commands are flexible and intended to be relatively
intuitive. It handles several sets of notation for total, specific, and molar
quantities; allows changes between symbols (e.g., A vs. F for Helmholtz free
energy); and greatly simplifies the typesetting of symbols and partial
derivatives commonly encountered in mixture thermodynamics. Changes of one's
notes from one textbook to another can be achieved relatively easily by
changing package options. The package offers a collection of macros and
environments which are intended to make typesetting thermodynamics documents
faster, more convenient, and more reliable. Macros include symbols for
extensive, molar, specific, and partial molar properties; excess and residual
(departure) properties; partial derivatives; heat capacities,
compressibilities, and expansivities; saturation, mixture, and pure-component
properties; Henry's Law parameters and activity coefficients; changes on
mixing, fusion, reaction, sublimation, and vaporization; and sets of all
moles/mole fractions/masses/etc. being held constant in derivatives. Conversion
of notes between textbooks is trivial for textbooks supported by the package,
and more general changes in notation are also possible through package options.

%package -n texlive-thmbox
Summary:        Decorate theorem statements
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(thmbox.sty) = %{tl_version}

%description -n texlive-thmbox
The package defines an environment thmbox that presents theorems, definitions
and similar objects in boxes decorated with frames and various aesthetic
features. The standard macro \newtheorem may be redefined to use the
environment.

%package -n texlive-thmtools
Summary:        Extensions to theorem environments
Version:        svn67018
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(remreset.sty)
Requires:       tex(shadethm.sty)
Requires:       tex(thmbox.sty)
Provides:       tex(aliasctr.sty) = %{tl_version}
Provides:       tex(parseargs.sty) = %{tl_version}
Provides:       tex(thm-amsthm.sty) = %{tl_version}
Provides:       tex(thm-autoref.sty) = %{tl_version}
Provides:       tex(thm-beamer.sty) = %{tl_version}
Provides:       tex(thm-kv.sty) = %{tl_version}
Provides:       tex(thm-listof.sty) = %{tl_version}
Provides:       tex(thm-llncs.sty) = %{tl_version}
Provides:       tex(thm-ntheorem.sty) = %{tl_version}
Provides:       tex(thm-patch.sty) = %{tl_version}
Provides:       tex(thm-restate.sty) = %{tl_version}
Provides:       tex(thmdef-mdframed.sty) = %{tl_version}
Provides:       tex(thmdef-shaded.sty) = %{tl_version}
Provides:       tex(thmdef-thmbox.sty) = %{tl_version}
Provides:       tex(thmtools.sty) = %{tl_version}
Provides:       tex(unique.sty) = %{tl_version}

%description -n texlive-thmtools
The bundle provides several packages for commonly-needed support for
typesetting theorems. The packages should work with kernel theorems (theorems
'out of the box' with LaTeX), and the theorem and amsthm packages. Features of
the bundle include: a key-value interface to \newtheorem; a \listoftheorems
command; hyperref and autoref compatibility; a mechanism for restating entire
theorems in a single macro call.

%package -n texlive-tiscreen
Summary:        Mimic the screen of older Texas Instruments calculators
Version:        svn62602
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(lcd.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textgreek.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tipa.sty)
Requires:       tex(wasysym.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(tiscreen.sty) = %{tl_version}

%description -n texlive-tiscreen
This package mimics the screen of older Texas Instruments dot matrix display
calculators, specifically the TI-82 STATS. It relies on the lcd and xcolor
packages.

%package -n texlive-tkz-interval
Summary:        Interval brackets made with TikZ
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tkz-interval.sty) = %{tl_version}

%description -n texlive-tkz-interval
The idea is to provide a command for representing intervals with brackets
created using TikZ, with automatic size management and customization of
thickness and depth, for examples. It is also possible to specify surrounding
spaces, and optional overlap for open brackets.

%package -n texlive-turnstile
Summary:        Typeset the (logic) turnstile notation
Version:        svn64967
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(turnstile.sty) = %{tl_version}

%description -n texlive-turnstile
Among other uses, the turnstile sign is used by logicians for denoting a
consequence relation, related to a given logic, between a collection of
formulas and a derived formula.

%package -n texlive-unitsdef
Summary:        Typesetting units in LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(units.sty)
Requires:       tex(xspace.sty)
Provides:       tex(unitsdef.sty) = %{tl_version}

%description -n texlive-unitsdef
Many packages for typesetting units have been written for use in LaTeX2e. Some
define macros to typeset a lot of units but do not suit to the actual font
settings, some make the characters needed available but do not predefine any
unit. This package tries to comply with both requirements. It predefines common
units, defines an easy to use interface to define new units and changes the
output concerning to the surrounding font settings.

%package -n texlive-venn
Summary:        Creating Venn diagrams with MetaPost
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-venn
MetaPost macros for venn diagrams.

%package -n texlive-witharrows
Summary:        "Aligned" math environments with arrows for comments
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(witharrows.sty) = %{tl_version}
Provides:       tex(witharrows.tex) = %{tl_version}

%description -n texlive-witharrows
This package provides an environment WithArrows which is similar to the
environment aligned of amsmath (and mathtools), but gives the possibility to
draw arrows on the right side of the alignment. These arrows are usually used
to give explanations concerning the mathematical calculus presented. The
package requires the following other LaTeX packages: expl3, footnote, l3keys2e,
tikz, and xparse.

%package -n texlive-xymtex
Summary:        Typesetting chemical structures
Version:        svn32182
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(epic.sty)
Requires:       tex(pgfcore.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(aliphat.sty) = %{tl_version}
Provides:       tex(assurechemist.sty) = %{tl_version}
Provides:       tex(assurelatexmode.sty) = %{tl_version}
Provides:       tex(bondcolor.sty) = %{tl_version}
Provides:       tex(carom.sty) = %{tl_version}
Provides:       tex(ccycle.sty) = %{tl_version}
Provides:       tex(chemist.sty) = %{tl_version}
Provides:       tex(chemstr.sty) = %{tl_version}
Provides:       tex(chemtimes.sty) = %{tl_version}
Provides:       tex(chmst-pdf.sty) = %{tl_version}
Provides:       tex(chmst-ps.sty) = %{tl_version}
Provides:       tex(fusering.sty) = %{tl_version}
Provides:       tex(hcycle.sty) = %{tl_version}
Provides:       tex(hetarom.sty) = %{tl_version}
Provides:       tex(hetaromh.sty) = %{tl_version}
Provides:       tex(lewisstruc.sty) = %{tl_version}
Provides:       tex(locant.sty) = %{tl_version}
Provides:       tex(lowcycle.sty) = %{tl_version}
Provides:       tex(methylen.sty) = %{tl_version}
Provides:       tex(polymers.sty) = %{tl_version}
Provides:       tex(sizeredc.sty) = %{tl_version}
Provides:       tex(steroid.sty) = %{tl_version}
Provides:       tex(xymtex.sty) = %{tl_version}
Provides:       tex(xymtexpdf.sty) = %{tl_version}
Provides:       tex(xymtexps.sty) = %{tl_version}
Provides:       tex(xymtx-pdf.sty) = %{tl_version}
Provides:       tex(xymtx-ps.sty) = %{tl_version}

%description -n texlive-xymtex
XyMTeX is a set of packages for drawing a wide variety of chemical structural
formulas in a way that reflects their structure. The package provides three
output modes: 'LaTeX', 'PostScript' and 'PDF'. XyMTeX's commands have a
systematic set of arguments for specifying substituents and their positions,
endocyclic double bonds, and bond patterns. In some cases there are additional
arguments for specifying hetero-atoms on the vertices of heterocycles. It is
believed that this systematic design allows XyMTeX to operate as a practical
(device-independent) tool for use with LaTeX.

%package -n texlive-yhmath
Summary:        Extended maths fonts for LaTeX
Version:        svn54377
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Provides:       tex(yhmath.sty) = %{tl_version}

%description -n texlive-yhmath
The yhmath bundle contains fonts (in Metafont and type 1 format) and a LaTeX
package for using them.

%package -n texlive-youngtab
Summary:        Typeset Young-Tableaux
Version:        svn73766
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(youngtab.sty) = %{tl_version}

%description -n texlive-youngtab
A package for typesetting Young-Tableaux, mathematical symbols for the
representations of groups, providing two macros, \yng(1) and \young(1) to
generate the whole Young-Tableau.

%package -n texlive-yquant
Summary:        Typesetting quantum circuits in a human-readable language
Version:        svn77263
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(yquant-circuit.tex) = %{tl_version}
Provides:       tex(yquant-config.tex) = %{tl_version}
Provides:       tex(yquant-draw.tex) = %{tl_version}
Provides:       tex(yquant-env.tex) = %{tl_version}
Provides:       tex(yquant-lang.tex) = %{tl_version}
Provides:       tex(yquant-langhelper.tex) = %{tl_version}
Provides:       tex(yquant-prepare.tex) = %{tl_version}
Provides:       tex(yquant-registers.tex) = %{tl_version}
Provides:       tex(yquant-shapes.tex) = %{tl_version}
Provides:       tex(yquant-tools.tex) = %{tl_version}
Provides:       tex(yquant.sty) = %{tl_version}
Provides:       tex(yquantlanguage-groups.sty) = %{tl_version}
Provides:       tex(yquantlanguage-qasm.sty) = %{tl_version}

%description -n texlive-yquant
This LaTeX package allows to quickly draw quantum circuits. It bridges the gap
between the two groups of packages that already exist: those that use a
logic-oriented custom language, which is then translated into TeX by means of
an external program; and the pure TeX versions that mainly provide some macros
to allow for an easier input. yquant is a pure-LaTeX solution -- i.e., it
requires no external program -- that introduces a logic oriented language and
thus brings the best of both worlds together. It builds on and interacts with
TikZ, which brings an enourmous flexibility for customization of individual
circuits.

%package -n texlive-ytableau
Summary:        Many-featured Young tableaux and Young diagrams
Version:        svn73766
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(ytableau.sty) = %{tl_version}

%description -n texlive-ytableau
The package provides several functions for drawing Young tableaux and Young
diagrams, extending the young and youngtab packages but providing lots more
features. Skew and coloured tableaux are easy, and pgfkeys-enabled options are
provided both at package load and configurably.

%package -n texlive-zeckendorf
Summary:        Knuth Fibonacci multiplication, Zeckendorf and Bergman representations of big integers
Version:        svn76884
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xintbinhex.sty)
Requires:       tex(xintexpr.sty)
Provides:       tex(zeckendorf.sty) = %{tl_version}
Provides:       tex(zeckendorf.tex) = %{tl_version}
Provides:       tex(zeckendorfcore.tex) = %{tl_version}

%description -n texlive-zeckendorf
This package extends the \xinteval syntax to do algebra in Q(phi) (where phi is
the golden ratio), and compute Fibonacci numbers, Zeckendorf representations of
positive integers and Bergman phi-representations of the positive elements of
Z[phi]. The $ character is used to compute the Knuth Fibonacci multiplication.
The package can be used either in a LaTeX document, or with Plain eTeX, or on
the command line in an interactive session using eTeX. Being based upon
xintexpr, it allows to compute with "arbitrarily" big integers, the reasonable
use being with integers of at most a few hundreds of digits.

%package -n texlive-zx-calculus
Summary:        A library to typeset ZX Calculus diagrams
Version:        svn70647
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz-cd.sty)
Requires:       tex(tikz.sty)
Provides:       tex(tikzlibraryzx-calculus.code.tex) = %{tl_version}
Provides:       tex(zx-calculus.sty) = %{tl_version}

%description -n texlive-zx-calculus
This library (based on the great TikZ and TikZ-cd packages) allows you to
typeset ZX-calculus directly in LaTeX. It comes with many pre-built wire
shapes, a highly customizable node style (with multiple flavours for putting
labels inside or outside nodes), and a "debugging" mode to avoid getting lost
in big diagrams.


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
tar -xf %{SOURCE548} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE549} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE550} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE551} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE552} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE553} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE554} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE555} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE556} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE557} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE558} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE559} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE560} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE561} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE562} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE563} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE564} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE565} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE566} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE567} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE568} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE569} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE570} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE571} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE572} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE573} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE574} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE575} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE576} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE577} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE578} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE579} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE580} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE581} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE582} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE583} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE584} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE585} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE586} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE587} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE588} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Apply sympytexpackage patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-bz#1442706-python-path.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Compile Python bytecode
%py_byte_compile %{python3} %{buildroot}%{_texmf_main}/scripts/sympytexpackage

# Main collection metapackage (empty)
%files

%files -n texlive-12many
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/12many/
%doc %{_texmf_main}/doc/latex/12many/

%files -n texlive-accents
%license mit.txt
%{_texmf_main}/tex/latex/accents/
%doc %{_texmf_main}/doc/latex/accents/

%files -n texlive-aiplans
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/aiplans/
%doc %{_texmf_main}/doc/latex/aiplans/

%files -n texlive-alg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/alg/
%doc %{_texmf_main}/doc/latex/alg/

%files -n texlive-algobox
%license gpl3.txt
%{_texmf_main}/tex/latex/algobox/
%doc %{_texmf_main}/doc/latex/algobox/

%files -n texlive-algorithm2e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/algorithm2e/
%doc %{_texmf_main}/doc/latex/algorithm2e/

%files -n texlive-algorithmicx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/algorithmicx/
%doc %{_texmf_main}/doc/latex/algorithmicx/

%files -n texlive-algorithms
%license lgpl2.1.txt
%{_texmf_main}/tex/latex/algorithms/
%doc %{_texmf_main}/doc/latex/algorithms/

%files -n texlive-algpseudocodex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/algpseudocodex/
%doc %{_texmf_main}/doc/latex/algpseudocodex/

%files -n texlive-algxpar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/algxpar/
%doc %{_texmf_main}/doc/latex/algxpar/

%files -n texlive-aligned-overset
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/aligned-overset/
%doc %{_texmf_main}/doc/latex/aligned-overset/

%files -n texlive-amscdx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/amscdx/
%doc %{_texmf_main}/doc/latex/amscdx/

%files -n texlive-annotate-equations
%license mit.txt
%{_texmf_main}/tex/latex/annotate-equations/
%doc %{_texmf_main}/doc/latex/annotate-equations/

%files -n texlive-apxproof
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/apxproof/
%doc %{_texmf_main}/doc/latex/apxproof/

%files -n texlive-aspen
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/aspen/
%doc %{_texmf_main}/doc/latex/aspen/

%files -n texlive-atableau
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/atableau/
%doc %{_texmf_main}/doc/latex/atableau/

%files -n texlive-autobreak
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/autobreak/
%doc %{_texmf_main}/doc/latex/autobreak/

%files -n texlive-backnaur
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/backnaur/
%doc %{_texmf_main}/doc/latex/backnaur/

%files -n texlive-begriff
%license gpl2.txt
%{_texmf_main}/tex/latex/begriff/
%doc %{_texmf_main}/doc/latex/begriff/

%files -n texlive-binomexp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/binomexp/
%doc %{_texmf_main}/doc/latex/binomexp/

%files -n texlive-biocon
%license gpl2.txt
%{_texmf_main}/tex/latex/biocon/
%doc %{_texmf_main}/doc/latex/biocon/

%files -n texlive-bitpattern
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bitpattern/
%doc %{_texmf_main}/doc/latex/bitpattern/

%files -n texlive-bodeplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bodeplot/
%doc %{_texmf_main}/doc/latex/bodeplot/

%files -n texlive-bohr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bohr/
%doc %{_texmf_main}/doc/latex/bohr/

%files -n texlive-boldtensors
%license gpl2.txt
%{_texmf_main}/tex/latex/boldtensors/
%doc %{_texmf_main}/doc/latex/boldtensors/

%files -n texlive-bosisio
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bosisio/
%doc %{_texmf_main}/doc/latex/bosisio/

%files -n texlive-bpchem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bpchem/
%doc %{_texmf_main}/doc/latex/bpchem/

%files -n texlive-bracealign
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bracealign/
%doc %{_texmf_main}/doc/latex/bracealign/

%files -n texlive-bropd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bropd/
%doc %{_texmf_main}/doc/latex/bropd/

%files -n texlive-broydensolve
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/broydensolve/
%doc %{_texmf_main}/doc/latex/broydensolve/

%files -n texlive-bussproofs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bussproofs/
%doc %{_texmf_main}/doc/latex/bussproofs/

%files -n texlive-bussproofs-colorful
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bussproofs-colorful/
%doc %{_texmf_main}/doc/latex/bussproofs-colorful/

%files -n texlive-bussproofs-extra
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bussproofs-extra/
%doc %{_texmf_main}/doc/latex/bussproofs-extra/

%files -n texlive-bytefield
%license lppl1.3.txt
%{_texmf_main}/tex/latex/bytefield/
%doc %{_texmf_main}/doc/latex/bytefield/

%files -n texlive-calculation
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/calculation/
%doc %{_texmf_main}/doc/latex/calculation/

%files -n texlive-cartonaugh
%{_texmf_main}/tex/latex/cartonaugh/
%doc %{_texmf_main}/doc/latex/cartonaugh/

%files -n texlive-cascade
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cascade/
%doc %{_texmf_main}/doc/latex/cascade/

%files -n texlive-causets
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/causets/
%doc %{_texmf_main}/doc/latex/causets/

%files -n texlive-ccfonts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ccfonts/
%doc %{_texmf_main}/doc/latex/ccfonts/

%files -n texlive-ccool
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ccool/
%doc %{_texmf_main}/doc/latex/ccool/

%files -n texlive-chemarrow
%license pd.txt
%{_texmf_main}/fonts/afm/public/chemarrow/
%{_texmf_main}/fonts/map/dvips/chemarrow/
%{_texmf_main}/fonts/source/public/chemarrow/
%{_texmf_main}/fonts/tfm/public/chemarrow/
%{_texmf_main}/fonts/type1/public/chemarrow/
%{_texmf_main}/tex/latex/chemarrow/
%doc %{_texmf_main}/doc/fonts/chemarrow/

%files -n texlive-chemcompounds
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemcompounds/
%doc %{_texmf_main}/doc/latex/chemcompounds/

%files -n texlive-chemcono
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemcono/
%doc %{_texmf_main}/doc/latex/chemcono/

%files -n texlive-chemexec
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemexec/
%doc %{_texmf_main}/doc/latex/chemexec/

%files -n texlive-chemformula
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemformula/
%doc %{_texmf_main}/doc/latex/chemformula/

%files -n texlive-chemformula-ru
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemformula-ru/
%doc %{_texmf_main}/doc/latex/chemformula-ru/

%files -n texlive-chemgreek
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemgreek/
%doc %{_texmf_main}/doc/latex/chemgreek/

%files -n texlive-chemmacros
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemmacros/
%doc %{_texmf_main}/doc/latex/chemmacros/

%files -n texlive-chemnum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemnum/
%doc %{_texmf_main}/doc/latex/chemnum/

%files -n texlive-chemobabel
%license bsd2.txt
%{_texmf_main}/tex/latex/chemobabel/
%doc %{_texmf_main}/doc/latex/chemobabel/

%files -n texlive-chemplants
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemplants/
%doc %{_texmf_main}/doc/latex/chemplants/

%files -n texlive-chemschemex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemschemex/
%doc %{_texmf_main}/doc/latex/chemschemex/

%files -n texlive-chemsec
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemsec/
%doc %{_texmf_main}/doc/latex/chemsec/

%files -n texlive-chemstyle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chemstyle/
%doc %{_texmf_main}/doc/latex/chemstyle/

%files -n texlive-clrscode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/clrscode/
%doc %{_texmf_main}/doc/latex/clrscode/

%files -n texlive-clrscode3e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/clrscode3e/
%doc %{_texmf_main}/doc/latex/clrscode3e/

%files -n texlive-codeanatomy
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/codeanatomy/
%doc %{_texmf_main}/doc/latex/codeanatomy/

%files -n texlive-coloredtheorem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/coloredtheorem/
%doc %{_texmf_main}/doc/latex/coloredtheorem/

%files -n texlive-commath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/commath/
%doc %{_texmf_main}/doc/latex/commath/

%files -n texlive-commutative-diagrams
%license mit.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/commutative-diagrams/
%{_texmf_main}/tex/latex/commutative-diagrams/
%{_texmf_main}/tex/plain/commutative-diagrams/
%doc %{_texmf_main}/doc/generic/commutative-diagrams/

%files -n texlive-complexity
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/complexity/
%doc %{_texmf_main}/doc/latex/complexity/

%files -n texlive-complexpolylongdiv
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/complexpolylongdiv/
%doc %{_texmf_main}/doc/latex/complexpolylongdiv/

%files -n texlive-computational-complexity
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/computational-complexity/
%{_texmf_main}/tex/latex/computational-complexity/
%doc %{_texmf_main}/doc/latex/computational-complexity/

%files -n texlive-concmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/concmath/
%doc %{_texmf_main}/doc/fonts/concmath/

%files -n texlive-concrete
%license knuth.txt
%{_texmf_main}/fonts/source/public/concrete/
%{_texmf_main}/fonts/tfm/public/concrete/
%doc %{_texmf_main}/doc/fonts/concrete/

%files -n texlive-conteq
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/conteq/
%doc %{_texmf_main}/doc/latex/conteq/

%files -n texlive-cora-macs
%license mit.txt
%{_texmf_main}/tex/latex/cora-macs/
%doc %{_texmf_main}/doc/latex/cora-macs/

%files -n texlive-correctmathalign
%license bsd.txt
%{_texmf_main}/tex/latex/correctmathalign/
%doc %{_texmf_main}/doc/latex/correctmathalign/

%files -n texlive-cryptocode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cryptocode/
%doc %{_texmf_main}/doc/latex/cryptocode/

%files -n texlive-cs-techrep
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cs-techrep/
%doc %{_texmf_main}/doc/latex/cs-techrep/

%files -n texlive-csassignments
%license mit.txt
%{_texmf_main}/tex/latex/csassignments/
%doc %{_texmf_main}/doc/latex/csassignments/

%files -n texlive-csthm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/csthm/
%doc %{_texmf_main}/doc/latex/csthm/

%files -n texlive-cvss
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cvss/
%doc %{_texmf_main}/doc/latex/cvss/

%files -n texlive-decision-table
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/decision-table/
%doc %{_texmf_main}/doc/latex/decision-table/

%files -n texlive-delim
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/delim/
%doc %{_texmf_main}/doc/latex/delim/

%files -n texlive-delimseasy
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/delimseasy/
%doc %{_texmf_main}/doc/latex/delimseasy/

%files -n texlive-delimset
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/delimset/
%doc %{_texmf_main}/doc/latex/delimset/

%files -n texlive-derivative
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/derivative/
%doc %{_texmf_main}/doc/latex/derivative/

%files -n texlive-diffcoeff
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/diffcoeff/
%doc %{_texmf_main}/doc/latex/diffcoeff/

%files -n texlive-digiconfigs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/digiconfigs/
%doc %{_texmf_main}/doc/latex/digiconfigs/

%files -n texlive-dijkstra
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dijkstra/
%doc %{_texmf_main}/doc/latex/dijkstra/

%files -n texlive-domaincoloring
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/domaincoloring/
%doc %{_texmf_main}/doc/lualatex/domaincoloring/

%files -n texlive-drawmatrix
%license mit.txt
%{_texmf_main}/tex/latex/drawmatrix/
%doc %{_texmf_main}/doc/latex/drawmatrix/

%files -n texlive-drawstack
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/drawstack/
%doc %{_texmf_main}/doc/latex/drawstack/

%files -n texlive-dyntree
%license lgpl2.1.txt
%{_texmf_main}/tex/latex/dyntree/
%doc %{_texmf_main}/doc/latex/dyntree/

%files -n texlive-easing
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/easing/
%doc %{_texmf_main}/doc/latex/easing/

%files -n texlive-ebproof
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ebproof/
%doc %{_texmf_main}/doc/latex/ebproof/

%files -n texlive-econometrics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/econometrics/
%doc %{_texmf_main}/doc/latex/econometrics/

%files -n texlive-eltex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eltex/
%doc %{_texmf_main}/doc/latex/eltex/

%files -n texlive-emf
%license gpl3.txt
%{_texmf_main}/tex/latex/emf/
%doc %{_texmf_main}/doc/latex/emf/

%files -n texlive-endiagram
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/endiagram/
%doc %{_texmf_main}/doc/latex/endiagram/

%files -n texlive-engtlc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/engtlc/
%doc %{_texmf_main}/doc/latex/engtlc/

%files -n texlive-eqexpl
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/eqexpl/
%doc %{_texmf_main}/doc/latex/eqexpl/

%files -n texlive-eqnarray
%license gpl3.txt
%{_texmf_main}/tex/latex/eqnarray/
%doc %{_texmf_main}/doc/latex/eqnarray/

%files -n texlive-eqnlines
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eqnlines/
%doc %{_texmf_main}/doc/latex/eqnlines/

%files -n texlive-eqnnumwarn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eqnnumwarn/
%doc %{_texmf_main}/doc/latex/eqnnumwarn/

%files -n texlive-euclidean-lattice
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/euclidean-lattice/
%doc %{_texmf_main}/doc/latex/euclidean-lattice/

%files -n texlive-euclideangeometry
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/euclideangeometry/
%doc %{_texmf_main}/doc/latex/euclideangeometry/

%files -n texlive-extarrows
%license lgpl2.1.txt
%{_texmf_main}/tex/latex/extarrows/
%doc %{_texmf_main}/doc/latex/extarrows/

%files -n texlive-extpfeil
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/extpfeil/
%doc %{_texmf_main}/doc/latex/extpfeil/

%files -n texlive-faktor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/faktor/
%doc %{_texmf_main}/doc/latex/faktor/

%files -n texlive-fascicules
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fascicules/
%doc %{_texmf_main}/doc/latex/fascicules/

%files -n texlive-fitch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fitch/
%doc %{_texmf_main}/doc/latex/fitch/

%files -n texlive-fixdif
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fixdif/
%doc %{_texmf_main}/doc/latex/fixdif/

%files -n texlive-fixmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fixmath/
%doc %{_texmf_main}/doc/latex/fixmath/

%files -n texlive-fnspe
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fnspe/
%doc %{_texmf_main}/doc/latex/fnspe/

%files -n texlive-fodot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fodot/
%doc %{_texmf_main}/doc/latex/fodot/

%files -n texlive-formal-grammar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/formal-grammar/
%doc %{_texmf_main}/doc/latex/formal-grammar/

%files -n texlive-fouridx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fouridx/
%doc %{_texmf_main}/doc/latex/fouridx/

%files -n texlive-freealign
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/freealign/
%doc %{_texmf_main}/doc/latex/freealign/

%files -n texlive-freemath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/freemath/
%doc %{_texmf_main}/doc/latex/freemath/

%files -n texlive-functan
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/functan/
%doc %{_texmf_main}/doc/latex/functan/

%files -n texlive-galois
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/galois/
%doc %{_texmf_main}/doc/latex/galois/

%files -n texlive-gastex
%license lppl1.3c.txt
%{_texmf_main}/dvips/gastex/
%{_texmf_main}/tex/latex/gastex/
%doc %{_texmf_main}/doc/latex/gastex/

%files -n texlive-gene-logic
%license other-free.txt
%{_texmf_main}/tex/latex/gene-logic/
%doc %{_texmf_main}/doc/latex/gene-logic/

%files -n texlive-ghsystem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ghsystem/
%doc %{_texmf_main}/doc/latex/ghsystem/

%files -n texlive-glosmathtools
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/glosmathtools/
%doc %{_texmf_main}/doc/latex/glosmathtools/

%files -n texlive-gotoh
%license mit.txt
%{_texmf_main}/tex/latex/gotoh/
%doc %{_texmf_main}/doc/latex/gotoh/

%files -n texlive-grundgesetze
%license gpl2.txt
%{_texmf_main}/tex/latex/grundgesetze/
%doc %{_texmf_main}/doc/latex/grundgesetze/

%files -n texlive-gu
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gu/
%doc %{_texmf_main}/doc/latex/gu/

%files -n texlive-helmholtz-ellis-ji-notation
%license cc-by-4.txt
%{_texmf_main}/fonts/opentype/public/helmholtz-ellis-ji-notation/
%{_texmf_main}/tex/latex/helmholtz-ellis-ji-notation/
%doc %{_texmf_main}/doc/fonts/helmholtz-ellis-ji-notation/

%files -n texlive-hep-graphic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hep-graphic/
%doc %{_texmf_main}/doc/latex/hep-graphic/

%files -n texlive-hep-reference
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hep-reference/
%doc %{_texmf_main}/doc/latex/hep-reference/

%files -n texlive-hepnames
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hepnames/
%doc %{_texmf_main}/doc/latex/hepnames/

%files -n texlive-hepparticles
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hepparticles/
%doc %{_texmf_main}/doc/latex/hepparticles/

%files -n texlive-hepthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hepthesis/
%doc %{_texmf_main}/doc/latex/hepthesis/

%files -n texlive-hepunits
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hepunits/
%doc %{_texmf_main}/doc/latex/hepunits/

%files -n texlive-hideproofs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hideproofs/
%doc %{_texmf_main}/doc/latex/hideproofs/

%files -n texlive-ibrackets
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ibrackets/
%doc %{_texmf_main}/doc/latex/ibrackets/

%files -n texlive-includernw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/includernw/
%doc %{_texmf_main}/doc/latex/includernw/

%files -n texlive-interval
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/interval/
%doc %{_texmf_main}/doc/latex/interval/

%files -n texlive-intexgral
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/intexgral/
%doc %{_texmf_main}/doc/latex/intexgral/

%files -n texlive-ionumbers
%license gpl2.txt
%{_texmf_main}/tex/latex/ionumbers/
%doc %{_texmf_main}/doc/latex/ionumbers/

%files -n texlive-isomath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/isomath/
%doc %{_texmf_main}/doc/latex/isomath/

%files -n texlive-isphysicalmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/isphysicalmath/
%doc %{_texmf_main}/doc/latex/isphysicalmath/

%files -n texlive-jkmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jkmath/
%doc %{_texmf_main}/doc/latex/jkmath/

%files -n texlive-jupynotex
%license apache2.txt
%{_texmf_main}/tex/latex/jupynotex/
%doc %{_texmf_main}/doc/latex/jupynotex/

%files -n texlive-karnaugh
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/karnaugh/
%doc %{_texmf_main}/doc/latex/karnaugh/

%files -n texlive-karnaugh-map
%{_texmf_main}/tex/latex/karnaugh-map/
%doc %{_texmf_main}/doc/latex/karnaugh-map/

%files -n texlive-karnaughmap
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/karnaughmap/
%doc %{_texmf_main}/doc/latex/karnaughmap/

%files -n texlive-keytheorems
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/keytheorems/
%doc %{_texmf_main}/doc/latex/keytheorems/

%files -n texlive-kvmap
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kvmap/
%doc %{_texmf_main}/doc/latex/kvmap/

%files -n texlive-letterswitharrows
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/letterswitharrows/
%doc %{_texmf_main}/doc/latex/letterswitharrows/

%files -n texlive-lie-hasse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lie-hasse/
%doc %{_texmf_main}/doc/latex/lie-hasse/

%files -n texlive-linearregression
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/linearregression/
%doc %{_texmf_main}/doc/latex/linearregression/

%files -n texlive-linkedthm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/linkedthm/
%doc %{_texmf_main}/doc/latex/linkedthm/

%files -n texlive-logicproof
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/logicproof/
%doc %{_texmf_main}/doc/latex/logicproof/

%files -n texlive-logictools
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/logictools/
%doc %{_texmf_main}/doc/latex/logictools/

%files -n texlive-longdivision
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/longdivision/
%doc %{_texmf_main}/doc/latex/longdivision/

%files -n texlive-lpform
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/lpform/
%doc %{_texmf_main}/doc/generic/lpform/

%files -n texlive-lplfitch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lplfitch/
%doc %{_texmf_main}/doc/latex/lplfitch/

%files -n texlive-lstbayes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lstbayes/
%doc %{_texmf_main}/doc/latex/lstbayes/

%files -n texlive-lua-regression
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/lua-regression/
%doc %{_texmf_main}/doc/lualatex/lua-regression/

%files -n texlive-luanumint
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luanumint/
%doc %{_texmf_main}/doc/lualatex/luanumint/

%files -n texlive-math-operator
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/math-operator/
%doc %{_texmf_main}/doc/latex/math-operator/

%files -n texlive-mathcommand
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mathcommand/
%doc %{_texmf_main}/doc/latex/mathcommand/

%files -n texlive-mathcomp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mathcomp/
%doc %{_texmf_main}/doc/latex/mathcomp/

%files -n texlive-mathfixs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mathfixs/
%doc %{_texmf_main}/doc/latex/mathfixs/

%files -n texlive-mathlig
%license other-free.txt
%{_texmf_main}/tex/generic/mathlig/

%files -n texlive-mathpartir
%license gpl2.txt
%{_texmf_main}/tex/latex/mathpartir/
%doc %{_texmf_main}/doc/latex/mathpartir/

%files -n texlive-mathpunctspace
%license bsd2.txt
%{_texmf_main}/tex/latex/mathpunctspace/
%doc %{_texmf_main}/doc/latex/mathpunctspace/

%files -n texlive-mathsemantics
%license mit.txt
%{_texmf_main}/tex/latex/mathsemantics/
%doc %{_texmf_main}/doc/latex/mathsemantics/

%files -n texlive-matlab-prettifier
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/matlab-prettifier/
%doc %{_texmf_main}/doc/latex/matlab-prettifier/

%files -n texlive-matrix-skeleton
%{_texmf_main}/tex/latex/matrix-skeleton/
%doc %{_texmf_main}/doc/latex/matrix-skeleton/

%files -n texlive-mattens
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mattens/
%doc %{_texmf_main}/doc/latex/mattens/

%files -n texlive-mecaso
%license gpl3.txt
%{_texmf_main}/tex/latex/mecaso/
%doc %{_texmf_main}/doc/latex/mecaso/

%files -n texlive-medmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/medmath/
%doc %{_texmf_main}/doc/latex/medmath/

%files -n texlive-membranecomputing
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/membranecomputing/
%doc %{_texmf_main}/doc/latex/membranecomputing/

%files -n texlive-memorygraphs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/memorygraphs/
%doc %{_texmf_main}/doc/latex/memorygraphs/

%files -n texlive-messagepassing
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/messagepassing/
%doc %{_texmf_main}/doc/latex/messagepassing/

%files -n texlive-mgltex
%license gpl3.txt
%{_texmf_main}/tex/latex/mgltex/
%doc %{_texmf_main}/doc/latex/mgltex/

%files -n texlive-mhchem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mhchem/
%doc %{_texmf_main}/doc/latex/mhchem/

%files -n texlive-mhequ
%license pd.txt
%{_texmf_main}/tex/latex/mhequ/
%doc %{_texmf_main}/doc/latex/mhequ/

%files -n texlive-miller
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/miller/
%doc %{_texmf_main}/doc/latex/miller/

%files -n texlive-mismath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mismath/
%doc %{_texmf_main}/doc/latex/mismath/

%files -n texlive-moremath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/moremath/
%doc %{_texmf_main}/doc/latex/moremath/

%files -n texlive-multiobjective
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/multiobjective/
%doc %{_texmf_main}/doc/latex/multiobjective/

%files -n texlive-naive-ebnf
%license mit.txt
%{_texmf_main}/tex/latex/naive-ebnf/
%doc %{_texmf_main}/doc/latex/naive-ebnf/

%files -n texlive-namedtensor
%license mit.txt
%{_texmf_main}/tex/latex/namedtensor/
%doc %{_texmf_main}/doc/latex/namedtensor/

%files -n texlive-natded
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/natded/
%doc %{_texmf_main}/doc/latex/natded/

%files -n texlive-nath
%license gpl2.txt
%{_texmf_main}/tex/latex/nath/
%doc %{_texmf_main}/doc/latex/nath/

%files -n texlive-nchairx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nchairx/
%doc %{_texmf_main}/doc/latex/nchairx/

%files -n texlive-nicematrix
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nicematrix/
%doc %{_texmf_main}/doc/latex/nicematrix/

%files -n texlive-nuc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nuc/
%doc %{_texmf_main}/doc/latex/nuc/

%files -n texlive-nucleardata
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nucleardata/
%doc %{_texmf_main}/doc/latex/nucleardata/

%files -n texlive-numbersets
%license mit.txt
%{_texmf_main}/tex/latex/numbersets/
%doc %{_texmf_main}/doc/latex/numbersets/

%files -n texlive-numerica
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/numerica/
%doc %{_texmf_main}/doc/latex/numerica/

%files -n texlive-numerica-plus
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/numerica-plus/
%doc %{_texmf_main}/doc/latex/numerica-plus/

%files -n texlive-numerica-tables
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/numerica-tables/
%doc %{_texmf_main}/doc/latex/numerica-tables/

%files -n texlive-objectz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/objectz/
%doc %{_texmf_main}/doc/latex/objectz/

%files -n texlive-odesandpdes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/odesandpdes/
%doc %{_texmf_main}/doc/latex/odesandpdes/

%files -n texlive-oplotsymbl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/oplotsymbl/
%doc %{_texmf_main}/doc/latex/oplotsymbl/

%files -n texlive-ot-tableau
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ot-tableau/
%doc %{_texmf_main}/doc/latex/ot-tableau/

%files -n texlive-oubraces
%license other-free.txt
%{_texmf_main}/tex/latex/oubraces/
%doc %{_texmf_main}/doc/latex/oubraces/

%files -n texlive-overarrows
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/overarrows/
%doc %{_texmf_main}/doc/latex/overarrows/

%files -n texlive-pascaltriangle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pascaltriangle/
%doc %{_texmf_main}/doc/latex/pascaltriangle/

%files -n texlive-perfectcut
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/perfectcut/
%doc %{_texmf_main}/doc/latex/perfectcut/

%files -n texlive-pfdicons
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pfdicons/
%doc %{_texmf_main}/doc/latex/pfdicons/

%files -n texlive-physconst
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/physconst/
%doc %{_texmf_main}/doc/latex/physconst/

%files -n texlive-physics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/physics/
%doc %{_texmf_main}/doc/latex/physics/

%files -n texlive-physics-patch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/physics-patch/
%doc %{_texmf_main}/doc/latex/physics-patch/

%files -n texlive-physics2
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/physics2/
%doc %{_texmf_main}/doc/latex/physics2/

%files -n texlive-physics3
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/physics3/
%doc %{_texmf_main}/doc/latex/physics3/

%files -n texlive-physunits
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/physunits/
%doc %{_texmf_main}/doc/latex/physunits/

%files -n texlive-pinoutikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pinoutikz/
%doc %{_texmf_main}/doc/latex/pinoutikz/

%files -n texlive-pm-isomath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pm-isomath/
%doc %{_texmf_main}/doc/latex/pm-isomath/

%files -n texlive-pmdraw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pmdraw/
%doc %{_texmf_main}/doc/latex/pmdraw/

%files -n texlive-polexpr
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/polexpr/
%doc %{_texmf_main}/doc/generic/polexpr/

%files -n texlive-prftree
%license gpl2.txt
%{_texmf_main}/tex/latex/prftree/
%doc %{_texmf_main}/doc/latex/prftree/

%files -n texlive-principia
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/principia/
%doc %{_texmf_main}/doc/latex/principia/

%files -n texlive-proba
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/proba/
%doc %{_texmf_main}/doc/latex/proba/

%files -n texlive-proof-at-the-end
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/proof-at-the-end/
%doc %{_texmf_main}/doc/latex/proof-at-the-end/

%files -n texlive-prooftrees
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/prooftrees/
%doc %{_texmf_main}/doc/latex/prooftrees/

%files -n texlive-pseudo
%license mit.txt
%{_texmf_main}/tex/latex/pseudo/
%doc %{_texmf_main}/doc/latex/pseudo/

%files -n texlive-pseudocode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pseudocode/
%doc %{_texmf_main}/doc/latex/pseudocode/

%files -n texlive-pythonhighlight
%license bsd.txt
%{_texmf_main}/tex/latex/pythonhighlight/
%doc %{_texmf_main}/doc/latex/pythonhighlight/

%files -n texlive-qsharp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qsharp/
%doc %{_texmf_main}/doc/latex/qsharp/

%files -n texlive-quantikz
%license cc-by-4.txt
%{_texmf_main}/tex/latex/quantikz/
%doc %{_texmf_main}/doc/latex/quantikz/

%files -n texlive-quantum-chemistry-bonn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quantum-chemistry-bonn/
%doc %{_texmf_main}/doc/latex/quantum-chemistry-bonn/

%files -n texlive-quantumcubemodel
%license mit.txt
%{_texmf_main}/tex/latex/quantumcubemodel/
%doc %{_texmf_main}/doc/latex/quantumcubemodel/

%files -n texlive-quickreaction
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quickreaction/
%doc %{_texmf_main}/doc/latex/quickreaction/

%files -n texlive-quiver
%license mit.txt
%{_texmf_main}/tex/latex/quiver/
%doc %{_texmf_main}/doc/latex/quiver/

%files -n texlive-qworld
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qworld/
%doc %{_texmf_main}/doc/latex/qworld/

%files -n texlive-rank-2-roots
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rank-2-roots/
%doc %{_texmf_main}/doc/latex/rank-2-roots/

%files -n texlive-rbt-mathnotes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rbt-mathnotes/
%doc %{_texmf_main}/doc/latex/rbt-mathnotes/

%files -n texlive-rec-thy
%license pd.txt
%{_texmf_main}/tex/latex/rec-thy/
%doc %{_texmf_main}/doc/latex/rec-thy/

%files -n texlive-reptheorem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/reptheorem/
%doc %{_texmf_main}/doc/latex/reptheorem/

%files -n texlive-resolsysteme
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/resolsysteme/
%doc %{_texmf_main}/doc/latex/resolsysteme/

%files -n texlive-rest-api
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rest-api/
%doc %{_texmf_main}/doc/latex/rest-api/

%files -n texlive-revquantum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/revquantum/
%doc %{_texmf_main}/doc/latex/revquantum/

%files -n texlive-ribbonproofs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ribbonproofs/
%doc %{_texmf_main}/doc/latex/ribbonproofs/

%files -n texlive-rigidnotation
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rigidnotation/
%doc %{_texmf_main}/doc/latex/rigidnotation/

%files -n texlive-rmathbr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rmathbr/
%doc %{_texmf_main}/doc/latex/rmathbr/

%files -n texlive-sankey
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/tex/latex/sankey/
%doc %{_texmf_main}/doc/latex/sankey/

%files -n texlive-sasnrdisplay
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sasnrdisplay/
%doc %{_texmf_main}/doc/latex/sasnrdisplay/

%files -n texlive-sciposter
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sciposter/
%doc %{_texmf_main}/doc/latex/sciposter/

%files -n texlive-sclang-prettifier
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sclang-prettifier/
%doc %{_texmf_main}/doc/latex/sclang-prettifier/

%files -n texlive-scratchx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scratchx/
%doc %{_texmf_main}/doc/latex/scratchx/

%files -n texlive-sesamanuel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sesamanuel/
%doc %{_texmf_main}/doc/latex/sesamanuel/

%files -n texlive-sfg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sfg/
%doc %{_texmf_main}/doc/latex/sfg/

%files -n texlive-shuffle
%license pd.txt
%{_texmf_main}/fonts/source/public/shuffle/
%{_texmf_main}/fonts/tfm/public/shuffle/
%{_texmf_main}/tex/latex/shuffle/
%doc %{_texmf_main}/doc/latex/shuffle/

%files -n texlive-simplebnf
%license mit.txt
%{_texmf_main}/tex/latex/simplebnf/
%doc %{_texmf_main}/doc/latex/simplebnf/

%files -n texlive-simpler-wick
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/simpler-wick/
%doc %{_texmf_main}/doc/latex/simpler-wick/

%files -n texlive-simples-matrices
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/simples-matrices/
%doc %{_texmf_main}/doc/latex/simples-matrices/

%files -n texlive-simplewick
%license gpl2.txt
%{_texmf_main}/tex/latex/simplewick/
%doc %{_texmf_main}/doc/latex/simplewick/

%files -n texlive-sistyle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sistyle/
%doc %{_texmf_main}/doc/latex/sistyle/

%files -n texlive-siunits
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/siunits/
%doc %{_texmf_main}/doc/latex/siunits/

%files -n texlive-siunitx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/siunitx/
%doc %{_texmf_main}/doc/latex/siunitx/

%files -n texlive-skmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/skmath/
%doc %{_texmf_main}/doc/latex/skmath/

%files -n texlive-spalign
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/spalign/
%doc %{_texmf_main}/doc/latex/spalign/

%files -n texlive-spbmark
%license cc-by-4.txt
%{_texmf_main}/tex/latex/spbmark/
%doc %{_texmf_main}/doc/latex/spbmark/

%files -n texlive-stanli
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/stanli/
%doc %{_texmf_main}/doc/latex/stanli/

%files -n texlive-statex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/statex/
%doc %{_texmf_main}/doc/latex/statex/

%files -n texlive-statex2
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/statex2/
%doc %{_texmf_main}/doc/latex/statex2/

%files -n texlive-statistics
%license gpl3.txt
%{_texmf_main}/tex/latex/statistics/
%doc %{_texmf_main}/doc/latex/statistics/

%files -n texlive-statistik
%license gpl2.txt
%{_texmf_main}/tex/latex/statistik/
%doc %{_texmf_main}/doc/latex/statistik/

%files -n texlive-statmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/statmath/
%doc %{_texmf_main}/doc/latex/statmath/

%files -n texlive-steinmetz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/steinmetz/
%doc %{_texmf_main}/doc/latex/steinmetz/

%files -n texlive-stmaryrd
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/stmaryrd/
%{_texmf_main}/fonts/map/dvips/stmaryrd/
%{_texmf_main}/fonts/source/public/stmaryrd/
%{_texmf_main}/fonts/tfm/public/stmaryrd/
%{_texmf_main}/fonts/type1/public/stmaryrd/
%{_texmf_main}/tex/latex/stmaryrd/
%doc %{_texmf_main}/doc/fonts/stmaryrd/

%files -n texlive-string-diagrams
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/string-diagrams/
%doc %{_texmf_main}/doc/latex/string-diagrams/

%files -n texlive-structmech
%license gpl3.txt
%{_texmf_main}/tex/latex/structmech/
%doc %{_texmf_main}/doc/latex/structmech/

%files -n texlive-struktex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/struktex/
%doc %{_texmf_main}/doc/latex/struktex/

%files -n texlive-substances
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/substances/
%doc %{_texmf_main}/doc/latex/substances/

%files -n texlive-subsupscripts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/subsupscripts/
%doc %{_texmf_main}/doc/latex/subsupscripts/

%files -n texlive-subtext
%license gpl3.txt
%{_texmf_main}/tex/latex/subtext/
%doc %{_texmf_main}/doc/latex/subtext/

%files -n texlive-susy
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/susy/
%doc %{_texmf_main}/doc/latex/susy/

%files -n texlive-syllogism
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/syllogism/
%doc %{_texmf_main}/doc/latex/syllogism/

%files -n texlive-sympytexpackage
%license gpl2.txt
%{_texmf_main}/scripts/sympytexpackage/
%{_texmf_main}/tex/latex/sympytexpackage/
%doc %{_texmf_main}/doc/latex/sympytexpackage/

%files -n texlive-synproof
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/synproof/
%doc %{_texmf_main}/doc/latex/synproof/

%files -n texlive-t-angles
%license gpl2.txt
%{_texmf_main}/tex/latex/t-angles/
%doc %{_texmf_main}/doc/latex/t-angles/

%files -n texlive-tablor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tablor/
%doc %{_texmf_main}/doc/latex/tablor/

%files -n texlive-temporal-logic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/temporal-logic/
%doc %{_texmf_main}/doc/latex/temporal-logic/

%files -n texlive-tensind
%license mit.txt
%{_texmf_main}/tex/latex/tensind/
%doc %{_texmf_main}/doc/latex/tensind/

%files -n texlive-tensor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tensor/
%doc %{_texmf_main}/doc/latex/tensor/

%files -n texlive-tensormatrix
%license gpl3.txt
%{_texmf_main}/tex/latex/tensormatrix/
%doc %{_texmf_main}/doc/latex/tensormatrix/

%files -n texlive-tex-ewd
%license bsd.txt
%{_texmf_main}/tex/generic/tex-ewd/
%doc %{_texmf_main}/doc/generic/tex-ewd/

%files -n texlive-textgreek
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/textgreek/
%doc %{_texmf_main}/doc/latex/textgreek/

%files -n texlive-textopo
%license gpl2.txt
%{_texmf_main}/tex/latex/textopo/
%doc %{_texmf_main}/doc/latex/textopo/

%files -n texlive-thermodynamics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thermodynamics/
%doc %{_texmf_main}/doc/latex/thermodynamics/

%files -n texlive-thmbox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thmbox/
%doc %{_texmf_main}/doc/latex/thmbox/

%files -n texlive-thmtools
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thmtools/
%doc %{_texmf_main}/doc/latex/thmtools/

%files -n texlive-tiscreen
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tiscreen/
%doc %{_texmf_main}/doc/latex/tiscreen/

%files -n texlive-tkz-interval
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tkz-interval/
%doc %{_texmf_main}/doc/latex/tkz-interval/

%files -n texlive-turnstile
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/turnstile/
%doc %{_texmf_main}/doc/latex/turnstile/

%files -n texlive-unitsdef
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/unitsdef/
%doc %{_texmf_main}/doc/latex/unitsdef/

%files -n texlive-venn
%license lppl1.3c.txt
%{_texmf_main}/metapost/venn/
%doc %{_texmf_main}/doc/metapost/venn/

%files -n texlive-witharrows
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/witharrows/
%doc %{_texmf_main}/doc/generic/witharrows/

%files -n texlive-xymtex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xymtex/
%doc %{_texmf_main}/doc/latex/xymtex/

%files -n texlive-yhmath
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/yhmath/
%{_texmf_main}/fonts/source/public/yhmath/
%{_texmf_main}/fonts/tfm/public/yhmath/
%{_texmf_main}/fonts/type1/public/yhmath/
%{_texmf_main}/fonts/vf/public/yhmath/
%{_texmf_main}/tex/latex/yhmath/
%doc %{_texmf_main}/doc/fonts/yhmath/

%files -n texlive-youngtab
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/youngtab/
%doc %{_texmf_main}/doc/generic/youngtab/

%files -n texlive-yquant
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/yquant/
%doc %{_texmf_main}/doc/latex/yquant/

%files -n texlive-ytableau
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ytableau/
%doc %{_texmf_main}/doc/latex/ytableau/

%files -n texlive-zeckendorf
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/zeckendorf/
%doc %{_texmf_main}/doc/generic/zeckendorf/

%files -n texlive-zx-calculus
%license mit.txt
%{_texmf_main}/tex/latex/zx-calculus/
%doc %{_texmf_main}/doc/latex/zx-calculus/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77507-1
- update to svn77507, fix descriptions, licensing, update components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn76005-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn76005-1
- Update to TeX Live 2025
