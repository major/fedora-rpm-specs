%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-pstricks
Epoch:          12
Version:        svn77232
Release:        1%{?dist}
Summary:        PSTricks

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-pstricks.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auto-pst-pdf.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auto-pst-pdf.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bclogo.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bclogo.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dsptricks.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dsptricks.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luapstricks.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luapstricks.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makeplot.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makeplot.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftricks.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftricks.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftricks2.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftricks2.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psbao.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psbao.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-2dplot.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-2dplot.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-3d.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-3d.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-3dplot.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-3dplot.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-abspos.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-abspos.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-am.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-am.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-antiprism.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-antiprism.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-arrow.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-arrow.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-asr.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-asr.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-bar.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-bar.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-barcode.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-barcode.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-bezier.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-bezier.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-blur.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-blur.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-bspline.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-bspline.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-calculate.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-calculate.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-calendar.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-calendar.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-cie.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-cie.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-circ.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-circ.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-coil.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-coil.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-contourplot.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-contourplot.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-cox.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-cox.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-dart.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-dart.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-dbicons.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-dbicons.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-diffraction.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-diffraction.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-electricfield.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-electricfield.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eps.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eps.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eucl.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eucl.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-exa.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-exa.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-feyn.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-feyn.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fill.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fill.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fit.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fit.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-flags.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-flags.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fourbarlinkage.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fourbarlinkage.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fr3d.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fr3d.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fractal.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fractal.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fun.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-fun.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-func.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-func.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-gantt.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-gantt.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-gears.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-gears.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-geo.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-geo.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-geometrictools.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-geometrictools.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-gr3d.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-gr3d.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-grad.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-grad.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-graphicx.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-graphicx.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-hsb.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-hsb.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-infixplot.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-infixplot.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-intersect.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-intersect.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-jtree.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-jtree.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-kepler.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-kepler.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-knot.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-knot.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-labo.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-labo.doc.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-layout.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-layout.doc.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-lens.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-lens.doc.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-light3d.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-light3d.doc.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-lsystem.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-lsystem.doc.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-magneticfield.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-magneticfield.doc.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-marble.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-marble.doc.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-massspring.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-massspring.doc.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-math.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-math.doc.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-mirror.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-mirror.doc.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-moire.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-moire.doc.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-node.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-node.doc.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-nutation.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-nutation.doc.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ob3d.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ob3d.doc.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ode.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ode.doc.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-optexp.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-optexp.doc.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-optic.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-optic.doc.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-osci.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-osci.doc.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ovl.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-ovl.doc.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pad.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pad.doc.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pdgr.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pdgr.doc.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-perspective.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-perspective.doc.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-platon.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-platon.doc.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-plot.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-plot.doc.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-poker.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-poker.doc.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-poly.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-poly.doc.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pulley.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pulley.doc.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-qtree.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-qtree.doc.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-rputover.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-rputover.doc.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-rubans.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-rubans.doc.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-shell.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-shell.doc.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-sigsys.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-sigsys.doc.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-slpe.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-slpe.doc.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-solarsystem.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-solarsystem.doc.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-solides3d.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-solides3d.doc.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-soroban.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-soroban.doc.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-spectra.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-spectra.doc.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-sphericaltrochoid.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-sphericaltrochoid.doc.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-spinner.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-spinner.doc.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-stru.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-stru.doc.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-support.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-support.doc.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-text.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-text.doc.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-thick.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-thick.doc.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-tools.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-tools.doc.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-tree.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-tree.doc.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-turtle.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-turtle.doc.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-tvz.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-tvz.doc.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-uml.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-uml.doc.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-vectorian.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-vectorian.doc.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-vehicle.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-vehicle.doc.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-venn.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-venn.doc.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-vowel.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-vowel.doc.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks.doc.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks-add.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks-add.doc.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks_calcnotes.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pstricks_calcnotes.doc.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uml.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uml.doc.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vaucanson-g.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vaucanson-g.doc.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vocaltract.tar.xz
Source231:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vocaltract.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-auto-pst-pdf
Requires:       texlive-bclogo
Requires:       texlive-collection-basic
Requires:       texlive-collection-plaingeneric
Requires:       texlive-dsptricks
Requires:       texlive-luapstricks
Requires:       texlive-makeplot
Requires:       texlive-pdftricks
Requires:       texlive-pdftricks2
Requires:       texlive-pedigree-perl
Requires:       texlive-psbao
Requires:       texlive-pst-2dplot
Requires:       texlive-pst-3d
Requires:       texlive-pst-3dplot
Requires:       texlive-pst-abspos
Requires:       texlive-pst-am
Requires:       texlive-pst-antiprism
Requires:       texlive-pst-arrow
Requires:       texlive-pst-asr
Requires:       texlive-pst-bar
Requires:       texlive-pst-barcode
Requires:       texlive-pst-bezier
Requires:       texlive-pst-blur
Requires:       texlive-pst-bspline
Requires:       texlive-pst-calculate
Requires:       texlive-pst-calendar
Requires:       texlive-pst-cie
Requires:       texlive-pst-circ
Requires:       texlive-pst-coil
Requires:       texlive-pst-contourplot
Requires:       texlive-pst-cox
Requires:       texlive-pst-dart
Requires:       texlive-pst-dbicons
Requires:       texlive-pst-diffraction
Requires:       texlive-pst-electricfield
Requires:       texlive-pst-eps
Requires:       texlive-pst-eucl
Requires:       texlive-pst-exa
Requires:       texlive-pst-feyn
Requires:       texlive-pst-fill
Requires:       texlive-pst-fit
Requires:       texlive-pst-flags
Requires:       texlive-pst-fourbarlinkage
Requires:       texlive-pst-fr3d
Requires:       texlive-pst-fractal
Requires:       texlive-pst-fun
Requires:       texlive-pst-func
Requires:       texlive-pst-gantt
Requires:       texlive-pst-gears
Requires:       texlive-pst-geo
Requires:       texlive-pst-geometrictools
Requires:       texlive-pst-gr3d
Requires:       texlive-pst-grad
Requires:       texlive-pst-graphicx
Requires:       texlive-pst-hsb
Requires:       texlive-pst-infixplot
Requires:       texlive-pst-intersect
Requires:       texlive-pst-jtree
Requires:       texlive-pst-kepler
Requires:       texlive-pst-knot
Requires:       texlive-pst-labo
Requires:       texlive-pst-layout
Requires:       texlive-pst-lens
Requires:       texlive-pst-light3d
Requires:       texlive-pst-lsystem
Requires:       texlive-pst-magneticfield
Requires:       texlive-pst-marble
Requires:       texlive-pst-massspring
Requires:       texlive-pst-math
Requires:       texlive-pst-mirror
Requires:       texlive-pst-moire
Requires:       texlive-pst-node
Requires:       texlive-pst-nutation
Requires:       texlive-pst-ob3d
Requires:       texlive-pst-ode
Requires:       texlive-pst-optexp
Requires:       texlive-pst-optic
Requires:       texlive-pst-osci
Requires:       texlive-pst-ovl
Requires:       texlive-pst-pad
Requires:       texlive-pst-pdf
Requires:       texlive-pst-pdgr
Requires:       texlive-pst-perspective
Requires:       texlive-pst-platon
Requires:       texlive-pst-plot
Requires:       texlive-pst-poker
Requires:       texlive-pst-poly
Requires:       texlive-pst-pulley
Requires:       texlive-pst-qtree
Requires:       texlive-pst-rputover
Requires:       texlive-pst-rubans
Requires:       texlive-pst-shell
Requires:       texlive-pst-sigsys
Requires:       texlive-pst-slpe
Requires:       texlive-pst-solarsystem
Requires:       texlive-pst-solides3d
Requires:       texlive-pst-soroban
Requires:       texlive-pst-spectra
Requires:       texlive-pst-sphericaltrochoid
Requires:       texlive-pst-spinner
Requires:       texlive-pst-stru
Requires:       texlive-pst-support
Requires:       texlive-pst-text
Requires:       texlive-pst-thick
Requires:       texlive-pst-tools
Requires:       texlive-pst-tree
Requires:       texlive-pst-turtle
Requires:       texlive-pst-tvz
Requires:       texlive-pst-uml
Requires:       texlive-pst-vectorian
Requires:       texlive-pst-vehicle
Requires:       texlive-pst-venn
Requires:       texlive-pst-vowel
Requires:       texlive-pst2pdf
Requires:       texlive-pstricks
Requires:       texlive-pstricks-add
Requires:       texlive-pstricks_calcnotes
Requires:       texlive-uml
Requires:       texlive-vaucanson-g
Requires:       texlive-vocaltract

%description
PSTricks core and all add-on packages.


