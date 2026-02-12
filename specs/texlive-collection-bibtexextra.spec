%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-bibtexextra
Epoch:          12
Version:        svn75480
Release:        6%{?dist}
Summary:        BibTeX additional styles

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-bibtexextra.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aaai-named.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aichej.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ajl.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsrefs.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsrefs.doc.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/annotate.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apacite.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apacite.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apalike-ejor.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apalike-ejor.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apalike2.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/archaeologie.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/archaeologie.doc.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/authordate.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/authordate.doc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beebe.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/besjournals.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/besjournals.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bestpapers.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bestpapers.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bib2qr.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bib2qr.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibarts.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibarts.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibbreeze.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibbreeze.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibhtml.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibhtml.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-abnt.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-abnt.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-anonymous.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-anonymous.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-apa.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-apa.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-apa6.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-apa6.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-archaeology.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-archaeology.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-arthistory-bonn.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-arthistory-bonn.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bath.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bath.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bookinarticle.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bookinarticle.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bookinother.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bookinother.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bwl.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-bwl.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-caspervector.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-caspervector.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-chem.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-chem.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-chicago.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-chicago.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-claves.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-claves.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-cse.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-cse.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-cv.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-cv.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-dw.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-dw.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-enc.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-enc.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ext.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ext.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-fiwi.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-fiwi.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-gb7714-2015.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-gb7714-2015.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-german-legal.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-german-legal.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-gost.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-gost.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-historian.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-historian.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ieee.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ieee.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ijsra.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ijsra.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-iso690.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-iso690.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-jura2.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-jura2.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-juradiss.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-juradiss.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-license.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-license.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-lncs.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-lncs.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-lni.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-lni.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-luh-ipw.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-luh-ipw.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-manuscripts-philology.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-manuscripts-philology.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-mla.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-mla.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-morenames.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-morenames.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ms.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-ms.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-multiple-dm.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-multiple-dm.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-musuos.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-musuos.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-nature.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-nature.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-nejm.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-nejm.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-nottsclassic.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-nottsclassic.doc.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-opcit-booktitle.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-opcit-booktitle.doc.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-oxref.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-oxref.doc.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-philosophy.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-philosophy.doc.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-phys.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-phys.doc.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-publist.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-publist.doc.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-readbbl.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-readbbl.doc.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-realauthor.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-realauthor.doc.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-sbl.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-sbl.doc.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-science.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-science.doc.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-shortfields.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-shortfields.doc.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-socialscienceshuberlin.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-socialscienceshuberlin.doc.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-software.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-software.doc.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-source-division.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-source-division.doc.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-spbasic.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-spbasic.doc.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-subseries.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-subseries.doc.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-swiss-legal.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-swiss-legal.doc.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-trad.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-trad.doc.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.doc.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-unified.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-unified.doc.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-vancouver.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-vancouver.doc.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex2bibitem.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex2bibitem.doc.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblist.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblist.doc.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtools.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtopic.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtopic.doc.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtopicprefix.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtopicprefix.doc.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibunits.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibunits.doc.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biolett-bst.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biolett-bst.doc.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookdb.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookdb.doc.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/breakcites.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/breakcites.doc.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cell.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cell.doc.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chbibref.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chbibref.doc.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chembst.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chembst.doc.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chicago.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chicago-annote.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chicago-annote.doc.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chicagoa.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chicagolinks.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chicagolinks.doc.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chscite.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chscite.doc.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeall.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeall.doc.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeref.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeref.doc.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeright.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/citeright.doc.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collref.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collref.doc.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/compactbib.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/custom-bib.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/custom-bib.doc.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/din1505.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/din1505.doc.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dk-bib.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dk-bib.doc.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doipubmed.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doipubmed.doc.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecobiblatex.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecobiblatex.doc.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/econ-bst.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/econ-bst.doc.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/economic.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/economic.doc.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fbs.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figbib.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figbib.doc.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footbib.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footbib.doc.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/francais-bst.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/francais-bst.doc.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gbt7714.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gbt7714.doc.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geschichtsfrkl.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geschichtsfrkl.doc.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harvard.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harvard.doc.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harvmac.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harvmac.doc.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-bibliography.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-bibliography.doc.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/historische-zeitschrift.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/historische-zeitschrift.doc.tar.xz
Source231:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/icite.tar.xz
Source232:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/icite.doc.tar.xz
Source233:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ietfbibs.tar.xz
Source234:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ietfbibs.doc.tar.xz
Source235:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ijqc.tar.xz
Source236:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ijqc.doc.tar.xz
Source237:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inlinebib.tar.xz
Source238:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inlinebib.doc.tar.xz
Source239:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iopart-num.tar.xz
Source240:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iopart-num.doc.tar.xz
Source241:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/is-bst.tar.xz
Source242:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/is-bst.doc.tar.xz
Source243:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jbact.tar.xz
Source244:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jmb.tar.xz
Source245:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jneurosci.tar.xz
Source246:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jneurosci.doc.tar.xz
Source247:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jurabib.tar.xz
Source248:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jurabib.doc.tar.xz
Source249:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ksfh_nat.tar.xz
Source250:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logreq.tar.xz
Source251:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logreq.doc.tar.xz
Source252:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltb2bib.tar.xz
Source253:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltb2bib.doc.tar.xz
Source254:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luabibentry.tar.xz
Source255:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luabibentry.doc.tar.xz
Source256:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/margbib.tar.xz
Source257:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/margbib.doc.tar.xz
Source258:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multibib.tar.xz
Source259:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multibib.doc.tar.xz
Source260:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/munich.tar.xz
Source261:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/munich.doc.tar.xz
Source262:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nar.tar.xz
Source263:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newcastle-bst.tar.xz
Source264:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newcastle-bst.doc.tar.xz
Source265:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nmbib.tar.xz
Source266:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nmbib.doc.tar.xz
Source267:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/notes2bib.tar.xz
Source268:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/notes2bib.doc.tar.xz
Source269:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/notex-bst.tar.xz
Source270:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oscola.tar.xz
Source271:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oscola.doc.tar.xz
Source272:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/perception.tar.xz
Source273:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/perception.doc.tar.xz
Source274:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plainyr.tar.xz
Source275:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pnas2009.tar.xz
Source276:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsc.tar.xz
Source277:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsc.doc.tar.xz
Source278:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/showtags.tar.xz
Source279:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/showtags.doc.tar.xz
Source280:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sort-by-letters.tar.xz
Source281:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sort-by-letters.doc.tar.xz
Source282:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splitbib.tar.xz
Source283:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splitbib.doc.tar.xz
Source284:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turabian-formatting.tar.xz
Source285:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turabian-formatting.doc.tar.xz
Source286:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uni-wtal-ger.tar.xz
Source287:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uni-wtal-ger.doc.tar.xz
Source288:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uni-wtal-lin.tar.xz
Source289:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uni-wtal-lin.doc.tar.xz
Source290:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/usebib.tar.xz
Source291:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/usebib.doc.tar.xz
Source292:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vak.tar.xz
Source293:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vak.doc.tar.xz
Source294:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/windycity.tar.xz
Source295:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/windycity.doc.tar.xz
Source296:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcite.tar.xz
Source297:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcite.doc.tar.xz
Source298:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zootaxa-bst.tar.xz
Source299:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zootaxa-bst.doc.tar.xz

# Patches
Patch0:         texlive-biblatex-abnt-no-l3regex.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-aaai-named
Requires:       texlive-aichej
Requires:       texlive-ajl
Requires:       texlive-amsrefs
Requires:       texlive-annotate
Requires:       texlive-apacite
Requires:       texlive-apalike-ejor
Requires:       texlive-apalike2
Requires:       texlive-archaeologie
Requires:       texlive-authordate
Requires:       texlive-beebe
Requires:       texlive-besjournals
Requires:       texlive-bestpapers
Requires:       texlive-bib2gls
Requires:       texlive-bib2qr
Requires:       texlive-bibarts
Requires:       texlive-bibbreeze
Requires:       texlive-bibcop
Requires:       biber
Requires:       texlive-bibexport
Requires:       texlive-bibhtml
Requires:       texlive-biblatex
Requires:       texlive-biblatex-abnt
Requires:       texlive-biblatex-ajc2020unofficial
Requires:       texlive-biblatex-anonymous
Requires:       texlive-biblatex-apa
Requires:       texlive-biblatex-apa6
Requires:       texlive-biblatex-archaeology
Requires:       texlive-biblatex-arthistory-bonn
Requires:       texlive-biblatex-bath
Requires:       texlive-biblatex-bookinarticle
Requires:       texlive-biblatex-bookinother
Requires:       texlive-biblatex-bwl
Requires:       texlive-biblatex-caspervector
Requires:       texlive-biblatex-chem
Requires:       texlive-biblatex-chicago
Requires:       texlive-biblatex-claves
Requires:       texlive-biblatex-cse
Requires:       texlive-biblatex-cv
Requires:       texlive-biblatex-dw
Requires:       texlive-biblatex-enc
Requires:       texlive-biblatex-ext
Requires:       texlive-biblatex-fiwi
Requires:       texlive-biblatex-gb7714-2015
Requires:       texlive-biblatex-german-legal
Requires:       texlive-biblatex-gost
Requires:       texlive-biblatex-historian
Requires:       texlive-biblatex-ieee
Requires:       texlive-biblatex-ijsra
Requires:       texlive-biblatex-iso690
Requires:       texlive-biblatex-jura2
Requires:       texlive-biblatex-juradiss
Requires:       texlive-biblatex-license
Requires:       texlive-biblatex-lncs
Requires:       texlive-biblatex-lni
Requires:       texlive-biblatex-luh-ipw
Requires:       texlive-biblatex-manuscripts-philology
Requires:       texlive-biblatex-mla
Requires:       texlive-biblatex-morenames
Requires:       texlive-biblatex-ms
Requires:       texlive-biblatex-multiple-dm
Requires:       texlive-biblatex-musuos
Requires:       texlive-biblatex-nature
Requires:       texlive-biblatex-nejm
Requires:       texlive-biblatex-nottsclassic
Requires:       texlive-biblatex-opcit-booktitle
Requires:       texlive-biblatex-oxref
Requires:       texlive-biblatex-philosophy
Requires:       texlive-biblatex-phys
Requires:       texlive-biblatex-publist
Requires:       texlive-biblatex-readbbl
Requires:       texlive-biblatex-realauthor
Requires:       texlive-biblatex-sbl
Requires:       texlive-biblatex-science
Requires:       texlive-biblatex-shortfields
Requires:       texlive-biblatex-socialscienceshuberlin
Requires:       texlive-biblatex-software
Requires:       texlive-biblatex-source-division
Requires:       texlive-biblatex-spbasic
Requires:       texlive-biblatex-subseries
Requires:       texlive-biblatex-swiss-legal
Requires:       texlive-biblatex-trad
Requires:       texlive-biblatex-true-citepages-omit
Requires:       texlive-biblatex-unified
Requires:       texlive-biblatex-vancouver
Requires:       texlive-biblatex2bibitem
Requires:       texlive-biblist
Requires:       texlive-bibtexperllibs
Requires:       texlive-bibtools
Requires:       texlive-bibtopic
Requires:       texlive-bibtopicprefix
Requires:       texlive-bibunits
Requires:       texlive-biolett-bst
Requires:       texlive-bookdb
Requires:       texlive-breakcites
Requires:       texlive-cell
Requires:       texlive-chbibref
Requires:       texlive-chembst
Requires:       texlive-chicago
Requires:       texlive-chicago-annote
Requires:       texlive-chicagoa
Requires:       texlive-chicagolinks
Requires:       texlive-chscite
Requires:       texlive-citation-style-language
Requires:       texlive-citeall
Requires:       texlive-citeref
Requires:       texlive-citeright
Requires:       texlive-collection-latex
Requires:       texlive-collref
Requires:       texlive-compactbib
Requires:       texlive-crossrefware
Requires:       texlive-custom-bib
Requires:       texlive-din1505
Requires:       texlive-dk-bib
Requires:       texlive-doipubmed
Requires:       texlive-ecobiblatex
Requires:       texlive-econ-bst
Requires:       texlive-economic
Requires:       texlive-fbs
Requires:       texlive-figbib
Requires:       texlive-footbib
Requires:       texlive-francais-bst
Requires:       texlive-gbt7714
Requires:       texlive-geschichtsfrkl
Requires:       texlive-harvard
Requires:       texlive-harvmac
Requires:       texlive-hep-bibliography
Requires:       texlive-historische-zeitschrift
Requires:       texlive-icite
Requires:       texlive-ietfbibs
Requires:       texlive-ijqc
Requires:       texlive-inlinebib
Requires:       texlive-iopart-num
Requires:       texlive-is-bst
Requires:       texlive-jbact
Requires:       texlive-jmb
Requires:       texlive-jneurosci
Requires:       texlive-jurabib
Requires:       texlive-ksfh_nat
Requires:       texlive-listbib
Requires:       texlive-logreq
Requires:       texlive-ltb2bib
Requires:       texlive-luabibentry
Requires:       texlive-margbib
Requires:       texlive-multibib
Requires:       texlive-multibibliography
Requires:       texlive-munich
Requires:       texlive-nar
Requires:       texlive-newcastle-bst
Requires:       texlive-nmbib
Requires:       texlive-notes2bib
Requires:       texlive-notex-bst
Requires:       texlive-oscola
Requires:       texlive-perception
Requires:       texlive-plainyr
Requires:       texlive-pnas2009
Requires:       texlive-rsc
Requires:       texlive-showtags
Requires:       texlive-sort-by-letters
Requires:       texlive-splitbib
Requires:       texlive-turabian-formatting
Requires:       texlive-uni-wtal-ger
Requires:       texlive-uni-wtal-lin
Requires:       texlive-urlbst
Requires:       texlive-usebib
Requires:       texlive-vak
Requires:       texlive-windycity
Requires:       texlive-xcite
Requires:       texlive-zootaxa-bst

%description
Additional BibTeX styles and bibliography data(bases), notably including
BibLaTeX.


%package -n texlive-aaai-named
Summary:        BibTeX style for AAAI
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-aaai-named
A BibTeX style derived from the standard master, presumably for use with the
aaai package.

%package -n texlive-aichej
Summary:        Bibliography style file for the AIChE Journal
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-aichej
The style was generated using custom-bib, and implements the style of the
American Institute of Chemical Engineers Journal (or AIChE Journal or AIChE J
or AIChEJ).

%package -n texlive-ajl
Summary:        BibTeX style for AJL
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ajl
Bibliographic style references in style of Australian Journal of Linguistics.

%package -n texlive-amsrefs
Summary:        A LaTeX-based replacement for BibTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(backref.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(url.sty)
Provides:       tex(amsbst.sty) = %{tl_version}
Provides:       tex(amsrefs.sty) = %{tl_version}
Provides:       tex(ifoption.sty) = %{tl_version}
Provides:       tex(mathscinet.sty) = %{tl_version}
Provides:       tex(pcatcode.sty) = %{tl_version}
Provides:       tex(rkeyval.sty) = %{tl_version}
Provides:       tex(textcmds.sty) = %{tl_version}

%description -n texlive-amsrefs
Amsrefs is a LaTeX package for bibliographies that provides an archival data
format similar to the format of BibTeX database files, but adapted to make
direct processing by LaTeX easier. The package can be used either in
conjunction with BibTeX or as a replacement for BibTeX.

%package -n texlive-annotate
Summary:        A bibliography style with annotations
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-annotate
The style is a derivative of the standard alpha style, which processes an
entry's annotate field as part of the printed output.

%package -n texlive-apacite
Summary:        Citation style following the rules of the APA
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(index.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Provides:       tex(apacdoc.sty) = %{tl_version}
Provides:       tex(apacite.sty) = %{tl_version}

%description -n texlive-apacite
Apacite provides a BibTeX style and a LaTeX package which are designed to match
the requirements of the American Psychological Association's style for
citations. The package follows the 6th edition of the APA manual, and is
designed to work with the apa6 class. A test document is provided. The package
is compatible with chapterbib and (to some extent) with hyperref (for limits of
compatibility, see the documentation). The package also includes a means of
generating an author index for a document.

%package -n texlive-apalike-ejor
Summary:        A BibTeX style file for the European Journal of Operational Research
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-apalike-ejor
This package contains a BibTeX style file, apalike-ejor.bst, made to follow the
European Journal of Operational Research reference style guidelines. It is a
fork of apalike version 0.99a, by Oren Patashnik, and consists of minor
modifications of standard APA style. Among other changes it adds support for
hyperlinked URL and DOI fields (which requires hyperref).

%package -n texlive-apalike2
Summary:        Bibliography style that approaches APA requirements
Version:        svn76790
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-apalike2
Described as a "local adaptation" of apalike (which is part of the base BibTeX
distribution).

%package -n texlive-archaeologie
Summary:        A citation-style which covers rules of the German Archaeological Institute
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(standard.bbx)
Requires:       tex(ulem.sty)
Provides:       tex(archaeologie.bbx) = %{tl_version}
Provides:       tex(archaeologie.cbx) = %{tl_version}

%description -n texlive-archaeologie
This citation-style covers the citation and bibliography rules of the German
Archaeological Institute (DAI). Various options are available to change and
adjust the outcome according to one's own preferences.

%package -n texlive-authordate
Summary:        Author/date style citation styles
Version:        svn77677
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(authordate1-4.sty) = %{tl_version}

%description -n texlive-authordate
Authordate produces styles loosely based on the recommendations of British
Standard 1629(1976), Butcher's Copy-editing and the Chicago Manual of Style.
The bundle provides four BibTeX styles (authordate1, ..., authordate4), and a
LaTeX package, for citation in author/date style. The BibTeX styles differ in
how they format names and titles; one of them is necessary for the LaTeX
package to work.

%package -n texlive-beebe
Summary:        A collection of bibliographies
Version:        svn77590
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bibnames.sty) = %{tl_version}
Provides:       tex(texnames.sty) = %{tl_version}
Provides:       tex(tugboat.def) = %{tl_version}

%description -n texlive-beebe
A collection of BibTeX bibliographies on TeX-related topics (including, for
example, spell-checking and SGML). Each includes a LaTeX wrapper file to
typeset the bibliography.

%package -n texlive-besjournals
Summary:        Bibliographies suitable for British Ecological Society journals
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-besjournals
The package provides a BibTeX style for use with journals published by the
British Ecological Society. The style was produced independently of the
Society, and has no formal approval by the BES.

%package -n texlive-bestpapers
Summary:        A BibTeX package to produce lists of authors' best papers
Version:        svn76790
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bestpapers
Many people preparing their resumes find the requirement "please list five (or
six, or ten) papers authored by you". The same requirement is often stated for
reports prepared by professional teams. The creation of such lists may be a
cumbersome task. Even more difficult is it to support such lists over the time,
when new papers are added. The BibTeX style bestpapers.bst is intended to
facilitate this task. It is based on the idea that it is easier to score than
to sort: We can assign a score to a paper and then let the computer select the
papers with highest scores. This work was commissioned by the Consumer
Financial Protection Bureau, United States Treasury. This package is in the
public domain.

