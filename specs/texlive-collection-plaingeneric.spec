%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-plaingeneric
Epoch:          12
Version:        svn75599
Release:        3%{?dist}
Summary:        Plain (La)TeX packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-plaingeneric.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abbr.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abbr.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abstyles.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abstyles.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/advice.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/advice.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apnum.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apnum.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autoaligne.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autoaligne.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/barr.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/barr.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitelist.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitelist.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/borceux.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/borceux.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/c-pascal.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/c-pascal.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calcfrac.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calcfrac.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/catcodes.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/catcodes.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chronosys.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chronosys.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collargs.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collargs.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/colorsep.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/compare.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossrefenum.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossrefenum.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cweb-old.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dinat.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dinat.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dirtree.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dirtree.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/docbytex.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/docbytex.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dowith.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dowith.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eijkhout.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/encxvlna.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/encxvlna.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eoldef.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eoldef.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epigram.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf.doc.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf-dvipdfmx.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf-dvipdfmx.doc.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox-generic.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox-generic.doc.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex-acro.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex-acro.doc.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expkv-bundle.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expkv-bundle.doc.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fenixpar.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fenixpar.doc.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figflow.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figflow.doc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixpdfmag.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fltpoint.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fltpoint.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fntproof.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fntproof.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/font-change.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/font-change.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontch.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontch.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontname.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontname.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gates.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gates.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/getoptk.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/getoptk.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfnotation.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfnotation.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gobble.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gobble.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-pln.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-pln.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtl.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtl.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hlist.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hlist.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyplain.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyplain.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifis-macros.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifis-macros.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inputnormalization.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inputnormalization.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/insbox.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/insbox.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/js-misc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/js-misc.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kastrup.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kastrup.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lambda-lists.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lambda-lists.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langcode.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langcode.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lecturer.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lecturer.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letterspacing.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librarian.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librarian.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listofitems.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listofitems.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/localloc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/localloc.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathdots.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathdots.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/measurebox.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/measurebox.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metatex.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metatex.doc.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/midnight.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/midnight.doc.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkpattern.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkpattern.doc.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mlawriter.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mlawriter.doc.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modulus.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modulus.doc.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multido.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multido.doc.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/namedef.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/namedef.doc.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/navigator.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/navigator.doc.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newsletr.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newsletr.doc.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nth.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ofs.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ofs.doc.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/olsak-misc.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/olsak-misc.doc.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/outerhbox.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/path.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/path.doc.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdf-trans.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdf-trans.doc.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmsym.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmsym.doc.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftoolbox.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftoolbox.doc.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pitex.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pitex.doc.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/placeins-plain.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plain-widow.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plain-widow.doc.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plainpkg.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plainpkg.doc.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plipsum.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plipsum.doc.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plnfss.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plnfss.doc.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plstmary.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plstmary.doc.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poormanlog.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poormanlog.doc.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/present.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/present.doc.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pwebmac.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pwebmac.doc.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/random.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/random.doc.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/randomlist.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/randomlist.doc.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resumemac.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resumemac.doc.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ruler.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schemata.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schemata.doc.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shade.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shade.doc.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplekv.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplekv.doc.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soul.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soul.doc.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stretchy.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stretchy.doc.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/swrule.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/systeme.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/systeme.doc.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabto-generic.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/termmenu.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/termmenu.doc.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-ps.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-ps.doc.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texapi.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texapi.doc.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdate.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdate.doc.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdimens.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdimens.doc.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texinfo.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/timetable.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tokmap.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tokmap.doc.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tracklang.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tracklang.doc.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/transparent-io.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/transparent-io.doc.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/treetex.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/treetex.doc.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trigonometry.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trigonometry.doc.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuple.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuple.doc.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ulem.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ulem.doc.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/upca.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/upca.doc.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/varisize.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/varisize.doc.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualtoks.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualtoks.doc.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xii.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xii.doc.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xii-lat.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xii-lat.doc.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xintsession.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xintsession.doc.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xlop.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xlop.doc.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yax.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yax.doc.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zztex.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zztex.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-abbr
Requires:       texlive-abstyles
Requires:       texlive-advice
Requires:       texlive-apnum
Requires:       texlive-autoaligne
Requires:       texlive-barr
Requires:       texlive-bitelist
Requires:       texlive-borceux
Requires:       texlive-c-pascal
Requires:       texlive-calcfrac
Requires:       texlive-catcodes
Requires:       texlive-chronosys
Requires:       texlive-collargs
Requires:       texlive-collection-basic
Requires:       texlive-colorsep
Requires:       texlive-compare
Requires:       texlive-crossrefenum
Requires:       texlive-cweb-old
Requires:       texlive-dinat
Requires:       texlive-dirtree
Requires:       texlive-docbytex
Requires:       texlive-dowith
Requires:       texlive-eijkhout
Requires:       texlive-encxvlna
Requires:       texlive-eoldef
Requires:       texlive-epigram
Requires:       texlive-epsf
Requires:       texlive-epsf-dvipdfmx
Requires:       texlive-etoolbox-generic
Requires:       texlive-expex-acro
Requires:       texlive-expkv-bundle
Requires:       texlive-fenixpar
Requires:       texlive-figflow
Requires:       texlive-fixpdfmag
Requires:       texlive-fltpoint
Requires:       texlive-fntproof
Requires:       texlive-font-change
Requires:       texlive-fontch
Requires:       texlive-fontname
Requires:       texlive-gates
Requires:       texlive-getoptk
Requires:       texlive-gfnotation
Requires:       texlive-gobble
Requires:       texlive-graphics-pln
Requires:       texlive-gtl
Requires:       texlive-hlist
Requires:       texlive-hyplain
Requires:       texlive-ifis-macros
Requires:       texlive-inputnormalization
Requires:       texlive-insbox
Requires:       texlive-js-misc
Requires:       texlive-kastrup
Requires:       texlive-lambda-lists
Requires:       texlive-langcode
Requires:       texlive-lecturer
Requires:       texlive-letterspacing
Requires:       texlive-librarian
Requires:       texlive-listofitems
Requires:       texlive-localloc
Requires:       texlive-mathdots
Requires:       texlive-measurebox
Requires:       texlive-metatex
Requires:       texlive-midnight
Requires:       texlive-mkpattern
Requires:       texlive-mlawriter
Requires:       texlive-modulus
Requires:       texlive-multido
Requires:       texlive-namedef
Requires:       texlive-navigator
Requires:       texlive-newsletr
Requires:       texlive-nth
Requires:       texlive-ofs
Requires:       texlive-olsak-misc
Requires:       texlive-outerhbox
Requires:       texlive-path
Requires:       texlive-pdf-trans
Requires:       texlive-pdfmsym
Requires:       texlive-pdftoolbox
Requires:       texlive-pitex
Requires:       texlive-placeins-plain
Requires:       texlive-plain-widow
Requires:       texlive-plainpkg
Requires:       texlive-plipsum
Requires:       texlive-plnfss
Requires:       texlive-plstmary
Requires:       texlive-poormanlog
Requires:       texlive-present
Requires:       texlive-pwebmac
Requires:       texlive-random
Requires:       texlive-randomlist
Requires:       texlive-resumemac
Requires:       texlive-ruler
Requires:       texlive-schemata
Requires:       texlive-shade
Requires:       texlive-simplekv
Requires:       texlive-soul
Requires:       texlive-stretchy
Requires:       texlive-swrule
Requires:       texlive-systeme
Requires:       texlive-tabto-generic
Requires:       texlive-termmenu
Requires:       texlive-tex-ps
Requires:       texlive-tex4ht
Requires:       texlive-texapi
Requires:       texlive-texdate
Requires:       texlive-texdimens
Requires:       texinfo
Requires:       texlive-timetable
Requires:       texlive-tokmap
Requires:       texlive-tracklang
Requires:       texlive-transparent-io
Requires:       texlive-treetex
Requires:       texlive-trigonometry
Requires:       texlive-tuple
Requires:       texlive-ulem
Requires:       texlive-upca
Requires:       texlive-varisize
Requires:       texlive-visualtoks
Requires:       texlive-xii
Requires:       texlive-xii-lat
Requires:       texlive-xintsession
Requires:       texlive-xlop
Requires:       texlive-yax
Requires:       texlive-zztex

%description
Add-on packages and macros that work with plain TeX, often LaTeX, and
occasionally other formats.


%package -n texlive-abbr
Summary:        Simple macros supporting abbreviations for Plain and LaTeX
Version:        svn77161
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(abbr.tex) = %{tl_version}

%description -n texlive-abbr
The package provides some simple macros to support abbreviations in Plain TeX
or LaTeX. It allows writing (e.g.) \<TEX> instead of \TeX, hence frees users
from having to escape space after parameterless macros.

%package -n texlive-abstyles
Summary:        Adaptable BibTeX styles
Version:        svn76790
License:        Abstyles
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(apreambl.tex) = %{tl_version}

%description -n texlive-abstyles
A family of modifications of the standard BibTeX styles whose behaviour may be
changed by changing the user document, without change to the styles themselves.
The package is largely used nowadays in its adaptation for working with Babel.

%package -n texlive-advice
Summary:        Extend commands and environments
Version:        svn70688
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(collargs.sty)
Requires:       tex(xparse.sty)
Provides:       tex(advice-tikz.code.tex) = %{tl_version}
Provides:       tex(advice.sty) = %{tl_version}
Provides:       tex(advice.tex) = %{tl_version}
Provides:       tex(t-advice.tex) = %{tl_version}

%description -n texlive-advice
Like its namesake from the Emacs world, this cross-format package implements a
generic framework for extending the functionality of selected commands and
environments. It was developed as an auxiliary package of Memoize. This is why
it is, somewhat unconventionally, documented alongside that package. This
applies to both the manual and the documented code listing.

%package -n texlive-apnum
Summary:        Arbitrary precision numbers implemented by TeX macros
Version:        svn47510
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(apnum.tex) = %{tl_version}

%description -n texlive-apnum
The basic operations (addition, subtraction, multiplication, division, power to
an integer) are implemented by TeX macros in this package. Operands may be
numbers with arbitrary numbers of digits; scientific notation is allowed. The
expression scanner is also provided. As of version 1.4 (December 2015) the
calculation of common functions (sqrt, exp, ln, sin, cos, tan, asin, acos,
atan, pi) with arbitrary precision in the result has been added. Exhaustive
documentation (including detailed TeXnical documentation) is included. The
macro includes many optimizations and uses only TeX primitives (from classic
TeX) and \newcount macro.

%package -n texlive-autoaligne
Summary:        Align terms and members in math expressions
Version:        svn66655
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(autoaligne-fr.tex) = %{tl_version}
Provides:       tex(autoaligne.sty) = %{tl_version}
Provides:       tex(autoaligne.tex) = %{tl_version}

%description -n texlive-autoaligne
This package allows to align terms and members between lines containing math
expressions.

%package -n texlive-barr
Summary:        Diagram macros by Michael Barr
Version:        svn38479
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(diagxy.tex) = %{tl_version}

%description -n texlive-barr
Diagxy is a general diagramming package, useful for diagrams in a number of
mathematical disciplines. Diagxy is a development of an earlier (successful)
package to use the facilities of the xypic bundle.

%package -n texlive-bitelist
Summary:        Split list, in TeX's mouth
Version:        svn25779
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bitedemo.tex) = %{tl_version}
Provides:       tex(bitelist.sty) = %{tl_version}

%description -n texlive-bitelist
The package provides commands for "splitting" a token list at the first
occurrence of another (specified) token list. I.e., for given token lists s, t
return b and the shortest a, such that t = a s b. The package's mechanism
differs from those of packages providing similar features, in the following
ways: the method uses TeX's mechanism of reading delimited macro parameters;
splitting macros work by pure expansion, without assignments; the operation is
carried out in a single macro call. A variant of the operation is provided,
that retains outer braces.

%package -n texlive-borceux
Summary:        Diagram macros by Francois Borceux
Version:        svn21047
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-borceux
The macros support the construction of diagrams, such as those that appear in
category theory texts. The user gives the list of vertices and arrows to be
included, just as when composing a matrix, and the program takes care of
computing the dimensions of the arrows and realizing the pagesetting. All the
user has to do about the arrows is to specify their type (monomorphism, pair of
adjoint arrows, etc.) and their direction (north, south-east, etc.); 12 types
and 32 directions are available.

%package -n texlive-c-pascal
Summary:        Typeset Python, C and Pascal programs
Version:        svn18337
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cap.tex) = %{tl_version}
Provides:       tex(cap_c.tex) = %{tl_version}
Provides:       tex(cap_comm.tex) = %{tl_version}
Provides:       tex(cap_pas.tex) = %{tl_version}
Provides:       tex(cap_pyt.tex) = %{tl_version}