%package -n texlive-auto-pst-pdf
Summary:        Wrapper for pst-pdf (with some psfrag features)
Version:        svn56596
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-ifplatform
Requires:       texlive-iftex
Requires:       texlive-xkeyval
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(pst-pdf.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(auto-pst-pdf.sty) = %{tl_version}

%description -n texlive-auto-pst-pdf
The package uses --shell-escape to execute pst-pdf when necessary. This makes
it especially easy to integrate into the workflow of an editor with just
"LaTeX" and "pdfLaTeX" buttons. Wrappers are provided for various
psfrag-related features so that Matlab figures via laprint, Mathematica figures
via MathPSfrag, and regular psfrag figures can all be input consistently and
easily.

%package -n texlive-bclogo
Summary:        Creating colourful boxes with logos
Version:        svn69578
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(pst-blur.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(bclogo.sty) = %{tl_version}

%description -n texlive-bclogo
The package facilitates the creation of colorful boxes with a title and logo.
It may use either TikZ or PSTricks as graphics engine.

%package -n texlive-dsptricks
Summary:        Macros for Digital Signal Processing plots
Version:        svn68753
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(dspblocks.sty) = %{tl_version}
Provides:       tex(dspfunctions.sty) = %{tl_version}
Provides:       tex(dsptricks.sty) = %{tl_version}

%description -n texlive-dsptricks
The package provides a set of LaTeX macros (based on PSTricks) for plotting the
kind of graphs and figures that are usually employed in digital signal
processing publications. DSPTricks provides facilities for standard
discrete-time "lollipop" plots, continuous-time and frequency plots, and
pole-zero plots. The companion package DSPFunctions (dspfunctions.sty) provides
macros for computing frequency responses and DFTs, while the package DSPBlocks
(dspblocks.sty) supports DSP block diagrams.

%package -n texlive-luapstricks
Summary:        A PSTricks backend for LuaLaTeX
Version:        svn77336
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-luapstricks
This package enables the use of PSTricks directly in LuaLaTeX documents,
without invoking external programmes, by implementing a PostScript interpreter
in Lua. Therefore it does not require shell escape to be enabled or special
environments, and instead allows PSTricks to be used exactly like in dvips
based documents.

%package -n texlive-makeplot
Summary:        Easy plots from Matlab in LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(makeplot.sty) = %{tl_version}

%description -n texlive-makeplot
Existing approaches to create EPS files from Matlab (laprint, mma2ltx, print
-eps, etc.) aren't satisfactory; makeplot aims to resolve this problem.
Makeplot is a LaTeX package that uses the pstricks pst-plot functions to plot
data that it takes from Matlab output files.

%package -n texlive-pdftricks
Summary:        Support for PSTricks in pdfTeX
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(moreverb.sty)
Provides:       tex(pdftricks.sty) = %{tl_version}

%description -n texlive-pdftricks
The PSTricks macros cannot be used (directly) with pdfTeX, since PSTricks uses
PostScript arithmetic, which isn't part of PDF. This package circumvents this
limitation so that the extensive facilities offered by the powerful PSTricks
package can be made use of in a pdfTeX document. This is done using the shell
escape function available in current TeX implementations. The package may also
be used in support of other 'PostScript-output-only' packages, such as PSfrag.
For alternatives, users may care to review the discussion in the PSTricks
online documentation.

%package -n texlive-pdftricks2
Summary:        Use PSTricks in pdfTeX
Version:        svn31016
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pdftricks2.sty) = %{tl_version}

%description -n texlive-pdftricks2
The package provides the means of processing documents (that contain pstricks
graphics specifications. The package is inspired by pdftricks

%package -n texlive-psbao
Summary:        Draw Bao diagrams
Version:        svn55013
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(cool.sty)
Requires:       tex(etex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(psbao.sty) = %{tl_version}

%description -n texlive-psbao
The package draws Bao diagrams in LaTeX. The package is a development of psgo,
and uses PSTricks to draw the diagrams.

%package -n texlive-pst-2dplot
Summary:        A PSTricks package for drawing 2D curves
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pst-2dplot.sty) = %{tl_version}

%description -n texlive-pst-2dplot
Pst-2dplot is a pstricks package that offers an easy-to-use and intuitive tool
for plotting 2-d curves. It defines an environment with commands similar to
MATLAB for plotting.

%package -n texlive-pst-3d
Summary:        A PSTricks package for tilting and other pseudo-3D tricks
Version:        svn17257
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-3d.sty) = %{tl_version}
Provides:       tex(pst-3d.tex) = %{tl_version}

%description -n texlive-pst-3d
The package provides basic macros that use PSTricks for shadows, tilting and
three dimensional representations of text or graphical objects.

%package -n texlive-pst-3dplot
Summary:        Draw 3D objects in parallel projection, using PSTricks
Version:        svn68727
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-3dplot.sty) = %{tl_version}
Provides:       tex(pst-3dplot.tex) = %{tl_version}

%description -n texlive-pst-3dplot
A package using PSTricks to draw a large variety of graphs and plots, including
3D maths functions. Data can be read from external data files, making this
package a generic tool for graphing within TeX/LaTeX, without the need for
external tools.

%package -n texlive-pst-abspos
Summary:        Put objects at an absolute position
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-abspos.sty) = %{tl_version}
Provides:       tex(pst-abspos.tex) = %{tl_version}

%description -n texlive-pst-abspos
The (PSTricks-related) package provides a command \pstPutAbs(x,y) to put an
object at an arbitrary absolute (or even a relative) position on the page.

%package -n texlive-pst-am
Summary:        Simulation of modulation and demodulation
Version:        svn19591
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(numprint.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-am.sty) = %{tl_version}

%description -n texlive-pst-am
The package allows the simulation of the modulated and demodulated amplitude of
radio waves. The user may plot curves of modulated signals, wave carrier,
signal modulation, signal recovery and signal demodulation.

%package -n texlive-pst-antiprism
Summary:        A PSTricks related package which draws an antiprism
Version:        svn46643
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-solides3d.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-antiprism.sty) = %{tl_version}
Provides:       tex(pst-antiprism.tex) = %{tl_version}

%description -n texlive-pst-antiprism
pst-antiprism is a PSTricks related package which draws an antiprism, which is
a semiregular polyhedron constructed with 2-gons and triangles.

%package -n texlive-pst-arrow
Summary:        Special arrows for PSTricks
Version:        svn61069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-arrow.sty) = %{tl_version}
Provides:       tex(pst-arrow.tex) = %{tl_version}

%description -n texlive-pst-arrow
This package has all the code from the package pstricks-add which was related
to arrows, like multiple arrows and so on.

%package -n texlive-pst-asr
Summary:        Typeset autosegmental representations for linguists
Version:        svn22138
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-asr.sty) = %{tl_version}
Provides:       tex(pst-asr.tex) = %{tl_version}

%description -n texlive-pst-asr
The package allows the user to typeset autosegmental representations. It uses
the PStricks, and xkeyval packages.

%package -n texlive-pst-bar
Summary:        Produces bar charts using PSTricks
Version:        svn64331
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-bar.sty) = %{tl_version}
Provides:       tex(pst-bar.tex) = %{tl_version}

%description -n texlive-pst-bar
The package uses pstricks to draw bar charts from data stored in a
comma-delimited file. Several types of bar charts may be drawn, and the drawing
parameters are highly customizable. No external packages are required except
those that are part of the standard PSTricks distribution.

%package -n texlive-pst-barcode
Summary:        Print barcodes using PostScript
Version:        svn77091
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-barcode.sty) = %{tl_version}
Provides:       tex(pst-barcode.tex) = %{tl_version}

%description -n texlive-pst-barcode
The pst-barcode package allows printing of barcodes, in a huge variety of
formats, including quick-response (qr) codes (see documentation for details).
As a PSTricks package, the package requires pstricks. The package uses
PostScript for calculating the bars. For PDF output use a multi-pass mechanism
such as pst-pdf.

%package -n texlive-pst-bezier
Summary:        Draw Bezier curves
Version:        svn41981
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-bezier.sty) = %{tl_version}
Provides:       tex(pst-bezier.tex) = %{tl_version}

%description -n texlive-pst-bezier
The package provides a macro \psbcurve for drawing a Bezier curve. Provision is
made for full control of over all the control points of the curve.

%package -n texlive-pst-blur
Summary:        PSTricks package for "blurred" shadows
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-blur.sty) = %{tl_version}
Provides:       tex(pst-blur.tex) = %{tl_version}

%description -n texlive-pst-blur
Pst-blur is a package built for use with PSTricks. It provides macros that
apply blurring to the normal shadow function of PSTricks.

%package -n texlive-pst-bspline
Summary:        Draw cubic Bspline curves and interpolations
Version:        svn40685
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Provides:       tex(pst-bspline.sty) = %{tl_version}
Provides:       tex(pst-bspline.tex) = %{tl_version}

%description -n texlive-pst-bspline
The package draws uniform, cubic B-spline curves, open and closed, based on a
sequence of B-spline control points. There is also code which permits drawing
the open or closed cubic Bspline curve interpolating a sequence of points.
Graphical output is created using PStricks.

%package -n texlive-pst-calculate
Summary:        Support for floating point operations at LaTeX level
Version:        svn49817
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(siunitx.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(pst-calculate.sty) = %{tl_version}

%description -n texlive-pst-calculate
This package provides an interface to the LaTeX3 floating point unit (part of
expl3), mainly used for PSTricks related packages to allow math expressions at
LaTeX level. siunitx is used for formatting the calculated number. The package
also depends on xkeyval and xparse.

%package -n texlive-pst-calendar
Summary:        Plot calendars in "fancy" ways
Version:        svn60480
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-calendar.sty) = %{tl_version}

%description -n texlive-pst-calendar
The package uses pstricks and pst-3d to draw tabular calendars, or calendars on
dodecahedra with a month to each face (the package also requires the multido
and pst-xkey packages). The package works for years 2000-2099, and has options
for calendars in French German and English, but the documentation is not
available in English.

%package -n texlive-pst-cie
Summary:        CIE color space
Version:        svn60959
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-cie.sty) = %{tl_version}
Provides:       tex(pst-cie.tex) = %{tl_version}

%description -n texlive-pst-cie
pst-cie is a PSTricks related package to show the different CIE color spaces:
Adobe, CIE, ColorMatch, NTSC, Pal-Secam, ProPhoto, SMPTE, and sRGB.

%package -n texlive-pst-circ
Summary:        PSTricks package for drawing electric circuits
Version:        svn72519
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-circ.sty) = %{tl_version}
Provides:       tex(pst-circ.tex) = %{tl_version}

%description -n texlive-pst-circ
The package is built using PSTricks and in particular pst-node. It can easily
draw current 2-terminal devices and some 3- and 4-terminal devices used in
electronic or electric theory. The package's macros are designed with a view to
'logical' representation of circuits, as far as possible, so as to relieve the
user of purely graphical considerations when expressing a circuit.

%package -n texlive-pst-coil
Summary:        A PSTricks package for coils, etc.
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-coil.sty) = %{tl_version}
Provides:       tex(pst-coil.tex) = %{tl_version}

%description -n texlive-pst-coil
Pst-coil is a PSTricks based package for coils and zigzags and for coil and
zigzag node connections.

%package -n texlive-pst-contourplot
Summary:        Draw implicit functions using the "marching squares" algorithm
Version:        svn48230
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-contourplot.sty) = %{tl_version}
Provides:       tex(pst-contourplot.tex) = %{tl_version}

%description -n texlive-pst-contourplot
This package allows to draw implicit functions "f(x,y) = 0" with options for
coloring the inside of the surfaces, for marking the points and arrowing the
curve at points chosen by the user. The package uses the "marching squares"
algorithm.

%package -n texlive-pst-cox
Summary:        Drawing regular complex polytopes with PSTricks
Version:        svn15878
License:        LGPL-2.1-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-coxcoor.sty) = %{tl_version}
Provides:       tex(pst-coxcoor.tex) = %{tl_version}
Provides:       tex(pst-coxeterp.sty) = %{tl_version}
Provides:       tex(pst-coxeterp.tex) = %{tl_version}

%description -n texlive-pst-cox
Pst-cox is a PSTricks package for drawing 2-dimensional projections of complex
regular polytopes (after the work of Coxeter). The package consists of a macro
library for drawing the projections. The complex polytopes appear in the study
of the root systems and play a crucial role in many domains related to
mathematics and physics. These polytopes have been completely described by
Coxeter in his book "Regular Complex Polytopes". There exist only a finite
numbers of exceptional regular complex polytopes (for example the icosahedron)
and some infinite series (for example, one can construct a multi-dimensional
analogue of the hypercube in any finite dimension). The library contains two
packages. The first, pst-coxcoor, is devoted to the exceptional complex regular
polytopes whose coordinates have been pre-computed. The second, pst-coxeterp,
is devoted to the infinite series.

%package -n texlive-pst-dart
Summary:        Plotting dart boards
Version:        svn60476
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-dart.sty) = %{tl_version}
Provides:       tex(pst-dart.tex) = %{tl_version}

%description -n texlive-pst-dart
pst-dart is a PSTricks related package and draws Dart Boards. Optional
arguments are the unit and the fontsize.

%package -n texlive-pst-dbicons
Summary:        Support for drawing ER diagrams
Version:        svn17556
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pst-dbicons.sty) = %{tl_version}