%package -n texlive-bib2qr
Summary:        Cite BibTeX entries with QR codes
Version:        svn71940
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(qrcode.sty)
Requires:       tex(xstring.sty)
Provides:       tex(bib2qr.sty) = %{tl_version}

%description -n texlive-bib2qr
This package provides functionality to cite BibTeX entries with QR codes for
easy sharing and referencing. The target of the QR code is the entry's digital
object identifier (DOI), or URL if no DOI exists. It is realised via the LaTeX
packages biblatex and qrcode.

%package -n texlive-bibarts
Summary:        "Arts"-style bibliographical information
Version:        svn74384
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bibarts.sty) = %{tl_version}

%description -n texlive-bibarts
BibArts is a LaTeX package to assist in making bibliographical features common
in the arts and the humanities (history, political science, philosophy, etc.).
bibarts.sty provides commands for quotations, abbreviations, and especially for
a formatted citation of literature, journals (periodicals), edited sources, and
archive sources. In difference to earlier versions, BibArts 2.x helps to use
slanted fonts (italics) and is able to set ibidem automatically in footnotes.
It will also copy all citation information, abbreviations, and register key
words into lists for an automatically generated appendix. These lists may refer
to page and footnote numbers. BibArts has nothing to do with BibTeX. The lists
are created by bibsort (see below). BibArts requires the program bibsort, for
which the sources and a Windows executable are provided. This program creates
the bibliography without using MakeIndex or BibTeX. Its source is not written
with any specific operating system in mind. A summary of contents is in
English; the full documentation is in German.

%package -n texlive-bibbreeze
Summary:        A referencing package for automatically reconstructing bibliography data
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric.bbx)
Provides:       tex(BibBreeze.bbx) = %{tl_version}

%description -n texlive-bibbreeze
This LaTeX package, called BibBreeze written using LaTeX3, is a referencing
package that automates bibliography reconstruction, eliminating manual effort
in reference handling. It reorders disorganized fields for bibliography
entries, fills in missing fields, and produces polished, referencing
style-compliant bibliographies--optimized for researchers, academics, and
writers. Currently, the package's referencing style is designed for APA (with
both numeric and author-year in-text citations) with more styles (Harvard,
Chicago, AMA, etc.) to come.

%package -n texlive-bibhtml
Summary:        BibTeX support for HTML files
Version:        svn31607
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bibhtml
Bibhtml consists of a Perl script and a set of BibTeX style files, which
together allow you to output a bibliography as a collection of HTML files. The
references in the text are linked directly to the corresponding bibliography
entry, and if a URL is defined in the entry within the BibTeX database file,
then the generated bibliography entry is linked to this. The package provides
three different style files derived from each of the standard plain.bst and
alpha.bst, as well as two style files derived from abbrv.bst and unsrt.bst
(i.e., eight in total).

%package -n texlive-biblatex
Summary:        Sophisticated Bibliographies in LaTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       texlive-kvoptions
Requires:       texlive-logreq
Requires:       texlive-pdftexcmds
Requires:       texlive-url
Requires:       biber
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(logreq.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(url.sty)
Requires:       tex(xparse.sty)
Provides:       tex(alphabetic-verb.bbx) = %{tl_version}
Provides:       tex(alphabetic-verb.cbx) = %{tl_version}
Provides:       tex(alphabetic.bbx) = %{tl_version}
Provides:       tex(alphabetic.cbx) = %{tl_version}
Provides:       tex(authortitle-comp.bbx) = %{tl_version}
Provides:       tex(authortitle-comp.cbx) = %{tl_version}
Provides:       tex(authortitle-ibid.bbx) = %{tl_version}
Provides:       tex(authortitle-ibid.cbx) = %{tl_version}
Provides:       tex(authortitle-icomp.bbx) = %{tl_version}
Provides:       tex(authortitle-icomp.cbx) = %{tl_version}
Provides:       tex(authortitle-tcomp.bbx) = %{tl_version}
Provides:       tex(authortitle-tcomp.cbx) = %{tl_version}
Provides:       tex(authortitle-terse.bbx) = %{tl_version}
Provides:       tex(authortitle-terse.cbx) = %{tl_version}
Provides:       tex(authortitle-ticomp.bbx) = %{tl_version}
Provides:       tex(authortitle-ticomp.cbx) = %{tl_version}
Provides:       tex(authortitle.bbx) = %{tl_version}
Provides:       tex(authortitle.cbx) = %{tl_version}
Provides:       tex(authoryear-comp.bbx) = %{tl_version}
Provides:       tex(authoryear-comp.cbx) = %{tl_version}
Provides:       tex(authoryear-ibid.bbx) = %{tl_version}
Provides:       tex(authoryear-ibid.cbx) = %{tl_version}
Provides:       tex(authoryear-icomp.bbx) = %{tl_version}
Provides:       tex(authoryear-icomp.cbx) = %{tl_version}
Provides:       tex(authoryear.bbx) = %{tl_version}
Provides:       tex(authoryear.cbx) = %{tl_version}
Provides:       tex(biblatex.def) = %{tl_version}
Provides:       tex(biblatex.sty) = %{tl_version}
Provides:       tex(blx-bibtex.def) = %{tl_version}
Provides:       tex(blx-case-expl3.sty) = %{tl_version}
Provides:       tex(blx-case-latex2e.sty) = %{tl_version}
Provides:       tex(blx-compat.def) = %{tl_version}
Provides:       tex(blx-dm.def) = %{tl_version}
Provides:       tex(blx-mcite.def) = %{tl_version}
Provides:       tex(blx-natbib.def) = %{tl_version}
Provides:       tex(blx-unicode.def) = %{tl_version}
Provides:       tex(debug.bbx) = %{tl_version}
Provides:       tex(debug.cbx) = %{tl_version}
Provides:       tex(draft.bbx) = %{tl_version}
Provides:       tex(draft.cbx) = %{tl_version}
Provides:       tex(numeric-comp.bbx) = %{tl_version}
Provides:       tex(numeric-comp.cbx) = %{tl_version}
Provides:       tex(numeric-verb.bbx) = %{tl_version}
Provides:       tex(numeric-verb.cbx) = %{tl_version}
Provides:       tex(numeric.bbx) = %{tl_version}
Provides:       tex(numeric.cbx) = %{tl_version}
Provides:       tex(reading.bbx) = %{tl_version}
Provides:       tex(reading.cbx) = %{tl_version}
Provides:       tex(standard.bbx) = %{tl_version}
Provides:       tex(verbose-ibid.bbx) = %{tl_version}
Provides:       tex(verbose-ibid.cbx) = %{tl_version}
Provides:       tex(verbose-inote.bbx) = %{tl_version}
Provides:       tex(verbose-inote.cbx) = %{tl_version}
Provides:       tex(verbose-note.bbx) = %{tl_version}
Provides:       tex(verbose-note.cbx) = %{tl_version}
Provides:       tex(verbose-trad1.bbx) = %{tl_version}
Provides:       tex(verbose-trad1.cbx) = %{tl_version}
Provides:       tex(verbose-trad2.bbx) = %{tl_version}
Provides:       tex(verbose-trad2.cbx) = %{tl_version}
Provides:       tex(verbose-trad3.bbx) = %{tl_version}
Provides:       tex(verbose-trad3.cbx) = %{tl_version}
Provides:       tex(verbose.bbx) = %{tl_version}
Provides:       tex(verbose.cbx) = %{tl_version}

%description -n texlive-biblatex
BibLaTeX is a complete reimplementation of the bibliographic facilities
provided by LaTeX. Formatting of the bibliography is entirely controlled by
LaTeX macros, and a working knowledge of LaTeX should be sufficient to design
new bibliography and citation styles. BibLaTeX uses its own data backend
program called "biber" to read and process the bibliographic data. With biber,
BibLaTeX has many features rivalling or surpassing other bibliography systems.
To mention a few: Full Unicode support Highly customisable sorting using the
Unicode Collation Algorithm + CLDR tailoring Highly customisable bibliography
labels Complex macro-based on-the-fly data modification without changing your
data sources A tool mode for transforming bibliographic data sources Multiple
bibliographies and lists of bibliographic information in the same document with
different sorting Highly customisable data source inheritance rules Polyglossia
and babel support for automatic language switching for bibliographic entries
and citations Automatic bibliography data recoding (UTF-8 -> latin1, LaTeX
macros -> UTF-8 etc) Remote data sources Highly sophisticated automatic name
and name list disambiguation system Highly customisable data model so users can
define their own bibliographic data types Validation of bibliographic data
against a data model Subdivided and/or filtered bibliographies, bibliographies
per chapter, section etc. Apart from the features unique to BibLaTeX, the
package also incorporates core features of the following packages: babelbib,
bibtopic, bibunits, chapterbib, cite, inlinebib, mcite and mciteplus, mlbib,
multibib, splitbib. The package strictly requires e-TeX BibTeX, bibtex8, or
Biber etoolbox 2.1 or later logreq 1.0 or later keyval ifthen url Biber, babel
/ polyglossia, and csquotes 4.4 or later are strongly recommended.

%package -n texlive-biblatex-abnt
Summary:        BibLaTeX style for Brazil's ABNT rules
Version:        svn72565
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.cbx)
Requires:       biber
Requires:       tex(numeric.cbx)
Requires:       tex(standard.bbx)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(abnt-ibid.bbx) = %{tl_version}
Provides:       tex(abnt-ibid.cbx) = %{tl_version}
Provides:       tex(abnt-numeric.bbx) = %{tl_version}
Provides:       tex(abnt-numeric.cbx) = %{tl_version}
Provides:       tex(abnt.bbx) = %{tl_version}
Provides:       tex(abnt.cbx) = %{tl_version}

%description -n texlive-biblatex-abnt
This package offers a BibLaTeX style for Brazil's ABNT (Brazilian Association
of Technical Norms) rules.

%package -n texlive-biblatex-ajc2020unofficial
Summary:        BibLaTeX style for the Australasian Journal of Combinatorics
Version:        svn54401
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
Requires:       tex(shortmathj.sty)
Requires:       tex(standard.bbx)
Provides:       tex(ajc2020unofficial.bbx) = %{tl_version}
Provides:       tex(ajc2020unofficial.cbx) = %{tl_version}

%description -n texlive-biblatex-ajc2020unofficial
This is an unofficial BibLaTeX style for the Australasian Journal of
Combinatorics. Note that the journal (as for 01 March 2020) does not accept
BibLaTeX, so you probably want to use biblatex2bibitem.

%package -n texlive-biblatex-anonymous
Summary:        A tool to manage anonymous work with BibLaTeX
Version:        svn48548
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(biblatex-anonymous.sty) = %{tl_version}

%description -n texlive-biblatex-anonymous
The package provides tools to help manage anonymous work with BibLaTeX. It will
be useful, for example, in history or classical philology.

%package -n texlive-biblatex-apa
Summary:        BibLaTeX citation and reference style for APA
Version:        svn76158
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(standard.bbx)
Provides:       tex(apa.bbx) = %{tl_version}
Provides:       tex(apa.cbx) = %{tl_version}

%description -n texlive-biblatex-apa
This is a fairly complete BibLaTeX style (citations and references) for APA
(American Psychological Association) publications. It implements and automates
most of the guidelines in the APA 7th edition style guide for citations and
references. An example document is also given which typesets every citation and
reference example in the APA 7th edition style guide. This version of the
package requires use of csquotes [?]4.3, BibLaTeX [?]3.4, and the biber backend
for BibLaTeX [?]2.5.

%package -n texlive-biblatex-apa6
Summary:        BibLaTeX citation and reference style for APA 6th Edition
Version:        svn56209
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(standard.bbx)
Provides:       tex(apa6.bbx) = %{tl_version}
Provides:       tex(apa6.cbx) = %{tl_version}

%description -n texlive-biblatex-apa6
This is a fairly complete BibLaTeX style (citations and references) for APA
(American Psychological Association) 6th Edition conformant publications. It
implements and automates most of the guidelines in the APA 6th edition style
guide for citations and references. An example document is also given which
typesets every citation and reference example in the APA 6th edition style
guide. This is a legacy style for 6th Edition documents. Please use the
BibLaTeX-apa style package for the latest APA edition conformance.