%description -n texlive-c-pascal
A TeX macro package for easy typesetting programs in Python, C and Pascal.
Program source files may also be input.

%package -n texlive-calcfrac
Summary:        Calculates the value of an expression containing fractions
Version:        svn68684
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(calcfrac.sty) = %{tl_version}
Provides:       tex(calcfrac.tex) = %{tl_version}

%description -n texlive-calcfrac
This package is an engine for calculating numerical expressions containing
fractions. The numerical value of the expression is calculated with a
non-expandable method and displayed in the form of an irreducible fraction or,
where appropriate, an integer. This package is intended for educational
purposes. The videos showing its writing from scratch are available on youtube
from episode 24: https://youtu.be/6lF4P6B3msw. This is why it is delivered with
only a minimalist documentation.

%package -n texlive-catcodes
Summary:        Generic handling of TeX category codes
Version:        svn38859
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(actcodes.sty) = %{tl_version}
Provides:       tex(catchdq.sty) = %{tl_version}
Provides:       tex(stacklet.sty) = %{tl_version}

%description -n texlive-catcodes
The bundle deals with category code switching; the packages of the bundle
should work with any TeX format (with the support of the plainpkg package). The
bundle provides: stacklet.sty, which supports stacks that control the use of
different catcodes; actcodes.sty, which deals with active characters; and
catchdq.sty, which provides a simple quotation character control mechanism.

%package -n texlive-chronosys
Summary:        Drawing time-line diagrams
Version:        svn26700
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(chronosys.sty) = %{tl_version}
Provides:       tex(chronosys.tex) = %{tl_version}
Provides:       tex(chronosyschr.tex) = %{tl_version}
Provides:       tex(x-chronosys.tex) = %{tl_version}

%description -n texlive-chronosys
Macros to produce time line diagrams. Interfaces for Plain TeX, ConTeXt and
LaTeX are provided.

%package -n texlive-collargs
Summary:        Collect arguments of any command
Version:        svn70689
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Provides:       tex(collargs.sty) = %{tl_version}
Provides:       tex(collargs.tex) = %{tl_version}
Provides:       tex(t-collargs.tex) = %{tl_version}

%description -n texlive-collargs
This is a cross-format package providing a command which can determine the
argument scope of any command whose argument structure conforms to xparse's
argument specification. It was implemented as an auxiliary package of Advice
... which in turn was implemented as an auxiliary package of Memoize. This is
why it is, somewhat unconventionally, documented alongside that package. This
applies to both the manual and the documented code listing.

%package -n texlive-colorsep
Summary:        Color separation
Version:        svn13293
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-colorsep
Support for colour separation when using dvips.

%package -n texlive-compare
Summary:        Compare two strings
Version:        svn54265
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(compare.tex) = %{tl_version}

%description -n texlive-compare
The file defines a macro \compare, which takes two arguments; the macro expands
to -1, 0, 1, according as the first argument is less than, equal to, or greater
than the second argument. Sorting is alphabetic, using ASCII collating order.

%package -n texlive-crossrefenum
Summary:        Smart typesetting of enumerated cross-references for various TeX formats
Version:        svn76004
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(crossrefenum.sty) = %{tl_version}
Provides:       tex(crossrefenum.tex) = %{tl_version}
Provides:       tex(t-crossrefenum.tex) = %{tl_version}

%description -n texlive-crossrefenum
This package lets TeX manage the formatting of bunches of cross-references for
you. It features: Automatic collapsing of references, Support for references by
various criteria, including page and note number, line number in ConTeXt and
edpage and edline when used in conjunction with reledmac, Handling of
references combining two criteria (e.g. by page and note number), Extension
mechanisms to add support to other types of references without modifying the
internal macros. Note that sorting is not supported. I assume that users know
in what order the labels they refer to appear in their document. It is written
in Plain TeX as much as possible in order to make it compatible with a wide
array of formats. For the moment, it works out of the box with ConTeXt and
LaTeX.

%package -n texlive-cweb-old
Summary:        Obsolete cweb files
Version:        svn49271
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pdfXcwebmac.tex) = %{tl_version}
Provides:       tex(pdfcwebmac.tex) = %{tl_version}
Provides:       tex(pdfdcwebmac.tex) = %{tl_version}
Provides:       tex(pdffcwebmac.tex) = %{tl_version}
Provides:       tex(pdficwebmac.tex) = %{tl_version}
Provides:       tex(pdfwebmac.tex) = %{tl_version}

%description -n texlive-cweb-old
A collection of obsolete cweb files, included in case they are somehow useful
to someone.

%package -n texlive-dinat
Summary:        Bibliography style for German texts
Version:        svn76790
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dinat
Bibliography style files intended for texts in german. They draw up
bibliographies in accordance with the german DIN 1505, parts 2 and 3.

%package -n texlive-dirtree
Summary:        Display trees in the style of windows explorer
Version:        svn42428
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dirtree.sty) = %{tl_version}
Provides:       tex(dirtree.tex) = %{tl_version}

%description -n texlive-dirtree
This package is designed to emulate the way windows explorer displays directory
and file trees, with the root at top left, and each level of subtree displaying
one step in to the right. The macros work equally well with Plain TeX and with
LaTeX.

%package -n texlive-docbytex
Summary:        Creating documentation from source code
Version:        svn34294
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(docby.tex) = %{tl_version}

%description -n texlive-docbytex
The package creates documentation from C source code, or other programming
languages.

%package -n texlive-dowith
Summary:        Apply a command to a list of items
Version:        svn38860
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(domore.sty) = %{tl_version}
Provides:       tex(dowith.sty) = %{tl_version}

%description -n texlive-dowith
The package provides macros for applying a command to all elements of a list
without separators, such as '\DoWithAllIn{<cmd>}{<list-macro>}', and also for
extending and reducing macros storing such lists. Applications in mind belonged
to LaTeX, but the package should work with other formats as well. Loop and list
macros in other packages are discussed. A further package, domore, is also
provided, which enhances the functionality of dowith.

%package -n texlive-eijkhout
Summary:        Victor Eijkhout's packages
Version:        svn15878
License:        GPL-2.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(CD_labeler.tex) = %{tl_version}
Provides:       tex(CD_labeler_test.tex) = %{tl_version}
Provides:       tex(DB_process.tex) = %{tl_version}
Provides:       tex(repeat.tex) = %{tl_version}

%description -n texlive-eijkhout
Three unrelated packages: DB_process, to parse and process database output;
CD_labeler, to typeset user text to fit on a CD label; and repeat, a nestable,
generic loop macro.

%package -n texlive-encxvlna
Summary:        Insert nonbreakable spaces, using encTeX
Version:        svn34087
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(encxvlna.sty) = %{tl_version}
Provides:       tex(encxvlna.tex) = %{tl_version}

%description -n texlive-encxvlna
The package provides tools for inserting nonbreakable spaces after nonsyllabic
prepositions and single letter conjunctions as required by Czech and Slovak
typographical rules. It is implemented using encTeX and provides files both for
plain TeX and LaTeX. The LaTeX solution tries to avoid conflicts with other
packages.

%package -n texlive-eoldef
Summary:        Define commands which absorb the whole source line as arguments
Version:        svn76050
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eoldef.sty) = %{tl_version}
Provides:       tex(eoldef.tex) = %{tl_version}

%description -n texlive-eoldef
This macro allows you to define commands that take the entire source line as
arguments. Usage: \eoldef <control sequence> <parameter text> { <replacement
text>} defines a control sequence that is delimited by the end-of-line in
addition to the specified parameter text. For instance, \eoldef\test#1:#2{} and
\test abc:def will give #1 = abc, #2 = def. \eolgdef is the \global variant to
\eoldef. Like \verb|...|, \eoldef'd commands may generally not be used as part
of another command's argument as it changes catcodes. However, if you must use
it in environments where catcodes are frozen, you may follow the command with a
braced argument, eg. \test{#1:#2} using the previous example. This package may
be used in plain TeX or LaTeX by \input{eoldef}.

%package -n texlive-epigram
Summary:        Display short quotations
Version:        svn20513
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(epigram.tex) = %{tl_version}

%description -n texlive-epigram
The package determines (on the basis of the width of the text of the epigram,
laid out on a single line) whether to produce a line or a displayed paragraph.

%package -n texlive-epsf
Summary:        Simple macros for EPS inclusion
Version:        svn21461
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(epsf.sty) = %{tl_version}
Provides:       tex(epsf.tex) = %{tl_version}

%description -n texlive-epsf
The original (and now obsolescent) graphics inclusion macros for use with
dvips, still widely used by Plain TeX users (in particular). For LaTeX users,
the package is nowadays (rather strongly) deprecated in favour of the more
sophisticated standard LaTeX latex-graphics bundle of packages. (The
latex-graphics bundle is also available to Plain TeX users, via its Plain TeX
version.)

%package -n texlive-epsf-dvipdfmx
Summary:        Plain TeX file for using epsf.tex with (x)dvipdfmx
Version:        svn35575
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(epsf-dvipdfmx.tex) = %{tl_version}

%description -n texlive-epsf-dvipdfmx
epsf-dvipdfmx.tex is a plain TeX file to be \input after epsf.tex when using
plain TeX with dvipdfmx. As in: \input epsf \input epsf-dvipdfmx It is needed
when an .eps file has anything except the origin (0,0) for the lower-left of
its bounding box.

%package -n texlive-etoolbox-generic
Summary:        A loader for etoolbox.sty in non-LaTeX formats
Version:        svn68513
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(etoolbox-generic.tex) = %{tl_version}

%description -n texlive-etoolbox-generic
This package implements a wrapper which allows the user to load the
LaTeX-independent part of LaTeX package etoolbox in other formats. It was
implemented as an auxiliary package of Memoize.

%package -n texlive-expex-acro
Summary:        Wrapper for the expex package
Version:        svn68046
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(acro.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expex.sty)
Requires:       tex(xspace.sty)
Provides:       tex(expex-acro.sty) = %{tl_version}

%description -n texlive-expex-acro
This is a small wrapper for the expex package, adding ways to define, use, and
summarize glossing abbreviations. It also provides commands to refer to
examples, as well as some inline formatting commands commonly used in
linguistics.

%package -n texlive-expkv-bundle
Summary:        An expandable key=val implementation and friends
Version:        svn73212
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(expkv-cs.sty) = %{tl_version}
Provides:       tex(expkv-cs.tex) = %{tl_version}
Provides:       tex(expkv-def.sty) = %{tl_version}
Provides:       tex(expkv-def.tex) = %{tl_version}
Provides:       tex(expkv-opt-2020-10-10.sty) = %{tl_version}
Provides:       tex(expkv-opt.sty) = %{tl_version}
Provides:       tex(expkv-pop.sty) = %{tl_version}
Provides:       tex(expkv-pop.tex) = %{tl_version}
Provides:       tex(expkv.sty) = %{tl_version}
Provides:       tex(expkv.tex) = %{tl_version}
Provides:       tex(t-expkv-cs.tex) = %{tl_version}
Provides:       tex(t-expkv-def.tex) = %{tl_version}
Provides:       tex(t-expkv-pop.tex) = %{tl_version}
Provides:       tex(t-expkv.tex) = %{tl_version}

%description -n texlive-expkv-bundle
This is a collection of different packages that provide key=value functionality
in plainTeX, LaTeX, and ConTeXt. At the core, the expkv package implements two
expandable key=value parsers that are somewhat fast and robust against common
bugs in many key=value implementations (no accidental brace stripping, no
fragility for active commas or equals signs). expkv-cs enables users to define
expandable key=value macros in a comfortable and straightforward way. expkv-def
provides an interface to define common key types for expkv similar to the key
defining interfaces of widespread key=value implementations. expkv-opt allows
to parse package or class options in LaTeX via expkv. expkv-pop is a utility
package to define prefix oriented parsers that allow a somewhat natural
formulation (it provides the core functionality for the key-defining front ends
of both expkv-cs and expkv-def).

%package -n texlive-fenixpar
Summary:        One-shot changes to token registers such as \everypar
Version:        svn24730
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fenixpar.sty) = %{tl_version}
Provides:       tex(fenixtok.sty) = %{tl_version}

%description -n texlive-fenixpar
The bundle provides two packages, fenxitok and fenixpar. The fenixtok package
provides user macros to add material to a token register; the material will be
(automatically) removed from the token register when the register is executed.
Material may be added either to the left or to the right, and care is taken not
to override any redefinition that may be included in the token register itself.
The fenixpar package uses the macros of fenixtok to provide a user interface to
manipulation of the \everypar token register. The packages require the e-TeX
extensions; with them, they work either with Plain TeX or with LaTeX.

%package -n texlive-figflow
Summary:        Flow text around a figure
Version:        svn21462
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(figflow.tex) = %{tl_version}