%description -n texlive-pst-dbicons
The package provides some useful macros in the database area. The package
focusses on typesetting ER-Diagrams in a declarative style, i.e., by
positioning some nodes and defining the position of all other nodes relative to
them by using the standard database terminology. The PSTricks package is
required for using pst-dbicons, but no deep knowledge of PSTricks commands is
required (although such knowledge is useful for exploiting the full
functionality of the package).

%package -n texlive-pst-diffraction
Summary:        Print diffraction patterns from various apertures
Version:        svn71819
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-3dplot.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-diffraction.sty) = %{tl_version}
Provides:       tex(pst-diffraction.tex) = %{tl_version}

%description -n texlive-pst-diffraction
The package enables the user to draw (using PSTricks) the diffraction patterns
for different geometric forms of apertures for monochromatic light (using
PSTricks). The aperture stops can have rectangular, circular or triangular
openings. The view of the diffraction may be planar, or three-dimensional.
Options available are the dimensions of the aperture under consideration and of
the particular optical setting, e.g. the radius in case of an circular opening.
Moreover one can choose the wavelength of the light (the associated color will
be calculated by the package).

%package -n texlive-pst-electricfield
Summary:        Draw electric field and equipotential lines with PSTricks
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-electricfield.sty) = %{tl_version}
Provides:       tex(pst-electricfield.tex) = %{tl_version}

%description -n texlive-pst-electricfield
The package provides macros to plot electric field and equipotential lines
using PStricks. There may be any number of charges which can be placed in a
cartesian coordinate system by (x,y) values.

%package -n texlive-pst-eps
Summary:        Create EPS files from PSTricks figures
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-eps.sty) = %{tl_version}
Provides:       tex(pst-eps.tex) = %{tl_version}

%description -n texlive-pst-eps
Pst-eps is a PSTricks-based package for exporting PSTricks images 'on the fly'
to encapsulated PostScript (EPS) image files, which can then be read into a
document in the usual way.

%package -n texlive-pst-eucl
Summary:        Euclidean geometry with PSTricks
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-calculate.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tools.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-eucl.sty) = %{tl_version}
Provides:       tex(pst-eucl.tex) = %{tl_version}

%description -n texlive-pst-eucl
The package allows the drawing of Euclidean geometric figures using TeX
pstricks macros for specifying mathematical constraints. It is thus possible to
build point using common transformations or intersections. The use of
coordinates is limited to points which controlled the figure.

%package -n texlive-pst-exa
Summary:        Typeset PSTricks examples, with code
Version:        svn45289
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accsupp.sty)
Requires:       tex(changepage.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(pst-exa.sty) = %{tl_version}

%description -n texlive-pst-exa
The (PSTricks-related) package provides an environment PSTexample to put code
and output side by side or one above the other.

%package -n texlive-pst-feyn
Summary:        Draw graphical elements for Feynman diagrams
Version:        svn48781
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-feyn.sty) = %{tl_version}
Provides:       tex(pst-feyn.tex) = %{tl_version}

%description -n texlive-pst-feyn
pst-feyn is a set of drawing graphical elements which are used for Feynman
diagrams. The package is based on the macros of the old package axodraw but
uses the capabilities of PSTricks.

%package -n texlive-pst-fill
Summary:        Fill or tile areas with PSTricks
Version:        svn60671
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-fill.sty) = %{tl_version}
Provides:       tex(pst-fill.tex) = %{tl_version}

%description -n texlive-pst-fill
Pst-fill is a PSTricks-based package for filling and tiling areas or
characters.

%package -n texlive-pst-fit
Summary:        Macros for curve fitting
Version:        svn70686
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-tools.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-fit.sty) = %{tl_version}
Provides:       tex(pst-fit.tex) = %{tl_version}

%description -n texlive-pst-fit
The package uses PSTricks to fit curves to: Linear Functions; Power Functions;
exp Function; Log_{10} and Log_e functions; Recip; Kings Law data; Gaussian;
and 4th order Polynomial

%package -n texlive-pst-flags
Summary:        Draw flags of countries using PSTricks
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(pst-all.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xfp.sty)
Provides:       tex(pst-Albania-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Angola-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Anguilla-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Barbados-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Dominica-flag.tex) = %{tl_version}
Provides:       tex(pst-Egypt-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Eritrea-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Iraq-flag-slogan.tex) = %{tl_version}
Provides:       tex(pst-Lesotho-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Malta-flag-seal-corner.tex) = %{tl_version}
Provides:       tex(pst-Malta-flag-seal-horse.tex) = %{tl_version}
Provides:       tex(pst-Malta-flag-seal-text.tex) = %{tl_version}
Provides:       tex(pst-Mongolia-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Nicaragua-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-Oman-seal.tex) = %{tl_version}
Provides:       tex(pst-Paraguay-seal-wreath.tex) = %{tl_version}
Provides:       tex(pst-Saudi-flag-seal.tex) = %{tl_version}
Provides:       tex(pst-SriLanka-seal.tex) = %{tl_version}
Provides:       tex(pst-Tajikistan-flag-seal-crown.tex) = %{tl_version}
Provides:       tex(pst-Uganda-flagseal.tex) = %{tl_version}
Provides:       tex(pst-flags-colors-html.sty) = %{tl_version}
Provides:       tex(pst-flags.sty) = %{tl_version}

%description -n texlive-pst-flags
This package provides a number of macros for rendering flags of countries and
their associated artefacts using PSTricks. Formatting of the resulting drawings
is entirely controlled by TeX macros. A good working knowledge of LaTeX should
be sufficient to design flags of sovereign countries and adapt them to create
new designs. Features such as color or shape customisation and dynamic
modifications are possible by cleverly adjusting the options supplied to the
TeX macros, see the documentation for examples. This package requires expl3,
fp, xfp, xcolor, pstricks and pst-all.

%package -n texlive-pst-fourbarlinkage
Summary:        Draw articulated quadrilaterals
Version:        svn77161
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-fourbarlinkage.sty) = %{tl_version}
Provides:       tex(pst-fourbarlinkage.tex) = %{tl_version}

%description -n texlive-pst-fourbarlinkage
An Articulated Quadrilateral is a four-bar linkage mechanism (four rods
connected by hinges) that changes shape as its joints move, creating complex,
predictable motions used in machines like pedal cranks, lamps, and even for
generating curves, functioning as a simple, one-degree-of-freedom system with
fascinating, non-intuitive movements and applications in engineering.

%package -n texlive-pst-fr3d
Summary:        Draw 3-dimensional framed boxes using PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pst-fr3d.sty) = %{tl_version}
Provides:       tex(pst-fr3d.tex) = %{tl_version}

%description -n texlive-pst-fr3d
A package using PSTricks to draw three dimensional framed boxes using a macro
\PstFrameBoxThreeD. The macro is especially useful for drawing 3d-seeming
buttons.

%package -n texlive-pst-fractal
Summary:        Draw fractal sets using PSTricks
Version:        svn64714
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-fractal.sty) = %{tl_version}
Provides:       tex(pst-fractal.tex) = %{tl_version}

%description -n texlive-pst-fractal
The package uses PSTricks to draw the Julia and Mandelbrot sets, the Sierpinski
triangle, Koch flake, and Apollonius Circle as well as fractal trees (which
need not be balanced) with a variety of different parameters (including varying
numbers of iterations). The package uses the pst-xkey package, part of the
xkeyval distribution.

%package -n texlive-pst-fun
Summary:        Draw "funny" objects with PSTricks
Version:        svn17909
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pst-slpe.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-fun.sty) = %{tl_version}
Provides:       tex(pst-fun.tex) = %{tl_version}

%description -n texlive-pst-fun
This is a PSTricks related package for drawing funny objects, like ant, bird,
fish, kangaroo, ... Such objects may be useful for testing other PSTricks
macros and/or packages. (Or they can be used for fun...)

%package -n texlive-pst-func
Summary:        PSTricks package for plotting mathematical functions
Version:        svn70822
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(luacode.sty)
Requires:       tex(pst-math.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-tools.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-func.sty) = %{tl_version}
Provides:       tex(pst-func.tex) = %{tl_version}

%description -n texlive-pst-func
The package is built for use with PSTricks. It provides macros for plotting and
manipulating various mathematical functions: polynomials and their derivatives
f(x)=an*x^n+an-1*x^(n-1)+...+a0 defined by the coefficients a0 a1 a2 ... and
the derivative order; the Fourier sum f(x) = a0/2+a1cos(omega
x)+...+b1sin(omega x)+... defined by the coefficients a0 a1 a2 ... b1 b2 b3
...; the Bessel function defined by its order; the Gauss function defined by
sigma and mu; Bezier curves from order 1 (two control points) to order 9 (10
control points); the superellipse function (the Lame curve); Chebyshev
polynomials of the first and second kind; the Thomae (or popcorn) function; the
Weierstrass function; various integration-derived functions; normal, binomial,
poisson, gamma, chi-squared, student's t, F, beta, Cauchy and Weibull
distribution functions and the Lorenz curve; the zeroes of a function, or the
intermediate point of two functions; the Vasicek function for describing the
evolution of interest rates; and implicit functions. The plots may be generated
as volumes of rotation about the X-axis, as well.

%package -n texlive-pst-gantt
Summary:        Draw GANTT charts with PSTricks
Version:        svn35832
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-gantt.sty) = %{tl_version}
Provides:       tex(pst-gantt.tex) = %{tl_version}

%description -n texlive-pst-gantt
The package uses PSTricks to draw GANTT charts, which are a kind of bar chart
that displays a project schedule. The package requires the pstricks apparatus,
of course.

%package -n texlive-pst-gears
Summary:        Drawing internal and external gears
Version:        svn77113
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-gears.sty) = %{tl_version}
Provides:       tex(pst-gears.tex) = %{tl_version}

%description -n texlive-pst-gears
The macro \pstgears[options](x,y) allows, among other things, the drawing of a
gear consisting of two or more external gears whose profile is an involute arc.

%package -n texlive-pst-geo
Summary:        Geographical Projections
Version:        svn74247
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(Staedte3dJG.tex) = %{tl_version}
Provides:       tex(capitals.tex) = %{tl_version}
Provides:       tex(capitals3d.tex) = %{tl_version}
Provides:       tex(cities.tex) = %{tl_version}
Provides:       tex(pst-geo.sty) = %{tl_version}
Provides:       tex(pst-geo.tex) = %{tl_version}
Provides:       tex(villesFrance.tex) = %{tl_version}
Provides:       tex(villesFrance3d.tex) = %{tl_version}
Provides:       tex(villesItalia.tex) = %{tl_version}
Provides:       tex(villesItalia3d.tex) = %{tl_version}

%description -n texlive-pst-geo
The package offers a set of PSTricks related packages for various cartographic
projections of the terrestrial sphere. The package pst-map2d provides
conventional projections such as Mercator, Lambert, cylindrical, etc. The
package pst-map3d treats representation in three dimensions of the terrestrial
sphere. Packages pst-map2dII and pst-map3dII allow use of the CIA World
DataBank II. Various parameters of the packages allow for choice of the level
of the detail and the layouts possible (cities, borders, rivers etc).
Substantial data files are provided, in an (internally) compressed format.
Decompression happens on-the-fly as a document using the data is displayed,
printed or converted to PDF format. A Perl script is provided for the user to
do the decompression, if the need should arise.