%package -n texlive-biblatex-archaeology
Summary:        A collection of BibLaTeX styles for German prehistory
Version:        svn53281
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear-ibid.bbx)
Requires:       tex(authoryear-ibid.cbx)
Requires:       tex(authoryear-icomp.bbx)
Requires:       tex(authoryear-icomp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       biber
Requires:       tex(calc.sty)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(tabulary.sty)
Requires:       tex(verbose-ibid.bbx)
Requires:       tex(verbose-ibid.cbx)
Requires:       tex(verbose-trad2.bbx)
Requires:       tex(verbose-trad2.cbx)
Requires:       tex(verbose.bbx)
Requires:       tex(verbose.cbx)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(aefkw.bbx) = %{tl_version}
Provides:       tex(aefkw.cbx) = %{tl_version}
Provides:       tex(afwl.bbx) = %{tl_version}
Provides:       tex(afwl.cbx) = %{tl_version}
Provides:       tex(amit.bbx) = %{tl_version}
Provides:       tex(amit.cbx) = %{tl_version}
Provides:       tex(archa.bbx) = %{tl_version}
Provides:       tex(archa.cbx) = %{tl_version}
Provides:       tex(authoryear-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-archaeology.cbx) = %{tl_version}
Provides:       tex(authoryear-comp-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-comp-archaeology.cbx) = %{tl_version}
Provides:       tex(authoryear-ibid-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-ibid-archaeology.cbx) = %{tl_version}
Provides:       tex(authoryear-icomp-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-icomp-archaeology.cbx) = %{tl_version}
Provides:       tex(biblatex-archaeology.sty) = %{tl_version}
Provides:       tex(dguf-alt.bbx) = %{tl_version}
Provides:       tex(dguf-alt.cbx) = %{tl_version}
Provides:       tex(dguf-apa.bbx) = %{tl_version}
Provides:       tex(dguf-apa.cbx) = %{tl_version}
Provides:       tex(dguf.bbx) = %{tl_version}
Provides:       tex(dguf.cbx) = %{tl_version}
Provides:       tex(eaz-alt.bbx) = %{tl_version}
Provides:       tex(eaz-alt.cbx) = %{tl_version}
Provides:       tex(eaz.bbx) = %{tl_version}
Provides:       tex(eaz.cbx) = %{tl_version}
Provides:       tex(foe.bbx) = %{tl_version}
Provides:       tex(foe.cbx) = %{tl_version}
Provides:       tex(jb-halle.bbx) = %{tl_version}
Provides:       tex(jb-halle.cbx) = %{tl_version}
Provides:       tex(jb-kreis-neuss.bbx) = %{tl_version}
Provides:       tex(jb-kreis-neuss.cbx) = %{tl_version}
Provides:       tex(karl.bbx) = %{tl_version}
Provides:       tex(karl.cbx) = %{tl_version}
Provides:       tex(kunde.bbx) = %{tl_version}
Provides:       tex(kunde.cbx) = %{tl_version}
Provides:       tex(maja.bbx) = %{tl_version}
Provides:       tex(maja.cbx) = %{tl_version}
Provides:       tex(mpk.bbx) = %{tl_version}
Provides:       tex(mpk.cbx) = %{tl_version}
Provides:       tex(mpkoeaw.bbx) = %{tl_version}
Provides:       tex(mpkoeaw.cbx) = %{tl_version}
Provides:       tex(niedersachsen.bbx) = %{tl_version}
Provides:       tex(niedersachsen.cbx) = %{tl_version}
Provides:       tex(nnu.bbx) = %{tl_version}
Provides:       tex(nnu.cbx) = %{tl_version}
Provides:       tex(numeric-comp-archaeology.bbx) = %{tl_version}
Provides:       tex(numeric-comp-archaeology.cbx) = %{tl_version}
Provides:       tex(offa.bbx) = %{tl_version}
Provides:       tex(offa.cbx) = %{tl_version}
Provides:       tex(rgk-inline-old.bbx) = %{tl_version}
Provides:       tex(rgk-inline-old.cbx) = %{tl_version}
Provides:       tex(rgk-inline.bbx) = %{tl_version}
Provides:       tex(rgk-inline.cbx) = %{tl_version}
Provides:       tex(rgk-numeric-old.bbx) = %{tl_version}
Provides:       tex(rgk-numeric-old.cbx) = %{tl_version}
Provides:       tex(rgk-numeric.bbx) = %{tl_version}
Provides:       tex(rgk-numeric.cbx) = %{tl_version}
Provides:       tex(rgk-verbose-old.bbx) = %{tl_version}
Provides:       tex(rgk-verbose-old.cbx) = %{tl_version}
Provides:       tex(rgk-verbose.bbx) = %{tl_version}
Provides:       tex(rgk-verbose.cbx) = %{tl_version}
Provides:       tex(rgzm-inline.bbx) = %{tl_version}
Provides:       tex(rgzm-inline.cbx) = %{tl_version}
Provides:       tex(rgzm-numeric.bbx) = %{tl_version}
Provides:       tex(rgzm-numeric.cbx) = %{tl_version}
Provides:       tex(rgzm-verbose.bbx) = %{tl_version}
Provides:       tex(rgzm-verbose.cbx) = %{tl_version}
Provides:       tex(ufg-muenster-inline.bbx) = %{tl_version}
Provides:       tex(ufg-muenster-inline.cbx) = %{tl_version}
Provides:       tex(ufg-muenster-numeric.bbx) = %{tl_version}
Provides:       tex(ufg-muenster-numeric.cbx) = %{tl_version}
Provides:       tex(ufg-muenster-verbose.bbx) = %{tl_version}
Provides:       tex(ufg-muenster-verbose.cbx) = %{tl_version}
Provides:       tex(verbose-archaeology.bbx) = %{tl_version}
Provides:       tex(verbose-archaeology.cbx) = %{tl_version}
Provides:       tex(verbose-ibid-archaeology.bbx) = %{tl_version}
Provides:       tex(verbose-ibid-archaeology.cbx) = %{tl_version}
Provides:       tex(verbose-trad2note-archaeology.bbx) = %{tl_version}
Provides:       tex(verbose-trad2note-archaeology.cbx) = %{tl_version}
Provides:       tex(volkskunde.bbx) = %{tl_version}
Provides:       tex(volkskunde.cbx) = %{tl_version}
Provides:       tex(zaak.bbx) = %{tl_version}
Provides:       tex(zaak.cbx) = %{tl_version}
Provides:       tex(zaes.bbx) = %{tl_version}
Provides:       tex(zaes.cbx) = %{tl_version}

%description -n texlive-biblatex-archaeology
This package provides additional BibLaTeX styles for German humanities. Its
core purpose is to enable the referencing rules of the Romano-Germanic
Commission (>Romisch-Germanische Kommission), the department of prehistory of
the German Archaeological Institute (Deutsches Archaologisches Institut), since
these are referenced by most guidelines in German prehistory and medieval
archaeology and serve as a kind of template. biblatex-archaeology provides
verbose, numeric and author date styles as well and adaptions to specific
document types like exhibition and auction catalogues.

%package -n texlive-biblatex-arthistory-bonn
Summary:        BibLaTeX citation style covers the citation and bibliography guidelines for art historians
Version:        svn46637
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-ibid.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(csquotes.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(arthistory-bonn.bbx) = %{tl_version}
Provides:       tex(arthistory-bonn.cbx) = %{tl_version}

%description -n texlive-biblatex-arthistory-bonn
This citation style covers the citation and bibliography guidelines of the
Kunsthistorisches Institut der Universitat Bonn for undergraduates. It
introduces bibliography entry types for catalogs and features a tabular
bibliography, among other things. Various options are available to change and
adjust the outcome according to one's own preferences. The style is compatible
with English and German.

%package -n texlive-biblatex-bath
Summary:        Harvard referencing style as recommended by the University of Bath Library
Version:        svn77530
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(etoolbox.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(bath.bbx) = %{tl_version}
Provides:       tex(bath.cbx) = %{tl_version}

%description -n texlive-biblatex-bath
This package provides a BibTeX style to format reference lists in the Harvard
style recommended by the University of Bath Library. It should be used in
conjunction with natbib for citations.

%package -n texlive-biblatex-bookinarticle
Summary:        Manage book edited in article
Version:        svn40323
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(biblatex-bookinarticle.sty) = %{tl_version}

%description -n texlive-biblatex-bookinarticle
This package provides three new BibLaTeX entry types - @bookinarticle,
@bookinincollection and @bookinthesis - to refer to a modern edition of an old
book, where this modern edition is provided in a @article, @incollection or in
a @thesis. The package is now superseded by biblatex-bookinother.

%package -n texlive-biblatex-bookinother
Summary:        Manage book edited in other entry type
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(verbose.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(bookinother.bbx) = %{tl_version}

%description -n texlive-biblatex-bookinother
This package provides new BibLaTeX entry types and fields for book edited in
other types, like for instance @bookinarticle. It offers more types than the
older package biblatex-bookinarticle which it supersedes.

%package -n texlive-biblatex-bwl
Summary:        BibLaTeX citations for FU Berlin
Version:        svn26556
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Provides:       tex(bwl-FU.bbx) = %{tl_version}
Provides:       tex(bwl-FU.cbx) = %{tl_version}

%description -n texlive-biblatex-bwl
The bundle provides a set of BibLaTeX implementations of bibliography and
citation styles for the Business Administration Department of the Free
University of Berlin.

%package -n texlive-biblatex-caspervector
Summary:        A simple citation style for Chinese users
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Provides:       tex(blx-caspervector-base.def) = %{tl_version}
Provides:       tex(blx-caspervector-gbk.def) = %{tl_version}
Provides:       tex(blx-caspervector-utf8.def) = %{tl_version}
Provides:       tex(caspervector-ay.bbx) = %{tl_version}
Provides:       tex(caspervector-ay.cbx) = %{tl_version}
Provides:       tex(caspervector.bbx) = %{tl_version}
Provides:       tex(caspervector.cbx) = %{tl_version}

%description -n texlive-biblatex-caspervector
The package provides a simple and easily extensible bibliography/citation style
for Chinese LaTeX users, using BibLaTeX.

%package -n texlive-biblatex-chem
Summary:        A set of BibLaTeX implementations of chemistry-related bibliography styles
Version:        svn76236
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Provides:       tex(chem-acs.bbx) = %{tl_version}
Provides:       tex(chem-acs.cbx) = %{tl_version}
Provides:       tex(chem-angew.bbx) = %{tl_version}
Provides:       tex(chem-angew.cbx) = %{tl_version}
Provides:       tex(chem-biochem.bbx) = %{tl_version}
Provides:       tex(chem-biochem.cbx) = %{tl_version}
Provides:       tex(chem-rsc.bbx) = %{tl_version}
Provides:       tex(chem-rsc.cbx) = %{tl_version}

%description -n texlive-biblatex-chem
The bundle offers a set of styles to allow chemists to use BibLaTeX. The
package has complete styles for: all ACS journals; RSC journals using standard
(Chem. Commun.) style; and Angewandte Chem. style, (thus covering a wide range
of journals). A comprehensive set of examples of use is included.

%package -n texlive-biblatex-chicago
Summary:        Chicago style files for BibLaTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Requires:       tex(endnotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(refcount.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(biblatex-chicago.sty) = %{tl_version}
Provides:       tex(chicago-authordate-trad.bbx) = %{tl_version}
Provides:       tex(chicago-authordate-trad.cbx) = %{tl_version}
Provides:       tex(chicago-authordate-trad16.bbx) = %{tl_version}
Provides:       tex(chicago-authordate-trad16.cbx) = %{tl_version}
Provides:       tex(chicago-authordate.bbx) = %{tl_version}
Provides:       tex(chicago-authordate.cbx) = %{tl_version}
Provides:       tex(chicago-authordate16.bbx) = %{tl_version}
Provides:       tex(chicago-authordate16.cbx) = %{tl_version}
Provides:       tex(chicago-dates-common.cbx) = %{tl_version}
Provides:       tex(chicago-dates-common16.cbx) = %{tl_version}
Provides:       tex(chicago-notes.bbx) = %{tl_version}
Provides:       tex(chicago-notes.cbx) = %{tl_version}
Provides:       tex(chicago-notes16.bbx) = %{tl_version}
Provides:       tex(chicago-notes16.cbx) = %{tl_version}
Provides:       tex(cmsdocs.sty) = %{tl_version}
Provides:       tex(cmsendnotes.sty) = %{tl_version}

%description -n texlive-biblatex-chicago
This is a BibLaTeX style that implements the Chicago 'author-date' and 'notes
with bibliography' style specifications given in the Chicago Manual of Style,
17th edition (with continuing support for the 16th edition, too). The style
implements entry types for citing audio-visual materials, among many others.
The package was previously known as biblatex-chicago-notes-df.

%package -n texlive-biblatex-claves
Summary:        A tool to manage claves of old literature with BibLaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(verbose.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(claves.bbx) = %{tl_version}

%description -n texlive-biblatex-claves
When studying antique and medieval literature, we may find many different texts
published with the same title, or, in contrary, the same text published with
different titles. To avoid confusion, scholars have published claves, which are
books listing ancient texts, identifying them by an identifier -- a number or a
string of text. For example, for early Christianity, we have the Bibliotheca
Hagiographica Graeca, the Clavis Apocryphorum Novi Testamenti and other claves.
It could be useful to print the identifier of a texts in one specific clavis,
or in many claves. The package allows us to create new field for different
claves, and to present all these fields in a consistent way.

%package -n texlive-biblatex-cse
Summary:        Council of Science Editors (CSE) style file for BibLaTeX
Version:        svn76777
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.cbx)
Requires:       tex(standard.bbx)
Provides:       tex(biblatex-cse.bbx) = %{tl_version}
Provides:       tex(biblatex-cse.cbx) = %{tl_version}

%description -n texlive-biblatex-cse
This is a BibLaTeX style that implements the bibliography style of the Council
of Science Editors (CSE) for BibLaTeX. I did this style file by request of a
user of my LaTeX template novathesis. He was quite thorough, double and triple
checking that the output was conforming to the requirements of his University
(Faculty of Veterinary from the University of Lisbon). Although this
biblatex-cse style served the requirements from his University, there may still
be some unconformities to the CSE style. If you find any, please open an issue
in the project's page on GitHub or, even better, submit a pull request.

%package -n texlive-biblatex-cv
Summary:        Create a CV from BibTeX files
Version:        svn59433
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(biblatex.sty)
Requires:       tex(datenumber.sty)
Requires:       tex(fp.sty)
Requires:       tex(totcount.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(biblatex-cv.bbx) = %{tl_version}
Provides:       tex(biblatex-cv.cbx) = %{tl_version}
Provides:       tex(biblatex-cv.sty) = %{tl_version}

%description -n texlive-biblatex-cv
This package creates an academic curriculum vitae (CV) from a BibTeX .bib file.
The package makes use of BibLaTeX/biber to automatically format, group, and
sort the entries on a CV.

%package -n texlive-biblatex-dw
Summary:        Humanities styles for BibLaTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(standard.bbx)
Provides:       tex(authortitle-dw.bbx) = %{tl_version}
Provides:       tex(authortitle-dw.cbx) = %{tl_version}
Provides:       tex(footnote-dw.bbx) = %{tl_version}
Provides:       tex(footnote-dw.cbx) = %{tl_version}
Provides:       tex(standard-dw.bbx) = %{tl_version}
Provides:       tex(standard-dw.cbx) = %{tl_version}

%description -n texlive-biblatex-dw
A small collection of styles for the BibLaTeX package. It was designed for
citations in the humanities and offers some features that are not provided by
the standard BibLaTeX styles. The styles are dependent on BibLaTeX (at least
version 0.9b) and cannot be used without it. Eine kleine Sammlung von Stilen
fur das Paket BibLaTeX. Es ist auf geisteswissenschaftliche Zitierweise
zugeschnitten und bietet einige Funktionen, die von den Standard-Stilen von
BibLaTeX nicht direkt bereitgestellt werden. Das Paket baut vollstandig auf
BibLaTeX auf und kann nicht ohne BibLaTeX (mindestens in der Version 0.9b)
verwendet werden.

%package -n texlive-biblatex-enc
Summary:        BibLaTeX style for the Ecole nationale des chartes (Paris)
Version:        svn73019
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(enc.bbx) = %{tl_version}
Provides:       tex(enc.cbx) = %{tl_version}

%description -n texlive-biblatex-enc
This package provides a citation and bibliography style for use with BibLaTeX.
It conforms to the bibliographic standards used at the Ecole nationale des
chartes (Paris), and may be suitable for a more general use in historical and
philological works. The package was initially derived from
historische-zeitschrift, with the necessary modifications.

%package -n texlive-biblatex-ext
Summary:        Extended BibLaTeX standard styles
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authortitle-comp.bbx)
Requires:       tex(authortitle-comp.cbx)
Requires:       tex(authortitle-ibid.bbx)
Requires:       tex(authortitle-ibid.cbx)
Requires:       tex(authortitle-icomp.bbx)
Requires:       tex(authortitle-icomp.cbx)
Requires:       tex(authortitle-tcomp.bbx)
Requires:       tex(authortitle-terse.bbx)
Requires:       tex(authortitle-ticomp.bbx)
Requires:       tex(authortitle.bbx)
Requires:       tex(authortitle.cbx)
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear-ibid.bbx)
Requires:       tex(authoryear-ibid.cbx)
Requires:       tex(authoryear-icomp.bbx)
Requires:       tex(authoryear-icomp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(biblatex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(numeric-verb.bbx)
Requires:       tex(numeric-verb.cbx)
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
Requires:       tex(standard.bbx)
Requires:       tex(tikz.sty)
Requires:       tex(verbose-ibid.bbx)
Requires:       tex(verbose-ibid.cbx)
Requires:       tex(verbose-inote.bbx)
Requires:       tex(verbose-inote.cbx)
Requires:       tex(verbose-note.bbx)
Requires:       tex(verbose-note.cbx)
Requires:       tex(verbose-trad1.bbx)
Requires:       tex(verbose-trad1.cbx)
Requires:       tex(verbose-trad2.bbx)
Requires:       tex(verbose-trad2.cbx)
Requires:       tex(verbose-trad3.bbx)
Requires:       tex(verbose-trad3.cbx)
Requires:       tex(verbose.bbx)
Requires:       tex(verbose.cbx)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xsavebox.sty)
Provides:       tex(biblatex-ext-oa-doiapi.sty) = %{tl_version}
Provides:       tex(biblatex-ext-oa.sty) = %{tl_version}
Provides:       tex(biblatex-ext-oasymb-l3draw.sty) = %{tl_version}
Provides:       tex(biblatex-ext-oasymb-pict2e.sty) = %{tl_version}
Provides:       tex(biblatex-ext-oasymb-tikz.sty) = %{tl_version}
Provides:       tex(biblatex-ext-tabular.sty) = %{tl_version}
Provides:       tex(ext-alphabetic-verb.bbx) = %{tl_version}
Provides:       tex(ext-alphabetic-verb.cbx) = %{tl_version}
Provides:       tex(ext-alphabetic.bbx) = %{tl_version}
Provides:       tex(ext-alphabetic.cbx) = %{tl_version}
Provides:       tex(ext-authornumber-comp.bbx) = %{tl_version}
Provides:       tex(ext-authornumber-comp.cbx) = %{tl_version}
Provides:       tex(ext-authornumber-ecomp.bbx) = %{tl_version}
Provides:       tex(ext-authornumber-ecomp.cbx) = %{tl_version}
Provides:       tex(ext-authornumber-tcomp.bbx) = %{tl_version}
Provides:       tex(ext-authornumber-tcomp.cbx) = %{tl_version}
Provides:       tex(ext-authornumber-tecomp.bbx) = %{tl_version}
Provides:       tex(ext-authornumber-tecomp.cbx) = %{tl_version}
Provides:       tex(ext-authornumber-terse.bbx) = %{tl_version}
Provides:       tex(ext-authornumber-terse.cbx) = %{tl_version}
Provides:       tex(ext-authornumber.bbx) = %{tl_version}
Provides:       tex(ext-authornumber.cbx) = %{tl_version}
Provides:       tex(ext-authortitle-common.bbx) = %{tl_version}
Provides:       tex(ext-authortitle-comp.bbx) = %{tl_version}
Provides:       tex(ext-authortitle-comp.cbx) = %{tl_version}
Provides:       tex(ext-authortitle-ibid.bbx) = %{tl_version}
Provides:       tex(ext-authortitle-ibid.cbx) = %{tl_version}
Provides:       tex(ext-authortitle-icomp.bbx) = %{tl_version}
Provides:       tex(ext-authortitle-icomp.cbx) = %{tl_version}
Provides:       tex(ext-authortitle-tcomp.bbx) = %{tl_version}
Provides:       tex(ext-authortitle-tcomp.cbx) = %{tl_version}
Provides:       tex(ext-authortitle-terse.bbx) = %{tl_version}
Provides:       tex(ext-authortitle-terse.cbx) = %{tl_version}
Provides:       tex(ext-authortitle-ticomp.bbx) = %{tl_version}
Provides:       tex(ext-authortitle-ticomp.cbx) = %{tl_version}
Provides:       tex(ext-authortitle.bbx) = %{tl_version}
Provides:       tex(ext-authortitle.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-common.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-comp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-comp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-ecomp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-ecomp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-ibid.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-ibid.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-icomp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-icomp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-iecomp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-iecomp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-tcomp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-tcomp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-tecomp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-tecomp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-terse.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-terse.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-ticomp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-ticomp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear-tiecomp.bbx) = %{tl_version}
Provides:       tex(ext-authoryear-tiecomp.cbx) = %{tl_version}
Provides:       tex(ext-authoryear.bbx) = %{tl_version}
Provides:       tex(ext-authoryear.cbx) = %{tl_version}
Provides:       tex(ext-biblatex-aux.def) = %{tl_version}
Provides:       tex(ext-dashed-common.bbx) = %{tl_version}
Provides:       tex(ext-numeric-comp.bbx) = %{tl_version}
Provides:       tex(ext-numeric-comp.cbx) = %{tl_version}
Provides:       tex(ext-numeric-verb.bbx) = %{tl_version}
Provides:       tex(ext-numeric-verb.cbx) = %{tl_version}
Provides:       tex(ext-numeric.bbx) = %{tl_version}
Provides:       tex(ext-numeric.cbx) = %{tl_version}
Provides:       tex(ext-standard.bbx) = %{tl_version}
Provides:       tex(ext-verbose-common.cbx) = %{tl_version}
Provides:       tex(ext-verbose-ibid.bbx) = %{tl_version}
Provides:       tex(ext-verbose-ibid.cbx) = %{tl_version}
Provides:       tex(ext-verbose-inote.bbx) = %{tl_version}
Provides:       tex(ext-verbose-inote.cbx) = %{tl_version}
Provides:       tex(ext-verbose-note-common.cbx) = %{tl_version}
Provides:       tex(ext-verbose-note.bbx) = %{tl_version}
Provides:       tex(ext-verbose-note.cbx) = %{tl_version}
Provides:       tex(ext-verbose-trad1.bbx) = %{tl_version}
Provides:       tex(ext-verbose-trad1.cbx) = %{tl_version}
Provides:       tex(ext-verbose-trad2.bbx) = %{tl_version}
Provides:       tex(ext-verbose-trad2.cbx) = %{tl_version}
Provides:       tex(ext-verbose-trad3.bbx) = %{tl_version}
Provides:       tex(ext-verbose-trad3.cbx) = %{tl_version}
Provides:       tex(ext-verbose.bbx) = %{tl_version}
Provides:       tex(ext-verbose.cbx) = %{tl_version}

%description -n texlive-biblatex-ext
The BibLaTeX-ext bundle provides styles that slightly extend the standard
styles that ship with BibLaTeX. The styles offered in this bundle provide a
simple interface to change some of the stylistic decisions made in the standard
styles. At the same time they stay as close to their standard counterparts as
possible, so that most customisation methods can be applied here as well.

%package -n texlive-biblatex-fiwi
Summary:        BibLaTeX styles for use in German humanities
Version:        svn45876
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(standard.bbx)
Provides:       tex(fiwi-yearbeginning.bbx) = %{tl_version}
Provides:       tex(fiwi.bbx) = %{tl_version}
Provides:       tex(fiwi.cbx) = %{tl_version}
Provides:       tex(fiwi2.bbx) = %{tl_version}
Provides:       tex(fiwi2.cbx) = %{tl_version}

%description -n texlive-biblatex-fiwi
The package provides a collection of styles for BibLaTeX (version 3.5 is
required, currently). It was designed for citations in German Humanities,
especially film studies, and offers some features that are not provided by the
standard BibLaTeX styles. The style is highly optimized for documents written
in German, and the main documentation is only available in German.

%package -n texlive-biblatex-gb7714-2015
Summary:        A BibLaTeX implementation of the GBT7714-2015 bibliography style for Chinese users
Version:        svn75481
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(mfirstuc.sty)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(xstring.sty)
Provides:       tex(chinese-cajhss.bbx) = %{tl_version}
Provides:       tex(chinese-cajhss.cbx) = %{tl_version}
Provides:       tex(chinese-cajhssay.bbx) = %{tl_version}
Provides:       tex(chinese-cajhssay.cbx) = %{tl_version}
Provides:       tex(chinese-css.bbx) = %{tl_version}
Provides:       tex(chinese-css.cbx) = %{tl_version}
Provides:       tex(chinese-erj.bbx) = %{tl_version}
Provides:       tex(chinese-erj.cbx) = %{tl_version}
Provides:       tex(chinese-jmw.bbx) = %{tl_version}
Provides:       tex(chinese-jmw.cbx) = %{tl_version}
Provides:       tex(chinese-molc.bbx) = %{tl_version}
Provides:       tex(chinese-molc.cbx) = %{tl_version}
Provides:       tex(gb7714-1987.bbx) = %{tl_version}
Provides:       tex(gb7714-1987.cbx) = %{tl_version}
Provides:       tex(gb7714-1987ay.bbx) = %{tl_version}
Provides:       tex(gb7714-1987ay.cbx) = %{tl_version}
Provides:       tex(gb7714-2005.bbx) = %{tl_version}
Provides:       tex(gb7714-2005.cbx) = %{tl_version}
Provides:       tex(gb7714-2005ay.bbx) = %{tl_version}
Provides:       tex(gb7714-2005ay.cbx) = %{tl_version}
Provides:       tex(gb7714-2015-gbk.def) = %{tl_version}
Provides:       tex(gb7714-2015.bbx) = %{tl_version}
Provides:       tex(gb7714-2015.cbx) = %{tl_version}
Provides:       tex(gb7714-2015ay.bbx) = %{tl_version}
Provides:       tex(gb7714-2015ay.cbx) = %{tl_version}
Provides:       tex(gb7714-2015ms.bbx) = %{tl_version}
Provides:       tex(gb7714-2015ms.cbx) = %{tl_version}
Provides:       tex(gb7714-2015mx.bbx) = %{tl_version}
Provides:       tex(gb7714-2015mx.cbx) = %{tl_version}
Provides:       tex(gb7714-2025.bbx) = %{tl_version}
Provides:       tex(gb7714-2025.cbx) = %{tl_version}
Provides:       tex(gb7714-2025ay.bbx) = %{tl_version}
Provides:       tex(gb7714-2025ay.cbx) = %{tl_version}
Provides:       tex(gb7714-CCNU.bbx) = %{tl_version}
Provides:       tex(gb7714-CCNU.cbx) = %{tl_version}
Provides:       tex(gb7714-CCNUay.bbx) = %{tl_version}
Provides:       tex(gb7714-CCNUay.cbx) = %{tl_version}
Provides:       tex(gb7714-NWAFU.bbx) = %{tl_version}
Provides:       tex(gb7714-NWAFU.cbx) = %{tl_version}
Provides:       tex(gb7714-SEU.bbx) = %{tl_version}
Provides:       tex(gb7714-SEU.cbx) = %{tl_version}
Provides:       tex(gb7714.bbx) = %{tl_version}
Provides:       tex(gb7714.cbx) = %{tl_version}
Provides:       tex(gb7714ay.bbx) = %{tl_version}
Provides:       tex(gb7714ay.cbx) = %{tl_version}

%description -n texlive-biblatex-gb7714-2015
This package provides an implementation of the GBT7714-2015 bibliography style.
This implementation follows the GBT7714-2015 standard and can be used by simply
loading BibLaTeX with the appropriate option. A demonstration database is
provided to show how to format input for the style.

%package -n texlive-biblatex-german-legal
Summary:        Comprehensive citation style for German legal texts
Version:        svn66461
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ext-authortitle.bbx)
Requires:       tex(ext-authortitle.cbx)
Requires:       tex(xpatch.sty)
Provides:       tex(german-legal-book.bbx) = %{tl_version}
Provides:       tex(german-legal-book.cbx) = %{tl_version}

%description -n texlive-biblatex-german-legal
This package aims to provide citation styles (for footnotes and bibliographies)
for German legal texts. It is currently focused on citations in books (style
german-legal-book), but may be extended to journal articles in the future.
Dieses Paket enthalt BibLaTeX-Zitierstile fur die Rechtswissenschaften in
Deutschland. Aktuell enthalt es einen auf Monographien in den deutschen
Rechtswissenschaften ausgerichteten Zitierstil namens german-legal-book.

%package -n texlive-biblatex-gost
Summary:        BibLaTeX support for GOST standard bibliographies
Version:        svn66935
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(numeric-comp.cbx)
Provides:       tex(biblatex-gost.def) = %{tl_version}
Provides:       tex(gost-alphabetic-min.bbx) = %{tl_version}
Provides:       tex(gost-alphabetic-min.cbx) = %{tl_version}
Provides:       tex(gost-alphabetic.bbx) = %{tl_version}
Provides:       tex(gost-alphabetic.cbx) = %{tl_version}
Provides:       tex(gost-authoryear-min.bbx) = %{tl_version}
Provides:       tex(gost-authoryear-min.cbx) = %{tl_version}
Provides:       tex(gost-authoryear.bbx) = %{tl_version}
Provides:       tex(gost-authoryear.cbx) = %{tl_version}
Provides:       tex(gost-footnote-min.bbx) = %{tl_version}
Provides:       tex(gost-footnote-min.cbx) = %{tl_version}
Provides:       tex(gost-footnote.bbx) = %{tl_version}
Provides:       tex(gost-footnote.cbx) = %{tl_version}
Provides:       tex(gost-inline-min.bbx) = %{tl_version}
Provides:       tex(gost-inline-min.cbx) = %{tl_version}
Provides:       tex(gost-inline.bbx) = %{tl_version}
Provides:       tex(gost-inline.cbx) = %{tl_version}
Provides:       tex(gost-numeric-min.bbx) = %{tl_version}
Provides:       tex(gost-numeric-min.cbx) = %{tl_version}
Provides:       tex(gost-numeric.bbx) = %{tl_version}
Provides:       tex(gost-numeric.cbx) = %{tl_version}
Provides:       tex(gost-standard.bbx) = %{tl_version}

%description -n texlive-biblatex-gost
The package provides BibLaTeX support for Russian bibliography style GOST
7.0.5-2008

%package -n texlive-biblatex-historian
Summary:        A BibLaTeX style
Version:        svn19787
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(standard.bbx)
Provides:       tex(historian.bbx) = %{tl_version}
Provides:       tex(historian.cbx) = %{tl_version}

%description -n texlive-biblatex-historian
A BibLaTeX style, based on the Turabian Manual (a version of Chicago).

%package -n texlive-biblatex-ieee
Summary:        IEEE style files for BibLaTeX
Version:        svn75952
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(numeric-verb.cbx)
Provides:       tex(ieee-alphabetic.bbx) = %{tl_version}
Provides:       tex(ieee-alphabetic.cbx) = %{tl_version}
Provides:       tex(ieee-comp.cbx) = %{tl_version}
Provides:       tex(ieee.bbx) = %{tl_version}
Provides:       tex(ieee.cbx) = %{tl_version}

%description -n texlive-biblatex-ieee
This is a BibLaTeX style that implements the bibliography style of the IEEE for
BibLaTeX. The implementation follows standard BibLaTeX conventions, and can be
used simply by loading BibLaTeX with the appropriate option:
\usepackage[style=ieee]{biblatex} A demonstration database is provided to show
how to format input for the style. biblatex-ieee requires BibLaTeX 2.7 or
later, and works with both BibTeX and Biber as the database back-end.

%package -n texlive-biblatex-ijsra
Summary:        BibLaTeX style for the International Journal of Student Research in Archaeology
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(xpatch.sty)
Provides:       tex(ijsra.bbx) = %{tl_version}
Provides:       tex(ijsra.cbx) = %{tl_version}

%description -n texlive-biblatex-ijsra
BibLaTeX style used for the journal International Journal of Student Research
in Archaeology.

%package -n texlive-biblatex-iso690
Summary:        BibLaTeX style for ISO 690 standard
Version:        svn62866
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authortitle.cbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(numeric.cbx)
Provides:       tex(iso-alphabetic.bbx) = %{tl_version}
Provides:       tex(iso-alphabetic.cbx) = %{tl_version}
Provides:       tex(iso-authortitle.bbx) = %{tl_version}
Provides:       tex(iso-authortitle.cbx) = %{tl_version}
Provides:       tex(iso-authoryear.bbx) = %{tl_version}
Provides:       tex(iso-authoryear.cbx) = %{tl_version}
Provides:       tex(iso-fullcite.cbx) = %{tl_version}
Provides:       tex(iso-numeric.bbx) = %{tl_version}
Provides:       tex(iso-numeric.cbx) = %{tl_version}
Provides:       tex(iso.bbx) = %{tl_version}

%description -n texlive-biblatex-iso690
The package provides a bibliography and citation style which conforms to the
latest revision of the international standard ISO 690:2010. The implementation
follows BibLaTeX conventions and requires BibLaTeX [?] 3.4 and biber [?] 2.5.

%package -n texlive-biblatex-jura2
Summary:        Citation style for the German legal profession
Version:        svn64762
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ext-authortitle-ibid.bbx)
Requires:       tex(ext-authortitle-ibid.cbx)
Provides:       tex(jura2.bbx) = %{tl_version}
Provides:       tex(jura2.cbx) = %{tl_version}

%description -n texlive-biblatex-jura2
The package offers BibLaTeX support for citations in German legal texts.

%package -n texlive-biblatex-juradiss
Summary:        BibLaTeX stylefiles for German law theses
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authortitle-dw.bbx)
Requires:       tex(authortitle-dw.cbx)
Provides:       tex(biblatex-juradiss.bbx) = %{tl_version}
Provides:       tex(biblatex-juradiss.cbx) = %{tl_version}

%description -n texlive-biblatex-juradiss
The package provides a custom citation-style for typesetting a German law
thesis with LaTeX. The package (using BibLaTeX) is based on biblatex-dw and
uses biber.

%package -n texlive-biblatex-license
Summary:        Add license data to the bibliography
Version:        svn58437
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(biblatex-license.sty) = %{tl_version}

%description -n texlive-biblatex-license
This package is for adding license data to bibliography entries via BibLaTeX's
built-in related mechanism. It provides a new relatedtype license and some
bibmacros for typesetting these related entries.

%package -n texlive-biblatex-lncs
Summary:        BibLaTeX style for Springer Lecture Notes in Computer Science
Version:        svn67053
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
Provides:       tex(lncs.bbx) = %{tl_version}
Provides:       tex(lncs.cbx) = %{tl_version}

%description -n texlive-biblatex-lncs
This is a BibLaTeX style for Springer Lecture Notes in Computer Science (LNCS).
It extends the standard BiBTeX model by an acronym entry.

%package -n texlive-biblatex-lni
Summary:        LNI style for BibLaTeX
Version:        svn73625
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(LNI.bbx) = %{tl_version}
Provides:       tex(LNI.cbx) = %{tl_version}

%description -n texlive-biblatex-lni
BibLaTeX style for the Lecture Notes in Informatics, which is published by the
Gesellschaft fur Informatik (GI e.V.).

%package -n texlive-biblatex-luh-ipw
Summary:        BibLaTeX styles for social sciences
Version:        svn32180
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-icomp.bbx)
Requires:       tex(authoryear-icomp.cbx)
Requires:       tex(verbose-inote.bbx)
Requires:       tex(verbose-inote.cbx)
Provides:       tex(authoryear-luh-ipw.bbx) = %{tl_version}
Provides:       tex(authoryear-luh-ipw.cbx) = %{tl_version}
Provides:       tex(standard-luh-ipw.bbx) = %{tl_version}
Provides:       tex(standard-luh-ipw.cbx) = %{tl_version}
Provides:       tex(verbose-inote-luh-ipw.bbx) = %{tl_version}
Provides:       tex(verbose-inote-luh-ipw.cbx) = %{tl_version}

%description -n texlive-biblatex-luh-ipw
The bundle is a small collection of styles for BibLaTeX. It was designed for
citations in the Humanities, following the guidelines of style of the
institutes for the social sciences of the Leibniz University Hannover/LUH
(especially the Institute of Political Science). The bundle depends on BibLaTeX
(version 1.1 at least) and cannot be used without it.

%package -n texlive-biblatex-manuscripts-philology
Summary:        Manage classical manuscripts with BibLaTeX
Version:        svn66977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(verbose.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(manuscripts-NewBibliographyString.sty) = %{tl_version}
Provides:       tex(manuscripts-noautoshorthand.bbx) = %{tl_version}
Provides:       tex(manuscripts-shared.bbx) = %{tl_version}
Provides:       tex(manuscripts.bbx) = %{tl_version}

%description -n texlive-biblatex-manuscripts-philology
The package adds a new entry type: @manuscript to manage manuscript in
classical philology, for example to prepare a critical edition.

%package -n texlive-biblatex-mla
Summary:        MLA style files for BibLaTeX
Version:        svn62138
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(standard.bbx)
Provides:       tex(mla-footnotes.cbx) = %{tl_version}
Provides:       tex(mla-new.bbx) = %{tl_version}
Provides:       tex(mla-new.cbx) = %{tl_version}
Provides:       tex(mla-strict.bbx) = %{tl_version}
Provides:       tex(mla-strict.cbx) = %{tl_version}
Provides:       tex(mla.bbx) = %{tl_version}
Provides:       tex(mla.cbx) = %{tl_version}
Provides:       tex(mla7.bbx) = %{tl_version}
Provides:       tex(mla7.cbx) = %{tl_version}

%description -n texlive-biblatex-mla
The package provides BibLaTeX support for citations in the format specified by
the MLA handbook.

%package -n texlive-biblatex-morenames
Summary:        New names for standard BibLaTeX entry type
Version:        svn43049
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(verbose.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(morenames.bbx) = %{tl_version}

%description -n texlive-biblatex-morenames
This package adds new fields of "name" type to the standard entry types of
BibLaTeX. For example: maineditor, for a @collection, means the editor of
@mvcollection, and not the editor of the @collection. bookineditor, for a
@bookinbook, means the editor of the entry, and not, as the standard editor
field, the editor of the volume in which the entry is contained.

%package -n texlive-biblatex-ms
Summary:        Sophisticated Bibliographies in LaTeX (multiscript version)
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       texlive-kvoptions
Requires:       texlive-logreq
Requires:       texlive-pdftexcmds
Requires:       texlive-url
Requires:       tex(authortitle-comp.cbx)
Requires:       tex(authortitle-icomp.cbx)
Requires:       tex(authortitle.bbx)
Requires:       tex(authortitle.cbx)
Requires:       tex(authoryear.bbx)
Requires:       biber
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(logreq.sty)
Requires:       tex(numeric.bbx)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(standard.bbx)
Requires:       tex(url.sty)
Requires:       tex(xparse.sty)
Provides:       tex(alphabetic-ms.bbx) = %{tl_version}
Provides:       tex(alphabetic-ms.cbx) = %{tl_version}
Provides:       tex(alphabetic-verb-ms.bbx) = %{tl_version}
Provides:       tex(alphabetic-verb-ms.cbx) = %{tl_version}
Provides:       tex(authortitle-comp-ms.bbx) = %{tl_version}
Provides:       tex(authortitle-comp-ms.cbx) = %{tl_version}
Provides:       tex(authortitle-ibid-ms.bbx) = %{tl_version}
Provides:       tex(authortitle-ibid-ms.cbx) = %{tl_version}
Provides:       tex(authortitle-icomp-ms.bbx) = %{tl_version}
Provides:       tex(authortitle-icomp-ms.cbx) = %{tl_version}
Provides:       tex(authortitle-ms.bbx) = %{tl_version}
Provides:       tex(authortitle-ms.cbx) = %{tl_version}
Provides:       tex(authortitle-tcomp-ms.bbx) = %{tl_version}
Provides:       tex(authortitle-tcomp-ms.cbx) = %{tl_version}
Provides:       tex(authortitle-terse-ms.bbx) = %{tl_version}
Provides:       tex(authortitle-terse-ms.cbx) = %{tl_version}
Provides:       tex(authortitle-ticomp-ms.bbx) = %{tl_version}
Provides:       tex(authortitle-ticomp-ms.cbx) = %{tl_version}
Provides:       tex(authoryear-comp-ms.bbx) = %{tl_version}
Provides:       tex(authoryear-comp-ms.cbx) = %{tl_version}
Provides:       tex(authoryear-ibid-ms.bbx) = %{tl_version}
Provides:       tex(authoryear-ibid-ms.cbx) = %{tl_version}
Provides:       tex(authoryear-icomp-ms.bbx) = %{tl_version}
Provides:       tex(authoryear-icomp-ms.cbx) = %{tl_version}
Provides:       tex(authoryear-ms.bbx) = %{tl_version}
Provides:       tex(authoryear-ms.cbx) = %{tl_version}
Provides:       tex(biblatex-ms.def) = %{tl_version}
Provides:       tex(biblatex-ms.sty) = %{tl_version}
Provides:       tex(blx-bibtex-ms.def) = %{tl_version}
Provides:       tex(blx-case-expl3-ms.sty) = %{tl_version}
Provides:       tex(blx-case-latex2e-ms.sty) = %{tl_version}
Provides:       tex(blx-compat-ms.def) = %{tl_version}
Provides:       tex(blx-dm-ms.def) = %{tl_version}
Provides:       tex(blx-mcite-ms.def) = %{tl_version}
Provides:       tex(blx-natbib-ms.def) = %{tl_version}
Provides:       tex(blx-unicode-ms.def) = %{tl_version}
Provides:       tex(debug-ms.bbx) = %{tl_version}
Provides:       tex(debug-ms.cbx) = %{tl_version}
Provides:       tex(draft-ms.bbx) = %{tl_version}
Provides:       tex(draft-ms.cbx) = %{tl_version}
Provides:       tex(numeric-comp-ms.bbx) = %{tl_version}
Provides:       tex(numeric-comp-ms.cbx) = %{tl_version}
Provides:       tex(numeric-ms.bbx) = %{tl_version}
Provides:       tex(numeric-ms.cbx) = %{tl_version}
Provides:       tex(numeric-verb-ms.bbx) = %{tl_version}
Provides:       tex(numeric-verb-ms.cbx) = %{tl_version}
Provides:       tex(reading-ms.bbx) = %{tl_version}
Provides:       tex(reading-ms.cbx) = %{tl_version}
Provides:       tex(standard-ms.bbx) = %{tl_version}
Provides:       tex(verbose-ibid-ms.bbx) = %{tl_version}
Provides:       tex(verbose-ibid-ms.cbx) = %{tl_version}
Provides:       tex(verbose-inote-ms.bbx) = %{tl_version}
Provides:       tex(verbose-inote-ms.cbx) = %{tl_version}
Provides:       tex(verbose-ms.bbx) = %{tl_version}
Provides:       tex(verbose-ms.cbx) = %{tl_version}
Provides:       tex(verbose-note-ms.bbx) = %{tl_version}
Provides:       tex(verbose-note-ms.cbx) = %{tl_version}
Provides:       tex(verbose-trad1-ms.bbx) = %{tl_version}
Provides:       tex(verbose-trad1-ms.cbx) = %{tl_version}
Provides:       tex(verbose-trad2-ms.bbx) = %{tl_version}
Provides:       tex(verbose-trad2-ms.cbx) = %{tl_version}
Provides:       tex(verbose-trad3-ms.bbx) = %{tl_version}
Provides:       tex(verbose-trad3-ms.cbx) = %{tl_version}

%description -n texlive-biblatex-ms
This package is the "multiscript" version of the BibLaTeX package intended to
solve the issues faced by those wishing to create multilingual bibliographies.
It is intended to be backwards-compatible with the standard BibLaTeX package
and includes significantly enhanced optional functionality: Fields in data
files can have different form/language alternates in the same entry Options to
select/print a specific alternate are generally available babel/polyglossia
language switching is done automatically based on the language associated with
a field The intention is that this version will eventually replace standard
BibLaTeX and is being released as an independent package to allow for wider
testing and feedback. It can be installed in parallel with standard BibLaTeX
and the package name is biblatex-ms. It requires the use of the multiscript
version of biber (biber-ms).

%package -n texlive-biblatex-multiple-dm
Summary:        Load multiple datamodels in BibLaTeX
Version:        svn37081
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(biblatex-multiple-dm.sty) = %{tl_version}
Provides:       tex(multiple-dm.bbx) = %{tl_version}

%description -n texlive-biblatex-multiple-dm
The package adds the possibility to BibLaTeX to load data models from multiple
sources.

%package -n texlive-biblatex-musuos
Summary:        A BibLaTeX style for citations in musuos.cls
Version:        svn24097
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authortitle.bbx)
Requires:       tex(verbose-ibid.cbx)
Provides:       tex(musuos.bbx) = %{tl_version}
Provides:       tex(musuos.cbx) = %{tl_version}

%description -n texlive-biblatex-musuos
The style is designed for use with the musuos class, but it should be usable
with other classes, too.

%package -n texlive-biblatex-nature
Summary:        BibLaTeX support for Nature
Version:        svn57262
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Provides:       tex(nature.bbx) = %{tl_version}
Provides:       tex(nature.cbx) = %{tl_version}

%description -n texlive-biblatex-nature
The bundle offers styles that allow authors to use BibLaTeX when preparing
papers for submission to the journal Nature.

%package -n texlive-biblatex-nejm
Summary:        BibLaTeX style for the New England Journal of Medicine (NEJM)
Version:        svn49839
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(numeric-comp.cbx)
Requires:       tex(numeric.bbx)
Provides:       tex(nejm.bbx) = %{tl_version}
Provides:       tex(nejm.cbx) = %{tl_version}

%description -n texlive-biblatex-nejm
This is a BibLaTeX numeric style based on the design of the New England Journal
of Medicine (NEJM).

%package -n texlive-biblatex-nottsclassic
Summary:        Citation style for the University of Nottingham
Version:        svn41596
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.bbx)
Provides:       tex(nottsclassic.bbx) = %{tl_version}
Provides:       tex(nottsclassic.cbx) = %{tl_version}

%description -n texlive-biblatex-nottsclassic
This citation-style covers the citation and bibliography rules of the
University of Nottingham.

%package -n texlive-biblatex-opcit-booktitle
Summary:        Use op. cit. for the booktitle of a subentry
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ltxcmds.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(biblatex-opcit-booktitle.sty) = %{tl_version}

%description -n texlive-biblatex-opcit-booktitle
The default citation styles verbose-trad1+; verbose-trad2 ; verbose-trad3 use
the op. cit. form in order to have a shorter reference when a title has already
been cited. However, when you cite two entries which share the same booktitle
but not the same title, the op. cit. mechanism does not work. This package
enables to obtain references like this: Author1, Title, in Booktitle, Location,
Publisher, Year, pages xxx Author2, Title2, in Booktitle, op. cit, pages.

%package -n texlive-biblatex-oxref
Summary:        BibLaTeX styles inspired by the Oxford Guide to Style
Version:        svn72164
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(standard.bbx)
Requires:       tex(verbose-ibid.cbx)
Requires:       tex(verbose-inote.cbx)
Requires:       tex(verbose-note.cbx)
Requires:       tex(verbose-trad1.cbx)
Requires:       tex(verbose-trad2.cbx)
Requires:       tex(verbose-trad3.cbx)
Requires:       tex(verbose.cbx)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(oxalph.bbx) = %{tl_version}
Provides:       tex(oxalph.cbx) = %{tl_version}
Provides:       tex(oxnotes-ibid.bbx) = %{tl_version}
Provides:       tex(oxnotes-ibid.cbx) = %{tl_version}
Provides:       tex(oxnotes-inote.bbx) = %{tl_version}
Provides:       tex(oxnotes-inote.cbx) = %{tl_version}
Provides:       tex(oxnotes-note.bbx) = %{tl_version}
Provides:       tex(oxnotes-note.cbx) = %{tl_version}
Provides:       tex(oxnotes-trad1.bbx) = %{tl_version}
Provides:       tex(oxnotes-trad1.cbx) = %{tl_version}
Provides:       tex(oxnotes-trad2.bbx) = %{tl_version}
Provides:       tex(oxnotes-trad2.cbx) = %{tl_version}
Provides:       tex(oxnotes-trad3.bbx) = %{tl_version}
Provides:       tex(oxnotes-trad3.cbx) = %{tl_version}
Provides:       tex(oxnotes.bbx) = %{tl_version}
Provides:       tex(oxnotes.cbx) = %{tl_version}
Provides:       tex(oxnum.bbx) = %{tl_version}
Provides:       tex(oxnum.cbx) = %{tl_version}
Provides:       tex(oxref.bbx) = %{tl_version}
Provides:       tex(oxyear.bbx) = %{tl_version}
Provides:       tex(oxyear.cbx) = %{tl_version}

%description -n texlive-biblatex-oxref
This bundle provides four BibLaTeX styles that implement (many of) the
stipulations and examples provided by the 2014 New Hart's Rules and the 2002
Oxford Guide to Style: 'oxnotes' is a style similar to the standard 'verbose',
intended for use with footnotes; 'oxnum' is a style similar to the standard
'numeric', intended for use with numeric in-text citations; 'oxalph' is a style
similar to the standard 'alphabetic', intended for use with alphabetic in-text
citations; 'oxyear' is a style similar to the standard 'author-year', intended
for use with parenthetical in-text citations. The bundle provides support for a
wide variety of content types, including manuscripts, audiovisual resources,
social media and legal references.

%package -n texlive-biblatex-philosophy
Summary:        Styles for using BibLaTeX for work in philosophy
Version:        svn64414
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authortitle.bbx)
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       biber
Requires:       tex(standard.bbx)
Requires:       tex(verbose-trad2.cbx)
Provides:       tex(philosophy-classic.bbx) = %{tl_version}
Provides:       tex(philosophy-classic.cbx) = %{tl_version}
Provides:       tex(philosophy-modern.bbx) = %{tl_version}
Provides:       tex(philosophy-modern.cbx) = %{tl_version}
Provides:       tex(philosophy-standard.bbx) = %{tl_version}
Provides:       tex(philosophy-verbose.bbx) = %{tl_version}
Provides:       tex(philosophy-verbose.cbx) = %{tl_version}

%description -n texlive-biblatex-philosophy
The bundle offers two styles - philosophy-classic and philosophy-modern - that
facilitate the production of two different kinds of bibliography, based on the
authoryear style, with options and features to manage the information about the
translation of foreign texts or their reprints. Though the package's default
settings are based on the conventions used in Italian publications, these
styles can be used with every language recognized by babel, possibly with some
simple redefinitions.

%package -n texlive-biblatex-phys
Summary:        A BibLaTeX implementation of the AIP and APS bibliography style
Version:        svn74898
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Provides:       tex(phys.bbx) = %{tl_version}
Provides:       tex(phys.cbx) = %{tl_version}

%description -n texlive-biblatex-phys
The package provides an implementation of the bibliography styles of both the
AIP and the APS for BibLaTeX. This implementation follows standard BibLaTeX
conventions, and can be used simply by loading BibLaTeX with the appropriate
option: \usepackage[style=phys]{biblatex} A demonstration database is provided
to show how to format input for the style. Style options are provided to cover
the minor formatting variations between the AIP and APS bibliography styles.

%package -n texlive-biblatex-publist
Summary:        BibLaTeX bibliography support for publication lists
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric.cbx)
Requires:       tex(xcolor.sty)
Provides:       tex(publist.bbx) = %{tl_version}
Provides:       tex(publist.cbx) = %{tl_version}

