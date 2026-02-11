%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-publishers
Epoch:          12
Version:        svn77587
Release:        2%{?dist}
Summary:        Publisher styles, theses, etc.

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-publishers.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aastex.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aastex.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abnt.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abnt.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abntex2.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abntex2.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abntexto.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abntexto.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abntexto-uece.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abntexto-uece.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/acmart.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/acmart.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/acmconf.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/acmconf.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/active-conf.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/active-conf.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adfathesis.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adfathesis.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aeskwadraat.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aeskwadraat.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/afthesis.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/afthesis.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aguplus.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aguplus.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aiaa.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aiaa.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amnestyreport.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amnestyreport.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anonymous-acm.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anonymous-acm.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anufinalexam.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anufinalexam.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa6.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa6.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa6e.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa6e.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa7.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apa7.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arsclassica.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arsclassica.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/articleingud.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/articleingud.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asaetr.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asaetr.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascelike.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascelike.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asmeconf.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asmeconf.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asmejour.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asmejour.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aucklandthesis.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aucklandthesis.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangorcsthesis.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangorcsthesis.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangorexam.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangorexam.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bath-bst.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bath-bst.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-fuberlin.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-fuberlin.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-verona.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-verona.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beilstein.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beilstein.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bfh-ci.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bfh-ci.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bgteubner.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bgteubner.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bjfuthesis.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bjfuthesis.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bmstu.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bmstu.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bmstu-iu8.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bmstu-iu8.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/br-lex.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/br-lex.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brandeis-dissertation.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brandeis-dissertation.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brandeis-problemset.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brandeis-problemset.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brandeis-thesis.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brandeis-thesis.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/buctthesis.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/buctthesis.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascadilla.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascadilla.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cesenaexam.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cesenaexam.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chem-journal.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chifoot.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chifoot.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chs-physics-report.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chs-physics-report.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cidarticle.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cidarticle.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cje.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cje.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjs-rcs-article.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjs-rcs-article.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/classicthesis.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/classicthesis.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cleanthesis.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cleanthesis.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmpj.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmpj.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/confproc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/confproc.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/contract.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/contract.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cqjtuthesis.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cqjtuthesis.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cquthesis.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cquthesis.doc.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dccpaper.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dccpaper.doc.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dithesis.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dithesis.doc.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dlrg-templates.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dlrg-templates.doc.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebook.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebook.doc.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebsthesis.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebsthesis.doc.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecothesis.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecothesis.doc.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edmaths.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edmaths.doc.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ejpecp.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ejpecp.doc.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ekaia.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ekaia.doc.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elbioimp.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elbioimp.doc.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/els-cas-templates.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/els-cas-templates.doc.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elsarticle.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elsarticle.doc.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elteiktdk.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elteiktdk.doc.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elteikthesis.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elteikthesis.doc.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emisa.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emisa.doc.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/erdc.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/erdc.doc.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/estcpmm.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/estcpmm.doc.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etsvthor.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etsvthor.doc.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/facture-belge-simple-sans-tva.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/facture-belge-simple-sans-tva.doc.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fbithesis.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fbithesis.doc.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fcavtex.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fcavtex.doc.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fcltxdoc.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fcltxdoc.doc.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fei.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fei.doc.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fhj-script.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fhj-script.doc.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ftc-notebook.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ftc-notebook.doc.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gaceta.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gaceta.doc.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gammas.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gammas.doc.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geradwp.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geradwp.doc.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfdl.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfdl.doc.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gradstudentresume.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gradstudentresume.doc.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grant.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grant.doc.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gsemthesis.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gsemthesis.doc.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gzt.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gzt.doc.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/h2020proposal.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/h2020proposal.doc.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hagenberg-thesis.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hagenberg-thesis.doc.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/har2nat.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/har2nat.doc.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hduthesis.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hduthesis.doc.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hecthese.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hecthese.doc.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-paper.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-paper.doc.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/heria.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/heria.doc.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfutexam.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfutexam.doc.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfutthesis.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfutthesis.doc.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hithesis.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hithesis.doc.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hitszbeamer.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hitszbeamer.doc.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hitszthesis.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hitszthesis.doc.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hobete.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hobete.doc.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hu-berlin-bundle.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hu-berlin-bundle.doc.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hustthesis.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hustthesis.doc.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hustvisual.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hustvisual.doc.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iaria.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iaria.doc.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iaria-lite.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iaria-lite.doc.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/icsv.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/icsv.doc.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieeeconf.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieeeconf.doc.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieeepes.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieeepes.doc.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieeetran.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieeetran.doc.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ijmart.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ijmart.doc.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ijsra.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ijsra.doc.tar.xz
Source231:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imac.tar.xz
Source232:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imac.doc.tar.xz
Source233:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imtekda.tar.xz
Source234:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imtekda.doc.tar.xz
Source235:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inkpaper.tar.xz
Source236:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inkpaper.doc.tar.xz
Source237:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iodhbwm.tar.xz
Source238:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iodhbwm.doc.tar.xz
Source239:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iscram.tar.xz
Source240:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iscram.doc.tar.xz
Source241:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jacow.tar.xz
Source242:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jacow.doc.tar.xz
Source243:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jmlr.tar.xz
Source244:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jmlr.doc.tar.xz
Source245:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jnuexam.tar.xz
Source246:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jnuexam.doc.tar.xz
Source247:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jourcl.tar.xz
Source248:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jourcl.doc.tar.xz
Source249:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jourrr.tar.xz
Source250:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jourrr.doc.tar.xz
Source251:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jpsj.tar.xz
Source252:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jpsj.doc.tar.xz
Source253:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jsonresume.tar.xz
Source254:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jsonresume.doc.tar.xz
Source255:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jwjournal.tar.xz
Source256:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jwjournal.doc.tar.xz
Source257:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kdgdocs.tar.xz
Source258:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kdgdocs.doc.tar.xz
Source259:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kdpcover.tar.xz
Source260:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kdpcover.doc.tar.xz
Source261:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kfupm-math-exam.tar.xz
Source262:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kfupm-math-exam.doc.tar.xz
Source263:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kluwer.tar.xz
Source264:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kluwer.doc.tar.xz
Source265:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ksp-thesis.tar.xz
Source266:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ksp-thesis.doc.tar.xz
Source267:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ku-template.tar.xz
Source268:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ku-template.doc.tar.xz
Source269:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langsci.tar.xz
Source270:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langsci.doc.tar.xz
Source271:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langsci-avm.tar.xz
Source272:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langsci-avm.doc.tar.xz
Source273:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/limecv.tar.xz
Source274:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/limecv.doc.tar.xz
Source275:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lion-msc.tar.xz
Source276:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lion-msc.doc.tar.xz
Source277:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/llncs.tar.xz
Source278:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/llncs.doc.tar.xz
Source279:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/llncsconf.tar.xz
Source280:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/llncsconf.doc.tar.xz
Source281:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lni.tar.xz
Source282:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lni.doc.tar.xz
Source283:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lps.tar.xz
Source284:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lps.doc.tar.xz
Source285:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maine-thesis.tar.xz
Source286:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maine-thesis.doc.tar.xz
Source287:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matc3.tar.xz
Source288:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matc3.doc.tar.xz
Source289:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matc3mem.tar.xz
Source290:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matc3mem.doc.tar.xz
Source291:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mcmthesis.tar.xz
Source292:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mcmthesis.doc.tar.xz
Source293:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mentis.tar.xz
Source294:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mentis.doc.tar.xz
Source295:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mitthesis.tar.xz
Source296:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mitthesis.doc.tar.xz
Source297:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mlacls.tar.xz
Source298:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mlacls.doc.tar.xz
Source299:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mluexercise.tar.xz
Source300:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mluexercise.doc.tar.xz
Source301:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnras.tar.xz
Source302:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnras.doc.tar.xz
Source303:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modeles-factures-belges-assocs.tar.xz
Source304:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modeles-factures-belges-assocs.doc.tar.xz
Source305:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modernnewspaper.tar.xz
Source306:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modernnewspaper.doc.tar.xz
Source307:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/msu-thesis.tar.xz
Source308:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/msu-thesis.doc.tar.xz
Source309:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mucproc.tar.xz
Source310:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mucproc.doc.tar.xz
Source311:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mugsthesis.tar.xz
Source312:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mugsthesis.doc.tar.xz
Source313:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/muling.tar.xz
Source314:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/muling.doc.tar.xz
Source315:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musuos.tar.xz
Source316:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musuos.doc.tar.xz
Source317:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/muthesis.tar.xz
Source318:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/muthesis.doc.tar.xz
Source319:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mynsfc.tar.xz
Source320:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mynsfc.doc.tar.xz
Source321:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nature.tar.xz
Source322:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nature.doc.tar.xz
Source323:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/navydocs.tar.xz
Source324:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/navydocs.doc.tar.xz
Source325:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nddiss.tar.xz
Source326:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nddiss.doc.tar.xz
Source327:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ndsu-thesis.tar.xz
Source328:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ndsu-thesis.doc.tar.xz
Source329:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ndsu-thesis-2022.tar.xz
Source330:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ndsu-thesis-2022.doc.tar.xz
Source331:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nih.tar.xz
Source332:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nih.doc.tar.xz
Source333:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nihbiosketch.tar.xz
Source334:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nihbiosketch.doc.tar.xz
Source335:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njustthesis.tar.xz
Source336:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njustthesis.doc.tar.xz
Source337:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njuthesis.tar.xz
Source338:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njuthesis.doc.tar.xz
Source339:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njuvisual.tar.xz
Source340:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njuvisual.doc.tar.xz
Source341:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nostarch.tar.xz
Source342:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nostarch.doc.tar.xz
Source343:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/novel.tar.xz
Source344:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/novel.doc.tar.xz
Source345:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nrc.tar.xz
Source346:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nrc.doc.tar.xz
Source347:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nstc-proposal.tar.xz
Source348:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nstc-proposal.doc.tar.xz
Source349:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nwafuthesis.tar.xz
Source350:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nwafuthesis.doc.tar.xz
Source351:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nwejm.tar.xz
Source352:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nwejm.doc.tar.xz
Source353:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nxuthesis.tar.xz
Source354:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nxuthesis.doc.tar.xz
Source355:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/omgtudoc-asoiu.tar.xz
Source356:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/omgtudoc-asoiu.doc.tar.xz
Source357:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/onrannual.tar.xz
Source358:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/onrannual.doc.tar.xz
Source359:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opteng.tar.xz
Source360:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opteng.doc.tar.xz
Source361:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oststud.tar.xz
Source362:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oststud.doc.tar.xz
Source363:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ou-tma.tar.xz
Source364:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ou-tma.doc.tar.xz
Source365:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oup-authoring-template.tar.xz
Source366:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oup-authoring-template.doc.tar.xz
Source367:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pats-resume.tar.xz
Source368:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pats-resume.doc.tar.xz
Source369:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/philosophersimprint.tar.xz
Source370:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/philosophersimprint.doc.tar.xz
Source371:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phimisci.tar.xz
Source372:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phimisci.doc.tar.xz
Source373:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pittetd.tar.xz
Source374:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pittetd.doc.tar.xz
Source375:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pkuthss.tar.xz
Source376:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pkuthss.doc.tar.xz
Source377:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/powerdot-fuberlin.tar.xz
Source378:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/powerdot-fuberlin.doc.tar.xz
Source379:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/powerdot-tuliplab.tar.xz
Source380:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/powerdot-tuliplab.doc.tar.xz
Source381:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pracjourn.tar.xz
Source382:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pracjourn.doc.tar.xz
Source383:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prociagssymp.tar.xz
Source384:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prociagssymp.doc.tar.xz
Source385:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proposal.tar.xz
Source386:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proposal.doc.tar.xz
Source387:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prtec.tar.xz
Source388:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prtec.doc.tar.xz
Source389:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptptex.tar.xz
Source390:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptptex.doc.tar.xz
Source391:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qrbill.tar.xz
Source392:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qrbill.doc.tar.xz
Source393:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantumarticle.tar.xz
Source394:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quantumarticle.doc.tar.xz
Source395:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rebuttal.tar.xz
Source396:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rebuttal.doc.tar.xz
Source397:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/regulatory.tar.xz
Source398:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/regulatory.doc.tar.xz
Source399:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resphilosophica.tar.xz
Source400:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resphilosophica.doc.tar.xz
Source401:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resumecls.tar.xz
Source402:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/resumecls.doc.tar.xz
Source403:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/retosmatematicos.tar.xz
Source404:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/retosmatematicos.doc.tar.xz
Source405:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revtex.tar.xz
Source406:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revtex.doc.tar.xz
Source407:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revtex4.tar.xz
Source408:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revtex4.doc.tar.xz
Source409:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revtex4-1.tar.xz
Source410:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/revtex4-1.doc.tar.xz
Source411:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rub-kunstgeschichte.tar.xz
Source412:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rub-kunstgeschichte.doc.tar.xz
Source413:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rutitlepage.tar.xz
Source414:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rutitlepage.doc.tar.xz
Source415:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rwth-ci.tar.xz
Source416:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rwth-ci.doc.tar.xz
Source417:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ryersonsgsthesis.tar.xz
Source418:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ryersonsgsthesis.doc.tar.xz
Source419:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ryethesis.tar.xz
Source420:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ryethesis.doc.tar.xz
Source421:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sageep.tar.xz
Source422:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sageep.doc.tar.xz
Source423:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sapthesis.tar.xz
Source424:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sapthesis.doc.tar.xz
Source425:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schule.tar.xz
Source426:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schule.doc.tar.xz
Source427:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scientific-thesis-cover.tar.xz
Source428:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scientific-thesis-cover.doc.tar.xz
Source429:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scripture.tar.xz
Source430:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scripture.doc.tar.xz
Source431:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scrjrnl.tar.xz
Source432:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scrjrnl.doc.tar.xz
Source433:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sduthesis.tar.xz
Source434:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sduthesis.doc.tar.xz
Source435:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/se2thesis.tar.xz
Source436:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/se2thesis.doc.tar.xz
Source437:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seu-ml-assign.tar.xz
Source438:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seu-ml-assign.doc.tar.xz
Source439:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seuthesis.tar.xz
Source440:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seuthesis.doc.tar.xz
Source441:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seuthesix.tar.xz
Source442:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seuthesix.doc.tar.xz
Source443:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sfee.tar.xz
Source444:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sfee.doc.tar.xz
Source445:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shortmathj.tar.xz
Source446:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shortmathj.doc.tar.xz
Source447:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shtthesis.tar.xz
Source448:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shtthesis.doc.tar.xz
Source449:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/smflatex.tar.xz
Source450:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/smflatex.doc.tar.xz
Source451:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soton.tar.xz
Source452:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soton.doc.tar.xz
Source453:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sphdthesis.tar.xz
Source454:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sphdthesis.doc.tar.xz
Source455:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spie.tar.xz
Source456:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spie.doc.tar.xz
Source457:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sr-vorl.tar.xz
Source458:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sr-vorl.doc.tar.xz
Source459:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/srdp-mathematik.tar.xz
Source460:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/srdp-mathematik.doc.tar.xz
Source461:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sshrc-insight.tar.xz
Source462:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sshrc-insight.doc.tar.xz
Source463:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stellenbosch.tar.xz
Source464:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stellenbosch.doc.tar.xz
Source465:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stellenbosch-2.tar.xz
Source466:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stellenbosch-2.doc.tar.xz
Source467:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suftesi.tar.xz
Source468:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suftesi.doc.tar.xz
Source469:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sugconf.tar.xz
Source470:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sugconf.doc.tar.xz
Source471:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sysuthesis.tar.xz
Source472:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sysuthesis.doc.tar.xz
Source473:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabriz-thesis.tar.xz
Source474:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabriz-thesis.doc.tar.xz
Source475:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/technion-thesis-template.tar.xz
Source476:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/technion-thesis-template.doc.tar.xz
Source477:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texilikechaps.tar.xz
Source478:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texilikecover.tar.xz
Source479:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-ekf.tar.xz
Source480:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-ekf.doc.tar.xz
Source481:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-gwu.tar.xz
Source482:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-gwu.doc.tar.xz
Source483:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-qom.tar.xz
Source484:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-qom.doc.tar.xz
Source485:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-titlepage-fhac.tar.xz
Source486:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thesis-titlepage-fhac.doc.tar.xz
Source487:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thuaslogos.tar.xz
Source488:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thuaslogos.doc.tar.xz
Source489:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thubeamer.tar.xz
Source490:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thubeamer.doc.tar.xz
Source491:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thucoursework.tar.xz
Source492:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thucoursework.doc.tar.xz
Source493:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thuthesis.tar.xz
Source494:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thuthesis.doc.tar.xz
Source495:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tidyres.tar.xz
Source496:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tidyres.doc.tar.xz
Source497:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tiet-question-paper.tar.xz
Source498:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tiet-question-paper.doc.tar.xz
Source499:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/timbreicmc.tar.xz
Source500:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/timbreicmc.doc.tar.xz
Source501:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlc-article.tar.xz
Source502:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlc-article.doc.tar.xz
Source503:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/topletter.tar.xz
Source504:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/topletter.doc.tar.xz
Source505:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/toptesi.tar.xz
Source506:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/toptesi.doc.tar.xz
Source507:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuda-ci.tar.xz
Source508:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuda-ci.doc.tar.xz
Source509:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tudscr.tar.xz
Source510:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tudscr.doc.tar.xz
Source511:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tugboat.tar.xz
Source512:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tugboat.doc.tar.xz
Source513:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tugboat-plain.tar.xz
Source514:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tugboat-plain.doc.tar.xz
Source515:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tui.tar.xz
Source516:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tui.doc.tar.xz
Source517:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turabian.tar.xz
Source518:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turabian.doc.tar.xz
Source519:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uaclasses.tar.xz
Source520:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uaclasses.doc.tar.xz
Source521:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uafthesis.tar.xz
Source522:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uafthesis.doc.tar.xz
Source523:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ualberta.tar.xz
Source524:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ualberta.doc.tar.xz
Source525:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uantwerpendocs.tar.xz
Source526:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uantwerpendocs.doc.tar.xz
Source527:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucalgmthesis.tar.xz
Source528:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucalgmthesis.doc.tar.xz
Source529:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucbthesis.tar.xz
Source530:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucbthesis.doc.tar.xz
Source531:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucdavisthesis.tar.xz
Source532:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucdavisthesis.doc.tar.xz
Source533:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucph-revy.tar.xz
Source534:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucph-revy.doc.tar.xz
Source535:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucsmonograph.tar.xz
Source536:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucsmonograph.doc.tar.xz
Source537:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucthesis.tar.xz
Source538:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucthesis.doc.tar.xz
Source539:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udepcolor.tar.xz
Source540:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udepcolor.doc.tar.xz
Source541:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udes-genie-these.tar.xz
Source542:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udes-genie-these.doc.tar.xz
Source543:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udiss.tar.xz
Source544:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udiss.doc.tar.xz
Source545:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uestcthesis.tar.xz
Source546:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uestcthesis.doc.tar.xz
Source547:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ufrgscca.tar.xz
Source548:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ufrgscca.doc.tar.xz
Source549:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhhassignment.tar.xz
Source550:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhhassignment.doc.tar.xz
Source551:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uiucredborder.tar.xz
Source552:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uiucredborder.doc.tar.xz
Source553:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uiucthesis.tar.xz
Source554:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uiucthesis.doc.tar.xz
Source555:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ukbill.tar.xz
Source556:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ukbill.doc.tar.xz
Source557:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ulthese.tar.xz
Source558:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ulthese.doc.tar.xz
Source559:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umbclegislation.tar.xz
Source560:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umbclegislation.doc.tar.xz
Source561:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umich-thesis.tar.xz
Source562:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umich-thesis.doc.tar.xz
Source563:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umthesis.tar.xz
Source564:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umthesis.doc.tar.xz
Source565:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unam-thesis.tar.xz
Source566:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unam-thesis.doc.tar.xz
Source567:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unamth-template.tar.xz
Source568:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unamth-template.doc.tar.xz
Source569:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unamthesis.tar.xz
Source570:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unamthesis.doc.tar.xz
Source571:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unbtex.tar.xz
Source572:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unbtex.doc.tar.xz
Source573:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unifith.tar.xz
Source574:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unifith.doc.tar.xz
Source575:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unigrazpub.tar.xz
Source576:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unigrazpub.doc.tar.xz
Source577:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unitn-bimrep.tar.xz
Source578:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unitn-bimrep.doc.tar.xz
Source579:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/univie-ling.tar.xz
Source580:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/univie-ling.doc.tar.xz
Source581:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unizgklasa.tar.xz
Source582:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unizgklasa.doc.tar.xz
Source583:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unswcover.tar.xz
Source584:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unswcover.doc.tar.xz
Source585:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uol-physics-report.tar.xz
Source586:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uol-physics-report.doc.tar.xz
Source587:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uothesis.tar.xz
Source588:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uothesis.doc.tar.xz
Source589:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uowthesis.tar.xz
Source590:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uowthesis.doc.tar.xz
Source591:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uowthesistitlepage.tar.xz
Source592:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uowthesistitlepage.doc.tar.xz
Source593:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/urcls.tar.xz
Source594:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/urcls.doc.tar.xz
Source595:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uspatent.tar.xz
Source596:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uspatent.doc.tar.xz
Source597:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ut-thesis.tar.xz
Source598:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ut-thesis.doc.tar.xz
Source599:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utexasthesis.tar.xz
Source600:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utexasthesis.doc.tar.xz
Source601:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uvaletter.tar.xz
Source602:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uvaletter.doc.tar.xz
Source603:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-colours.tar.xz
Source604:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-colours.doc.tar.xz
Source605:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-letterhead.tar.xz
Source606:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-letterhead.doc.tar.xz
Source607:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-pcf.tar.xz
Source608:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-pcf.doc.tar.xz
Source609:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-pif.tar.xz
Source610:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwa-pif.doc.tar.xz
Source611:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwthesis.tar.xz
Source612:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uwthesis.doc.tar.xz
Source613:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vancouver.tar.xz
Source614:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vancouver.doc.tar.xz
Source615:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wsemclassic.tar.xz
Source616:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wsemclassic.doc.tar.xz
Source617:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xduthesis.tar.xz
Source618:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xduthesis.doc.tar.xz
Source619:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xduts.tar.xz
Source620:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xduts.doc.tar.xz
Source621:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xmuthesis.tar.xz
Source622:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xmuthesis.doc.tar.xz
Source623:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yathesis.tar.xz
Source624:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yathesis.doc.tar.xz
Source625:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yazd-thesis.tar.xz
Source626:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yazd-thesis.doc.tar.xz
Source627:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yb-book.tar.xz
Source628:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yb-book.doc.tar.xz
Source629:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/york-thesis.tar.xz
Source630:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/york-thesis.doc.tar.xz

# Patches
Patch0:         texlive-proposal-no-workaddress.patch
Patch1:         texlive-bgteubner-scrpage2-obsolete-fixes.patch
Patch2:         texlive-mentis-scrpage2-obsolete-fixes.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-aastex
Requires:       texlive-abnt
Requires:       texlive-abntex2
Requires:       texlive-abntexto
Requires:       texlive-abntexto-uece
Requires:       texlive-acmart
Requires:       texlive-acmconf
Requires:       texlive-active-conf
Requires:       texlive-adfathesis
Requires:       texlive-aeskwadraat
Requires:       texlive-afthesis
Requires:       texlive-aguplus
Requires:       texlive-aiaa
Requires:       texlive-amnestyreport
Requires:       texlive-anonymous-acm
Requires:       texlive-anufinalexam
Requires:       texlive-aomart
Requires:       texlive-apa
Requires:       texlive-apa6
Requires:       texlive-apa6e
Requires:       texlive-apa7
Requires:       texlive-arsclassica
Requires:       texlive-articleingud
Requires:       texlive-asaetr
Requires:       texlive-ascelike
Requires:       texlive-asmeconf
Requires:       texlive-asmejour
Requires:       texlive-aucklandthesis
Requires:       texlive-bangorcsthesis
Requires:       texlive-bangorexam
Requires:       texlive-bath-bst
Requires:       texlive-beamer-fuberlin
Requires:       texlive-beamer-verona
Requires:       texlive-beilstein
Requires:       texlive-bfh-ci
Requires:       texlive-bgteubner
Requires:       texlive-bjfuthesis
Requires:       texlive-bmstu
Requires:       texlive-bmstu-iu8
Requires:       texlive-br-lex
Requires:       texlive-brandeis-dissertation
Requires:       texlive-brandeis-problemset
Requires:       texlive-brandeis-thesis
Requires:       texlive-buctthesis
Requires:       texlive-cascadilla
Requires:       texlive-cesenaexam
Requires:       texlive-chem-journal
Requires:       texlive-chifoot
Requires:       texlive-chs-physics-report
Requires:       texlive-cidarticle
Requires:       texlive-cje
Requires:       texlive-cjs-rcs-article
Requires:       texlive-classicthesis
Requires:       texlive-cleanthesis
Requires:       texlive-cmpj
Requires:       texlive-collection-latex
Requires:       texlive-confproc
Requires:       texlive-contract
Requires:       texlive-cqjtuthesis
Requires:       texlive-cquthesis
Requires:       texlive-dccpaper
Requires:       texlive-dithesis
Requires:       texlive-dlrg-templates
Requires:       texlive-ebook
Requires:       texlive-ebsthesis
Requires:       texlive-ecothesis
Requires:       texlive-edmaths
Requires:       texlive-ejpecp
Requires:       texlive-ekaia
Requires:       texlive-elbioimp
Requires:       texlive-els-cas-templates
Requires:       texlive-elsarticle
Requires:       texlive-elteiktdk
Requires:       texlive-elteikthesis
Requires:       texlive-emisa
Requires:       texlive-erdc
Requires:       texlive-estcpmm
Requires:       texlive-etsvthor
Requires:       texlive-facture-belge-simple-sans-tva
Requires:       texlive-fbithesis
Requires:       texlive-fcavtex
Requires:       texlive-fcltxdoc
Requires:       texlive-fei
Requires:       texlive-fhj-script
Requires:       texlive-ftc-notebook
Requires:       texlive-gaceta
Requires:       texlive-gammas
Requires:       texlive-geradwp
Requires:       texlive-gfdl
Requires:       texlive-gradstudentresume
Requires:       texlive-grant
Requires:       texlive-gsemthesis
Requires:       texlive-gzt
Requires:       texlive-h2020proposal
Requires:       texlive-hagenberg-thesis
Requires:       texlive-har2nat
Requires:       texlive-hduthesis
Requires:       texlive-hecthese
Requires:       texlive-hep-paper
Requires:       texlive-heria
Requires:       texlive-hfutexam
Requires:       texlive-hfutthesis
Requires:       texlive-hithesis
Requires:       texlive-hitszbeamer
Requires:       texlive-hitszthesis
Requires:       texlive-hobete
Requires:       texlive-hu-berlin-bundle
Requires:       texlive-hustthesis
Requires:       texlive-hustvisual
Requires:       texlive-iaria
Requires:       texlive-iaria-lite
Requires:       texlive-icsv
Requires:       texlive-ieeeconf
Requires:       texlive-ieeepes
Requires:       texlive-ieeetran
Requires:       texlive-ijmart
Requires:       texlive-ijsra
Requires:       texlive-imac
Requires:       texlive-imtekda
Requires:       texlive-inkpaper
Requires:       texlive-iodhbwm
Requires:       texlive-iscram
Requires:       texlive-jacow
Requires:       texlive-jmlr
Requires:       texlive-jnuexam
Requires:       texlive-jourcl
Requires:       texlive-jourrr
Requires:       texlive-jpsj
Requires:       texlive-jsonresume
Requires:       texlive-jwjournal
Requires:       texlive-kdgdocs
Requires:       texlive-kdpcover
Requires:       texlive-kfupm-math-exam
Requires:       texlive-kluwer
Requires:       texlive-ksp-thesis
Requires:       texlive-ku-template
Requires:       texlive-langsci
Requires:       texlive-langsci-avm
Requires:       texlive-limecv
Requires:       texlive-lion-msc
Requires:       texlive-llncs
Requires:       texlive-llncsconf
Requires:       texlive-lni
Requires:       texlive-lps
Requires:       texlive-maine-thesis
Requires:       texlive-matc3
Requires:       texlive-matc3mem
Requires:       texlive-mcmthesis
Requires:       texlive-mentis
Requires:       texlive-mitthesis
Requires:       texlive-mlacls
Requires:       texlive-mluexercise
Requires:       texlive-mnras
Requires:       texlive-modeles-factures-belges-assocs
Requires:       texlive-modernnewspaper
Requires:       texlive-msu-thesis
Requires:       texlive-mucproc
Requires:       texlive-mugsthesis
Requires:       texlive-muling
Requires:       texlive-musuos
Requires:       texlive-muthesis
Requires:       texlive-mynsfc
Requires:       texlive-nature
Requires:       texlive-navydocs
Requires:       texlive-nddiss
Requires:       texlive-ndsu-thesis
Requires:       texlive-ndsu-thesis-2022
Requires:       texlive-nih
Requires:       texlive-nihbiosketch
Requires:       texlive-njustthesis
Requires:       texlive-njuthesis
Requires:       texlive-njuvisual
Requires:       texlive-nostarch
Requires:       texlive-novel
Requires:       texlive-nrc
Requires:       texlive-nstc-proposal
Requires:       texlive-nwafuthesis
Requires:       texlive-nwejm
Requires:       texlive-nxuthesis
Requires:       texlive-omgtudoc-asoiu
Requires:       texlive-onrannual
Requires:       texlive-opteng
Requires:       texlive-oststud
Requires:       texlive-ou-tma
Requires:       texlive-oup-authoring-template
Requires:       texlive-pats-resume
Requires:       texlive-philosophersimprint
Requires:       texlive-phimisci
Requires:       texlive-pittetd
Requires:       texlive-pkuthss
Requires:       texlive-powerdot-fuberlin
Requires:       texlive-powerdot-tuliplab
Requires:       texlive-pracjourn
Requires:       texlive-prociagssymp
Requires:       texlive-proposal
Requires:       texlive-prtec
Requires:       texlive-ptptex
Requires:       texlive-qrbill
Requires:       texlive-quantumarticle
Requires:       texlive-rebuttal
Requires:       texlive-regulatory
Requires:       texlive-resphilosophica
Requires:       texlive-resumecls
Requires:       texlive-retosmatematicos
Requires:       texlive-revtex
Requires:       texlive-revtex4
Requires:       texlive-revtex4-1
Requires:       texlive-rub-kunstgeschichte
Requires:       texlive-rutitlepage
Requires:       texlive-rwth-ci
Requires:       texlive-ryersonsgsthesis
Requires:       texlive-ryethesis
Requires:       texlive-sageep
Requires:       texlive-sapthesis
Requires:       texlive-schule
Requires:       texlive-scientific-thesis-cover
Requires:       texlive-scripture
Requires:       texlive-scrjrnl
Requires:       texlive-sduthesis
Requires:       texlive-se2thesis
Requires:       texlive-seu-ml-assign
Requires:       texlive-seuthesis
Requires:       texlive-seuthesix
Requires:       texlive-sfee
Requires:       texlive-shortmathj
Requires:       texlive-shtthesis
Requires:       texlive-smflatex
Requires:       texlive-soton
Requires:       texlive-sphdthesis
Requires:       texlive-spie
Requires:       texlive-sr-vorl
Requires:       texlive-srdp-mathematik
Requires:       texlive-sshrc-insight
Requires:       texlive-stellenbosch
Requires:       texlive-stellenbosch-2
Requires:       texlive-suftesi
Requires:       texlive-sugconf
Requires:       texlive-sysuthesis
Requires:       texlive-tabriz-thesis
Requires:       texlive-technion-thesis-template
Requires:       texlive-texilikechaps
Requires:       texlive-texilikecover
Requires:       texlive-thesis-ekf
Requires:       texlive-thesis-gwu
Requires:       texlive-thesis-qom
Requires:       texlive-thesis-titlepage-fhac
Requires:       texlive-thuaslogos
Requires:       texlive-thubeamer
Requires:       texlive-thucoursework
Requires:       texlive-thuthesis
Requires:       texlive-tidyres
Requires:       texlive-tiet-question-paper
Requires:       texlive-timbreicmc
Requires:       texlive-tlc-article
Requires:       texlive-topletter
Requires:       texlive-toptesi
Requires:       texlive-tuda-ci
Requires:       texlive-tudscr
Requires:       texlive-tugboat
Requires:       texlive-tugboat-plain
Requires:       texlive-tui
Requires:       texlive-turabian
Requires:       texlive-uaclasses
Requires:       texlive-uafthesis
Requires:       texlive-ualberta
Requires:       texlive-uantwerpendocs
Requires:       texlive-ucalgmthesis
Requires:       texlive-ucbthesis
Requires:       texlive-ucdavisthesis
Requires:       texlive-ucph-revy
Requires:       texlive-ucsmonograph
Requires:       texlive-ucthesis
Requires:       texlive-udepcolor
Requires:       texlive-udes-genie-these
Requires:       texlive-udiss
Requires:       texlive-uestcthesis
Requires:       texlive-ufrgscca
Requires:       texlive-uhhassignment
Requires:       texlive-uiucredborder
Requires:       texlive-uiucthesis
Requires:       texlive-ukbill
Requires:       texlive-ulthese
Requires:       texlive-umbclegislation
Requires:       texlive-umich-thesis
Requires:       texlive-umthesis
Requires:       texlive-unam-thesis
Requires:       texlive-unamth-template
Requires:       texlive-unamthesis
Requires:       texlive-unbtex
Requires:       texlive-unifith
Requires:       texlive-unigrazpub
Requires:       texlive-unitn-bimrep
Requires:       texlive-univie-ling
Requires:       texlive-unizgklasa
Requires:       texlive-unswcover
Requires:       texlive-uol-physics-report
Requires:       texlive-uothesis
Requires:       texlive-uowthesis
Requires:       texlive-uowthesistitlepage
Requires:       texlive-urcls
Requires:       texlive-uspatent
Requires:       texlive-ut-thesis
Requires:       texlive-utexasthesis
Requires:       texlive-uvaletter
Requires:       texlive-uwa-colours
Requires:       texlive-uwa-letterhead
Requires:       texlive-uwa-pcf
Requires:       texlive-uwa-pif
Requires:       texlive-uwthesis
Requires:       texlive-vancouver
Requires:       texlive-wsemclassic
Requires:       texlive-xduthesis
Requires:       texlive-xduts
Requires:       texlive-xmuthesis
Requires:       texlive-yathesis
Requires:       texlive-yazd-thesis
Requires:       texlive-yb-book
Requires:       texlive-york-thesis