%package -n texlive-pst-geometrictools
Summary:        A PSTricks package to draw geometric tools
Version:        svn70953
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-geometrictools.sty) = %{tl_version}
Provides:       tex(pst-geometrictools.tex) = %{tl_version}

%description -n texlive-pst-geometrictools
This PSTricks package facilitates the drawing of protractors, rulers, compasses
and pencils.

%package -n texlive-pst-gr3d
Summary:        Three dimensional grids with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-gr3d.sty) = %{tl_version}
Provides:       tex(pst-gr3d.tex) = %{tl_version}

%description -n texlive-pst-gr3d
This PSTricks package provides a command \PstGridThreeD that will draw a three
dimensional grid, offering a number of options for its appearance.

%package -n texlive-pst-grad
Summary:        Filling with colour gradients, using PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-grad.sty) = %{tl_version}
Provides:       tex(pst-grad.tex) = %{tl_version}

%description -n texlive-pst-grad
The package fills with colour gradients, using PSTricks. The RGB, CMYK and HSB
models are supported. Other colour gradient mechanisms are to be found in
package pst-slpe.

%package -n texlive-pst-graphicx
Summary:        A PSTricks-compatible graphicx for use with Plain TeX
Version:        svn21717
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pst-graphicx.tex) = %{tl_version}

%description -n texlive-pst-graphicx
The package provides a version of graphicx that avoids loading the graphics
bundle's (original) keyval package, which clashes with pstricks' use of
xkeyval.

%package -n texlive-pst-hsb
Summary:        Curves with continuous colours
Version:        svn66739
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-hsb.sty) = %{tl_version}
Provides:       tex(pst-hsb.tex) = %{tl_version}

%description -n texlive-pst-hsb
This is a PSTricks-related package. It can plot lines and/or curves with
continuous colours. Only colours defined in the hsb model are supported.

%package -n texlive-pst-infixplot
Summary:        Using PSTricks plotting capacities with infix expressions rather than RPN
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(infix-RPN.sty) = %{tl_version}
Provides:       tex(infix-RPN.tex) = %{tl_version}
Provides:       tex(pst-infixplot.sty) = %{tl_version}
Provides:       tex(pst-infixplot.tex) = %{tl_version}

%description -n texlive-pst-infixplot
Plotting functions with pst-plot is very powerful but sometimes difficult to
learn since the syntax of \psplot and \parametricplot requires some PostScript
knowledge. The infix-RPN and pst-infixplot styles simplify the usage of
pst-plot for the beginner, providing macro commands that convert natural
mathematical expressions to PostScript syntax.

%package -n texlive-pst-intersect
Summary:        Compute intersections of arbitrary curves
Version:        svn33210
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-func.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-intersect.sty) = %{tl_version}
Provides:       tex(pst-intersect.tex) = %{tl_version}

%description -n texlive-pst-intersect
The package computes the intersections between arbitrary PostScript paths or
Bezier curves, using the Bezier clipping algorithm.

%package -n texlive-pst-jtree
Summary:        Typeset complex trees for linguists
Version:        svn20946
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pst-jtree.sty) = %{tl_version}
Provides:       tex(pst-jtree.tex) = %{tl_version}

%description -n texlive-pst-jtree
jTree uses PSTricks to enable linguists to typeset complex trees. The package
requires use of PStricks (of course) and xkeyval packages. jTree is a
development of, and replacement for, the jftree package, which is no longer
available.

%package -n texlive-pst-kepler
Summary:        Models for Johannes Kepler's view of the world
Version:        svn77232
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(animate.sty)
Requires:       tex(hvextern.sty)
Requires:       tex(pst-eucl.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xint.sty)
Requires:       tex(xintexpr.sty)
Provides:       tex(pst-kepler.sty) = %{tl_version}
Provides:       tex(pst-kepler.tex) = %{tl_version}

%description -n texlive-pst-kepler
This package is dedicated to Jurgen Gilg (8.2.1966-6.5.2022). It defines macros
which show Johannes Kepler's view of the world.

%package -n texlive-pst-knot
Summary:        PSTricks package for displaying knots
Version:        svn16033
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-knot.sty) = %{tl_version}
Provides:       tex(pst-knot.tex) = %{tl_version}

%description -n texlive-pst-knot
The package can produce a fair range of knot shapes, with all the standard
graphics controls one expects.

%package -n texlive-pst-labo
Summary:        Draw objects for Chemistry laboratories
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-labo.sty) = %{tl_version}
Provides:       tex(pst-labo.tex) = %{tl_version}
Provides:       tex(pst-laboObj.tex) = %{tl_version}

%description -n texlive-pst-labo
Pst-labo is a PSTricks related package for drawing basic and complex chemical
objects. The documentation of the package is illuminated with plenty of
illustrations together with their source code, making it an easy read.

%package -n texlive-pst-layout
Summary:        Page layout macros based on PSTricks packages
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(arrayjobx.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(pst-layout.sty) = %{tl_version}

%description -n texlive-pst-layout
The package provides a means of creating elaborate ("pseudo-tabular") layouts
of material, typically to be overlaid on an included graphic. The package
requires a recent version of the package pst-node and some other
pstricks-related material.

%package -n texlive-pst-lens
Summary:        Lenses with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-lens.sty) = %{tl_version}
Provides:       tex(pst-lens.tex) = %{tl_version}

%description -n texlive-pst-lens
This PSTricks package provides a really rather simple command \PstLens that
will draw a lens. Command parameters provide a remarkable range of effects.

%package -n texlive-pst-light3d
Summary:        Three dimensional lighting effects (PSTricks)
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-light3d.sty) = %{tl_version}
Provides:       tex(pst-light3d.tex) = %{tl_version}

%description -n texlive-pst-light3d
A PSTricks package for three dimensional lighting effects on characters and
PSTricks graphics, like lines, curves, plots, ...

%package -n texlive-pst-lsystem
Summary:        Create images based on a L-system
Version:        svn49556
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-lsystem.sty) = %{tl_version}
Provides:       tex(pst-lsystem.tex) = %{tl_version}

%description -n texlive-pst-lsystem
pst-lsystem is a PSTricks based package for creating images based on a
L-system. A L-system (Lindenmayer system) is a set of rules which can be used
to model the morphology of a variety of organisms or fractals like the
Kochflake or Hilbert curve.

%package -n texlive-pst-magneticfield
Summary:        Plotting a magnetic field with PSTricks
Version:        svn69493
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-magneticfield.sty) = %{tl_version}
Provides:       tex(pst-magneticfield.tex) = %{tl_version}

%description -n texlive-pst-magneticfield
pst-magneticfield is a PSTricks related package to draw the magnetic field
lines of Helmholtz coils in a two or three dimensional view. There are several
parameters to create a different output. For more information or some examples
read the documentation of the package.

%package -n texlive-pst-marble
Summary:        A PSTricks package to draw marble-like patterns
Version:        svn50925
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-marble.sty) = %{tl_version}
Provides:       tex(pst-marble.tex) = %{tl_version}

%description -n texlive-pst-marble
This is a PSTricks package to draw marble-like patterns.

%package -n texlive-pst-massspring
Summary:        Create animations for two masses connected by a spring
Version:        svn77131
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-massspring.sty) = %{tl_version}
Provides:       tex(pst-massspring.tex) = %{tl_version}

%description -n texlive-pst-massspring
This package can create animations (gif or pdf) for two masses connected by a
spring in a free fall.

%package -n texlive-pst-math
Summary:        Enhancement of PostScript math operators to use with PSTricks
Version:        svn67535
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-calculate.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xstring.sty)
Provides:       tex(pst-math.sty) = %{tl_version}
Provides:       tex(pst-math.tex) = %{tl_version}

%description -n texlive-pst-math
PostScript lacks a lot of basic operators such as tan, acos, asin, cosh, sinh,
tanh, acosh, asinh, atanh, exp (with e base). Also (oddly) cos and sin use
arguments in degrees. Pst-math provides all those operators in a header file
pst-math.pro with wrappers pst-math.sty and pst-math.tex. In addition, sinc,
gauss, gammaln and bessel are implemented (only partially for the latter). The
package is designed essentially to work with pst-plot but can be used in
whatever PS code (such as PSTricks SpecialCoor "!", which is useful for placing
labels). The package also provides a routine SIMPSON for numerical integration
and a solver of linear equation systems.

%package -n texlive-pst-mirror
Summary:        Images on a spherical mirror
Version:        svn71294
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-mirror.sty) = %{tl_version}
Provides:       tex(pst-mirror.tex) = %{tl_version}

%description -n texlive-pst-mirror
The package provides commands and supporting PostScript material for drawing
images as if reflected by a spherical mirror.

%package -n texlive-pst-moire
Summary:        A PSTricks package to draw moire patterns
Version:        svn60411
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-moire.sty) = %{tl_version}
Provides:       tex(pst-moire.tex) = %{tl_version}

%description -n texlive-pst-moire
This is a PSTricks package to draw moire patterns.

%package -n texlive-pst-node
Summary:        Nodes and node connections in PSTricks
Version:        svn71773
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-node.sty) = %{tl_version}
Provides:       tex(pst-node.tex) = %{tl_version}
Provides:       tex(pst-node97.tex) = %{tl_version}

%description -n texlive-pst-node
The package enables the user to connect information, and to place labels,
without knowing (in advance) the actual positions of the items to be connected,
or where the connecting line should go. The macros are useful for making graphs
and trees, mathematical diagrams, linguistic syntax diagrams, and so on. The
package contents were previously distributed as a part of the pstricks base
distribution; the package serves as an extension to PSTricks.

%package -n texlive-pst-nutation
Summary:        Rotation, precession, nutation of the earth
Version:        svn77145
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-nutation.sty) = %{tl_version}
Provides:       tex(pst-nutation.tex) = %{tl_version}

%description -n texlive-pst-nutation
This package illustrates the concepts of rotation, precession, and nutation of
the earth. pst-nutation defines the command \psNutation[options] to simulate
the behaviour of the earth.

%package -n texlive-pst-ob3d
Summary:        Three dimensional objects using PSTricks
Version:        svn54514
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-ob3d.sty) = %{tl_version}
Provides:       tex(pst-ob3d.tex) = %{tl_version}

%description -n texlive-pst-ob3d
The package uses PSTricks to provide basic three-dimensional objects. As yet,
only cubes (which can be deformed to rectangular parallelipipeds) and dies
(which are only a special kind of cubes) are defined.

%package -n texlive-pst-ode
Summary:        Solving initial value problems for sets of Ordinary Differential Equations
Version:        svn69296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-ode.sty) = %{tl_version}
Provides:       tex(pst-ode.tex) = %{tl_version}