%description -n texlive-biblatex-publist
The package provides a BibLaTeX bibliography style file (*.bbx) for publication
lists. The style file draws on BibLaTeX's authoryear style, but provides some
extra features often desired for publication lists, such as the omission of the
author's own name from author or editor data. At least version 3.4 of biblatex
is required.

%package -n texlive-biblatex-readbbl
Summary:        Read a .bbl file created by biber
Version:        svn61549
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(biblatex-readbbl.sty) = %{tl_version}

%description -n texlive-biblatex-readbbl
This small package modifies the biblatex macro which reads a .bbl file created
by Biber. It is thus possible to include a .bbl file into the main document
with the filecontents environment and send it to a publisher who does not need
to run the Biber program. However, when the bibliography changes one has to
create a new .bbl file.

%package -n texlive-biblatex-realauthor
Summary:        Indicate the real author of a work
Version:        svn45865
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(verbose.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(realauthor.bbx) = %{tl_version}

%description -n texlive-biblatex-realauthor
This package allows to use a new field "realauthor", which indicates the real
author of a work, when published in a pseudepigraphic name.

%package -n texlive-biblatex-sbl
Summary:        Society of Biblical Literature (SBL) style files for BibLaTeX
Version:        svn71470
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Requires:       tex(bibleref-parse.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(setspace.sty)
Requires:       tex(textcase.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Provides:       tex(biblatex-sbl.def) = %{tl_version}
Provides:       tex(sbl-paper.sty) = %{tl_version}
Provides:       tex(sbl.bbx) = %{tl_version}
Provides:       tex(sbl.cbx) = %{tl_version}

%description -n texlive-biblatex-sbl
The package provides BibLaTeX support for citations in the format specified by
the second edition of the Society of Biblical Literature (SBL) Handbook of
Style. All example notes and bibliography entries from the handbook are
supported and shown in an example file. A style file for writing SBL student
papers is also included.

%package -n texlive-biblatex-science
Summary:        BibLaTeX implementation of the Science bibliography style
Version:        svn48945
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Provides:       tex(science.bbx) = %{tl_version}
Provides:       tex(science.cbx) = %{tl_version}

%description -n texlive-biblatex-science
The bundle offers styles that allow authors to use BibLaTeX when preparing
papers for submission to the journal Science.

%package -n texlive-biblatex-shortfields
Summary:        Use short forms of fields with BibLaTeX
Version:        svn45858
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(biblatex-shortfields.sty) = %{tl_version}

%description -n texlive-biblatex-shortfields
The BibLaTeX package provides shortseries and shortjournal field, but the
default styles don't use them. It also provides a mechanism to print the
equivalence between short forms of fields and long fields (\printbiblist), but
this mechanism does not allow to mix between different type of short fields,
for example, between short forms of journal title and short forms of series
titles. This package provides a solution to these two problems: If a
shortjournal field is defined, it prints it instead of the \journal field. If a
shortseries field is defined, it prints it instead of the \series field. It
provides a \printbibshortfields command to print a list of the sort forms of
the fields. This list also includes the claves defined with the biblatex-claves
package version 1.2 or later.

%package -n texlive-biblatex-socialscienceshuberlin
Summary:        BibLaTeX-style for the social sciences at HU Berlin
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ext-authoryear.bbx)
Requires:       tex(ext-authoryear.cbx)
Requires:       tex(xcolor.sty)
Provides:       tex(socialscienceshuberlin.bbx) = %{tl_version}
Provides:       tex(socialscienceshuberlin.cbx) = %{tl_version}

%description -n texlive-biblatex-socialscienceshuberlin
This is a BibLaTeX style for the social sciences at the Humboldt-Universitat zu
Berlin.

%package -n texlive-biblatex-software
Summary:        BibLaTeX stylefiles for software products
Version:        svn77180
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(xurl.sty)
Provides:       tex(software-biblatex.sty) = %{tl_version}
Provides:       tex(software.bbx) = %{tl_version}

%description -n texlive-biblatex-software
This package implements software entry types for BibLaTeX in the form of a
bibliography style extension. It requires the Biber backend.

%package -n texlive-biblatex-source-division
Summary:        References by "division" in classical sources
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(biblatex-source-division.sty) = %{tl_version}

%description -n texlive-biblatex-source-division
The package enables the user to make reference to "division marks" (such as
book, chapter, section), in the document being referenced, in addition to the
page-based references that BibTeX-based citations have always had. The citation
is made in the same way as the LaTeX standard, but what's inside the square
brackets may include the "division" specification, as in \cite[(<division
spec.>)<page number>]{<document>}

%package -n texlive-biblatex-spbasic
Summary:        A BibLaTeX style emulating Springer's old spbasic.bst
Version:        svn61439
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Provides:       tex(biblatex-spbasic.bbx) = %{tl_version}
Provides:       tex(biblatex-spbasic.cbx) = %{tl_version}

%description -n texlive-biblatex-spbasic
This package provides a bibliography and citation style for BibLaTeX/biber for
typesetting articles for Springer's journals. It is the same as the old BibTeX
style spbasic.bst.

%package -n texlive-biblatex-subseries
Summary:        Manages subseries with BibLaTeX
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(verbose.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(subseries.bbx) = %{tl_version}

%description -n texlive-biblatex-subseries
Some publishers organize book series with subseries. In this case, two numbers
are associated with one volume: the number inside the series and the number
inside the subseries. That is the case of the series Corpus Scriptorium
Christianorum Orientalium published by Peeters. This package provides new
fields to manage such system.

%package -n texlive-biblatex-swiss-legal
Summary:        Bibliography and citation styles following Swiss legal practice
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       biber
Requires:       tex(xstring.sty)
Provides:       tex(biblatex-swiss-legal-base.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-base.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-bibliography.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-bibliography.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-general.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-general.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-longarticle.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-longarticle.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-shortarticle.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-shortarticle.cbx) = %{tl_version}

%description -n texlive-biblatex-swiss-legal
The package provides BibLaTeX bibliography and citation styles for documents
written in accordance with Swiss legal citation standards in either French or
German. However, according to
https://tex.stackexchange.com/questions/426142/bibliography-usi
ng-biblatex-swiss-legal-not-displayed-correctly the package is at present
outdated and does not work properly with newer versions of BibLaTeX.

%package -n texlive-biblatex-trad
Summary:        "Traditional" BibTeX styles with BibLaTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(numeric.cbx)
Requires:       tex(standard.bbx)
Provides:       tex(trad-abbrv.bbx) = %{tl_version}
Provides:       tex(trad-abbrv.cbx) = %{tl_version}
Provides:       tex(trad-alpha.bbx) = %{tl_version}
Provides:       tex(trad-alpha.cbx) = %{tl_version}
Provides:       tex(trad-plain.bbx) = %{tl_version}
Provides:       tex(trad-plain.cbx) = %{tl_version}
Provides:       tex(trad-standard.bbx) = %{tl_version}
Provides:       tex(trad-standard.cbx) = %{tl_version}
Provides:       tex(trad-unsrt.bbx) = %{tl_version}
Provides:       tex(trad-unsrt.cbx) = %{tl_version}

%description -n texlive-biblatex-trad
The bundle provides implementations of the "traditional" BibTeX styles (plain,
abbrev, unsrt and alpha) with BibLaTeX.

%package -n texlive-biblatex-true-citepages-omit
Summary:        Correction of some limitation of the citepages=omit option of BibLaTeX styles
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xstring.sty)
Provides:       tex(biblatex-true-citepages-omit.sty) = %{tl_version}

%description -n texlive-biblatex-true-citepages-omit
This package deals with a limitation of the citepages=omit option of the
verbose family of BibLaTeX citestyles. The option works when you
\cite[xx]{key}, but not when you \cite[\pno~xx, some text]{key}. The package
corrects this problem.

%package -n texlive-biblatex-unified
Summary:        BibLaTeX implementation of the unified stylesheet for linguistics journals
Version:        svn64975
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(unified.bbx) = %{tl_version}
Provides:       tex(unified.cbx) = %{tl_version}

%description -n texlive-biblatex-unified
BibLaTeX-unified is an opinionated BibLaTeX implementation of the Unified
Stylesheet for Linguistics Journals

%package -n texlive-biblatex-vancouver
Summary:        Vancouver style for BibLaTeX
Version:        svn75301
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(ifthen.sty)
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
Provides:       tex(vancouver.bbx) = %{tl_version}
Provides:       tex(vancouver.cbx) = %{tl_version}

%description -n texlive-biblatex-vancouver
This package provides the Vancouver reference style for BibLaTeX. It is based
on the numeric style and requires biber.

%package -n texlive-biblatex2bibitem
Summary:        Convert BibLaTeX-generated bibliography to bibitems
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Provides:       tex(biblatex2bibitem.sty) = %{tl_version}

%description -n texlive-biblatex2bibitem
Some journals accept the reference list only as \bibitems. If you use BibTeX,
there is no problem: just paste the content of the .bbl file into your
document. However, there was no out-of-the-box way to do the same for biblatex,
and you had to struggle with searching appropriate .bst files, or formatting
your reference list by hand, or something like that. Using the workaround
provided by this package solves the problem.

%package -n texlive-biblist
Summary:        Print a BibTeX database
Version:        svn77677
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(biblist.sty) = %{tl_version}

%description -n texlive-biblist
The package provides the means of listing an entire BibTeX database, avoiding
the potentially large (macro) impact associated with \nocite{*}.

%package -n texlive-bibtools
Summary:        Bib management tools
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bibtools
A set of bibliography tools. Includes: aux2bib, a perl script which will take
an .aux file and make a portable .bib file to go with it; bibify, a shell
script that will optimise away one pass of the LaTeX/BibTeX cycle, in some
cases; bibkey, a shell script that finds entries whose "keyword" field matches
the given keys (uses sed and awk); cleantex, a shell script to tidy up after a
LaTeX run; looktex, a shell script to list entries that match a given regexp;
makebib, a shell script to make an exportable .bib file from an existing (set
of) .bib file(s) and an optional set of citations (uses sed) printbib, a shell
script to make a dvi file from a .bib file, sorted by cite key, and including
fields like "keyword", "abstract", and "comment". bib2html, a perl script that
makes a browsable HTML version of a bibliography (several .bst files are
supplied); and citekeys, a shell script that lists the citation keys of a .bib
file.

%package -n texlive-bibtopic
Summary:        Include multiple bibliographies in a document
Version:        svn77677
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(bibtopic.sty) = %{tl_version}

%description -n texlive-bibtopic
The package allows the user to include several bibliographies covering
different 'topics' or bibliographic material into a document (e.g., one
bibliography for primary literature and one for secondary literature). The
package provides commands to include either all references from a .bib file,
only the references actually cited or those not cited in your document. The
user has to construct a separate .bib file for each bibliographic 'topic', each
of which will be processed separately by BibTeX. If you want to have
bibliographies specific to one part of a document, see the packages bibunits or
chapterbib.

%package -n texlive-bibtopicprefix
Summary:        Prefix references to bibliographies produced by bibtopic
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibtopic.sty)
Requires:       tex(scrlfile.sty)
Provides:       tex(bibtopicprefix.sty) = %{tl_version}

%description -n texlive-bibtopicprefix
The package permits users to apply prefixes (fixed strings) to references to
entries in bibliographies produced by the bibtopic package.

%package -n texlive-bibunits
Summary:        Multiple bibliographies in one document
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bibunits.sty) = %{tl_version}