%description -n texlive-figflow
Provides a Plain TeX macro \figflow that allows one to insert a figure into an
area inset into a paragraph. Command arguments are width and height of the
figure, and the figure (and its caption) itself. Usage details are to be found
in the TeX file itself. The package does not work with LaTeX; packages such as
wrapfig, floatflt and picins support the needs of LaTeX users in this area.

%package -n texlive-fixpdfmag
Summary:        Fix magnification in pdfTeX
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fixpdfmag.tex) = %{tl_version}

%description -n texlive-fixpdfmag
A recent change to pdfTeX has caused magnification to apply to page dimensions.
This small package changes the values set in the page dimension variables from
pt to truept, thus evading the effects of \mag.

%package -n texlive-fltpoint
Summary:        Simple floating point arithmetic
Version:        svn56594
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(deccomma.sty) = %{tl_version}
Provides:       tex(fltpoint.sty) = %{tl_version}
Provides:       tex(fltpoint.tex) = %{tl_version}

%description -n texlive-fltpoint
The package provides simple floating point operations (addition, subtraction,
multiplication, division and rounding). Used, for example, by rccol.

%package -n texlive-fntproof
Summary:        A programmable font test pattern generator
Version:        svn20638
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fntproof.tex) = %{tl_version}

%description -n texlive-fntproof
The package implements all the font testing commands of Knuth's testfont.tex,
but arranges that information necessary for each command is supplied as
arguments to that command, rather than prompted for. This makes it possible to
type all the tests in one command line, and easy to input the package in a file
and to use the commands there. A few additional commands supporting this last
purpose are also made available.

%package -n texlive-font-change
Summary:        Macros to change text and mathematics fonts in plain TeX
Version:        svn40403
License:        CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(default-amssymbols.tex) = %{tl_version}
Provides:       tex(font_antp_euler.tex) = %{tl_version}
Provides:       tex(font_antt-condensed-light.tex) = %{tl_version}
Provides:       tex(font_antt-condensed-medium.tex) = %{tl_version}
Provides:       tex(font_antt-condensed.tex) = %{tl_version}
Provides:       tex(font_antt-light.tex) = %{tl_version}
Provides:       tex(font_antt-medium.tex) = %{tl_version}
Provides:       tex(font_antt.tex) = %{tl_version}
Provides:       tex(font_arev.tex) = %{tl_version}
Provides:       tex(font_artemisia_euler.tex) = %{tl_version}
Provides:       tex(font_bera_concrete.tex) = %{tl_version}
Provides:       tex(font_bera_euler.tex) = %{tl_version}
Provides:       tex(font_bera_fnc.tex) = %{tl_version}
Provides:       tex(font_bookman.tex) = %{tl_version}
Provides:       tex(font_century.tex) = %{tl_version}
Provides:       tex(font_charter.tex) = %{tl_version}
Provides:       tex(font_cm.tex) = %{tl_version}
Provides:       tex(font_cmbright.tex) = %{tl_version}
Provides:       tex(font_concrete.tex) = %{tl_version}
Provides:       tex(font_epigrafica_euler.tex) = %{tl_version}
Provides:       tex(font_epigrafica_palatino.tex) = %{tl_version}
Provides:       tex(font_iwona-bold.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed-bold.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed-light.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed-medium.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed.tex) = %{tl_version}
Provides:       tex(font_iwona-light.tex) = %{tl_version}
Provides:       tex(font_iwona-medium.tex) = %{tl_version}
Provides:       tex(font_iwona.tex) = %{tl_version}
Provides:       tex(font_kp-light.tex) = %{tl_version}
Provides:       tex(font_kp.tex) = %{tl_version}
Provides:       tex(font_kurier-bold.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed-bold.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed-light.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed-medium.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed.tex) = %{tl_version}
Provides:       tex(font_kurier-light.tex) = %{tl_version}
Provides:       tex(font_kurier-medium.tex) = %{tl_version}
Provides:       tex(font_kurier.tex) = %{tl_version}
Provides:       tex(font_libertine_kp.tex) = %{tl_version}
Provides:       tex(font_libertine_palatino.tex) = %{tl_version}
Provides:       tex(font_libertine_times.tex) = %{tl_version}
Provides:       tex(font_mdutopia.tex) = %{tl_version}
Provides:       tex(font_pagella.tex) = %{tl_version}
Provides:       tex(font_palatino.tex) = %{tl_version}
Provides:       tex(font_times.tex) = %{tl_version}
Provides:       tex(font_utopia.tex) = %{tl_version}

%description -n texlive-font-change
Macros to Change Text and Mathematics fonts in TeX: 45 Beautiful Variants The
macros are written for plain TeX and may be used with other packages like
AmSTeX, eplain, etc. They also work with XeTeX. The macros allow users to
change the fonts (for both text and mathematics) in their TeX document with
only one statement. The fonts may be used readily at various predefined sizes.
All the fonts called by these macro files are free and are included in current
MiKTeX and TeX Live distributions.

%package -n texlive-fontch
Summary:        Changing fonts, sizes and encodings in Plain TeX
Version:        svn17859
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(DSmac.tex) = %{tl_version}
Provides:       tex(TS1mac.tex) = %{tl_version}
Provides:       tex(bsymbols.tex) = %{tl_version}
Provides:       tex(fontch.tex) = %{tl_version}
Provides:       tex(fontch_doc.tex) = %{tl_version}

%description -n texlive-fontch
The fontch macros allow the user to change font size and family anywhere in a
plain TeX document. Sizes of 8, 10, 12, 14, 20 and 24 points are available. A
sans serif family (\sf) is defined in addition to the families already defined
in plain TeX. Optional support for Latin Modern T1 and TS1 fonts is given.
There are macros for non-latin1 letters and for most TS1 symbols. Math mode
always uses CM fonts. A command for producing doubled-spaced documents is also
provided. The present version of the package is designed to deal with the
latest release of the Latin Modern fonts version 1.106. Unfortunately, it can
no longer support earlier versions of the fonts, so an obsolete version of the
package is retained for users who don't yet have access to the latest version
of the fonts.

%package -n texlive-fontname
Summary:        Scheme for naming fonts in TeX
Version:        svn75544
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fontname
The scheme for assigning names is described (in the documentation part of the
package), and map files giving the relation between foundry name and 'TeX-name'
are also provided.

%package -n texlive-gates
Summary:        Support for writing modular and customisable code
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gates.sty) = %{tl_version}
Provides:       tex(gates.tex) = %{tl_version}
Provides:       tex(t-gates.tex) = %{tl_version}

%description -n texlive-gates
The package provides the means of writing code in a modular fashion: big macros
or functions are divided into small chunks (called gates) with names, which can
be externally controlled (e.g. they can be disabled, subjected to conditionals,
loops...) and/or augmented with new chunks. Thus complex code may easily be
customised without having to rewrite it, or even understand its implementation:
the behavior of existing gates can be modified, and new ones can be added,
without endangering the whole design. This allows code to be hacked in ways the
original authors might have never envisioned. The gates package is implemented
independently for both TeX and Lua. The TeX implementation, running in any
current environment, requires the texapi package, whereas the Lua version can
be run with any Lua interpreter, not just LuaTeX.

%package -n texlive-getoptk
Summary:        Define macros with sophisticated options
Version:        svn23567
License:        CeCILL-B
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(getoptk.tex) = %{tl_version}
Provides:       tex(guide.tex) = %{tl_version}

%description -n texlive-getoptk
The package provides a means of defining macros whose options are taken from a
dictionary, which includes options which themselves have arguments. The package
was designed for use with Plain TeX; its syntax derives from that of the \hbox,
\hrule, etc., TeX primitives.

%package -n texlive-gfnotation
Summary:        Typeset Gottlob Frege's notation in plain TeX
Version:        svn37156
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(GFnotation.tex) = %{tl_version}

%description -n texlive-gfnotation
The package implements macros for plain TeX to typeset the notation invented by
Gottlob Frege in 1879 for his books "Begriffsschrift" and "Grundgesetze der
Arithmetik" (two volumes). The output styles of both books are supported.

%package -n texlive-gobble
Summary:        More gobble macros for PlainTeX and LaTeX
Version:        svn64967
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gobble-user.sty) = %{tl_version}
Provides:       tex(gobble-user.tex) = %{tl_version}
Provides:       tex(gobble.sty) = %{tl_version}
Provides:       tex(gobble.tex) = %{tl_version}

%description -n texlive-gobble
The LaTeX package gobble includes several gobble macros not included in the
LaTeX kernel. These macros remove a number of arguments after them, a feature
regulary used inside other macros. This includes gobble macros for optional
arguments. The LaTeX package gobble-user provides these macros at the user
level, i.e. using names without @ so that these can be used without
\makeatletter and \makeatother. The same macros are provided inside .tex files
for use with plain-TeX or other TeX formats. However, the gobble macros for
optional macros require \@ifnextchar to be defined.

%package -n texlive-graphics-pln
Summary:        LaTeX-style graphics for Plain TeX users
Version:        svn71575
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(autopict.sty) = %{tl_version}
Provides:       tex(color.tex) = %{tl_version}
Provides:       tex(graphicx.tex) = %{tl_version}
Provides:       tex(miniltx.tex) = %{tl_version}
Provides:       tex(picture.tex) = %{tl_version}
Provides:       tex(psfrag.tex) = %{tl_version}

%description -n texlive-graphics-pln
The Plain TeX graphics package is mostly a thin shell around the LaTeX graphicx
and color packages, with support of the LaTeX-isms in those packages provided
by miniltx (which is the largest part of the bundle). The bundle also contains
a file "picture.tex", which is a wrapper around the autopict.sty, and provides
the LaTeX picture mode to Plain TeX users.

%package -n texlive-gtl
Summary:        Manipulating generalized token lists
Version:        svn69297
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gtl.sty) = %{tl_version}

%description -n texlive-gtl
The package provides tools for simple operations on lists of tokens which are
not necessarily balanced. It is in particular used a lot in the unravel
package, to go through tokens one at a time rather than having to work with
entire braced groups at a time.

%package -n texlive-hlist
Summary:        Horizontal and columned lists
Version:        svn44983
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hlist.sty) = %{tl_version}
Provides:       tex(hlist.tex) = %{tl_version}

%description -n texlive-hlist
This plain TeX and LaTeX package provides the "hlist" environment in which
\hitem starts a horizontal and columned item. It depends upon the simplekv
package.

%package -n texlive-hyplain
Summary:        Basic support for multiple languages in Plain TeX
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hylang.tex) = %{tl_version}
Provides:       tex(hyplain.tex) = %{tl_version}
Provides:       tex(hyrules.tex) = %{tl_version}

%description -n texlive-hyplain
The package offers a means to set up hyphenation suitable for several languages
and/or dialects, and to select them or switch between them while typesetting.

%package -n texlive-ifis-macros
Summary:        Check if a given input string is a number or dimension for TeX
Version:        svn75195
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ifisdimension.tex) = %{tl_version}
Provides:       tex(ifisglue.tex) = %{tl_version}
Provides:       tex(ifisinteger.tex) = %{tl_version}

%description -n texlive-ifis-macros
This package provides three macros: \ifisint, \ifisdim, and \ifisglue. They
test if a given input string represents either a valid integer or a valid
dimension or a valid (mu)glue specification for TeX.

%package -n texlive-inputnormalization
Summary:        Wrapper for XeTeX's and LuaTeX's input normalization
Version:        svn59850
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(inputnormalization.sty) = %{tl_version}

%description -n texlive-inputnormalization
This package provides a cross engine interface to normalizing input before it's
read by TeX. It is based on XeTeX's \XeTeXinputnormalization primitive and
lua-uni-algos for LuaTeX.

%package -n texlive-insbox
Summary:        Insert pictures/boxes into paragraphs
Version:        svn34299
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(insbox.tex) = %{tl_version}

%description -n texlive-insbox
The package provides convenient bundling of the \parshape primitive. LaTeX
users should note that this is a generic package, and should be loaded using
\input .

%package -n texlive-js-misc
Summary:        Miscellaneous macros from Joachim Schrod
Version:        svn16211
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cassette.tex) = %{tl_version}
Provides:       tex(idverb.tex) = %{tl_version}
Provides:       tex(js-misc.tex) = %{tl_version}
Provides:       tex(schild.tex) = %{tl_version}
Provides:       tex(sperr.tex) = %{tl_version}
Provides:       tex(xfig.tex) = %{tl_version}

%description -n texlive-js-misc
A bunch of packages, including: idverb.tex, for 'short verbatim'; xfig.tex, for
including xfig/transfig output in a TeX document; and cassette.tex for setting
cassette labels.

%package -n texlive-kastrup
Summary:        Convert numbers into binary, octal and hexadecimal
Version:        svn15878
License:        Kastrup
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(binhex.tex) = %{tl_version}

%description -n texlive-kastrup
Provides expandable macros for both fixed-width and minimum-width numbers to
bases 2, 4, 8 and 16.