%description -n texlive-pst-ode
The package defines \pstODEsolve for solving initial value problems for sets of
Ordinary Differential Equations (ODE) using the Runge-Kutta-Fehlberg (RKF45)
method with automatic step size adjustment. The result is stored as a
PostScript object and may be plotted later using macros from other PSTricks
packages, such as \listplot (pst-plot) and \listplotThreeD (pst-3dplot), or may
be further processed by user-defined PostScript procedures. Optionally, the
computed state vectors can be written as a table to a text file.

%package -n texlive-pst-optexp
Summary:        Drawing optical experimental setups
Version:        svn62977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-eucl.sty)
Requires:       tex(pst-intersect.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-optexp.sty) = %{tl_version}

%description -n texlive-pst-optexp
The package is a collection of optical components that facilitate easy
sketching of optical experimental setups. The package uses PSTricks for its
output. A wide range of free-ray and fibre components is provided, the
alignment, positioning and labelling of which can be achieved in very simple
and flexible ways. The components may be connected with fibers or beams, and
realistic raytraced beam paths are also possible.

%package -n texlive-pst-optic
Summary:        Drawing optics diagrams
Version:        svn72694
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-optic.sty) = %{tl_version}
Provides:       tex(pst-optic.tex) = %{tl_version}

%description -n texlive-pst-optic
A package for drawing both reflective and refractive optics diagrams. The
package requires pstricks later than version 1.10.

%package -n texlive-pst-osci
Summary:        Oscgons with PSTricks
Version:        svn68781
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-osci.sty) = %{tl_version}
Provides:       tex(pst-osci.tex) = %{tl_version}

%description -n texlive-pst-osci
This PSTricks package enables you to produce oscilloscope "screen shots". Three
channels can be used to represent the most common signals (damped or not):
namely sinusoidal, rectangular, triangular, dog's tooth (left and right
oriented). The third channel allows you to add, to subtract or to multiply the
two other signals. Lissajous diagrams (XY-mode) can also be obtained.

%package -n texlive-pst-ovl
Summary:        Create and manage graphical overlays
Version:        svn54963
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-ovl.sty) = %{tl_version}
Provides:       tex(pst-ovl.tex) = %{tl_version}

%description -n texlive-pst-ovl
The package is useful when building an image from assorted material, as in the
slides of a projected presentation. The package requires pstricks, and shares
that package's restrictions on usage when generating PDF output.

%package -n texlive-pst-pad
Summary:        Draw simple attachment systems with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-pad.sty) = %{tl_version}
Provides:       tex(pst-pad.tex) = %{tl_version}

%description -n texlive-pst-pad
The package collects a set of graphical elements based on PStricks that can be
used to facilitate display of attachment systems such as two differently shaped
surfaces with or without a fluid wedged in between. These macros ease the
display of wet adhesion models and common friction systems such as boundary
lubrication, elastohydrodynamic lubrication and hydrodynamic lubrication.

%package -n texlive-pst-pdgr
Summary:        Draw medical pedigrees using PSTricks
Version:        svn45875
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-pdgr.sty) = %{tl_version}
Provides:       tex(pst-pdgr.tex) = %{tl_version}

%description -n texlive-pst-pdgr
The package provides a set of macros based on PSTricks to draw medical
pedigrees according to the recommendations for standardized human pedigree
nomenclature. The drawing commands place the symbols on a pspicture canvas. An
interface for making trees is also provided. The package may be used both with
LaTeX and PlainTeX. A separate Perl program for generating TeX files from
spreadsheets is available.

%package -n texlive-pst-perspective
Summary:        Draw perspective views using PSTricks
Version:        svn39585
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-grad.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-perspective.sty) = %{tl_version}
Provides:       tex(pst-perspective.tex) = %{tl_version}

%description -n texlive-pst-perspective
The package provides the means to draw an orthogonal parallel projection with
an arbitrarily chosen angle and a variable shortening factor.

%package -n texlive-pst-platon
Summary:        Platonic solids in PSTricks
Version:        svn16538
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-platon.sty) = %{tl_version}

%description -n texlive-pst-platon
The package adds to PSTricks the ability to draw 3-dimensional views of the
five Platonic solids.

%package -n texlive-pst-plot
Summary:        Plot data using PSTricks
Version:        svn65346
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-plot.sty) = %{tl_version}
Provides:       tex(pst-plot.tex) = %{tl_version}
Provides:       tex(pst-plot97.tex) = %{tl_version}

%description -n texlive-pst-plot
The package provides plotting of data (typically from external files), using
PSTricks. Plots may be configured using a wide variety of parameters.

%package -n texlive-pst-poker
Summary:        Drawing poker cards
Version:        svn75726
License:        LGPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-blur.sty)
Requires:       tex(pst-fill.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-poker.sty) = %{tl_version}

%description -n texlive-pst-poker
This PSTricks related package can create poker cards in various manners.

%package -n texlive-pst-poly
Summary:        Polygons with PSTricks
Version:        svn35062
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-poly.sty) = %{tl_version}
Provides:       tex(pst-poly.tex) = %{tl_version}

%description -n texlive-pst-poly
This PSTricks package provides a really rather simple command \PstPolygon that
will draw various regular and non-regular polygons (according to command
parameters); various shortcuts to commonly-used polygons are provided, as well
as a command \pspolygonbox that frames text with a polygon. The package uses
the xkeyval package for argument decoding.

%package -n texlive-pst-pulley
Summary:        Plot pulleys, using PSTricks
Version:        svn62977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-pulley.sty) = %{tl_version}
Provides:       tex(pst-pulley.tex) = %{tl_version}

%description -n texlive-pst-pulley
The package enables the user to draw pulley systems with up to 6 pulleys. The
pulley diagrams are labelled with the physical properties of the system. The
package uses pstricks and requires several PSTricks-related packages.

%package -n texlive-pst-qtree
Summary:        Simple syntax for trees
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tree.sty)
Provides:       tex(pst-qtree.sty) = %{tl_version}
Provides:       tex(pst-qtree.tex) = %{tl_version}

%description -n texlive-pst-qtree
The package provides a qtree-like front end for PSTricks.

%package -n texlive-pst-rputover
Summary:        Place text over objects without obscuring background colors
Version:        svn44724
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-rputover.sty) = %{tl_version}
Provides:       tex(pst-rputover.tex) = %{tl_version}

%description -n texlive-pst-rputover
This is a PSTricks package which allows to place text over objects without
obscuring background colors.

%package -n texlive-pst-rubans
Summary:        Draw three-dimensional ribbons
Version:        svn23464
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-rubans.sty) = %{tl_version}
Provides:       tex(pst-rubans.tex) = %{tl_version}

%description -n texlive-pst-rubans
The package uses PStricks and pst-solides3d to draw three dimensional ribbons
on a cylinder, torus, sphere, cone or paraboloid. The width of the ribbon, the
number of turns, the colour of the outer and the inner surface of the ribbon
may be set. In the case of circular and conical helices, one may also choose
the number of ribbons.

%package -n texlive-pst-shell
Summary:        Plotting sea shells
Version:        svn56070
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-shell.sty) = %{tl_version}
Provides:       tex(pst-shell.tex) = %{tl_version}

%description -n texlive-pst-shell
pst-shell is a PSTricks related package to draw seashells in 3D view:
Argonauta, Epiteonium, Lyria, Turritella, Tonna, Achatina, Oxystele, Conus,
Ammonite, Codakia, Escalaria, Helcion, Natalina, Planorbis, and Nautilus, all
with different parameters. pst-shell needs pst-solides3d and an up-to-date
PSTricks, which should be part of your local TeX installation, otherwise get it
from a CTAN server.

%package -n texlive-pst-sigsys
Summary:        Support of signal processing-related disciplines
Version:        svn21667
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-sigsys.sty) = %{tl_version}
Provides:       tex(pst-sigsys.tex) = %{tl_version}

%description -n texlive-pst-sigsys
The package offers a collection of useful macros for disciplines related to
signal processing. It defines macros for plotting a sequence of numbers,
drawing the pole-zero diagram of a system, shading the region of convergence,
creating an adder or a multiplier node, placing a framed node at a given
coordinate, creating an up-sampler or a down-sampler node, drawing the block
diagram of a system, drawing adaptive systems, sequentially connecting a list
of nodes, and connecting a list of nodes using any node-connecting macro.

%package -n texlive-pst-slpe
Summary:        Sophisticated colour gradients
Version:        svn24391
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-slpe.sty) = %{tl_version}
Provides:       tex(pst-slpe.tex) = %{tl_version}

%description -n texlive-pst-slpe
This PStricks package covers all the colour gradient functionality of pst-grad
(part of the base PSTricks distribution), and provides the following
facilities: it permits the user to specify an arbitrary number of colours,
along with the points at which they are to be reached; it converts between RGB
and HSV behind the scenes; it provides concentric and radial gradients; it
provides a command \psBall that generates bullets with a three-dimensional
appearance; and uses the xkeyval package for the extended key handling.

%package -n texlive-pst-solarsystem
Summary:        Plot the solar system for a specific date
Version:        svn69675
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-solarsystem.sty) = %{tl_version}
Provides:       tex(pst-solarsystem.tex) = %{tl_version}

%description -n texlive-pst-solarsystem
The package uses pstricks to produce diagrams of the visible planets, projected
on the plane of the ecliptic. It is not possible to represent all the planets
in their real proportions, so only Mercury, Venus, Earth and Mars have their
orbits in correct proportions and their relative sizes are observed. Saturn and
Jupiter are in the right direction, but not in the correct size.

%package -n texlive-pst-solides3d
Summary:        Draw perspective views of 3D solids
Version:        svn68786
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-solides3d.sty) = %{tl_version}
Provides:       tex(pst-solides3d.tex) = %{tl_version}

%description -n texlive-pst-solides3d
The package is designed to draw solids in 3d perspective. Features include:
create primitive solids; create solids by including a list of its vertices and
faces; faces of solids and surfaces can be colored by choosing from a very
large palette of colors; draw parametric surfaces in algebraic and reverse
polish notation; create explicit and parameterized algebraic functions drawn in
2 or 3 dimensions; project text onto a plane or onto the faces of a solid;
support for including external database files.

%package -n texlive-pst-soroban
Summary:        Draw a Soroban using PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pstricks-add.sty)
Provides:       tex(pst-soroban.sty) = %{tl_version}

%description -n texlive-pst-soroban
The package uses PSTricks to draw a Japanese abacus, or soroban. The soroban is
still used in Japan today.

%package -n texlive-pst-spectra
Summary:        Draw continuum, emission and absorption spectra with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(pst-spectra.sty) = %{tl_version}
Provides:       tex(pst-spectra.tex) = %{tl_version}

%description -n texlive-pst-spectra
The package is a PSTricks extension, based on a NASA lines database. It allows
you to draw continuum, emission and absorption spectra. A Total of 16 880
visible lines from 99 elements can be displayed. The package requires the
xkeyval package for decoding its arguments.

%package -n texlive-pst-sphericaltrochoid
Summary:        Create animations of a spherical trochoid
Version:        svn77173
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-sphericaltrochoid.sty) = %{tl_version}
Provides:       tex(pst-sphericaltrochoid.tex) = %{tl_version}