%description -n texlive-bibunits
The package provide a mechanism to generate separate bibliographies for
different units (chapters, sections or bibunit-environments) of a text. The
package separates the citations of each unit of text into a separate file to be
processed by BibTeX. The global bibliography section produced by LaTeX may also
appear in the document and citations can be placed in both the local unit and
the global bibliographies at the same time. The package is compatible with
koma-script and with the babel French option frenchb.

%package -n texlive-biolett-bst
Summary:        A BibTeX style for the journal "Biology Letters"
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-biolett-bst
This package provides a BibTeX style (.bst) file for the journal "Biology
Letters" published by the Royal Society. This style was produced independently
and hence has no formal approval from the Royal Society.

%package -n texlive-bookdb
Summary:        A BibTeX style file for cataloguing a home library
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bookdb
This package provides an extended book entry for use in cataloguing a home
library. The extensions include fields for binding, category, collator,
condition, copy, illustrations, introduction, location, pages, size, value,
volumes.

%package -n texlive-breakcites
Summary:        Ensure that multiple citations may break at line end
Version:        svn21014
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(breakcites.sty) = %{tl_version}

%description -n texlive-breakcites
Makes a very minor change to the operation of the \cite command. Note that the
change is not necessary in unmodified LaTeX; however, there remain packages
that restore the undesirable behaviour of the command as provided in LaTeX
2.09. (Note that neither cite nor natbib make this mistake.)