%description
Publisher styles, theses, etc.


%package -n texlive-aastex
Summary:        Macros for Manuscript Preparation for AAS Journals
Version:        svn75970
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-aastex
The package provides a document class for preparing papers for American
Astronomical Society publications. Authors who wish to submit papers to AAS
journals are strongly urged to use this class in preference to any of the
alternatives available.

%package -n texlive-abnt
Summary:        Typesetting academic works according to ABNT rules
Version:        svn55471
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(caption.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(emptypage.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(newfloat.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tocbasic.sty)
Provides:       tex(abnt.sty) = %{tl_version}

%description -n texlive-abnt
The ABNT package provides a clean and practical implementation of the ABNT
rules for academic texts. Its purpose is to be as simple and user-friendly as
possible.

%package -n texlive-abntex2
Summary:        Typeset technical and scientific Brazilian documents based on ABNT rules
Version:        svn49248
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(breakurl.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(relsize.sty)
Requires:       tex(setspace.sty)
Requires:       tex(url.sty)
Provides:       tex(abntex2abrev.sty) = %{tl_version}
Provides:       tex(abntex2cite.sty) = %{tl_version}

%description -n texlive-abntex2
The bundle provides support for typesetting technical and scientific Brazilian
documents (like academic thesis, articles, reports, research project and
others) based on the ABNT rules (Associacao Brasileira de Normas Tecnicas). It
replaces the old abntex.

%package -n texlive-abntexto
Summary:        LaTeX class for formatting academic papers in ABNT standards
Version:        svn76889
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-abntexto
This is a LaTeX class created for Brazilian students to facilitate the use of
standards from the Associacao Brasileira de Normas Tecnicas (ABNT) in academic
works like TCCs, dissertations, theses.

%package -n texlive-abntexto-uece
Summary:        LaTeX class for formatting academic papers in UECE standards
Version:        svn76157
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-abntexto-uece
This is a unofficial LaTeX class created for Brazilian students to facilitate
the use of standards from the Universidade Estadual do Ceara (UECE) in academic
works like TCCs, dissertations, and theses.

%package -n texlive-acmart
Summary:        Class for typesetting publications of ACM
Version:        svn76177
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(numeric.cbx)
Requires:       tex(trad-plain.bbx)
Requires:       tex(xpatch.sty)
Provides:       tex(acmauthoryear.bbx) = %{tl_version}
Provides:       tex(acmauthoryear.cbx) = %{tl_version}
Provides:       tex(acmnumeric.bbx) = %{tl_version}
Provides:       tex(acmnumeric.cbx) = %{tl_version}

%description -n texlive-acmart
This package provides a class for typesetting publications of the Association
for Computing Machinery (ACM).

%package -n texlive-acmconf
Summary:        Class for ACM conference proceedings
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-acmconf
This class may be used to typeset articles to be published in the proceedings
of ACM (Association for Computing Machinery) conferences and workshops. The
layout produced by the acmconf class is based on the ACM's own specification.

%package -n texlive-active-conf
Summary:        Class for typesetting ACTIVE conference papers
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-active-conf
Active-conf is a class for typesetting papers for the Active conference on
noise and vibration control. It is initially intended for the 2006 conference
in Adelaide, Australia. The class is based on article with more flexible
front-matter, and can be customised for conferences in future years with a
header file.

%package -n texlive-adfathesis
Summary:        Australian Defence Force Academy thesis format
Version:        svn26048
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-adfathesis
The bundle includes a BibTeX style file.

%package -n texlive-aeskwadraat
Summary:        A-Eskwadraat package catalogue
Version:        svn75506
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(merriweather.sty)
Requires:       tex(substr.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tikzducks.sty)
Requires:       tex(xspace.sty)
Provides:       tex(aes.sty) = %{tl_version}
Provides:       tex(aeskwadraat.sty) = %{tl_version}
Provides:       tex(aeskwadraatfactuur.sty) = %{tl_version}
Provides:       tex(aeskwadraatnotulen.sty) = %{tl_version}
Provides:       tex(aeskwadraattaal.sty) = %{tl_version}
Provides:       tex(beamerthemeaes2.sty) = %{tl_version}
Provides:       tex(beamerthemeaeskwadraat.sty) = %{tl_version}

%description -n texlive-aeskwadraat
This is the official package catalogue of the A-Eskwadraat association.
A-Eskwadraat is the study association for mathematics and physics at Utrecht
University. The catalogue includes packages for meeting notes, a beamer theme,
invoices and letters. The beamer theme can also be used for Utrecht
University-styled presentations. Do refer to the UU website for information on
logo use.

%package -n texlive-afthesis
Summary:        Air Force Institute of Technology thesis class
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(afthes10.sty) = %{tl_version}
Provides:       tex(afthes11.sty) = %{tl_version}
Provides:       tex(afthes12.sty) = %{tl_version}
Provides:       tex(afthesis.sty) = %{tl_version}

%description -n texlive-afthesis
LaTeX thesis/dissertation class for US Air Force Institute Of Technology.

%package -n texlive-aguplus
Summary:        Styles for American Geophysical Union
Version:        svn17156
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(aguplus.sty) = %{tl_version}
Provides:       tex(agupp.sty) = %{tl_version}

%description -n texlive-aguplus
This bundle started as an extension to the AGU's own published styles,
providing extra facilities and improved usability. The AGU now publishes
satisfactory LaTeX materials of its own; the author of aguplus recommends that
users switch to using the official distribution.

%package -n texlive-aiaa
Summary:        Typeset AIAA conference papers
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-aiaa
A bundle of LaTeX/BibTeX files and sample documents to aid those producing
papers and journal articles according to the guidelines of the American
Institute of Aeronautics and Astronautics (AIAA).

%package -n texlive-amnestyreport
Summary:        A LaTeX class for Amnesty International
Version:        svn69439
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-amnestyreport
This package provides a class for Amnesty International reports according to
guidelines at https://brandhub.amnesty.org/.

%package -n texlive-anonymous-acm
Summary:        Typeset anonymous versions for ACM articles
Version:        svn55121
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(anonymous-acm.sty) = %{tl_version}

%description -n texlive-anonymous-acm
Academics often need to submit anonymous versions of their papers for
peer-review. This often requires anonymization which at some future date needs
to be reversed. However de-anonymizing an anonymized paper can be laborious and
error-prone. This LaTeX package allows anonymization options to be specified at
the time of writing for authors using acmart.cls, the official Association of
Computing Machinery (ACM) master article template. Anonymization or
deanonymization is carried out by simply changing one option and recompiling.

%package -n texlive-anufinalexam
Summary:        LaTeX document shell for ANU final exam
Version:        svn26053
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-anufinalexam-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-anufinalexam-doc <= 11:%{version}

%description -n texlive-anufinalexam
This LaTeX document shell is created for the standard formatting of final exams
in The Australian National University.

%package -n texlive-apa
Summary:        American Psychological Association format
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-apa
A LaTeX class to format text according to the American Psychological
Association Publication Manual (5th ed.) specifications for manuscripts or to
the APA journal look found in journals like the Journal of Experimental
Psychology etc. In addition, it provides regular LaTeX-like output with a few
enhancements and APA-motivated changes. Note that the apa7 class (covering the
7th edition of the manual) and apa6 (covering the 6th edition of the manual)
are now commonly in use. Apacite, which used to work with this class, has been
updated for use with apa6.

%package -n texlive-apa6
Summary:        Format documents in APA style (6th edition)
Version:        svn67848
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-apa6
The class formats documents in APA style (6th Edition). It provides a full set
of facilities in three different output modes (journal-like appearance,
double-spaced manuscript, LaTeX-like document), in contrast to the earlier
apa6e, which only formats double-spaced manuscripts in APA style. The class can
mask author identity for copies for use in masked peer review. The class is a
development of the apa class (which is no longer maintained).

%package -n texlive-apa6e
Summary:        Format manuscripts to APA 6th edition guidelines
Version:        svn23350
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-apa6e
This is a minimalist class file for formatting manuscripts in the style
described in the American Psychological Association (APA) 6th edition
guidelines. The apa6 class provides better coverage of the requirements.

%package -n texlive-apa7
Summary:        Format documents in APA style (7th edition)
Version:        svn63974
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-apa7
This class formats documents in APA style (7th Edition). It provides a full set
of facilities in four different output modes (journal-like appearance,
double-spaced manuscript, double-spaced student manuscript, LaTeX-like
document). The class can mask author identity for copies for use in masked peer
review. The class is a development of the apa6 class.

%package -n texlive-arsclassica
Summary:        A different view of the ClassicThesis package
Version:        svn45656
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(caption.sty)
Requires:       tex(classicthesis.sty)
Requires:       tex(soul.sty)
Requires:       tex(titlesec.sty)
Provides:       tex(arsclassica.sty) = %{tl_version}

%description -n texlive-arsclassica
The package changes some typographical points of the ClassicThesis style, by
Andre Miede. It enables the user to reproduce the look of the guide The art of
writing with LaTeX (the web page is in Italian).

%package -n texlive-articleingud
Summary:        LaTeX class for articles published in INGENIERIA review
Version:        svn38741
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-articleingud
The class is for articles published in INGENIERIA review. It is derived from
the standard LaTeX class article.

%package -n texlive-asaetr
Summary:        Transactions of the ASAE
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(asaesub.sty) = %{tl_version}
Provides:       tex(asaetr.sty) = %{tl_version}

%description -n texlive-asaetr
A class and BibTeX style for submissions to the Transactions of the American
Society of Agricultural Engineers. Also included is the Metafont source of a
slanted Computer Modern Caps and Small Caps font.

%package -n texlive-ascelike
Summary:        Bibliography style for the ASCE
Version:        svn75662
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(standard.bbx)
Provides:       tex(ascelike.bbx) = %{tl_version}
Provides:       tex(ascelike.cbx) = %{tl_version}

%description -n texlive-ascelike
A document class and bibliographic style that prepares documents in the style
required by the American Society of Civil Engineers (ASCE). These are
unofficial files, not sanctioned by that organization, and the files
specifically give this caveat. Also included is a short documentation/example
of how to use the class.

%package -n texlive-asmeconf
Summary:        A LaTeX template for ASME conference papers
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-asmeconf
The asmeconf class provides a LaTeX template for ASME conference papers,
following ASME's guidelines for margins, fonts, headings, captions, and
reference formats as of 2025. This LaTeX template is intended to be used with
the asmeconf.bst BibTeX style, for reference formatting, which is part of this
distribution. Unlike older ASME conference LaTeX templates, asmeconf pdfs will
contain hyperlinks, bookmarks, and metadata; and the references can include the
DOI and URL fields. This LaTeX template enables inline author names, following
ASME's current style, but it can also produce the traditional grid style.
Options include line numbering, final column balancing, various math options,
government copyright, archivability and accessibility (PDF/A), and multilingual
support. The code is compatible with pdfLaTeX or LuaLaTeX. This LaTeX template
is not a publication of ASME, but it does conform to ASME's currently published
guidelines for conference papers.

%package -n texlive-asmejour
Summary:        A template for ASME journal papers
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-asmejour
The asmejour class provides a template to format preprints submitted to ASME
journals. The layout and reference formats closely follow the style that is
currently being used for published papers. The class is intended to be used
with the asmejour.bst BibTeX style, which is part of this distribution. Unlike
older ASME LaTeX templates, asmejour pdfs will contain hyperlinks, bookmarks,
and metadata, and references can include the DOI and URL fields. Options
include line numbering, final column balancing, various math options,
government copyright, and accessibility (PDF/A). The class is compatible with
pdfLaTeX or LuaLaTeX. This package is not a publication of ASME.

%package -n texlive-aucklandthesis
Summary:        Memoir-based class for formatting University of Auckland masters' and doctors' theses
Version:        svn51323
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-aucklandthesis
A memoir-based class for formatting University of Auckland masters' and
doctors' thesis dissertations in any discipline. The title page does not handle
short dissertations for diplomas.

%package -n texlive-bangorcsthesis
Summary:        Typeset a thesis at Bangor University
Version:        svn75154
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bangorcsthesis
The class typesets thesis/dissertation documents for all levels (i.e., both
undergraduate and graduate students may use the class). It also provides macros
designed to optimise the process of producing a thesis.

%package -n texlive-bangorexam
Summary:        Typeset an examination at Bangor University
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bangorexam
The package allows typesetting of Bangor University's exam style. It currently
supports a standard A/B choice, A-only compulsory and 'n' from 'm' exam styles.
Marks are totalled and checked automatically.

%package -n texlive-bath-bst
Summary:        Harvard referencing style as recommended by the University of Bath Library
Version:        svn77532
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bath-bst
This package provides a BibTeX style to format reference lists in the Harvard
style recommended by the University of Bath Library. It should be used in
conjunction with natbib for citations.

%package -n texlive-beamer-fuberlin
Summary:        Beamer, using the style of FU Berlin
Version:        svn63161
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(beamercolorthemeBerlinFU.sty) = %{tl_version}
Provides:       tex(beamerfontthemeBerlinFU.sty) = %{tl_version}
Provides:       tex(beamerouterthemeBerlinFU.sty) = %{tl_version}
Provides:       tex(beamerthemeBerlinFU.sty) = %{tl_version}

%description -n texlive-beamer-fuberlin
The bundle provides a beamer-derived class and a theme style file for the
corporate design of the Free University in Berlin. Users may use the class
itself (FUbeamer) or use the theme in the usual way with \usetheme{BerlinFU}.
Examples of using both the class and the theme are provided; the PDF is
visually identical, so the catalogue only lists one; the sources of the
examples do of course differ.

%package -n texlive-beamer-verona
Summary:        A theme for the beamer class
Version:        svn39180
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Provides:       tex(beamerthemeVerona.sty) = %{tl_version}

%description -n texlive-beamer-verona
This package provides the 'Verona' theme for the beamer class by Till Tantau.

%package -n texlive-beilstein
Summary:        Support for submissions to the "Beilstein Journal of Nanotechnology"
Version:        svn56193
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-beilstein
The package provides a LaTeX class file and a BibTeX style file in accordance
with the requirements of submissions to the ``Beilstein Journal of
Nanotechnology''. Although the files can be used for any kind of document, they
have only been designed and tested to be suitable for submissions to the
Beilstein Journal of Nanotechnology.

%package -n texlive-bfh-ci
Summary:        Corporate Design for Bern University of Applied Sciences
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-adjustbox
Requires:       texlive-amsfonts
Requires:       texlive-amsmath
Requires:       texlive-anyfontsize
Requires:       texlive-beamer
Requires:       texlive-fontawesome
Requires:       texlive-fontspec
Requires:       texlive-geometry
Requires:       texlive-graphics
Requires:       texlive-handoutwithnotes
Requires:       texlive-hyperref
Requires:       texlive-iftex
Requires:       texlive-koma-script
Requires:       texlive-l3kernel
Requires:       texlive-l3packages
Requires:       texlive-listings
Requires:       texlive-nunito
Requires:       texlive-pgf
Requires:       texlive-qrcode
Requires:       texlive-sourceserifpro
Requires:       texlive-tcolorbox
Requires:       texlive-tools
Requires:       texlive-translations
Requires:       texlive-url
Requires:       texlive-xcolor
Requires:       texlive-zref
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(anyfontsize.sty)
# Ignoring dependency on bfhlogo.sty - not part of TeX Live
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(nunito.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(scrletter.sty)
Requires:       tex(sourceserifpro.sty)
Requires:       tex(translations.sty)
Requires:       tex(trimclip.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(zref.sty)
Provides:       tex(beamercolorthemeBFH.sty) = %{tl_version}
Provides:       tex(beamerfontthemeBFH.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeBFH.sty) = %{tl_version}
Provides:       tex(beamerouterthemeBFH-sidebar.sty) = %{tl_version}
Provides:       tex(beamerouterthemeBFH.sty) = %{tl_version}
Provides:       tex(beamerthemeBFH.sty) = %{tl_version}
Provides:       tex(bfhcolors.sty) = %{tl_version}
Provides:       tex(bfhfonts.sty) = %{tl_version}
Provides:       tex(bfhlayout.sty) = %{tl_version}
Provides:       tex(bfhletter.sty) = %{tl_version}
Provides:       tex(bfhmodule.sty) = %{tl_version}

%description -n texlive-bfh-ci
This bundle provides possibilities to use the Corporate Design of Bern
University of Applied Sciences (BFH) with LaTeX. To this end it contains
classes as well as some helper packages and config files together with some
demo files.

%package -n texlive-bgteubner
Summary:        Class for producing books for the publisher "Teubner Verlag"
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathcomp.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(hhfixme.sty) = %{tl_version}
Provides:       tex(hhsubfigure.sty) = %{tl_version}
Provides:       tex(ptmxcomp.sty) = %{tl_version}

%description -n texlive-bgteubner
The bgteubner document class has been programmed by order of the Teubner
Verlag, Wiesbaden, Germany, to ensure that books of this publisher have a
unique layout. Unfortunately, most of the documentation is only available in
German. Since the document class is intended to generate a unique layout, many
things (layout etc.) are fixed and cannot be altered by the user. If you want
to use the document class for another purpose than publishing with the Teubner
Verlag, this may arouse unwanted restrictions (for instance, the document class
provides only two paper sizes: DIN A5 and 17cm x 24cm; only two font families
are supported: Times and European Computer Modern).

%package -n texlive-bjfuthesis
Summary:        A thesis class for Beijing Forestry University
Version:        svn59809
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bjfuthesis
This is a class file for producing dissertations and theses according to the
Beijing Forestry University (BJFU) Guidelines for Undergraduate Theses and
Dissertations. The class should meet all current requirements and is updated
whenever the university guidelines change.

%package -n texlive-bmstu
Summary:        A LaTeX class for Bauman Moscow State Technical University
Version:        svn65897
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(appendix.sty)
Requires:       tex(assoccnt.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(float.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(listings.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(tikzscale.sty)
Requires:       tex(totcount.sty)
Requires:       tex(ulem.sty)
Requires:       tex(wrapfig.sty)
Provides:       tex(bmstu-appendix.sty) = %{tl_version}
Provides:       tex(bmstu-biblio.sty) = %{tl_version}
Provides:       tex(bmstu-defabbr.sty) = %{tl_version}
Provides:       tex(bmstu-essay.sty) = %{tl_version}
Provides:       tex(bmstu-figure.sty) = %{tl_version}
Provides:       tex(bmstu-listing.sty) = %{tl_version}
Provides:       tex(bmstu-title.sty) = %{tl_version}
Provides:       tex(bmstu-toc.sty) = %{tl_version}

%description -n texlive-bmstu
The class defines commands and environments for creating reports and
explanatory notes in Bauman Moscow State Technical University (Russia). Klass
opredeliaet komandy i okruzheniia dlia sozdaniia otchetov i
raschetno-poiasnitel'nykh zapisok v MGTU im. N. E. Baumana. Sgenerirovannye
faily sootvetstvuiut trebovaniiam MGTU im. N. E. Baumanai GOST 7.32-2017.
Raschetno-poiasnitel'nye zapiski k vypusknym kvalifikatsionnym rabotam uspeshno
prokhodiat proverku TestVKR (sborka 203).

%package -n texlive-bmstu-iu8
Summary:        A class for IU8 reports
Version:        svn76373
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-algorithm2e
Requires:       texlive-amscls
Requires:       texlive-anyfontsize
Requires:       texlive-babel
Requires:       texlive-biblatex
Requires:       texlive-bookmark
Requires:       texlive-caption
Requires:       texlive-chngcntr
Requires:       texlive-csquotes
Requires:       texlive-enumitem
Requires:       texlive-fancyhdr
Requires:       texlive-float
Requires:       texlive-fontspec
Requires:       texlive-geometry
Requires:       texlive-glossaries
Requires:       texlive-glossaries-extra
Requires:       texlive-graphics
Requires:       texlive-ifoddpage
Requires:       texlive-koma-script
Requires:       texlive-lastpage
Requires:       texlive-lineno
Requires:       texlive-listings
Requires:       texlive-ltablex
Requires:       texlive-multirow
Requires:       texlive-nowidow
Requires:       texlive-oberdiek
Requires:       texlive-relsize
Requires:       texlive-setspace
Requires:       texlive-stackengine
Requires:       texlive-tabto-ltx
Requires:       texlive-titlesec
Requires:       texlive-tools
Requires:       texlive-totcount
Requires:       texlive-ulem
Requires:       texlive-xassoccnt
Requires:       texlive-xcolor
Requires:       texlive-xltabular
Requires:       texlive-xstring
Requires:       tex(amsthm.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(geometry.sty)
Requires:       tex(glossaries-extra.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hhline.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(lineno.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(multirow.sty)
Requires:       tex(nowidow.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(setspace.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(tabto.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(totcount.sty)
Requires:       tex(ulem.sty)
Requires:       tex(xassoccnt.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xltabular.sty)
Requires:       tex(xstring.sty)
Provides:       tex(IU8-01-base.sty) = %{tl_version}
Provides:       tex(IU8-02-construction.sty) = %{tl_version}
Provides:       tex(IU8-03-numbering.sty) = %{tl_version}
Provides:       tex(IU8-04-section-numbering.sty) = %{tl_version}
Provides:       tex(IU8-05-figures.sty) = %{tl_version}
Provides:       tex(IU8-06-tables.sty) = %{tl_version}
Provides:       tex(IU8-07-footnotes.sty) = %{tl_version}
Provides:       tex(IU8-08-formulas.sty) = %{tl_version}
Provides:       tex(IU8-09-cites.sty) = %{tl_version}
Provides:       tex(IU8-10-titlepage.sty) = %{tl_version}
Provides:       tex(IU8-11-performers.sty) = %{tl_version}
Provides:       tex(IU8-12-abstract.sty) = %{tl_version}
Provides:       tex(IU8-13-contents.sty) = %{tl_version}
Provides:       tex(IU8-14-terms-and-definitions.sty) = %{tl_version}
Provides:       tex(IU8-15-list-of-abbreviations.sty) = %{tl_version}
Provides:       tex(IU8-16-references.sty) = %{tl_version}
Provides:       tex(IU8-17-appendices.sty) = %{tl_version}
Provides:       tex(IU8-18-extra.sty) = %{tl_version}
Provides:       tex(IU8-19-counters.sty) = %{tl_version}
Provides:       tex(IU8-20-listing.sty) = %{tl_version}
Provides:       tex(IU8-21-math.sty) = %{tl_version}
Provides:       tex(IU8-22-algorithms.sty) = %{tl_version}

%description -n texlive-bmstu-iu8
This package consists of a class file and style files for writing reports at
the IU8 department of IU faculty of BMSTU (Bauman Moscow State Technical
University). The class defines all headings, structure elements and other
things in respect of Russian standard GOST 7.32-2017. But there are correctives
to be compatible with our local IU8 department requirements.

%package -n texlive-br-lex
Summary:        A Class for Typesetting Brazilian legal texts
Version:        svn44939
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-br-lex
This class implements rules to typeset Brazilian legal texts. Its purpose is to
be an easy-to-use implementation for the end-user.

%package -n texlive-brandeis-dissertation
Summary:        Class for Brandeis University dissertations
Version:        svn67935
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-brandeis-dissertation
The class will enable the user to typeset a dissertation which adheres to the
formatting guidelines of Brandeis University Graduate School of Arts and
Sciences (GSAS).

%package -n texlive-brandeis-problemset
Summary:        Document class for COSI Problem sets at Brandeis University (Waltham, MA)
Version:        svn50991
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(changepage.sty)
Requires:       tex(comment.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fp.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(brandeis-problemset.sty) = %{tl_version}

%description -n texlive-brandeis-problemset
Brandeis University's computer science ("COSI") courses often assign "problem
sets" which require fairly rigorous formatting. This document class, which
extends article, provides a simple way to typeset these problem sets in LaTeX.
Although the class is compatible with all LaTeX flavors, XeLaTeX or LuaLaTeX
are recommended for fontspec support.

%package -n texlive-brandeis-thesis
Summary:        A class for Brandeis University M.A. theses
Version:        svn68092
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-brandeis-thesis
brandeis-thesis.cls provides the structures and formatting information for an
M.A. thesis for the Brandeis University Graduate School of Arts and Sciences.

%package -n texlive-buctthesis
Summary:        Beijing University of Chemical Technology Thesis Template
Version:        svn67818
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-buctthesis
This package provides a LaTeX class and template for Beijing University of
Chemical Technology, supporting bachelor, master, and doctor theses.

%package -n texlive-cascadilla
Summary:        Typeset papers conforming to the stylesheet of the Cascadilla Proceedings Project
Version:        svn25144
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cascadilla
The class provides an extension of the standard LaTeX article class that may be
used to typeset papers conforming to the stylesheet of the Cascadilla
Proceedings Project, which is used by a number of linguistics conference
proceedings (e.g., WCCFL).

%package -n texlive-cesenaexam
Summary:        A class file to typeset exams
Version:        svn44960
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(circuitikz.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(titlesec.sty)
Provides:       tex(cesenaexam.sty) = %{tl_version}

%description -n texlive-cesenaexam
This LaTeX document class has been designed to typeset exams.

%package -n texlive-chem-journal
Summary:        Various BibTeX formats for journals in Chemistry
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-chem-journal
Various BibTeX formats for journals in Chemistry, including Reviews in
Computational Chemistry, Journal of Physical Chemistry, Journal of
Computational Chemistry, and Physical Chemistry Chemical Physics.

%package -n texlive-chifoot
Summary:        Chicago-style footnote formatting
Version:        svn57312
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chifoot.sty) = %{tl_version}

%description -n texlive-chifoot
A very short snippet. Will set the footnotes to be conformant with the Chicago
style, so the footnotes at the bottom of the page are now marked with a
full-sized number, rather than with a superscript number.

%package -n texlive-chs-physics-report
Summary:        Physics lab reports for Carmel High School
Version:        svn54512
License:        LicenseRef-Fedora-Public-Domain AND CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(transparent.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(chs-physics-report.sty) = %{tl_version}

%description -n texlive-chs-physics-report
This package may optionally be used by students at Carmel High School in
Indiana in the United States to write physics lab reports for FW physics
courses. As many students are beginners at LaTeX, it also attempts to simplify
the report-writing process by offering macros for commonly used notation and by
automatically formatting the documents for students who will only use TeX for
mathematics and not typesetting. The package depends on amsmath, calc,
fancyhdr, geometry, graphicx, letltxmacro, titlesec, transparent, and xcolor.

%package -n texlive-cidarticle
Summary:        A class for submissions to the "Commentarii informaticae didacticae" (CID)
Version:        svn68976
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cidarticle
The cidarticle bundle is used for writing articles to be published in the
"Commentarii informaticae didacticae (CID)". The LaTeX class file is based on
the class used for the "Lecture Notes in Informatics (LNI)"
(https://github.com/gi-ev/LNI).

%package -n texlive-cje
Summary:        LaTeX document class for CJE articles
Version:        svn68656
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsbsy.sty)
Requires:       tex(natbib.sty)
Provides:       tex(cjenatbib.sty) = %{tl_version}
Provides:       tex(cjeupmath.sty) = %{tl_version}

%description -n texlive-cje
The cje article class allows authors to format their papers to Canadian Journal
of Economics style with minimum effort. The class includes options for two
other formats: "review" (double spaced, for use at the submission stage) and
"proof" (used by the typesetters to prepare the proof authors will receive for
approval).

%package -n texlive-cjs-rcs-article
Summary:        Article class for The Canadian Journal of Statistics
Version:        svn76790
License:        LPPL-1.3c AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cjs-rcs-article
The document class cjs-rcs-article and its companion bibliographic styles
cjs-rcs-en and cjs-rcs-fr typeset manuscripts immediately in accordance with
the presentation rules of The Canadian Journal of Statistics. The package also
contains the official Author guidelines for The Canadian Journal of Statistics.

%package -n texlive-classicthesis
Summary:        A "classically styled" thesis package
Version:        svn73676
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(beramono.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(euler-math.sty)
Requires:       tex(eulervm.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(microtype.sty)
Requires:       tex(mparhack.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(scrtime.sty)
Requires:       tex(textcase.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(typearea.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(classicthesis-arsclassica.sty) = %{tl_version}
Provides:       tex(classicthesis-linedheaders.sty) = %{tl_version}
Provides:       tex(classicthesis-plain.sty) = %{tl_version}
Provides:       tex(classicthesis.sty) = %{tl_version}

%description -n texlive-classicthesis
This package provides an elegant layout designed in homage to Bringhurst's "The
Elements of Typographic Style". It makes use of a range of techniques to get
the best results achievable using TeX. Included in the bundle are templates to
make thesis writing easier.

%package -n texlive-cleanthesis
Summary:        A clean LaTeX style for thesis documents
Version:        svn51472
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Requires:       tex(blindtext.sty)
Requires:       tex(caption.sty)
Requires:       tex(charter.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(microtype.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tgheros.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(cleanthesis.sty) = %{tl_version}

%description -n texlive-cleanthesis
The package offers a clean, simple, and elegant LaTeX style for thesis
documents.

%package -n texlive-cmpj
Summary:        Style for the journal Condensed Matter Physics
Version:        svn58506
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(doi.sty)
Requires:       tex(droidsansmono.sty)
Requires:       tex(droidsans.sty)
Requires:       tex(droidsansmono.sty)
Requires:       tex(droidserif.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fourier.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(natbib.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(scalerel.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(txfonts.sty)
Requires:       tex(url.sty)
Provides:       tex(cmpj.sty) = %{tl_version}
Provides:       tex(cmpj2.sty) = %{tl_version}
Provides:       tex(cmpj3.sty) = %{tl_version}

%description -n texlive-cmpj
The package contains macros and some documentation for typesetting papers for
submission to the Condensed Matter Physics journal published by the Institute
for Condensed Matter Physics of the National Academy of Sciences of Ukraine.

%package -n texlive-confproc
Summary:        A set of tools for generating conference proceedings
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(newapave.sty) = %{tl_version}

%description -n texlive-confproc
The confproc collection comprises a class, a BibTeX style, and some scripts for
generating conference proceedings. It derives from LaTeX scripts written for
the DAFx-06 conference proceedings, largely based on the pdfpages package for
including the proceedings papers and the hyperref package for creating a proper
table of contents, bookmarks and general bibliography back-references. Confproc
also uses many other packages for fine tuning of the table of contents,
bibliography and index of authors. The added value of the class resides in its
time-saving aspects when designing conference proceedings.

%package -n texlive-contract
Summary:        Typeset formalized legal documents such as contracts, statutes, etc.
Version:        svn69759
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(scrkbase.sty)
Requires:       tex(tocbasic.sty)
Provides:       tex(contract.sty) = %{tl_version}

%description -n texlive-contract
This package enables the typesetting of formalized legal documents such as
contracts, statutes etc. It will be the successor to the scrjura package. Like
the latter, "contract" allows the typographically appealing typesetting of many
different legal texts. The typesetting of contracts according to German
conventions is supported "out of the box". In addition, the package supports
the definition of custom environments in order to typeset contracts and legal
texts according to Anglo-American specifications, for example.

%package -n texlive-cqjtuthesis
Summary:        Thesis template for Chongqing Jiaotong University (CQJTU)
Version:        svn77587
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cqjtuthesis
This is a LaTeX document class for typesetting theses at Chongqing Jiaotong
University. It supports Bachelor's thesis, Academic Master's thesis,
Professional Master's thesis, and Doctoral dissertation. The template strictly
follows the official formatting requirements from the university.

%package -n texlive-cquthesis
Summary:        LaTeX Thesis Template for Chongqing University
Version:        svn55643
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(dirtree.sty)
Provides:       tex(cquthesis.sty) = %{tl_version}

%description -n texlive-cquthesis
CQUThesis stands for Chongqing University Thesis Template for LaTeX, bearing
the ability to support bachelor, master, doctor dissertations with grace and
speed.

%package -n texlive-dccpaper
Summary:        Typeset papers for the International Journal of Digital Curation
Version:        svn75491
License:        LPPL-1.3c AND CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(GoSans.sty)
Requires:       tex(array.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(babel.sty)
Requires:       tex(baskervald.sty)
Requires:       tex(Baskervaldx.sty)
Requires:       tex(baskervillef.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(tgheros.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(dccpaper-base.sty) = %{tl_version}

%description -n texlive-dccpaper
The LaTeX class ijdc-v14 produces camera-ready papers and articles suitable for
inclusion in the International Journal of Digital Curation, with applicability
from volume 14 onwards; a legacy class ijdc-v9 is provided for papers and
articles written for volumes 9-13. The similar idcc class can be used for
submissions to the International Digital Curation Conference, beginning with
the 2015 conference. As of August 2023 these classes are no longer officially
supported for new submissions to the IJDC and IDCC, but nevertheless they
continue to be maintained to support existing documents.

%package -n texlive-dithesis
Summary:        A class for undergraduate theses at the University of Athens
Version:        svn34295
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dithesis
The class conforms to the requirements of the Department of Informatics and
Telecommunications at the University of Athens regarding the preparation of
undergraduate theses, as of Sep 1, 2011. The class is designed for use with
XeLaTeX; by default (on a Windows platform), the font Arial is used, but
provision is made for use under Linux (with a different sans-serif font).

%package -n texlive-dlrg-templates
Summary:        Templates for the German Lifesaving Association (DLRG)
Version:        svn74633
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(babel.sty)
Requires:       tex(environ.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(forarray.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(silence.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(beamercolorthemeDLRG.sty) = %{tl_version}
Provides:       tex(beamerouterthemeDLRG.sty) = %{tl_version}
Provides:       tex(beamerthemeDLRG.sty) = %{tl_version}
Provides:       tex(dlrg.mod.Adler.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Adler.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Bauchbinde.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Bauchbinde.optionen.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Bauchbinde.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Farben.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Hausarbeit.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Hausarbeit.optionen.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Hausarbeit.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Paketbeschreibung.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Paketbeschreibung.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Personenicon.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Rettungssport.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Rettungssport.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Schrift.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Schrift.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Stoerer.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Stoerer.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Tabellen.code.tex) = %{tl_version}
Provides:       tex(dlrg.mod.Tabellen.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.sty) = %{tl_version}
Provides:       tex(dlrg.typ.beamer.code.tex) = %{tl_version}
Provides:       tex(dlrg.typ.beamer.optionen.tex) = %{tl_version}
Provides:       tex(dlrg.typ.beamer.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.typ.doc.code.tex) = %{tl_version}
Provides:       tex(dlrg.typ.doc.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.typ.letter.code.tex) = %{tl_version}
Provides:       tex(dlrg.typ.letter.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.typ.message.code.tex) = %{tl_version}
Provides:       tex(dlrg.typ.message.optionen.tex) = %{tl_version}
Provides:       tex(dlrg.typ.message.pakete.tex) = %{tl_version}
Provides:       tex(dlrg.typ.pub.code.tex) = %{tl_version}
Provides:       tex(dlrg.typ.pub.optionen.tex) = %{tl_version}
Provides:       tex(dlrg.typ.pub.pakete.tex) = %{tl_version}

%description -n texlive-dlrg-templates
This bundle provides templates for members of the German Lifesaving Association
(DLRG). This includes the letter template, presentations, specialist
publications and press releases. These templates are based on the current
cooperative design. They can be adapted to the local structure with simple
settings.

%package -n texlive-ebook
Summary:        Helps creating an ebook by providing an ebook class
Version:        svn29466
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(moreverb.sty)
Provides:       tex(ebook.sty) = %{tl_version}

%description -n texlive-ebook
The package defines a command \ebook that defines page layout, fonts, and
font-sizes for documents to be rendered as PDF-ebooks on small ebook-readers.
The package has been tested with Kindle e-ink and iPad mini.

%package -n texlive-ebsthesis
Summary:        Typesetting theses for economics
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ebsthesis
The ebsthesis class and ebstools package facilitate the production of
camera-ready manuscripts in conformance with the guidelines of Gabler Verlag
and typographical rules established by the European Business School.

%package -n texlive-ecothesis
Summary:        LaTeX thesis template for the Universidade Federal de Vicosa (UFV), Brazil
Version:        svn48007
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ecothesis-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ecothesis-doc <= 11:%{version}

%description -n texlive-ecothesis
The package provides a LaTeX thesis template for the Universidade Federal de
Vicosa (UFV), Brazil.

%package -n texlive-edmaths
Summary:        A report and thesis package for the University of Edinburgh (UoE)
Version:        svn77050
License:        LPPL-1.3c AND 0BSD
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amscd.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(cmap.sty)
Requires:       tex(cmbright.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(fourier.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(microtype.sty)
Requires:       tex(setspace.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(edmaths.sty) = %{tl_version}

%description -n texlive-edmaths
A report and thesis package for The School of Mathematics, Scotland at the
University of Edinburgh (UoE). When working on a report or thesis, an easy way
to implement the University's typesetting rules in LaTeX is provided by
edmaths.sty. It sets the page margins as required and defines commands to
create the correct cover page and standard declaration. It also loads the
amsmath, amsthm, amscd, and amssymb packages, which are required by almost all
mathematical publications. Through setspace line spacing settings are available
that only affect the body text and not footnotes and captions. Additional
in-built options can be found in more detail in the project's documentation.

%package -n texlive-ejpecp
Summary:        Class for EJP and ECP
Version:        svn60950
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ejpecp
The class is designed for typesetting articles for the mathematical research
periodicals Electronic Journal of Probability (EJP) and Electronic
Communications in Probability (ECP). It depends on amsmath, amsfonts, amsthm,
bera, dsfont, geometry, graphicx, hyperref, lastpage, latexsym, mathtools,
microtype, and afterpackage.

%package -n texlive-ekaia
Summary:        Article format for publishing the Basque Country Science and Technology Journal "Ekaia"
Version:        svn49594
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(basque-date.sty)
Requires:       tex(ccicons.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(sectsty.sty)
Provides:       tex(ekaia.sty) = %{tl_version}

%description -n texlive-ekaia
The package provides the article format for publishing the Basque Country
Science and Technology Journal "Ekaia" at the University of the Basque Country.

%package -n texlive-elbioimp
Summary:        A LaTeX document class for the Journal of Electrical Bioimpedance
Version:        svn21758
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-elbioimp
A document class for writing articles to the Journal of Electrical
Bioimpedance.

%package -n texlive-els-cas-templates
Summary:        Elsevier updated LaTeX templates
Version:        svn71189
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(moreverb.sty)
Requires:       tex(wrapfig.sty)
Provides:       tex(cas-common.sty) = %{tl_version}

%description -n texlive-els-cas-templates
This bundle provides two class and corresponding template files for typesetting
journal articles supposed to go through Elsevier's updated workflow. One of the
sets is meant for one-column, the other for two-column layout. These are now
accepted for submitting articles both in Elsevier's electronic submission
system and elsewhere.

%package -n texlive-elsarticle
Summary:        Class for articles for submission to Elsevier journals
Version:        svn77318
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-elsarticle
This class for typesetting journal articles is accepted for submitted articles
both in Elsevier's electronic submission system and elsewhere. Please note that
this webpage is meant for uploading updates to the elsarticle software itself,
not for submitting articles using it .

%package -n texlive-elteiktdk
Summary:        TDK-thesis template for Hungarian TDK conferences, Section of Computer Science
Version:        svn71086
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-elteiktdk
The National Conference of Scientific Students Associations (OTDK) of Hungary
is the most significant scientific event for Bachelor and Master students in
the country, where students compete with their research papers in all field of
science. It is organized in every 2 years. The conference/competition has 2
rounds: a university level and a country level (for the best papers). This
class template enforces the required formatting rules for TDK theses and
generates the cover and title page given on the provided metadata. The
formatting rules are defined to meet the requirements for TDK theses submitted
at the Eotvos Lorand University, Faculty of Informatics (Budapest, Hungary).
This also fits the formatting requirements of the Computer Science Section of
the country level round. With sufficient modifications the template could be
usable for TDK theses at other national and faculty level sections, too. The
template supports producing both Hungarian and English theses.

%package -n texlive-elteikthesis
Summary:        Thesis template for Eotvos Lorand University (Informatics)
Version:        svn71087
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-elteikthesis
This package provides a Bachelor and Master thesis template for the Eotvos
Lorand University, Faculty of Informatics (Budapest, Hungary). The template
supports producing both Hungarian and English theses.

%package -n texlive-emisa
Summary:        A LaTeX package for preparing manuscripts for the journal EMISA
Version:        svn71883
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear.bbx)
Provides:       tex(emisa.bbx) = %{tl_version}
Provides:       tex(emisa.cbx) = %{tl_version}

%description -n texlive-emisa
The EMISA LaTeX package is provided for preparing manuscripts for submission to
EMISA (Enterprise Modelling and Information Systems Architectures), and for
preparing accepted submissions for publication as well as for typesetting the
final document by the editorial office. Articles in EMISA are published online
at EMISA in the Portable Document Format (PDF).

%package -n texlive-erdc
Summary:        Style for Reports by US Army Corps of Engineers
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-erdc
A class for typesetting Technical Information Reports of the Engineer Research
and Development Center, US Army Corps of Engineers. The class was commissioned
and paid for by US Army Corps of Engineers, Engineer Research and Development
Center, 3909 Halls Ferry Road, Vicksburg, MS 39180-6199.

%package -n texlive-estcpmm
Summary:        Style for Munitions Management Project Reports
Version:        svn17335
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-estcpmm
Provides a class which supports typesetting Cost and Performance Reports and
Final Reports for Munitions Management Reports, US Environmental Security
Technology Certification Program. The class was commissioned and paid for by US
Army Corps of Engineers, Engineer Research and Development Center, 3909 Halls
Ferry Road, Vicksburg, MS 39180-6199.

%package -n texlive-etsvthor
Summary:        Some useful abbreviations for members of e.t.s.v. Thor
Version:        svn48186
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(epsfig.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(etsvthor.sty) = %{tl_version}

%description -n texlive-etsvthor
"e.t.s.v. Thor" stands for "Elektrotechnische Studievereniging Thor", a study
association of Electrical Engeering at the Eindhoven University of Technology.
The author of the package tells us: "Most of our committees use LaTeX to create
meeting notes or other formal documents within the association. When you create
a lot of these documents (which I do a lot, since I am currently the candidate
Secretary of the new board), some abbreviations are extremely useful. I
discovered that more people from our association are interested in using these,
so I decided to put them in a package, so they can use it very easily too."

%package -n texlive-facture-belge-simple-sans-tva
Summary:        Simple Belgian invoice without VAT
Version:        svn67573
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(facture-belge-simple-sans-tva.sty) = %{tl_version}

%description -n texlive-facture-belge-simple-sans-tva
This package can be used to generate invoices for Belgian individuals who do
not have a VAT number and who wish to do occasional work, or to carry out paid
additional activities during their free time up to 6,000 euros per calendar
year (amount indexed annually) without having to pay tax or social security
contributions (see the website Activites complementaires). The package can also
generate expense reports. All totals are calculated automatically, in the
invoice and in the expense report. The package depends on calctab, ifthen,
hyperref, fancyhdr, multirow, eurosym, color, and colortbl.

%package -n texlive-fbithesis
Summary:        Computer Science thesis class for University of Dortmund
Version:        svn21340
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fbithesis
At the department of computer science at the University of Dortmund there are
cardboard cover pages for research or internal reports like master/phd-theses.
The main function of this LaTeX2e document-class is a replacement for the
\maketitle command to typeset a title page that is adjusted to these cover
pages.

%package -n texlive-fcavtex
Summary:        A thesis class for the FCAV/UNESP (Brazil)
Version:        svn38074
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fcavtex
This package provides a class and a bibliography style for the FCAV-UNESP
(Faculdade de Ciencias Agrarias e Veterinarias de Jaboticabal UNESP) brazilian
university, written based on the institution rules for thesis publications.

%package -n texlive-fcltxdoc
Summary:        Macros for use in the author's documentation
Version:        svn24500
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amsopn.sty)
Requires:       tex(amssymb.sty)
Provides:       tex(fcltxdoc.sty) = %{tl_version}

%description -n texlive-fcltxdoc
The package is not advertised for public use, but is necessary for the support
of others of the author's packages (which are compiled under the ltxdoc class).

%package -n texlive-fei
Summary:        Class for academic works at FEI University Center -- Brazil
Version:        svn65352
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fei
fei is a class created by graduate students and LaTeX enthusiasts that allows
students from FEI University Center to create their academic works, be it a
monograph, masters dissertation or phd thesis, under the typographic rules of
the institution. The class makes it possible to create a full academic work,
supporting functionalities such as cover, title page, catalog entry,
dedication, summary, lists of figures, tables, algorithms, acronyms and
symbols, multiple authors, index, references, appendices and attachments. fei
is loosely based in the Brazilian National Standards Organization (Associacao
Brasileira de Normas Tecnicas, ABNT) standards for the creation of academic
works, such as ABNT NBR 10520:2002 (Citations) and ABNT NBR 6023:2002
(Bibliographic References).

%package -n texlive-fhj-script
Summary:        Classes and packages for formatting documents for FH JOANNEUM
Version:        svn77111
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xstring.sty)
Provides:       tex(fhjcommon.sty) = %{tl_version}

%description -n texlive-fhj-script
This is a collection of classes and packages for the university of applied
sciences (FH JOANNEUM, Graz, Austria). It is used by the institute for applied
informatics. Mainly for creation of the master thesis and expose. It could be
also the base for other academic work related to the study programs.

%package -n texlive-ftc-notebook
Summary:        Typeset FIRST Tech Challenge (FTC) notebooks
Version:        svn50043
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(anyfontsize.sty)
Requires:       tex(array.sty)
Requires:       tex(arrayjobx.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(datetime.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenx.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(mfirstuc.sty)
Requires:       tex(multido.sty)
Requires:       tex(multirow.sty)
Requires:       tex(needspace.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(paralist.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tabu.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Provides:       tex(ftc-notebook.sty) = %{tl_version}

%description -n texlive-ftc-notebook
This LaTeX package will greatly simplify filling entries for your FIRST Tech
Challenge (FTC) engineering or outreach notebook. We developed this package to
support most frequently used constructs encountered in an FTC notebook:
meetings, tasks, decisions with pros and cons, tables, figures with
explanations, team stories and bios, and more. We developed this package during
the 2018-2019 season and are using it for our engineering notebook. Team
Robocracy is sharing this style in the spirit of coopertition.

%package -n texlive-gaceta
Summary:        A class to typeset La Gaceta de la RSME
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gaceta
The class will typeset papers for <<La Gaceta de la Real Sociedad Matematica
Espanola>>.

%package -n texlive-gammas
Summary:        Template for the GAMM Archive for Students
Version:        svn56403
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gammas
This is the official document class for typesetting journal articles for GAMM
Archive for Students (GAMMAS), the open-access online yournal run by the GAMM
Juniors (GAMM = Gesellschaft fur angewandte Mathematik und Mechanik).

%package -n texlive-geradwp
Summary:        Document class for the Cahiers du GERAD series
Version:        svn63134
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-geradwp
This package provides the geradwp class, a class based on article and
compatible with LaTeX. With this class, researchers at GERAD will be able to
write their working paper while complying to all the presentation standards
required by the Cahiers du GERAD series.

%package -n texlive-gfdl
Summary:        Support for using GNU Free Documentation License in LaTeX
Version:        svn75712
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(csquotes.sty)
Requires:       tex(expkv-def.sty)
Requires:       tex(expkv-opt.sty)
Requires:       tex(float.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyperxmp.sty)
Provides:       tex(gfdl-tex-1p1.tex) = %{tl_version}
Provides:       tex(gfdl-tex-1p2.tex) = %{tl_version}
Provides:       tex(gfdl-tex-1p3.tex) = %{tl_version}
Provides:       tex(gfdl.sty) = %{tl_version}

%description -n texlive-gfdl
The GFDL (GNU Free Documentation License) is a popular license used for
programming manuals, documentations and various other textual works too, but
using this license with LaTeX is not very convenient. This package aims to help
users in easily using the license without violating any rules of the license.
With a handful of commands, users can rest assured that their document will be
perfectly licensed under GFDL.

%package -n texlive-gradstudentresume
Summary:        A generic template for graduate student resumes
Version:        svn38832
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gradstudentresume
The package offers a template for graduate students writing an academic CV. The
goal is to create a flexible template that can be customized based on each
specific individual's needs.

%package -n texlive-grant
Summary:        Classes for formatting federal grant proposals
Version:        svn56852
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-grant
LaTeX classes for formatting federal grant proposals: grant: Base class for
formatting grant proposals grant-arl: Army Research Laboratory grant-darpa:
Defense Advanced Research Projects Agency grant-doe: Department of Energy
grant-nih: National Institutes of Health grant-nrl: Naval Research Laboratory
grant-nsf: National Science Foundation grant-onr: Office of Naval Research

%package -n texlive-gsemthesis
Summary:        Geneva School of Economics and Management PhD thesis format
Version:        svn56291
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gsemthesis
The class provides a PhD thesis template for the Geneva School of Economics and
Management (GSEM), University of Geneva, Switzerland. The class provides
utilities to easily set up the cover page, the front matter pages, the page
headers, etc., conformant to the official guidelines of the GSEM Faculty for
writing PhD dissertations.

%package -n texlive-gzt
Summary:        Bundle of classes for "La Gazette des Mathematiciens"
Version:        svn74605
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gzt
This bundle provides two classes and BibLaTeX styles for the French journal "La
Gazette des Mathematiciens": gzt for the complete issues of the journal, aimed
at the Gazette's team, gztarticle, intended for authors who wish to publish an
article in the Gazette. This class's goals are to faithfully reproduce the
layout of the Gazette, thus enabling the authors to be able to work their
document in actual conditions, and provide a number of tools (commands and
environments) to facilitate the drafting of documents, in particular those
containing mathematical formulas.

%package -n texlive-h2020proposal
Summary:        LaTeX class and template for EU H2020 RIA proposal
Version:        svn38428
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-h2020proposal
This package consists of a class file as well as FET and ICT proposal templates
for writing EU H2020 RIA proposals and generating automatically the many
cross-referenced tables that are required.

%package -n texlive-hagenberg-thesis
Summary:        Collection of LaTeX classes, style files and example documents for academic manuscripts
Version:        svn74272
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithm.sty)
Requires:       tex(algpseudocodex.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(breakurl.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(cmap.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(epstopdf.sty)
Requires:       tex(exscale.sty)
Requires:       tex(extramarks.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(forloop.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hypcap.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lengthconvert.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(longtable.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(multirow.sty)
Requires:       tex(overpic.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(soul.sty)
Requires:       tex(subdepth.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocbasic.sty)
Requires:       tex(upquote.sty)
Requires:       tex(url.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(hgb.sty) = %{tl_version}
Provides:       tex(hgbabbrev.sty) = %{tl_version}
Provides:       tex(hgbalgo.sty) = %{tl_version}
Provides:       tex(hgbbib.sty) = %{tl_version}
Provides:       tex(hgbdict.sty) = %{tl_version}
Provides:       tex(hgbheadings.sty) = %{tl_version}
Provides:       tex(hgblistings.sty) = %{tl_version}
Provides:       tex(hgbmath.sty) = %{tl_version}
Provides:       tex(hgbpdfa.sty) = %{tl_version}
Provides:       tex(hgbtheme-custom.sty) = %{tl_version}
Provides:       tex(hgbtheme-default.sty) = %{tl_version}
Provides:       tex(hgbtheme-fhooe24.sty) = %{tl_version}

%description -n texlive-hagenberg-thesis
This is a collection of modern LaTeX classes, style files and example documents
for authoring Bachelor, Master, Diploma, or PhD theses and related academic
manuscripts in English and German. Pre-configured English and German documents
are available. They are easy to use even for LaTeX beginners, and compatible
with LaTeX distributions for Windows, macOS, and Linux. The document classes
are immediately usable and convenient to customize.

%package -n texlive-har2nat
Summary:        Replace the harvard package with natbib
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(natbib.sty)
Requires:       tex(suffix.sty)
Provides:       tex(har2nat.sty) = %{tl_version}

%description -n texlive-har2nat
This small package allows a LaTeX document containing the citation commands
provided by the Harvard package to be compiled using the natbib package.
Migration from harvard to natbib thus can be achieved simply by replacing
\usepackage{harvard} with usepackage{natbib} usepackage{har2nat} It is
important that har2nat be loaded after natbib, since it modifies natbib
commands.

%package -n texlive-hduthesis
Summary:        LaTeX class for bachelor and MPhil theses in Hangzhou Dianzi University
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(beamerthemehdu.sty) = %{tl_version}
Provides:       tex(hdu-bc.config.code.tex) = %{tl_version}
Provides:       tex(hdu-exam.code.tex) = %{tl_version}
Provides:       tex(hdu-l3doc.code.tex) = %{tl_version}
Provides:       tex(hdu-layout.code.tex) = %{tl_version}
Provides:       tex(hdu-pg.config.code.tex) = %{tl_version}
Provides:       tex(hdu-stationery.code.tex) = %{tl_version}
Provides:       tex(hdu-typeset.code.tex) = %{tl_version}

%description -n texlive-hduthesis
This package provides a LaTeX template for graduation theses from Hangzhou
Dianzi University. It supports the formatting of bachelor and MPhil degree
theses.

%package -n texlive-hecthese
Summary:        A class for dissertations and theses at HEC Montreal
Version:        svn68584
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hecthese
This package provides the hecthese class, a class based on memoir and
compatible with LaTeX. Using this class, postgraduate students at HEC Montreal
will be able to write their dissertation or thesis while complying with all the
presentation standards required by the University. This class is meant to be as
flexible as possible; in particular, there are very few hardcoded features
except those that take care of the document's layout. Dissertations and theses
at HEC Montreal can be written on a per-chapter or per-article basis. Documents
that are written on a per-article basis require a bibliography for each of the
included articles and a general bibliography for the entire document. The
hecthese class takes care of these requirements. The class depends on babel,
color, enumitem, fontawesome, framed, numprint, url, and hyperref.

%package -n texlive-hep-paper
Summary:        Publications in High Energy Physics
Version:        svn76220
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hep-acronym.sty)
Requires:       tex(hep-bibliography.sty)
Requires:       tex(hep-float.sty)
Requires:       tex(hep-font.sty)
Requires:       tex(hep-math-font.sty)
Requires:       tex(hep-math.sty)
Requires:       tex(hep-reference.sty)
Requires:       tex(hep-text.sty)
Requires:       tex(hep-title.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(parskip.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(hep-paper.sty) = %{tl_version}
Provides:       tex(hep-revtex.sty) = %{tl_version}
Provides:       tex(hep-sissa.sty) = %{tl_version}

%description -n texlive-hep-paper
This package aims to provide a single style file containing most configurations
and macros necessary to write appealing publications in High Energy Physics.
Instead of reinventing the wheel by introducing newly created macros, hep-paper
preferably loads third party packages as long as they are light-weight enough.
For usual publications it suffices to load the hep-paper package, without
optional arguments, in addition to the article class.

%package -n texlive-heria
Summary:        A LaTeX class for Horizon Europe RIA and IA grant proposals
Version:        svn76077
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hi-annexes.tex) = %{tl_version}
Provides:       tex(hi-capacity.tex) = %{tl_version}
Provides:       tex(hi-criticalrisks.tex) = %{tl_version}
Provides:       tex(hi-deliverables-key.tex) = %{tl_version}
Provides:       tex(hi-deliverables.tex) = %{tl_version}
Provides:       tex(hi-excellence.tex) = %{tl_version}
Provides:       tex(hi-impact.tex) = %{tl_version}
Provides:       tex(hi-inkind.tex) = %{tl_version}
Provides:       tex(hi-measures.tex) = %{tl_version}
Provides:       tex(hi-methodology.tex) = %{tl_version}
Provides:       tex(hi-milestones.tex) = %{tl_version}
Provides:       tex(hi-objectives.tex) = %{tl_version}
Provides:       tex(hi-othercosts.tex) = %{tl_version}
Provides:       tex(hi-participant-numbering.tex) = %{tl_version}
Provides:       tex(hi-participants.tex) = %{tl_version}
Provides:       tex(hi-pathways.tex) = %{tl_version}
Provides:       tex(hi-purchasecosts.tex) = %{tl_version}
Provides:       tex(hi-quality.tex) = %{tl_version}
Provides:       tex(hi-staffeffort.tex) = %{tl_version}
Provides:       tex(hi-subcontractingcosts.tex) = %{tl_version}
Provides:       tex(hi-summary.tex) = %{tl_version}
Provides:       tex(hi-tables.tex) = %{tl_version}
Provides:       tex(hi-workplan.tex) = %{tl_version}
Provides:       tex(hi-wp-description.tex) = %{tl_version}
Provides:       tex(hi-wp-objectives.tex) = %{tl_version}

%description -n texlive-heria
This class facilitates the preparation of Research and Innovation Action (RIA)
and Innovation Action (IA) funding proposals for the European Commission's
Horizon Europe program. The class is a conversion of the official Part B
template into LaTeX; it preserves the formatting and most of the instructions
of the original version, and has the additional feature that tables (listing
the participants, work packages, deliverables, etc.) are programmatically
generated according to data supplied by the user.

%package -n texlive-hfutexam
Summary:        Exam class for Hefei University of Technology (China)
Version:        svn75068
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hfutexam
This package provides an exam class for Hefei University of Technology (China).
Gai Wen Dang Lei Ti Gong Liao He Fei Gong Ye Da Xue Kao Shi Shi Juan Mo Ban ,
Dian Ji Xia Fang Download Lai Xia Zai Suo You Wen Jian .

%package -n texlive-hfutthesis
Summary:        LaTeX Thesis Template for Hefei University of Technology
Version:        svn64025
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hfutthesis
This project is based on the HFUT_Thesis LaTeX template of Hefei University of
Technology compiled on the basis of ustctug/ustcthesis, in accordance with the
latest version of Hefei University of Technology Graduate Dissertation Writing
Specifications and Hefei University of Technology Undergraduate Graduation
Project (Thesis) Work Implementation Rules.

%package -n texlive-hithesis
Summary:        Harbin Institute of Technology Thesis Template
Version:        svn64005
License:        LPPL-1.3a
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bm.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(rotating.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(ctex-fontset-siyuan.def) = %{tl_version}
Provides:       tex(hithesis.sty) = %{tl_version}

%description -n texlive-hithesis
hithesis is a LaTeX thesis template package for Harbin Institute of Technology
supporting bachelor, master, doctor dissertations.

%package -n texlive-hitszbeamer
Summary:        A beamer theme for Harbin Institute of Technology, ShenZhen
Version:        svn54381
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ctex.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multimedia.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Provides:       tex(beamercolorthemehitszbeamer.sty) = %{tl_version}
Provides:       tex(beamerinnerthemehitszbeamer.sty) = %{tl_version}
Provides:       tex(beamerouterthemehitszbeamer.sty) = %{tl_version}
Provides:       tex(beamerthemehitszbeamer.sty) = %{tl_version}

%description -n texlive-hitszbeamer
This is a beamer theme designed for Harbin Institute of Technology, ShenZhen
(HITSZ).

%package -n texlive-hitszthesis
Summary:        A dissertation template for Harbin Institute of Technology, ShenZhen
Version:        svn61073
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bm.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(rotating.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(hitszthesis.sty) = %{tl_version}

%description -n texlive-hitszthesis
This package provides a dissertation template for Harbin Institute of
Technology, ShenZhen (HITSZ), including bachelor, master and doctor
dissertations.

%package -n texlive-hobete
Summary:        Unofficial beamer theme for the University of Hohenheim
Version:        svn27036
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xfrac.sty)
Requires:       tex(xparse.sty)
Provides:       tex(beamercolorthemehohenheim.sty) = %{tl_version}
Provides:       tex(beamerouterthemehohenheim.sty) = %{tl_version}
Provides:       tex(beamerouterthemehohenheimposter.sty) = %{tl_version}
Provides:       tex(beamerthemehohenheim.sty) = %{tl_version}
Provides:       tex(hobete.sty) = %{tl_version}

%description -n texlive-hobete
The package provides a beamer theme which features the Ci colors of the
University of Hohenheim. Please note that this is not an official Theme, and
that there will be no support for it, from the University. Furthermore there is
NO relationship between the University and this theme.

%package -n texlive-hu-berlin-bundle
Summary:        LaTeX classes for the Humboldt-Universitat zu Berlin
Version:        svn76790
License:        LPPL-1.3c AND GPL-2.0-only AND BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(calc.sty)
Requires:       tex(ccicons.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(dirtree.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(libertine.sty)
Requires:       tex(listings.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(markdown.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(microtype.sty)
Requires:       tex(newfile.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Provides:       tex(hu-berlin-base.sty) = %{tl_version}
Provides:       tex(hu-berlin-bundle-style.sty) = %{tl_version}

%description -n texlive-hu-berlin-bundle
This package provides files according to the corporate design of the
Humboldt-Universitat zu Berlin. This is not an official package by the
university itself, and not officially approved by it. More information can be
found in the Humboldt University's corporate design guideline and on the
website https://www.hu-berlin.de/de/hu-intern/design. At present, the bundle
contains a letter class based on scrlttr2 and a package hu-berlin-base.sty
which contains all relevant code for documents and documentclasses of the
bundle.

%package -n texlive-hustthesis
Summary:        Unofficial thesis template for Huazhong University
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(gb7714-2015.bbx)
Requires:       tex(gb7714-2015.cbx)
Provides:       tex(hustthesis-d.def) = %{tl_version}
Provides:       tex(hustthesis-doc.sty) = %{tl_version}
Provides:       tex(hustthesis-m.def) = %{tl_version}
Provides:       tex(hustthesis.bbx) = %{tl_version}
Provides:       tex(hustthesis.cbx) = %{tl_version}

%description -n texlive-hustthesis
The package provides an Unofficial Thesis Template in LaTeX for Huazhong
University of Science and Technology.

%package -n texlive-hustvisual
Summary:        Visual identity of Huazhong University of Science and Technology
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(hustvisual-vi-emblem.def) = %{tl_version}
Provides:       tex(hustvisual-vi-horizontal-name-zh.def) = %{tl_version}
Provides:       tex(hustvisual.sty) = %{tl_version}

%description -n texlive-hustvisual
The package provides a collection of visual identity assets for Huazhong
University of Science and Technology (HUST), implemented using LaTeX3 and TikZ.

%package -n texlive-iaria
Summary:        Write documents for the IARIA publications
Version:        svn77504
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-iaria
This package contains templates for the creation of documents for IARIA
publications (International Academy, Research, and Industry Association) and
implements the specifications for the IARIA citation style.

%package -n texlive-iaria-lite
Summary:        Write documents for the IARIA publications
Version:        svn77505
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-iaria-lite
This package provides a convenient environment for writing IARIA (International
Academy, Research, and Industry Association) scholary publications. It does not
implement the specifications for the IARIA citation style, for which you have
to use the iaria class.

%package -n texlive-icsv
Summary:        Class for typesetting articles for the ICSV conference
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-icsv
This is an ad-hoc class for typesetting articles for the ICSV conference, based
on the earler active-conf by the same author.

%package -n texlive-ieeeconf
Summary:        Macros for IEEE conference proceedings
Version:        svn59665
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ieeeconf
The IEEEconf class implements the formatting dictated by the IEEE Computer
Society Press for conference proceedings.

%package -n texlive-ieeepes
Summary:        IEEE Power Engineering Society Transactions
Version:        svn17359
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(mathptm.sty)
Requires:       tex(times.sty)
Requires:       tex(vmargin.sty)
Provides:       tex(ieeepes.sty) = %{tl_version}

%description -n texlive-ieeepes
Supports typesetting of transactions, as well as discussions and closures, for
the IEEE Power Engineering Society Transactions journals.

%package -n texlive-ieeetran
Summary:        Document class for IEEE Transactions journals and conferences
Version:        svn59672
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(IEEEtrantools.sty) = %{tl_version}

%description -n texlive-ieeetran
The class and its BibTeX style enable authors to produce officially-correct
output for the Institute of Electrical and Electronics Engineers (IEEE)
transactions, journals and conferences.

%package -n texlive-ijmart
Summary:        LaTeX Class for the Israel Journal of Mathematics
Version:        svn30958
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ijmart
The Israel Journal of Mathematics is published by The Hebrew University Magnes
Press. This class provides LaTeX support for its authors and editors. It
strives to achieve the distinct "look and feel" of the journal, while having
the interface similar to that of the amsart document class. This will help
authors already familiar with amsart to easily submit manuscripts for The
Israel Journal of Mathematics or to put the preprints in arXiv with minimal
changes in the LaTeX source.

%package -n texlive-ijsra
Summary:        LaTeX document class for the International Journal of Student Research in Archaeology
Version:        svn44886
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ijsra
This is a document class called ijsra which is used for the International
Journal of Student Research in Archaeology.

%package -n texlive-imac
Summary:        International Modal Analysis Conference format
Version:        svn17347
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(cite.sty)
# Ignoring dependency on citesort.sty - not part of TeX Live
Requires:       tex(ifthen.sty)
Provides:       tex(imac.sty) = %{tl_version}

%description -n texlive-imac
A set of files for producing correctly formatted documents for the
International Modal Analysis Conference. The bundle provides a LaTeX package
and a BibTeX style file.

%package -n texlive-imtekda
Summary:        IMTEK thesis class
Version:        svn17667
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-imtekda
The class permits typesetting of diploma, bachelor's and master's theses for
the Institute of Microsystem Technology (IMTEK) at the University of Freiburg
(Germany). The class is based on the KOMA-Script class scrbook. Included in the
documentation is a large collection of useful tips for typesetting theses and a
list of recommended packages.

%package -n texlive-inkpaper
Summary:        A mathematical paper template
Version:        svn54080
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-inkpaper
InkPaper is designed to write mathematical papers,especially designed for
Mathematics Students. ZJGS students. magazine editors. NOTICE.This is not a
Thesis class.

%package -n texlive-iodhbwm
Summary:        Unofficial template of the DHBW Mannheim
Version:        svn57773
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(totalcount.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(iodhbwm-i18n.def) = %{tl_version}
Provides:       tex(iodhbwm-templates.sty) = %{tl_version}

%description -n texlive-iodhbwm
This package provides an unofficial template of the DHBW Mannheim for the
creation of bachelor thesis, studies or project work with LaTeX. The aim of the
package is the quick creation of a basic framework without much effort.

%package -n texlive-iscram
Summary:        A LaTeX class to publish article to ISCRAM conferences
Version:        svn45801
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-iscram
LaTeX class to publish article to ISCRAM (International Conference on
Information Systems for Crisis Response and Management).

%package -n texlive-jacow
Summary:        A class for submissions to the proceedings of conferences on JACoW.org
Version:        svn63060
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jacow
The jacow class is used for submissions to the proceedings of conferences on
Joint Accelerator Conferences Website (JACoW), an international collaboration
that publishes the proceedings of accelerator conferences held around the
world.

%package -n texlive-jmlr
Summary:        Class files for the Journal of Machine Learning Research
Version:        svn61957
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(aliascnt.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(jmlrutils.sty) = %{tl_version}

%description -n texlive-jmlr
The jmlr bundle provides a class for authors (jmlr) and a class for production
editors (jmlrbook). The jmlrbook class can be used to combine articles written
using the jmlr class into a book. The class uses the combine class and the
hyperref package to produce either a colour hyperlinked book for on-line
viewing or a greyscale nonhyperlinked book for printing. Production editors can
use makejmlrbookgui to help build the proceedings from the articles.

%package -n texlive-jnuexam
Summary:        Exam class for Jinan University
Version:        svn71883
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jnuexam
The package provides an exam class for Jinan University (China).

%package -n texlive-jourcl
Summary:        Cover letter for journal submissions
Version:        svn65290
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jourcl
Paper submissions to journals are usually accompanied by a cover letter. This
package provides a LaTeX class and a template for such a cover letter with the
following main features: Minimalistic design. Custom image. Pre-defined
commands for journal name, author, date, etc. Many macros contained in this
package speed up the process of preparing the necessary ingredients for the
cover letter. Macros for recommending up to three reviewers and/or editors.
ORCID logo and link to the submitting author's ORCID page. Controls for adding
a "Conflict of interest" statement and declaration. Custom greeting (e.g.,
"Dear Editor" for a regular submission, "Dear Editor-in-Chief" for a submission
to a journal's special issue, etc.) Predefined valedictions for different types
of submissions (e.g., Yours sincerely, Yours faithfully, Best regards, etc.)

%package -n texlive-jourrr
Summary:        A LaTeX template for journal rebuttal letters
Version:        svn68556
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jourrr
This package provides an elegant LaTeX template designed for crafting
professional rebuttal letters in response to editors or reviewers. It consists
of a LaTeX class and a template, fine-tuned to support your publishing journey
with several pre-defined commands that drastically speed up the process of
preparing letters during the revision process. The repository hosts a template
for writing responses to editors/reviewers comments for journal submissions
written in LaTeX that is minimalistic in one way while pre-defined with several
commands that drastically speed up the process of preparing letters during the
revision process. Main Features of this template: With front page included
Response ticks to mark as completed Custom response color Minimalistic design
Everything is customizable Predefined commands for a journal name, submission
ID, author, editor, associate editor, date, etc. Many macros included
Predefined different valedictions for different types of submissions (e.g.,
Yours sincerely, Yours faithfully, Best regards, etc.) Custom greeting (e.g.,
"Dear Editor" or bDear Editor-in-Chief" for regular submission, etc.)
(Optional) Table of contents, jump to the reply you wish to address Option to
add custom Signature (i.e. an image of your hand-written signature)

%package -n texlive-jpsj
Summary:        Document Class for Journal of the Physical Society of Japan
Version:        svn66115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jpsj
Document Class for Journal of the Physical Society of Japan

%package -n texlive-jsonresume
Summary:        A minimal LuaLaTeX package for rendering JSON Resume data into LaTeX documents
Version:        svn77560
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(xparse.sty)
Provides:       tex(jsonresume.sty) = %{tl_version}

%description -n texlive-jsonresume
A minimal LuaLaTeX package for rendering JSON Resume data into clean,
professional resumes. Features Full JSON Resume Schema Support All 12 sections
(basics, work, volunteer, education, awards, certificates, publications,
skills, languages, interests, references, projects) Load from File or URL Local
JSON files or remote URLs Schema Validation Strict mode warns about schema
violations Clean FAANG-style Formatting Professional typography with no
distracting design elements Customizable Section Titles Override default
section headers Requirements LuaLaTeXPart of TeX Live or MiKTeX curl For URL
loading, pre-installed on most systems

%package -n texlive-jwjournal
Summary:        A personal class for writing journals
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-einfart

%description -n texlive-jwjournal
This LaTeX document class enables the user to turn simple pure text entries
into a colorful and nicely formatted journal.

%package -n texlive-kdgdocs
Summary:        Document classes for Karel de Grote University College
Version:        svn24498
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-kdgdocs
The bundle provides two classes for usage by KdG professors and master
students: kdgcoursetext: for writing course texts, and kdgmasterthesis: for
writing master's theses. The bundle replaces the original kdgcoursetext package
(now removed from the archive).

%package -n texlive-kdpcover
Summary:        Covers for books published by Kindle Direct Publishing
Version:        svn74392
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-anyfontsize
Requires:       texlive-etoolbox
Requires:       texlive-geometry
Requires:       texlive-iexec
Requires:       texlive-microtype
Requires:       texlive-pgf
Requires:       texlive-pgfopts
Requires:       texlive-setspace
Requires:       texlive-textpos
Requires:       texlive-xcolor

%description -n texlive-kdpcover
The problem this class solves is the necessity to change the size of the cover
PDF according to the number of pages in the book -- the bigger the book, the
larger the spine of the book must be. The provided class makes the necessary
calculations on-the-fly, using the qpdf tool. Obviously, you need to have it
installed. Also, you must run pdflatex with the --shell-escape option, in order
to allow LaTeX to run qpdf.

%package -n texlive-kfupm-math-exam
Summary:        A LaTeX document style to produce homework, quiz and exam papers
Version:        svn63977
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-kfupm-math-exam
The package provides commands and environments that simplify and streamline the
process of preparing homework, quiz and exam papers according to apreffered
style. The default style is based on the guidelines set by the department of
mathematics at King Fahd University of Petroleum and Minerals (KFUPM). It can
be easily customized to fit any style for any institution.

%package -n texlive-kluwer
Summary:        Kluwer publication support
Version:        svn54074
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(doc.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mathptm.sty)
# Ignoring dependency on mathtime.sty - non-free
Requires:       tex(textcomp.sty)
Requires:       tex(wasysym.sty)
Provides:       tex(klucite.sty) = %{tl_version}
Provides:       tex(kluedit.sty) = %{tl_version}
Provides:       tex(klufloa.sty) = %{tl_version}
Provides:       tex(klulist.sty) = %{tl_version}
Provides:       tex(klumac.sty) = %{tl_version}
Provides:       tex(klumath.sty) = %{tl_version}
Provides:       tex(klumono.sty) = %{tl_version}
Provides:       tex(klunote.sty) = %{tl_version}
Provides:       tex(kluopen.sty) = %{tl_version}
Provides:       tex(klups.sty) = %{tl_version}
Provides:       tex(kluref.sty) = %{tl_version}
Provides:       tex(klusec.sty) = %{tl_version}
Provides:       tex(klutab.sty) = %{tl_version}

%description -n texlive-kluwer
Most likely long obsolete, unfortunately.

%package -n texlive-ksp-thesis
Summary:        A LaTeX class for theses published with KIT Scientific Publishing
Version:        svn39080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ksp-thesis
This package provides a LaTeX class intended for authors who want to publish
their thesis or other scientific work with KIT Scientific Publishing (KSP). The
class is based on the scrbook class of the KOMA-script bundle in combination
with the ClassicThesis and ArsClassica packages. It modifies some of the layout
and style definitions of these packages in order to provide a document layout
that should be compatible with the requirements by KSP.

%package -n texlive-ku-template
Summary:        Copenhagen University or faculty logo for front page
Version:        svn45935
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(titling.sty)
Requires:       tex(wallpaper.sty)
Provides:       tex(ku-template.sty) = %{tl_version}

%description -n texlive-ku-template
A comprehensive package for adding University of Copenhagen or faculty logo to
your front page. For use by student or staff at University of Copenhagen
(Kobenhavns Universitet).

%package -n texlive-langsci
Summary:        Typeset books for publication with Language Science Press
Version:        svn73027
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(authoryear.bbx)
Requires:       tex(calc.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(pbox.sty)
Requires:       tex(pifont.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(ulem.sty)
Requires:       tex(xparse.sty)
Provides:       tex(langsci-affiliations.sty) = %{tl_version}
Provides:       tex(langsci-bidi.sty) = %{tl_version}
Provides:       tex(langsci-gb4e.sty) = %{tl_version}
Provides:       tex(langsci-lgr.sty) = %{tl_version}
Provides:       tex(langsci-optional.sty) = %{tl_version}
Provides:       tex(langsci-plot-templates.sty) = %{tl_version}
Provides:       tex(langsci-series.def) = %{tl_version}
Provides:       tex(langsci-subparts.sty) = %{tl_version}
Provides:       tex(langsci-tbls.sty) = %{tl_version}
Provides:       tex(langsci-textipa.sty) = %{tl_version}
Provides:       tex(langsci-unified.bbx) = %{tl_version}
Provides:       tex(langsci-unified.cbx) = %{tl_version}

%description -n texlive-langsci
This package allows you to typeset monographs and edited volumes for
publication with Language Science Press (https://www.langsci-press.org). It
includes all necessary files for title pages, frontmatter, main content, list
of references and indexes. Dust jackets for BoD and Createspace
(print-on-demand service providers) can also be produced.

%package -n texlive-langsci-avm
Summary:        Feature structures and attribute-value matrices (AVM)
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xparse.sty)
Provides:       tex(langsci-avm.sty) = %{tl_version}

%description -n texlive-langsci-avm
A package for typesetting feature structures, also known as attribute-value
matrices (AVMs), for use in linguistics. The package provides a minimal and
easy to read syntax. It depends only on the array package and can be placed
almost everywhere, in particular in footnotes or graphs and tree structures.
The package serves the same purpose as, Christopher Manning's avm package, but
shares no code base with that package.

%package -n texlive-limecv
Summary:        A (Xe/Lua)LaTeX document class for curriculum vitae
Version:        svn75301
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-limecv
limecv is a (Xe/Lua)LaTeX document class to write curriculum vitae. It is
designed with the following design rules: simple, elegant and clean. To this
end, it offers several environments and macros for convenience.

%package -n texlive-lion-msc
Summary:        LaTeX class for B.Sc. and M.Sc. reports at Leiden Institute of Physics (LION)
Version:        svn75184
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lion-msc
LaTeX class for B.Sc. and M.Sc. reports at Leiden Institute of Physics (LION).
The purpose of this class is twofold: It creates a uniform layout of the
student theses from our department. More importantly it contains several fields
on the front-page that the user needs to fill that are used in the university
administration (name, student number and name of supervisor). Students are free
to change the layout of the text but should leave the title page as it is.

%package -n texlive-llncs
Summary:        Document class and bibliography style for Lecture Notes in Computer Science (LNCS)
Version:        svn77677
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-llncs
This is Springer's official macro package for typesetting contributions to be
published in Springer's Lecture Notes in Computer Science (LNCS) and its
related proceedings series CCIS, LNBIP, LNICST, and IFIP AICT.

%package -n texlive-llncsconf
Summary:        LaTeX package extending Springer's llncs class
Version:        svn63136
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(eso-pic.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(rcsinfo.sty)
Requires:       tex(svninfo.sty)
Provides:       tex(llncsconf.sty) = %{tl_version}

%description -n texlive-llncsconf
The package extends Springer's llncs class for adding additional notes
describing the status of the paper (submitted, accepted) as well as for
creating author-archived versions that include the references to the official
version hosted by Springer (as requested by the copyright transfer agreement
for Springer's LNCS series).

%package -n texlive-lni
Summary:        Official class for the "Lecture Notes in Informatics"
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lni
This is the official version of the class "lni" for submissions to the Lecture
Notes in Informatics published by the Gesellschaft fur Informatik. To use it,
download the file lni-author-template.tex and edit it in your favorite LaTeX
editor.

%package -n texlive-lps
Summary:        Class for "Logic and Philosophy of Science"
Version:        svn21322
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lps
The 'Logic and Philosophy of Science' journal is an online publication of the
University of Trieste (Italy). The class builds on the standard article class
to offer a format that LaTeX authors may use when submitting to the journal.

%package -n texlive-maine-thesis
Summary:        A document class for University of Maine graduate theses
Version:        svn77208
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-maine-thesis
The maine-thesis class provides support for the formatting requirements for
graduate theses of the Graduate School at The University of Maine. It sets
default parameters for the report class, modifies captions, references, and the
table of contents, and makes specific environments available. The maine-thesis
class reflects the guidelines published by the Graduate School at The
University of Maine. The Graduate School at the University of Maine does not
provide official support for any thesis style class or template.

%package -n texlive-matc3
Summary:        Commands for MatematicaC3 textbooks
Version:        svn29845
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(matc3.sty) = %{tl_version}

%description -n texlive-matc3
The package provides support for the Matematica C3 project to produce free
mathematical text books for use in Italian high schools.

%package -n texlive-matc3mem
Summary:        Class for MatematicaC3 textbooks
Version:        svn35773
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-matc3mem
The class is a development of memoir, with additions (specifically,
mathematical extensions) that provide support for writing the books for the
Matematica C3 project to produce free mathematical textbooks for use in Italian
high schools.

%package -n texlive-mcmthesis
Summary:        Template designed for MCM/ICM
Version:        svn69538
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mcmthesis
The package offers a template for MCM (The Mathematical Contest in Modeling)
and ICM (The Interdisciplinary Contest in Modeling) for typesetting the
submitted paper.

%package -n texlive-mentis
Summary:        A basis for books to be published by Mentis publishers
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mentis
This LaTeX class loads scrbook and provides changes necessary for publishing at
Mentis publishers in Paderborn, Germany. It is not an official Mentis class,
merely one developed by an author in close co-operation with Mentis.

%package -n texlive-mitthesis
Summary:        A LaTeX template for an MIT thesis
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mitthesis
This class provides a LaTeX template for an MIT thesis or dissertation
formatted according to the requirements of the Massachusetts Institute of
Technology Libraries (as posted in 2025):
https://libraries.mit.edu/distinctive-collections/thesis-specs/ This template
is appropriate for an MIT thesis or MIT dissertation of any type. This template
works with either pdfLaTeX or LuaLaTeX. The bibliography may be prepared with
biblatex/biber. The class requires TeX Live 2022 or later distributions. This
template replaces the older version of mitthesis.cls, which was first composed
in the 1980s.

%package -n texlive-mlacls
Summary:        LaTeX class for MLA papers
Version:        svn72271
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mlacls
In the United States, secondary and undergraduate students are generally
expected to adhere to the format prescribed by the Modern Language Association
(MLA) for typewritten essays, research papers and writings. This package
provides a simple, straightforward LaTeX class for composing papers almost
perfectly adherent to the MLA style guide.

%package -n texlive-mluexercise
Summary:        Exercises/homework at the Martin Luther University Halle-Wittenberg
Version:        svn56927
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mluexercise
This package provides a template class for solving weekly exercises at the
Institute for Computer Science of Martin Luther University Halle-Wittenberg.
The class can be used by all students--especially first semesters--to typeset
their exercises with low effort in beautiful LaTeX. A bunch of handy macros are
included that are used throughout many lectures during the bachelor's degree
program. The class is maintained by the students' council of the university.
The focus is on encouraging first semester students to use LaTeX for
typesetting, thus the package has been kept as simple as possible.

%package -n texlive-mnras
Summary:        Monthly Notices of the Royal Astronomical Society
Version:        svn68878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mnras
Package for preparing papers in the journal "Monthly Notices of the Royal
Astronomical Society".

%package -n texlive-modeles-factures-belges-assocs
Summary:        Generate invoices for Belgian non-profit organizations
Version:        svn67840
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(calctab.sty)
Requires:       tex(color.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multirow.sty)
Requires:       tex(soul.sty)
Requires:       tex(ulem.sty)
Provides:       tex(modeles-factures-belges-associations.sty) = %{tl_version}

%description -n texlive-modeles-factures-belges-assocs
This package provides templates and a sty file for generating invoices for
Belgian non-profit organizations.

%package -n texlive-modernnewspaper
Summary:        A modern, Unicode-first newspaper package for LaTeX
Version:        svn77279
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bidi.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(lettrine.sty)
Requires:       tex(multicol.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(setspace.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(modernnewspaper.sty) = %{tl_version}

%description -n texlive-modernnewspaper
modernnewspaper is a Unicode-first LaTeX package for producing newspaper-style
documents. It supports multi-column layouts, multilingual content (including
right-to-left scripts), Unicode-safe drop caps, column-safe images, and modern
metadata such as website URLs. The package is designed for XeLaTeX and LuaLaTeX
and is suitable for both print and digital newspapers.

%package -n texlive-msu-thesis
Summary:        Class for Michigan State University Master's and PhD theses
Version:        svn71883
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-msu-thesis
This is a class file for producing dissertations and theses according to the
Michigan State University Graduate School Guidelines for Electronic Submission
of Master's Theses and Dissertations. The class should meet all current
requirements and is updated whenever the university guidelines change. The
class is based on the memoir document class, and inherits the functionality of
that class.

%package -n texlive-mucproc
Summary:        Conference proceedings for the German MuC-conference
Version:        svn43445
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mucproc
The mucproc.cls is a document class to support the formatting guidelines for
submissions to the German Mensch und Computer conference. This work consists of
the files mucproc.dtx and mucproc.ins and the derived files mucproc.cls,
mucfontsize10pt.clo. A compilable demonstration file using the mucproc class
can be found on https://github.com/Blubu/mucproc/. This example fulfills the
formatting guidelines for MuC 2017.

%package -n texlive-mugsthesis
Summary:        Thesis class complying with Marquette University Graduate School requirements
Version:        svn75301
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mugsthesis
The bundle offers a thesis class, based on memoir, that complies with Marquette
University Graduate School requirements.

%package -n texlive-muling
Summary:        MA Thesis class for the Department of Linguistics, University of Mumbai
Version:        svn66741
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-muling
This is a class file for writing MA thesis as required by the Department of
Linguistics at the University of Mumbai.

%package -n texlive-musuos
Summary:        Typeset papers for the department of music, Osnabruck
Version:        svn24857
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-musuos
The package provides a LaTeX class for typesetting term papers at the institute
of music and musicology of the University of Osnabruck, Germany, according to
the specifications of Prof. Stefan Hahnheide. A BibLaTeX style is provided.

%package -n texlive-muthesis
Summary:        Classes for University of Manchester Dept of Computer Science
Version:        svn23861
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-muthesis
The bundle provides thesis and project report document classes from the
University of Manchester's Department of Computer Science.

%package -n texlive-mynsfc
Summary:        A CTeX-based template for writing the main body of NSFC proposals
Version:        svn77520
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mynsfc.def) = %{tl_version}

%description -n texlive-mynsfc
This package provides a CTeX-based template for writing the main text of
National Natural Science Foundation of China (NSFC) proposals. The package
defines styles of the outlines and uses BibLaTeX/biber for the management of
references.

%package -n texlive-nature
Summary:        Prepare papers for the journal Nature
Version:        svn21819
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nature
Nature does not accept papers in LaTeX, but it does accept PDF. This class and
BibTeX style provide what seems to be necessary to produce papers in a format
acceptable to the publisher.

%package -n texlive-navydocs
Summary:        Support for Technical Reports by US Navy Organizations
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(eso-pic.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(relsize.sty)
Requires:       tex(rotating.sty)
Requires:       tex(setspace.sty)
Requires:       tex(xparse.sty)
Provides:       tex(navydocs.sty) = %{tl_version}

%description -n texlive-navydocs
The navydocs package provides an easy means for creating title pages and the
following supplementary material pages used in technical reports by United
States Navy organizations. These pages are generated by specifying the page
content via a set of commands and then calling a macro to create the page at
its occurrence in the document. This package is provided in the hope that it
proves useful to other Navy organizations, with users contributing macros for
their organizations.

%package -n texlive-nddiss
Summary:        Notre Dame Dissertation format class
Version:        svn45107
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nddiss
This class file conforms to the requirements of the Graduate School of the
University of Notre Dame; with it a user can format a thesis or dissertation in
LaTeX.

%package -n texlive-ndsu-thesis
Summary:        North Dakota State University disquisition class
Version:        svn46639
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ndsu-thesis
A class for generating disquisitions, intended to be in compliance with North
Dakota State University requirements.

%package -n texlive-ndsu-thesis-2022
Summary:        North Dakota State University disquisition class 2022
Version:        svn63881
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ndsu-thesis-2022
A class for generating disquisitions (MS and PhD - thesis, dissertation, and
paper), intended to be in compliance with North Dakota State University
requirements. Updated (2022) North Dakota State University LaTeX thesis class
features several functionalities, including not limited to, numbered and
non-numbered versions, overall justification, document point sizes, fonts
options, SI units, show frames, URL breaking, long tables, subfigures,
multi-page figures, chapter styles, subfiles, algorithm listing, BibTeX and
BibLaTeX support, individual chapter and whole document bibliography, natbib
citations, and clever references. The supplied simple and extended samples
illustrate these features and guide students to use the class.

%package -n texlive-nih
Summary:        A class for NIH grant applications
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(denselists.sty) = %{tl_version}

%description -n texlive-nih
The nih class offers support for grant applications to NIH, the National
Institutes of Health, a US government agency. The example-* files provide a
template for using nih.cls and submitting the biographical sketches the NIH
wants. They (potentially) use denselists package, which just reduces list
spacing; the package is distributed with the class, but is not part of the
class proper. (The examples may be distributed without even the restrictions of
the LaTeX licence.)

%package -n texlive-nihbiosketch
Summary:        A class for NIH biosketches based on the 2015 updated format
Version:        svn54191
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nihbiosketch
This LaTeX document class tries to adhere to the Biographical Sketch formatting
requirements outlined in NIH Notice [NOT-OD-15-032]
(grants.nih.gov/grants/guide/notice-files/NOT-OD-15-032.html). This new format
is required for applications submitted for due dates on or after May 25, 2015.
The package tries to mimic the example documents provided on the [SF 424 (R&R)
Forms and Applications page]
(grants.nih.gov/grants/funding/424/index.htm#format) as closely as possible.
The author has used this class for his own grant submissions; however he offers
no guarantee of conformity to NIH requirements.

%package -n texlive-njustthesis
Summary:        Thesis template for the Nanjing University of Science and Technology
Version:        svn62451
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-njustthesis
This is a thesis template for the Nanjing University of Science and
Technology>.

%package -n texlive-njuthesis
Summary:        LaTeX thesis template for Nanjing University
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(njuthesis-graduate.def) = %{tl_version}
Provides:       tex(njuthesis-postdoctoral.def) = %{tl_version}
Provides:       tex(njuthesis-undergraduate.def) = %{tl_version}

%description -n texlive-njuthesis
The njuthesis class is intended for typesetting Nanjing University
dissertations with LaTeX, providing support for bachelor, master, and doctoral
theses as well as postdoctoral reports. Compilation of this class requires
either XeLaTeX or LuaLaTeX.

%package -n texlive-njuvisual
Summary:        Display logos related to Nanjing University
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(njuvisual-emblem-ai.def) = %{tl_version}
Provides:       tex(njuvisual-emblem-chem.def) = %{tl_version}
Provides:       tex(njuvisual-emblem-cs.def) = %{tl_version}
Provides:       tex(njuvisual-emblem-dii.def) = %{tl_version}
Provides:       tex(njuvisual-emblem-eng.def) = %{tl_version}
Provides:       tex(njuvisual-emblem-nju.def) = %{tl_version}
Provides:       tex(njuvisual-emblem-physics.def) = %{tl_version}
Provides:       tex(njuvisual-emblem-software.def) = %{tl_version}
Provides:       tex(njuvisual-motto-nju.def) = %{tl_version}
Provides:       tex(njuvisual-name-en-nju.def) = %{tl_version}
Provides:       tex(njuvisual-name-zh-nju.def) = %{tl_version}
Provides:       tex(njuvisual-spirit-nju.def) = %{tl_version}
Provides:       tex(njuvisual.sty) = %{tl_version}

%description -n texlive-njuvisual
The njuvisual package collects standard colors and logos related to Nanjing
University, saves the vector logos as TikZ pictures and provides a
user-friendly interface to display them in documents and beamers.

%package -n texlive-nostarch
Summary:        LaTeX class for No Starch Press
Version:        svn67683
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)
Provides:       tex(nshyper.sty) = %{tl_version}

%description -n texlive-nostarch
The package provides the "official" LaTeX style for No Starch Press. Provided
are a class, a package for interfacing to hyperref and an index style file. The
style serves both for printed and for electronic books.

%package -n texlive-novel
Summary:        Class for printing fiction, such as novels
Version:        svn77677
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fancyhdr.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(luacode.sty)
Requires:       tex(microtype.sty)
Requires:       tex(wrapfig.sty)
Provides:       tex(novel-CalculateLayout.sty) = %{tl_version}
Provides:       tex(novel-ChapterScene.sty) = %{tl_version}
Provides:       tex(novel-DropCap.sty) = %{tl_version}
Provides:       tex(novel-FileData.sty) = %{tl_version}
Provides:       tex(novel-Fonts.sty) = %{tl_version}
Provides:       tex(novel-Footnotes.sty) = %{tl_version}
Provides:       tex(novel-HeadFootStyles.sty) = %{tl_version}
Provides:       tex(novel-Images.sty) = %{tl_version}
Provides:       tex(novel-LayoutSettings.sty) = %{tl_version}
Provides:       tex(novel-PostLayout.sty) = %{tl_version}
Provides:       tex(novel-Sandbox.sty) = %{tl_version}
Provides:       tex(novel-TextMacros.sty) = %{tl_version}
Provides:       tex(novel-pdfx.sty) = %{tl_version}
Provides:       tex(novel-xmppacket.sty) = %{tl_version}

%description -n texlive-novel
This LuaLaTeX document class is specifically written to meet the needs of
original fiction writers, who are typesetting their own novels for non-color
print-on-demand technology. Built-in PDF/X is available, using new technology.
The package is well suited for detective novels, science fiction, and short
stories. It is however not recommended for creating color picture books or
dissertations.

%package -n texlive-nrc
Summary:        Class for the NRC technical journals
Version:        svn29027
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(nrc1.sty) = %{tl_version}
Provides:       tex(nrc2.sty) = %{tl_version}

%description -n texlive-nrc
Macros, and some documentation, for typesetting papers for submission to
journals published by the National Research Council Research Press. At present,
only nrc2.cls (for two-column layout) should be used.

%package -n texlive-nstc-proposal
Summary:        LaTeX classes for preparing grant proposals to National Science and Technology Council, Taiwan
Version:        svn72795
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nstc-proposal
This package consists of LaTeX classes for preparing grant proposals to the
National Science and Technology Council, Taiwan, that is: CM03 CM302 which
support typesetting in both Chinese and English and are compatible with
pdfLaTeX and XeTeX.

%package -n texlive-nwafuthesis
Summary:        A thesis template package for Northwest A&F University, China
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nwafuthesis
This template supports doctoral and master dissertations and undergraduate
theses in Chinese. With the help of modern LaTeX3 technology, nwafuthesis aims
to create a simple interface, a normative format, as well as a hackable class
for the users. At present, nwafuthesis only supports XeTeX and LuaTeX engines.
nwafuthesis only allows UTF-8 encoding. nwafuthesis is based on the fduthesis
template.

%package -n texlive-nwejm
Summary:        Support for the journal "North-Western European Journal of Mathematics"
Version:        svn70597
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Provides:       tex(nwejm-logos-collection.tex) = %{tl_version}
Provides:       tex(nwejm.bbx) = %{tl_version}
Provides:       tex(nwejm.cbx) = %{tl_version}

%description -n texlive-nwejm
The bundle includes LaTeX classes and BibLaTeX styles files dedicated to the
new journal "North-Western European Journal of Mathematics": nwejm for the
complete issues of the journal, aimed at the NWEJM's team, nwejmart, intended
for the authors who wish to publish an article in the NWEJM. This class's goal
is to: faithfully reproduce the layout of the nwejm, thus enabling the authors
to be able to work their document in actual conditions, provide a number of
tools (commands and environments) to facilitate the drafting of documents, in
particular those containing mathematical formulas.

%package -n texlive-nxuthesis
Summary:        Thesis template for Ningxia University
Version:        svn74831
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nxuthesis
This package provides a LaTeX thesis template for Ningxia University in order
to make it easy to write theses for graduate students.

%package -n texlive-omgtudoc-asoiu
Summary:        A class for documents of the ASOIU department at Omsk State Technical University
Version:        svn74183
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(gost-standard.bbx)
Provides:       tex(omgtudoc-asoiu-gost-numeric.bbx) = %{tl_version}

%description -n texlive-omgtudoc-asoiu
This package provides a class for documents which are prepared on the
"Automatic systems for information processing and control" (ASOIU) of Omsk
State Technical University, Omsk, Russia. The class is based on the article
class and requires XeLaTeX or LuaLaTeX for its proper working. Formatting
complies with the instructions issued on January 29, 2024 and at GOST
7.32-2017.

%package -n texlive-onrannual
Summary:        Class for Office of Naval Research Ocean Battlespace Sensing annual report
Version:        svn17474
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-onrannual
This is an unofficial document class for writing ONR annual reports using
LaTeX; as ONR has had numerous problems with LaTeX-generated PDF submissions in
the past. A skeleton document (and its PDF output) are included.

%package -n texlive-opteng
Summary:        SPIE Optical Engineering and OE Letters manuscript template
Version:        svn27331
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(overcite.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(opteng.sty) = %{tl_version}

%description -n texlive-opteng
With this template, and associated style and LaTeX packages, it is possible to
estimate the page length of manuscripts for submission to the SPIE journals
'Optical Engineering' and 'Optical Engineering Letters'. With a strict
three-page limit, this is particularly important for the latter. The template
gives simple instructions on how to prepare the manuscript.

%package -n texlive-oststud
Summary:        Templates for the student organization at OST FH, Switzerland
Version:        svn67217
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(esint.sty)
Requires:       tex(esvect.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(hsrstud.sty) = %{tl_version}
Provides:       tex(oststud.sty) = %{tl_version}

%description -n texlive-oststud
This package is made by the student organization at the University of Applied
Sciences of Eastern Switzerland (Ostschweizer Fachhochschule) to provide an
easy to use interface for newbies and give a more consistent look and feel to
the works produced by the organization's members. This package also contains
hsrstud.{ins,dtx} which is the older version of the oststud package before the
school changed its name in 2021. We would like to keep it for backwards
compatibility when compiling old documents that have not been migrated yet.

%package -n texlive-ou-tma
Summary:        A package to aid in the writing of Tutor Marked Assessments for the Open University
Version:        svn76460
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)
Requires:       tex(calc.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(isodate.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(upgreek.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(wasysym.sty)
Requires:       tex(xifthen.sty)
Provides:       tex(ou-tma.sty) = %{tl_version}

%description -n texlive-ou-tma
The ou-tma package simplifies the creation of TMAs (Tutor Marked Assessments)
by providing an environment to encompass answers to questions, commands to
enumerate parts and subparts of those questions, and a set of macros
facilitating mathematical entry based on the styles used by the Open University
(OU).

%package -n texlive-oup-authoring-template
Summary:        A general template for journals published by Oxford University Press (OUP)
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-oup-authoring-template
This package provides a general LaTeX template for journals published by Oxford
University Press (OUP). The template outputs to the three official page designs
(traditional, contemporary, modern) used by many journals published by OUP,
with large, medium and small page options. For more information see
https://academic.oup.com/journals/pages/authors/preparing_your_ manuscript.

%package -n texlive-pats-resume
Summary:        A LaTeX template for your resume
Version:        svn74532
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pats-resume
This package provides a compact and elegant template for your resume.

%package -n texlive-philosophersimprint
Summary:        Typesetting articles for "Philosophers' Imprint"
Version:        svn56954
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-philosophersimprint
In its mission statement we read "Philosophers' Imprint is a refereed series of
original papers in philosophy, edited by philosophy faculty at the University
of Michigan, with the advice of an international Board of Editors, and
published on the World Wide Web by the University of Michigan Digital Library.
The mission of the Imprint is to promote a future in which funds currently
spent on journal subscriptions are redirected to the dissemination of
scholarship for free, via the Internet". The class helps authors to typeset
their own articles in "Web-ready" format. No assumption is made about the fonts
available to the author: the class itself is restricted to freely available and
freely distributed fonts, only.

%package -n texlive-phimisci
Summary:        A document class for the journal "Philosophy and the Mind Sciences"
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-phimisci
This package provides a document class for the open-access journal Philosophy
and the Mind Sciences.

%package -n texlive-pittetd
Summary:        Electronic Theses and Dissertations at Pitt
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pittetd
A document class for theses and dissertations. Provides patch files that enable
pittetd to use files prepared for use with the pittdiss or pitthesis classes.
The manual provides a detailed guide for users who wish to use the class to
prepare their thesis or dissertation.

%package -n texlive-pkuthss
Summary:        LaTeX template for dissertations in Peking University
Version:        svn70491
License:        LPPL-1.3c AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pkuthss-gbk.def) = %{tl_version}
Provides:       tex(pkuthss-utf8.def) = %{tl_version}
Provides:       tex(pkuthss.def) = %{tl_version}

%description -n texlive-pkuthss
The package provides a simple, clear and flexible LaTeX template for
dissertations in Peking University.

%package -n texlive-powerdot-fuberlin
Summary:        Powerdot, using the style of FU Berlin
Version:        svn52922
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(pifont.sty)
Requires:       tex(tabularx.sty)
Provides:       tex(powerdot-BerlinFU.sty) = %{tl_version}

%description -n texlive-powerdot-fuberlin
The bundle provides a powerdot-derived class and a package for use with
powerdot to provide the corporate design of the Free University in Berlin.
Users may use the class itself (FUpowerdot) or use the package in the usual way
with \style=BerlinFU as a class option. Examples of using both the class and
the package are provided; the PDF is visually identical, so the catalogue only
lists one; the sources of the examples do of course differ.

%package -n texlive-powerdot-tuliplab
Summary:        A style package for Powerdot to provide the design of TULIP Lab
Version:        svn47963
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pifont.sty)
Provides:       tex(powerdot-tuliplab.sty) = %{tl_version}

%description -n texlive-powerdot-tuliplab
powerdot-tuliplab is the LaTeX package used in TULIP Lab for presentation
drafting. It comes with several sample .tex files so that you can quickly start
working with it.

%package -n texlive-pracjourn
Summary:        Typeset articles for PracTeX
Version:        svn61719
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pracjourn
The pracjourn class is used for typesetting articles in the PracTeX Journal. It
is based on the article class with modifications to allow for more flexible
front-matter and revision control, among other small changes.

%package -n texlive-prociagssymp
Summary:        Macros for IAG symposium papers
Version:        svn70888
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(procIAGssymp.sty) = %{tl_version}

%description -n texlive-prociagssymp
This package provides (re-)definitions of some LaTeX commands that can be
useful for the preparation of papers with the style of the proceedings of
symposia sponsored by the 'International Association of Geodesy (IAG)'
published by Springer-Verlag.

%package -n texlive-proposal
Summary:        A set of LaTeX classes for preparing proposals for collaborative projects
Version:        svn40538
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(eurosym.sty)
# Ignoring dependency on workaddress.sty - not part of TeX Live
Requires:       tex(xspace.sty)
Provides:       tex(dfgpdata.sty) = %{tl_version}
Provides:       tex(eupdata.sty) = %{tl_version}
Provides:       tex(pdata.sty) = %{tl_version}

%description -n texlive-proposal
The process of preparing a collaborative proposal, to a major funding body,
involves integration of contributions of a many people at many sites. It is
therefore an ideal application for a text-based document preparation system
such as LaTeX, in concert with a distributed version control system such as
SVN. The proposal class itself provides a basis for such an enterprise. The
dfgproposal and dfgproposal classes provide two specialisations of the base
class for (respectively) German and European research proposals. The packages
depend on the author's stex bundle.

%package -n texlive-prtec
Summary:        A template for PRTEC conference papers
Version:        svn76790
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-prtec
This package provides a LaTeX class, a BibTeX style, and a LaTeX template to
format conference papers for the Pacific Rim Thermal Engineering Conference
(PRTEC). The .tex and .cls files are commented and should be self-explanatory.
The package depends on newtx.

%package -n texlive-ptptex
Summary:        Macros for 'Progress of Theoretical Physics'
Version:        svn19440
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(wrapfig.sty)
Provides:       tex(wrapft.sty) = %{tl_version}

%description -n texlive-ptptex
The distribution contains the class (which offers an option file for
preprints), and a template. The class requires the cite, overcite and wrapfig
packages.

%package -n texlive-qrbill
Summary:        Create QR bills using LaTeX
Version:        svn76924
License:        LPPL-1.3c AND BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(anyfontsize.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(numprint.sty)
Requires:       tex(qrcode.sty)
Requires:       tex(scrbase.sty)
Provides:       tex(epc.qrbill-cfg.tex) = %{tl_version}
Provides:       tex(qrbill.sty) = %{tl_version}
Provides:       tex(swiss.qrbill-cfg.tex) = %{tl_version}

%description -n texlive-qrbill
This LaTeX package provides support for creating QR-bills for the new Swiss
payment standards. This open source implementation is intended to offer a free
option to support these regulations and can be adapted for international use.
Packages loaded by qrbill are expl3, fontspec (except if one is using a custom
font setup), graphicx, scrbase, qrcode, iftex, l3keys2e, and numprint.

%package -n texlive-quantumarticle
Summary:        Document class for submissions to the Quantum journal
Version:        svn65242
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-quantumarticle
This package provides the preferred document class for papers to be submitted
to "Quantum -- the open journal of quantum science". It is based on the widely
used article document class and designed to allow a seamless transition from
documents typeset with the article, revtex4-1, and elsarticle document classes.
As a service to authors, the document class comes with a predefined
bibilography style quantum.bst that is optimized to be used with the
quantumarticle document class. Additionally, the quantumview documentclass is
provided, which can be used as a proxy to typeset the HTML-only editorial
pieces in Quantum Views in a LaTeX editor. The quantumarticle document class
also offers an option to remove the Quantum-related branding. In that way,
users appreciating the esthetics of this document class can use it for their
notes as well.

%package -n texlive-rebuttal
Summary:        Markup for structured journal and conference paper rebuttals
Version:        svn72851
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(pdfcomment.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(soul.sty)
Requires:       tex(tikz.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(ulem.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
Provides:       tex(rebuttal.sty) = %{tl_version}

%description -n texlive-rebuttal
This package provides means for writing structured journal and conference paper
rebuttals.

%package -n texlive-regulatory
Summary:        Flexible drafting of legal documents, especially in Dutch
Version:        svn72197
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(glossaries-extra.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(keyval.sty)
Requires:       tex(markdown.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(translations.sty)
Requires:       tex(xassoccnt.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xr-hyper.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Requires:       tex(zref-clever.sty)
Requires:       tex(zref-hyperref.sty)
Requires:       tex(zref-user.sty)
Requires:       tex(zref-xr.sty)
Requires:       tex(zref.sty)
Provides:       tex(regulatory.sty) = %{tl_version}

%description -n texlive-regulatory
This package aims to simplify the writing process, especially for Dutch legal
authors. It has also been implemented in English and can be expanded to include
other languages. The package offers macros for typical legal structures and
contains a referencing system.

%package -n texlive-resphilosophica
Summary:        Typeset articles for the journal Res Philosophica
Version:        svn76471
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-resphilosophica
The bundle provides a class for typesetting articles for the journal Res
Philosophica. This work was commissioned by the Saint Louis University.

%package -n texlive-resumecls
Summary:        Typeset a resume both in English and Chinese
Version:        svn54815
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-resumecls
A LaTeX document class to typeset a resume or CV both in English and Chinese
with more ease and flexibility.

%package -n texlive-retosmatematicos
Summary:        LaTeX template for the Telegram group "Retos Matematicos"
Version:        svn76358
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cancel.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(esvect.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(polynom.sty)
Requires:       tex(scalerel.sty)
Requires:       tex(setspace.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(systeme.sty)
Requires:       tex(upgreek.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xfrac.sty)
Requires:       tex(yhmath.sty)
Provides:       tex(RetoExtra.sty) = %{tl_version}

%description -n texlive-retosmatematicos
This package provides the class RetoMatematico.cls, which is used to typeset
the final solutions of the mathematical challenges published in the Telegram
group Retos Matematicos (by Jose Manuel Sanchez Munoz). Among its features, the
class sets the document size to letter paper, switches the font to Palatino
Linotype (via the mathpazo package), and places information such as the group's
ISSN and link in the page margins. Further details and usage examples are
available in the package documentation.

%package -n texlive-revtex
Summary:        Styles for various Physics Journals
Version:        svn67271
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(shortvrb.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(ltxdocext.sty) = %{tl_version}
Provides:       tex(ltxfront.sty) = %{tl_version}
Provides:       tex(ltxgrid.sty) = %{tl_version}
Provides:       tex(ltxutil.sty) = %{tl_version}
Provides:       tex(revsymb4-2.sty) = %{tl_version}

%description -n texlive-revtex
Includes styles for American Physical Society, American Institute of Physics,
and Optical Society of America. The distribution consists of the RevTeX class
itself, and several support packages.

%package -n texlive-revtex4
Summary:        Styles for various Physics Journals (old version)
Version:        svn56589
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(revsymb.sty) = %{tl_version}

%description -n texlive-revtex4
This is an old version of revtex, and is kept as a courtesy to users having
difficulty with the incompatibility of that latest version.

%package -n texlive-revtex4-1
Summary:        Styles for various Physics Journals
Version:        svn56590
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(revsymb4-1.sty) = %{tl_version}

%description -n texlive-revtex4-1
This is an old version of revtex, and is kept as a courtesy to users having
difficulty with the incompatibility of that latest version.

%package -n texlive-rub-kunstgeschichte
Summary:        A class for the art history institute at Ruhr University Bochum
Version:        svn73739
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-rub-kunstgeschichte
This package provides a LaTeX class implementing the guidelines on scientific
writing of the art history institute (Kunstgeschichtliches Institut) at Ruhr
University Bochum.

%package -n texlive-rutitlepage
Summary:        Radboud University Titlepage Package
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Provides:       tex(rutitlepage.sty) = %{tl_version}

%description -n texlive-rutitlepage
This is an unofficial LaTeX package to generate titlepages for the Radboud
University, Nijmegen. It uses official vector logos from the university. This
package requires the following other LaTeX packages: geometry, graphicx, ifpdf,
keyval, iflang, and, optionally, babel-dutch.

%package -n texlive-rwth-ci
Summary:        LaTeX templates using CI of RWTH Aachen University
Version:        svn77480
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(anyfontsize.sty)
Requires:       tex(arimo.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(scrletter.sty)
Requires:       tex(trimclip.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(beamercolorthemeRWTH.sty) = %{tl_version}
Provides:       tex(beamerfontthemeRWTH.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeRWTH.sty) = %{tl_version}
Provides:       tex(beamerouterthemeRWTH.sty) = %{tl_version}
Provides:       tex(beamerthemeRWTH.sty) = %{tl_version}
Provides:       tex(rwth-colors.sty) = %{tl_version}
Provides:       tex(rwth-fonts.sty) = %{tl_version}
Provides:       tex(rwth-layout.sty) = %{tl_version}
Provides:       tex(rwth-letter.sty) = %{tl_version}
Provides:       tex(rwthcolors.def) = %{tl_version}

%description -n texlive-rwth-ci
The RWTH-CI-Bundle is the official LaTeX bundle of RWTH Aachen University to
use their Corporate Identity within LaTeX.

%package -n texlive-ryersonsgsthesis
Summary:        Ryerson School of Graduate Studies thesis template
Version:        svn50119
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ryersonsgsthesis
This package provides a LaTeX class and template files for Ryerson School of
Graduate Studies (SGS) theses.

%package -n texlive-ryethesis
Summary:        Class for Ryerson University Graduate School requirements
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ryethesis
The class offers support for formatting a thesis, dissertation or project
according to Ryerson University's School of Graduate Studies thesis formatting
regulations.

%package -n texlive-sageep
Summary:        Format papers for the annual meeting of EEGS
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sageep
The class provides formatting for papers for the annual meeting of the
Environmental and Engineering Geophysical Society (EEGS) ("Application of
Geophysics to Engineering and Environmental Problems", known as SAGEEP).

%package -n texlive-sapthesis
Summary:        Typeset theses for Sapienza-University, Rome
Version:        svn63810
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sapthesis
The class will typeset Ph.D., Master, and Bachelor theses that adhere to the
publishing guidelines of the Sapienza University of Rome.

%package -n texlive-schule
Summary:        Support for teachers at German schools
Version:        svn77551
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(cancel.sty)
Requires:       tex(ccicons.sty)
Requires:       tex(circuitikz.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(environ.sty)
Requires:       tex(etex.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(forarray.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listings.sty)
Requires:       tex(mhchem.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pgf-umlcd.sty)
Requires:       tex(pgf-umlsd.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(rotating.sty)
Requires:       tex(silence.sty)
Requires:       tex(struktex.sty)
Requires:       tex(svn-multi.sty)
Requires:       tex(syntaxdi.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(units.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xmpincl.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(relaycircuit.sty) = %{tl_version}
Provides:       tex(schule.fach.EvReligion.code.tex) = %{tl_version}
Provides:       tex(schule.fach.Geschichte.code.tex) = %{tl_version}
Provides:       tex(schule.fach.Geschichte.pakete.tex) = %{tl_version}
Provides:       tex(schule.fach.Informatik.code.tex) = %{tl_version}
Provides:       tex(schule.fach.Informatik.pakete.tex) = %{tl_version}
Provides:       tex(schule.fach.Physik.code.tex) = %{tl_version}
Provides:       tex(schule.fach.Physik.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Aufgaben.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Aufgaben.optionen.tex) = %{tl_version}
Provides:       tex(schule.mod.Aufgaben.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Aufgabenpool.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Aufgabenpool.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Bewertung.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Bewertung.optionen.tex) = %{tl_version}
Provides:       tex(schule.mod.Bewertung.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Format.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Format.optionen.tex) = %{tl_version}
Provides:       tex(schule.mod.Format.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Formulare.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Kuerzel.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Kuerzel.optionen.tex) = %{tl_version}
Provides:       tex(schule.mod.Lizenzen.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Lizenzen.optionen.tex) = %{tl_version}
Provides:       tex(schule.mod.Lizenzen.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Metadaten.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Metadaten.optionen.tex) = %{tl_version}
Provides:       tex(schule.mod.Papiertypen.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Storycard.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Storycard.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Symbole.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Symbole.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.Texte.code.tex) = %{tl_version}
Provides:       tex(schule.mod.Texte.pakete.tex) = %{tl_version}
Provides:       tex(schule.mod.genord.code.tex) = %{tl_version}
Provides:       tex(schule.sty) = %{tl_version}
Provides:       tex(schule.typ.Beurteilung.code.tex) = %{tl_version}
Provides:       tex(schule.typ.Beurteilung.optionen.tex) = %{tl_version}
Provides:       tex(schule.typ.Beurteilung.pakete.tex) = %{tl_version}
Provides:       tex(schule.typ.ab.code.tex) = %{tl_version}
Provides:       tex(schule.typ.ab.pakete.tex) = %{tl_version}
Provides:       tex(schule.typ.folie.code.tex) = %{tl_version}
Provides:       tex(schule.typ.folie.pakete.tex) = %{tl_version}
Provides:       tex(schule.typ.kl.code.tex) = %{tl_version}
Provides:       tex(schule.typ.kl.optionen.tex) = %{tl_version}
Provides:       tex(schule.typ.kl.pakete.tex) = %{tl_version}
Provides:       tex(schule.typ.leit.code.tex) = %{tl_version}
Provides:       tex(schule.typ.leit.optionen.tex) = %{tl_version}
Provides:       tex(schule.typ.leit.pakete.tex) = %{tl_version}
Provides:       tex(schule.typ.lzk.code.tex) = %{tl_version}
Provides:       tex(schule.typ.lzk.pakete.tex) = %{tl_version}
Provides:       tex(schule.typ.ub.code.tex) = %{tl_version}
Provides:       tex(schule.typ.ub.pakete.tex) = %{tl_version}
Provides:       tex(schule.typ.ueb.code.tex) = %{tl_version}
Provides:       tex(schule.typ.ueb.pakete.tex) = %{tl_version}
Provides:       tex(schulealt.sty) = %{tl_version}
Provides:       tex(schulekl.sty) = %{tl_version}
Provides:       tex(schulinf.sty) = %{tl_version}
Provides:       tex(schullzk.sty) = %{tl_version}
Provides:       tex(schulphy.sty) = %{tl_version}
Provides:       tex(xsim.style.schule-binnen.code.tex) = %{tl_version}
Provides:       tex(xsim.style.schule-default.code.tex) = %{tl_version}
Provides:       tex(xsim.style.schule-keinenummer.code.tex) = %{tl_version}
Provides:       tex(xsim.style.schule-keinepunkte.code.tex) = %{tl_version}
Provides:       tex(xsim.style.schule-keintitel.code.tex) = %{tl_version}
Provides:       tex(xsim.style.schule-randpunkte.code.tex) = %{tl_version}
Provides:       tex(xsim.style.schule-tabelle-kurz.code.tex) = %{tl_version}
Provides:       tex(xsim.style.schule-tcolorbox.code.tex) = %{tl_version}

%description -n texlive-schule
The 'schule' bundle was built to provide packages and commands that could be
useful for documents in German schools. At the moment its main focus lies on
documents for informatics as a school subject. An extension for physics is
currently in progress. Extensions for other subjects are welcome. For the time
being, the whole package splits up into individual packages for informatics
(including syntax diagrams, Nassi-Shneiderman diagrams, sequence diagrams,
object diagrams, and class diagrams) as well as classes for written exams
(tests, quizzes, teaching observations, information sheets, worksheets, and
answer keys).

%package -n texlive-scientific-thesis-cover
Summary:        Provides cover page and affirmation at the end of a thesis
Version:        svn47923
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(scientific-thesis-cover.sty) = %{tl_version}

%description -n texlive-scientific-thesis-cover
Institutions require a cover page and an affirmation at the end of a thesis.
This package provides both.

%package -n texlive-scripture
Summary:        A LaTeX style for typesetting Bible quotations
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(scripture.sty) = %{tl_version}

%description -n texlive-scripture
The scripture package provides a set of macros for typesetting quotations from
the Bible. It provides many features commonly seen in Bibles such as dropped
text for chapter numbers, superscripts for verse numbers, indented lines for
poetry sections, narrow sections and hanging paragraphs. A reference for the
quotation can optionally be added.

%package -n texlive-scrjrnl
Summary:        Typeset diaries or journals
Version:        svn74998
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-scrjrnl
A class, based on scrbook, designed for typesetting diaries, journals or
devotionals.

%package -n texlive-sduthesis
Summary:        Thesis Template of Shandong University
Version:        svn41401
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sduthesis-cover.def) = %{tl_version}
Provides:       tex(sduthesis-statement.def) = %{tl_version}

%description -n texlive-sduthesis
Thesis Template of Shandong University.

%package -n texlive-se2thesis
Summary:        A Thesis Class for the Chair of Software Engineering II at the University of Passau, Germany
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biblatex.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(fvextra.sty)
Requires:       tex(inconsolata-nerd-font.sty)
Requires:       tex(inconsolata.sty)
Requires:       tex(libertinus-otf.sty)
Requires:       tex(libertinus-type1.sty)
Requires:       tex(listings.sty)
Requires:       tex(lua-widow-control.sty)
Requires:       tex(microtype.sty)
Requires:       tex(minted.sty)
Requires:       tex(mismath.sty)
Requires:       tex(selnolig.sty)
Requires:       tex(sidenotesplus.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(software-biblatex.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(se2colors.sty) = %{tl_version}
Provides:       tex(se2fonts.sty) = %{tl_version}
Provides:       tex(se2packages.sty) = %{tl_version}

%description -n texlive-se2thesis
The se2thesis bundle provides a document class for writing a theses with the
Chair of Software Engineering II at the University of Passau, Germany. The
class is based on Markus Kohm's KOMA-Script classes and provides several
additions and customizations to these classes. While the class provides some
basic settings, mostly regrading the type area, fonts, and the title page, it
still provides large degrees of freedom to its users. However, the package's
documentation also provides recommendations regarding several aspects, for
example, recommending BibLaTeX for bibliographies.

%package -n texlive-seu-ml-assign
Summary:        Southeast University Machine Learning Assignment template
Version:        svn62933
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-seu-ml-assign
This is a template for the Southeast University Machine Learning Assignment
that can be easily adapted to other usages. This template features a colorful
theme that makes it look elegant and attractive. You can also find the template
available on Overleaf.

%package -n texlive-seuthesis
Summary:        LaTeX template for theses at Southeastern University
Version:        svn33042
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-seuthesis
This template is for theses at Southeastern University, Nanjing, China.

%package -n texlive-seuthesix
Summary:        LaTeX class for theses at Southeast University, Nanjing, China
Version:        svn40088
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-seuthesix
This project provides a LaTeX document class as well as a bibliography style
file for typesetting theses at the Southeast University, Nanjing, China. It is
based on the seuthesis package which, according to the author of seuthesix, is
buggy and has not been maintained for some time.

%package -n texlive-sfee
Summary:        A LaTeX class for the Smart Factory and Energy Efficence magazine of the Tecnologico
Version:        svn70718
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sfee
The SFEE class belongs to the Smart Factory and Energy Efficence magazine of
the Tecnologico Nacional de Mexico/ITS Purisima del Rincon. SFEE.cls was
designed using the LaTeX document class standard. It is accompanied by
SFEE.bst, which provides the necessary elements to generate the article
citations.

%package -n texlive-shortmathj
Summary:        Automatically shortify titles of mathematical journals
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(xstring.sty)
Provides:       tex(shortmathj.sty) = %{tl_version}

%description -n texlive-shortmathj
This small dummy package just contains a simple list of full and short journal
names as written in AMS standard:
https://mathscinet.ams.org/msnhtml/serials.pdf

%package -n texlive-shtthesis
Summary:        An unofficial LaTeX thesis template for ShanghaiTech University
Version:        svn62441
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-alphalph
Requires:       biber
Requires:       texlive-biblatex
Requires:       texlive-biblatex-gb7714-2015
Requires:       texlive-booktabs
Requires:       texlive-caption
Requires:       texlive-colortbl
Requires:       texlive-ctex
Requires:       texlive-datetime
Requires:       texlive-enumitem
Requires:       texlive-fancyhdr
Requires:       texlive-fmtcount
Requires:       texlive-lastpage
Requires:       latexmk
Requires:       texlive-listings
Requires:       texlive-lua-alt-getopt
Requires:       texlive-lualatex-math
Requires:       texlive-mathtools
Requires:       texlive-ntheorem
Requires:       texlive-tex-gyre
Requires:       texlive-tocvsec2
Requires:       texlive-transparent
Requires:       texlive-undolabl
Requires:       texlive-unicode-math
Requires:       texlive-xits
Requires:       texlive-xstring

%description -n texlive-shtthesis
This package, forked from ucasthesis, is an unofficial LaTeX thesis template
for ShanghaiTech University and satisfies all format requirements of the
school. The user just needs to set \documentclass{shtthesis} and to set up
mandatory information via \shtsetup, then his or her thesis document will be
typeset properly.

%package -n texlive-smflatex
Summary:        Classes for Societe mathematique de France publications
Version:        svn58910
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ae.sty)
Requires:       tex(amscd.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
# Ignoring dependency on europs.sty - non-free
Requires:       tex(fontenc.sty)
Requires:       tex(mltex.sty)
# Ignoring dependency on smfbask.sty - not part of TeX Live
Requires:       tex(textcomp.sty)
Requires:       tex(url.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xy.sty)
Provides:       tex(smfbib.sty) = %{tl_version}
Provides:       tex(smfbull.sty) = %{tl_version}
Provides:       tex(smfenum.sty) = %{tl_version}
Provides:       tex(smfgen.sty) = %{tl_version}
Provides:       tex(smfhyperref.sty) = %{tl_version}
Provides:       tex(smfmulti.sty) = %{tl_version}
Provides:       tex(smfthm.sty) = %{tl_version}

%description -n texlive-smflatex
The Societe mathematique de France provides a set of classes, packages and
BibTeX styles that are used in its publications. They are based on AMS classes
(whose code is sometimes recopied) and mainly 'upward-compatible'. Their main
features are: quite different design; new environments for typesetting some
information in two languages (altabstract, alttitle, altkeywords); if
necessary, use of babel (option frenchb) and deactivation of some features of
frenchb. Includes smfart.cls, smfbook.cls, smfplain.bst, smfalpha.bst, amongst
others.

%package -n texlive-soton
Summary:        University of Southampton-compliant slides
Version:        svn16215
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Provides:       tex(soton-beamer.sty) = %{tl_version}
Provides:       tex(soton-palette.sty) = %{tl_version}

%description -n texlive-soton
The bundle contains two packages: soton-palette which defines colour-ways, and
soton-beamer, which uses the colours to produce compliant presentations.

%package -n texlive-sphdthesis
Summary:        LaTeX template for writing PhD Thesis
Version:        svn34374
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sphdthesis
The package provides a LaTeX document class for writing a PhD thesis. The
author developed it while writing his PhD thesis in School of Computing (SoC),
National University of Singapore (NUS). By default, the class adheres to the
NUS Guidelines on Format of Research Thesis Submitted For Examination. However,
the class for conformation to a different guideline should not be difficult.

%package -n texlive-spie
Summary:        Support for formatting SPIE Proceedings manuscripts
Version:        svn75447
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-spie
A class and a BibTeX style are provided.

%package -n texlive-sr-vorl
Summary:        Class for Springer books
Version:        svn59333
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sr-vorl
This package provides a LaTeX class and templates for books to be published at
Springer Gabler Research, Springer Vieweg Research, Springer Spektrum Research,
Springer VS Research, or Springer VS Forschung. It may be used to produce
monographs in different formats and "several-authors-books" fitting the
conditions of the aforementioned publishers.

%package -n texlive-srdp-mathematik
Summary:        Typeset Austrian SRDP in mathematics
Version:        svn76697
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(cancel.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(color.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(delarray.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(esvect.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(float.sty)
Requires:       tex(forloop.sty)
Requires:       tex(fp.sty)
Requires:       tex(framed.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hhline.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(linegoal.sty)
Requires:       tex(longtable.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(pgf-pie.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(pgfplotstable.sty)
Requires:       tex(phaistos.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(setspace.sty)
Requires:       tex(spreadtab.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(wasysym.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(ziffer.sty)
Provides:       tex(srdp-mathematik.sty) = %{tl_version}
Provides:       tex(srdp-tables.sty) = %{tl_version}

%description -n texlive-srdp-mathematik
This package provides basic commands for the defined formats of the Austrian
sRDP (Standardisierte Reife- und Diplomprufung) in mathematics. Furthermore, it
includes ways to implement answers in the tex file which can optionally be
displayed in the pdf file, and it offers a way to vary the answers in order to
create different groups (e. g. for tests) easily.

%package -n texlive-sshrc-insight
Summary:        A LaTeX class for SSHRC Insight Grant proposals
Version:        svn76065
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sshrc-insight
The sshrc-insight LaTeX class facilitates the preparation of funding proposals
for the Insight Grants program of Canada's Social Sciences and Humanities
Research Council (SSHRC). It has the following key features: Formats the
proposal according to the SSHRC's specifications. Allows parts of the proposal
to be compiled into separate PDFs to attach to the appropriate places in the
online application form. Alternatively, allows the proposal to be compiled into
a single PDF in order to facilitate the writing and pre-submission reviewing
process. Ensures that citation numbering remains consistent regardless whether
the proposal is compiled as separate PDFs or a single PDF. Provides character
counts for long-answer form fields. Supports preparation of proposals in either
English or French. Compatible with pdfLaTeX, XeLaTeX, and LuaLaTeX.

%package -n texlive-stellenbosch
Summary:        Stellenbosch thesis bundle (legacy version)
Version:        svn68039
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(longtable.sty)
Provides:       tex(usbib.sty) = %{tl_version}
Provides:       tex(usnomencl.sty) = %{tl_version}
Provides:       tex(ussummary.sty) = %{tl_version}
Provides:       tex(usthesis.sty) = %{tl_version}
Provides:       tex(ustitle.sty) = %{tl_version}

%description -n texlive-stellenbosch
Note: This bundle should only be used for typesetting legacy documents. For new
documents, its successor stellenbosch-2 is available. The usthesis class/style
files are provided to typeset reports, theses and dissertations that conform to
the requirements of the Engineering Faculty of the University of Stellenbosch.
The class file usthesis.cls is based on the standard LaTeX book class, while
usthesis.sty is a style file to be loaded on top of the very powerful memoir
class. Both options give identical output, but the benefit of the using memoir
is that it has many additional command and environments for formatting and
processing of a document. Usthesis is primarily concerned with the formatting
of the front matter such as the title page, abstract, etc. and a decent page
layout on A4 paper. It also works together with the babel package to provide
language options to typeset documents in Afrikaans or in English. Additional
packages are provided for bibliographic matter, note title pages, lists of
symbols, as well as various graphic files for logos.

%package -n texlive-stellenbosch-2
Summary:        Stellenbosch University thesis bundle
Version:        svn68183
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(stb-beamer-a.sty) = %{tl_version}
Provides:       tex(stb-beamer-b.sty) = %{tl_version}
Provides:       tex(stb-bib.sty) = %{tl_version}
Provides:       tex(stb-nomencl.sty) = %{tl_version}
Provides:       tex(stb-titlepage.sty) = %{tl_version}

%description -n texlive-stellenbosch-2
Typesetting dissertations, theses and reports as well as presentations of
Stellenbosch University, South Africa. Note: The previous version,
stellenbosch, is still available for legacy documents.

%package -n texlive-suftesi
Summary:        A document class for typesetting theses, books and articles
Version:        svn73055
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-suftesi
The class can be used to typeset any kind of book (originally designed for use
in the humanities).

%package -n texlive-sugconf
Summary:        SAS(R) user group conference proceedings document class
Version:        svn58752
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sugconf
The class may be used to typeset articles to be published in the proceedings of
SAS(R) User group conferences and workshops. The layout produced by the class
is based on that published by SAS Institute (2021).

%package -n texlive-sysuthesis
Summary:        LaTeX thesis template for Sun Yat-sen University
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sysuvisual.sty) = %{tl_version}

%description -n texlive-sysuthesis
This class is intended for typesetting Sun Yat-sen University dissertations
with LaTeX, providing support for bachelor, master, doctoral thesis.
Compilation of this class requires either the XeLaTeX or the LuaLaTeX engine.

%package -n texlive-tabriz-thesis
Summary:        A template for the University of Tabriz
Version:        svn51729
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tabriz-thesis
The package offers a document class for typesetting theses and dissertations at
the University of Tabriz. The class requires use of XeLaTeX.

%package -n texlive-technion-thesis-template
Summary:        Template for theses on the Technion graduate school
Version:        svn49889
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(technionThesisSetup.sty) = %{tl_version}

%description -n texlive-technion-thesis-template
This is a template for writing a thesis according to the Technion
specifications.

%package -n texlive-texilikechaps
Summary:        Format chapters with a texi-like format
Version:        svn28553
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(texilikechaps.sty) = %{tl_version}

%description -n texlive-texilikechaps
The package enables the user to reduce the size of the rather large chapter
headings in standard classes into a texi-like smaller format. Details of the
format may be controlled with internal commands.

%package -n texlive-texilikecover
Summary:        A cover-page package, like TeXinfo
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(texilikecover.sty) = %{tl_version}

%description -n texlive-texilikecover
The package creates document cover pages, like those that TeXinfo produces.

%package -n texlive-thesis-ekf
Summary:        Thesis class for Eszterhazy Karoly Catholic University
Version:        svn77332
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-thesis-ekf
This bundle provides a LaTeX class for theses and dissertations at Eszterhazy
Karoly Catholic University (Eger, Hungary). The documentation is written in
Hungarian.

%package -n texlive-thesis-gwu
Summary:        Thesis class for George Washington University School of Engineering and Applied Science
Version:        svn54287
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-thesis-gwu
This class is an attempt to create a standard format for GWU SEAS
dissertations/theses. It automatically handles many of the complicated
formatting requirements and includes many useful packages. An example thesis is
provided serving as a user guide and a demonstration of the thesis.

%package -n texlive-thesis-qom
Summary:        Thesis style of the University of Qom, Iran
Version:        svn63524
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-thesis-qom
This package provides a class file for writing theses and dissertations
according to the University of Qom Graduate Schools's guidelines for the
electronic submission of master theses and PhD dissertations. The class should
meet all the current requirements and is updated whenever the university
guidelines change. The class needs XeLaTeX in conjunction with the following
fonts: XB Niloofar, IranNastaliq, IRlotus, XB Zar, XB Titre, and Yas.

%package -n texlive-thesis-titlepage-fhac
Summary:        Little style to create a standard titlepage for diploma thesis
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(figbib.sty)
Requires:       tex(gloss.sty)
Provides:       tex(fhACtitlepage.sty) = %{tl_version}
Provides:       tex(figbib_add.sty) = %{tl_version}
Provides:       tex(gloss_add.sty) = %{tl_version}

%description -n texlive-thesis-titlepage-fhac
Yet another thesis titlepage style: support of Fachhochschule Aachen (Standort
Juelich)

%package -n texlive-thuaslogos
Summary:        Logos for The Hague University of Applied Sciences (THUAS)
Version:        svn51347
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgf.sty)
Provides:       tex(thuaslogos.sty) = %{tl_version}

%description -n texlive-thuaslogos
This package contains some logos of The Hague University of Applied Sciences
(THUAS). These Logos are available in English and in Dutch. They are rendered
via PGF.

%package -n texlive-thubeamer
Summary:        A beamer theme for Tsinghua University
Version:        svn61071
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithm.sty)
Requires:       tex(algorithmic.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(calligra.sty)
Requires:       tex(ctex.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(listings.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multimedia.sty)
Requires:       tex(multirow.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(beamercolorthemethubeamer.sty) = %{tl_version}
Provides:       tex(beamerinnerthemethubeamer.sty) = %{tl_version}
Provides:       tex(beamerouterthemethubeamer.sty) = %{tl_version}
Provides:       tex(beamerthemethubeamer.sty) = %{tl_version}

%description -n texlive-thubeamer
This package provides a beamer theme designed for Tsinghua University.

%package -n texlive-thucoursework
Summary:        Coursework template for Tsinghua University
Version:        svn56435
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(iidef.sty) = %{tl_version}

%description -n texlive-thucoursework
A LaTeX package for students of Tsinghua University to write coursework more
efficiently. It can also be used by students from other universities. Note that
the package itself does not import the ctex package; to use it with Chinese
writing, see example file ithw.tex for details.

%package -n texlive-thuthesis
Summary:        Thesis template for Tsinghua University
Version:        svn74775
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(gb7714-2015.bbx)
Requires:       tex(gb7714-2015.cbx)
Requires:       tex(gb7714-2015ay.bbx)
Requires:       tex(gb7714-2015ay.cbx)
Provides:       tex(thuthesis-author-year.bbx) = %{tl_version}
Provides:       tex(thuthesis-author-year.cbx) = %{tl_version}
Provides:       tex(thuthesis-bachelor.bbx) = %{tl_version}
Provides:       tex(thuthesis-bachelor.cbx) = %{tl_version}
Provides:       tex(thuthesis-inline.cbx) = %{tl_version}
Provides:       tex(thuthesis-numeric.bbx) = %{tl_version}
Provides:       tex(thuthesis-numeric.cbx) = %{tl_version}

%description -n texlive-thuthesis
This package establishes a simple and easy-to-use LaTeX template for Tsinghua
dissertations, including general undergraduate research papers, masters theses,
doctoral dissertations, and postdoctoral reports.

%package -n texlive-tidyres
Summary:        Create formal resumes easily
Version:        svn67738
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(expkv-cs.sty)
Requires:       tex(expkv-def.sty)
Requires:       tex(fontawesome.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(minted.sty)
Requires:       tex(paracol.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(tidyres.sty) = %{tl_version}

%description -n texlive-tidyres
This LaTeX package aims to provide users with a simple interface to create
multi-column formal resumes.

%package -n texlive-tiet-question-paper
Summary:        A LaTeX question paper class for the TIET
Version:        svn71601
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tiet-question-paper
This package provides a LaTeX document class tiet-question-paper.cls in order
to create question papers for the Thapar Institute of Engineering and
Technologie (TIET). Although created for the TIET, the module is easily
adaptable to any organisation.

%package -n texlive-timbreicmc
Summary:        Typeset documents with ICMC/USP watermarks
Version:        svn49740
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xwatermark.sty)
Provides:       tex(timbreicmc.sty) = %{tl_version}

%description -n texlive-timbreicmc
With this package you can typeset documents with ICMC/USP Sao Carlos
watermarks. ICMC is acronym for "Instituto de Ciencias Matematicas e de
Computacao" of the "Universidade de Sao Paulo" (USP), in the city of Sao
Carlos-SP, Brazil.

%package -n texlive-tlc-article
Summary:        A LaTeX document class for formal documents
Version:        svn51431
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tlc-article
The package provides a LaTeX document class that orchestrates a logical
arrangement for document header, footer, author, abstract, table of contents,
and margins. It standardizes a document layout intended for formal documents.
The tlc_article GitHub repository uses a SCRUM framework adapted to standard
GitHub tooling. tlc_article is integrated with Travis-ci.org for continuous
integration and AllanConsulting.slack.com for centralized notification.

%package -n texlive-topletter
Summary:        Letter class for the Politecnico di Torino
Version:        svn48182
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-topletter
This package provides a LaTeX class for typesetting letters conforming to the
official Corporate Image guidelines for the Politecnico di Torino. The class
can be used for letters written in Italian and in English.

%package -n texlive-toptesi
Summary:        Bundle for typesetting multilanguage theses
Version:        svn73464
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(float.sty)
Requires:       tex(frontespizio.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(lscape.sty)
Requires:       tex(multirow.sty)
Requires:       tex(nomencl.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(setspace.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Provides:       tex(topcoman.sty) = %{tl_version}
Provides:       tex(topfront.sty) = %{tl_version}
Provides:       tex(toptesi-dottorale.sty) = %{tl_version}
Provides:       tex(toptesi-magistrale.sty) = %{tl_version}
Provides:       tex(toptesi-monografia.sty) = %{tl_version}
Provides:       tex(toptesi-scudo.sty) = %{tl_version}
Provides:       tex(toptesi-sss.sty) = %{tl_version}
Provides:       tex(toptesi.sty) = %{tl_version}

%description -n texlive-toptesi
This bundle contains everything needed for typesetting a bachelor, master, or
PhD thesis in Italian (or in any other language supported by LaTeX: the bundle
is constructed to support multilingual use). The infix strings may be selected
and specified at will by means of a configuration file, so as to customize the
layout of the front page to the requirements of a specific university. Thanks
to its language management, the bundle is suited for multilanguage theses that
are becoming more and more frequent thanks to the double degree programs of the
European Community Socrates programs. Toptesi is designed to save the PDF
version of a thesis in PDF/A-1b compliant mode and with all the necessary
metadata.

%package -n texlive-tuda-ci
Summary:        LaTeX templates of Technische Universitat Darmstadt
Version:        svn76863
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(XCharter.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(luainputenc.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(roboto-mono.sty)
Requires:       tex(roboto.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(trimclip.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(beamercolorthemeTUDa.sty) = %{tl_version}
Provides:       tex(beamercolorthemeTUDa2008.sty) = %{tl_version}
Provides:       tex(beamerfontthemeTUDa.sty) = %{tl_version}
Provides:       tex(beamerfontthemeTUDa2008.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeTUDa.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeTUDa2008.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeTUDa2023.sty) = %{tl_version}
Provides:       tex(beamerouterthemeTUDa.sty) = %{tl_version}
Provides:       tex(beamerouterthemeTUDa2008.sty) = %{tl_version}
Provides:       tex(beamerthemeTUDa-mecheng.sty) = %{tl_version}
Provides:       tex(beamerthemeTUDa.sty) = %{tl_version}
Provides:       tex(beamerthemeTUDa2008.sty) = %{tl_version}
Provides:       tex(beamerthemeTUDa2023.sty) = %{tl_version}
Provides:       tex(tuda-pgfplots.sty) = %{tl_version}
Provides:       tex(tudacolors.def) = %{tl_version}
Provides:       tex(tudacolors.sty) = %{tl_version}
Provides:       tex(tudafonts.sty) = %{tl_version}
Provides:       tex(tudarules.sty) = %{tl_version}

%description -n texlive-tuda-ci
The TUDa-CI-Bundle provides a possibility to use the Corporate Design of TU
Darmstadt in LaTeX. It contains documentclasses as well as some helper packages
and config files together with some templates for user documentation, which
currently are only available in German.

%package -n texlive-tudscr
Summary:        Corporate Design of Technische Universitat Dresden
Version:        svn64085
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cbfonts
Requires:       texlive-environ
Requires:       texlive-etoolbox
Requires:       texlive-geometry
Requires:       texlive-graphics
Requires:       texlive-greek-inputenc
Requires:       texlive-iwona
Requires:       texlive-koma-script
Requires:       texlive-mathastext
Requires:       texlive-mweights
Requires:       texlive-oberdiek
Requires:       texlive-opensans
Requires:       texlive-trimspaces
Requires:       texlive-xcolor
Requires:       texlive-xpatch
Requires:       tex(auto-pst-pdf.sty)
Requires:       tex(babel.sty)
Requires:       tex(bm.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(calc.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(filemod.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyphsubst.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(iftex.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(isodate.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(listings.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(mathastext.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(quoting.sty)
Requires:       tex(scrbase.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(scrhack.sty)
Requires:       tex(scrlfile.sty)
Requires:       tex(scrwfile.sty)
Requires:       tex(setspace.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(url.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xspace.sty)
Provides:       tex(fix-tudscrfonts.sty) = %{tl_version}
Provides:       tex(mathswap.sty) = %{tl_version}
Provides:       tex(tudscr-gitinfo.sty) = %{tl_version}
Provides:       tex(tudscrbase.sty) = %{tl_version}
Provides:       tex(tudscrcolor.sty) = %{tl_version}
Provides:       tex(tudscrcomp.sty) = %{tl_version}
Provides:       tex(tudscrfonts.sty) = %{tl_version}
Provides:       tex(tudscrmanual.sty) = %{tl_version}
Provides:       tex(tudscrsupervisor.sty) = %{tl_version}
Provides:       tex(twocolfix.sty) = %{tl_version}

%description -n texlive-tudscr
The TUD-Script bundle provides both classes and packages in order to create
LaTeX documents in the corporate design of the Technische Universitat Dresden.
It bases on the KOMA-Script bundle, which must necessarily be present. For
questions, problems and comments, please refer to either the LaTeX forum of the
Dresden University of Technology or the GitHub "tudscr" repository. The bundle
offers: the three document classes tudscrartcl, tudscrreprt, and tudscrbook
which serve as wrapper classes for scrartcl, scrreprt, and scrbook, the class
tudscrposter for creating posters, the package tudscrsupervisor providing
environments and macros to create tasks, evaluations and notices for scientific
theses, the package tudscrfonts, which makes the corporate design fonts of the
Technische Universitat Dresden available for LaTeX standard classes and
KOMA-Script classes, the package fix-tudscrfonts, which provides the same fonts
to additional corporate design classes not related to TUD-Script, the package
tudscrcomp, which simplifies the switch to TUD-Script from external corporate
design classes, the package mathswap for swapping math delimiters within
numbers (similar to ionumbers), the package twocolfix for fixing the
positioning bug of headings in twocolumn layout, and a comprehensive user
documentation as well as several tutorials.

%package -n texlive-tugboat
Summary:        LaTeX macros for TUGboat articles
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(mflogo.sty)
Provides:       tex(ltugboat.sty) = %{tl_version}
Provides:       tex(ltugcomn.sty) = %{tl_version}
Provides:       tex(ltugproc.sty) = %{tl_version}

%description -n texlive-tugboat
Provides ltugboat.cls for both regular and proceedings issues of the TUGboat
journal. Also provides a BibTeX style, tugboat.bst.

%package -n texlive-tugboat-plain
Summary:        Plain TeX macros for TUGboat
Version:        svn75521
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tugboat.sty) = %{tl_version}
Provides:       tex(tugproc.sty) = %{tl_version}

%description -n texlive-tugboat-plain
The macros defined in this directory (in files tugboat.sty and tugboat.cmn) are
used in papers written in Plain TeX for publication in TUGboat.

%package -n texlive-tui
Summary:        Thesis style for the University of the Andes, Colombia
Version:        svn27253
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tui
Doctoral Dissertations from the Faculty of Engineering at the Universidad de
los Andes, Bogota, Colombia. The class is implemented as an extension of the
memoir class. Clase de Tesis doctorales para ingenieria, Universidad de los
Andes, Bogota.

%package -n texlive-turabian
Summary:        Create Turabian-formatted material using LaTeX
Version:        svn36298
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-turabian
The bundle provides a class file and a template for creating Turabian-formatted
projects. The class file supports citation formatting conforming to the
Turabian 8th Edition style guide.

%package -n texlive-uaclasses
Summary:        University of Arizona thesis and dissertation format
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(my-title.sty) = %{tl_version}
Provides:       tex(ua-title.sty) = %{tl_version}

%description -n texlive-uaclasses
This package provides a LaTeX2e document class named 'ua-thesis' for
typesetting theses and dissertations in the official format required by the
University of Arizona. Moreover, there is a fully compatible alternative
document class 'my-thesis' for private 'nice' copies of the dissertation, and
the respective title pages are available as separate packages to work with any
document class.

%package -n texlive-uafthesis
Summary:        Document class for theses at University of Alaska Fairbanks
Version:        svn57349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uafthesis
This is an "unofficial" official class.

%package -n texlive-ualberta
Summary:        A LaTeX template for the University of Alberta
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ualberta
This package provides a comprehensive template designed to meet the formatting
requirements of the University of Alberta (
https://www.ualberta.ca/en/graduate-studies/resources/graduate-
students/thesis-preparation-requirements-deadlines/index.html) for MSc and PhD
theses. It provides a structured and customizable framework that ensures
compliance with university guidelines while allowing flexibility in document
formatting.

%package -n texlive-uantwerpendocs
Summary:        Course texts, master theses, and exams in University of Antwerp style
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(bm.sty)
Requires:       tex(cmbright.sty)
Requires:       tex(environ.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(sansmathaccent.sty)
Requires:       tex(tikz.sty)
Provides:       tex(beamercolorthemeuantwerpen.sty) = %{tl_version}
Provides:       tex(beamerfontthemeuantwerpen.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeuantwerpen.sty) = %{tl_version}
Provides:       tex(beamerouterthemeuantwerpen.sty) = %{tl_version}
Provides:       tex(beamerthemeuantwerpen.sty) = %{tl_version}
Provides:       tex(uantwerpencolorlogoscheme.sty) = %{tl_version}

%description -n texlive-uantwerpendocs
These class files implement the house style of the University of Antwerp. This
package originated from the Faculty of Applied Engineering. Using these class
files will make it easy for you to make and keep your documents compliant to
this version and future versions of the house style of the University of
Antwerp.

%package -n texlive-ucalgmthesis
Summary:        LaTeX thesis class for University of Calgary Faculty of Graduate Studies
Version:        svn66602
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ucalgmthesis
ucalgmthesis.cls is a LaTeX class file that produces documents according to the
thesis guidelines of the University of Calgary Faculty of Graduate Studies. It
uses the memoir class, which provides very powerful and flexible mechanisms for
book design and layout. All memoir commands for changing chapter and section
headings, page layout, fancy foot- and endnotes, typesetting poems, etc., can
be used. (Memoir is meant as a replacement for the standard LaTeX classes, so
all standard LaTeX commands such as \chapter, \section, etc., still work.)
Likewise, any of memoir's class options can be passed as options to
ucalgmthesis, in particular 12pt to select 12 point type (11 point is the
default).

%package -n texlive-ucbthesis
Summary:        Thesis and dissertation class supporting UCB requirements
Version:        svn51690
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ucbthesis
The class provides the necessary framework for electronic submission of Masters
theses and Ph.D. dissertations at the University of California, Berkeley. It is
based on the memoir class.

%package -n texlive-ucdavisthesis
Summary:        A thesis/dissertation class for University of California at Davis
Version:        svn40772
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ucdavisthesis
The ucdavisthesis class is a LaTeX class that allows you to create a
dissertation or thesis conforming to UC Davis formatting requirements as of
April 2016.

%package -n texlive-ucph-revy
Summary:        Musical script formatting
Version:        svn74857
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ucph-revy
This package provides a class for typesetting scripts containing both lyrics
and prose, in the style used by the student revues (revy) at the Faculties of
Science at the University of Copenhagen (uchp).

%package -n texlive-ucsmonograph
Summary:        Typesetting academic documents from the University of Caxias do Sul
Version:        svn52698
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ucsmonograph
This is a LaTeX class for typesetting academic documents according to the ABNT
(Brazilian Technical Standards Association) standards and the UCS (University
of Caxias do Sul) specifications.

%package -n texlive-ucthesis
Summary:        University of California thesis format
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ucthesis
A modified version of the standard LaTeX report style that is accepted for use
with University of California PhD dissertations and Masters theses. A sample
dissertation source and bibliography are provided.

%package -n texlive-udepcolor
Summary:        University of Piura (UDEP) institutional and corporate colors for digital and electronic media
Version:        svn69701
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Provides:       tex(udepcolor.sty) = %{tl_version}

%description -n texlive-udepcolor
This package defines University of Piura (UDEP) institutional and corporate
colors for digital and electronic media according to brand and style guidelines
published by UDEP DIRCOM. The colors have been selected and implemented using
the xcolor package and following the brand and visual identity guidelines of
the University of Piura.

%package -n texlive-udes-genie-these
Summary:        A thesis class file for the Faculte de genie at the Universite de Sherbrooke
Version:        svn68141
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-udes-genie-these
The udes-genie-these class can be used for Ph.D. theses, master's theses and
project definitions at the Faculte de genie of the Universite de Sherbrooke
(Quebec, Canada). The class file is coherent with the latest version of the
Protocole de redaction aux etudes superieures which is available on the
faculte's intranet. The class file documentation is in French, the language of
the typical user at the Universite de Sherbrooke. An example of use is also
distributed with the documentation.

%package -n texlive-udiss
Summary:        A LaTeX bundle for typesetting dissertations
Version:        svn75301
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-udiss
The udiss bundle is a LaTeX-class-file developed to assist students in
typesetting their university dissertations. It is a collection of multiple
support files. Universities often have strict requirements regarding the
formatting of the dissertations/theses submitted to them. This bundle
pre-supplies a generic style (university-agnostic) for creating dissertations.
It also supports custom layouts required for different universities.

%package -n texlive-uestcthesis
Summary:        Thesis class for UESTC
Version:        svn36371
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uestcthesis
The class is for typesetting a thesis at the University of Electronic Science
and Technology of China.

%package -n texlive-ufrgscca
Summary:        A bundle for undergraduate students final work/report (tcc) at UFRGS/EE
Version:        svn77050
License:        LPPL-1.3c OR AGPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(appendix.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(caption.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(codedescribe.sty)
Requires:       tex(contour.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(geometry.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multirow.sty)
Requires:       tex(newfloat.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(pdfcomment.sty)
Requires:       tex(pgfcalendar.sty)
Requires:       tex(showframe.sty)
Requires:       tex(showlabels.sty)
Requires:       tex(soul.sty)
Requires:       tex(starray.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(ufrgscca-abnt.sty) = %{tl_version}
Provides:       tex(ufrgscca-base-en.def) = %{tl_version}
Provides:       tex(ufrgscca-base-ptBR.def) = %{tl_version}
Provides:       tex(ufrgscca-coord.sty) = %{tl_version}
Provides:       tex(ufrgscca-core.sty) = %{tl_version}
Provides:       tex(ufrgscca-cover.sty) = %{tl_version}
Provides:       tex(ufrgscca-curr.sty) = %{tl_version}
Provides:       tex(ufrgscca-forms.sty) = %{tl_version}
Provides:       tex(ufrgscca-lists.sty) = %{tl_version}
Provides:       tex(ufrgscca-ppc.sty) = %{tl_version}

%description -n texlive-ufrgscca
This bundle is aimed at producing undergraduate students' final work/report at
UFRGS/EE (Engineering School at the Federal University of Rio Grande do Sul),
closely following ABNT rules (Brazilian Association for Technical Norms). It is
composed of a main class, ufrgscca, and a set of auxiliary packages, some of
which can be used independently.

%package -n texlive-uhhassignment
Summary:        A document class for typesetting homework assignments
Version:        svn44026
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uhhassignment
This document class was created for typesetting solutions to homework
assignments at the university of Hamburg (Universitat Hamburg).

%package -n texlive-uiucredborder
Summary:        Class for UIUC thesis red-bordered forms
Version:        svn29974
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uiucredborder
The class offers a means of filling out the "red-bordered form" that gets
signed by the department head, your advisor, and -- for doctoral dissertations
-- your thesis committee members.

%package -n texlive-uiucthesis
Summary:        UIUC thesis class
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(setspace.sty)
Provides:       tex(uiucthesis.sty) = %{tl_version}

%description -n texlive-uiucthesis
The class produces a document that conforms to the format described in the
University's Handbook for Graduate Students Preparing to Deposit.

%package -n texlive-ukbill
Summary:        A class for typesetting UK legislation
Version:        svn69362
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ukbill
This package provides formatting to easily typeset draft UK legislation. The
libre font Palatine Parliamentary is required to use this package.

%package -n texlive-ulthese
Summary:        Thesis class and templates for Universite Laval
Version:        svn77089
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ulthese
The package provides a class based on memoir to prepare theses and memoirs
compliant with the presentation rules set forth by the Faculty of Graduate
Studies of Universite Laval, Quebec, Canada. The class also comes with an
extensive set of templates for the various types of theses and memoirs offered
at Laval. Please note that the documentation for the class and the comments in
the templates are all written in French, the language of the target audience.

%package -n texlive-umbclegislation
Summary:        A LaTeX class for building legislation files for UMBC Student Government Association Bills
Version:        svn41348
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-umbclegislation
LaTeX class for building legislation files for UMBC Student Government
Association Bills. Requires pdflatex and the mdframed enumitem, lineno, and
xifthen packages.

%package -n texlive-umich-thesis
Summary:        University of Michigan Thesis LaTeX class
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-umich-thesis
A LaTeX2e class to create a University of Michigan dissertation according to
the Rackham dissertation handbook.

%package -n texlive-umthesis
Summary:        Dissertations at the University of Michigan
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-umthesis
The class loads book class, and makes minimal changes to it; its coding aims to
be as robust as possible, and as a result it has few conflicts with potential
add-on packages.

%package -n texlive-unam-thesis
Summary:        Create documents according to the UNAM guidelines
Version:        svn51207
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unam-thesis
This is a class for creating dissertation documents according to the National
Autonomous University of Mexico (UNAM) guidelines.

%package -n texlive-unamth-template
Summary:        UNAM Thesis LaTeX Template
Version:        svn76790
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-unamth-template-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-unamth-template-doc <= 11:%{version}

%description -n texlive-unamth-template
The bundle provides a template for UNAM's College of Engineering Theses. The
work is based on Harish Bhanderi's PhD/MPhil template, then University of
Cambridge.

%package -n texlive-unamthesis
Summary:        Style for Universidad Nacional Autonoma de Mexico theses
Version:        svn43639
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(setspace.sty)
Provides:       tex(UNAMThesis.sty) = %{tl_version}

%description -n texlive-unamthesis
The package provides a customisable format to typeset Theses according to the
Universidad Nacional Autonoma de Mexico guidelines. Support for use in
Scientific Workplace (SWP) 3.x is also provided. The bundle also includes an
appropriate bibliographic style which enables the use of author-year schemes
using the natbib package.

%package -n texlive-unbtex
Summary:        A class for theses at University of Brasilia (UnB)
Version:        svn76237
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unbtex
This package provides a class based on abnTeX and compatible with pdflatex and
BibTeXr to prepare bachelor, master, and doctoral theses for the University of
Brasilia (UnB), Brazil. The class also comes with a template for the various
types of theses for undergraduate and graduate programs at UnB. The
documentation for the class and the comments in the templates are all written
in Portuguese, the language of the target audience.

%package -n texlive-unifith
Summary:        Typeset theses for University of Florence (Italy)
Version:        svn60698
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unifith
The package provides a class to typeset Ph.D., Master, and Bachelor theses that
adhere to the publishing guidelines of the University of Florence (Italy).

%package -n texlive-unigrazpub
Summary:        LaTeX templates for University of Graz Library Publishing Services
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unigrazpub
This package provides a LaTeX class matching the preparation guidelines of the
Library Publishing Services of University of Graz. The bundle also includes a
comprehensive set of example files for books and collections.

%package -n texlive-unitn-bimrep
Summary:        A bimonthly report class for the PhD School of Materials, Mechatronics and System Engineering
Version:        svn45581
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unitn-bimrep
This package allows to rapidly write the bimonthly report for The Ph.D. School
in Materials, Mechatronics and System Engineering. It allows to define the
research activities, the participation to school and congress, and the
publication performed by a student.

%package -n texlive-univie-ling
Summary:        Papers, theses and research proposals in (Applied) Linguistics at Vienna University
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Provides:       tex(univie-ling.bbx) = %{tl_version}
Provides:       tex(univie-ling.cbx) = %{tl_version}

%description -n texlive-univie-ling
This bundle provides LaTeX2e classes, BibLaTeX files, and templates suitable
for student papers, PhD research proposals (Exposes), and theses in (Applied)
Linguistics at the University of Vienna. The classes implement some standards
for these types of text, such as suitable title pages. They are particularly
suited for the field of (Applied) Linguistics and pre-load some packages that
are considered useful in this context. The classes can also be used for General
and Historical Linguistics as well as for other fields of study at Vienna
University. In this case, however, some settings may have to be adjusted.

%package -n texlive-unizgklasa
Summary:        A LaTeX class for theses at the Faculty Of Graphic Arts in Zagreb
Version:        svn51647
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unizgklasa
This class is intended for generating graduate and final theses according to
the instructions of the Faculty of Graphic Arts, University of Zagreb. It does
not necessarily correspond to the requirements of each component of the
University, but is designed as an idea for linking and uniformizing the look of
all graduate papers. Anyone who likes it is welcome to use it.

%package -n texlive-unswcover
Summary:        Typeset a dissertation cover page following UNSW guidelines
Version:        svn66115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(pdfpages.sty)
Provides:       tex(unswcover.sty) = %{tl_version}

%description -n texlive-unswcover
The package an UNSW cover sheet following the 2011 GRS guidelines. It may also
(optionally) provide other required sheets such as Originality, Copyright and
Authenticity statements.

%package -n texlive-uol-physics-report
Summary:        A LaTeX document class for writing lab reports
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uol-physics-report
The package provides physics students at the University of Oldenburg with a
prepared document class for writing laboratory reports for the laboratory
courses conducted by the Institute of Physics. The document class consists of
predefined margins and heading formats. Furthermore, it presets the headers of
the pages and excludes the titlepage and table of contents from the page
numbering.

%package -n texlive-uothesis
Summary:        Class for dissertations and theses at the University of Oregon
Version:        svn25355
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uothesis
The class generates documents that are suitable for submission to the Graduate
School and conform with the style requirements for dissertations and theses as
laid out in the Fall 2010 UO graduate school student manual.

%package -n texlive-uowthesis
Summary:        Document class for dissertations at the University of Wollongong
Version:        svn19700
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uowthesis
A document class for higher degree research theses in compliance with the
specifications of University of Wollongong (UoW) theses in the "Guidelines for
Preparation and Submission of Higher Degree Research Theses" (March 2006), by
the Research Student Centre, Research & Innovation Division, UoW.

%package -n texlive-uowthesistitlepage
Summary:        Title page for dissertations at the University of Wollongong
Version:        svn54512
License:        LPPL-1.3c AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(setspace.sty)
Provides:       tex(uowthesistitlepage.sty) = %{tl_version}

%description -n texlive-uowthesistitlepage
The package redefines \maketitle to generate a title page for a University of
Wollongong thesis, in accordance with the UoW branding guidelines. The package
should be used with the book class to typeset a thesis. The package also
defines a \declaration command that typesets the declaration that this thesis
is your own work, etc., which is required in the front of each PhD Thesis.

%package -n texlive-urcls
Summary:        Beamer and scrlttr2 classes and styles for the University of Regensburg
Version:        svn49903
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(textcase.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(URcolors.sty) = %{tl_version}
Provides:       tex(URoptions.sty) = %{tl_version}
Provides:       tex(URpagestyles.sty) = %{tl_version}
Provides:       tex(URrules.sty) = %{tl_version}
Provides:       tex(URspecialopts.sty) = %{tl_version}
Provides:       tex(beamercolorthemeUR.sty) = %{tl_version}
Provides:       tex(beamerfontthemeUR.sty) = %{tl_version}
Provides:       tex(beamerouterthemeUR.sty) = %{tl_version}
Provides:       tex(beamerthemeUR.sty) = %{tl_version}

%description -n texlive-urcls
The bundle provides a beamer-derived class and a theme style file for the
corporate design of the University of Regensburg. It also contains a
scrlttr2-derived class for letters using the corporate design of the UR. Users
may use the class itself (URbeamer) or use the theme in the usual way with
\usetheme{UR}. Examples of using both letters and presentations are provided as
.tex and .pdf-files.

%package -n texlive-uspatent
Summary:        U.S. Patent Application Tools for LaTeX and LyX
Version:        svn27744
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uspatent
The package provides a class and other tools for developing a beautifully
formatted, consistent U.S. Patent Application using LaTeX and/or LyX.

%package -n texlive-ut-thesis
Summary:        University of Toronto thesis style
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ut-thesis
This LaTeX document class implements the formatting requirements of the
University of Toronto School of Graduate Studies (SGS), as of Fall 2020 (
https://www.sgs.utoronto.ca/academic-progress/program-completio n/formatting).
For example usage, see the GitHub repository.

%package -n texlive-utexasthesis
Summary:        University of Texas at Austin graduate thesis style
Version:        svn48648
License:        CC0-1.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-utexasthesis
This class file complies with the Digital Submission Requirement for Masters
and Ph.D. thesis submissions of the University of Texas at Austin.

%package -n texlive-uvaletter
Summary:        Unofficial letterhead template for the University of Amsterdam
Version:        svn66712
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(microtype.sty)
Requires:       tex(setspace.sty)
Requires:       tex(soul.sty)
Requires:       tex(times.sty)
Provides:       tex(uvaletter.sty) = %{tl_version}

%description -n texlive-uvaletter
This is an unofficial LaTeX package that provides a letterhead template for the
University of Amsterdam. The design mimics the official Word template of the
University and complies with the University's house style.

%package -n texlive-uwa-colours
Summary:        The colour palette of The University of Western Australia
Version:        svn60443
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Provides:       tex(uwa-colours.sty) = %{tl_version}

%description -n texlive-uwa-colours
This package uses the xcolor package to define macros for the colour palette of
The University of Western Australia.

%package -n texlive-uwa-letterhead
Summary:        The letterhead of the University of Western Australia
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(microtype.sty)
Requires:       tex(sourcecodepro.sty)
Requires:       tex(sourcesanspro.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(textpos.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(uwa-letterhead.sty) = %{tl_version}

%description -n texlive-uwa-letterhead
This package generates the letterhead of the University of Western Australia.
It requires the UWA logo in PDF format, which is available in SVG format at
https://static-listing.weboffice.uwa.edu.au/visualid/core-rebra
nd/img/uwacrest/, and uses the Arial and UWA Slab fonts by default. The package
works with XeLaTeX and LuaLaTeX.

%package -n texlive-uwa-pcf
Summary:        A Participant Consent Form (PCF) for a human research protocol at the University of Western Australia
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uwa-pcf
This LaTeX class generates a Participant Consent Form (PCF) for a human
research protocol at the University of Western Australia. It requires the UWA
logo in PDF format, which is available in SVG format at
https://static-listing.weboffice.uwa.edu.au/visualid/core-rebra
nd/img/uwacrest/, and uses the Arial and UWA Slab fonts by default. The class
works with XeLaTeX and LuaLaTeX. It depends on the uwa-letterhead package.

%package -n texlive-uwa-pif
Summary:        A Participant Information Form (PIF) for a human research protocol at the University of Western Australia
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uwa-pif
This package generates a Participant Information Form (PIF) for a human
research protocol at the University of Western Australia. It requires the UWA
logo in PDF format, which is available in SVG format at
https://static-listing.weboffice.uwa.edu.au/visualid/core-rebra
nd/img/uwacrest/, and uses the Calibri fonts by default. The class works with
XeLaTeX and LuaLaTeX. It depends on the uwa-letterhead package.

%package -n texlive-uwthesis
Summary:        University of Washington thesis class
Version:        svn15878
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uwthesis
University of Washington thesis class

%package -n texlive-vancouver
Summary:        Bibliographic style file for Biomedical Journals
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-vancouver
This BibTeX style file is generated with the docstrip utility and modified
manually to meet the Uniform Requirements for Manuscripts Submitted to
Biomedical Journals as published in N Engl J Med 1997;336:309-315 (also known
as the Vancouver style). The complete set of requirements may be viewed on the
ICMJE web site.

%package -n texlive-wsemclassic
Summary:        LaTeX class for Bavarian school w-seminar papers
Version:        svn31532
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-wsemclassic
The class is designed either to conform with the recommendations of the
Bavarian Kultusministerium for typesetting w-seminar papers (strict mode), or
to use another style which should look better. The class is based on the LaTeX
standard report class.

%package -n texlive-xduthesis
Summary:        XeLaTeX template for writing Xidian University Thesis
Version:        svn63116
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xduthesis
This is a XeLaTeX template for writing theses to apply academic degrees in
Xidian University. The template is designed according to the official
requirements on typesetting theses. The template currently supports all levels
of degrees from bachelor to doctor, including both academic master and
professional master. But it is not guaranteed that you will pass the
typesetting check and obtain your degree by using this template.

%package -n texlive-xduts
Summary:        Xidian University TeX Suite
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xdufont.sty) = %{tl_version}

%description -n texlive-xduts
XDUTS is designed to help Xidian University students use LaTeX typesetting
efficiently. XDUTS contains a font configuration package that meets the
school's requirements and can be applied to any document class. In addition,
there are thesis and thesis proposal templates for both undergraduate and
postgraduate that meet the school's requirements.

%package -n texlive-xmuthesis
Summary:        XMU thesis style
Version:        svn56614
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(xmulogo.sty) = %{tl_version}

%description -n texlive-xmuthesis
This class is designed for XMU thesis's writing.

%package -n texlive-yathesis
Summary:        A LaTeX class for writing a thesis following French rules
Version:        svn70511
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(letltxmacro.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Requires:       tex(zref.sty)
Provides:       tex(yathesis-demo.sty) = %{tl_version}
Provides:       tex(yathesis-translations.tex) = %{tl_version}

%description -n texlive-yathesis
The purpose of yathesis is to facilitate the typesetting of theses prepared in
France, whatever the disciplines and institutes. It implements most notably
recommendations from the Ministry of Higher Education and Research, and this
transparently to the user. It has also been designed to (optionally) take
advantage of powerful tools available in LaTeX, including packages: BibLaTeX
for the bibliography; glossaries for the glossary, list of acronyms and symbols
list. The yathesis class, based on the book class, aims to be both simple to
use and, to some extent, (easily) customizable. yathesis comes with templates
and samples in the doc/latex/yathesis/french/exemples/ directory in the
distribution. They can also be tested on ShareLaTeX (template and specimen) and
on Overleaf (template and specimen). Note: The "ya" in the package name stands
for "yet another".

%package -n texlive-yazd-thesis
Summary:        A template for the Yazd University
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-yazd-thesis
This package offers a document class for typesetting theses and dissertations
at the Yazd University. The class requires use of XeLaTeX.

%package -n texlive-yb-book
Summary:        Template for YB Branded Books
Version:        svn74649
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-anyfontsize
Requires:       texlive-biblatex
Requires:       texlive-bigfoot
Requires:       texlive-changepage
Requires:       texlive-chngcntr
Requires:       texlive-collection-fontsextra
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-csquotes
Requires:       texlive-cyrillic
Requires:       texlive-doi
Requires:       texlive-enumitem
Requires:       texlive-fancyhdr
Requires:       texlive-float
Requires:       texlive-footmisc
Requires:       texlive-geometry
Requires:       texlive-href-ul
Requires:       texlive-hypdoc
Requires:       texlive-ifmtarg
Requires:       texlive-imakeidx
Requires:       texlive-lastpage
Requires:       texlive-lh
Requires:       texlive-libertine
Requires:       texlive-mdframed
Requires:       texlive-microtype
Requires:       texlive-needspace
Requires:       texlive-paralist
Requires:       texlive-pgf
Requires:       texlive-pgfopts
Requires:       texlive-qrcode
Requires:       texlive-setspace
Requires:       texlive-soul
Requires:       texlive-textpos
Requires:       texlive-titlesec
Requires:       texlive-titlesec
Requires:       texlive-ulem
Requires:       texlive-wrapfig
Requires:       texlive-wrapfig
Requires:       texlive-xcolor
Requires:       texlive-xifthen
Requires:       texlive-xkeyval
Requires:       texlive-zref

%description -n texlive-yb-book
This template helps the author design books published on Amazon under the
"Y.B." brand. You are welcome to use it too for your own books.

%package -n texlive-york-thesis
Summary:        A thesis class file for York University, Toronto
Version:        svn23348
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-york-thesis
York Graduate Studies has again changed the requirements for theses and
dissertations. The established york-thesis class file now implements the
changes made in Spring 2005.


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
tar -xf %{SOURCE589} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE590} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE591} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE592} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE593} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE594} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE595} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE596} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE597} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE598} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE599} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE600} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE601} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE602} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE603} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE604} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE605} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE606} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE607} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE608} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE609} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE610} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE611} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE612} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE613} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE614} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE615} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE616} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE617} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE618} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE619} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE620} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE621} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE622} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE623} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE624} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE625} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE626} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE627} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE628} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE629} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE630} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Apply proposal patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-proposal-no-workaddress.patch
popd

# Apply scrpage2 obsolete fix patches
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-bgteubner-scrpage2-obsolete-fixes.patch
popd
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-mentis-scrpage2-obsolete-fixes.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-aastex
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/aastex/
%{_texmf_main}/tex/latex/aastex/
%doc %{_texmf_main}/doc/latex/aastex/

%files -n texlive-abnt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/abnt/
%doc %{_texmf_main}/doc/latex/abnt/

%files -n texlive-abntex2
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/abntex2/
%{_texmf_main}/bibtex/bst/abntex2/
%{_texmf_main}/tex/latex/abntex2/
%doc %{_texmf_main}/doc/latex/abntex2/

%files -n texlive-abntexto
%license pd.txt
%{_texmf_main}/tex/latex/abntexto/
%doc %{_texmf_main}/doc/latex/abntexto/

%files -n texlive-abntexto-uece
%license pd.txt
%{_texmf_main}/tex/latex/abntexto-uece/
%doc %{_texmf_main}/doc/latex/abntexto-uece/

%files -n texlive-acmart
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/acmart/
%{_texmf_main}/tex/latex/acmart/
%doc %{_texmf_main}/doc/latex/acmart/

%files -n texlive-acmconf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/acmconf/
%doc %{_texmf_main}/doc/latex/acmconf/

%files -n texlive-active-conf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/active-conf/
%doc %{_texmf_main}/doc/latex/active-conf/

%files -n texlive-adfathesis
%license pd.txt
%{_texmf_main}/bibtex/bst/adfathesis/
%{_texmf_main}/tex/latex/adfathesis/
%doc %{_texmf_main}/doc/latex/adfathesis/

%files -n texlive-aeskwadraat
%license gpl3.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/aeskwadraat/
%doc %{_texmf_main}/doc/latex/aeskwadraat/

%files -n texlive-afthesis
%license pd.txt
%{_texmf_main}/bibtex/bst/afthesis/
%{_texmf_main}/tex/latex/afthesis/
%doc %{_texmf_main}/doc/latex/afthesis/

%files -n texlive-aguplus
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/aguplus/
%{_texmf_main}/tex/latex/aguplus/
%doc %{_texmf_main}/doc/latex/aguplus/

%files -n texlive-aiaa
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/aiaa/
%{_texmf_main}/tex/latex/aiaa/
%doc %{_texmf_main}/doc/latex/aiaa/

%files -n texlive-amnestyreport
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/amnestyreport/
%doc %{_texmf_main}/doc/latex/amnestyreport/

%files -n texlive-anonymous-acm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/anonymous-acm/
%doc %{_texmf_main}/doc/latex/anonymous-acm/

%files -n texlive-anufinalexam
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/anufinalexam/

%files -n texlive-apa
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/apa/
%doc %{_texmf_main}/doc/latex/apa/

%files -n texlive-apa6
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/apa6/
%doc %{_texmf_main}/doc/latex/apa6/

%files -n texlive-apa6e
%license bsd.txt
%{_texmf_main}/tex/latex/apa6e/
%doc %{_texmf_main}/doc/latex/apa6e/

%files -n texlive-apa7
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/apa7/
%doc %{_texmf_main}/doc/latex/apa7/

%files -n texlive-arsclassica
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/arsclassica/
%doc %{_texmf_main}/doc/latex/arsclassica/

%files -n texlive-articleingud
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/articleingud/
%doc %{_texmf_main}/doc/latex/articleingud/

%files -n texlive-asaetr
%license pd.txt
%{_texmf_main}/bibtex/bst/asaetr/
%{_texmf_main}/tex/latex/asaetr/
%doc %{_texmf_main}/doc/latex/asaetr/

%files -n texlive-ascelike
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/ascelike/
%{_texmf_main}/tex/latex/ascelike/
%doc %{_texmf_main}/doc/latex/ascelike/

%files -n texlive-asmeconf
%license mit.txt
%{_texmf_main}/bibtex/bst/asmeconf/
%{_texmf_main}/tex/latex/asmeconf/
%doc %{_texmf_main}/doc/latex/asmeconf/

%files -n texlive-asmejour
%license mit.txt
%{_texmf_main}/bibtex/bst/asmejour/
%{_texmf_main}/tex/latex/asmejour/
%doc %{_texmf_main}/doc/latex/asmejour/

%files -n texlive-aucklandthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/aucklandthesis/
%doc %{_texmf_main}/doc/latex/aucklandthesis/

%files -n texlive-bangorcsthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bangorcsthesis/
%doc %{_texmf_main}/doc/latex/bangorcsthesis/

%files -n texlive-bangorexam
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bangorexam/
%doc %{_texmf_main}/doc/latex/bangorexam/

%files -n texlive-bath-bst
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/bath-bst/
%doc %{_texmf_main}/doc/bibtex/bath-bst/

%files -n texlive-beamer-fuberlin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/beamer-fuberlin/
%doc %{_texmf_main}/doc/latex/beamer-fuberlin/

%files -n texlive-beamer-verona
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/beamer-verona/
%doc %{_texmf_main}/doc/latex/beamer-verona/

%files -n texlive-beilstein
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/beilstein/
%{_texmf_main}/tex/latex/beilstein/
%doc %{_texmf_main}/doc/latex/beilstein/

%files -n texlive-bfh-ci
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bfh-ci/
%doc %{_texmf_main}/doc/latex/bfh-ci/

%files -n texlive-bgteubner
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/bgteubner/
%{_texmf_main}/makeindex/bgteubner/
%{_texmf_main}/tex/latex/bgteubner/
%doc %{_texmf_main}/doc/latex/bgteubner/

%files -n texlive-bjfuthesis
%license gpl3.txt
%{_texmf_main}/tex/latex/bjfuthesis/
%doc %{_texmf_main}/doc/latex/bjfuthesis/

%files -n texlive-bmstu
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bmstu/
%doc %{_texmf_main}/doc/latex/bmstu/

%files -n texlive-bmstu-iu8
%license mit.txt
%{_texmf_main}/tex/latex/bmstu-iu8/
%doc %{_texmf_main}/doc/latex/bmstu-iu8/

%files -n texlive-br-lex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/br-lex/
%doc %{_texmf_main}/doc/latex/br-lex/

%files -n texlive-brandeis-dissertation
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/brandeis-dissertation/
%doc %{_texmf_main}/doc/latex/brandeis-dissertation/

%files -n texlive-brandeis-problemset
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/brandeis-problemset/
%doc %{_texmf_main}/doc/latex/brandeis-problemset/

%files -n texlive-brandeis-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/brandeis-thesis/
%doc %{_texmf_main}/doc/latex/brandeis-thesis/

%files -n texlive-buctthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/buctthesis/
%doc %{_texmf_main}/doc/xelatex/buctthesis/

%files -n texlive-cascadilla
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/cascadilla/
%{_texmf_main}/tex/latex/cascadilla/
%doc %{_texmf_main}/doc/latex/cascadilla/

%files -n texlive-cesenaexam
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cesenaexam/
%doc %{_texmf_main}/doc/latex/cesenaexam/

%files -n texlive-chem-journal
%license gpl2.txt
%{_texmf_main}/bibtex/bst/chem-journal/

%files -n texlive-chifoot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chifoot/
%doc %{_texmf_main}/doc/latex/chifoot/

%files -n texlive-chs-physics-report
%license pd.txt
%license other-free.txt
%{_texmf_main}/tex/latex/chs-physics-report/
%doc %{_texmf_main}/doc/latex/chs-physics-report/

%files -n texlive-cidarticle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cidarticle/
%doc %{_texmf_main}/doc/latex/cidarticle/

%files -n texlive-cje
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/cje/
%{_texmf_main}/tex/latex/cje/
%doc %{_texmf_main}/doc/latex/cje/

%files -n texlive-cjs-rcs-article
%license lppl1.3c.txt
%license cc-by-sa-4.txt
%{_texmf_main}/bibtex/bst/cjs-rcs-article/
%{_texmf_main}/tex/latex/cjs-rcs-article/
%doc %{_texmf_main}/doc/latex/cjs-rcs-article/

%files -n texlive-classicthesis
%license gpl2.txt
%{_texmf_main}/tex/latex/classicthesis/
%doc %{_texmf_main}/doc/latex/classicthesis/

%files -n texlive-cleanthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cleanthesis/
%doc %{_texmf_main}/doc/latex/cleanthesis/

%files -n texlive-cmpj
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/cmpj/
%{_texmf_main}/tex/latex/cmpj/
%doc %{_texmf_main}/doc/latex/cmpj/

%files -n texlive-confproc
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/confproc/
%{_texmf_main}/makeindex/confproc/
%{_texmf_main}/tex/latex/confproc/
%doc %{_texmf_main}/doc/latex/confproc/

%files -n texlive-contract
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/contract/
%doc %{_texmf_main}/doc/latex/contract/

%files -n texlive-cqjtuthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cqjtuthesis/
%doc %{_texmf_main}/doc/latex/cqjtuthesis/

%files -n texlive-cquthesis
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/cquthesis/
%{_texmf_main}/tex/latex/cquthesis/
%doc %{_texmf_main}/doc/latex/cquthesis/

%files -n texlive-dccpaper
%license lppl1.3c.txt
%license cc-by-4.txt
%{_texmf_main}/tex/latex/dccpaper/
%doc %{_texmf_main}/doc/latex/dccpaper/

%files -n texlive-dithesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dithesis/
%doc %{_texmf_main}/doc/latex/dithesis/

%files -n texlive-dlrg-templates
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dlrg-templates/
%doc %{_texmf_main}/doc/latex/dlrg-templates/

%files -n texlive-ebook
%license pd.txt
%{_texmf_main}/tex/latex/ebook/
%doc %{_texmf_main}/doc/latex/ebook/

%files -n texlive-ebsthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ebsthesis/
%doc %{_texmf_main}/doc/latex/ebsthesis/

%files -n texlive-ecothesis
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/ecothesis/

%files -n texlive-edmaths
%license lppl1.3c.txt
%license other-free.txt
%{_texmf_main}/tex/latex/edmaths/
%doc %{_texmf_main}/doc/latex/edmaths/

%files -n texlive-ejpecp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ejpecp/
%doc %{_texmf_main}/doc/latex/ejpecp/

%files -n texlive-ekaia
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ekaia/
%doc %{_texmf_main}/doc/latex/ekaia/

%files -n texlive-elbioimp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/elbioimp/
%doc %{_texmf_main}/doc/latex/elbioimp/

%files -n texlive-els-cas-templates
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/els-cas-templates/
%{_texmf_main}/tex/latex/els-cas-templates/
%doc %{_texmf_main}/doc/latex/els-cas-templates/

%files -n texlive-elsarticle
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/elsarticle/
%{_texmf_main}/tex/latex/elsarticle/
%doc %{_texmf_main}/doc/latex/elsarticle/

%files -n texlive-elteiktdk
%license mit.txt
%{_texmf_main}/tex/latex/elteiktdk/
%doc %{_texmf_main}/doc/latex/elteiktdk/

%files -n texlive-elteikthesis
%license mit.txt
%{_texmf_main}/tex/latex/elteikthesis/
%doc %{_texmf_main}/doc/latex/elteikthesis/

%files -n texlive-emisa
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/emisa/
%doc %{_texmf_main}/doc/latex/emisa/

%files -n texlive-erdc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/erdc/
%doc %{_texmf_main}/doc/latex/erdc/

%files -n texlive-estcpmm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/estcpmm/
%doc %{_texmf_main}/doc/latex/estcpmm/

%files -n texlive-etsvthor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/etsvthor/
%doc %{_texmf_main}/doc/latex/etsvthor/

%files -n texlive-facture-belge-simple-sans-tva
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/facture-belge-simple-sans-tva/
%doc %{_texmf_main}/doc/xelatex/facture-belge-simple-sans-tva/

%files -n texlive-fbithesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fbithesis/
%doc %{_texmf_main}/doc/latex/fbithesis/

%files -n texlive-fcavtex
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/fcavtex/
%{_texmf_main}/tex/latex/fcavtex/
%doc %{_texmf_main}/doc/latex/fcavtex/

%files -n texlive-fcltxdoc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fcltxdoc/
%doc %{_texmf_main}/doc/latex/fcltxdoc/

%files -n texlive-fei
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fei/
%doc %{_texmf_main}/doc/latex/fei/

%files -n texlive-fhj-script
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fhj-script/
%doc %{_texmf_main}/doc/latex/fhj-script/

%files -n texlive-ftc-notebook
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ftc-notebook/
%doc %{_texmf_main}/doc/latex/ftc-notebook/

%files -n texlive-gaceta
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gaceta/
%doc %{_texmf_main}/doc/latex/gaceta/

%files -n texlive-gammas
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/gammas/
%{_texmf_main}/tex/latex/gammas/
%doc %{_texmf_main}/doc/latex/gammas/

%files -n texlive-geradwp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/geradwp/
%doc %{_texmf_main}/doc/latex/geradwp/

%files -n texlive-gfdl
%license gpl3.txt
%license fdl.txt
%{_texmf_main}/tex/latex/gfdl/
%doc %{_texmf_main}/doc/latex/gfdl/

%files -n texlive-gradstudentresume
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gradstudentresume/
%doc %{_texmf_main}/doc/latex/gradstudentresume/

%files -n texlive-grant
%license mit.txt
%{_texmf_main}/tex/latex/grant/
%doc %{_texmf_main}/doc/latex/grant/

%files -n texlive-gsemthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gsemthesis/
%doc %{_texmf_main}/doc/latex/gsemthesis/

%files -n texlive-gzt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gzt/
%doc %{_texmf_main}/doc/latex/gzt/

%files -n texlive-h2020proposal
%license gpl3.txt
%{_texmf_main}/tex/latex/h2020proposal/
%doc %{_texmf_main}/doc/latex/h2020proposal/

%files -n texlive-hagenberg-thesis
%license cc-by-4.txt
%{_texmf_main}/tex/latex/hagenberg-thesis/
%doc %{_texmf_main}/doc/latex/hagenberg-thesis/

%files -n texlive-har2nat
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/har2nat/
%doc %{_texmf_main}/doc/latex/har2nat/

%files -n texlive-hduthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hduthesis/
%doc %{_texmf_main}/doc/latex/hduthesis/

%files -n texlive-hecthese
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hecthese/
%doc %{_texmf_main}/doc/latex/hecthese/

%files -n texlive-hep-paper
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hep-paper/
%doc %{_texmf_main}/doc/latex/hep-paper/

%files -n texlive-heria
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/heria/
%doc %{_texmf_main}/doc/latex/heria/

%files -n texlive-hfutexam
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hfutexam/
%doc %{_texmf_main}/doc/latex/hfutexam/

%files -n texlive-hfutthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/hfutthesis/
%doc %{_texmf_main}/doc/xelatex/hfutthesis/

%files -n texlive-hithesis
%license lppl1.3.txt
%{_texmf_main}/bibtex/bst/hithesis/
%{_texmf_main}/makeindex/hithesis/
%{_texmf_main}/tex/xelatex/hithesis/
%doc %{_texmf_main}/doc/xelatex/hithesis/

%files -n texlive-hitszbeamer
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/hitszbeamer/
%{_texmf_main}/tex/latex/hitszbeamer/
%doc %{_texmf_main}/doc/latex/hitszbeamer/

%files -n texlive-hitszthesis
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/hitszthesis/
%{_texmf_main}/makeindex/hitszthesis/
%{_texmf_main}/tex/latex/hitszthesis/
%doc %{_texmf_main}/doc/latex/hitszthesis/

%files -n texlive-hobete
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hobete/
%doc %{_texmf_main}/doc/latex/hobete/

%files -n texlive-hu-berlin-bundle
%license lppl1.3c.txt
%license gpl2.txt
%license bsd.txt
%{_texmf_main}/tex/lualatex/hu-berlin-bundle/
%doc %{_texmf_main}/doc/lualatex/hu-berlin-bundle/

%files -n texlive-hustthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hustthesis/
%doc %{_texmf_main}/doc/latex/hustthesis/

%files -n texlive-hustvisual
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hustvisual/
%doc %{_texmf_main}/doc/latex/hustvisual/

%files -n texlive-iaria
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/iaria/
%doc %{_texmf_main}/doc/latex/iaria/

%files -n texlive-iaria-lite
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/iaria-lite/
%doc %{_texmf_main}/doc/latex/iaria-lite/

%files -n texlive-icsv
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/icsv/
%doc %{_texmf_main}/doc/latex/icsv/

%files -n texlive-ieeeconf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ieeeconf/
%doc %{_texmf_main}/doc/latex/ieeeconf/

%files -n texlive-ieeepes
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/ieeepes/
%{_texmf_main}/tex/latex/ieeepes/
%doc %{_texmf_main}/doc/latex/ieeepes/

%files -n texlive-ieeetran
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/ieeetran/
%{_texmf_main}/bibtex/bst/ieeetran/
%{_texmf_main}/tex/latex/ieeetran/
%doc %{_texmf_main}/doc/latex/ieeetran/

%files -n texlive-ijmart
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/ijmart/
%{_texmf_main}/tex/latex/ijmart/
%doc %{_texmf_main}/doc/latex/ijmart/

%files -n texlive-ijsra
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ijsra/
%doc %{_texmf_main}/doc/latex/ijsra/

%files -n texlive-imac
%license gpl2.txt
%{_texmf_main}/bibtex/bst/imac/
%{_texmf_main}/tex/latex/imac/
%doc %{_texmf_main}/doc/latex/imac/

%files -n texlive-imtekda
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/imtekda/
%doc %{_texmf_main}/doc/latex/imtekda/

%files -n texlive-inkpaper
%license gpl3.txt
%{_texmf_main}/tex/latex/inkpaper/
%doc %{_texmf_main}/doc/latex/inkpaper/

%files -n texlive-iodhbwm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/iodhbwm/
%doc %{_texmf_main}/doc/latex/iodhbwm/

%files -n texlive-iscram
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/iscram/
%doc %{_texmf_main}/doc/latex/iscram/

%files -n texlive-jacow
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jacow/
%doc %{_texmf_main}/doc/latex/jacow/

%files -n texlive-jmlr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jmlr/
%doc %{_texmf_main}/doc/latex/jmlr/

%files -n texlive-jnuexam
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jnuexam/
%doc %{_texmf_main}/doc/latex/jnuexam/

%files -n texlive-jourcl
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/jourcl/
%doc %{_texmf_main}/doc/latex/jourcl/

%files -n texlive-jourrr
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/jourrr/
%doc %{_texmf_main}/doc/latex/jourrr/

%files -n texlive-jpsj
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jpsj/
%doc %{_texmf_main}/doc/latex/jpsj/

%files -n texlive-jsonresume
%license mit.txt
%{_texmf_main}/tex/lualatex/jsonresume/
%doc %{_texmf_main}/doc/lualatex/jsonresume/

%files -n texlive-jwjournal
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jwjournal/
%doc %{_texmf_main}/doc/latex/jwjournal/

%files -n texlive-kdgdocs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kdgdocs/
%doc %{_texmf_main}/doc/latex/kdgdocs/

%files -n texlive-kdpcover
%license mit.txt
%{_texmf_main}/tex/latex/kdpcover/
%doc %{_texmf_main}/doc/latex/kdpcover/

%files -n texlive-kfupm-math-exam
%license mit.txt
%{_texmf_main}/tex/latex/kfupm-math-exam/
%doc %{_texmf_main}/doc/latex/kfupm-math-exam/

%files -n texlive-kluwer
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/kluwer/
%{_texmf_main}/tex/latex/kluwer/
%doc %{_texmf_main}/doc/latex/kluwer/

%files -n texlive-ksp-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ksp-thesis/
%doc %{_texmf_main}/doc/latex/ksp-thesis/

%files -n texlive-ku-template
%license mit.txt
%{_texmf_main}/tex/latex/ku-template/
%doc %{_texmf_main}/doc/latex/ku-template/

%files -n texlive-langsci
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/langsci/
%doc %{_texmf_main}/doc/xelatex/langsci/

%files -n texlive-langsci-avm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/langsci-avm/
%doc %{_texmf_main}/doc/latex/langsci-avm/

%files -n texlive-limecv
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/limecv/
%doc %{_texmf_main}/doc/latex/limecv/

%files -n texlive-lion-msc
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/lion-msc/
%{_texmf_main}/tex/latex/lion-msc/
%doc %{_texmf_main}/doc/latex/lion-msc/

%files -n texlive-llncs
%license cc-by-4.txt
%{_texmf_main}/bibtex/bst/llncs/
%{_texmf_main}/tex/latex/llncs/
%doc %{_texmf_main}/doc/latex/llncs/

%files -n texlive-llncsconf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/llncsconf/
%doc %{_texmf_main}/doc/latex/llncsconf/

%files -n texlive-lni
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lni/
%doc %{_texmf_main}/doc/latex/lni/

%files -n texlive-lps
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lps/
%doc %{_texmf_main}/doc/latex/lps/

%files -n texlive-maine-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/maine-thesis/
%doc %{_texmf_main}/doc/latex/maine-thesis/

%files -n texlive-matc3
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/matc3/
%doc %{_texmf_main}/doc/latex/matc3/

%files -n texlive-matc3mem
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/matc3mem/
%doc %{_texmf_main}/doc/latex/matc3mem/

%files -n texlive-mcmthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mcmthesis/
%doc %{_texmf_main}/doc/latex/mcmthesis/

%files -n texlive-mentis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mentis/
%doc %{_texmf_main}/doc/latex/mentis/

%files -n texlive-mitthesis
%license mit.txt
%{_texmf_main}/tex/latex/mitthesis/
%doc %{_texmf_main}/doc/latex/mitthesis/

%files -n texlive-mlacls
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mlacls/
%doc %{_texmf_main}/doc/latex/mlacls/

%files -n texlive-mluexercise
%license mit.txt
%{_texmf_main}/tex/latex/mluexercise/
%doc %{_texmf_main}/doc/latex/mluexercise/

%files -n texlive-mnras
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/mnras/
%{_texmf_main}/tex/latex/mnras/
%doc %{_texmf_main}/doc/latex/mnras/

%files -n texlive-modeles-factures-belges-assocs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/modeles-factures-belges-assocs/
%doc %{_texmf_main}/doc/latex/modeles-factures-belges-assocs/

%files -n texlive-modernnewspaper
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/modernnewspaper/
%doc %{_texmf_main}/doc/latex/modernnewspaper/

%files -n texlive-msu-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/msu-thesis/
%doc %{_texmf_main}/doc/latex/msu-thesis/

%files -n texlive-mucproc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mucproc/
%doc %{_texmf_main}/doc/latex/mucproc/

%files -n texlive-mugsthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mugsthesis/
%doc %{_texmf_main}/doc/latex/mugsthesis/

%files -n texlive-muling
%license gpl3.txt
%license fdl.txt
%{_texmf_main}/tex/latex/muling/
%doc %{_texmf_main}/doc/latex/muling/

%files -n texlive-musuos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musuos/
%doc %{_texmf_main}/doc/latex/musuos/

%files -n texlive-muthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/muthesis/
%doc %{_texmf_main}/doc/latex/muthesis/

%files -n texlive-mynsfc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mynsfc/
%doc %{_texmf_main}/doc/latex/mynsfc/

%files -n texlive-nature
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/nature/
%{_texmf_main}/tex/latex/nature/
%doc %{_texmf_main}/doc/latex/nature/

%files -n texlive-navydocs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/navydocs/
%doc %{_texmf_main}/doc/latex/navydocs/

%files -n texlive-nddiss
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/nddiss/
%{_texmf_main}/tex/latex/nddiss/
%doc %{_texmf_main}/doc/latex/nddiss/

%files -n texlive-ndsu-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ndsu-thesis/
%doc %{_texmf_main}/doc/latex/ndsu-thesis/

%files -n texlive-ndsu-thesis-2022
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ndsu-thesis-2022/
%doc %{_texmf_main}/doc/latex/ndsu-thesis-2022/

%files -n texlive-nih
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nih/
%doc %{_texmf_main}/doc/latex/nih/

%files -n texlive-nihbiosketch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nihbiosketch/
%doc %{_texmf_main}/doc/latex/nihbiosketch/

%files -n texlive-njustthesis
%license gpl3.txt
%{_texmf_main}/tex/latex/njustthesis/
%doc %{_texmf_main}/doc/latex/njustthesis/

%files -n texlive-njuthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/njuthesis/
%doc %{_texmf_main}/doc/latex/njuthesis/

%files -n texlive-njuvisual
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/njuvisual/
%doc %{_texmf_main}/doc/latex/njuvisual/

%files -n texlive-nostarch
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/nostarch/
%{_texmf_main}/makeindex/nostarch/
%{_texmf_main}/tex/latex/nostarch/
%doc %{_texmf_main}/doc/latex/nostarch/

%files -n texlive-novel
%license lppl1.3c.txt
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/novel/
%{_texmf_main}/tex/lualatex/novel/
%doc %{_texmf_main}/doc/lualatex/novel/

%files -n texlive-nrc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nrc/
%doc %{_texmf_main}/doc/latex/nrc/

%files -n texlive-nstc-proposal
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nstc-proposal/
%doc %{_texmf_main}/doc/latex/nstc-proposal/

%files -n texlive-nwafuthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nwafuthesis/
%doc %{_texmf_main}/doc/latex/nwafuthesis/

%files -n texlive-nwejm
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nwejm/
%doc %{_texmf_main}/doc/latex/nwejm/

%files -n texlive-nxuthesis
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/nxuthesis/
%{_texmf_main}/tex/latex/nxuthesis/
%doc %{_texmf_main}/doc/latex/nxuthesis/

%files -n texlive-omgtudoc-asoiu
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/omgtudoc-asoiu/
%doc %{_texmf_main}/doc/latex/omgtudoc-asoiu/

%files -n texlive-onrannual
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/onrannual/
%doc %{_texmf_main}/doc/latex/onrannual/

%files -n texlive-opteng
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/opteng/
%doc %{_texmf_main}/doc/latex/opteng/

%files -n texlive-oststud
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/oststud/
%doc %{_texmf_main}/doc/latex/oststud/

%files -n texlive-ou-tma
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ou-tma/
%doc %{_texmf_main}/doc/latex/ou-tma/

%files -n texlive-oup-authoring-template
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/oup-authoring-template/
%{_texmf_main}/tex/latex/oup-authoring-template/
%doc %{_texmf_main}/doc/latex/oup-authoring-template/

%files -n texlive-pats-resume
%license mit.txt
%{_texmf_main}/tex/latex/pats-resume/
%doc %{_texmf_main}/doc/latex/pats-resume/

%files -n texlive-philosophersimprint
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/philosophersimprint/
%doc %{_texmf_main}/doc/latex/philosophersimprint/

%files -n texlive-phimisci
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/phimisci/
%doc %{_texmf_main}/doc/latex/phimisci/

%files -n texlive-pittetd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pittetd/
%doc %{_texmf_main}/doc/latex/pittetd/

%files -n texlive-pkuthss
%license lppl1.3c.txt
%license bsd.txt
%license pd.txt
%{_texmf_main}/tex/latex/pkuthss/
%doc %{_texmf_main}/doc/latex/pkuthss/

%files -n texlive-powerdot-fuberlin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/powerdot-fuberlin/
%doc %{_texmf_main}/doc/latex/powerdot-fuberlin/

%files -n texlive-powerdot-tuliplab
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/powerdot-tuliplab/
%doc %{_texmf_main}/doc/latex/powerdot-tuliplab/

%files -n texlive-pracjourn
%license gpl2.txt
%{_texmf_main}/tex/latex/pracjourn/
%doc %{_texmf_main}/doc/latex/pracjourn/

%files -n texlive-prociagssymp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/prociagssymp/
%doc %{_texmf_main}/doc/latex/prociagssymp/

%files -n texlive-proposal
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/proposal/
%doc %{_texmf_main}/doc/latex/proposal/

%files -n texlive-prtec
%license mit.txt
%{_texmf_main}/bibtex/bst/prtec/
%{_texmf_main}/tex/latex/prtec/
%doc %{_texmf_main}/doc/latex/prtec/

%files -n texlive-ptptex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ptptex/
%doc %{_texmf_main}/doc/latex/ptptex/

%files -n texlive-qrbill
%license lppl1.3c.txt
%license bsd.txt
%{_texmf_main}/scripts/qrbill/
%{_texmf_main}/tex/latex/qrbill/
%doc %{_texmf_main}/doc/latex/qrbill/

%files -n texlive-quantumarticle
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/quantumarticle/
%{_texmf_main}/tex/latex/quantumarticle/
%doc %{_texmf_main}/doc/latex/quantumarticle/

%files -n texlive-rebuttal
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rebuttal/
%doc %{_texmf_main}/doc/latex/rebuttal/

%files -n texlive-regulatory
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/regulatory/
%doc %{_texmf_main}/doc/latex/regulatory/

%files -n texlive-resphilosophica
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/resphilosophica/
%{_texmf_main}/tex/latex/resphilosophica/
%doc %{_texmf_main}/doc/latex/resphilosophica/

%files -n texlive-resumecls
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/resumecls/
%doc %{_texmf_main}/doc/xelatex/resumecls/

%files -n texlive-retosmatematicos
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/retosmatematicos/
%doc %{_texmf_main}/doc/latex/retosmatematicos/

%files -n texlive-revtex
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/revtex/
%{_texmf_main}/tex/latex/revtex/
%doc %{_texmf_main}/doc/latex/revtex/

%files -n texlive-revtex4
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/revtex4/
%{_texmf_main}/tex/latex/revtex4/
%doc %{_texmf_main}/doc/latex/revtex4/

%files -n texlive-revtex4-1
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/revtex4-1/
%{_texmf_main}/tex/latex/revtex4-1/
%doc %{_texmf_main}/doc/latex/revtex4-1/

%files -n texlive-rub-kunstgeschichte
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rub-kunstgeschichte/
%doc %{_texmf_main}/doc/latex/rub-kunstgeschichte/

%files -n texlive-rutitlepage
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rutitlepage/
%doc %{_texmf_main}/doc/latex/rutitlepage/

%files -n texlive-rwth-ci
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rwth-ci/
%doc %{_texmf_main}/doc/latex/rwth-ci/

%files -n texlive-ryersonsgsthesis
%license apache2.txt
%{_texmf_main}/tex/latex/ryersonsgsthesis/
%doc %{_texmf_main}/doc/latex/ryersonsgsthesis/

%files -n texlive-ryethesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ryethesis/
%doc %{_texmf_main}/doc/latex/ryethesis/

%files -n texlive-sageep
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/sageep/
%{_texmf_main}/tex/latex/sageep/
%doc %{_texmf_main}/doc/latex/sageep/

%files -n texlive-sapthesis
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/sapthesis/
%{_texmf_main}/tex/latex/sapthesis/
%doc %{_texmf_main}/doc/latex/sapthesis/

%files -n texlive-schule
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/schule/
%doc %{_texmf_main}/doc/latex/schule/

%files -n texlive-scientific-thesis-cover
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scientific-thesis-cover/
%doc %{_texmf_main}/doc/latex/scientific-thesis-cover/

%files -n texlive-scripture
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scripture/
%doc %{_texmf_main}/doc/latex/scripture/

%files -n texlive-scrjrnl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scrjrnl/
%doc %{_texmf_main}/doc/latex/scrjrnl/

%files -n texlive-sduthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sduthesis/
%doc %{_texmf_main}/doc/latex/sduthesis/

%files -n texlive-se2thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/se2thesis/
%doc %{_texmf_main}/doc/latex/se2thesis/

%files -n texlive-seu-ml-assign
%license mit.txt
%{_texmf_main}/tex/latex/seu-ml-assign/
%doc %{_texmf_main}/doc/latex/seu-ml-assign/

%files -n texlive-seuthesis
%license gpl3.txt
%{_texmf_main}/bibtex/bst/seuthesis/
%doc %{_texmf_main}/doc/latex/seuthesis/

%files -n texlive-seuthesix
%license gpl3.txt
%{_texmf_main}/bibtex/bst/seuthesix/
%{_texmf_main}/tex/latex/seuthesix/
%doc %{_texmf_main}/doc/latex/seuthesix/

%files -n texlive-sfee
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/sfee/
%{_texmf_main}/tex/latex/sfee/
%doc %{_texmf_main}/doc/latex/sfee/

%files -n texlive-shortmathj
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/shortmathj/
%doc %{_texmf_main}/doc/latex/shortmathj/

%files -n texlive-shtthesis
%license gpl3.txt
%{_texmf_main}/tex/latex/shtthesis/
%doc %{_texmf_main}/doc/latex/shtthesis/

%files -n texlive-smflatex
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/smflatex/
%{_texmf_main}/tex/latex/smflatex/
%doc %{_texmf_main}/doc/latex/smflatex/

%files -n texlive-soton
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/soton/
%doc %{_texmf_main}/doc/latex/soton/

%files -n texlive-sphdthesis
%license pd.txt
%{_texmf_main}/tex/latex/sphdthesis/
%doc %{_texmf_main}/doc/latex/sphdthesis/

%files -n texlive-spie
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/spie/
%{_texmf_main}/bibtex/bst/spie/
%{_texmf_main}/tex/latex/spie/
%doc %{_texmf_main}/doc/latex/spie/

%files -n texlive-sr-vorl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sr-vorl/
%doc %{_texmf_main}/doc/latex/sr-vorl/

%files -n texlive-srdp-mathematik
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/srdp-mathematik/
%doc %{_texmf_main}/doc/latex/srdp-mathematik/

%files -n texlive-sshrc-insight
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sshrc-insight/
%doc %{_texmf_main}/doc/latex/sshrc-insight/

%files -n texlive-stellenbosch
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/stellenbosch/
%{_texmf_main}/tex/latex/stellenbosch/
%doc %{_texmf_main}/doc/latex/stellenbosch/

%files -n texlive-stellenbosch-2
%license cc-by-4.txt
%{_texmf_main}/bibtex/bst/stellenbosch-2/
%{_texmf_main}/tex/latex/stellenbosch-2/
%doc %{_texmf_main}/doc/latex/stellenbosch-2/

%files -n texlive-suftesi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/suftesi/
%doc %{_texmf_main}/doc/latex/suftesi/

%files -n texlive-sugconf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sugconf/
%doc %{_texmf_main}/doc/latex/sugconf/

%files -n texlive-sysuthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sysuthesis/
%doc %{_texmf_main}/doc/latex/sysuthesis/

%files -n texlive-tabriz-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tabriz-thesis/
%{_texmf_main}/tex/xelatex/tabriz-thesis/
%doc %{_texmf_main}/doc/latex/tabriz-thesis/
%doc %{_texmf_main}/doc/xelatex/tabriz-thesis/

%files -n texlive-technion-thesis-template
%license cc-by-4.txt
%{_texmf_main}/tex/xelatex/technion-thesis-template/
%doc %{_texmf_main}/doc/xelatex/technion-thesis-template/

%files -n texlive-texilikechaps
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/texilikechaps/

%files -n texlive-texilikecover
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/texilikecover/

%files -n texlive-thesis-ekf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thesis-ekf/
%doc %{_texmf_main}/doc/latex/thesis-ekf/

%files -n texlive-thesis-gwu
%license gpl3.txt
%{_texmf_main}/tex/latex/thesis-gwu/
%doc %{_texmf_main}/doc/latex/thesis-gwu/

%files -n texlive-thesis-qom
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/thesis-qom/
%doc %{_texmf_main}/doc/xelatex/thesis-qom/

%files -n texlive-thesis-titlepage-fhac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thesis-titlepage-fhac/
%doc %{_texmf_main}/doc/latex/thesis-titlepage-fhac/

%files -n texlive-thuaslogos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thuaslogos/
%doc %{_texmf_main}/doc/latex/thuaslogos/

%files -n texlive-thubeamer
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/thubeamer/
%{_texmf_main}/tex/latex/thubeamer/
%doc %{_texmf_main}/doc/latex/thubeamer/

%files -n texlive-thucoursework
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thucoursework/
%doc %{_texmf_main}/doc/latex/thucoursework/

%files -n texlive-thuthesis
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/thuthesis/
%{_texmf_main}/tex/latex/thuthesis/
%doc %{_texmf_main}/doc/latex/thuthesis/

%files -n texlive-tidyres
%license cc-by-4.txt
%{_texmf_main}/tex/latex/tidyres/
%doc %{_texmf_main}/doc/latex/tidyres/

%files -n texlive-tiet-question-paper
%license mit.txt
%{_texmf_main}/tex/latex/tiet-question-paper/
%doc %{_texmf_main}/doc/latex/tiet-question-paper/

%files -n texlive-timbreicmc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/timbreicmc/
%doc %{_texmf_main}/doc/latex/timbreicmc/

%files -n texlive-tlc-article
%license bsd.txt
%{_texmf_main}/tex/latex/tlc-article/
%doc %{_texmf_main}/doc/latex/tlc-article/

%files -n texlive-topletter
%license apache2.txt
%{_texmf_main}/tex/latex/topletter/
%doc %{_texmf_main}/doc/latex/topletter/

%files -n texlive-toptesi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/toptesi/
%doc %{_texmf_main}/doc/latex/toptesi/

%files -n texlive-tuda-ci
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tuda-ci/
%doc %{_texmf_main}/doc/latex/tuda-ci/

%files -n texlive-tudscr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tudscr/
%doc %{_texmf_main}/doc/latex/tudscr/

%files -n texlive-tugboat
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/tugboat/
%{_texmf_main}/tex/latex/tugboat/
%doc %{_texmf_main}/doc/latex/tugboat/

%files -n texlive-tugboat-plain
%license other-free.txt
%{_texmf_main}/tex/plain/tugboat-plain/
%doc %{_texmf_main}/doc/plain/tugboat-plain/

%files -n texlive-tui
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tui/
%doc %{_texmf_main}/doc/latex/tui/

%files -n texlive-turabian
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/turabian/
%doc %{_texmf_main}/doc/latex/turabian/

%files -n texlive-uaclasses
%license pd.txt
%{_texmf_main}/tex/latex/uaclasses/
%doc %{_texmf_main}/doc/latex/uaclasses/

%files -n texlive-uafthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uafthesis/
%doc %{_texmf_main}/doc/latex/uafthesis/

%files -n texlive-ualberta
%license mit.txt
%{_texmf_main}/tex/latex/ualberta/
%doc %{_texmf_main}/doc/latex/ualberta/

%files -n texlive-uantwerpendocs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uantwerpendocs/
%doc %{_texmf_main}/doc/latex/uantwerpendocs/

%files -n texlive-ucalgmthesis
%license mit.txt
%{_texmf_main}/tex/latex/ucalgmthesis/
%doc %{_texmf_main}/doc/latex/ucalgmthesis/

%files -n texlive-ucbthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ucbthesis/
%doc %{_texmf_main}/doc/latex/ucbthesis/

%files -n texlive-ucdavisthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ucdavisthesis/
%doc %{_texmf_main}/doc/latex/ucdavisthesis/

%files -n texlive-ucph-revy
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ucph-revy/
%doc %{_texmf_main}/doc/latex/ucph-revy/

%files -n texlive-ucsmonograph
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ucsmonograph/
%doc %{_texmf_main}/doc/latex/ucsmonograph/

%files -n texlive-ucthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ucthesis/
%doc %{_texmf_main}/doc/latex/ucthesis/

%files -n texlive-udepcolor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/udepcolor/
%doc %{_texmf_main}/doc/latex/udepcolor/

%files -n texlive-udes-genie-these
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/udes-genie-these/
%doc %{_texmf_main}/doc/latex/udes-genie-these/

%files -n texlive-udiss
%license gpl3.txt
%license fdl.txt
%{_texmf_main}/tex/latex/udiss/
%doc %{_texmf_main}/doc/latex/udiss/

%files -n texlive-uestcthesis
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/uestcthesis/
%{_texmf_main}/tex/latex/uestcthesis/
%doc %{_texmf_main}/doc/latex/uestcthesis/

%files -n texlive-ufrgscca
%license lppl1.3c.txt
%license other-free.txt
%{_texmf_main}/tex/latex/ufrgscca/
%doc %{_texmf_main}/doc/latex/ufrgscca/

%files -n texlive-uhhassignment
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uhhassignment/
%doc %{_texmf_main}/doc/latex/uhhassignment/

%files -n texlive-uiucredborder
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uiucredborder/
%doc %{_texmf_main}/doc/latex/uiucredborder/

%files -n texlive-uiucthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uiucthesis/
%doc %{_texmf_main}/doc/latex/uiucthesis/

%files -n texlive-ukbill
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ukbill/
%doc %{_texmf_main}/doc/latex/ukbill/

%files -n texlive-ulthese
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ulthese/
%doc %{_texmf_main}/doc/latex/ulthese/

%files -n texlive-umbclegislation
%license gpl3.txt
%{_texmf_main}/tex/latex/umbclegislation/
%doc %{_texmf_main}/doc/latex/umbclegislation/

%files -n texlive-umich-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/umich-thesis/
%doc %{_texmf_main}/doc/latex/umich-thesis/

%files -n texlive-umthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/umthesis/
%doc %{_texmf_main}/doc/latex/umthesis/

%files -n texlive-unam-thesis
%license gpl3.txt
%{_texmf_main}/tex/latex/unam-thesis/
%doc %{_texmf_main}/doc/latex/unam-thesis/

%files -n texlive-unamth-template
%license gpl3.txt
%doc %{_texmf_main}/doc/latex/unamth-template/

%files -n texlive-unamthesis
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/unamthesis/
%{_texmf_main}/tex/latex/unamthesis/
%doc %{_texmf_main}/doc/latex/unamthesis/

%files -n texlive-unbtex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/unbtex/
%doc %{_texmf_main}/doc/latex/unbtex/

%files -n texlive-unifith
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/unifith/
%{_texmf_main}/tex/latex/unifith/
%doc %{_texmf_main}/doc/latex/unifith/

%files -n texlive-unigrazpub
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/unigrazpub/
%doc %{_texmf_main}/doc/latex/unigrazpub/

%files -n texlive-unitn-bimrep
%license mit.txt
%{_texmf_main}/tex/latex/unitn-bimrep/
%doc %{_texmf_main}/doc/latex/unitn-bimrep/

%files -n texlive-univie-ling
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/univie-ling/
%doc %{_texmf_main}/doc/latex/univie-ling/

%files -n texlive-unizgklasa
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/unizgklasa/
%doc %{_texmf_main}/doc/latex/unizgklasa/

%files -n texlive-unswcover
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/unswcover/
%doc %{_texmf_main}/doc/latex/unswcover/

%files -n texlive-uol-physics-report
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uol-physics-report/
%doc %{_texmf_main}/doc/latex/uol-physics-report/

%files -n texlive-uothesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uothesis/
%doc %{_texmf_main}/doc/latex/uothesis/

%files -n texlive-uowthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uowthesis/
%doc %{_texmf_main}/doc/latex/uowthesis/

%files -n texlive-uowthesistitlepage
%license lppl1.3c.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/uowthesistitlepage/
%doc %{_texmf_main}/doc/latex/uowthesistitlepage/

%files -n texlive-urcls
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/urcls/
%doc %{_texmf_main}/doc/latex/urcls/

%files -n texlive-uspatent
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uspatent/
%doc %{_texmf_main}/doc/latex/uspatent/

%files -n texlive-ut-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ut-thesis/
%doc %{_texmf_main}/doc/latex/ut-thesis/

%files -n texlive-utexasthesis
%license cc-zero-1.txt
%{_texmf_main}/tex/latex/utexasthesis/
%doc %{_texmf_main}/doc/latex/utexasthesis/

%files -n texlive-uvaletter
%license mit.txt
%{_texmf_main}/tex/latex/uvaletter/
%doc %{_texmf_main}/doc/latex/uvaletter/

%files -n texlive-uwa-colours
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uwa-colours/
%doc %{_texmf_main}/doc/latex/uwa-colours/

%files -n texlive-uwa-letterhead
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uwa-letterhead/
%doc %{_texmf_main}/doc/latex/uwa-letterhead/

%files -n texlive-uwa-pcf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uwa-pcf/
%doc %{_texmf_main}/doc/latex/uwa-pcf/

%files -n texlive-uwa-pif
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uwa-pif/
%doc %{_texmf_main}/doc/latex/uwa-pif/

%files -n texlive-uwthesis
%license apache2.txt
%{_texmf_main}/tex/latex/uwthesis/
%doc %{_texmf_main}/doc/latex/uwthesis/

%files -n texlive-vancouver
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/vancouver/
%doc %{_texmf_main}/doc/bibtex/vancouver/

%files -n texlive-wsemclassic
%license bsd.txt
%{_texmf_main}/tex/latex/wsemclassic/
%doc %{_texmf_main}/doc/latex/wsemclassic/

%files -n texlive-xduthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xduthesis/
%doc %{_texmf_main}/doc/latex/xduthesis/

%files -n texlive-xduts
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xduts/
%doc %{_texmf_main}/doc/xelatex/xduts/

%files -n texlive-xmuthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xmuthesis/
%doc %{_texmf_main}/doc/latex/xmuthesis/

%files -n texlive-yathesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/yathesis/
%doc %{_texmf_main}/doc/latex/yathesis/

%files -n texlive-yazd-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/yazd-thesis/
%doc %{_texmf_main}/doc/xelatex/yazd-thesis/

%files -n texlive-yb-book
%license mit.txt
%{_texmf_main}/tex/latex/yb-book/
%doc %{_texmf_main}/doc/latex/yb-book/

%files -n texlive-york-thesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/york-thesis/
%doc %{_texmf_main}/doc/latex/york-thesis/

%changelog
* Mon Feb  9 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77587-2
- remove Requires: tex(uarial.sty), it is optional in the code and not provided by texlive (bz437624)
- update asmeconf asmejour har2nat llncs lni mitthesis novel oup-authoring-template sysuthesis tugboat
  ualberta univie-ling ut-thesis uwa-letterhead uwa-pcf uwa-pif

* Wed Feb 04 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77587-1
- Update to svn77587, fix descriptions, licensing, update components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75966-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75966-1
- Update to TeX Live 2025