%description -n texlive-pst-sphericaltrochoid
This package simulates the generation of a spherical trochoid by a point on a
circle rolling without sliding along the edge of another circle, but on the
same sphere. (See https://demonstrations.wolfram.com/SphericalTrochoid/)

%package -n texlive-pst-spinner
Summary:        Drawing a fidget spinner
Version:        svn66115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-spinner.sty) = %{tl_version}
Provides:       tex(pst-spinner.tex) = %{tl_version}

%description -n texlive-pst-spinner
This package aims to propose a model of the fidget spinner gadget. It exists
under different forms with 2, 3 poles and even more. We chose the most popular
model: the triple Fidget Spinner. You can run the PSTricks related documents
with XeLaTeX.

%package -n texlive-pst-stru
Summary:        Civil engineering diagrams, using PSTricks
Version:        svn38613
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-stru.sty) = %{tl_version}
Provides:       tex(pst-stru.tex) = %{tl_version}

%description -n texlive-pst-stru
This PSTricks-based package provides facilities to draw structural schemes in
civil engineering analysis, for beams, portals, arches and piles.

%package -n texlive-pst-support
Summary:        Assorted support files for use with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pst-support-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pst-support-doc <= 11:%{version}

%description -n texlive-pst-support
An appropriate set of job options, together with process scripts for use with
TeXnicCenter/

%package -n texlive-pst-text
Summary:        Text and character manipulation in PSTricks
Version:        svn49542
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-char.sty) = %{tl_version}
Provides:       tex(pst-text.sty) = %{tl_version}
Provides:       tex(pst-text.tex) = %{tl_version}

%description -n texlive-pst-text
Pst-text is a PSTricks based package for plotting text along a different path
and manipulating characters. It includes the functionality of the old package
pst-char.

%package -n texlive-pst-thick
Summary:        Drawing very thick lines and curves
Version:        svn16369
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-thick.sty) = %{tl_version}
Provides:       tex(pst-thick.tex) = %{tl_version}

%description -n texlive-pst-thick
The package supports drawing of very thick lines and curves in PSTricks, with
various fillings for the body of the lines.

%package -n texlive-pst-tools
Summary:        PSTricks support functions
Version:        svn60621
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-tools.sty) = %{tl_version}
Provides:       tex(pst-tools.tex) = %{tl_version}

%description -n texlive-pst-tools
The package provides helper functions for other PSTricks related packages.

%package -n texlive-pst-tree
Summary:        Trees, using PSTricks
Version:        svn60421
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-tree.sty) = %{tl_version}
Provides:       tex(pst-tree.tex) = %{tl_version}

%description -n texlive-pst-tree
pst-tree is a pstricks package that defines a macro \pstree which offers a
structured way of joining nodes created using pst-node in order to draw trees.

%package -n texlive-pst-turtle
Summary:        Commands for "turtle operations"
Version:        svn52261
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-turtle.sty) = %{tl_version}
Provides:       tex(pst-turtle.tex) = %{tl_version}

%description -n texlive-pst-turtle
This is a PSTricks related package for creating "Turtle" graphics. It supports
the commands forward, back, left, right, penup, and pendown.

%package -n texlive-pst-tvz
Summary:        Draw trees with more than one root node, using PSTricks
Version:        svn77256
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-tvz.sty) = %{tl_version}
Provides:       tex(pst-tvz.tex) = %{tl_version}

%description -n texlive-pst-tvz
The package uses PSTricks to draw trees with more than one root node. It is
similar to pst-tree, though it uses a different placement algorithm.

%package -n texlive-pst-uml
Summary:        UML diagrams with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-multido
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tree.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-uml.sty) = %{tl_version}

%description -n texlive-pst-uml
This a PSTricks package that provides support for drawing moderately complex
UML (Universal Modelling Language) diagrams. (The PDF documentation is written
in French.)

%package -n texlive-pst-vectorian
Summary:        Printing ornaments
Version:        svn60488
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(psvectorian.sty) = %{tl_version}

%description -n texlive-pst-vectorian
The package uses PSTricks to draw ornaments (a substantial repertoire of
ornaments is provided).

%package -n texlive-pst-vehicle
Summary:        A PSTricks package for rolling vehicles on graphs of mathematical functions
Version:        svn61438
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-vehicle.sty) = %{tl_version}
Provides:       tex(pst-vehicle.tex) = %{tl_version}

%description -n texlive-pst-vehicle
This package permits to represent vehicles rolling without slipping on
mathematical curves. Different types of vehicles are proposed, the shape of the
curve is to be defined by its equation "y=f(x)" in algebraic notation.

%package -n texlive-pst-venn
Summary:        A PSTricks package for drawing Venn sets
Version:        svn49316
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pst-venn.sty) = %{tl_version}

%description -n texlive-pst-venn
This is a PSTricks related package for drawing Venn diagrams with three
circles.

%package -n texlive-pst-vowel
Summary:        Enable arrows showing diphthongs on vowel charts
Version:        svn25228
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-node.sty)
Requires:       tex(vowel.sty)
Provides:       tex(pst-vowel.sty) = %{tl_version}

%description -n texlive-pst-vowel
The package extends the vowel package (distributed as part of the tipa bundle)
by allowing the user to draw arrows between vowels to show relationships such
as diphthong membership. The package depends on use of pstricks.