%package -n texlive-cell
Summary:        Bibliography style for Cell
Version:        svn76790
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cite.sty)
Provides:       tex(cell.sty) = %{tl_version}

%description -n texlive-cell
This is an "apa-like" style (cf. apalike.bst in the BibTeX distribution),
developed from the same author's JMB style. A supporting LaTeX package is also
provided.

%package -n texlive-chbibref
Summary:        Change the Bibliography/References title
Version:        svn17120
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chbibref.sty) = %{tl_version}

%description -n texlive-chbibref
Defines a single command, \setbibref, which sets whichever of \bibname and
\refname is in use. (\bibname is used in book.cls and report.cls, and \refname
is used in article.cls.)

%package -n texlive-chembst
Summary:        A collection of BibTeX files for chemistry journals
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-chembst
The package offers a collection of advanced BibTeX style files suitable for
publications in chemistry journals. Currently, style files for journals
published by the American Chemical Society, Wiley-VCH and The Royal Society of
Chemistry are available. The style files support advanced features such as
automatic formatting of errata or creating an appropriate entry for
publications in Angewandte Chemie where both English and German should be cited
simultaneously.

%package -n texlive-chicago
Summary:        A "Chicago" bibliography style
Version:        svn77677
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chicago.sty) = %{tl_version}

%description -n texlive-chicago
Chicago is a BibTeX style that follows the "B" reference style of the 13th
Edition of the Chicago manual of style; a LaTeX package (to LaTeX 2.09
conventions) is also provided. The style was derived from the newapa style.

%package -n texlive-chicago-annote
Summary:        Chicago-based annotated BibTeX style
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-chicago-annote
This is a revision of chicagoa.bst, using the commonly-used annote field in
place of the original's annotation.

%package -n texlive-chicagoa
Summary:        "Chicago" bibliography style with annotations
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-chicagoa
This is a modification of the author's chicago style, to support an
'annotation' field in bibliographies.

%package -n texlive-chicagolinks
Summary:        "Chicago" bibliography style that allows annotations
Version:        svn76790
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-chicagolinks
This bibliography style is intended to extend the "Chicago" bibliography style
so that it can be annotated and at the same allowing DOI and URL fields.

%package -n texlive-chscite
Summary:        Bibliography style for Chalmers University of Technology
Version:        svn28552
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(url.sty)
Provides:       tex(chscite.sty) = %{tl_version}

%description -n texlive-chscite
The package, heavily based on the harvard package for Harvard-style citations,
provides a citation suite for students at Chalmers University of Technology
that follows given recommendations.

%package -n texlive-citeall
Summary:        Cite all entries of a bbl created with BibLaTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(citeall.sty) = %{tl_version}

%description -n texlive-citeall
This small package allows to cite all entries of a bbl-file created with
BibLaTeX (v1.9).

%package -n texlive-citeref
Summary:        Add reference-page-list to bibliography-items
Version:        svn47407
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(citeref.sty) = %{tl_version}

%description -n texlive-citeref
The package does its job without using the indexing facilities, and needs no
special \cite-replacement package.

%package -n texlive-citeright
Summary:        Specify accurate natbib citations for diverse naming conventions
Version:        svn75480
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(citeright.sty) = %{tl_version}

%description -n texlive-citeright
This package provides the command \citeright for aliasing in-text citations and
specifying their appearance in the list of references. It is specifically
tailored for use with the natbib package and is compatible with citation
managers such as BibDesk and JabRef. The package is intended to provide a means
for respecting the diverse naming conventions of cited authors and, in this
way, decolonizing academia.

%package -n texlive-collref
Summary:        Collect blocks of references into a single reference
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(collref.sty) = %{tl_version}

%description -n texlive-collref
The package automatically collects multiple \bibitem references, which always
appear in the same sequence in \cite, into a single \bibitem block.

%package -n texlive-compactbib
Summary:        Multiple thebibliography environments
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(compactbib.sty) = %{tl_version}

%description -n texlive-compactbib
Allows a second bibliography, optionally with a different title, after the main
bibliography.

%package -n texlive-custom-bib
Summary:        Customised BibTeX styles
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(geophys.tex) = %{tl_version}
Provides:       tex(makebst.tex) = %{tl_version}
Provides:       tex(shorthnd.tex) = %{tl_version}

%description -n texlive-custom-bib
Package generating customized BibTeX bibliography styles from a generic file
using docstrip driven by parameters generated by a menu application. Includes
support for the Harvard style of citations.

%package -n texlive-din1505
Summary:        Bibliography styles for German texts
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-din1505
A set of bibliography styles that conformt to DIN 1505, and match the original
BibTeX standard set (plain, unsrt, alpha and abbrv), together with a style
natdin to work with natbib.

%package -n texlive-dk-bib
Summary:        Danish variants of standard BibTeX styles
Version:        svn76790
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(url.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(dk-apali.sty) = %{tl_version}
Provides:       tex(dk-bib.sty) = %{tl_version}

%description -n texlive-dk-bib
Dk-bib is a translation of the four standard BibTeX style files (abbrv, alpha,
plain and unsrt) and the apalike style file into Danish. The files have been
extended with URL, ISBN, ISSN, annote and printing fields which can be enabled
through a LaTeX style file. Dk-bib also comes with a couple of Danish sorting
order files for BibTeX8.

%package -n texlive-doipubmed
Summary:        Special commands for use in bibliographies
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(url.sty)
Provides:       tex(doipubmed.sty) = %{tl_version}

%description -n texlive-doipubmed
The package provides the commands \doi, \pubmed and \citeurl. These commands
are primarily designed for use in bibliographies. A LaTeX2HTML style file is
also provided.

%package -n texlive-ecobiblatex
Summary:        Global Ecology and Biogeography BibLaTeX styles for the Biber backend
Version:        svn39233
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(standard.bbx)
Provides:       tex(ecobiblatex.bbx) = %{tl_version}
Provides:       tex(ecobiblatex.cbx) = %{tl_version}

%description -n texlive-ecobiblatex
This bundle provides a set of styles for creating bibliographies using BibLaTeX
in the style of the Global Ecology and Biogeography journal. It comprises
styles based on the conventions of John Wiley & Sons Ltd and Global Ecology and
Biogeography Conventions (c).

%package -n texlive-econ-bst
Summary:        BibTeX style for economics papers
Version:        svn76907
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-econ-bst
This is a BibTeX style file for papers in economics. It provides the following
features: author-year type citation reference style used in economics papers
highly customizable use of "certified random order" as proposed by Ray Robson
(2018)

%package -n texlive-economic
Summary:        BibTeX support for submitting to Economics journals
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ulem.sty)
Provides:       tex(aer.sty) = %{tl_version}
Provides:       tex(aertt.sty) = %{tl_version}
Provides:       tex(agecon.cls) = %{tl_version}
Provides:       tex(ajae.cls) = %{tl_version}
Provides:       tex(apecon.cls) = %{tl_version}
Provides:       tex(cje.sty) = %{tl_version}
Provides:       tex(ecca.cls) = %{tl_version}
Provides:       tex(erae.cls) = %{tl_version}
Provides:       tex(itaxpf.cls) = %{tl_version}
Provides:       tex(jrurstud.cls) = %{tl_version}
Provides:       tex(njf.cls) = %{tl_version}
Provides:       tex(oegatb.cls) = %{tl_version}
Provides:       tex(pocoec.cls) = %{tl_version}
Provides:       tex(regstud.cls) = %{tl_version}
Provides:       tex(worlddev.cls) = %{tl_version}

%description -n texlive-economic
The bundle offers macros and BibTeX styles for the American Economic Review
(AER), the American Journal of Agricultural Economics (AJAE), the Canadian
Journal of Economics (CJE), the European Review of Agricultural Economics
(ERAE), the International Economic Review (IER) and Economica. The macro sets
are based on (and require) the harvard package, and all provide variations of
author-date styles of presentation.

%package -n texlive-fbs
Summary:        BibTeX style for Frontiers in Bioscience
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fbs
A BibTeX style file made with custom-bib to fit Frontiers in Bioscience
requirements: all authors, no et al, full author names, initials abbreviated;
only abbreviated journal name italicised, no abbreviation dots; only year, no
month, at end of reference; and DOI excluded, ISSN excluded.

%package -n texlive-figbib
Summary:        Organize figure databases with BibTeX
Version:        svn19388
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(epsfig.sty)
Provides:       tex(figbib.sty) = %{tl_version}

%description -n texlive-figbib
FigBib lets you organize your figures in BibTeX databases. Some FigBib features
are: Store and manage figures in a BibTeX database; Include figures in your
LaTeX document with one short command; Generate a List of Figures containing
more/other information than the figure captions; Control with one switch where
to output the figures, either as usual float objects or in a separate part at
the end of your document.

%package -n texlive-footbib
Summary:        Bibliographic references as footnotes
Version:        svn17115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(footbib.sty) = %{tl_version}

%description -n texlive-footbib
The package makes bibliographic references appear as footnotes. It defines a
command \footcite which is similar to the LaTeX \cite command but the
references cited in this way appear at the bottom of the pages. This 'foot
bibliography' does not conflict with the standard one and both may exist
simultaneously in a document. The command \cite may still be used to produce
the standard bibliography. The foot bibliography uses its own style and
bibliographic database which may be specified independently of the standard
one. Any standard bibliography style may be used.

%package -n texlive-francais-bst
Summary:        Bibliographies conforming to French typographic standards
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(francaisbst.tex) = %{tl_version}

%description -n texlive-francais-bst
The package provides bibliographies (in French) conforming to the rules in
"Guide de la communication ecrite" (Malo, M., Quebec Amerique, 1996. ISBN
978-2-8903-7875-9). The BibTeX styles were generated using custom-bib and they
are compatible with natbib.

%package -n texlive-gbt7714
Summary:        BibTeX implementation of China's bibliography style standard GB/T 7714-2015
Version:        svn77401
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-bibtex
Requires:       texlive-natbib
Requires:       texlive-url
Requires:       tex(natbib.sty)
Requires:       tex(url.sty)
Provides:       tex(gbt7714.sty) = %{tl_version}

%description -n texlive-gbt7714
The package provides a BibTeX implementation for the Chinese national
bibliography style standard GB/T 7714-2015. It consists of two bst files for
numerical and author-year styles as well as a LaTeX package which provides the
citation style defined in the standard. The package is compatible with natbib
and supports language detection (Chinese and English) for each biblilography
entry.

%package -n texlive-geschichtsfrkl
Summary:        BibLaTeX style for historians
Version:        svn42121
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(standard.bbx)
Provides:       tex(geschichtsfrkl.bbx) = %{tl_version}
Provides:       tex(geschichtsfrkl.cbx) = %{tl_version}
Provides:       tex(geschichtsfrkldoc.sty) = %{tl_version}

%description -n texlive-geschichtsfrkl
The package provides a BibLaTeX style, (mostly) meeting the requirements of the
History Faculty of the University of Freiburg (Germany).

%package -n texlive-harvard
Summary:        Harvard citation package for use with LaTeX2e
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
# Adding for dependency on html.sty
Requires:       latex2html
Requires:       tex(ifthen.sty)
Provides:       tex(harvard.sty) = %{tl_version}

%description -n texlive-harvard
This is a re-implementation, for LaTeX2e, of the original Harvard package. The
bundle contains the LaTeX package, several BibTeX styles, and a 'Perl package'
for use with LaTeX2HTML. Harvard is an author-year citation style (all but the
first author are suppressed in second and subsequent citations of the same
entry); the package defines several variant styles: apsr.bst for the American
Political Science Review; agsm.bst for Australian Government publications;
dcu.bst from the Design Computing Unit of the University of Sydney;
kluwer.bstwhich aims at the format preferred in Kluwer publications;
nederlands.bst which deals with sorting Dutch names with prefixes (such as van)
according to Dutch rules, together with several styles whose authors offer no
description of their behaviour.

%package -n texlive-harvmac
Summary:        Macros for scientific articles
Version:        svn15878
License:        CC-BY-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(harvmac.tex) = %{tl_version}

%description -n texlive-harvmac
Known as 'Harvard macros', since written at that University.

%package -n texlive-hep-bibliography
Summary:        An acronym extension for glossaries
Version:        svn76220
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(relsize.sty)
Requires:       tex(xparse.sty)
Provides:       tex(hep-bibliography.sty) = %{tl_version}

%description -n texlive-hep-bibliography
The hep-bibliography package extends the BibLaTeX package with some
functionality mostly useful for high energy physics. In particular it makes
full use of all BibTeX fields provided by Discover High-Energy Physics. The
package is loaded with \usepackage{hep-bibliography}.

%package -n texlive-historische-zeitschrift
Summary:        BibLaTeX style for the journal 'Historische Zeitschrift'
Version:        svn42635
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(historische-zeitschrift.bbx) = %{tl_version}
Provides:       tex(historische-zeitschrift.cbx) = %{tl_version}

%description -n texlive-historische-zeitschrift
The package provides citations according with the house style of the
'Historische Zeitschrift', a German historical journal. The scheme is a
fullcite for the first citation and 'Author, Shorttitle (as note N, P)' for
later citations (P being the page number). For further details, see the
description of the house style at the journal's site. The package depends on
BibLaTeX (version 3.3 or higher) as well as etoolbox (version 1.5 or higher).