%package -n texlive-lambda-lists
Summary:        Lists in TeX's mouth
Version:        svn31402
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lambda.sty) = %{tl_version}

%description -n texlive-lambda-lists
These list-processing macros avoid the reassignments employed in the macros
shown in Appendix D of the TeXbook: all the manipulations take place in what
Knuth is pleased to call "TeX's mouth".

%package -n texlive-langcode
Summary:        Simple language-dependent settings based on language codes
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(dhua.sty)
Requires:       tex(dowith.sty)
Provides:       tex(langcode.sty) = %{tl_version}

%description -n texlive-langcode
The package provides a command \uselangcode{<code>} to adjust
language-dependent settings such as key words, typographical conventions and
language codes (ISO 639-1). The package provides a means of selecting macros
according to the specified code, for preparing a document that is to be
separately typeset in different languages. The package is dependent on the
plainpkg package, and is already in use in the morehype and catcodes packages.

%package -n texlive-lecturer
Summary:        On-screen presentations for (almost) all formats
Version:        svn23916
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lecturer.sty) = %{tl_version}
Provides:       tex(lecturer.tex) = %{tl_version}
Provides:       tex(ltr-areas.tex) = %{tl_version}
Provides:       tex(ltr-graphics.tex) = %{tl_version}
Provides:       tex(ltr-job.tex) = %{tl_version}
Provides:       tex(ltr-navigation.tex) = %{tl_version}
Provides:       tex(ltr-slides.tex) = %{tl_version}
Provides:       tex(ltr-steps.tex) = %{tl_version}
Provides:       tex(t-lecturer.tex) = %{tl_version}

%description -n texlive-lecturer
The package creates slides for on-screen presentations based on PDF features
without manipulating TeX's typesetting process. The presentation flow relies on
PDF's abilities to display content step by step. Features include: Free
positioning of anything anywhere in painted areas on the slide, as well as in
the main textblock; Numerous attributes to control the layout and the
presentation flow, from TeX's primitive dimensions to the visibility of steps;
Feature inheritance from global to local settings, with intermediate types;
Basic drawing facilities to produce symbols, e.g., for list items or buttons;
Colours, transparency, shades, and pictures; Navigation with links, pop-up
menus, and customizable bookmarks; Easy switch between presentation and
handout; and PDF transitions. Besides the traditional documentation, the
distribution includes visual documentation and six demo presentations ranging
from geometric abstraction to classic style to silly video game. Lecturer is
designed to work with all formats, but presently fails with ConTeXt MkIV
(because of clashes in management of PDF objects, probably), works only with
pdfTeX and LuaTeX for the time being, and requires texapi and yax, both v.1.02.

%package -n texlive-letterspacing
Summary:        Letter spacing
Version:        svn54266
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(letterspacing.tex) = %{tl_version}

%description -n texlive-letterspacing
Space out the letters of text; the command is \letterspace<\hbox
modifier>{<text>}: the text is placed in an \hbox of the specified size, and
space is inserted between each glyph to make the text fit the box. Note that
letterspacing is not ordinarily considered acceptable in modern typesetting of
English.

%package -n texlive-librarian
Summary:        Tools to create bibliographies in TeX
Version:        svn19880
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(librarian.sty) = %{tl_version}
Provides:       tex(librarian.tex) = %{tl_version}
Provides:       tex(t-librarian.tex) = %{tl_version}

%description -n texlive-librarian
The package extracts information in bib files, makes it available in the
current document, and sorts lists of entries according to that information and
the user's specifications. Citation and bibliography styles can then be written
directly in TeX, without any use of BibTeX. Creating references thus depends
entirely on the user's skill in TeX. The package works with all formats that
use plain TeX's basic syntactic sugar; the distribution includes a third-party
file for ConTeXt and a style file for LaTeX. As an example of use, an Author
(Year) style is given in a separate file and explained in the documentation.

%package -n texlive-listofitems
Summary:        Grab items in lists using user-specified sep char
Version:        svn70579
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(listofitems.sty) = %{tl_version}
Provides:       tex(listofitems.tex) = %{tl_version}

%description -n texlive-listofitems
This simple package is designed to read a list of items whose parsing character
may be selected by the user. Once the list is read, its items are stored in a
structure that behaves as a dimensioned array. As such, it becomes very easy to
access an item in the list by its number. For example, if the list is stored in
the macro \foo, the item #3 is designated by \foo[3]. A component may, in turn,
be a list with a parsing delimiter different from the parent list, paving the
way for nesting and employing a syntax reminiscent of an array of several
dimensions of the type \foo[3,2] to access the item #2 of the list contained
within the item #3 of the top-tier list.

%package -n texlive-localloc
Summary:        Macros for localizing TeX register allocations
Version:        svn56496
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(localloc.sty) = %{tl_version}

%description -n texlive-localloc
This package approaches the problem of the shortage of registers, by providing
a mechanism for local allocation. The package works with Plain TeX, LaTeX, and
LaTeX 2.09.

%package -n texlive-mathdots
Summary:        Commands to produce dots in math that respect font size
Version:        svn34301
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mathdots.sty) = %{tl_version}
Provides:       tex(mathdots.tex) = %{tl_version}

%description -n texlive-mathdots
Redefines \ddots and \vdots, and defines \iddots. The dots produced by \iddots
slant in the opposite direction to \ddots. All the commands are designed to
change size appropriately in scripts, as well as in response to LaTeX size
changing commands. The commands may also be used in plain TeX.

%package -n texlive-measurebox
Summary:        Precise measurements of glyphs
Version:        svn75139
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(measurebox.tex) = %{tl_version}

%description -n texlive-measurebox
MeasureBox is a (plain TeX) package for measuring material. It is intended for
precise measurements of glyphs so that they can be manipulated by other macros
and packages (e.g. the Stretchy package). Its only dependency is the pdfToolbox
package, which is currently only supported by plain-pdfTeX.

%package -n texlive-metatex
Summary:        Incorporate Metafont pictures in TeX source
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(metatex.tex) = %{tl_version}

%description -n texlive-metatex
METATeX is a set of plain TeX and Metafont macros that you can use to define
both the text and the figures in a single source file. Because METATeX sets up
two way communication, from TeX to Metafont and back from Metafont to TeX,
drawing dimensions can be controlled by TeX and labels can be located by
Metafont. Only standard features of TeX and Metafont are used, but two runs of
TeX and one of Metafont are needed.

%package -n texlive-midnight
Summary:        A set of useful macro tools
Version:        svn15878
License:        LicenseRef-midnight
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(border.tex) = %{tl_version}
Provides:       tex(dolines.tex) = %{tl_version}
Provides:       tex(gloss.tex) = %{tl_version}
Provides:       tex(labels.tex) = %{tl_version}
Provides:       tex(loop.tex) = %{tl_version}
Provides:       tex(quire.tex) = %{tl_version}
Provides:       tex(styledef.tex) = %{tl_version}

%description -n texlive-midnight
Included are: quire: making booklets, etc.; gloss: vertically align words in
consecutive sentences; loop: a looping construct; dolines: 'meta'-macros to
separate arguments by newlines; labels: address labels and bulk mail letters;
styledef: selectively input part of a file; and border: borders around boxes.

%package -n texlive-mkpattern
Summary:        A utility for making hyphenation patterns
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mkpatter.tex) = %{tl_version}

%description -n texlive-mkpattern
Mkpattern is a general purpose program for the generation of hyphenation
patterns, with definition of letter sets and template-like constructions. It
also provides an easy way to handle different input and output encodings, and
features generation of clean UTF-8 patterns. The package was used for the
creation of the Galician patterns.

%package -n texlive-mlawriter
Summary:        Write MLA style documents in Plain TeX
Version:        svn67558
License:        CC0-1.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mlawriter.tex) = %{tl_version}

%description -n texlive-mlawriter
With this Plain TeX extension, papers can be written in MLA style. These appear
as if they were written in MS Word.

%package -n texlive-modulus
Summary:        A non-destructive modulus and integer quotient operator for TeX
Version:        svn47599
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(modulus.sty) = %{tl_version}

%description -n texlive-modulus
The package provides an easy way to take the remainder of a division operation
without destroying the values of the counters containing the dividend and
divisor. Also provides a way to take the integer quotient of a division
operation without destroying the values of the counters containing the dividend
and divisor. A tiny but occasionally useful package, when doing heavy TeX
programming.

%package -n texlive-multido
Summary:        A loop facility for Generic TeX
Version:        svn18302
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(multido.sty) = %{tl_version}
Provides:       tex(multido.tex) = %{tl_version}

%description -n texlive-multido
The package provides the \multido command, which was originally designed for
use with PSTricks. Fixed-point arithmetic is used when working on the loop
variable, so that the package is equally applicable in graphics applications
like PSTricks as it is with the more common integer loops.

%package -n texlive-namedef
Summary:        TeX definitions with named parameters
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-l3kernel
Provides:       tex(namedef.sty) = %{tl_version}

%description -n texlive-namedef
This package provides a prefix \named to be used in TeX definitions so that
parameters can be identified by their name rather than by number, giving
parameters a semantic rather than syntactic meaning, making it easy to
understand long definitions. A usual definition reads: \def\SayHello#1{Hello,
#1!} but with namedef you can replace #1 by, say, #[person]:
\named\def\SayHello#[person]{Hello, #[person]!} and \named will figure out the
numbering of the parameters for you.

%package -n texlive-navigator
Summary:        PDF features across formats and engines
Version:        svn41413
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(navigator.sty) = %{tl_version}
Provides:       tex(navigator.tex) = %{tl_version}
Provides:       tex(t-navigator.tex) = %{tl_version}

%description -n texlive-navigator
Navigator implements PDF features for all formats (with some limitations in
ConTeXt) with pdfTeX, LuaTeX and XeTeX (i.e. xdvipdfmx). Features include:
Customizable outlines (i.e. bookmarks); Anchors; Links and actions (e.g.
JavaScript or user-defined PDF actions); File embedding (not in ConTeXt);
Document information and PDF viewer's display (not in ConTeXt); and Commands to
create and use raw PDF objects. Navigator requires texapi and yax, both version
at least 1.03.

%package -n texlive-newsletr
Summary:        Macros for making newsletters with Plain TeX
Version:        svn15878
License:        Newsletr
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(newsletr.tex) = %{tl_version}

%description -n texlive-newsletr
Macros for making newsletters with Plain TeX

%package -n texlive-nth
Summary:        Generate English ordinal numbers
Version:        svn54252
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(nth.sty) = %{tl_version}

%description -n texlive-nth
The command \nth{<number>} generates English ordinal numbers of the form 1st,
2nd, 3rd, 4th, etc. LaTeX package options may specify that the ordinal mark be
superscripted, and that negative numbers may be treated; Plain TeX users have
no access to package options, so need to redefine macros for these changes.

%package -n texlive-ofs
Summary:        Macros for managing large font collections
Version:        svn16991
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(a117.tex) = %{tl_version}
Provides:       tex(a35.sty) = %{tl_version}
Provides:       tex(a35.tex) = %{tl_version}
Provides:       tex(allfonts.sty) = %{tl_version}
Provides:       tex(allfonts.tex) = %{tl_version}
Provides:       tex(amsfn.tex) = %{tl_version}
Provides:       tex(mtfn.tex) = %{tl_version}
Provides:       tex(ofs-6a.tex) = %{tl_version}
Provides:       tex(ofs-6c.tex) = %{tl_version}
Provides:       tex(ofs-6k.tex) = %{tl_version}
Provides:       tex(ofs-6s.tex) = %{tl_version}
Provides:       tex(ofs-6t.tex) = %{tl_version}
Provides:       tex(ofs-6x.tex) = %{tl_version}
Provides:       tex(ofs-6y.tex) = %{tl_version}
Provides:       tex(ofs-8c.tex) = %{tl_version}
Provides:       tex(ofs-8t.tex) = %{tl_version}
Provides:       tex(ofs-8x.tex) = %{tl_version}
Provides:       tex(ofs-8z.tex) = %{tl_version}
Provides:       tex(ofs-ams.tex) = %{tl_version}
Provides:       tex(ofs-cm.tex) = %{tl_version}
Provides:       tex(ofs-mt.tex) = %{tl_version}
Provides:       tex(ofs-ps.tex) = %{tl_version}
Provides:       tex(ofs-px.tex) = %{tl_version}
Provides:       tex(ofs-slt.tex) = %{tl_version}
Provides:       tex(ofs-tx.tex) = %{tl_version}
Provides:       tex(ofs.sty) = %{tl_version}
Provides:       tex(ofs.tex) = %{tl_version}
Provides:       tex(ofsdef.tex) = %{tl_version}
Provides:       tex(pantyk.tex) = %{tl_version}
Provides:       tex(txfn.tex) = %{tl_version}