%package -n texlive-pstricks
Summary:        PostScript macros for TeX
Version:        svn77093
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(iftex.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-calculate.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pst-eps.sty)
Requires:       tex(pst-fill.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-pdf.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-text.sty)
Requires:       tex(pst-tree.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(pst-all.sty) = %{tl_version}
Provides:       tex(pst-code-arc.tex) = %{tl_version}
Provides:       tex(pst-code-box.tex) = %{tl_version}
Provides:       tex(pst-code-circle_ellipse.tex) = %{tl_version}
Provides:       tex(pst-code-grid.tex) = %{tl_version}
Provides:       tex(pst-code-pspicture.tex) = %{tl_version}
Provides:       tex(pst-code-put.tex) = %{tl_version}
Provides:       tex(pst-code-ref_rot.tex) = %{tl_version}
Provides:       tex(pst-fp.tex) = %{tl_version}
Provides:       tex(pst-key.sty) = %{tl_version}
Provides:       tex(pst-key.tex) = %{tl_version}
Provides:       tex(pstcol.sty) = %{tl_version}
Provides:       tex(pstricks-arrows.tex) = %{tl_version}
Provides:       tex(pstricks-color.tex) = %{tl_version}
Provides:       tex(pstricks-dots.tex) = %{tl_version}
Provides:       tex(pstricks-pdf.sty) = %{tl_version}
Provides:       tex(pstricks-plain.tex) = %{tl_version}
Provides:       tex(pstricks-tex.def) = %{tl_version}
Provides:       tex(pstricks-xetex.def) = %{tl_version}
Provides:       tex(pstricks.sty) = %{tl_version}
Provides:       tex(pstricks.tex) = %{tl_version}
Provides:       tex(pstricks97.tex) = %{tl_version}

%description -n texlive-pstricks
PSTricks offers an extensive collection of macros for generating PostScript
that is usable with most TeX macro formats, including Plain TeX, LaTeX,
AMS-TeX, and AMS-LaTeX. Included are macros for colour, graphics, pie charts,
rotation, trees and overlays. It has many special features, including a wide
variety of graphics (picture drawing) macros, with a flexible interface and
with colour support. There are macros for colouring or shading the cells of
tables. The package pstricks-add contains bug-fixes and additions for PSTricks
(among other things). PSTricks ordinarily uses PostScript \special commands,
which are not supported by pdf(La)TeX. This limitation may be overcome by using
either the pst-pdf or the pdftricks package, to generate a PDF inclusion from a
PSTricks diagram. PSTricks macros can also generate PDF output when the
document is processed XeTeX, without the need for other supporting packages.

%package -n texlive-pstricks-add
Summary:        A collection of add-ons and bugfixes for PSTricks
Version:        svn66887
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-calculate.sty)
Requires:       tex(pst-math.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(pstricks-add.sty) = %{tl_version}
Provides:       tex(pstricks-add.tex) = %{tl_version}

%description -n texlive-pstricks-add
Collects together examples that have been posted to the PSTricks mailing list,
together with many additional features for the basic pstricks, pst-plot and
pst-node, including: bugfixes; new options for the pspicture environment;
arrows; braces as node connection/linestyle; extended axes for plots (e.g.,
logarithm axes); polar plots; plotting tangent lines of curves or functions;
solving and printing differential equations; box plots; matrix plots; and pie
charts. The package makes use of PostScript routines provided by pst-math.

%package -n texlive-pstricks_calcnotes
Summary:        Use of PSTricks in calculus lecture notes
Version:        svn34363
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pstricks_calcnotes-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pstricks_calcnotes-doc <= 11:%{version}

%description -n texlive-pstricks_calcnotes
The bundle shows the construction of PSTricks macros to draw Riemann sums of an
integral and to draw the vector field of an ordinary differential equation. The
results are illustrated in a fragment of lecture notes.

%package -n texlive-uml
Summary:        UML diagrams in LaTeX
Version:        svn17476
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-node.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(relsize.sty)
Provides:       tex(uml.sty) = %{tl_version}

%description -n texlive-uml
A PSTricks related package for writing UML (Unified Modelling Language)
diagrams in LaTeX. Currently, it implements a subset of class diagrams, and
some extra constructs as well. The package cannot be used together with
pst-uml.

%package -n texlive-vaucanson-g
Summary:        PSTricks macros for drawing automata
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(VCColor-names.def) = %{tl_version}
Provides:       tex(VCPref-beamer.tex) = %{tl_version}
Provides:       tex(VCPref-default.tex) = %{tl_version}
Provides:       tex(VCPref-mystyle.tex) = %{tl_version}
Provides:       tex(VCPref-slides.tex) = %{tl_version}
Provides:       tex(Vaucanson-G.tex) = %{tl_version}
Provides:       tex(vaucanson-g.sty) = %{tl_version}
Provides:       tex(vaucanson.sty) = %{tl_version}

%description -n texlive-vaucanson-g
VauCanSon-G is a package that enables the user to draw automata within texts
written using LaTeX. The package macros make use of commands of PStricks.

%package -n texlive-vocaltract
Summary:        Visualise the vocal tract using LaTeX and PSTricks
Version:        svn25629
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(animate.sty)
Requires:       tex(arrayjob.sty)
Requires:       tex(color.sty)
Requires:       tex(fltpoint.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(multimedia.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(VocalTract.sty) = %{tl_version}

%description -n texlive-vocaltract
The package enables the user to visualise the vocal tract. The vocal tract (in
the package) is manipulated by a vector of articulation parameters according to
the S. Maeda model. Animation may be achieved by providing a sequence of
vectors over time (e.g., from Matlab). A sequence of vectors for certain German
phonemes is embedded in the package, which allows for animation when no other
vector is available. The package's graphics are produced using pstricks.


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-auto-pst-pdf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/auto-pst-pdf/
%doc %{_texmf_main}/doc/latex/auto-pst-pdf/

%files -n texlive-bclogo
%license lppl1.3c.txt
%{_texmf_main}/metapost/bclogo/
%{_texmf_main}/tex/latex/bclogo/
%doc %{_texmf_main}/doc/latex/bclogo/

%files -n texlive-dsptricks
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dsptricks/
%doc %{_texmf_main}/doc/latex/dsptricks/

%files -n texlive-luapstricks
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/luapstricks/
%{_texmf_main}/tex/lualatex/luapstricks/
%doc %{_texmf_main}/doc/lualatex/luapstricks/

%files -n texlive-makeplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/makeplot/
%doc %{_texmf_main}/doc/latex/makeplot/

%files -n texlive-pdftricks
%license gpl2.txt
%{_texmf_main}/tex/latex/pdftricks/
%doc %{_texmf_main}/doc/latex/pdftricks/

%files -n texlive-pdftricks2
%license gpl2.txt
%{_texmf_main}/tex/latex/pdftricks2/
%doc %{_texmf_main}/doc/latex/pdftricks2/

%files -n texlive-psbao
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/psbao/
%doc %{_texmf_main}/doc/latex/psbao/

%files -n texlive-pst-2dplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-2dplot/
%doc %{_texmf_main}/doc/generic/pst-2dplot/

%files -n texlive-pst-3d
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-3d/
%{_texmf_main}/tex/generic/pst-3d/
%{_texmf_main}/tex/latex/pst-3d/
%doc %{_texmf_main}/doc/generic/pst-3d/

%files -n texlive-pst-3dplot
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-3dplot/
%{_texmf_main}/tex/generic/pst-3dplot/
%{_texmf_main}/tex/latex/pst-3dplot/
%doc %{_texmf_main}/doc/generic/pst-3dplot/

%files -n texlive-pst-abspos
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-abspos/
%{_texmf_main}/tex/latex/pst-abspos/
%doc %{_texmf_main}/doc/generic/pst-abspos/

%files -n texlive-pst-am
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-am/
%doc %{_texmf_main}/doc/generic/pst-am/

%files -n texlive-pst-antiprism
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-antiprism/
%{_texmf_main}/tex/generic/pst-antiprism/
%{_texmf_main}/tex/latex/pst-antiprism/
%doc %{_texmf_main}/doc/generic/pst-antiprism/

%files -n texlive-pst-arrow
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-arrow/
%{_texmf_main}/tex/latex/pst-arrow/
%doc %{_texmf_main}/doc/generic/pst-arrow/

%files -n texlive-pst-asr
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-asr/
%{_texmf_main}/tex/latex/pst-asr/
%doc %{_texmf_main}/doc/generic/pst-asr/

%files -n texlive-pst-bar
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-bar/
%{_texmf_main}/tex/generic/pst-bar/
%{_texmf_main}/tex/latex/pst-bar/
%doc %{_texmf_main}/doc/generic/pst-bar/

%files -n texlive-pst-barcode
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-barcode/
%{_texmf_main}/tex/generic/pst-barcode/
%{_texmf_main}/tex/latex/pst-barcode/
%doc %{_texmf_main}/doc/generic/pst-barcode/

%files -n texlive-pst-bezier
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-bezier/
%{_texmf_main}/tex/generic/pst-bezier/
%{_texmf_main}/tex/latex/pst-bezier/
%doc %{_texmf_main}/doc/generic/pst-bezier/

%files -n texlive-pst-blur
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-blur/
%{_texmf_main}/tex/generic/pst-blur/
%{_texmf_main}/tex/latex/pst-blur/
%doc %{_texmf_main}/doc/generic/pst-blur/

%files -n texlive-pst-bspline
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-bspline/
%{_texmf_main}/tex/generic/pst-bspline/
%{_texmf_main}/tex/latex/pst-bspline/
%doc %{_texmf_main}/doc/generic/pst-bspline/

%files -n texlive-pst-calculate
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-calculate/
%doc %{_texmf_main}/doc/generic/pst-calculate/

%files -n texlive-pst-calendar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-calendar/
%doc %{_texmf_main}/doc/latex/pst-calendar/

%files -n texlive-pst-cie
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-cie/
%{_texmf_main}/tex/generic/pst-cie/
%{_texmf_main}/tex/latex/pst-cie/
%doc %{_texmf_main}/doc/generic/pst-cie/

%files -n texlive-pst-circ
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-circ/
%{_texmf_main}/tex/generic/pst-circ/
%{_texmf_main}/tex/latex/pst-circ/
%doc %{_texmf_main}/doc/generic/pst-circ/

%files -n texlive-pst-coil
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-coil/
%{_texmf_main}/tex/generic/pst-coil/
%{_texmf_main}/tex/latex/pst-coil/
%doc %{_texmf_main}/doc/generic/pst-coil/

%files -n texlive-pst-contourplot
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-contourplot/
%{_texmf_main}/tex/latex/pst-contourplot/
%doc %{_texmf_main}/doc/generic/pst-contourplot/

%files -n texlive-pst-cox
%license lgpl2.1.txt
%{_texmf_main}/dvips/pst-cox/
%{_texmf_main}/tex/generic/pst-cox/
%{_texmf_main}/tex/latex/pst-cox/
%doc %{_texmf_main}/doc/generic/pst-cox/

%files -n texlive-pst-dart
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-dart/
%{_texmf_main}/tex/latex/pst-dart/
%doc %{_texmf_main}/doc/generic/pst-dart/

%files -n texlive-pst-dbicons
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-dbicons/
%doc %{_texmf_main}/doc/generic/pst-dbicons/

%files -n texlive-pst-diffraction
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-diffraction/
%{_texmf_main}/tex/latex/pst-diffraction/
%doc %{_texmf_main}/doc/generic/pst-diffraction/

%files -n texlive-pst-electricfield
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-electricfield/
%{_texmf_main}/tex/generic/pst-electricfield/
%{_texmf_main}/tex/latex/pst-electricfield/
%doc %{_texmf_main}/doc/generic/pst-electricfield/

%files -n texlive-pst-eps
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-eps/
%{_texmf_main}/tex/latex/pst-eps/
%doc %{_texmf_main}/doc/generic/pst-eps/

%files -n texlive-pst-eucl
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-eucl/
%{_texmf_main}/tex/generic/pst-eucl/
%{_texmf_main}/tex/latex/pst-eucl/
%doc %{_texmf_main}/doc/generic/pst-eucl/

%files -n texlive-pst-exa
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-exa/
%doc %{_texmf_main}/doc/latex/pst-exa/

%files -n texlive-pst-feyn
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-feyn/
%{_texmf_main}/tex/generic/pst-feyn/
%{_texmf_main}/tex/latex/pst-feyn/
%doc %{_texmf_main}/doc/generic/pst-feyn/

%files -n texlive-pst-fill
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-fill/
%{_texmf_main}/tex/latex/pst-fill/
%doc %{_texmf_main}/doc/generic/pst-fill/

%files -n texlive-pst-fit
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-fit/
%{_texmf_main}/tex/latex/pst-fit/
%doc %{_texmf_main}/doc/generic/pst-fit/

%files -n texlive-pst-flags
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-flags/
%doc %{_texmf_main}/doc/latex/pst-flags/

%files -n texlive-pst-fourbarlinkage
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-fourbarlinkage/
%{_texmf_main}/tex/generic/pst-fourbarlinkage/
%{_texmf_main}/tex/latex/pst-fourbarlinkage/
%doc %{_texmf_main}/doc/generic/pst-fourbarlinkage/

%files -n texlive-pst-fr3d
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-fr3d/
%{_texmf_main}/tex/latex/pst-fr3d/
%doc %{_texmf_main}/doc/generic/pst-fr3d/

%files -n texlive-pst-fractal
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-fractal/
%{_texmf_main}/tex/generic/pst-fractal/
%{_texmf_main}/tex/latex/pst-fractal/
%doc %{_texmf_main}/doc/generic/pst-fractal/

%files -n texlive-pst-fun
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-fun/
%{_texmf_main}/tex/generic/pst-fun/
%{_texmf_main}/tex/latex/pst-fun/
%doc %{_texmf_main}/doc/generic/pst-fun/

%files -n texlive-pst-func
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-func/
%{_texmf_main}/tex/generic/pst-func/
%{_texmf_main}/tex/latex/pst-func/
%doc %{_texmf_main}/doc/generic/pst-func/

%files -n texlive-pst-gantt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-gantt/
%{_texmf_main}/tex/latex/pst-gantt/
%doc %{_texmf_main}/doc/generic/pst-gantt/

%files -n texlive-pst-gears
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-gears/
%{_texmf_main}/tex/latex/pst-gears/
%doc %{_texmf_main}/doc/generic/pst-gears/

%files -n texlive-pst-geo
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-geo/
%{_texmf_main}/tex/generic/pst-geo/
%{_texmf_main}/tex/latex/pst-geo/
%doc %{_texmf_main}/doc/generic/pst-geo/

%files -n texlive-pst-geometrictools
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-geometrictools/
%{_texmf_main}/tex/latex/pst-geometrictools/
%doc %{_texmf_main}/doc/generic/pst-geometrictools/

%files -n texlive-pst-gr3d
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-gr3d/
%{_texmf_main}/tex/latex/pst-gr3d/
%doc %{_texmf_main}/doc/generic/pst-gr3d/

%files -n texlive-pst-grad
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-grad/
%{_texmf_main}/tex/generic/pst-grad/
%{_texmf_main}/tex/latex/pst-grad/
%doc %{_texmf_main}/doc/generic/pst-grad/

%files -n texlive-pst-graphicx
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-graphicx/
%doc %{_texmf_main}/doc/generic/pst-graphicx/

%files -n texlive-pst-hsb
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-hsb/
%{_texmf_main}/tex/latex/pst-hsb/
%doc %{_texmf_main}/doc/generic/pst-hsb/

%files -n texlive-pst-infixplot
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-infixplot/
%{_texmf_main}/tex/latex/pst-infixplot/
%doc %{_texmf_main}/doc/generic/pst-infixplot/

%files -n texlive-pst-intersect
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-intersect/
%{_texmf_main}/tex/generic/pst-intersect/
%{_texmf_main}/tex/latex/pst-intersect/
%doc %{_texmf_main}/doc/latex/pst-intersect/

%files -n texlive-pst-jtree
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-jtree/
%{_texmf_main}/tex/latex/pst-jtree/
%doc %{_texmf_main}/doc/generic/pst-jtree/

%files -n texlive-pst-kepler
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-kepler/
%{_texmf_main}/tex/latex/pst-kepler/
%doc %{_texmf_main}/doc/generic/pst-kepler/

%files -n texlive-pst-knot
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-knot/
%{_texmf_main}/tex/generic/pst-knot/
%{_texmf_main}/tex/latex/pst-knot/
%doc %{_texmf_main}/doc/generic/pst-knot/

%files -n texlive-pst-labo
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-labo/
%{_texmf_main}/tex/latex/pst-labo/
%doc %{_texmf_main}/doc/generic/pst-labo/

%files -n texlive-pst-layout
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-layout/
%doc %{_texmf_main}/doc/latex/pst-layout/

%files -n texlive-pst-lens
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-lens/
%{_texmf_main}/tex/latex/pst-lens/
%doc %{_texmf_main}/doc/generic/pst-lens/

%files -n texlive-pst-light3d
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-light3d/
%{_texmf_main}/tex/generic/pst-light3d/
%{_texmf_main}/tex/latex/pst-light3d/
%doc %{_texmf_main}/doc/generic/pst-light3d/

%files -n texlive-pst-lsystem
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-lsystem/
%{_texmf_main}/tex/generic/pst-lsystem/
%{_texmf_main}/tex/latex/pst-lsystem/
%doc %{_texmf_main}/doc/generic/pst-lsystem/

%files -n texlive-pst-magneticfield
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-magneticfield/
%{_texmf_main}/tex/generic/pst-magneticfield/
%{_texmf_main}/tex/latex/pst-magneticfield/
%doc %{_texmf_main}/doc/generic/pst-magneticfield/

%files -n texlive-pst-marble
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-marble/
%{_texmf_main}/tex/generic/pst-marble/
%{_texmf_main}/tex/latex/pst-marble/
%doc %{_texmf_main}/doc/generic/pst-marble/

%files -n texlive-pst-massspring
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-massspring/
%{_texmf_main}/tex/latex/pst-massspring/
%doc %{_texmf_main}/doc/generic/pst-massspring/

%files -n texlive-pst-math
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-math/
%{_texmf_main}/tex/generic/pst-math/
%{_texmf_main}/tex/latex/pst-math/
%doc %{_texmf_main}/doc/generic/pst-math/

%files -n texlive-pst-mirror
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-mirror/
%{_texmf_main}/tex/generic/pst-mirror/
%{_texmf_main}/tex/latex/pst-mirror/
%doc %{_texmf_main}/doc/generic/pst-mirror/

%files -n texlive-pst-moire
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-moire/
%{_texmf_main}/tex/generic/pst-moire/
%{_texmf_main}/tex/latex/pst-moire/
%doc %{_texmf_main}/doc/generic/pst-moire/

%files -n texlive-pst-node
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-node/
%{_texmf_main}/tex/generic/pst-node/
%{_texmf_main}/tex/latex/pst-node/
%doc %{_texmf_main}/doc/generic/pst-node/

%files -n texlive-pst-nutation
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-nutation/
%{_texmf_main}/tex/generic/pst-nutation/
%{_texmf_main}/tex/latex/pst-nutation/
%doc %{_texmf_main}/doc/generic/pst-nutation/

%files -n texlive-pst-ob3d
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-ob3d/
%{_texmf_main}/tex/latex/pst-ob3d/
%doc %{_texmf_main}/doc/generic/pst-ob3d/

%files -n texlive-pst-ode
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-ode/
%{_texmf_main}/tex/generic/pst-ode/
%{_texmf_main}/tex/latex/pst-ode/
%doc %{_texmf_main}/doc/generic/pst-ode/

%files -n texlive-pst-optexp
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-optexp/
%{_texmf_main}/makeindex/pst-optexp/
%{_texmf_main}/tex/latex/pst-optexp/
%doc %{_texmf_main}/doc/latex/pst-optexp/

%files -n texlive-pst-optic
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-optic/
%{_texmf_main}/tex/latex/pst-optic/
%doc %{_texmf_main}/doc/generic/pst-optic/

%files -n texlive-pst-osci
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-osci/
%{_texmf_main}/tex/latex/pst-osci/
%doc %{_texmf_main}/doc/generic/pst-osci/

%files -n texlive-pst-ovl
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-ovl/
%{_texmf_main}/tex/generic/pst-ovl/
%{_texmf_main}/tex/latex/pst-ovl/
%doc %{_texmf_main}/doc/generic/pst-ovl/

%files -n texlive-pst-pad
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-pad/
%{_texmf_main}/tex/latex/pst-pad/
%doc %{_texmf_main}/doc/generic/pst-pad/

%files -n texlive-pst-pdgr
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-pdgr/
%{_texmf_main}/tex/latex/pst-pdgr/
%doc %{_texmf_main}/doc/generic/pst-pdgr/

%files -n texlive-pst-perspective
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-perspective/
%{_texmf_main}/tex/latex/pst-perspective/
%doc %{_texmf_main}/doc/generic/pst-perspective/

%files -n texlive-pst-platon
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-platon/
%doc %{_texmf_main}/doc/generic/pst-platon/

%files -n texlive-pst-plot
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-plot/
%{_texmf_main}/tex/latex/pst-plot/
%doc %{_texmf_main}/doc/generic/pst-plot/

%files -n texlive-pst-poker
%license lgpl.txt
%{_texmf_main}/tex/latex/pst-poker/
%doc %{_texmf_main}/doc/latex/pst-poker/

%files -n texlive-pst-poly
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-poly/
%{_texmf_main}/tex/latex/pst-poly/
%doc %{_texmf_main}/doc/generic/pst-poly/

%files -n texlive-pst-pulley
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-pulley/
%{_texmf_main}/tex/latex/pst-pulley/
%doc %{_texmf_main}/doc/generic/pst-pulley/

%files -n texlive-pst-qtree
%license gpl2.txt
%{_texmf_main}/tex/generic/pst-qtree/
%{_texmf_main}/tex/latex/pst-qtree/
%doc %{_texmf_main}/doc/generic/pst-qtree/

%files -n texlive-pst-rputover
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-rputover/
%{_texmf_main}/tex/latex/pst-rputover/
%doc %{_texmf_main}/doc/generic/pst-rputover/

%files -n texlive-pst-rubans
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-rubans/
%{_texmf_main}/tex/latex/pst-rubans/
%doc %{_texmf_main}/doc/generic/pst-rubans/

%files -n texlive-pst-shell
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-shell/
%{_texmf_main}/tex/generic/pst-shell/
%{_texmf_main}/tex/latex/pst-shell/
%doc %{_texmf_main}/doc/generic/pst-shell/

%files -n texlive-pst-sigsys
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-sigsys/
%{_texmf_main}/tex/latex/pst-sigsys/
%doc %{_texmf_main}/doc/generic/pst-sigsys/

%files -n texlive-pst-slpe
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-slpe/
%{_texmf_main}/tex/generic/pst-slpe/
%{_texmf_main}/tex/latex/pst-slpe/
%doc %{_texmf_main}/doc/generic/pst-slpe/

%files -n texlive-pst-solarsystem
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-solarsystem/
%{_texmf_main}/tex/generic/pst-solarsystem/
%{_texmf_main}/tex/latex/pst-solarsystem/
%doc %{_texmf_main}/doc/generic/pst-solarsystem/

%files -n texlive-pst-solides3d
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-solides3d/
%{_texmf_main}/tex/generic/pst-solides3d/
%{_texmf_main}/tex/latex/pst-solides3d/
%doc %{_texmf_main}/doc/generic/pst-solides3d/

%files -n texlive-pst-soroban
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-soroban/
%doc %{_texmf_main}/doc/generic/pst-soroban/

%files -n texlive-pst-spectra
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-spectra/
%{_texmf_main}/tex/generic/pst-spectra/
%{_texmf_main}/tex/latex/pst-spectra/
%doc %{_texmf_main}/doc/generic/pst-spectra/

%files -n texlive-pst-sphericaltrochoid
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-sphericaltrochoid/
%{_texmf_main}/tex/latex/pst-sphericaltrochoid/
%doc %{_texmf_main}/doc/generic/pst-sphericaltrochoid/

%files -n texlive-pst-spinner
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-spinner/
%{_texmf_main}/tex/generic/pst-spinner/
%{_texmf_main}/tex/latex/pst-spinner/
%doc %{_texmf_main}/doc/generic/pst-spinner/

%files -n texlive-pst-stru
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-stru/
%{_texmf_main}/tex/latex/pst-stru/
%doc %{_texmf_main}/doc/generic/pst-stru/

%files -n texlive-pst-support
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/generic/pst-support/

%files -n texlive-pst-text
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-text/
%{_texmf_main}/tex/generic/pst-text/
%{_texmf_main}/tex/latex/pst-text/
%doc %{_texmf_main}/doc/generic/pst-text/

%files -n texlive-pst-thick
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-thick/
%{_texmf_main}/tex/latex/pst-thick/
%doc %{_texmf_main}/doc/generic/pst-thick/

%files -n texlive-pst-tools
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-tools/
%{_texmf_main}/tex/generic/pst-tools/
%{_texmf_main}/tex/latex/pst-tools/
%doc %{_texmf_main}/doc/generic/pst-tools/

%files -n texlive-pst-tree
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-tree/
%{_texmf_main}/tex/latex/pst-tree/
%doc %{_texmf_main}/doc/generic/pst-tree/

%files -n texlive-pst-turtle
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-turtle/
%{_texmf_main}/tex/generic/pst-turtle/
%{_texmf_main}/tex/latex/pst-turtle/
%doc %{_texmf_main}/doc/generic/pst-turtle/

%files -n texlive-pst-tvz
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-tvz/
%{_texmf_main}/tex/latex/pst-tvz/
%doc %{_texmf_main}/doc/generic/pst-tvz/

%files -n texlive-pst-uml
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-uml/
%doc %{_texmf_main}/doc/generic/pst-uml/

%files -n texlive-pst-vectorian
%license lppl1.3c.txt
%{_texmf_main}/dvips/pst-vectorian/
%{_texmf_main}/tex/latex/pst-vectorian/
%doc %{_texmf_main}/doc/latex/pst-vectorian/

%files -n texlive-pst-vehicle
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pst-vehicle/
%{_texmf_main}/tex/latex/pst-vehicle/
%doc %{_texmf_main}/doc/generic/pst-vehicle/

%files -n texlive-pst-venn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-venn/
%doc %{_texmf_main}/doc/generic/pst-venn/

%files -n texlive-pst-vowel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pst-vowel/
%doc %{_texmf_main}/doc/latex/pst-vowel/

%files -n texlive-pstricks
%license lppl1.3c.txt
%{_texmf_main}/dvips/pstricks/
%{_texmf_main}/tex/generic/pstricks/
%{_texmf_main}/tex/latex/pstricks/
%doc %{_texmf_main}/doc/generic/pstricks/

%files -n texlive-pstricks-add
%license lppl1.3c.txt
%{_texmf_main}/dvips/pstricks-add/
%{_texmf_main}/tex/generic/pstricks-add/
%{_texmf_main}/tex/latex/pstricks-add/
%doc %{_texmf_main}/doc/generic/pstricks-add/

%files -n texlive-pstricks_calcnotes
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/pstricks_calcnotes/

%files -n texlive-uml
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uml/
%doc %{_texmf_main}/doc/latex/uml/

%files -n texlive-vaucanson-g
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/vaucanson-g/
%doc %{_texmf_main}/doc/generic/vaucanson-g/

%files -n texlive-vocaltract
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/vocaltract/
%doc %{_texmf_main}/doc/latex/vocaltract/

%changelog
* Wed Feb 04 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77232-1
- Update to svn77232, fix descriptions, licensing

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn65367-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn65367-1
- Update to TeX Live 2025