%package -n texlive-icite
Summary:        Indices locorum citatorum
Version:        svn67201
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(datatool.sty)
Requires:       tex(usebib.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(icite.sty) = %{tl_version}

%description -n texlive-icite
The package is designed to produce from BibTeX or BibLaTeX bibliographical
databases the different indices of authors and works cited which are called
indices locorum citatorum. It relies on a specific \icite command and can
operate with either BibTeX or BibLaTeX.

%package -n texlive-ietfbibs
Summary:        Generate BibTeX entries for various IETF index files
Version:        svn41332
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ietfbibs-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ietfbibs-doc <= 11:%{version}

%description -n texlive-ietfbibs
The package provides scripts to translate IETF index files to BibTeX files.

%package -n texlive-ijqc
Summary:        BibTeX style file for the Intl. J. Quantum Chem
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ijqc
ijqc.bst is a BibTeX style file to support publication in Wiley's International
Journal of Quantum Chemistry. It is not in any way officially endorsed by the
publisher or editors, and is provided without any warranty one could ever think
of.

%package -n texlive-inlinebib
Summary:        Citations in footnotes
Version:        svn22018
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(inlinebib.sty) = %{tl_version}
Provides:       tex(pageranges.sty) = %{tl_version}

%description -n texlive-inlinebib
A BibTeX style and a LaTeX package that allow for a full bibliography at the
end of the document as well as citation details in footnotes. The footnote
details include "op. cit." and "ibid." contractions.

%package -n texlive-iopart-num
Summary:        Numeric citation style for IOP journals
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-iopart-num
A BibTeX style providing numeric citation in Harvard-like format. Intended for
use with Institute of Physics (IOP) journals, including Journal of Physics.

%package -n texlive-is-bst
Summary:        Extended versions of standard BibTeX styles
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-is-bst
The bundle contains an extended version (xbtxbst.doc) of the source of the
standard BibTeX styles, together with corresponding versions of the standard
styles. The styles offer support for CODEN, ISBN, ISSN, LCCN, and PRICE fields,
extended PAGES fields, the PERIODICAL entry, and extended citation label
suffixing.

%package -n texlive-jbact
Summary:        BibTeX style for biology journals
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jbact
The style is a development of apalike.bst in the BibTeX bundle. The style
serves two journals -- if the user executes "\nocite{TitlesOn}", the style
serves for the Journal of Theoretical Biology; otherwise it serves for the
Journal of Molecular Biology.

%package -n texlive-jmb
Summary:        BibTeX style for the Journal of Theoretical Biology
Version:        svn77677
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(jmb.sty) = %{tl_version}

%description -n texlive-jmb
This BibTeX bibliography style is for the Journal of Molecular Biology and
Journal of Theoretical Biology; the accompanying LaTeX (2.09) package is a
close relative of apalike.sty in the BibTeX distribution; it features
author-date references. The bibliography style has control over whether to
print reference titles; if your database contains an article with the cite key
"TitlesOn", and you invoke it by \nocite{TitlesOn}, titles will be printed;
otherwise titles will not be printed.

%package -n texlive-jneurosci
Summary:        BibTeX style for the Journal of Neuroscience
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(jneurosci.sty) = %{tl_version}

%description -n texlive-jneurosci
This is a slightly modified version of the namedplus style, which fully
conforms with the Journal of Neuroscience citation style. It should be
characterised as an author-date citation style; a BibTeX style and a LaTeX
package are provided.

%package -n texlive-jurabib
Summary:        Extended BibTeX citation support for the humanities and legal texts
Version:        svn77677
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(bibunits.sty)
Requires:       tex(calc.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(url.sty)
Provides:       tex(dajbbib.ldf) = %{tl_version}
Provides:       tex(dejbbib.ldf) = %{tl_version}
Provides:       tex(dujbbib.ldf) = %{tl_version}
Provides:       tex(enjbbib.ldf) = %{tl_version}
Provides:       tex(fijbbib.ldf) = %{tl_version}
Provides:       tex(frjbbib.ldf) = %{tl_version}
Provides:       tex(itjbbib.ldf) = %{tl_version}
Provides:       tex(jurabib.sty) = %{tl_version}
Provides:       tex(nojbbib.ldf) = %{tl_version}
Provides:       tex(ptjbbib.ldf) = %{tl_version}
Provides:       tex(spjbbib.ldf) = %{tl_version}

%description -n texlive-jurabib
This package enables automated citation with BibTeX for legal studies and the
humanities. In addition, the package provides commands for specifying editors
in a commentary in a convenient way. Simplified formatting of the citation as
well as the bibliography entry is also provided. It is possible to display the
(short) title of a work only if an authors is cited with multiple works. Giving
a full citation in the text, conforming to the bibliography entry, is
supported. Several options are provided which might be of special interest for
those outside legal studies--for instance, displaying multiple full citations.
In addition, the format of last names and first names of authors may be changed
easily. Cross references to other footnotes are possible. Language dependent
handling of bibliography entries is possible by the special language field.

%package -n texlive-ksfh_nat
Summary:        BibTeX style for KSFH Munich
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ksfh_nat
The package supports bibliographies as standard for KSFH (Katholische
Stiftungsfachhochschule) Munich. BibTeX entries in article, book, inbook,
incollection and misc formats are supported.

%package -n texlive-logreq
Summary:        Support for automation of the LaTeX workflow
Version:        svn53003
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Provides:       tex(logreq.def) = %{tl_version}
Provides:       tex(logreq.sty) = %{tl_version}

%description -n texlive-logreq
The package helps to automate a typical LaTeX workflow that involves running
LaTeX several times, running tools such as BibTeX or makeindex, and so on. It
will log requests like "please rerun LaTeX" or "please run BibTeX on file X" to
an external XML file which lists all open tasks in a machine-readable format.
Compiler scripts and integrated LaTeX editing environments may parse this file
to determine the next steps in the workflow in a way that is more efficient
than parsing the main log file. In sum, the package will do two things: enable
package authors to use LaTeX commands to issue requests, collect all requests
from all packages and write them to an external XML file at the end of the
document.

%package -n texlive-ltb2bib
Summary:        Converts amsrefs' .ltb bibliographical databases to BibTeX format
Version:        svn43746
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsrefs.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(ltb2bib.sty) = %{tl_version}

%description -n texlive-ltb2bib
This package implements a LaTeX command that converts an amsrefs
bibliographical database (.ltb) to a BibTeX bibliographical database (.bib).
ltb2bib is the reverse of the "amsxport" option in amsrefs. Typical uses are:
produce bib entries for some publishers which don't accept amsrefs (Taylor &
Francis, for example); import an ltb database in a database management program,
e.g. for sorting; access one's ltb database within emacs's RefTeX mode.

%package -n texlive-luabibentry
Summary:        Repeat BibTeX entries in a LuaLaTeX document body
Version:        svn55777
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Provides:       tex(luabibentry.sty) = %{tl_version}

%description -n texlive-luabibentry
The package reimplements bibentry, for use in LuaLaTeX.

%package -n texlive-margbib
Summary:        Display bibitem tags in the margins
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
# Ignoring dependency on marn.sty - not part of TeX Live
Provides:       tex(margbib.sty) = %{tl_version}

%description -n texlive-margbib
The package redefines the 'thebibliography' environment to place the citation
key into the margin.

%package -n texlive-multibib
Summary:        Multiple bibliographies within one document
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(multibib.sty) = %{tl_version}

%description -n texlive-multibib
The package the creation of references to multiple bibliographies within one
document. It thus provides complementary functionality to packages like
bibunits and chapterbib, which allow the creation of one bibliography for
multiple, but different parts of the document. Multibib is compatible with
inlinebib, natbib, and koma-script.

%package -n texlive-munich
Summary:        An alternative authordate bibliography style
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-munich
The Munich BibTeX style is produced with custom-bib, as a German (and, more
generally, Continental European) alternative to such author-date styles as
harvard and oxford.

%package -n texlive-nar
Summary:        BibTeX style for Nucleic Acid Research
Version:        svn77677
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nar
This BibTeX bibliography style is for the journal Nucleic Acid Research. It was
adapted from the standard unsrt.bst style file.

%package -n texlive-newcastle-bst
Summary:        A BibTeX style to format reference lists in the Harvard at Newcastle style
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-newcastle-bst
This package provides a BibTeX style to format reference lists in the Harvard
at Newcastle style recommended by Newcastle University. It should be used
alongside natbib for citations.

%package -n texlive-nmbib
Summary:        Multiple versions of a bibliography, with different sort orders
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(natbib.sty)
Provides:       tex(nmbib.sty) = %{tl_version}

%description -n texlive-nmbib
This package is a rewrite of the multibibliography package providing multiple
bibliographies with different sorting. The new version offers a number of
citation commands, streamlines the creation of bibliographies, ensures
compatibility with the natbib package, and provides other improvements.

%package -n texlive-notes2bib
Summary:        Integrating notes into the bibliography
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(notes2bib.sty) = %{tl_version}

%description -n texlive-notes2bib
The package defines a new type of note, bibnote, which will always be added to
the bibliography. The package allows footnotes and endnotes to be moved into
the bibliography in the same way. The package can be used with natbib and
BibLaTeX as well as plain LaTeX citations. Both sorted and unsorted
bibliography styles are supported. The package uses the LaTeX 3 macros and the
associated xpackages bundle. It also makes use of the e-TeX extensions (any
post-2005 LaTeX distribution will provide these by default, but users of older
systems may need to use an elatex command or equivalent). The package relies on
LaTeX 3 support from the l3kernel and l3packages bundles.

%package -n texlive-notex-bst
Summary:        A BibTeX style that outputs HTML
Version:        svn76790
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-notex-bst
noTeX.bst produces a number of beautifully formatted HTML P elements instead of
TeX code. It can be used to automatically generate bibliographies to be served
on the web starting from BibTeX files.

%package -n texlive-oscola
Summary:        BibLaTeX style for the Oxford Standard for the Citation of Legal Authorities
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authortitle.bbx)
Requires:       biber
Requires:       tex(verbose-inote.cbx)
Provides:       tex(oscola.bbx) = %{tl_version}
Provides:       tex(oscola.cbx) = %{tl_version}

%description -n texlive-oscola
The package provides a set of style files for use with BibLaTeX (v 2+) and
Biber (v 1+) to produce citations and bibliographies in accordance with the
widely-used Oxford Standard for the Citation of Legal Authorities. It also
includes facilities for constructing tables of cases and legislation from
citations (in conjunction with appropriate indexing packages).

%package -n texlive-perception
Summary:        BibTeX style for the journal Perception
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-perception
A product of custom-bib, provided simply to save others' time.