%description -n texlive-ofs
OFS (Olsak's Font System) is a set of Plain TeX and LaTeX macros for managing
large font collections; it has been used by Czech/Slovak users for many years.
Main features include: Mapping from long names of fonts to the metric file
name. The user can specify only exact long names in documents. Support for many
font encodings. Printing of catalogues of fonts and test samples of font
families; the interactive macro \showfonts shows all font families you have
installed via OFS. The user interface is the same for Plain TeX and for LaTeX,
but the implementation differs: the LaTeX variant of OFS uses NFSS, but the
Plain variant implements its own font management (which may even be better than
NFSS) Support for math fonts including TX fonts.

%package -n texlive-olsak-misc
Summary:        Collection of plain TeX macros written by Petr Olsak
Version:        svn74906
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(booklet.tex) = %{tl_version}
Provides:       tex(cropmarks.tex) = %{tl_version}
Provides:       tex(qrcode.tex) = %{tl_version}
Provides:       tex(scanbase.tex) = %{tl_version}
Provides:       tex(scancsv.tex) = %{tl_version}
Provides:       tex(xmlparser.tex) = %{tl_version}

%description -n texlive-olsak-misc
This is a collection of various single-file plain TeX macros written by Petr
Olsak. The documentation is included in each file separately. booklet.tex:
re-orders PDF pages and collects them for booklet printing circu.tex: features
from circuitikz.sty enableda cnv.tex: conversion of texts cnv-pu.tex: example
of usage of cnv.tex --- pdf outlines in Unicode cnv-word.tex: example of usage
of cnv.tex --- word to word conversion eparam.tex: Full expansion during
parameter scanning fun-coffee.tex: generates splotches in the document
openclose.tex: repairs balanced text between \Open ...\Close pair qrcode.tex:
QR code generated at TeX level scanbase.tex: parser of text-style mysql outputs
scancsv.tex: parser of CSV format seplist.tex: macros with alternative
separators of a parameter xmlparser.tex: parser of XML language

%package -n texlive-outerhbox
Summary:        Collect horizontal material for contributing to a paragraph
Version:        svn54254
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(outerhbox.sty) = %{tl_version}

%description -n texlive-outerhbox
The package provides the \outerhbox command, which is similar to \hbox, except
that material is set in outer horizontal mode. This prevents TeX from
optimising away maths penalties and the like, that are needed when the material
is \unhbox'ed.

%package -n texlive-path
Summary:        Typeset paths, making them breakable
Version:        svn22045
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(path.sty) = %{tl_version}

%description -n texlive-path
Defines a macro \path|...|, similar to the LaTeX \verb|...|, that sets the text
in typewriter font and allows hyphen-less breaks at punctuation characters. The
set of characters to be regarded as punctuation may be changed from the
package's default.

%package -n texlive-pdf-trans
Summary:        A set of macros for various transformations of TeX boxes
Version:        svn32809
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pdf-trans.tex) = %{tl_version}

%description -n texlive-pdf-trans
pdf-trans is a set of macros offering various transformations of TeX boxes
(based on plain and pdfeTeX primitives). It was initially inspired by
trans.tex, remade to work with pdfTeX.

%package -n texlive-pdfmsym
Summary:        PDF Math Symbols -- various drawn mathematical symbols
Version:        svn66618
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pdfmsym.tex) = %{tl_version}

%description -n texlive-pdfmsym
This package defines a handful of mathematical symbols many of which are
implemented via PDF's builtin drawing utility. It is intended for use with
pdfTeX and LuaTeX and is supported by XeTeX to a lesser extent. Among the
symbols it defines are some variants of commonly used ones, as well as more
obscure symbols which cannot be as easily found in other TeX or LaTeX packages.

%package -n texlive-pdftoolbox
Summary:        A plain-pdfTeX toolbox for creating beautiful documents
Version:        svn74832
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pdfToolbox.tex) = %{tl_version}
Provides:       tex(ptb-arrays.tex) = %{tl_version}
Provides:       tex(ptb-colorboxes.tex) = %{tl_version}
Provides:       tex(ptb-colors.tex) = %{tl_version}
Provides:       tex(ptb-counters.tex) = %{tl_version}
Provides:       tex(ptb-dictionaries.tex) = %{tl_version}
Provides:       tex(ptb-fonts.tex) = %{tl_version}
Provides:       tex(ptb-hooks.tex) = %{tl_version}
Provides:       tex(ptb-hyperlinks.tex) = %{tl_version}
Provides:       tex(ptb-index.tex) = %{tl_version}
Provides:       tex(ptb-key-value.tex) = %{tl_version}
Provides:       tex(ptb-layout.tex) = %{tl_version}
Provides:       tex(ptb-listings.tex) = %{tl_version}
Provides:       tex(ptb-lists.tex) = %{tl_version}
Provides:       tex(ptb-math.tex) = %{tl_version}
Provides:       tex(ptb-mergesort.tex) = %{tl_version}
Provides:       tex(ptb-pdfData.tex) = %{tl_version}
Provides:       tex(ptb-pdfDstruct.tex) = %{tl_version}
Provides:       tex(ptb-pdfGraphics.tex) = %{tl_version}
Provides:       tex(ptb-pdfdraw-utils.tex) = %{tl_version}
Provides:       tex(ptb-pdfdraw.tex) = %{tl_version}
Provides:       tex(ptb-stack.tex) = %{tl_version}
Provides:       tex(ptb-syntax-C.tex) = %{tl_version}
Provides:       tex(ptb-syntax-TeX.tex) = %{tl_version}
Provides:       tex(ptb-tableofcontents.tex) = %{tl_version}
Provides:       tex(ptb-utils.tex) = %{tl_version}

%description -n texlive-pdftoolbox
pdfToolbox is a toolbox of various "subpackages" intended for programming and
creating beautiful plain-pdfTeX documents. It is an amalgamation of the
following "subpackages" (in the future there will be an ability to access each
one by itself): pdfData -- for storing and manipulating data; pdfDstruct -- for
managing the layout and structure of your document; pdfGraphics -- for adding
some color and illustrations to your document. pdfToolbox currently only works
with pdfTeX. It is not compatible with any form of LaTeX, and currently does
not work with XeTeX or LuaTeX (though hopefully LuaTeX support will be added in
the future).

%package -n texlive-pitex
Summary:        Documentation macros
Version:        svn24731
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pitex.tex) = %{tl_version}

%description -n texlive-pitex
The bundle provides macros that the author uses when writing documentation (for
example, that of the texapi and yax packages). The tools could be used by
anyone, but there is no documentation, and the macros are subject to change
without notice.

%package -n texlive-placeins-plain
Summary:        Insertions that keep their place
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(placeins.tex) = %{tl_version}

%description -n texlive-placeins-plain
This TeX file provides various mechanisms (for plain TeX and close relatives)
to let insertions (footnotes, topins, pageins, etc.) float within their
appropriate section, but to prevent them from intruding into the following
section, even when sections do not normally begin a new page. (If your sections
normally begin a new page, just use \supereject to flush out insertions.)

%package -n texlive-plain-widow
Summary:        Three output routines that extend \plainoutput
Version:        svn75230
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pxwmanual.tex) = %{tl_version}
Provides:       tex(pxwreport.tex) = %{tl_version}
Provides:       tex(pxwsingle.tex) = %{tl_version}
Provides:       tex(pxwspread.tex) = %{tl_version}

%description -n texlive-plain-widow
This package contains three output routines that extend \plainoutput. The first
adds a reporting of problematic lines, i.e., for widow, club, and broken lines.
The second prevents widow lines by changing the \vsize by one line. The third
tries to avoid widow, club, and broken lines as much as possible for spreads.

%package -n texlive-plainpkg
Summary:        A minimal method for making generic packages
Version:        svn27765
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(plainpkg.tex) = %{tl_version}

%description -n texlive-plainpkg
The package provides a minimal method for making generic (i.e.,
TeX-format-independent) packaged, combining maybeload functionality, fallback
definitions for LaTeX \ProvidesPackage and \RequirePackage functionality, and
handling of arbitrary (multiple) "private letters" (analagous LaTeX packages'
use of "@") in nested package files. The documentation contains a central
reference for making and using generic packages based on the package.

%package -n texlive-plipsum
Summary:        'Lorem ipsum' for Plain TeX developers
Version:        svn30353
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(plipsum.tex) = %{tl_version}

%description -n texlive-plipsum
The package provides a paragraph generator designed for use in Plain TeX
documents. The paragraphs generated contain many 'f-groups' (ff, fl etc.) so
the text can act as a test of the ligatures of the font in use.

%package -n texlive-plnfss
Summary:        Font selection for Plain TeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(MIKmathf.tex) = %{tl_version}
Provides:       tex(plnfss.tex) = %{tl_version}

%description -n texlive-plnfss
Plnfss is a set of macros to provide easy font access (somewhat similar to NFSS
but with some limitations) with Plain TeX. Plnfss can automatically make use of
PSNFSS fd files, i.e., when an Adobe Type 1 is used the relevant fd file will
be loaded automatically. For cmr-like fonts (ec, vnr, csr or plr fonts), a
special format called pfd (plain fd) is required and must be loaded manually.
See ot1cmr.pfd for further information.

%package -n texlive-plstmary
Summary:        St. Mary's Road font support for plain TeX
Version:        svn31088
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(stmary.tex) = %{tl_version}

%description -n texlive-plstmary
The package provides commands to produce all the symbols of the St Mary's Road
fonts, in a Plain TeX environment.

%package -n texlive-poormanlog
Summary:        Logarithms and powers with (almost) 9 digits
Version:        svn63400
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(poormanlog.sty) = %{tl_version}
Provides:       tex(poormanlog.tex) = %{tl_version}

%description -n texlive-poormanlog
This small package (usable with Plain e-TeX, LaTeX, or others) with no
dependencies provides two fast expandable macros computing logarithms in base
10 and fractional powers of 10. They handle arguments of 9 digit tokens which
stand for either 1 <= d.dddddddd < 10 (for the log) or 0.xxxxxxxxx (for powers
of 10). They achieve a precision of 1ulp for the logarithm and 2ulp for
fractional powers of ten. Extension to other numerical ranges has to be done by
user, via own macros or some math engine. The xintexpr package (at 1.3f)
imports the poormanlog macros as core constituents of its log10(), pow10(),
log(), exp() and pow() functions.

%package -n texlive-present
Summary:        Presentations with Plain TeX
Version:        svn50048
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(present.tex) = %{tl_version}

%description -n texlive-present
The package offers a collection of simple macros for preparing presentations in
Plain TeX. Slide colour and text colour may be set, links between parts of the
presentation, to other files, and to web addresses may be inserted. Images may
be included easily, and code is available to provide transition effects between
slides or frames. The structure of the macros is not overly complex, so that
users should find it easy to adapt the macros to their specific needs.

%package -n texlive-pwebmac
Summary:        Consolidated WEB macros for DVI and PDF output
Version:        svn74648
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pwebmac.tex) = %{tl_version}

%description -n texlive-pwebmac
The original WEB system by Donald Knuth has the macros webmac.tex that produce
DVI output only; for historic reasons, it will never be modified (apart from
catastrophic errors). Han The Thanh has modified these macros in his
pdfwebmac.tex for PDF output (only) with pdfTeX. Jonathan Kew's XeTeX has
similar macros xewebmac.tex by Khaled Hosny that modify webmac.tex for PDF
output; these macros can only be used with a specific "TeX engine" each. The
present pwebmac package integrates these three WEB macro files similar to
cwebmac.tex in Silvio Levy's and Don Knuth's CWEB system, so pwebmac.tex can be
used with "plain TeX", pdfTeX, and XeTeX alike. Its initial application is the
production of PDF files for all major WEB programs for "TeX and friends" as
distributed in TeX Live. For this purpose, the shell script makeall was whipped
together; it provides various commandline options and works around several
"quirks" in the WEB sources. WEB programmers who want to use pwebmac.tex
instead of the default webmac.tex in their programs have to change the first
line in the TeX file created by weave. From there, all depends on the "TeX
engine" you use.

%package -n texlive-random
Summary:        Generating "random" numbers in TeX
Version:        svn54723
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(random.tex) = %{tl_version}