%package -n texlive-plainyr
Summary:        Plain bibliography style, sorted by year first
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-plainyr
This is a version of the standard plain BibTeX style, modified to sort
chronologically (by year) first, then by author, title, etc. (The style's name
isn't what the author submitted: it was renamed for clarity.)

%package -n texlive-pnas2009
Summary:        BibTeX style for PNAS (newer version)
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pnas2009
This style produces bibliographies in the format of "Proceedings of the
National Academy of Sciences, USA". The style was derived from the standard
unsrt.bst and adapted to the new (2009) formatting rules.

%package -n texlive-rsc
Summary:        BibTeX style for use with RSC journals
Version:        svn41923
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(mciteplus.sty)
Requires:       tex(natbib.sty)
Requires:       tex(natmove.sty)
Provides:       tex(rsc.sty) = %{tl_version}

%description -n texlive-rsc
The rsc package provides a BibTeX style in accordance with the requirements of
the Royal Society of Chemistry. It was originally based on the file pccp.bst,
but also implements a number of styles from the achemso package. The package is
now a stub for the chemstyle package, which the author developed to unify the
writing of articles with a chemistry content.

%package -n texlive-showtags
Summary:        Print the tags of bibliography entries
Version:        svn77677
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(showtags.sty) = %{tl_version}

%description -n texlive-showtags
Prints the tag right-aligned on each line of the bibliography.

%package -n texlive-sort-by-letters
Summary:        Bibliography styles for alphabetic sorting
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sort-by-letters
This bundle contains several bibliography styles for separating a document's
references by the first letter of the first author/editor in the bibliography
entry. The styles are adapted from standard ones or from natbib ones.

%package -n texlive-splitbib
Summary:        Split and reorder your bibliography
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(splitbib.sty) = %{tl_version}

%description -n texlive-splitbib
This package enables you to split a bibliography into several categories and
subcategories. It does not depend on BibTeX: any bibliography may be split and
reordered.

%package -n texlive-turabian-formatting
Summary:        Formatting based on Turabian's Manual
Version:        svn58561
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(endnotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(nowidow.sty)
Requires:       tex(setspace.sty)
Provides:       tex(turabian-formatting.sty) = %{tl_version}
Provides:       tex(turabian-researchpaper.cls) = %{tl_version}
Provides:       tex(turabian-thesis.cls) = %{tl_version}

%description -n texlive-turabian-formatting
The turabian-formatting package provides Chicago-style formatting based on Kate
L. Turabian's "A Manual for Writers of Research Papers, Theses, and
Dissertations: Chicago Style for Students and Researchers" (9th edition).

%package -n texlive-uni-wtal-ger
Summary:        Citation style for literary studies at the University of Wuppertal
Version:        svn31541
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authortitle-dw.bbx)
Requires:       tex(authortitle-dw.cbx)
Provides:       tex(uni-wtal-ger.bbx) = %{tl_version}
Provides:       tex(uni-wtal-ger.cbx) = %{tl_version}

%description -n texlive-uni-wtal-ger
The package defines a BibLaTeX citation style based on the author-title style
of biblatex-dw. The citations are optimised for literary studies in faculty of
humanities at the Bergische Universitat Wuppertal.

%package -n texlive-uni-wtal-lin
Summary:        Citation style for linguistic studies at the University of Wuppertal
Version:        svn31409
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Provides:       tex(uni-wtal-lin.bbx) = %{tl_version}
Provides:       tex(uni-wtal-lin.cbx) = %{tl_version}

%description -n texlive-uni-wtal-lin
The package defines a BibLaTeX citation style based on the standard author-year
style. The citations are optimised for linguistic studies at the Institute of
Linguistics at the Bergische Universitat Wuppertal.

%package -n texlive-usebib
Summary:        A simple bibliography processor
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(url.sty)
Provides:       tex(usebib.sty) = %{tl_version}

%description -n texlive-usebib
The package is described by its author as "a poor person's replacement for the
more powerful methods provided by BibLaTeX to access data from a .bib file".
Its principle commands are \bibinput (which specifies a database to use) and
\usebibdata (which typesets a single field from a specified entry in that
database.

%package -n texlive-vak
Summary:        BibTeX style for Russian Theses, books, etc.
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-vak
The file can be used to format the bibliographies of PhD theses, books etc.,
according to the latest Russian standards: GOST 7.82 - 2001 and GOST 7.1 -
2003. It introduces the minimum number of new entries and styles to cover all
frequently used situations. The style file provides an easy way to perform a
semiautomatic, or a completely manual sort of the list of the references.
Processing bibliographies produced by the style requires a 8-bit BibTeX system.

%package -n texlive-windycity
Summary:        A Chicago style for BibLaTeX
Version:        svn67011
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(btxdockit.sty)
Requires:       tex(caption.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(pifont.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tgtermes.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)
Provides:       tex(windycity.bbx) = %{tl_version}
Provides:       tex(windycity.cbx) = %{tl_version}
Provides:       tex(windycity.sty) = %{tl_version}

%description -n texlive-windycity
Windy City is a style for BibLaTeX that formats notes, bibliographies,
parenthetical citations, and reference lists according to the 17th edition of
The Chicago Manual of Style.

%package -n texlive-xcite
Summary:        Use citation keys from a different document
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xr.sty)
Provides:       tex(xcite.sty) = %{tl_version}

%description -n texlive-xcite
The package xcite is no longer necessary, because its functionality has been
taken over by xr, so this final version is just a stub that loads xr.

%package -n texlive-zootaxa-bst
Summary:        A BibTeX style for the journal Zootaxa
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-zootaxa-bst
This package provides a .bst reference style file for the journal Zootaxa that
publishes contributions in zoology and classification. This is a fork of
apa.bst as provided by TeX Live since this style file resembled the most
Zootaxa's own style. Further modifications were made to the code in order to
generate in-text citations and bibliography sections appropriately.


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Apply biblatex-abnt patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-biblatex-abnt-no-l3regex.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-aaai-named
%license other-free.txt
%{_texmf_main}/bibtex/bst/aaai-named/

%files -n texlive-aichej
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/aichej/

%files -n texlive-ajl
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/ajl/

%files -n texlive-amsrefs
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/amsrefs/
%{_texmf_main}/bibtex/bst/amsrefs/
%{_texmf_main}/tex/latex/amsrefs/
%doc %{_texmf_main}/doc/latex/amsrefs/

%files -n texlive-annotate
%license other-free.txt
%{_texmf_main}/bibtex/bst/annotate/

%files -n texlive-apacite
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/apacite/
%{_texmf_main}/tex/latex/apacite/
%doc %{_texmf_main}/doc/bibtex/apacite/

%files -n texlive-apalike-ejor
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/apalike-ejor/
%doc %{_texmf_main}/doc/bibtex/apalike-ejor/

%files -n texlive-apalike2
%license knuth.txt
%{_texmf_main}/bibtex/bst/apalike2/

%files -n texlive-archaeologie
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/archaeologie/
%{_texmf_main}/tex/latex/archaeologie/
%doc %{_texmf_main}/doc/latex/archaeologie/

%files -n texlive-authordate
%license knuth.txt
%{_texmf_main}/bibtex/bst/authordate/
%{_texmf_main}/tex/latex/authordate/
%doc %{_texmf_main}/doc/bibtex/authordate/

%files -n texlive-beebe
%license pd.txt
%{_texmf_main}/bibtex/bib/beebe/
%{_texmf_main}/tex/generic/beebe/

%files -n texlive-besjournals
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/besjournals/
%doc %{_texmf_main}/doc/bibtex/besjournals/

%files -n texlive-bestpapers
%license pd.txt
%{_texmf_main}/bibtex/bst/bestpapers/
%doc %{_texmf_main}/doc/bibtex/bestpapers/

%files -n texlive-bib2qr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bib2qr/
%doc %{_texmf_main}/doc/latex/bib2qr/

%files -n texlive-bibarts
%license gpl2.txt
%{_texmf_main}/tex/latex/bibarts/
%doc %{_texmf_main}/doc/latex/bibarts/

%files -n texlive-bibbreeze
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibbreeze/
%doc %{_texmf_main}/doc/latex/bibbreeze/

%files -n texlive-bibhtml
%license gpl2.txt
%{_texmf_main}/bibtex/bst/bibhtml/
%doc %{_texmf_main}/doc/bibtex/bibhtml/

%files -n texlive-biblatex
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/biblatex/
%{_texmf_main}/bibtex/bst/biblatex/
%{_texmf_main}/tex/latex/biblatex/
%doc %{_texmf_main}/doc/latex/biblatex/

%files -n texlive-biblatex-abnt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-abnt/
%doc %{_texmf_main}/doc/latex/biblatex-abnt/

%files -n texlive-biblatex-ajc2020unofficial
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-ajc2020unofficial/
%doc %{_texmf_main}/doc/latex/biblatex-ajc2020unofficial/

%files -n texlive-biblatex-anonymous
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-anonymous/
%doc %{_texmf_main}/doc/latex/biblatex-anonymous/

%files -n texlive-biblatex-apa
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-apa/
%doc %{_texmf_main}/doc/latex/biblatex-apa/

%files -n texlive-biblatex-apa6
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-apa6/
%doc %{_texmf_main}/doc/latex/biblatex-apa6/

%files -n texlive-biblatex-archaeology
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-archaeology/
%doc %{_texmf_main}/doc/latex/biblatex-archaeology/

%files -n texlive-biblatex-arthistory-bonn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-arthistory-bonn/
%doc %{_texmf_main}/doc/latex/biblatex-arthistory-bonn/

%files -n texlive-biblatex-bath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-bath/
%doc %{_texmf_main}/doc/latex/biblatex-bath/

%files -n texlive-biblatex-bookinarticle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-bookinarticle/
%doc %{_texmf_main}/doc/latex/biblatex-bookinarticle/

%files -n texlive-biblatex-bookinother
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-bookinother/
%doc %{_texmf_main}/doc/latex/biblatex-bookinother/

%files -n texlive-biblatex-bwl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-bwl/
%doc %{_texmf_main}/doc/latex/biblatex-bwl/

%files -n texlive-biblatex-caspervector
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-caspervector/
%doc %{_texmf_main}/doc/latex/biblatex-caspervector/

%files -n texlive-biblatex-chem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-chem/
%doc %{_texmf_main}/doc/latex/biblatex-chem/

%files -n texlive-biblatex-chicago
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-chicago/
%doc %{_texmf_main}/doc/latex/biblatex-chicago/

%files -n texlive-biblatex-claves
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-claves/
%doc %{_texmf_main}/doc/latex/biblatex-claves/

%files -n texlive-biblatex-cse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-cse/
%doc %{_texmf_main}/doc/latex/biblatex-cse/

%files -n texlive-biblatex-cv
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-cv/
%doc %{_texmf_main}/doc/latex/biblatex-cv/

%files -n texlive-biblatex-dw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-dw/
%doc %{_texmf_main}/doc/latex/biblatex-dw/

%files -n texlive-biblatex-enc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-enc/
%doc %{_texmf_main}/doc/latex/biblatex-enc/

%files -n texlive-biblatex-ext
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-ext/
%doc %{_texmf_main}/doc/latex/biblatex-ext/

%files -n texlive-biblatex-fiwi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-fiwi/
%doc %{_texmf_main}/doc/latex/biblatex-fiwi/

%files -n texlive-biblatex-gb7714-2015
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-gb7714-2015/
%doc %{_texmf_main}/doc/latex/biblatex-gb7714-2015/

%files -n texlive-biblatex-german-legal
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-german-legal/
%doc %{_texmf_main}/doc/latex/biblatex-german-legal/

%files -n texlive-biblatex-gost
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-gost/
%doc %{_texmf_main}/doc/latex/biblatex-gost/

%files -n texlive-biblatex-historian
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-historian/
%doc %{_texmf_main}/doc/latex/biblatex-historian/

%files -n texlive-biblatex-ieee
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-ieee/
%doc %{_texmf_main}/doc/latex/biblatex-ieee/

%files -n texlive-biblatex-ijsra
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-ijsra/
%doc %{_texmf_main}/doc/latex/biblatex-ijsra/

%files -n texlive-biblatex-iso690
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-iso690/
%doc %{_texmf_main}/doc/latex/biblatex-iso690/

%files -n texlive-biblatex-jura2
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-jura2/
%doc %{_texmf_main}/doc/latex/biblatex-jura2/

%files -n texlive-biblatex-juradiss
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-juradiss/
%doc %{_texmf_main}/doc/latex/biblatex-juradiss/

%files -n texlive-biblatex-license
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-license/
%doc %{_texmf_main}/doc/latex/biblatex-license/

%files -n texlive-biblatex-lncs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-lncs/
%doc %{_texmf_main}/doc/latex/biblatex-lncs/

%files -n texlive-biblatex-lni
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-lni/
%doc %{_texmf_main}/doc/latex/biblatex-lni/

%files -n texlive-biblatex-luh-ipw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-luh-ipw/
%doc %{_texmf_main}/doc/latex/biblatex-luh-ipw/

%files -n texlive-biblatex-manuscripts-philology
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-manuscripts-philology/
%doc %{_texmf_main}/doc/latex/biblatex-manuscripts-philology/

%files -n texlive-biblatex-mla
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-mla/
%doc %{_texmf_main}/doc/latex/biblatex-mla/

%files -n texlive-biblatex-morenames
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-morenames/
%doc %{_texmf_main}/doc/latex/biblatex-morenames/

%files -n texlive-biblatex-ms
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/biblatex-ms/
%{_texmf_main}/bibtex/bst/biblatex-ms/
%{_texmf_main}/tex/latex/biblatex-ms/
%doc %{_texmf_main}/doc/latex/biblatex-ms/

%files -n texlive-biblatex-multiple-dm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-multiple-dm/
%doc %{_texmf_main}/doc/latex/biblatex-multiple-dm/

%files -n texlive-biblatex-musuos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-musuos/
%doc %{_texmf_main}/doc/latex/biblatex-musuos/

%files -n texlive-biblatex-nature
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-nature/
%doc %{_texmf_main}/doc/latex/biblatex-nature/

%files -n texlive-biblatex-nejm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-nejm/
%doc %{_texmf_main}/doc/latex/biblatex-nejm/

%files -n texlive-biblatex-nottsclassic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-nottsclassic/
%doc %{_texmf_main}/doc/latex/biblatex-nottsclassic/

%files -n texlive-biblatex-opcit-booktitle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-opcit-booktitle/
%doc %{_texmf_main}/doc/latex/biblatex-opcit-booktitle/

%files -n texlive-biblatex-oxref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-oxref/
%doc %{_texmf_main}/doc/latex/biblatex-oxref/

%files -n texlive-biblatex-philosophy
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-philosophy/
%doc %{_texmf_main}/doc/latex/biblatex-philosophy/

%files -n texlive-biblatex-phys
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-phys/
%doc %{_texmf_main}/doc/latex/biblatex-phys/

%files -n texlive-biblatex-publist
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-publist/
%doc %{_texmf_main}/doc/latex/biblatex-publist/

%files -n texlive-biblatex-readbbl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-readbbl/
%doc %{_texmf_main}/doc/latex/biblatex-readbbl/

%files -n texlive-biblatex-realauthor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-realauthor/
%doc %{_texmf_main}/doc/latex/biblatex-realauthor/

%files -n texlive-biblatex-sbl
%license lppl1.3c.txt
%{_texmf_main}/makeindex/biblatex-sbl/
%{_texmf_main}/tex/latex/biblatex-sbl/
%doc %{_texmf_main}/doc/latex/biblatex-sbl/

%files -n texlive-biblatex-science
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-science/
%doc %{_texmf_main}/doc/latex/biblatex-science/

%files -n texlive-biblatex-shortfields
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-shortfields/
%doc %{_texmf_main}/doc/latex/biblatex-shortfields/

%files -n texlive-biblatex-socialscienceshuberlin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-socialscienceshuberlin/
%doc %{_texmf_main}/doc/latex/biblatex-socialscienceshuberlin/

%files -n texlive-biblatex-software
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-software/
%doc %{_texmf_main}/doc/latex/biblatex-software/

%files -n texlive-biblatex-source-division
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-source-division/
%doc %{_texmf_main}/doc/latex/biblatex-source-division/

%files -n texlive-biblatex-spbasic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-spbasic/
%doc %{_texmf_main}/doc/latex/biblatex-spbasic/

%files -n texlive-biblatex-subseries
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-subseries/
%doc %{_texmf_main}/doc/latex/biblatex-subseries/

%files -n texlive-biblatex-swiss-legal
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-swiss-legal/
%doc %{_texmf_main}/doc/latex/biblatex-swiss-legal/

%files -n texlive-biblatex-trad
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-trad/
%doc %{_texmf_main}/doc/latex/biblatex-trad/

%files -n texlive-biblatex-true-citepages-omit
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-true-citepages-omit/
%doc %{_texmf_main}/doc/latex/biblatex-true-citepages-omit/

%files -n texlive-biblatex-unified
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-unified/
%doc %{_texmf_main}/doc/latex/biblatex-unified/

%files -n texlive-biblatex-vancouver
%license gpl3.txt
%{_texmf_main}/tex/latex/biblatex-vancouver/
%doc %{_texmf_main}/doc/latex/biblatex-vancouver/

%files -n texlive-biblatex2bibitem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex2bibitem/
%doc %{_texmf_main}/doc/latex/biblatex2bibitem/

%files -n texlive-biblist
%license gpl2.txt
%{_texmf_main}/tex/latex/biblist/
%doc %{_texmf_main}/doc/latex/biblist/

%files -n texlive-bibtools
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/bibtools/

%files -n texlive-bibtopic
%license gpl2.txt
%{_texmf_main}/tex/latex/bibtopic/
%doc %{_texmf_main}/doc/latex/bibtopic/

%files -n texlive-bibtopicprefix
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibtopicprefix/
%doc %{_texmf_main}/doc/latex/bibtopicprefix/

%files -n texlive-bibunits
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibunits/
%doc %{_texmf_main}/doc/latex/bibunits/

%files -n texlive-biolett-bst
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/biolett-bst/
%doc %{_texmf_main}/doc/bibtex/biolett-bst/

%files -n texlive-bookdb
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/bookdb/
%doc %{_texmf_main}/doc/bibtex/bookdb/

%files -n texlive-breakcites
%license other-free.txt
%{_texmf_main}/tex/latex/breakcites/
%doc %{_texmf_main}/doc/latex/breakcites/

%files -n texlive-cell
%license pd.txt
%{_texmf_main}/bibtex/bst/cell/
%{_texmf_main}/tex/latex/cell/
%doc %{_texmf_main}/doc/latex/cell/

%files -n texlive-chbibref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chbibref/
%doc %{_texmf_main}/doc/latex/chbibref/

%files -n texlive-chembst
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/chembst/
%doc %{_texmf_main}/doc/latex/chembst/

%files -n texlive-chicago
%license knuth.txt
%{_texmf_main}/bibtex/bst/chicago/
%{_texmf_main}/tex/latex/chicago/

%files -n texlive-chicago-annote
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/chicago-annote/
%doc %{_texmf_main}/doc/bibtex/chicago-annote/

%files -n texlive-chicagoa
%license other-free.txt
%{_texmf_main}/bibtex/bst/chicagoa/

%files -n texlive-chicagolinks
%license mit.txt
%{_texmf_main}/bibtex/bst/chicagolinks/
%doc %{_texmf_main}/doc/bibtex/chicagolinks/

%files -n texlive-chscite
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/chscite/
%{_texmf_main}/tex/latex/chscite/
%doc %{_texmf_main}/doc/latex/chscite/

%files -n texlive-citeall
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/citeall/
%doc %{_texmf_main}/doc/latex/citeall/

%files -n texlive-citeref
%license bsd.txt
%{_texmf_main}/tex/latex/citeref/
%doc %{_texmf_main}/doc/latex/citeref/

%files -n texlive-citeright
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/citeright/
%doc %{_texmf_main}/doc/latex/citeright/

%files -n texlive-collref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/collref/
%doc %{_texmf_main}/doc/latex/collref/

%files -n texlive-compactbib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/compactbib/

%files -n texlive-custom-bib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/custom-bib/
%doc %{_texmf_main}/doc/latex/custom-bib/

%files -n texlive-din1505
%license other-free.txt
%{_texmf_main}/bibtex/bst/din1505/
%doc %{_texmf_main}/doc/latex/din1505/

%files -n texlive-dk-bib
%license gpl2.txt
%{_texmf_main}/bibtex/bib/dk-bib/
%{_texmf_main}/bibtex/bst/dk-bib/
%{_texmf_main}/bibtex/csf/dk-bib/
%{_texmf_main}/tex/latex/dk-bib/
%doc %{_texmf_main}/doc/latex/dk-bib/

%files -n texlive-doipubmed
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/doipubmed/
%doc %{_texmf_main}/doc/latex/doipubmed/

%files -n texlive-ecobiblatex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ecobiblatex/
%doc %{_texmf_main}/doc/latex/ecobiblatex/

%files -n texlive-econ-bst
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/econ-bst/
%doc %{_texmf_main}/doc/bibtex/econ-bst/

%files -n texlive-economic
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/economic/
%{_texmf_main}/tex/latex/economic/
%doc %{_texmf_main}/doc/bibtex/economic/

%files -n texlive-fbs
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/fbs/

%files -n texlive-figbib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/figbib/
%{_texmf_main}/tex/latex/figbib/
%doc %{_texmf_main}/doc/latex/figbib/

%files -n texlive-footbib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/footbib/
%doc %{_texmf_main}/doc/latex/footbib/

%files -n texlive-francais-bst
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/francais-bst/
%{_texmf_main}/tex/latex/francais-bst/
%doc %{_texmf_main}/doc/bibtex/francais-bst/

%files -n texlive-gbt7714
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/gbt7714/
%{_texmf_main}/tex/latex/gbt7714/
%doc %{_texmf_main}/doc/bibtex/gbt7714/

%files -n texlive-geschichtsfrkl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/geschichtsfrkl/
%doc %{_texmf_main}/doc/latex/geschichtsfrkl/

%files -n texlive-harvard
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/harvard/
%{_texmf_main}/bibtex/bst/harvard/
%{_texmf_main}/tex/latex/harvard/
%doc %{_texmf_main}/doc/latex/harvard/

%files -n texlive-harvmac
%license cc-by-3.txt
%{_texmf_main}/tex/plain/harvmac/
%doc %{_texmf_main}/doc/plain/harvmac/

%files -n texlive-hep-bibliography
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hep-bibliography/
%doc %{_texmf_main}/doc/latex/hep-bibliography/

%files -n texlive-historische-zeitschrift
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/historische-zeitschrift/
%doc %{_texmf_main}/doc/latex/historische-zeitschrift/

%files -n texlive-icite
%license gpl3.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/icite/
%doc %{_texmf_main}/doc/latex/icite/

%files -n texlive-ietfbibs
%license mit.txt
%doc %{_texmf_main}/doc/bibtex/ietfbibs/

%files -n texlive-ijqc
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/ijqc/
%doc %{_texmf_main}/doc/bibtex/ijqc/

%files -n texlive-inlinebib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/inlinebib/
%{_texmf_main}/tex/latex/inlinebib/
%doc %{_texmf_main}/doc/bibtex/inlinebib/

%files -n texlive-iopart-num
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/iopart-num/
%doc %{_texmf_main}/doc/bibtex/iopart-num/

%files -n texlive-is-bst
%license other-free.txt
%{_texmf_main}/bibtex/bst/is-bst/
%doc %{_texmf_main}/doc/bibtex/is-bst/

%files -n texlive-jbact
%license other-free.txt
%{_texmf_main}/bibtex/bst/jbact/

%files -n texlive-jmb
%license other-free.txt
%{_texmf_main}/bibtex/bst/jmb/
%{_texmf_main}/tex/latex/jmb/

%files -n texlive-jneurosci
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/jneurosci/
%{_texmf_main}/tex/latex/jneurosci/
%doc %{_texmf_main}/doc/latex/jneurosci/

%files -n texlive-jurabib
%license gpl2.txt
%{_texmf_main}/bibtex/bib/jurabib/
%{_texmf_main}/bibtex/bst/jurabib/
%{_texmf_main}/tex/latex/jurabib/
%doc %{_texmf_main}/doc/latex/jurabib/

%files -n texlive-ksfh_nat
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/ksfh_nat/

%files -n texlive-logreq
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/logreq/
%doc %{_texmf_main}/doc/latex/logreq/

%files -n texlive-ltb2bib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ltb2bib/
%doc %{_texmf_main}/doc/latex/ltb2bib/

%files -n texlive-luabibentry
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luabibentry/
%doc %{_texmf_main}/doc/lualatex/luabibentry/

%files -n texlive-margbib
%license gpl2.txt
%{_texmf_main}/tex/latex/margbib/
%doc %{_texmf_main}/doc/latex/margbib/

%files -n texlive-multibib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/multibib/
%{_texmf_main}/makeindex/multibib/
%{_texmf_main}/tex/latex/multibib/
%doc %{_texmf_main}/doc/latex/multibib/

%files -n texlive-munich
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/munich/
%doc %{_texmf_main}/doc/latex/munich/

%files -n texlive-nar
%license other-free.txt
%{_texmf_main}/bibtex/bst/nar/

%files -n texlive-newcastle-bst
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/newcastle-bst/
%doc %{_texmf_main}/doc/bibtex/newcastle-bst/

%files -n texlive-nmbib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/nmbib/
%{_texmf_main}/tex/latex/nmbib/
%doc %{_texmf_main}/doc/latex/nmbib/

%files -n texlive-notes2bib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/notes2bib/
%doc %{_texmf_main}/doc/latex/notes2bib/

%files -n texlive-notex-bst
%license pd.txt
%{_texmf_main}/bibtex/bst/notex-bst/

%files -n texlive-oscola
%license lppl1.3c.txt
%{_texmf_main}/makeindex/oscola/
%{_texmf_main}/tex/latex/oscola/
%doc %{_texmf_main}/doc/latex/oscola/

%files -n texlive-perception
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/perception/
%doc %{_texmf_main}/doc/bibtex/perception/

%files -n texlive-plainyr
%license other-free.txt
%{_texmf_main}/bibtex/bst/plainyr/

%files -n texlive-pnas2009
%license other-free.txt
%{_texmf_main}/bibtex/bst/pnas2009/

%files -n texlive-rsc
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/rsc/
%{_texmf_main}/tex/latex/rsc/
%doc %{_texmf_main}/doc/latex/rsc/

%files -n texlive-showtags
%license pd.txt
%{_texmf_main}/tex/latex/showtags/
%doc %{_texmf_main}/doc/latex/showtags/

%files -n texlive-sort-by-letters
%license other-free.txt
%{_texmf_main}/bibtex/bst/sort-by-letters/
%doc %{_texmf_main}/doc/bibtex/sort-by-letters/

%files -n texlive-splitbib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/splitbib/
%doc %{_texmf_main}/doc/latex/splitbib/

%files -n texlive-turabian-formatting
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/turabian-formatting/
%doc %{_texmf_main}/doc/latex/turabian-formatting/

%files -n texlive-uni-wtal-ger
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uni-wtal-ger/
%doc %{_texmf_main}/doc/latex/uni-wtal-ger/

%files -n texlive-uni-wtal-lin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uni-wtal-lin/
%doc %{_texmf_main}/doc/latex/uni-wtal-lin/

%files -n texlive-usebib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/usebib/
%doc %{_texmf_main}/doc/latex/usebib/

%files -n texlive-vak
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/vak/
%doc %{_texmf_main}/doc/bibtex/vak/

%files -n texlive-windycity
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/windycity/
%doc %{_texmf_main}/doc/latex/windycity/

%files -n texlive-xcite
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xcite/
%doc %{_texmf_main}/doc/latex/xcite/

%files -n texlive-zootaxa-bst
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/zootaxa-bst/
%doc %{_texmf_main}/doc/bibtex/zootaxa-bst/

%changelog
* Tue Feb 10 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75480-6
- Update amsrefs apacite authordate biblatex biblatex-chicago biblatex-dw
  biblatex-ext biblatex-juradiss biblatex-publist biblatex-swiss-legal
  biblatex-trad biblatex2bibitem biblist bibtopic bibunits chicago
  citeall collref harvard jmb jurabib multibib nar nmbib notes2bib oscola
  showtags splitbib usebib xcite
- add cls Provides

* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75480-5
- update beebe, biblatex-bath, biblatex-swiss-legal, gbt7714

* Thu Jan 15 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75480-4
- more license fixes
- newer beebe

* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75480-3
- fix licensing, descriptions
- update components to latest

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75480-2
- Regenerated, no longer pulls deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75480-1
- Update to TeX Live 2025