%description -n texlive-random
Generates pseudo-random integers in the range 1 to 2^{31}. Macros are to
provide random integers in a given range, or random dimensions which can be
used to provide random `real' numbers, are also available.

%package -n texlive-randomlist
Summary:        Deal with database, loop, and random in order to build personalized exercises
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(randomlist.sty) = %{tl_version}
Provides:       tex(randomlist.tex) = %{tl_version}

%description -n texlive-randomlist
The main aim of this package is to work on lists, especially with random
operations. The hidden aim is to build a personal collection of exercises with
different data for each pupil.

%package -n texlive-resumemac
Summary:        Plain TeX macros for resumes
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(resumemac.tex) = %{tl_version}

%description -n texlive-resumemac
A set of macros is provided, together with an file that offers an example of
use.

%package -n texlive-ruler
Summary:        A typographic ruler for TeX
Version:        svn54251
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ruler.tex) = %{tl_version}

%description -n texlive-ruler
The file processes to produce (real) rulers; the author suggests printing them
on transparent plastic and trimming for use as a "real" ruler. The rule widths
are 0.05mm, which can be challenging for (old) laser printers.

%package -n texlive-schemata
Summary:        Print topical diagrams
Version:        svn76178
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(schemata.sty) = %{tl_version}

%description -n texlive-schemata
The package facilitates the creation of "topical schemata", i.e. outlines that
use braces (or facsimiles thereof) to illustrate the breakdown of concepts and
categories in Scholastic thought from late medieval and early modern periods.

%package -n texlive-shade
Summary:        Shade pieces of text
Version:        svn22212
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(shade.tex) = %{tl_version}

%description -n texlive-shade
The package provides a shaded backdrop to a box of text. It uses a Metafont
font (provided) which generates to appropriate shading dependent on the
resolution used in the Metafont printer parameters.

%package -n texlive-simplekv
Summary:        A simple key/value system for TeX and LaTeX
Version:        svn75515
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(simplekv.sty) = %{tl_version}
Provides:       tex(simplekv.tex) = %{tl_version}

%description -n texlive-simplekv
The package provides a simple key/value system for TeX and LaTeX.

%package -n texlive-soul
Summary:        Hyphenation for letterspacing, underlining, and more
Version:        svn67365
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etexcmds.sty)
Requires:       tex(infwarerr.sty)
Provides:       tex(soul-ori.sty) = %{tl_version}
Provides:       tex(soul.sty) = %{tl_version}
Provides:       tex(soulutf8.sty) = %{tl_version}

%description -n texlive-soul
The package provides hyphenable spacing out (letterspacing), underlining,
striking out, etc., using the TeX hyphenation algorithm to find the proper
hyphens automatically. It also provides a mechanism that can be used to
implement similar tasks, that have to treat text syllable by syllable. This is
shown in two examples. This version is a merge of the original soul package
from Melchior Franz and the soulutf8 package from Heiko Oberdiek and supports
also UTF8.

%package -n texlive-stretchy
Summary:        Macros for creating stretchy TeX symbols
Version:        svn75140
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(stretchy.tex) = %{tl_version}
Provides:       tex(strty-logo.tex) = %{tl_version}
Provides:       tex(strty-repeatedsyms.tex) = %{tl_version}
Provides:       tex(strty-stretchedsyms.tex) = %{tl_version}
Provides:       tex(strty-utils.tex) = %{tl_version}

%description -n texlive-stretchy
This package helps to create "stretchy" math symbols. It provides various
ready-made stretchy symbols, as well as auxiliary macros for creating them. The
package has no dependencies and supports both pdfTeX and LuaTeX.

%package -n texlive-swrule
Summary:        Lines thicker in the middle than at the ends
Version:        svn54267
License:        swrule
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(swrule.sty) = %{tl_version}

%description -n texlive-swrule
Defines commands that create rules split into a (specified) number of pieces,
whose size varies to produce the effect of a rule that swells in its centre.

%package -n texlive-systeme
Summary:        Format systems of equations
Version:        svn77138
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(simplekv.sty)
Requires:       tex(xstring.sty)
Provides:       tex(systeme.sty) = %{tl_version}
Provides:       tex(systeme.tex) = %{tl_version}

%description -n texlive-systeme
The package allows you to enter systems of equations or inequalities in an
intuitive way, and produces typeset output where the terms and signs are
aligned vertically. The package works with plain TeX or LaTeX, but e-TeX is
required. Cette petite extension permet de saisir des systemes d'equations ou
inequations de facon intuitive, et produit un affichage ou les termes et les
signes sont alignes verticalement.

%package -n texlive-tabto-generic
Summary:        "Tab" to a measured position in the line
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tabto.tex) = %{tl_version}

%description -n texlive-tabto-generic
\tabto{<length>} moves the typesetting position to <length> from the left
margin of the paragraph. If the typesetting position is already further along,
\tabto starts a new line.

%package -n texlive-termmenu
Summary:        The package provides support for terminal-based menus using expl3
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(termmenu.tex) = %{tl_version}

%description -n texlive-termmenu
When writing programs, it's often required to present the user with a list of
options/actions. The user is then expected to select one of these options for
the program to process. termmenu provides this mechanism for TeX. It requires
only expl3 support, thus the l3kernel and l3packages are both required.

%package -n texlive-tex-ps
Summary:        TeX to PostScript generic macros and add-ons
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cmyk-hax.tex) = %{tl_version}
Provides:       tex(epsfx.tex) = %{tl_version}
Provides:       tex(poligraf.sty) = %{tl_version}
Provides:       tex(trans.tex) = %{tl_version}

%description -n texlive-tex-ps
TeX to PostScript generic macros and add-ons: transformations of EPS files,
prepress preparation, color separation, mirror, etc.

%package -n texlive-texapi
Summary:        Macros to write format-independent packages
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(texapi.tex) = %{tl_version}

%description -n texlive-texapi
Texapi provides utility macros to write format-independent (and -aware)
packages. It is similar in spirit to the etoolbox, except that it isn't tied to
LaTeX. Tools include: engine and format detection, expansion control, command
definition and manipulation, various testing macros, string operations, and
highly customizable while and for loops. The package requires e-TeX (and,
should you want to compile its documentation, the pitex package is also
needed).

%package -n texlive-texdate
Summary:        Date printing, formatting, and manipulation in TeX
Version:        svn49362
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iflang.sty)
Requires:       tex(modulus.sty)
Requires:       tex(padcount.sty)
Provides:       tex(texdate.sty) = %{tl_version}

%description -n texlive-texdate
TeX and LaTeX provide few facilities for dates by default, though many packages
have filled this gap. This package fills it, as well, with a pure TeX-primitive
implementation. It can print dates, advance them by numbers of days, weeks, or
months, determine the weekday automatically (with an algorithm cribbed from the
dayofweek.tex file written by Martin Minow), and print them in (mostly)
arbitrary format. It can also print calendars (monthly and yearly)
automatically, and can be easily localized for non-English languages.

%package -n texlive-texdimens
Summary:        Conversion of TeX dimensions to decimals
Version:        svn61070
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(texdimens.sty) = %{tl_version}
Provides:       tex(texdimens.tex) = %{tl_version}

%description -n texlive-texdimens
Utilities and documentation related to TeX dimensional units, usable both with
Plain (\input texdimens) and with LaTeX (\usepackage{texdimens}).

%package -n texlive-texinfo
Summary:        Texinfo documentation system
Version:        svn77327
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(texinfo-ja.tex) = %{tl_version}
Provides:       tex(texinfo-zh.tex) = %{tl_version}
Provides:       tex(texinfo.tex) = %{tl_version}
Provides:       tex(txi-ca.tex) = %{tl_version}
Provides:       tex(txi-cs.tex) = %{tl_version}
Provides:       tex(txi-de.tex) = %{tl_version}
Provides:       tex(txi-en.tex) = %{tl_version}
Provides:       tex(txi-es.tex) = %{tl_version}
Provides:       tex(txi-fi.tex) = %{tl_version}
Provides:       tex(txi-fr.tex) = %{tl_version}
Provides:       tex(txi-hu.tex) = %{tl_version}
Provides:       tex(txi-is.tex) = %{tl_version}
Provides:       tex(txi-it.tex) = %{tl_version}
Provides:       tex(txi-ja.tex) = %{tl_version}
Provides:       tex(txi-nb.tex) = %{tl_version}
Provides:       tex(txi-nl.tex) = %{tl_version}
Provides:       tex(txi-nn.tex) = %{tl_version}
Provides:       tex(txi-pl.tex) = %{tl_version}
Provides:       tex(txi-pt.tex) = %{tl_version}
Provides:       tex(txi-ru.tex) = %{tl_version}
Provides:       tex(txi-sr.tex) = %{tl_version}
Provides:       tex(txi-tr.tex) = %{tl_version}
Provides:       tex(txi-uk.tex) = %{tl_version}
Provides:       tex(txi-zh.tex) = %{tl_version}

%description -n texlive-texinfo
Texinfo is the preferred format for documentation in the GNU project; the
format may be used to produce online or printed output from a single source.
The Texinfo macros may be used to produce printable output using TeX; other
programs in the distribution offer online interactive use (with hypertext
linkages in some cases). The latest release of the texinfo.tex macros and
texi2dvi and texi2pdf scripts may be found in the texinfo-latest package, which
are usually newer than the last full release. CTAN does not hold any other
Texinfo-related files; see its GNU home page for downloads and other info.

%package -n texlive-timetable
Summary:        Generate timetables
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(timetable.tex) = %{tl_version}

%description -n texlive-timetable
A highly-configurable package, with nice output and simple input. The macros
use a radix sort mechanism so that the order of input is not critical.

%package -n texlive-tokmap
Summary:        Iterate over a token list expandably, without dropping spaces or braced groups
Version:        svn75599
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tokmap.sty) = %{tl_version}
Provides:       tex(tokmap.tex) = %{tl_version}

%description -n texlive-tokmap
Usage: \tokmap <command> { <tokens> } applies command over the token list
tokens. Space tokens, left and right braces are replaced with the marker tokens
\tokmap@space, \tokmap@bgroup, and \tokmap@egroup respectively (which are
\ifx-equal to themselves exclusively). For convenience, command may contain
multiple tokens. It is assumed that { and } are the only characters with
category codes 1 (beginning of group) and 2 (end of group) respectively.
Expandable. This package may be used in LaTeX by \usepackage{tokmap}, or in
plain TeX and other formats by \input{tokmap}. See the visualtoks package for
an example application.

%package -n texlive-tracklang
Summary:        Language and dialect tracker
Version:        svn74576
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tracklang-region-codes.tex) = %{tl_version}
Provides:       tex(tracklang-scripts.sty) = %{tl_version}
Provides:       tex(tracklang-scripts.tex) = %{tl_version}
Provides:       tex(tracklang.sty) = %{tl_version}
Provides:       tex(tracklang.tex) = %{tl_version}

%description -n texlive-tracklang
The tracklang package is provided for package developers who want a simple
interface to find out which languages the user has requested through packages
such as babel or polyglossia. This package does not provide any translations!
Its purpose is simply to track which languages have been requested by the user.
Generic TeX code is in tracklang.tex for non-LaTeX users.

%package -n texlive-transparent-io
Summary:        Show for approval the filenames used in \input, \openin, or \openout
Version:        svn64113
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-transparent-io-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-transparent-io-doc <= 11:%{version}

%description -n texlive-transparent-io
This package provides macros to make the file I/O in plain TeX more
transparent. That is, every \input, \openin, and \openout operation by TeX is
presented to the user who must check carefully if the file name of the source
is acceptable. The user must sometimes enter additional text and has to specify
the file name that the TeX operation should use. The macros require a complex
installation procedure; the package contains sed and bash scripts to do this on
a UNIX-like operating system. Every installation is different from any other as
password-protected macro names and private messages have to be chosen by the
installer. Therefore, the files in the package cannot be used directly. The
files carry the extension .org, and only after the user has performed an
individual customization for a private installation the changed files are
renamed and have the extension .tex. For details see the manual.

%package -n texlive-treetex
Summary:        Draw trees
Version:        svn28176
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(classes.tex) = %{tl_version}
Provides:       tex(l_pic.tex) = %{tl_version}
Provides:       tex(treetex.tex) = %{tl_version}

%description -n texlive-treetex
Macros to draw trees, within TeX (or LaTeX). The algorithm used is discussed in
an accompanying paper (written using LaTeX 2.09).

%package -n texlive-trigonometry
Summary:        Demonstration code for cos and sin in TeX macros
Version:        svn43006
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(trigonometry.tex) = %{tl_version}

%description -n texlive-trigonometry
A document that both provides macros that are usable elsewhere, and
demonstrates the macros. The code uses the "classical" analytical expansion of
sin and cos (the more recent trig uses a "numerical analyst's" expansion).

%package -n texlive-tuple
Summary:        Expandable operations for tuples of numbers
Version:        svn77463
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tuple.sty) = %{tl_version}
Provides:       tex(tuple.tex) = %{tl_version}

%description -n texlive-tuple
This package provides expandable operations for tuples of numbers: len, sum,
min, max, mean, med, quantile, standard deviation, get item, position of item
sort, add or set(*) items, filter, operations, composition(*), split(*),
formatting and display All with a concise syntax that is easy and intuitive to
use : object.method1.method2... (*): unexpandable method
--------------------------------------------------------------- -------- Cette
extension met a disposition des operations developpables pour les tuples de
nombres : len, sum, min, max, mean, med, quantile, ecart type, get item,
position d'un element tri, ajout ou modification(*) d'elements, filtre,
operations, composition(*), coupure(*), formattage et affichage Le tout avec
une syntaxe concise et d'un usage facile et intuitif :
object.methode1.methode2... (*) : methode non developpable

%package -n texlive-ulem
Summary:        Package for underlining
Version:        svn53365
License:        ulem
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ulem.sty) = %{tl_version}

%description -n texlive-ulem
The package provides an \ul (underline) command which will break over line
ends; this technique may be used to replace \em (both in that form and as the
\emph command), so as to make output look as if it comes from a typewriter. The
package also offers double and wavy underlining, and striking out (line through
words) and crossing out (/// over words). The package works with both Plain TeX
and LaTeX.

%package -n texlive-upca
Summary:        Print UPC-A barcodes
Version:        svn22511
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(upca.tex) = %{tl_version}

%description -n texlive-upca
The package defines a single macro \upca, to print UPC-A barcodes.

%package -n texlive-varisize
Summary:        Change font size in Plain TeX
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(10point.tex) = %{tl_version}
Provides:       tex(10pointss.tex) = %{tl_version}
Provides:       tex(11point.tex) = %{tl_version}
Provides:       tex(12point.tex) = %{tl_version}
Provides:       tex(14point.tex) = %{tl_version}
Provides:       tex(17point.tex) = %{tl_version}
Provides:       tex(20point.tex) = %{tl_version}
Provides:       tex(7point.tex) = %{tl_version}
Provides:       tex(8point.tex) = %{tl_version}
Provides:       tex(9point.tex) = %{tl_version}

%description -n texlive-varisize
A series of files, each of which defines a size-change macro. Note that
10point.tex is by convention called by one of the other files, so that there's
always a "way back".

%package -n texlive-visualtoks
Summary:        Typeset TeXbook-style visualisations of token lists
Version:        svn76207
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tokmap.sty)
Provides:       tex(visualtoks.sty) = %{tl_version}
Provides:       tex(visualtoks.tex) = %{tl_version}

%description -n texlive-visualtoks
This package provides the \visualtoks command to display arbitrary list of
tokens, for pedagogical or debugging purposes, in a style inspired by Knuth's
TeXbook. The package may be used in plain TeX or LaTeX.

%package -n texlive-xii
Summary:        Christmas silliness (English)
Version:        svn45804
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xii-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xii-doc <= 11:%{version}

%description -n texlive-xii
This is the plain TeX file xii.tex. Call "pdftex xii.tex" to produce a
(perhaps) surprising typeset document.

%package -n texlive-xii-lat
Summary:        Christmas silliness (Latin)
Version:        svn45805
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xii-lat-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xii-lat-doc <= 11:%{version}

%description -n texlive-xii-lat
This is the plain TeX file xii-lat.tex. Call "pdftex xii-lat.tex" to produce a
(perhaps) surprising typeset document.

%package -n texlive-xintsession
Summary:        Interactive computing sessions (fractions, floating points, polynomials)
Version:        svn60926
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xintsession.tex) = %{tl_version}

%description -n texlive-xintsession
This package provides support for interactive computing sessions with etex (or
pdftex) executed on the command line, on the basis of the xintexpr and polexpr
packages. Once xintsession is loaded, eTeX becomes an interactive computing
software capable of executing arbitrary precision calculations, or exact
calculations with arbitrarily big fractions. It can also manipulate polynomials
as algebraic entities. Numerical variables and functions can be defined during
the session, and each evaluation result is stored in automatically labeled
variables. A file is automatically created storing inputs and outputs.

%package -n texlive-xlop
Summary:        Calculates and displays arithmetic operations
Version:        svn56910
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xlop.sty) = %{tl_version}
Provides:       tex(xlop.tex) = %{tl_version}

%description -n texlive-xlop
Xlop (eXtra Large OPeration) will typeset arithmetic problems either in-line or
"as in school" (using French school conventions). So for example, \opadd{2}{3}
can give either $2+3=5$ or something similar to: \begin{tabular}{r} 2\\ +3\\
\hline 5\end{tabular}. Furthermore, numbers may be very large, e.g 200 figures
(with a very long compilation time). Many other features allow to deal with
numbers (tests, display, some high level operations, etc.)

%package -n texlive-yax
Summary:        Yet Another Key System
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(t-yax.tex) = %{tl_version}
Provides:       tex(yax.sty) = %{tl_version}
Provides:       tex(yax.tex) = %{tl_version}

%description -n texlive-yax
YaX is advertised as a key system, but it rather organizes attributes in
parameters, which parameters can be executed, so that YaX is halfway between
key management and macro definition (and actually hopes to provide a user's
interface). Values assigned to attributes can be retrieved and tested in
various ways, with full expandability ensured as much as possible. Finally,
YaX's syntax is a quite peculiar (as few braces as possible), but may be
customized. YaX is based on texapi and thus requires e-TeX.

%package -n texlive-zztex
Summary:        A full-featured TeX macro package for producing books, journals, and manuals
Version:        svn55862
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(zzart.tex) = %{tl_version}
Provides:       tex(zzbiblio.tex) = %{tl_version}
Provides:       tex(zzbibtex.tex) = %{tl_version}
Provides:       tex(zzblock.tex) = %{tl_version}
Provides:       tex(zzcmmath.tex) = %{tl_version}
Provides:       tex(zzcomenc.tex) = %{tl_version}
Provides:       tex(zzdiv.tex) = %{tl_version}
Provides:       tex(zzdoc.tex) = %{tl_version}
Provides:       tex(zzerror.tex) = %{tl_version}
Provides:       tex(zzfloat.tex) = %{tl_version}
Provides:       tex(zzfont.tex) = %{tl_version}
Provides:       tex(zzfront.tex) = %{tl_version}
Provides:       tex(zzhelp.tex) = %{tl_version}
Provides:       tex(zzhmode.tex) = %{tl_version}
Provides:       tex(zzhmodeb.tex) = %{tl_version}
Provides:       tex(zzhyper.tex) = %{tl_version}
Provides:       tex(zzhyph.tex) = %{tl_version}
Provides:       tex(zzindexv1.tex) = %{tl_version}
Provides:       tex(zzindexv2.tex) = %{tl_version}
Provides:       tex(zzio.tex) = %{tl_version}
Provides:       tex(zzlist.tex) = %{tl_version}
Provides:       tex(zzltrspc.tex) = %{tl_version}
Provides:       tex(zzlucida.tex) = %{tl_version}
Provides:       tex(zzmath.tex) = %{tl_version}
Provides:       tex(zzmathv3.tex) = %{tl_version}
Provides:       tex(zzmathv4.tex) = %{tl_version}
Provides:       tex(zzmathv5.tex) = %{tl_version}
Provides:       tex(zzmathv6.tex) = %{tl_version}
Provides:       tex(zzmerge.tex) = %{tl_version}
Provides:       tex(zzmisc.tex) = %{tl_version}
Provides:       tex(zzmtime.tex) = %{tl_version}
Provides:       tex(zznewmath.tex) = %{tl_version}
Provides:       tex(zznote.tex) = %{tl_version}
Provides:       tex(zzoverlay.tex) = %{tl_version}
Provides:       tex(zzpage.tex) = %{tl_version}
Provides:       tex(zzplain.tex) = %{tl_version}
Provides:       tex(zzprog.tex) = %{tl_version}
Provides:       tex(zzps.tex) = %{tl_version}
Provides:       tex(zzreg.tex) = %{tl_version}
Provides:       tex(zzrunner.tex) = %{tl_version}
Provides:       tex(zzsect.tex) = %{tl_version}
Provides:       tex(zztabbing.tex) = %{tl_version}
Provides:       tex(zztabularv1.tex) = %{tl_version}
Provides:       tex(zztabularv2.tex) = %{tl_version}
Provides:       tex(zztabularv3.tex) = %{tl_version}
Provides:       tex(zztag.tex) = %{tl_version}
Provides:       tex(zztex.tex) = %{tl_version}
Provides:       tex(zztext.tex) = %{tl_version}
Provides:       tex(zzttladj.tex) = %{tl_version}
Provides:       tex(zztures.tex) = %{tl_version}
Provides:       tex(zzver.tex) = %{tl_version}
Provides:       tex(zzvmode.tex) = %{tl_version}
Provides:       tex(zzxref.tex) = %{tl_version}

%description -n texlive-zztex
The ZzTeX macro package is a full-featured TeX macro package specially designed
for producing books, journals, and manuals. Development of the package began in
1989. Since then, about 500 textbooks and journals have been produced with it
for a variety of publishers. Numerous authors have used the package to produce
subsequent editions of their books. ZzTeX runs under Plain TeX. The only
documentation available for the package is contained in the zz*.dat files that
accompany the TeX files.


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-abbr
%license pd.txt
%{_texmf_main}/tex/generic/abbr/
%doc %{_texmf_main}/doc/generic/abbr/

%files -n texlive-abstyles
%license other-free.txt
%{_texmf_main}/bibtex/bib/abstyles/
%{_texmf_main}/bibtex/bst/abstyles/
%{_texmf_main}/tex/generic/abstyles/
%doc %{_texmf_main}/doc/bibtex/abstyles/

%files -n texlive-advice
%license lppl1.3c.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/advice/
%{_texmf_main}/tex/latex/advice/
%{_texmf_main}/tex/plain/advice/
%doc %{_texmf_main}/doc/generic/advice/

%files -n texlive-apnum
%license pd.txt
%{_texmf_main}/tex/generic/apnum/
%doc %{_texmf_main}/doc/generic/apnum/

%files -n texlive-autoaligne
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/autoaligne/
%doc %{_texmf_main}/doc/generic/autoaligne/

%files -n texlive-barr
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/barr/
%doc %{_texmf_main}/doc/generic/barr/

%files -n texlive-bitelist
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/bitelist/
%doc %{_texmf_main}/doc/generic/bitelist/

%files -n texlive-borceux
%license other-free.txt
%{_texmf_main}/tex/generic/borceux/
%doc %{_texmf_main}/doc/generic/borceux/

%files -n texlive-c-pascal
%license pd.txt
%{_texmf_main}/tex/generic/c-pascal/
%doc %{_texmf_main}/doc/generic/c-pascal/

%files -n texlive-calcfrac
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/calcfrac/
%doc %{_texmf_main}/doc/generic/calcfrac/

%files -n texlive-catcodes
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/catcodes/
%doc %{_texmf_main}/doc/generic/catcodes/

%files -n texlive-chronosys
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/chronosys/
%doc %{_texmf_main}/doc/generic/chronosys/

%files -n texlive-collargs
%license lppl1.3c.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/latex/collargs/
%{_texmf_main}/tex/plain/collargs/
%doc %{_texmf_main}/doc/generic/collargs/

%files -n texlive-colorsep
%license pd.txt
%{_texmf_main}/dvips/colorsep/

%files -n texlive-compare
%license pd.txt
%{_texmf_main}/tex/generic/compare/

%files -n texlive-crossrefenum
%license gpl3.txt
%license fdl.txt
%{_texmf_main}/tex/generic/crossrefenum/
%doc %{_texmf_main}/doc/generic/crossrefenum/

%files -n texlive-cweb-old
%license pd.txt
%{_texmf_main}/tex/plain/cweb-old/

%files -n texlive-dinat
%license pd.txt
%{_texmf_main}/bibtex/bst/dinat/
%doc %{_texmf_main}/doc/bibtex/dinat/

%files -n texlive-dirtree
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/dirtree/
%doc %{_texmf_main}/doc/generic/dirtree/

%files -n texlive-docbytex
%{_texmf_main}/tex/generic/docbytex/
%doc %{_texmf_main}/doc/generic/docbytex/

%files -n texlive-dowith
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/dowith/
%doc %{_texmf_main}/doc/generic/dowith/

%files -n texlive-eijkhout
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/eijkhout/

%files -n texlive-encxvlna
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/encxvlna/
%{_texmf_main}/tex/plain/encxvlna/
%doc %{_texmf_main}/doc/generic/encxvlna/

%files -n texlive-eoldef
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/eoldef/
%doc %{_texmf_main}/doc/generic/eoldef/

%files -n texlive-epigram
%license pd.txt
%{_texmf_main}/tex/generic/epigram/

%files -n texlive-epsf
%license pd.txt
%{_texmf_main}/tex/generic/epsf/
%doc %{_texmf_main}/doc/generic/epsf/

%files -n texlive-epsf-dvipdfmx
%license pd.txt
%{_texmf_main}/tex/plain/epsf-dvipdfmx/
%doc %{_texmf_main}/doc/plain/epsf-dvipdfmx/

%files -n texlive-etoolbox-generic
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/etoolbox-generic/
%doc %{_texmf_main}/doc/generic/etoolbox-generic/

%files -n texlive-expex-acro
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/expex-acro/
%doc %{_texmf_main}/doc/generic/expex-acro/

%files -n texlive-expkv-bundle
%license lppl1.3c.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/expkv-bundle/
%{_texmf_main}/tex/latex/expkv-bundle/
%doc %{_texmf_main}/doc/latex/expkv-bundle/

%files -n texlive-fenixpar
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/fenixpar/
%doc %{_texmf_main}/doc/generic/fenixpar/

%files -n texlive-figflow
%license other-free.txt
%{_texmf_main}/tex/plain/figflow/
%doc %{_texmf_main}/doc/plain/figflow/

%files -n texlive-fixpdfmag
%license pd.txt
%{_texmf_main}/tex/plain/fixpdfmag/

%files -n texlive-fltpoint
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/fltpoint/
%doc %{_texmf_main}/doc/generic/fltpoint/

%files -n texlive-fntproof
%license pd.txt
%{_texmf_main}/tex/generic/fntproof/
%doc %{_texmf_main}/doc/generic/fntproof/

%files -n texlive-font-change
%license other-free.txt
%{_texmf_main}/tex/plain/font-change/
%doc %{_texmf_main}/doc/plain/font-change/

%files -n texlive-fontch
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/fontch/
%doc %{_texmf_main}/doc/plain/fontch/

%files -n texlive-fontname
%license gpl2.txt
%{_texmf_main}/fonts/map/fontname/
%doc %{_texmf_main}/doc/fonts/fontname/
%doc %{_texmf_main}/doc/info/

%files -n texlive-gates
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/gates/
%doc %{_texmf_main}/doc/generic/gates/

%files -n texlive-getoptk
%license other-free.txt
%{_texmf_main}/tex/plain/getoptk/
%doc %{_texmf_main}/doc/plain/getoptk/

%files -n texlive-gfnotation
%license gpl3.txt
%{_texmf_main}/tex/plain/gfnotation/
%doc %{_texmf_main}/doc/plain/gfnotation/

%files -n texlive-gobble
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/gobble/
%doc %{_texmf_main}/doc/generic/gobble/

%files -n texlive-graphics-pln
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/graphics-pln/
%doc %{_texmf_main}/doc/plain/graphics-pln/

%files -n texlive-gtl
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/gtl/
%doc %{_texmf_main}/doc/generic/gtl/

%files -n texlive-hlist
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hlist/
%doc %{_texmf_main}/doc/generic/hlist/

%files -n texlive-hyplain
%license pd.txt
%{_texmf_main}/tex/plain/hyplain/
%doc %{_texmf_main}/doc/plain/hyplain/

%files -n texlive-ifis-macros
%license gpl3.txt
%{_texmf_main}/tex/plain/ifis-macros/
%doc %{_texmf_main}/doc/plain/ifis-macros/

%files -n texlive-inputnormalization
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/inputnormalization/
%doc %{_texmf_main}/doc/latex/inputnormalization/

%files -n texlive-insbox
%license pd.txt
%{_texmf_main}/tex/generic/insbox/
%doc %{_texmf_main}/doc/generic/insbox/

%files -n texlive-js-misc
%license pd.txt
%{_texmf_main}/tex/plain/js-misc/
%doc %{_texmf_main}/doc/plain/js-misc/

%files -n texlive-kastrup
%license other-free.txt
%{_texmf_main}/tex/generic/kastrup/
%doc %{_texmf_main}/doc/generic/kastrup/

%files -n texlive-lambda-lists
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/lambda-lists/
%doc %{_texmf_main}/doc/plain/lambda-lists/

%files -n texlive-langcode
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/langcode/
%doc %{_texmf_main}/doc/generic/langcode/

%files -n texlive-lecturer
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/lecturer/
%doc %{_texmf_main}/doc/generic/lecturer/

%files -n texlive-letterspacing
%license knuth.txt
%{_texmf_main}/tex/generic/letterspacing/

%files -n texlive-librarian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/librarian/
%doc %{_texmf_main}/doc/generic/librarian/

%files -n texlive-listofitems
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/listofitems/
%doc %{_texmf_main}/doc/generic/listofitems/

%files -n texlive-localloc
%license other-free.txt
%{_texmf_main}/tex/generic/localloc/
%doc %{_texmf_main}/doc/generic/localloc/

%files -n texlive-mathdots
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/mathdots/
%doc %{_texmf_main}/doc/generic/mathdots/

%files -n texlive-measurebox
%license mit.txt
%{_texmf_main}/tex/generic/measurebox/
%doc %{_texmf_main}/doc/generic/measurebox/

%files -n texlive-metatex
%license gpl2.txt
%{_texmf_main}/tex/plain/metatex/
%doc %{_texmf_main}/doc/plain/metatex/

%files -n texlive-midnight
%license other-free.txt
%{_texmf_main}/tex/generic/midnight/
%doc %{_texmf_main}/doc/generic/midnight/

%files -n texlive-mkpattern
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/mkpattern/
%doc %{_texmf_main}/doc/plain/mkpattern/

%files -n texlive-mlawriter
%license cc-zero-1.txt
%{_texmf_main}/tex/plain/mlawriter/
%doc %{_texmf_main}/doc/plain/mlawriter/

%files -n texlive-modulus
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/modulus/
%doc %{_texmf_main}/doc/generic/modulus/

%files -n texlive-multido
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/multido/
%{_texmf_main}/tex/latex/multido/
%doc %{_texmf_main}/doc/generic/multido/

%files -n texlive-namedef
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/namedef/
%doc %{_texmf_main}/doc/generic/namedef/

%files -n texlive-navigator
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/navigator/
%doc %{_texmf_main}/doc/generic/navigator/

%files -n texlive-newsletr
%license other-free.txt
%{_texmf_main}/tex/plain/newsletr/
%doc %{_texmf_main}/doc/plain/newsletr/

%files -n texlive-nth
%license pd.txt
%{_texmf_main}/tex/generic/nth/

%files -n texlive-ofs
%license knuth.txt
%{_texmf_main}/tex/generic/ofs/
%doc %{_texmf_main}/doc/generic/ofs/

%files -n texlive-olsak-misc
%license pd.txt
%{_texmf_main}/tex/generic/olsak-misc/
%doc %{_texmf_main}/doc/generic/olsak-misc/

%files -n texlive-outerhbox
%license gpl2.txt
%{_texmf_main}/tex/generic/outerhbox/

%files -n texlive-path
%license other-free.txt
%{_texmf_main}/tex/generic/path/
%doc %{_texmf_main}/doc/generic/path/

%files -n texlive-pdf-trans
%license pd.txt
%{_texmf_main}/tex/generic/pdf-trans/
%doc %{_texmf_main}/doc/generic/pdf-trans/

%files -n texlive-pdfmsym
%license mit.txt
%{_texmf_main}/tex/generic/pdfmsym/
%doc %{_texmf_main}/doc/generic/pdfmsym/

%files -n texlive-pdftoolbox
%license mit.txt
%{_texmf_main}/tex/plain/pdftoolbox/
%doc %{_texmf_main}/doc/latex/pdftoolbox/

%files -n texlive-pitex
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/pitex/
%doc %{_texmf_main}/doc/plain/pitex/

%files -n texlive-placeins-plain
%license pd.txt
%{_texmf_main}/tex/plain/placeins-plain/

%files -n texlive-plain-widow
%license gpl3.txt
%{_texmf_main}/tex/plain/plain-widow/
%doc %{_texmf_main}/doc/plain/plain-widow/

%files -n texlive-plainpkg
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/plainpkg/
%doc %{_texmf_main}/doc/generic/plainpkg/

%files -n texlive-plipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/plipsum/
%doc %{_texmf_main}/doc/plain/plipsum/

%files -n texlive-plnfss
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/plnfss/
%doc %{_texmf_main}/doc/plain/plnfss/

%files -n texlive-plstmary
%license pd.txt
%{_texmf_main}/tex/plain/plstmary/
%doc %{_texmf_main}/doc/plain/plstmary/

%files -n texlive-poormanlog
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/poormanlog/
%doc %{_texmf_main}/doc/generic/poormanlog/

%files -n texlive-present
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/present/
%doc %{_texmf_main}/doc/plain/present/

%files -n texlive-pwebmac
%license pd.txt
%{_texmf_main}/tex/plain/pwebmac/
%doc %{_texmf_main}/doc/plain/pwebmac/

%files -n texlive-random
%license pd.txt
%{_texmf_main}/tex/generic/random/
%doc %{_texmf_main}/doc/generic/random/

%files -n texlive-randomlist
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/randomlist/
%doc %{_texmf_main}/doc/generic/randomlist/

%files -n texlive-resumemac
%license pd.txt
%{_texmf_main}/tex/plain/resumemac/
%doc %{_texmf_main}/doc/plain/resumemac/

%files -n texlive-ruler
%license gpl2.txt
%{_texmf_main}/tex/generic/ruler/

%files -n texlive-schemata
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/schemata/
%doc %{_texmf_main}/doc/generic/schemata/

%files -n texlive-shade
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/shade/
%{_texmf_main}/tex/generic/shade/
%doc %{_texmf_main}/doc/generic/shade/

%files -n texlive-simplekv
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/simplekv/
%doc %{_texmf_main}/doc/generic/simplekv/

%files -n texlive-soul
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/soul/
%doc %{_texmf_main}/doc/generic/soul/

%files -n texlive-stretchy
%license mit.txt
%{_texmf_main}/tex/generic/stretchy/
%doc %{_texmf_main}/doc/generic/stretchy/

%files -n texlive-swrule
%license other-free.txt
%{_texmf_main}/tex/generic/swrule/

%files -n texlive-systeme
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/systeme/
%doc %{_texmf_main}/doc/generic/systeme/

%files -n texlive-tabto-generic
%license pd.txt
%{_texmf_main}/tex/generic/tabto-generic/

%files -n texlive-termmenu
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/termmenu/
%doc %{_texmf_main}/doc/generic/termmenu/

%files -n texlive-tex-ps
%license pd.txt
%{_texmf_main}/dvips/tex-ps/
%{_texmf_main}/tex/generic/tex-ps/
%doc %{_texmf_main}/doc/generic/tex-ps/

%files -n texlive-texapi
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/texapi/
%doc %{_texmf_main}/doc/generic/texapi/

%files -n texlive-texdate
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/texdate/
%doc %{_texmf_main}/doc/generic/texdate/

%files -n texlive-texdimens
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/texdimens/
%doc %{_texmf_main}/doc/generic/texdimens/

%files -n texlive-texinfo
%license gpl2.txt
%{_texmf_main}/tex/texinfo/

%files -n texlive-timetable
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/timetable/

%files -n texlive-tokmap
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/tokmap/
%doc %{_texmf_main}/doc/generic/tokmap/

%files -n texlive-tracklang
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/tracklang/
%{_texmf_main}/tex/latex/tracklang/
%doc %{_texmf_main}/doc/generic/tracklang/

%files -n texlive-transparent-io
%license gpl3.txt
%doc %{_texmf_main}/doc/plain/transparent-io/

%files -n texlive-treetex
%license pd.txt
%{_texmf_main}/tex/plain/treetex/
%doc %{_texmf_main}/doc/plain/treetex/

%files -n texlive-trigonometry
%license knuth.txt
%{_texmf_main}/tex/generic/trigonometry/
%doc %{_texmf_main}/doc/generic/trigonometry/

%files -n texlive-tuple
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/tuple/
%doc %{_texmf_main}/doc/generic/tuple/

%files -n texlive-ulem
%license other-free.txt
%{_texmf_main}/tex/generic/ulem/
%doc %{_texmf_main}/doc/generic/ulem/

%files -n texlive-upca
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/upca/
%doc %{_texmf_main}/doc/generic/upca/

%files -n texlive-varisize
%license pd.txt
%{_texmf_main}/tex/plain/varisize/
%doc %{_texmf_main}/doc/plain/varisize/

%files -n texlive-visualtoks
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/visualtoks/
%doc %{_texmf_main}/doc/generic/visualtoks/

%files -n texlive-xii
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/plain/xii/

%files -n texlive-xii-lat
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/plain/xii-lat/

%files -n texlive-xintsession
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/xintsession/
%doc %{_texmf_main}/doc/plain/xintsession/

%files -n texlive-xlop
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/xlop/
%doc %{_texmf_main}/doc/generic/xlop/

%files -n texlive-yax
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/yax/
%doc %{_texmf_main}/doc/generic/yax/

%files -n texlive-zztex
%license mit.txt
%{_texmf_main}/tex/plain/zztex/
%doc %{_texmf_main}/doc/plain/zztex/

%changelog
* Wed Feb 04 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75599-3
- fix descriptions, licensing

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75599-2
- regen, no deps from docs

* Thu Sep 18 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75599-1
- Update to TeX Live 2025
