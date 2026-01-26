%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-fontsextra
Epoch:          12
Version:        svn77044
Release:        2%{?dist}
Summary:        Additional fonts

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-fontsextra.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aboensis.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aboensis.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/academicons.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/academicons.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/accanthis.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/accanthis.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adforn.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adforn.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adfsymbols.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adfsymbols.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aesupp.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aesupp.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alegreya.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alegreya.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alfaslabone.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alfaslabone.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algolrevived.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/algolrevived.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/allrunes.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/allrunes.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/almendra.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/almendra.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/almfixed.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/almfixed.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/andika.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/andika.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anonymouspro.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anonymouspro.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antiqua.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antiqua.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antt.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antt.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/archaic.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/archaic.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/archivo.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/archivo.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arev.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arev.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arimo.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arimo.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arsenal.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arsenal.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arsenal-math.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arsenal-math.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arvo.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arvo.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asana-math.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asana-math.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asapsym.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asapsym.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascii-font.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascii-font.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aspectratio.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aspectratio.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/astro.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/astro.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atkinson.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atkinson.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/augie.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/augie.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auncial-new.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auncial-new.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aurical.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aurical.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/b1encoding.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/b1encoding.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bahaistar.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bahaistar.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/barcodes.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/barcodes.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baskervaldadf.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baskervaldadf.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baskervaldx.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baskervaldx.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baskervillef.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baskervillef.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbding.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbding.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbm.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbm.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbm-macros.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbm-macros.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbold.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbold.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbold-type1.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbold-type1.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bboldx.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bboldx.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/belleek.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/belleek.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bera.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bera.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/berenisadf.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/berenisadf.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beuron.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beuron.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bguq.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bguq.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitter.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitter.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blacklettert1.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blacklettert1.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/boisik.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/boisik.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bonum-otf.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bonum-otf.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookhands.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookhands.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/boondox.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/boondox.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/braille.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/braille.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brushscr.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/brushscr.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cabin.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cabin.doc.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/caladea.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/caladea.doc.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calligra.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calligra.doc.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calligra-type1.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/calligra-type1.doc.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cantarell.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cantarell.doc.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carlito.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carlito.doc.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carolmin-ps.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carolmin-ps.doc.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascadia-code.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascadia-code.doc.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascadiamono-otf.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cascadiamono-otf.doc.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ccicons.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ccicons.doc.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cfr-initials.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cfr-initials.doc.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cfr-lm.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cfr-lm.doc.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/charissil.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/charissil.doc.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cherokee.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cherokee.doc.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chivo.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chivo.doc.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cinzel.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cinzel.doc.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clara.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clara.doc.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clearsans.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clearsans.doc.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-lgc.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-lgc.doc.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-mf-extra-bold.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-unicode.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-unicode.doc.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmathbb.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmathbb.doc.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmbright.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmbright.doc.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmexb.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmexb.doc.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmll.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmll.doc.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmpica.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmpica.doc.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmsrb.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmsrb.doc.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmtiup.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmtiup.doc.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmupint.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmupint.doc.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cochineal.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cochineal.doc.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coelacanth.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/coelacanth.doc.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/comfortaa.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/comfortaa.doc.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/comicneue.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/comicneue.doc.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concmath-fonts.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concmath-fonts.doc.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concmath-otf.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/concmath-otf.doc.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cookingsymbols.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cookingsymbols.doc.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cooperhewitt.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cooperhewitt.doc.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cormorantgaramond.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cormorantgaramond.doc.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/countriesofeurope.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/countriesofeurope.doc.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/courier-scaled.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/courier-scaled.doc.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/courierten.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/courierten.doc.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crimson.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crimson.doc.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crimsonpro.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crimsonpro.doc.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cryst.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cryst.doc.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cuprum.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cuprum.doc.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyklop.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyklop.doc.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrillic-modern.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrillic-modern.doc.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dancers.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dantelogo.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dantelogo.doc.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dejavu.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dejavu.doc.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dejavu-otf.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dejavu-otf.doc.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dice.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dice.doc.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dictsym.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dictsym.doc.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dingbat.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dingbat.doc.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/domitian.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/domitian.doc.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doublestroke.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doublestroke.doc.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doulossil.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/doulossil.doc.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dozenal.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dozenal.doc.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drm.tar.xz
Source231:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drm.doc.tar.xz
Source232:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/droid.tar.xz
Source233:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/droid.doc.tar.xz
Source234:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dsserif.tar.xz
Source235:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dsserif.doc.tar.xz
Source236:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/duerer.tar.xz
Source237:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/duerer.doc.tar.xz
Source238:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/duerer-latex.tar.xz
Source239:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/duerer-latex.doc.tar.xz
Source240:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dutchcal.tar.xz
Source241:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dutchcal.doc.tar.xz
Source242:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ean.tar.xz
Source243:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ean.doc.tar.xz
Source244:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebgaramond.tar.xz
Source245:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebgaramond.doc.tar.xz
Source246:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebgaramond-maths.tar.xz
Source247:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebgaramond-maths.doc.tar.xz
Source248:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecc.tar.xz
Source249:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecc.doc.tar.xz
Source250:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eco.tar.xz
Source251:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eco.doc.tar.xz
Source252:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eczar.tar.xz
Source253:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eczar.doc.tar.xz
Source254:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eiad.tar.xz
Source255:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eiad.doc.tar.xz
Source256:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eiad-ltx.tar.xz
Source257:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eiad-ltx.doc.tar.xz
Source258:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ektype-tanka.tar.xz
Source259:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ektype-tanka.doc.tar.xz
Source260:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/electrumadf.tar.xz
Source261:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/electrumadf.doc.tar.xz
Source262:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elvish.tar.xz
Source263:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/elvish.doc.tar.xz
Source264:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epigrafica.tar.xz
Source265:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epigrafica.doc.tar.xz
Source266:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsdice.tar.xz
Source267:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsdice.doc.tar.xz
Source268:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/erewhon.tar.xz
Source269:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/erewhon.doc.tar.xz
Source270:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/erewhon-math.tar.xz
Source271:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/erewhon-math.doc.tar.xz
Source272:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esrelation.tar.xz
Source273:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esrelation.doc.tar.xz
Source274:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esstix.tar.xz
Source275:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esstix.doc.tar.xz
Source276:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esvect.tar.xz
Source277:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/esvect.doc.tar.xz
Source278:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etbb.tar.xz
Source279:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etbb.doc.tar.xz
Source280:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euler-math.tar.xz
Source281:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euler-math.doc.tar.xz
Source282:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eulervm.tar.xz
Source283:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eulervm.doc.tar.xz
Source284:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euxm.tar.xz
Source285:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fbb.tar.xz
Source286:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fbb.doc.tar.xz
Source287:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fdsymbol.tar.xz
Source288:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fdsymbol.doc.tar.xz
Source289:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fetamont.tar.xz
Source290:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fetamont.doc.tar.xz
Source291:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feyn.tar.xz
Source292:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feyn.doc.tar.xz
Source293:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fge.tar.xz
Source294:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fge.doc.tar.xz
Source295:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fira.tar.xz
Source296:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fira.doc.tar.xz
Source297:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firamath.tar.xz
Source298:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firamath.doc.tar.xz
Source299:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firamath-otf.tar.xz
Source300:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firamath-otf.doc.tar.xz
Source301:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/foekfont.tar.xz
Source302:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/foekfont.doc.tar.xz
Source303:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonetika.tar.xz
Source304:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonetika.doc.tar.xz
Source305:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome.tar.xz
Source306:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome.doc.tar.xz
Source307:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome5.tar.xz
Source308:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome5.doc.tar.xz
Source309:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome6.tar.xz
Source310:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome6.doc.tar.xz
Source311:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome7.tar.xz
Source312:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesome7.doc.tar.xz
Source313:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesomescaled.tar.xz
Source314:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontawesomescaled.doc.tar.xz
Source315:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontmfizz.tar.xz
Source316:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontmfizz.doc.tar.xz
Source317:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonts-churchslavonic.tar.xz
Source318:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonts-churchslavonic.doc.tar.xz
Source319:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontscripts.tar.xz
Source320:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontscripts.doc.tar.xz
Source321:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forum.tar.xz
Source322:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forum.doc.tar.xz
Source323:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fourier.tar.xz
Source324:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fourier.doc.tar.xz
Source325:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fouriernc.tar.xz
Source326:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fouriernc.doc.tar.xz
Source327:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frcursive.tar.xz
Source328:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frcursive.doc.tar.xz
Source329:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frederika2016.tar.xz
Source330:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frederika2016.doc.tar.xz
Source331:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frimurer.tar.xz
Source332:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frimurer.doc.tar.xz
Source333:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garamond-libre.tar.xz
Source334:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garamond-libre.doc.tar.xz
Source335:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garamond-math.tar.xz
Source336:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garamond-math.doc.tar.xz
Source337:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gelasio.tar.xz
Source338:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gelasio.doc.tar.xz
Source339:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gelasiomath.tar.xz
Source340:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gelasiomath.doc.tar.xz
Source341:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/genealogy.tar.xz
Source342:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/genealogy.doc.tar.xz
Source343:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gentium-otf.tar.xz
Source344:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gentium-otf.doc.tar.xz
Source345:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gentium-sil.tar.xz
Source346:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gentium-sil.doc.tar.xz
Source347:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsartemisia.tar.xz
Source348:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsartemisia.doc.tar.xz
Source349:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsbodoni.tar.xz
Source350:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsbodoni.doc.tar.xz
Source351:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfscomplutum.tar.xz
Source352:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfscomplutum.doc.tar.xz
Source353:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsdidot.tar.xz
Source354:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsdidot.doc.tar.xz
Source355:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsdidotclassic.tar.xz
Source356:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsdidotclassic.doc.tar.xz
Source357:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsneohellenic.tar.xz
Source358:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsneohellenic.doc.tar.xz
Source359:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsneohellenicmath.tar.xz
Source360:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsneohellenicmath.doc.tar.xz
Source361:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfssolomos.tar.xz
Source362:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfssolomos.doc.tar.xz
Source363:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gillcm.tar.xz
Source364:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gillcm.doc.tar.xz
Source365:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gillius.tar.xz
Source366:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gillius.doc.tar.xz
Source367:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gnu-freefont.tar.xz
Source368:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gnu-freefont.doc.tar.xz
Source369:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gofonts.tar.xz
Source370:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gofonts.doc.tar.xz
Source371:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gothic.tar.xz
Source372:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gothic.doc.tar.xz
Source373:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greenpoint.tar.xz
Source374:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greenpoint.doc.tar.xz
Source375:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grotesq.tar.xz
Source376:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grotesq.doc.tar.xz
Source377:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gudea.tar.xz
Source378:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gudea.doc.tar.xz
Source379:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hacm.tar.xz
Source380:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hacm.doc.tar.xz
Source381:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hamnosys.tar.xz
Source382:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hamnosys.doc.tar.xz
Source383:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hands.tar.xz
Source384:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-font.tar.xz
Source385:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-font.doc.tar.xz
Source386:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-math-font.tar.xz
Source387:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hep-math-font.doc.tar.xz
Source388:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/heros-otf.tar.xz
Source389:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/heros-otf.doc.tar.xz
Source390:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/heuristica.tar.xz
Source391:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/heuristica.doc.tar.xz
Source392:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfbright.tar.xz
Source393:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfbright.doc.tar.xz
Source394:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfoldsty.tar.xz
Source395:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hfoldsty.doc.tar.xz
Source396:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hindmadurai.tar.xz
Source397:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hindmadurai.doc.tar.xz
Source398:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibarra.tar.xz
Source399:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibarra.doc.tar.xz
Source400:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifsym.tar.xz
Source401:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifsym.doc.tar.xz
Source402:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imfellenglish.tar.xz
Source403:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imfellenglish.doc.tar.xz
Source404:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inconsolata.tar.xz
Source405:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inconsolata.doc.tar.xz
Source406:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inconsolata-nerd-font.tar.xz
Source407:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inconsolata-nerd-font.doc.tar.xz
Source408:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/initials.tar.xz
Source409:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/initials.doc.tar.xz
Source410:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inriafonts.tar.xz
Source411:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inriafonts.doc.tar.xz
Source412:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inter.tar.xz
Source413:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/inter.doc.tar.xz
Source414:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex-type1.tar.xz
Source415:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex-type1.doc.tar.xz
Source416:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iwona.tar.xz
Source417:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iwona.doc.tar.xz
Source418:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jablantile.tar.xz
Source419:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jablantile.doc.tar.xz
Source420:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jamtimes.tar.xz
Source421:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jamtimes.doc.tar.xz
Source422:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jetbrainsmono-otf.tar.xz
Source423:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jetbrainsmono-otf.doc.tar.xz
Source424:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/josefin.tar.xz
Source425:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/josefin.doc.tar.xz
Source426:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juliamono.tar.xz
Source427:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juliamono.doc.tar.xz
Source428:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/junicode.tar.xz
Source429:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/junicode.doc.tar.xz
Source430:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/junicodevf.tar.xz
Source431:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/junicodevf.doc.tar.xz
Source432:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kixfont.tar.xz
Source433:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kixfont.doc.tar.xz
Source434:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kpfonts.tar.xz
Source435:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kpfonts.doc.tar.xz
Source436:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kpfonts-otf.tar.xz
Source437:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kpfonts-otf.doc.tar.xz
Source438:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kurier.tar.xz
Source439:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kurier.doc.tar.xz
Source440:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lato.tar.xz
Source441:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lato.doc.tar.xz
Source442:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lete-sans-math.tar.xz
Source443:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lete-sans-math.doc.tar.xz
Source444:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexend.tar.xz
Source445:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexend.doc.tar.xz
Source446:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lfb.tar.xz
Source447:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lfb.doc.tar.xz
Source448:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertine.tar.xz
Source449:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertine.doc.tar.xz
Source450:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinegc.tar.xz
Source451:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinegc.doc.tar.xz
Source452:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus.tar.xz
Source453:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus.doc.tar.xz
Source454:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus-fonts.tar.xz
Source455:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus-fonts.doc.tar.xz
Source456:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus-otf.tar.xz
Source457:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus-otf.doc.tar.xz
Source458:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus-type1.tar.xz
Source459:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinus-type1.doc.tar.xz
Source460:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinust1math.tar.xz
Source461:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libertinust1math.doc.tar.xz
Source462:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librebaskerville.tar.xz
Source463:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librebaskerville.doc.tar.xz
Source464:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librebodoni.tar.xz
Source465:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librebodoni.doc.tar.xz
Source466:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librecaslon.tar.xz
Source467:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librecaslon.doc.tar.xz
Source468:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librefranklin.tar.xz
Source469:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/librefranklin.doc.tar.xz
Source470:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libris.tar.xz
Source471:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/libris.doc.tar.xz
Source472:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lineara.tar.xz
Source473:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lineara.doc.tar.xz
Source474:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguisticspro.tar.xz
Source475:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguisticspro.doc.tar.xz
Source476:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lobster2.tar.xz
Source477:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lobster2.doc.tar.xz
Source478:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logix.tar.xz
Source479:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logix.doc.tar.xz
Source480:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luciole.tar.xz
Source481:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luciole.doc.tar.xz
Source482:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luwiantype.tar.xz
Source483:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luwiantype.doc.tar.xz
Source484:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lxfonts.tar.xz
Source485:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lxfonts.doc.tar.xz
Source486:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ly1.tar.xz
Source487:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ly1.doc.tar.xz
Source488:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lydtype.tar.xz
Source489:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lydtype.doc.tar.xz
Source490:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/magra.tar.xz
Source491:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/magra.doc.tar.xz
Source492:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marcellus.tar.xz
Source493:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marcellus.doc.tar.xz
Source494:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathabx.tar.xz
Source495:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathabx.doc.tar.xz
Source496:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathabx-type1.tar.xz
Source497:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathabx-type1.doc.tar.xz
Source498:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathdesign.tar.xz
Source499:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathdesign.doc.tar.xz
Source500:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mdputu.tar.xz
Source501:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mdputu.doc.tar.xz
Source502:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mdsymbol.tar.xz
Source503:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mdsymbol.doc.tar.xz
Source504:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/merriweather.tar.xz
Source505:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/merriweather.doc.tar.xz
Source506:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metsymb.tar.xz
Source507:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metsymb.doc.tar.xz
Source508:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfb-oldstyle.tar.xz
Source509:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfb-oldstyle.doc.tar.xz
Source510:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/miama.tar.xz
Source511:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/miama.doc.tar.xz
Source512:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mintspirit.tar.xz
Source513:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mintspirit.doc.tar.xz
Source514:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/missaali.tar.xz
Source515:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/missaali.doc.tar.xz
Source516:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mlmodern.tar.xz
Source517:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mlmodern.doc.tar.xz
Source518:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnsymbol.tar.xz
Source519:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnsymbol.doc.tar.xz
Source520:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/monaspace-otf.tar.xz
Source521:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/monaspace-otf.doc.tar.xz
Source522:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/montserrat.tar.xz
Source523:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/montserrat.doc.tar.xz
Source524:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpfonts.tar.xz
Source525:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpfonts.doc.tar.xz
Source526:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mweights.tar.xz
Source527:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mweights.doc.tar.xz
Source528:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newcomputermodern.tar.xz
Source529:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newcomputermodern.doc.tar.xz
Source530:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newpx.tar.xz
Source531:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newpx.doc.tar.xz
Source532:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newtx.tar.xz
Source533:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newtx.doc.tar.xz
Source534:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newtxsf.tar.xz
Source535:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newtxsf.doc.tar.xz
Source536:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newtxtt.tar.xz
Source537:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newtxtt.doc.tar.xz
Source538:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/niceframe-type1.tar.xz
Source539:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/niceframe-type1.doc.tar.xz
Source540:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nimbus15.tar.xz
Source541:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nimbus15.doc.tar.xz
Source542:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nkarta.tar.xz
Source543:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nkarta.doc.tar.xz
Source544:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/noto.tar.xz
Source545:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/noto.doc.tar.xz
Source546:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/noto-emoji.tar.xz
Source547:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/noto-emoji.doc.tar.xz
Source548:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/notomath.tar.xz
Source549:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/notomath.doc.tar.xz
Source550:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nunito.tar.xz
Source551:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nunito.doc.tar.xz
Source552:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/obnov.tar.xz
Source553:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/obnov.doc.tar.xz
Source554:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ocherokee.tar.xz
Source555:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ocherokee.doc.tar.xz
Source556:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ocr-b.tar.xz
Source557:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ocr-b.doc.tar.xz
Source558:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ocr-b-outline.tar.xz
Source559:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ocr-b-outline.doc.tar.xz
Source560:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ogham.tar.xz
Source561:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ogham.doc.tar.xz
Source562:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oinuit.tar.xz
Source563:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oinuit.doc.tar.xz
Source564:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/old-arrows.tar.xz
Source565:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/old-arrows.doc.tar.xz
Source566:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oldlatin.tar.xz
Source567:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oldlatin.doc.tar.xz
Source568:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oldstandard.tar.xz
Source569:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oldstandard.doc.tar.xz
Source570:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opensans.tar.xz
Source571:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opensans.doc.tar.xz
Source572:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/orkhun.tar.xz
Source573:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/orkhun.doc.tar.xz
Source574:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oswald.tar.xz
Source575:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oswald.doc.tar.xz
Source576:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overlock.tar.xz
Source577:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overlock.doc.tar.xz
Source578:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pacioli.tar.xz
Source579:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pacioli.doc.tar.xz
Source580:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pagella-otf.tar.xz
Source581:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pagella-otf.doc.tar.xz
Source582:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/paratype.tar.xz
Source583:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/paratype.doc.tar.xz
Source584:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pennstander-otf.tar.xz
Source585:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pennstander-otf.doc.tar.xz
Source586:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phaistos.tar.xz
Source587:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phaistos.doc.tar.xz
Source588:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phonetic.tar.xz
Source589:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phonetic.doc.tar.xz
Source590:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pigpen.tar.xz
Source591:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pigpen.doc.tar.xz
Source592:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/playfair.tar.xz
Source593:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/playfair.doc.tar.xz
Source594:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plex.tar.xz
Source595:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plex.doc.tar.xz
Source596:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plex-otf.tar.xz
Source597:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plex-otf.doc.tar.xz
Source598:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plimsoll.tar.xz
Source599:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plimsoll.doc.tar.xz
Source600:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poiretone.tar.xz
Source601:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poiretone.doc.tar.xz
Source602:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poltawski.tar.xz
Source603:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poltawski.doc.tar.xz
Source604:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prodint.tar.xz
Source605:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/prodint.doc.tar.xz
Source606:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/punk.tar.xz
Source607:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/punk.doc.tar.xz
Source608:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/punk-latex.tar.xz
Source609:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/punk-latex.doc.tar.xz
Source610:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/punknova.tar.xz
Source611:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/punknova.doc.tar.xz
Source612:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxtxalfa.tar.xz
Source613:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxtxalfa.doc.tar.xz
Source614:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qualitype.tar.xz
Source615:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qualitype.doc.tar.xz
Source616:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quattrocento.tar.xz
Source617:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quattrocento.doc.tar.xz
Source618:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/raleway.tar.xz
Source619:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/raleway.doc.tar.xz
Source620:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/recycle.tar.xz
Source621:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/recycle.doc.tar.xz
Source622:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rit-fonts.tar.xz
Source623:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rit-fonts.doc.tar.xz
Source624:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roboto.tar.xz
Source625:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roboto.doc.tar.xz
Source626:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/romandeadf.tar.xz
Source627:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/romandeadf.doc.tar.xz
Source628:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rosario.tar.xz
Source629:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rosario.doc.tar.xz
Source630:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsfso.tar.xz
Source631:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsfso.doc.tar.xz
Source632:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ruscap.tar.xz
Source633:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ruscap.doc.tar.xz
Source634:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathaccent.tar.xz
Source635:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathaccent.doc.tar.xz
Source636:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathfonts.tar.xz
Source637:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmathfonts.doc.tar.xz
Source638:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sauter.tar.xz
Source639:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sauterfonts.tar.xz
Source640:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sauterfonts.doc.tar.xz
Source641:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schola-otf.tar.xz
Source642:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schola-otf.doc.tar.xz
Source643:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scholax.tar.xz
Source644:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scholax.doc.tar.xz
Source645:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schulschriften.tar.xz
Source646:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schulschriften.doc.tar.xz
Source647:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/semaphor.tar.xz
Source648:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/semaphor.doc.tar.xz
Source649:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shobhika.tar.xz
Source650:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shobhika.doc.tar.xz
Source651:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simpleicons.tar.xz
Source652:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simpleicons.doc.tar.xz
Source653:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skull.tar.xz
Source654:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sourcecodepro.tar.xz
Source655:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sourcecodepro.doc.tar.xz
Source656:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sourcesanspro.tar.xz
Source657:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sourcesanspro.doc.tar.xz
Source658:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sourceserifpro.tar.xz
Source659:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sourceserifpro.doc.tar.xz
Source660:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spectral.tar.xz
Source661:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spectral.doc.tar.xz
Source662:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splentinex.tar.xz
Source663:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splentinex.doc.tar.xz
Source664:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/srbtiks.tar.xz
Source665:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/srbtiks.doc.tar.xz
Source666:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/starfont.tar.xz
Source667:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/starfont.doc.tar.xz
Source668:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/staves.tar.xz
Source669:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/staves.doc.tar.xz
Source670:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/step.tar.xz
Source671:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/step.doc.tar.xz
Source672:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stepgreek.tar.xz
Source673:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stepgreek.doc.tar.xz
Source674:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stickstoo.tar.xz
Source675:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stickstoo.doc.tar.xz
Source676:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stix.tar.xz
Source677:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stix.doc.tar.xz
Source678:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stix2-otf.tar.xz
Source679:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stix2-otf.doc.tar.xz
Source680:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stix2-type1.tar.xz
Source681:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stix2-type1.doc.tar.xz
Source682:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/superiors.tar.xz
Source683:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/superiors.doc.tar.xz
Source684:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svrsymbols.tar.xz
Source685:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svrsymbols.doc.tar.xz
Source686:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/symbats3.tar.xz
Source687:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/symbats3.doc.tar.xz
Source688:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tapir.tar.xz
Source689:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tapir.doc.tar.xz
Source690:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tempora.tar.xz
Source691:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tempora.doc.tar.xz
Source692:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tengwarscript.tar.xz
Source693:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tengwarscript.doc.tar.xz
Source694:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/termes-otf.tar.xz
Source695:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/termes-otf.doc.tar.xz
Source696:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tfrupee.tar.xz
Source697:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tfrupee.doc.tar.xz
Source698:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theanodidot.tar.xz
Source699:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theanodidot.doc.tar.xz
Source700:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theanomodern.tar.xz
Source701:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theanomodern.doc.tar.xz
Source702:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theanooldstyle.tar.xz
Source703:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theanooldstyle.doc.tar.xz
Source704:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tinos.tar.xz
Source705:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tinos.doc.tar.xz
Source706:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tpslifonts.tar.xz
Source707:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tpslifonts.doc.tar.xz
Source708:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trajan.tar.xz
Source709:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trajan.doc.tar.xz
Source710:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twemoji-colr.tar.xz
Source711:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twemoji-colr.doc.tar.xz
Source712:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txfontsb.tar.xz
Source713:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txfontsb.doc.tar.xz
Source714:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txuprcal.tar.xz
Source715:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txuprcal.doc.tar.xz
Source716:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typicons.tar.xz
Source717:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typicons.doc.tar.xz
Source718:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umtypewriter.tar.xz
Source719:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umtypewriter.doc.tar.xz
Source720:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/universa.tar.xz
Source721:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/universa.doc.tar.xz
Source722:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/universalis.tar.xz
Source723:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/universalis.doc.tar.xz
Source724:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uppunctlm.tar.xz
Source725:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uppunctlm.doc.tar.xz
Source726:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/urwchancal.tar.xz
Source727:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/urwchancal.doc.tar.xz
Source728:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/venturisadf.tar.xz
Source729:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/venturisadf.doc.tar.xz
Source730:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wsuipa.tar.xz
Source731:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wsuipa.doc.tar.xz
Source732:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcharter.tar.xz
Source733:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcharter.doc.tar.xz
Source734:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcharter-math.tar.xz
Source735:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcharter-math.doc.tar.xz
Source736:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xits.tar.xz
Source737:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xits.doc.tar.xz
Source738:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yfonts.tar.xz
Source739:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yfonts.doc.tar.xz
Source740:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yfonts-otf.tar.xz
Source741:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yfonts-otf.doc.tar.xz
Source742:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yfonts-t1.tar.xz
Source743:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yfonts-t1.doc.tar.xz
Source744:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yinit-otf.tar.xz
Source745:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yinit-otf.doc.tar.xz
Source746:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ysabeau.tar.xz
Source747:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ysabeau.doc.tar.xz
Source748:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zlmtt.tar.xz
Source749:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zlmtt.doc.tar.xz

# AppStream metadata for font components
Source750:        algolrevived.metainfo.xml
Source751:        almfixed.metainfo.xml
Source752:        antt.metainfo.xml
Source753:        asapsym.metainfo.xml
Source754:        baskervaldx.metainfo.xml
Source755:        baskervillef.metainfo.xml
Source756:        berenisadf.metainfo.xml
Source757:        beuron.metainfo.xml
Source758:        cabin.metainfo.xml
Source759:        ccicons.metainfo.xml
Source760:        chivo.metainfo.xml
Source761:        clara.metainfo.xml
Source762:        cm-unicode.metainfo.xml
Source763:        cochineal.metainfo.xml
Source764:        coelacanth.metainfo.xml
Source765:        comicneue.metainfo.xml
Source766:        countriesofeurope.metainfo.xml
Source767:        crimson.metainfo.xml
Source768:        cyklop.metainfo.xml
Source769:        dantelogo.metainfo.xml
Source770:        domitian.metainfo.xml
Source771:        drm.metainfo.xml
Source772:        erewhon.metainfo.xml
Source773:        erewhon-math.metainfo.xml
Source774:        etbb.metainfo.xml
Source775:        fbb.metainfo.xml
Source776:        fdsymbol.metainfo.xml
Source777:        fetamont.metainfo.xml
Source778:        firamath.metainfo.xml
Source779:        fonts-churchslavonic.metainfo.xml
Source780:        forum.metainfo.xml
Source781:        fourier.metainfo.xml
Source782:        frederika2016.metainfo.xml
Source783:        garamond-libre.metainfo.xml
Source784:        garamond-math.metainfo.xml
Source785:        gnu-freefont.metainfo.xml
Source786:        ibarra.metainfo.xml
Source787:        imfellenglish.metainfo.xml
Source788:        inriafonts.metainfo.xml
Source789:        iwona.metainfo.xml
Source790:        kurier.metainfo.xml
Source791:        libertinus-fonts.metainfo.xml
Source792:        librebodoni.metainfo.xml
Source793:        librecaslon.metainfo.xml
Source794:        librefranklin.metainfo.xml
Source795:        linguisticspro.metainfo.xml
Source796:        lobster2.metainfo.xml
Source797:        logix.metainfo.xml
Source798:        mdsymbol.metainfo.xml
Source799:        miama.metainfo.xml
Source800:        mintspirit.metainfo.xml
Source801:        missaali.metainfo.xml
Source802:        mnsymbol.metainfo.xml
Source803:        newcomputermodern.metainfo.xml
Source804:        newpx.metainfo.xml
Source805:        newtx.metainfo.xml
Source806:        nimbus15.metainfo.xml
Source807:        ocr-b-outline.metainfo.xml
Source808:        overlock.metainfo.xml
Source809:        phaistos.metainfo.xml
Source810:        playfair.metainfo.xml
Source811:        poltawski.metainfo.xml
Source812:        punknova.metainfo.xml
Source813:        qualitype.metainfo.xml
Source814:        rosario.metainfo.xml
Source815:        scholax.metainfo.xml
Source816:        semaphor.metainfo.xml
Source817:        step.metainfo.xml
Source818:        svrsymbols.metainfo.xml
Source819:        tempora.metainfo.xml
Source820:        txfontsb.metainfo.xml
Source821:        umtypewriter.metainfo.xml
Source822:        universalis.metainfo.xml
Source823:        xcharter.metainfo.xml
Source824:        xits.metainfo.xml
Source825:        yinit-otf.metainfo.xml

# Patches
Patch0:         texlive-droid-fixmono.patch

# Special license file
Source826:        yfonts-t1-license-email.pdf
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-aboensis
Requires:       texlive-academicons
Requires:       texlive-accanthis
Requires:       texlive-adforn
Requires:       texlive-adfsymbols
Requires:       texlive-aesupp
Requires:       texlive-alegreya
Requires:       texlive-alfaslabone
Requires:       texlive-algolrevived
Requires:       texlive-allrunes
Requires:       texlive-almendra
Requires:       texlive-almfixed
Requires:       texlive-andika
Requires:       texlive-anonymouspro
Requires:       texlive-antiqua
Requires:       texlive-antt
Requires:       texlive-archaic
Requires:       texlive-archivo
Requires:       texlive-arev
Requires:       texlive-arimo
Requires:       texlive-arsenal
Requires:       texlive-arsenal-math
Requires:       texlive-arvo
Requires:       texlive-asana-math
Requires:       texlive-asapsym
Requires:       texlive-ascii-font
Requires:       texlive-aspectratio
Requires:       texlive-astro
Requires:       texlive-atkinson
Requires:       texlive-augie
Requires:       texlive-auncial-new
Requires:       texlive-aurical
Requires:       texlive-b1encoding
Requires:       texlive-bahaistar
Requires:       texlive-barcodes
Requires:       texlive-baskervaldadf
Requires:       texlive-baskervaldx
Requires:       texlive-baskervillef
Requires:       texlive-bbding
Requires:       texlive-bbm
Requires:       texlive-bbm-macros
Requires:       texlive-bbold
Requires:       texlive-bbold-type1
Requires:       texlive-bboldx
Requires:       texlive-belleek
Requires:       texlive-bera
Requires:       texlive-berenisadf
Requires:       texlive-beuron
Requires:       texlive-bguq
Requires:       texlive-bitter
Requires:       texlive-blacklettert1
Requires:       texlive-boisik
Requires:       texlive-bonum-otf
Requires:       texlive-bookhands
Requires:       texlive-boondox
Requires:       texlive-braille
Requires:       texlive-brushscr
Requires:       texlive-cabin
Requires:       texlive-caladea
Requires:       texlive-calligra
Requires:       texlive-calligra-type1
Requires:       texlive-cantarell
Requires:       texlive-carlito
Requires:       texlive-carolmin-ps
Requires:       texlive-cascadia-code
Requires:       texlive-cascadiamono-otf
Requires:       texlive-ccicons
Requires:       texlive-cfr-initials
Requires:       texlive-cfr-lm
Requires:       texlive-charissil
Requires:       texlive-cherokee
Requires:       texlive-chivo
Requires:       texlive-cinzel
Requires:       texlive-clara
Requires:       texlive-clearsans
Requires:       texlive-cm-lgc
Requires:       texlive-cm-mf-extra-bold
Requires:       texlive-cm-unicode
Requires:       texlive-cmathbb
Requires:       texlive-cmbright
Requires:       texlive-cmexb
Requires:       texlive-cmll
Requires:       texlive-cmpica
Requires:       texlive-cmsrb
Requires:       texlive-cmtiup
Requires:       texlive-cmupint
Requires:       texlive-cochineal
Requires:       texlive-coelacanth
Requires:       texlive-collection-basic
Requires:       texlive-comfortaa
Requires:       texlive-comicneue
Requires:       texlive-concmath-fonts
Requires:       texlive-concmath-otf
Requires:       texlive-cookingsymbols
Requires:       texlive-cooperhewitt
Requires:       texlive-cormorantgaramond
Requires:       texlive-countriesofeurope
Requires:       texlive-courier-scaled
Requires:       texlive-courierten
Requires:       texlive-crimson
Requires:       texlive-crimsonpro
Requires:       texlive-cryst
Requires:       texlive-cuprum
Requires:       texlive-cyklop
Requires:       texlive-cyrillic-modern
Requires:       texlive-dancers
Requires:       texlive-dantelogo
Requires:       texlive-dejavu
Requires:       texlive-dejavu-otf
Requires:       texlive-dice
Requires:       texlive-dictsym
Requires:       texlive-dingbat
Requires:       texlive-domitian
Requires:       texlive-doublestroke
Requires:       texlive-doulossil
Requires:       texlive-dozenal
Requires:       texlive-drm
Requires:       texlive-droid
Requires:       texlive-dsserif
Requires:       texlive-duerer
Requires:       texlive-duerer-latex
Requires:       texlive-dutchcal
Requires:       texlive-ean
Requires:       texlive-ebgaramond
Requires:       texlive-ebgaramond-maths
Requires:       texlive-ecc
Requires:       texlive-eco
Requires:       texlive-eczar
Requires:       texlive-eiad
Requires:       texlive-eiad-ltx
Requires:       texlive-ektype-tanka
Requires:       texlive-electrumadf
Requires:       texlive-elvish
Requires:       texlive-epigrafica
Requires:       texlive-epsdice
Requires:       texlive-erewhon
Requires:       texlive-erewhon-math
Requires:       texlive-esrelation
Requires:       texlive-esstix
Requires:       texlive-esvect
Requires:       texlive-etbb
Requires:       texlive-euler-math
Requires:       texlive-eulervm
Requires:       texlive-euxm
Requires:       texlive-fbb
Requires:       texlive-fdsymbol
Requires:       texlive-fetamont
Requires:       texlive-feyn
Requires:       texlive-fge
Requires:       texlive-fira
Requires:       texlive-firamath
Requires:       texlive-firamath-otf
Requires:       texlive-foekfont
Requires:       texlive-fonetika
Requires:       texlive-fontawesome
Requires:       texlive-fontawesome5
Requires:       texlive-fontawesome6
Requires:       texlive-fontawesome7
Requires:       texlive-fontawesomescaled
Requires:       texlive-fontmfizz
Requires:       texlive-fonts-churchslavonic
Requires:       texlive-fontscripts
Requires:       texlive-forum
Requires:       texlive-fourier
Requires:       texlive-fouriernc
Requires:       texlive-frcursive
Requires:       texlive-frederika2016
Requires:       texlive-frimurer
Requires:       texlive-garamond-libre
Requires:       texlive-garamond-math
Requires:       texlive-gelasio
Requires:       texlive-gelasiomath
Requires:       texlive-genealogy
Requires:       texlive-gentium-otf
Requires:       texlive-gentium-sil
Requires:       texlive-gfsartemisia
Requires:       texlive-gfsbodoni
Requires:       texlive-gfscomplutum
Requires:       texlive-gfsdidot
Requires:       texlive-gfsdidotclassic
Requires:       texlive-gfsneohellenic
Requires:       texlive-gfsneohellenicmath
Requires:       texlive-gfssolomos
Requires:       texlive-gillcm
Requires:       texlive-gillius
Requires:       texlive-gnu-freefont
Requires:       texlive-gofonts
Requires:       texlive-gothic
Requires:       texlive-greenpoint
Requires:       texlive-grotesq
Requires:       texlive-gudea
Requires:       texlive-hacm
Requires:       texlive-hamnosys
Requires:       texlive-hands
Requires:       texlive-hep-font
Requires:       texlive-hep-math-font
Requires:       texlive-heros-otf
Requires:       texlive-heuristica
Requires:       texlive-hfbright
Requires:       texlive-hfoldsty
Requires:       texlive-hindmadurai
Requires:       texlive-ibarra
Requires:       texlive-ifsym
Requires:       texlive-imfellenglish
Requires:       texlive-inconsolata
Requires:       texlive-inconsolata-nerd-font
Requires:       texlive-initials
Requires:       texlive-inriafonts
Requires:       texlive-inter
Requires:       texlive-ipaex-type1
Requires:       texlive-iwona
Requires:       texlive-jablantile
Requires:       texlive-jamtimes
Requires:       texlive-jetbrainsmono-otf
Requires:       texlive-josefin
Requires:       texlive-juliamono
Requires:       texlive-junicode
Requires:       texlive-junicodevf
Requires:       texlive-kixfont
Requires:       texlive-kpfonts
Requires:       texlive-kpfonts-otf
Requires:       texlive-kurier
Requires:       texlive-lato
Requires:       texlive-lete-sans-math
Requires:       texlive-lexend
Requires:       texlive-lfb
Requires:       texlive-libertine
Requires:       texlive-libertinegc
Requires:       texlive-libertinus
Requires:       texlive-libertinus-fonts
Requires:       texlive-libertinus-otf
Requires:       texlive-libertinus-type1
Requires:       texlive-libertinust1math
Requires:       texlive-librebaskerville
Requires:       texlive-librebodoni
Requires:       texlive-librecaslon
Requires:       texlive-librefranklin
Requires:       texlive-libris
Requires:       texlive-lineara
Requires:       texlive-linguisticspro
Requires:       texlive-lobster2
Requires:       texlive-logix
Requires:       texlive-luciole
Requires:       texlive-luwiantype
Requires:       texlive-lxfonts
Requires:       texlive-ly1
Requires:       texlive-lydtype
Requires:       texlive-magra
Requires:       texlive-marcellus
Requires:       texlive-mathabx
Requires:       texlive-mathabx-type1
Requires:       texlive-mathdesign
Requires:       texlive-mdputu
Requires:       texlive-mdsymbol
Requires:       texlive-merriweather
Requires:       texlive-metsymb
Requires:       texlive-mfb-oldstyle
Requires:       texlive-miama
Requires:       texlive-mintspirit
Requires:       texlive-missaali
Requires:       texlive-mlmodern
Requires:       texlive-mnsymbol
Requires:       texlive-monaspace-otf
Requires:       texlive-montserrat
Requires:       texlive-mpfonts
Requires:       texlive-mweights
Requires:       texlive-newcomputermodern
Requires:       texlive-newpx
Requires:       texlive-newtx
Requires:       texlive-newtxsf
Requires:       texlive-newtxtt
Requires:       texlive-niceframe-type1
Requires:       texlive-nimbus15
Requires:       texlive-nkarta
Requires:       texlive-noto
Requires:       texlive-noto-emoji
Requires:       texlive-notomath
Requires:       texlive-nunito
Requires:       texlive-obnov
Requires:       texlive-ocherokee
Requires:       texlive-ocr-b
Requires:       texlive-ocr-b-outline
Requires:       texlive-ogham
Requires:       texlive-oinuit
Requires:       texlive-old-arrows
Requires:       texlive-oldlatin
Requires:       texlive-oldstandard
Requires:       texlive-opensans
Requires:       texlive-orkhun
Requires:       texlive-oswald
Requires:       texlive-overlock
Requires:       texlive-pacioli
Requires:       texlive-pagella-otf
Requires:       texlive-paratype
Requires:       texlive-pennstander-otf
Requires:       texlive-phaistos
Requires:       texlive-phonetic
Requires:       texlive-pigpen
Requires:       texlive-playfair
Requires:       texlive-plex
Requires:       texlive-plex-otf
Requires:       texlive-plimsoll
Requires:       texlive-poiretone
Requires:       texlive-poltawski
Requires:       texlive-prodint
Requires:       texlive-punk
Requires:       texlive-punk-latex
Requires:       texlive-punknova
Requires:       texlive-pxtxalfa
Requires:       texlive-qualitype
Requires:       texlive-quattrocento
Requires:       texlive-raleway
Requires:       texlive-recycle
Requires:       texlive-rit-fonts
Requires:       texlive-roboto
Requires:       texlive-romandeadf
Requires:       texlive-rosario
Requires:       texlive-rsfso
Requires:       texlive-ruscap
Requires:       texlive-sansmathaccent
Requires:       texlive-sansmathfonts
Requires:       texlive-sauter
Requires:       texlive-sauterfonts
Requires:       texlive-schola-otf
Requires:       texlive-scholax
Requires:       texlive-schulschriften
Requires:       texlive-semaphor
Requires:       texlive-shobhika
Requires:       texlive-simpleicons
Requires:       texlive-skull
Requires:       texlive-sourcecodepro
Requires:       texlive-sourcesanspro
Requires:       texlive-sourceserifpro
Requires:       texlive-spectral
Requires:       texlive-splentinex
Requires:       texlive-srbtiks
Requires:       texlive-starfont
Requires:       texlive-staves
Requires:       texlive-step
Requires:       texlive-stepgreek
Requires:       texlive-stickstoo
Requires:       texlive-stix
Requires:       texlive-stix2-otf
Requires:       texlive-stix2-type1
Requires:       texlive-superiors
Requires:       texlive-svrsymbols
Requires:       texlive-symbats3
Requires:       texlive-tapir
Requires:       texlive-tempora
Requires:       texlive-tengwarscript
Requires:       texlive-termes-otf
Requires:       texlive-tfrupee
Requires:       texlive-theanodidot
Requires:       texlive-theanomodern
Requires:       texlive-theanooldstyle
Requires:       texlive-tinos
Requires:       texlive-tpslifonts
Requires:       texlive-trajan
Requires:       texlive-twemoji-colr
Requires:       texlive-txfontsb
Requires:       texlive-txuprcal
Requires:       texlive-typicons
Requires:       texlive-umtypewriter
Requires:       texlive-universa
Requires:       texlive-universalis
Requires:       texlive-uppunctlm
Requires:       texlive-urwchancal
Requires:       texlive-venturisadf
Requires:       texlive-wsuipa
Requires:       texlive-xcharter
Requires:       texlive-xcharter-math
Requires:       texlive-xits
Requires:       texlive-yfonts
Requires:       texlive-yfonts-otf
Requires:       texlive-yfonts-t1
Requires:       texlive-yinit-otf
Requires:       texlive-ysabeau
Requires:       texlive-zlmtt

%description
Additional fonts


%package -n texlive-aboensis
Summary:        A late medieval OpenType cursive font
Version:        svn62977
License:        OFL-1.1 AND LPPL-1.3c AND CC-BY-4.0 AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(aboensis.sty) = %{tl_version}

%description -n texlive-aboensis
The package contains the free OpenType medieval cursive font Aboensis and a
style file to use it in XeLaTeX documents. The font is based on Codex Aboensis,
that is a law book written in Sweden in the 1430s. Since medieval cursive is
very difficult to read for modern people, the font is not suitable for use as
an ordinary book font, but is intended for emulating late medieval manuscripts.
The font contains two sets of initials: Lombardic and cursive to go with the
basic alphabet, and there is support for writing two-colored initials and
capitals. There are also a large number of abbreviation sigla that can be
accessed as ligature substitutions. The style file contains macros that help to
use the extended features of the font such as initials and two-colored
capitals. There are also macros to help achieve even pages with consistent line
spacing.

%package -n texlive-academicons
Summary:        Font containing high quality icons of online academic profiles
Version:        svn76366
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Provides:       tex(academicons-generic.tex) = %{tl_version}
Provides:       tex(academicons-pdftex.tex) = %{tl_version}
Provides:       tex(academicons-xeluatex.tex) = %{tl_version}
Provides:       tex(academicons.sty) = %{tl_version}

%description -n texlive-academicons
The academicons package provides access in (La)TeX to 146 high quality icons of
online academic profiles included in the free "Academicons" font. This package
works with both Xe(La)TeX or Lua(La)TeX by using fontspec to load the included
font, as well as with pdf(La)TeX by loading a Type 1 converted format of the
original font. The "Academicons" font was designed by James Walsh and released
(see http://jpswalsh.github.io/academicons/) under the open SIL Open Font
License. This package is a redistribution of the free "Academicons" font with
specific bindings for (La)TeX. It is inspired and based on the fontawesome
package. The generic \aiicon macro takes as mandatory argument the [?]name[?]
of the desired icon. Icons can also be accessed directly by their respective
macro. For example, \aiicon{googlescholar} yields the same result as
\aiGoogleScholar. The full list of icons with their respective names and direct
commands can be found in the manual.

%package -n texlive-accanthis
Summary:        Accanthis fonts, with LaTeX support
Version:        svn64844
License:        GPL-2.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(accanthis.sty) = %{tl_version}

%description -n texlive-accanthis
Accanthis No. 3 is designed by Hirwin Harendal and is suitable as an
alternative to fonts such as Garamond, Galliard, Horley old style, Sabon, and
Bembo. The support files are suitable for use with all LaTeX engines.

%package -n texlive-adforn
Summary:        OrnementsADF font with TeX/LaTeX support
Version:        svn74834
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(svn-prov.sty)
Provides:       tex(adforn.sty) = %{tl_version}

%description -n texlive-adforn
The bundle provides the Ornements ADF font in PostScript type 1 format with
TeX/LaTeX support files. The font is licensed under GPL v2 or later with font
exception. (See NOTICE, COPYING, README.) The TeX/LaTeX support is licensed
under LPPL. (See README, manifest.txt.)

%package -n texlive-adfsymbols
Summary:        SymbolsADF with TeX/LaTeX support
Version:        svn74819
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(svn-prov.sty)
Provides:       tex(adfarrows.sty) = %{tl_version}
Provides:       tex(adfbullets.sty) = %{tl_version}
Provides:       tex(adfsymbols-uni.tex) = %{tl_version}

%description -n texlive-adfsymbols
The package provides Arkandis foundry's ArrowsADF and BulletsADF fonts in Adobe
Type 1 format, together with TeX/LaTeX support files.

%package -n texlive-aesupp
Summary:        Special support for the ae character
Version:        svn58253
License:        LPPL-1.3c AND GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(aesupp.sty) = %{tl_version}

%description -n texlive-aesupp
This package provides special support for the italic 'ae' character in some
fonts, due to design flaws (in the author's opinion) regarding this character.
At the moment only the fonts TeX Gyre Bonum, TeX Gyre Schola, TeX Gyre Pagella,
and the Latin Modern fonts are supported. The other fonts in the TeX Gyre
bundle do not need this support.

%package -n texlive-alegreya
Summary:        Alegreya fonts with LaTeX support
Version:        svn75301
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(Alegreya.sty) = %{tl_version}
Provides:       tex(AlegreyaSans.sty) = %{tl_version}

%description -n texlive-alegreya
The Alegreya fonts are designed by Juan Pablo del Peral for Huerta Tipografica.
Alegreya is a typeface originally intended for literature. It conveys a dynamic
and varied rhythm which facilitates the reading of long texts. The italic has
just as much care and attention to detail in the design as the roman. Bold,
black, small caps and five number styles are available.

%package -n texlive-alfaslabone
Summary:        The Alfa Slab One font face with support for LaTeX and pdfLaTeX
Version:        svn57452
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(alfaslabone.sty) = %{tl_version}

%description -n texlive-alfaslabone
The alfaslabone package supports the Alfa Slab One font face for LaTeX. There
is only a Regular font face. It's useful for book-chapter headlines.

%package -n texlive-algolrevived
Summary:        A revival of Frutiger's Algol alphabet
Version:        svn71368
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(algolrevived.sty) = %{tl_version}

%description -n texlive-algolrevived
The package revives Frutiger's Algol alphabet, designed in 1963 for the code
segments in an ALGOL manual. OpenType and type1, regular and medium weights,
upright and slanted. Not monospaced, but good for listings if you don't need
code to be aligned with specific columns. It also makes a passable but limited
text font.

%package -n texlive-allrunes
Summary:        Fonts and LaTeX package for almost all runes
Version:        svn42221
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(allrunes.sty) = %{tl_version}

%description -n texlive-allrunes
This large collection of fonts (in Adobe Type 1 format), with the LaTeX package
gives access to almost all runes ever used in Europe. The bundle covers not
only the main forms but also a lot of varieties.

%package -n texlive-almendra
Summary:        Almendra fonts with LaTeX support
Version:        svn64539
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(almendra.sty) = %{tl_version}

%description -n texlive-almendra
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for the
Almendra family of fonts, designed by Ana Sanfelippo. Almendra is a typeface
design based on calligraphy. Its style is related to the chancery and gothic
hands. There are regular and bold weights with matching italics. There is also
a regular-weight small-caps.

%package -n texlive-almfixed
Summary:        Arabic-Latin Modern Fixed extends TeX-Gyre Latin Modern Mono 10 Regular to full Arabic Unicode support
Version:        svn35065
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-almfixed
Arabic-Latin Modern Fixed is an extension of TeX-Gyre Latin Modern Mono 10
Regular. Every glyph and OpenType feature of the Latin Modern Mono has been
retained, with minor improvements. On the other hand, we have changed the
vertical metrics of the font. Although the Arabic script is designed to use the
same x-size as Latin Modern Mono, the former script needs greater ascender and
descender space. Every Arabic glyph in each Unicode-code block is supported (up
to Unicode 7.0): Arabic, Arabic Supplement, Arabic Extended, Arabic
Presentation-Forms A, and Arabic Presentation-Forms B. There are two versions
of the font: otf and ttf. The ?penType version is for print applications (and
usually the default for TeX). The TrueType version is for on-screen
applications such as text editors. Hinting in the ttf version is much better
for on-screen, at least on Microsoft Windows. The unique feature of
Arabic-Latin Modern is its treatment of vowels and diacritics. Each vowel and
diacritic (ALM Fixed contains a total of 68 such glyphs) may now be edited
horizontally within any text editor or processor. The author believes this is
the very first OpenType Arabic font ever to have this capability. Editing
complex Arabic texts will now be much easier to input and to proofread.

%package -n texlive-andika
Summary:        Andika fonts with support for all LaTeX engines
Version:        svn64540
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(andika.sty) = %{tl_version}

%description -n texlive-andika
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Andika family of fonts designed by SIL International especially for literacy
use, taking into account the needs of beginning readers. The focus is on clear,
easy-to-perceive letterforms that will not be readily confused with one
another.

%package -n texlive-anonymouspro
Summary:        Use AnonymousPro fonts with LaTeX
Version:        svn51631
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(AnonymousPro.sty) = %{tl_version}

%description -n texlive-anonymouspro
The fonts are a monowidth set, designed for use by coders. They appear as a set
of four TrueType, or Adobe Type 1 font files, and LaTeX support is also
provided.

%package -n texlive-antiqua
Summary:        URW Antiqua condensed font, for use with TeX
Version:        svn24266
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-antiqua
The package contains a copy of the Type 1 font "URW Antiqua 2051 Regular
Condensed" released under the GPL by URW, with supporting files for use with
(La)TeX.

%package -n texlive-antt
Summary:        Antykwa Torunska: a Type 1 family of a Polish traditional type
Version:        svn18651
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(antt-math.tex) = %{tl_version}
Provides:       tex(anttor.sty) = %{tl_version}
Provides:       tex(antyktor.sty) = %{tl_version}

%description -n texlive-antt
Antykwa Torunska is a serif font designed by the late Polish typographer
Zygfryd Gardzielewski, reconstructed and digitized as Type 1.

%package -n texlive-archaic
Summary:        A collection of archaic fonts
Version:        svn38005
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(aramaic.sty) = %{tl_version}
Provides:       tex(cypriot.sty) = %{tl_version}
Provides:       tex(etruscan.sty) = %{tl_version}
Provides:       tex(greek4cbc.sty) = %{tl_version}
Provides:       tex(greek6cbc.sty) = %{tl_version}
Provides:       tex(hieroglf.sty) = %{tl_version}
Provides:       tex(linearb.sty) = %{tl_version}
Provides:       tex(nabatean.sty) = %{tl_version}
Provides:       tex(oands.sty) = %{tl_version}
Provides:       tex(oldprsn.sty) = %{tl_version}
Provides:       tex(phoenician.sty) = %{tl_version}
Provides:       tex(protosem.sty) = %{tl_version}
Provides:       tex(runic.sty) = %{tl_version}
Provides:       tex(sarabian.sty) = %{tl_version}
Provides:       tex(ugarite.sty) = %{tl_version}
Provides:       tex(viking.sty) = %{tl_version}

%description -n texlive-archaic
The collection contains fonts to represent Aramaic, Cypriot, Etruscan, Greek of
the 6th and 4th centuries BCE, Egyptian hieroglyphics, Linear A, Linear B,
Nabatean old Persian, the Phaistos disc, Phoenician, proto-Semitic, runic,
South Arabian Ugaritic and Viking scripts. The bundle also includes a small
font for use in phonetic transcription of the archaic writings. The bundle's
own directory includes a font installation map file for the whole collection.

%package -n texlive-archivo
Summary:        The Archivo font face with support for LaTeX and pdfLaTeX
Version:        svn57283
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(Archivo.sty) = %{tl_version}

%description -n texlive-archivo
This package provides the Archivo family of fonts designed by Omnibus-Type,
with support for LaTeX and pdfLaTeX.

%package -n texlive-arev
Summary:        Fonts and LaTeX support files for Arev Sans
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(beramono.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(ams-mdbch.sty) = %{tl_version}
Provides:       tex(arev.sty) = %{tl_version}
Provides:       tex(arevmath.sty) = %{tl_version}
Provides:       tex(arevsymbols.tex) = %{tl_version}
Provides:       tex(arevtext.sty) = %{tl_version}

%description -n texlive-arev
The package arev provides type 1 and virtual fonts, together with LaTeX
packages for using Arev Sans in both text and mathematics. Arev Sans is a
derivative of Bitstream Vera Sans created by Tavmjong Bah, adding support for
Greek and Cyrillic characters. Bah also added a few variant letters that are
more appropriate for mathematics. The primary purpose for using Arev Sans in
LaTeX is presentations, particularly when using a computer projector. In such a
context, Arev Sans is quite readable, with large x-height, "open letters", wide
spacing, and thick stems. The style is very similar to the SliTeX font lcmss,
but heavier. Arev is one of a very small number of sans-font mathematics
support packages. Others are cmbright, hvmath and kerkis.

%package -n texlive-arimo
Summary:        Arimo sans serif fonts with LaTeX support
Version:        svn68950
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(arimo.sty) = %{tl_version}

%description -n texlive-arimo
The Arimo family, designed by Steve Matteson, is an innovative, refreshing sans
serif design which is metrically compatible with Arial.

%package -n texlive-arsenal
Summary:        Open Type font by Andrij Shevchenko
Version:        svn77099
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(arsenal-math.sty)
Requires:       tex(fontspec.sty)
Provides:       tex(arsenal.sty) = %{tl_version}

%description -n texlive-arsenal
In 2011 Andrij's typeface became a winner of the Ukrainian Type Design
Competition "Mystetsky Arsenal" in which three main criteria were sought for:
being zeitgeist, practical, and Ukrainian. Andrij's winning entry was crowned
Arsenal and made publicly available. Arsenal is a semi-grotesque with
traditional forms. It is primarily designed for body text and intended for
various professional communication. Its special qualities of letter shapes and
subtle contrast modulation articulate grace and expressivity. Arsenal's
somewhat lyrical sentiment abides to the Ukrainian nature of the font. This
package provides the fonts and LaTeX support for them with matching math. It
needs LuaLaTeX or XeLaTeX.

%package -n texlive-arsenal-math
Summary:        Arsenal Math OpenType fonts
Version:        svn77272
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(arsenal-math.sty) = %{tl_version}

%description -n texlive-arsenal-math
Arsenal Math is a math companion font for the Arsenal text font. It is based on
KpMath-Sans, with Latin characters, numerals and a few symbols from the Arsenal
font. XeTeX or LuaTeX is required to use these OpenType math fonts.

%package -n texlive-arvo
Summary:        The Arvo font face with support for LaTeX and pdfLaTeX
Version:        svn57213
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(Arvo.sty) = %{tl_version}

%description -n texlive-arvo
This package provides the Arvo family of fonts designed by Anton Koovit, with
support for LaTeX and pdfLaTeX.

%package -n texlive-asana-math
Summary:        A font to typeset maths in Xe(La)TeX and Lua(La)TeX
Version:        svn76895
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-asana-math
The Asana-Math font is an OpenType font that includes almost all mathematical
Unicode symbols and it can be used to typeset mathematical text with any
software that can understand the MATH OpenType table (e.g., XeTeX 0.997 and
Microsoft Word 2007). The font is beta software. Typesetting support for use
with LaTeX is provided by the fontspec and unicode-math packages.

%package -n texlive-asapsym
Summary:        Using the free ASAP Symbol font with LaTeX and Plain TeX
Version:        svn40201
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(asapsym-generic.tex) = %{tl_version}
Provides:       tex(asapsym.code.tex) = %{tl_version}
Provides:       tex(asapsym.sty) = %{tl_version}

%description -n texlive-asapsym
The package provides macros (usable with LaTeX or Plain TeX) for using the
freely available ASAP Symbol font, which is also included. The font is
distributed in OpenType format, and makes extensive use of OpenType features.
Therefore, at this time, only XeTeX and LuaTeX are supported. An error message
is issued if an OTF-capable engine is not detected.

%package -n texlive-ascii-font
Summary:        Use the ASCII "font" in LaTeX
Version:        svn29989
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(ascii.sty) = %{tl_version}

%description -n texlive-ascii-font
The package provides glyph and font access commands so that LaTeX users can use
the ASCII glyphs in their documents. The ASCII font is encoded according to the
IBM PC Code Page 437 C0 Graphics. This package replaces any early LaTeX 2.09
package and "font" by R. Ramasubramanian and R.W.D. Nickalls.

%package -n texlive-aspectratio
Summary:        Capital A and capital R ligature for Aspect Ratio
Version:        svn25243
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ar.sty) = %{tl_version}

%description -n texlive-aspectratio
The package provides fonts (both as Adobe Type 1 format, and as Metafont
source) for the 'AR' symbol (for Aspect Ratio) used by aeronautical scientists
and engineers. Note that the package supersedes the package ar

%package -n texlive-astro
Summary:        Astronomical (planetary) symbols
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-astro
Astrosym is a font containing astronomical symbols, including those used for
the planets, four planetoids, the phases of the moon, the signs of the zodiac,
and some additional symbols. The font is distributed as Metafont source.

%package -n texlive-atkinson
Summary:        Support for the Atkinson Hyperlegible family of fonts
Version:        svn77391
License:        LicenseRef-AHFL AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(atkinson.sty) = %{tl_version}

%description -n texlive-atkinson
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Atkinson Hyperlegible family of fonts, named after Braille Institute founder,
J. Robert Atkinson. What makes it different from traditional typography design
is that it focuses on letterform distinction to increase character recognition,
ultimately improving readability.

%package -n texlive-augie
Summary:        Calligraphic font for typesetting handwriting
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-augie
A calligraphic font for simulating American-style informal handwriting. The
font is distributed in Adobe Type 1 format.

%package -n texlive-auncial-new
Summary:        Artificial Uncial font and LaTeX support macros
Version:        svn62977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(allauncl.sty) = %{tl_version}
Provides:       tex(auncial.sty) = %{tl_version}

%description -n texlive-auncial-new
The auncial-new bundle provides packages and fonts for a script based on the
Artificial Uncial manuscript book-hand used between the 6th & 10th century AD.
The script consists of minuscules and digits, with some appropriate period
punctuation marks. Both normal and bold versions are provided, and the font is
distributed in Adobe Type 1 format. This is an experimental new version of the
auncial bundle, which is one of a series of bookhand fonts. The font follows
the B1 encoding developed for bookhands. Access to the encoding is essential.
The encoding mainly follows the standard T1 encoding.

%package -n texlive-aurical
Summary:        Calligraphic fonts for use with LaTeX in T1 encoding
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(aurical.sty) = %{tl_version}

%description -n texlive-aurical
The package that implements a set (AuriocusKalligraphicus) of three
calligraphic fonts derived from the author's handwriting in Adobe Type 1
Format, T1 encoding for use with LaTeX: Auriocus Kalligraphicus; Lukas Svatba;
and Jana Skrivana. Each font features oldstyle digits and (machine-generated)
boldface and slanted versions. A variant of Lukas Svatba offers a 'long s'.

%package -n texlive-b1encoding
Summary:        LaTeX encoding tools for Bookhands fonts
Version:        svn21271
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(b1enc.def) = %{tl_version}

%description -n texlive-b1encoding
The package characterises and defines the author's B1 encoding for use with
LaTeX when typesetting things using his Bookhands fonts.

%package -n texlive-bahaistar
Summary:        Metafont source and macros for the Baha'i nine-pointed star
Version:        svn76351
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accsupp.sty)
Requires:       tex(newunicodechar.sty)
Provides:       tex(bahaistar.sty) = %{tl_version}

%description -n texlive-bahaistar
This package provides a Metafont-based implementation of the Baha'i
nine-pointed star [?] for usage in LaTeX documents, while still providing
proper copy behavior with the official Unicode codepoints and supporting the
usage of the character directly.

%package -n texlive-barcodes
Summary:        Fonts for making barcodes
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(barcodes.sty) = %{tl_version}

%description -n texlive-barcodes
The package deals with EAN barcodes; Metafont sources for fonts are provided,
and a set of examples; for some codes, a small Perl script is needed.

%package -n texlive-baskervaldadf
Summary:        Baskervald ADF fonts collection with TeX/LaTeX support
Version:        svn72484
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(baskervald.sty) = %{tl_version}

%description -n texlive-baskervaldadf
Baskervald ADF is a serif family with lining figures designed as a substitute
for Baskerville. The family currently includes upright and italic or oblique
shapes in each of regular, bold and heavy weights. All fonts include the
slashed zero and additional non-standard ligatures. The support package renames
them according to the Karl Berry fontname scheme and defines two families. One
of these primarily provides access to the "standard" or default characters
while the other supports additional ligatures. The included package files
provide access to these features in LaTeX.

%package -n texlive-baskervaldx
Summary:        Extension and modification of BaskervaldADF with LaTeX support
Version:        svn73362
License:        GPL-2.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(Baskervaldx.sty) = %{tl_version}

%description -n texlive-baskervaldx
Extends and modifies the BaskervaldADF font (a Baskerville substitute) with
more accented glyphs, with small caps and oldstyle figures in all shapes.
Includes OpenType and PostScript fonts, as well as LaTeX support files.

%package -n texlive-baskervillef
Summary:        Fry's Baskerville look-alike, with math support
Version:        svn73381
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(baskervillef.sty) = %{tl_version}

%description -n texlive-baskervillef
BaskervilleF is a fork from the Libre Baskerville fonts (Roman, Italic, Bold
only) released under the OFL by Paolo Impallari and Rodrigo Fuenzalida. Their
fonts are optimized for web usage, while BaskervilleF is optimized for
traditional TeX usage, normally destined for production of pdf files. A bold
italic style was added and mathematical support is offered as an option to
newtxmath.

%package -n texlive-bbding
Summary:        A symbol (dingbat) font and LaTeX macros for its use
Version:        svn17186
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bbding.sty) = %{tl_version}

%description -n texlive-bbding
A symbol font (distributed as Metafont source) that contains many of the
symbols of the Zapf dingbats set, together with an NFSS interface for using the
font. An Adobe Type 1 version of the fonts is available in the niceframe fonts
bundle.

%package -n texlive-bbm
Summary:        "Blackboard-style" cm fonts
Version:        svn15878
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bbm
Blackboard variants of Computer Modern fonts. The fonts are distributed as
Metafont source (only); LaTeX support is available with the bbm-macros package.
The Sauter font package has Metafont parameter source files for building the
fonts at more sizes than you could reasonably imagine. A sample of these fonts
appears in the blackboard bold sampler.

%package -n texlive-bbm-macros
Summary:        LaTeX support for "blackboard-style" cm fonts
Version:        svn17224
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bbm.sty) = %{tl_version}

%description -n texlive-bbm-macros
Provides LaTeX support for Blackboard variants of Computer Modern fonts.
Declares a font family bbm so you can in principle write running text in
blackboard bold, and lots of math alphabets for using the fonts within maths.

%package -n texlive-bbold
Summary:        Sans serif blackboard bold
Version:        svn17187
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bbold.sty) = %{tl_version}

%description -n texlive-bbold
A geometric sans serif blackboard bold font, for use in mathematics; Metafont
sources are provided, as well as macros for use with LaTeX. The Sauter font
package has Metafont parameter source files for building the fonts at more
sizes than you could reasonably imagine. See the blackboard sampler for a feel
for the font's appearance.

%package -n texlive-bbold-type1
Summary:        An Adobe Type 1 format version of the bbold font
Version:        svn33143
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bbold-type1
The files offer an Adobe Type 1 format version of the 5pt, 7pt and 10pt
versions of the bbold fonts. The distribution also includes a map file, for use
when incorporating the fonts into TeX documents; the macros provided with the
original Metafont version of the font serve for the scaleable version, too. The
fonts were produced to be part of the TeX distribution from Y&Y; they were
generously donated to the TeX Users Group when Y&Y closed its doors as a
business.

%package -n texlive-bboldx
Summary:        Extension of the bbold package with a Blackboard Bold alphabet
Version:        svn65424
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(bboldx.sty) = %{tl_version}

%description -n texlive-bboldx
Extension of bbold to a package with three weights, of which the original is
considered as light and the additions as regular and bold.

%package -n texlive-belleek
Summary:        Free replacement for basic MathTime fonts
Version:        svn66115
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-belleek
This package replaces the original MathTime fonts, not MathTime-Plus or
MathTime Professional (the last being the only currently available commercial
bundle).

%package -n texlive-bera
Summary:        Bera fonts
Version:        svn20031
License:        Bitstream-Vera
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(bera.sty) = %{tl_version}
Provides:       tex(beramono.sty) = %{tl_version}
Provides:       tex(berasans.sty) = %{tl_version}
Provides:       tex(beraserif.sty) = %{tl_version}

%description -n texlive-bera
The package contains the Bera Type 1 fonts, and a zip archive containing files
to use the fonts with LaTeX. Bera is a set of three font families: Bera Serif
(a slab-serif Roman), Bera Sans (a Frutiger descendant), and Bera Mono
(monospaced/typewriter). Support for use in LaTeX is also provided. The Bera
family is a repackaging, for use with TeX, of the Bitstream Vera family.

%package -n texlive-berenisadf
Summary:        Berenis ADF fonts and TeX/LaTeX support
Version:        svn72484
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(berenis.sty) = %{tl_version}

%description -n texlive-berenisadf
The bundle provides the BerenisADF Pro font collection, in OpenType and
PostScript Type 1 formats, together with support files to use the fonts in
TeXnANSI (LY1) and LaTeX standard T1 and TS1 encodings.

%package -n texlive-beuron
Summary:        The script of the Beuronese art school
Version:        svn46374
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(xparse.sty)
Provides:       tex(beuron.sty) = %{tl_version}

%description -n texlive-beuron
This package provides the script used in the works of the Beuron art school for
use with TeX and LaTeX. It is a monumental script consisting of capital letters
only. The fonts are provided as Metafont sources, in the Type1 and in the
OpenType format. The package includes suitable font selection commands for use
with LaTeX.

%package -n texlive-bguq
Summary:        Improved quantifier stroke for Begriffsschrift packages
Version:        svn27401
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(begriff-bguq.sty) = %{tl_version}
Provides:       tex(bguq.sty) = %{tl_version}

%description -n texlive-bguq
The font contains a single character: the Begriffsschrift quantifier (in
several sizes), as used to set the Begriffsschrift (concept notation) of Frege.
The font is not intended for end users; instead it is expected that it will be
used by other packages which implement the Begriffsschrift. An (unofficial)
modified version of Josh Parsons' begriff is included as an example of
implementation.

%package -n texlive-bitter
Summary:        The Bitter family of fonts with LaTeX support
Version:        svn67598
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(bitter.sty) = %{tl_version}

%description -n texlive-bitter
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for the
Bitter family of fonts, designed by Sol Matas for Huerta Tipografica. Bitter is
a contemporary slab-serif typeface for text. There are regular and bold weights
and an italic, but no bold italic.

%package -n texlive-blacklettert1
Summary:        T1-encoded versions of Haralambous old German fonts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-blacklettert1
This package contains virtual fonts that offer T1-alike encoded variants of
Yannis Haralambous's old German fonts Gothic, Schwabacher and Fraktur (which
are also available in Adobe type 1 format). The package includes LaTeX macros
to embed the fonts into the LaTeX font selection scheme.

%package -n texlive-boisik
Summary:        A font inspired by Baskerville design
Version:        svn15878
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(boisik.sty) = %{tl_version}
Provides:       tex(lblenc.def) = %{tl_version}
Provides:       tex(lbmenc.def) = %{tl_version}
Provides:       tex(lbsenc.def) = %{tl_version}

%description -n texlive-boisik
Boisik is a serif font set (inspired by the Baskerville typeface), written in
Metafont. The set comprises roman and italic text fonts and maths fonts. LaTeX
support is offered for use with OT1, IL2 and OM* encodings.

%package -n texlive-bonum-otf
Summary:        Support for the OpenType font Bonum
Version:        svn76342
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(bonum-otf.sty) = %{tl_version}

%description -n texlive-bonum-otf
Support for the OpenType font Bonum (text and math) of the TeXGyre Fonts.

%package -n texlive-bookhands
Summary:        A collection of book-hand fonts
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(allcmin.sty) = %{tl_version}
Provides:       tex(allegoth.sty) = %{tl_version}
Provides:       tex(allhmin.sty) = %{tl_version}
Provides:       tex(allhuncl.sty) = %{tl_version}
Provides:       tex(allimaj.sty) = %{tl_version}
Provides:       tex(allimin.sty) = %{tl_version}
Provides:       tex(allpgoth.sty) = %{tl_version}
Provides:       tex(allrtnd.sty) = %{tl_version}
Provides:       tex(allrust.sty) = %{tl_version}
Provides:       tex(allsqrc.sty) = %{tl_version}
Provides:       tex(alltgoth.sty) = %{tl_version}
Provides:       tex(alluncl.sty) = %{tl_version}
Provides:       tex(carolmin.sty) = %{tl_version}
Provides:       tex(egothic.sty) = %{tl_version}
Provides:       tex(humanist.sty) = %{tl_version}
Provides:       tex(huncial.sty) = %{tl_version}
Provides:       tex(inslrmaj.sty) = %{tl_version}
Provides:       tex(inslrmin.sty) = %{tl_version}
Provides:       tex(pgothic.sty) = %{tl_version}
Provides:       tex(rotunda.sty) = %{tl_version}
Provides:       tex(rustic.sty) = %{tl_version}
Provides:       tex(sqrcaps.sty) = %{tl_version}
Provides:       tex(tgothic.sty) = %{tl_version}
Provides:       tex(uncial.sty) = %{tl_version}

%description -n texlive-bookhands
This is a set of book-hand (Metafont) fonts and packages covering manuscript
scripts from the 1st century until Gutenberg and Caxton. The included hands
are: Square Capitals (1st century onwards); Roman Rustic (1st-6th centuries);
Insular Minuscule (6th century onwards); Carolingian Minuscule (8th-12th
centuries); Early Gothic (11th-12th centuries); Gothic Textura Quadrata
(13th-15th centuries); Gothic Textura Prescisus vel sine pedibus (13th century
onwards); Rotunda (13-15th centuries); Humanist Minuscule (14th century
onwards); Uncial (3rd-6th centuries); Half Uncial (3rd-9th centuries);
Artificial Uncial (6th-10th centuries); and Insular Majuscule (6th-9th
centuries).

%package -n texlive-boondox
Summary:        Mathematical alphabets derived from the STIX fonts
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(BOONDOX-cal.sty) = %{tl_version}
Provides:       tex(BOONDOX-calo.sty) = %{tl_version}
Provides:       tex(BOONDOX-ds.sty) = %{tl_version}
Provides:       tex(BOONDOX-frak.sty) = %{tl_version}
Provides:       tex(BOONDOX-uprscr.sty) = %{tl_version}

%description -n texlive-boondox
The package contains a number of PostScript fonts derived from the STIX
OpenType fonts that may be used in maths mode in regular and bold weights for
calligraphic, fraktur and double-struck alphabets. Virtual fonts with metrics
suitable for maths mode are provided, as are LaTeX support files.

%package -n texlive-braille
Summary:        Support for braille
Version:        svn20655
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(braille.sty) = %{tl_version}

%description -n texlive-braille
This package allows the user to produce Braille documents on paper for the
blind without knowing Braille (which can take years to learn). Python scripts
grade1.py and grade2.py convert ordinary text to grade 1 and 2 Braille tags;
then, the LaTeX package takes the tags and prints out corresponding Braille
symbols.

%package -n texlive-brushscr
Summary:        A handwriting script font
Version:        svn28363
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pbsi.sty) = %{tl_version}

%description -n texlive-brushscr
The BrushScript font simulates hand-written characters; it is distributed in
Adobe Type 1 format (but is available in italic shape only). The package
includes the files needed by LaTeX in order to use that font. The file
AAA_readme.tex fully describes the package and sample.tex illustrates its use.

%package -n texlive-cabin
Summary:        A humanist Sans Serif font, with LaTeX support
Version:        svn68373
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(cabin.sty) = %{tl_version}

%description -n texlive-cabin
Cabin is a humanist sans with four weights and true italics and small capitals.
According to the designer, Pablo Impallari, Cabin was inspired by Edward
Johnston's and Eric Gill's typefaces, with a touch of modernism. Cabin
incorporates modern proportions, optical adjustments, and some elements of the
geometric sans. cabin.sty supports use of the font under LaTeX, pdfLaTeX,
XeLaTeX and LuaLaTeX; it uses the mweights, to manage the user's view of all
those font weights. An sfdefault option is provided to enable Cabin as the
default text font. The fontaxes package is required for use with [pdf]LaTeX.

%package -n texlive-caladea
Summary:        Support for the Caladea family of fonts
Version:        svn64549
License:        Apache-2.0 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(caladea.sty) = %{tl_version}

%description -n texlive-caladea
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Caladea family of fonts, designed by Carolina Giovagnoli and Andres Torresi of
the Huerta Tipografica foundry and adopted by Google for ChromeOS as a
font-metric compatible replacement for Cambria.

%package -n texlive-calligra
Summary:        Calligraphic font
Version:        svn15878
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-calligra
A calligraphic font in the handwriting style of the author, Peter Vanroose. The
font is supplied as Metafont source. LaTeX support of the font is provided in
the calligra package in the fundus bundle.

%package -n texlive-calligra-type1
Summary:        Type 1 version of Calligra
Version:        svn24302
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-calligra-type1
This is a conversion (using mf2pt1) of Peter Vanroose's handwriting font.

%package -n texlive-cantarell
Summary:        LaTeX support for the Cantarell font family
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(cantarell.sty) = %{tl_version}

%description -n texlive-cantarell
Cantarell is a contemporary Humanist sans serif designed by Dave Crossland and
Jakub Steiner. This font, delivered under the OFL version 1.1, is available on
the GNOME download server. The present package provides support for this font
in LaTeX. It includes Type 1 versions of the fonts, converted for this package
using FontForge from its sources, for full support with Dvips.

%package -n texlive-carlito
Summary:        Support for Carlito sans-serif fonts
Version:        svn76790
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(carlito.sty) = %{tl_version}

%description -n texlive-carlito
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Carlito family of sans serif fonts, designed by Lukasz Dziedzic of the tyPoland
foundry and adopted by Google for ChromeOS as a font-metric compatible
replacement for Calibri.

%package -n texlive-carolmin-ps
Summary:        Adobe Type 1 format of Carolingian Minuscule fonts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-carolmin-ps
The bundle offers Adobe Type 1 format versions of Peter Wilson's Carolingian
Minuscule font set (part of the bookhands collection). The fonts in the bundle
are ready-to-use replacements for the Metafont originals.

%package -n texlive-cascadia-code
Summary:        The Cascadia Code font with support for LaTeX and pdfLaTeX
Version:        svn68485
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(cascadia-code.sty) = %{tl_version}

%description -n texlive-cascadia-code
Cascadia Code is a monospaced font by Microsoft. This package provides the
Cascadia Code family of fonts with support for LaTeX and pdfLaTeX. Adding
\usepackage{cascadia-code} to the preamble of your document will activate
Cascadia Code as the typewriter font (\ttdefault).

%package -n texlive-cascadiamono-otf
Summary:        Fontspec support for the OpenType font CascadiaMono
Version:        svn76343
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(cascadiamono-otf.sty) = %{tl_version}

%description -n texlive-cascadiamono-otf
Support for the OpenType font CascadiaMono (so with LuaLaTeX/XeTeX and
fontspec), which is a variant of CascadiaCode, but without ligatures.
\setmonofont{CascadiaMono} for regular version,
\setmonofont{CascadiaMono-SemiLight} for semilight version.
\setmonofont{CascadiaMono-Light} for light version,
\setmonofont{CascadiaMono-ExtraLight} for extralight version.

%package -n texlive-ccicons
Summary:        LaTeX support for Creative Commons icons
Version:        svn54512
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(ccicons.sty) = %{tl_version}

%description -n texlive-ccicons
The package provides the means to typeset Creative Commons icons, in documents
licensed under CC licences. A font (in Adobe Type 1 format) and LaTeX support
macros are provided.

%package -n texlive-cfr-initials
Summary:        LaTeX packages for use of initials
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(Acorn.sty) = %{tl_version}
Provides:       tex(AnnSton.sty) = %{tl_version}
Provides:       tex(ArtNouv.sty) = %{tl_version}
Provides:       tex(ArtNouvc.sty) = %{tl_version}
Provides:       tex(Carrickc.sty) = %{tl_version}
Provides:       tex(Eichenla.sty) = %{tl_version}
Provides:       tex(Eileen.sty) = %{tl_version}
Provides:       tex(EileenBl.sty) = %{tl_version}
Provides:       tex(Elzevier.sty) = %{tl_version}
Provides:       tex(GotIn.sty) = %{tl_version}
Provides:       tex(GoudyIn.sty) = %{tl_version}
Provides:       tex(Kinigcap.sty) = %{tl_version}
Provides:       tex(Konanur.sty) = %{tl_version}
Provides:       tex(Kramer.sty) = %{tl_version}
Provides:       tex(MorrisIn.sty) = %{tl_version}
Provides:       tex(Nouveaud.sty) = %{tl_version}
Provides:       tex(Romantik.sty) = %{tl_version}
Provides:       tex(Rothdn.sty) = %{tl_version}
Provides:       tex(Royal.sty) = %{tl_version}
Provides:       tex(Sanremo.sty) = %{tl_version}
Provides:       tex(Starburst.sty) = %{tl_version}
Provides:       tex(Typocaps.sty) = %{tl_version}
Provides:       tex(Zallman.sty) = %{tl_version}

%description -n texlive-cfr-initials
This is a set of 23 tiny packages designed to make it easier to use fonts from
the initials package in LaTeX, e.g. with the lettrine package. It is a response
to comments on an answer at TeX StackExchange requesting sample package files
for others to copy. I had previously assumed these were too trivial to be of
interest, but if they would be useful, then I would prefer them to be generally
available via CTAN.

%package -n texlive-cfr-lm
Summary:        Enhanced support for the Latin Modern fonts
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(cfr-lm.sty) = %{tl_version}

%description -n texlive-cfr-lm
The package supports a number of features of the Latin Modern fonts which are
not easily accessible via the default (La)TeX support provided in the official
distribution. In particular, the package supports the use of the various styles
of digits available, small-caps and upright italic shapes, and alternative
weights and widths. It also supports variable width typewriter and the
"quotation" font. Version 2.004 of the Latin Modern fonts is supported. By
default, the package uses proportional oldstyle digits and variable width
typewriter but this can be changed by passing appropriate options to the
package. The package also supports using (for example) different styles of
digits within a document so it is possible to use proportional oldstyle digits
by default, say, but tabular lining digits within a particular table. The
package requires the official Latin Modern distribution, including its (La)TeX
support. The package relies on the availability of both the fonts themselves
and the official font support files. The package also makes use of the
nfssext-cfr package. Only the T1 and TS1 encodings are supported for text
fonts. The set up of fonts for mathematics is identical to that provided by
Latin Modern.

%package -n texlive-charissil
Summary:        CharisSIL fonts with support for all LaTeX engines
Version:        svn64998
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(CharisSIL.sty) = %{tl_version}

%description -n texlive-charissil
This package provides the CharisSIL family of fonts adapted by SIL
International from Bitstream Charter in TrueType format, with support for
LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX.

%package -n texlive-cherokee
Summary:        A font for the Cherokee script
Version:        svn21046
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cherokee.sty) = %{tl_version}

%description -n texlive-cherokee
The Cherokee script was designed in 1821 by Segwoya. The alphabet is
essentially syllabic, only 6 characters (a e i o s u) correspond to Roman
letters: the font encodes these to the corresponding roman letter. The
remaining 79 characters have been arbitrarily encoded in the range 38-122; the
cherokee package provides commands that map each such syllable to the
appropriate character; for example, Segwoya himself would be represented
\Cse\Cgwo\Cya. The font is distributed as Metafont source; it works very poorly
in modern environments, and could do with expert attention (if you are
interested, please contact the CTAN team for details).

%package -n texlive-chivo
Summary:        Using the free Chivo fonts with LaTeX
Version:        svn65029
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(Chivo.sty) = %{tl_version}

%description -n texlive-chivo
This work provides the necessary files to use the Chivo fonts with LaTeX. Chivo
is a set of eight fonts provided by Hector Gatti & Omnibus Team under the Open
Font License (OFL), version 1.1. The fonts are copyright (c) 2011-2019,
Omnibus-Type.

%package -n texlive-cinzel
Summary:        LaTeX support for Cinzel and Cinzel Decorative fonts
Version:        svn64550
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(cinzel.sty) = %{tl_version}

%description -n texlive-cinzel
Cinzel and Cinzel Decorative fonts, designed by Natanael Gama Natanael Gama),
find their inspiration in first century roman inscriptions, and are based on
classical proportions. Cinzel is all-caps (similar to Trajan and Michelangelo),
but is available in three weights (Regular, Bold, Black). There are no italic
fonts, but there are Decorative variants, which can be selected by the usual
italic-selection commands in the package's LaTeX support.

%package -n texlive-clara
Summary:        A serif font family
Version:        svn75301
License:        OFL-1.1 AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(clara.sty) = %{tl_version}

%description -n texlive-clara
Clara is a type family created specially by Seamas O Brogain for printing A
Dictionary of Editing (2015). The family includes italic, bold, bold italic,
and small capitals, while the character set includes (monotonic) Greek,
Cyrillic, ogham, phonetic and mathematical ranges, scribal abbreviations and
other specialist characters. The fonts also include some OpenType features
(such as ligature substitution, small capitals, and old-style numerals) and
variant forms for particular languages.

%package -n texlive-clearsans
Summary:        Clear Sans fonts with LaTeX support
Version:        svn74767
License:        Apache-2.0 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(ClearSans.sty) = %{tl_version}

%description -n texlive-clearsans
Clear Sans was designed by Daniel Ratighan at Monotype under the direction of
the User Experience team at Intel's Open Source Technology Center. Clear Sans
is available in three weights (regular, medium, and bold) with corresponding
italics, plus light and thin upright (without italics). Clear Sans has
minimized, unambiguous characters and slightly narrow proportions, making it
ideal for UI design. Its strong, recognizable forms avoid distracting
ambiguity, making Clear Sans comfortable for reading short UI labels and long
passages in both screen and print. The fonts are available in both TrueType and
Type 1 formats.

%package -n texlive-cm-lgc
Summary:        Type 1 CM-based fonts for Latin, Greek and Cyrillic
Version:        svn28250
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(antcmlgc.sty) = %{tl_version}
Provides:       tex(cmlgc.sty) = %{tl_version}

%description -n texlive-cm-lgc
The fonts are converted from Metafont sources of the Computer Modern font
families, using textrace. Supported encodings are: T1 (Latin), T2A (Cyrillic),
LGR (Greek) and TS1. The package also includes Unicode virtual fonts for use
with Omega. The font set is not a replacement for any of the other Computer
Modern-based font sets (for example, cm-super for Latin and Cyrillic, or
cbgreek for Greek), since it is available at a single size only; it offers a
compact set for 'general' working. The fonts themselves are encoded to external
standards, and virtual fonts are provided for use with TeX.

%package -n texlive-cm-mf-extra-bold
Summary:        Extra Metafont files for CM
Version:        svn54512
License:        GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cm-mf-extra-bold
The bundle provides bold versions of cmcsc, cmex, cmtex and cmtt fonts (all
parts of the standard computer modern font distribution), as Metafont base
files.

%package -n texlive-cm-unicode
Summary:        Computer Modern Unicode font family
Version:        svn58661
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cm-unicode
Computer Modern Unicode fonts, converted from Metafont sources using mftrace
with autotrace backend and fontforge. Some characters in several fonts are
copied from Blue Sky type 1 fonts released by AMS. Currently the fonts contain
glyphs from Latin (Metafont ec, tc, vnr), Cyrillic (lh), Greek (cbgreek when
available) code sets and IPA extensions (from tipa). This font set contains 33
fonts. This archive contains AFM, PFB and OTF versions; the OTF version of the
Computer Modern Unicode fonts works with TeX engines that directly support
OpenType features, such as XeTeX and LuaTeX.

%package -n texlive-cmathbb
Summary:        Computer modern mathematical blackboard bold font
Version:        svn56414
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Provides:       tex(cmathbb.sty) = %{tl_version}

%description -n texlive-cmathbb
This font contains all digits and latin letters uppercase and lowercase for the
Computer Modern font family in blackboard bold.

%package -n texlive-cmbright
Summary:        Computer Modern Bright fonts
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cmbright.sty) = %{tl_version}

%description -n texlive-cmbright
A family of sans serif fonts for TeX and LaTeX, based on Donald Knuth's CM
fonts. It comprises OT1, T1 and TS1 encoded text fonts of various shapes as
well as all the fonts necessary for mathematical typesetting, including AMS
symbols. This collection provides all the necessary files for using the fonts
with LaTeX. Free versions are available, in the cm-super font bundle (the T1
and TS1 encoded part of the set), and in the hfbright package (the OT1 encoded
part, and the maths fonts).

%package -n texlive-cmexb
Summary:        Cmexb10 metrics and Type 1
Version:        svn54074
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmexb
Computer Modern Math Extension bold, metrics and .pfb file. Made by Petr Olsak
via autotracing.

%package -n texlive-cmll
Summary:        Symbols for linear logic
Version:        svn17964
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
Provides:       tex(cmll.sty) = %{tl_version}

%description -n texlive-cmll
This is a very small font set that contain some symbols useful in linear logic,
which are apparently not available elsewhere. Variants are included for use
with Computer Modern serif and sans-serif and with the AMS Euler series. The
font is provided both as Metafont source, and in Adobe Type 1 format. LaTeX
support is provided.

%package -n texlive-cmpica
Summary:        A Computer Modern Pica variant
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmpica
An approximate equivalent of the Xerox Pica typeface; the font is optimised for
submitting fiction manuscripts to mainline publishers. The font is a
fixed-width one, rather less heavy than Computer Modern typewriter. Emphasis
for bold-face comes from a wavy underline of each letter. The two fonts are
supplied as Metafont source.

%package -n texlive-cmsrb
Summary:        Computer Modern for Serbian and Macedonian
Version:        svn76790
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(cmupint.sty)
Provides:       tex(cmsrb.sty) = %{tl_version}
Provides:       tex(ecmsrb1enc.def) = %{tl_version}
Provides:       tex(ecmsrb2enc.def) = %{tl_version}

%description -n texlive-cmsrb
This package provides Adobe Type 1 Computer Modern fonts for the Serbian and
Macedonian languages. Although the cm-super package provides great support for
cyrillic script in various languages, there remains a problem with italic
variants of some letters for Serbian and Macedonian. This package includes the
correct shapes for italic letters \cyrb, \cyrg, \cyrd, \cyrp, and \cyrt. It
also offers some improvements in letters and accents used in the Serbian
language. Supported encodings are: T1, T2A, TS1, X2 and OT2. The OT2 encoding
is modified so that it is now easy to transcribe Latin text to Cyrillic.

%package -n texlive-cmtiup
Summary:        Upright punctuation with CM italic
Version:        svn77050
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cmtiup.sty) = %{tl_version}

%description -n texlive-cmtiup
The cmtiup fonts address a problem with the appearance of punctuation in italic
text in mathematical documents. To achieve this, all punctuation characters are
upright, and kerning between letters and punctuation is adjusted to allow for
the italic correction. The fonts are implemented as a set of vf files; a
package for support in LaTeX2e is provided.

%package -n texlive-cmupint
Summary:        Upright integral symbols for Computer Modern
Version:        svn54735
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cmupint.sty) = %{tl_version}

%description -n texlive-cmupint
This package contains various upright integral symbols to match the Computer
Modern font.

%package -n texlive-cochineal
Summary:        Cochineal fonts with LaTeX support
Version:        svn70528
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(realscripts.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cochineal.sty) = %{tl_version}

%description -n texlive-cochineal
Cochineal is a fork from the Crimson fonts (Roman, Italic, Bold, BoldItalic
only) released under the OFL by Sebastian Kosch. These remarkable fonts are
inspired by the famous oldstyle fonts in the garalde family (Garamond, Bembo)
but, in the end, look more similar to Minion, though with smaller xheight and
less plain in detail. The Crimson fonts on which these were based had roughly
4200 glyphs in the four styles mentioned above. Cochineal adds more than 1500
glyphs in those styles so that it is possible to make a TeX support collection
that contains essentially all glyphs in all styles. Bringing the Semibold
styles up the same level would have required adding about 2000 additional
glyphs, which I could not even contemplate. The fonts are provided in OpenType
and PostScript formats.

%package -n texlive-coelacanth
Summary:        Coelacanth fonts with LaTeX support
Version:        svn64558
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(coelacanth.sty) = %{tl_version}

%description -n texlive-coelacanth
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
Coelecanth fonts, designed by Ben Whitmore. Coelacanth is inspired by the
classic Centaur type design of Bruce Rogers, described by some as the most
beautiful typeface ever designed. It aims to be a professional quality type
family for general book typesetting.

%package -n texlive-comfortaa
Summary:        Sans serif font, with LaTeX support
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(comfortaa.sty) = %{tl_version}

%description -n texlive-comfortaa
Comfortaa is a sans-serif font, comfortable in every aspect, designed by Johan
Aakerlund. The font, which includes three weights (thin, regular and bold), is
available on Johan's deviantArt web page as TrueType files under the Open Font
License version 1.1. This package provides support for this font in LaTeX, and
includes both the TrueType fonts, and conversions to Adobe Type 1 format.

%package -n texlive-comicneue
Summary:        Use Comic Neue with TeX(-alike) systems
Version:        svn54891
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(mweights.sty)
Requires:       tex(xparse.sty)
Provides:       tex(comicneue.sty) = %{tl_version}

%description -n texlive-comicneue
Comic Neue is a well-known redesign of the (in)famous Comic Sans font. The
package provides the original OpenType font for XeTeX and LuaTeX users, and
also has converted Type1 files for pdfTeX users. Issues with this package can
be reported on GitHub or emailed to tex@slxh.nl.

%package -n texlive-concmath-fonts
Summary:        Concrete mathematics fonts
Version:        svn17218
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-concmath-fonts
The fonts are derived from the computer modern mathematics fonts and from
Knuth's Concrete Roman fonts; they are distributed as Metafont source. LaTeX
support is offered by the concmath package.

%package -n texlive-concmath-otf
Summary:        Concrete based OpenType Math font
Version:        svn76683
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(concmath-otf.sty) = %{tl_version}

%description -n texlive-concmath-otf
This package provides an OpenType version of the Concrete Math font created by
Ulrik Vieth in Metafont. "concmath-otf.sty" is a replacement for the original
"concmath.sty" package to be used with LuaTeX or XeTeX engines.

%package -n texlive-cookingsymbols
Summary:        Symbols for recipes
Version:        svn74247
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cookingsymbols.sty) = %{tl_version}

%description -n texlive-cookingsymbols
The package provides 11 symbols for typesetting recipes: oven, gasstove,
topheat, fanoven, gloves and dish symbol (among others). The symbols are
defined using Metafont.

%package -n texlive-cooperhewitt
Summary:        LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the Cooper Hewitt family of sans serif fonts
Version:        svn64967
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(CooperHewitt.sty) = %{tl_version}

%description -n texlive-cooperhewitt
Cooper Hewitt is a contemporary sans serif, with characters composed of
modified-geometric curves and arches. Initially commissioned by Pentagram to
evolve his Polaris Condensed typeface, Chester Jenkins created a new digital
form to support the newly transformed Smithsonian Design Museum.

%package -n texlive-cormorantgaramond
Summary:        Cormorant Garamond family of fonts
Version:        svn71057
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(CormorantGaramond.sty) = %{tl_version}

%description -n texlive-cormorantgaramond
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Cormorant Garamond family of fonts, designed by Christian Thalman of Catharsis
Fonts. The family includes light, regular, medium, semi-bold, and bold weights,
with italics.

%package -n texlive-countriesofeurope
Summary:        A font with the images of the countries of Europe
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(countriesofeurope.sty) = %{tl_version}

%description -n texlive-countriesofeurope
The bundle provides a font "CountriesOfEurope" (in Adobe Type 1 format) and the
necessary metrics, together with LaTeX macros for its use. The font provides
glyphs with a filled outline of the shape of each country; each glyph is at the
same cartographic scale.

%package -n texlive-courier-scaled
Summary:        Provides a scaled Courier font
Version:        svn24940
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(couriers.sty) = %{tl_version}

%description -n texlive-courier-scaled
This package sets the default typewriter font to Courier with a possible scale
factor (in the same way as the helvet package for Helvetica works for sans
serif).

%package -n texlive-courierten
Summary:        Courier 10 Pitch BT with LaTeX support
Version:        svn55436
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(courierten.sty) = %{tl_version}

%description -n texlive-courierten
This is the font Courier 10 Pitch BT, with LaTeX support and an OpenType
conversion as well.

%package -n texlive-crimson
Summary:        Crimson fonts with LaTeX support
Version:        svn75712
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(crimson.sty) = %{tl_version}

%description -n texlive-crimson
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for the
Crimson family of fonts, designed by Sebastian Kosch. The Crimson family is for
book production in the tradition of beautiful oldstyle typefaces, inspired
particularly by the work of people like Jan Tschichold (Sabon), Robert Slimbach
(Arno, Minion), and Jonathan Hoefler (Hoefler Text). Small caps and old-style
numerals are mostly available, except old-style numerals are not supported in
Bold or Semibold.

%package -n texlive-crimsonpro
Summary:        CrimsonPro fonts with LaTeX support
Version:        svn64565
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(CrimsonPro.sty) = %{tl_version}

%description -n texlive-crimsonpro
The CrimsonPro fonts are designed by Jacques Le Bailly and derived from the
Crimson Text fonts designed by Sebastian Kosch. The family includes eight
weights and italics for each weight.

%package -n texlive-cryst
Summary:        Font for graphical symbols used in crystallography
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cryst
The font is provided as an Adobe Type 1 font, and as Metafont source.
Instructions for use are available both in the README file and (with a font
diagram) in the documentation.

%package -n texlive-cuprum
Summary:        Cuprum font family support for LaTeX
Version:        svn49909
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cuprum.sty) = %{tl_version}

%description -n texlive-cuprum
This package provides support for the Cuprum font family (see
http://jovanny.ru).

%package -n texlive-cyklop
Summary:        The Cyclop typeface
Version:        svn77161
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cyklop.sty) = %{tl_version}

%description -n texlive-cyklop
The Cyclop typeface was designed in the 1920s at the workshop of Warsaw type
foundry "Odlewnia Czcionek J. Idzkowski i S-ka". This sans serif typeface has a
highly modulated stroke so it has high typographic contrast. The vertical stems
are much heavier then horizontal ones. Most characters have thin rectangles as
additional counters giving the unique shape of the characters. The lead types
of Cyclop typeface were produced in slanted variant at sizes 8-48 pt. It was
heavily used for heads in newspapers and accidents prints. Typesetters used
Cyclop in the inter-war period, during the occupation in the underground press.
The typeface was used until the beginnings of the offset print and computer
typesetting era. Nowadays it is hard to find the metal types of this typeface.
The font was generated using the Metatype1 package. Then the original set of
characters was completed by adding the full set of accented letters and
characters of the modern Latin alphabets (including Vietnamese). The upright
variant was generated and it was more complicated task than it appeared at the
beginning. 11 upright letters of the Cyclop typeface were presented in the book
by Filip Trzaska, "Podstawy techniki wydawniczej" ("Foundation of the
publishing technology"), Warsaw 1967. But even the author of the book does not
know what was the source of the presented examples. The fonts are distributed
in the Type1 and OpenType formats along with the files necessary for use these
fonts in TeX and LaTeX including encoding definition files: T1 (ec), T5
(Vietnamese), OT4, QX, texnansi and nonstandard ones (IL2 for Czech fonts).

%package -n texlive-cyrillic-modern
Summary:        Slightly modified computer modern fonts with Cyrillics
Version:        svn71183
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ls2enc.def) = %{tl_version}
Provides:       tex(nm.sty) = %{tl_version}

%description -n texlive-cyrillic-modern
The Cyrillic Modern fonts are based on the Computer Modern fonts designed in
Metafont by D. E. Knuth and released in Type 1 format by the American
Mathematical Society under the SIL Open Font License (OFL). The Cyrillic Modern
fonts are intended to make the Cyrillic letters with classical shapes typical
to the modern fonts. Currently, the fonts add support for the Russian language,
the numero sign and quotation marks required for Russian typesetting.

%package -n texlive-dancers
Summary:        Font for Conan Doyle's "The Dancing Men"
Version:        svn13293
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dancers
The (Sherlock Holmes) book contains a code which uses dancing men as glyphs.
The alphabet as given is not complete, lacking f, j, k, q, u, w, x and z, so
those letters in the font are not due to Conan Doyle. The code required word
endings to be marked by the dancing man representing the last letter to be
holding a flag: these are coded as A-Z.
thaTiStOsaYsentenceSiNthEcodElooKlikEthiS. In some cases, the man has no arms,
making it impossible for him to hold a flag. In these cases, he is wearing a
flag on his hat in the 'character'. The font is distributed as Metafont source;
it works poorly in modern environments, and could do with expert attention (if
you are interested, please contact the CTAN team for details).

%package -n texlive-dantelogo
Summary:        A font for DANTE's logo
Version:        svn38599
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Provides:       tex(dantelogo.sty) = %{tl_version}

%description -n texlive-dantelogo
The DANTE font for the logo of DANTE (http://www.dante.de), the German speaking
TeX users group. The font includes only the five characters d, a, n, t, and e.
dantelogo.sty provides an interface for LuaLaTeX/XeLaTeX/pdfLaTeX.

%package -n texlive-dejavu
Summary:        LaTeX support for the DejaVu fonts
Version:        svn31771
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(DejaVuSans.sty) = %{tl_version}
Provides:       tex(DejaVuSansCondensed.sty) = %{tl_version}
Provides:       tex(DejaVuSansMono.sty) = %{tl_version}
Provides:       tex(DejaVuSerif.sty) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed.sty) = %{tl_version}
Provides:       tex(dejavu.sty) = %{tl_version}

%description -n texlive-dejavu
The package contains LaTeX support for the DejaVu fonts, which are derived from
the Vera fonts but contain more characters and styles. The fonts are included
in the original TrueType format, and in converted Type 1 format. The
(currently) supported encodings are: OT1, T1, IL2, TS1, T2*, X2, QX, and LGR.
The package doesn't (currently) support mathematics. More encodings and/or
features are expected.

%package -n texlive-dejavu-otf
Summary:        Support for the ttf and otf DejaVu fonts
Version:        svn75301
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(dejavu-otf.sty) = %{tl_version}

%description -n texlive-dejavu-otf
This package supports the free ttf-fonts from the DejaVu project which are
available from GitHub or already part of your system (Windows/Linux/...), and
the OpenType version of TeXGyre Math, which is part of any TeX distribution.
The following font files are supported: DejaVuSans-BoldOblique.ttf
DejaVuSans-Bold.ttf DejaVuSansCondensed-BoldOblique.ttf
DejaVuSansCondensed-Bold.ttf DejaVuSansCondensed-Oblique.ttf
DejaVuSansCondensed.ttf DejaVuSans-ExtraLight.ttf
DejaVuSansMono-BoldOblique.ttf DejaVuSansMono-Bold.ttf
DejaVuSansMono-Oblique.ttf DejaVuSansMono.ttf DejaVuSans-Oblique.ttf
DejaVuSans.ttf DejaVuSerif-BoldItalic.ttf DejaVuSerif-Bold.ttf
DejaVuSerifCondensed-BoldItalic.ttf DejaVuSerifCondensed-Bold.ttf
DejaVuSerifCondensed-Italic.ttf DejaVuSerifCondensed.ttf DejaVuSerif-Italic.ttf
DejaVuSerif.ttf texgyredejavu-math.otf

%package -n texlive-dice
Summary:        A font for die faces
Version:        svn28501
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dice
A Metafont font that can produce die faces in 2D or with various 3D effects.

%package -n texlive-dictsym
Summary:        DictSym font and macro package
Version:        svn69720
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(pifont.sty)
Provides:       tex(dictsym.sty) = %{tl_version}

%description -n texlive-dictsym
This directory contains the DictSym Type1 font designed by Georg Verweyen and
all files required to use it with LaTeX on the Unix or PC platforms. The font
provides a number of symbols commonly used in dictionaries. The accompanying
macro package makes the symbols accessible as LaTeX commands.

%package -n texlive-dingbat
Summary:        Two dingbat symbol fonts
Version:        svn27918
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dingbat.sty) = %{tl_version}

%description -n texlive-dingbat
The fonts (ark10 and dingbat) are specified in Metafont; support macros are
provided for use in LaTeX. An Adobe Type 1 version of the fonts is available in
the niceframe fonts bundle.

%package -n texlive-domitian
Summary:        Drop-in replacement for Palatino
Version:        svn55286
License:        AGPL-3.0-or-later WITH PS-or-PDF-font-exception-20170817 OR LPPL-1.3c OR OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(domitian.sty) = %{tl_version}

%description -n texlive-domitian
The Domitian fonts are a free and open-source OpenType font family, based on
the Palatino design by Hermann Zapf (1918-2015), as implemented in Palladio,
the version distributed as part of URW's free Core 35 PostScript fonts (2.0).
Domitian is meant as a drop-in replacement for Adobe's version of Palatino. It
extends Palladio with small capitals, old-style figures and scientific
inferiors. The metrics have been adjusted to more closely match Adobe Palatino,
and hinting has been improved.

%package -n texlive-doublestroke
Summary:        Typeset mathematical double stroke symbols
Version:        svn15878
License:        LicenseRef-DoubleStroke
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dsfont.sty) = %{tl_version}

%description -n texlive-doublestroke
A font based on Computer Modern Roman useful for typesetting the mathematical
symbols for the natural numbers (N), whole numbers (Z), rational numbers (Q),
real numbers (R) and complex numbers (C); coverage includes all Roman capital
letters, '1', 'h' and 'k'. The font is available both as Metafont source and in
Adobe Type 1 format, and LaTeX macros for its use are provided. The fonts
appear in the blackboard bold sampler.

%package -n texlive-doulossil
Summary:        A font for typesetting the International Phonetic Alphabet (IPA)
Version:        svn63255
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-doulossil
This package provides the IPA font Doulos SIL in TrueType format.

%package -n texlive-dozenal
Summary:        Typeset documents using base twelve numbering (also called "dozenal")
Version:        svn75722
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(mfirstuc.sty)
Requires:       tex(xstring.sty)
Provides:       tex(dozenal.sty) = %{tl_version}

%description -n texlive-dozenal
The package supports typesetting documents whose counters are represented in
base twelve, also called "dozenal". It includes a macro by David Kastrup for
converting positive whole numbers to dozenal from decimal (base ten)
representation. The package also includes a few other macros and redefines all
the standard counters to produce dozenal output. Fonts, in Roman, italic,
slanted, and boldface versions, provide ten and eleven (the Pitman characters
preferred by the Dozenal Society of Great Britain). The fonts were designed to
blend well with the Computer Modern fonts, and are available both as Metafont
source and in Adobe Type 1 format.

%package -n texlive-drm
Summary:        A complete family of fonts written in Metafont
Version:        svn38157
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(gmp.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(modroman.sty)
Provides:       tex(drm.sty) = %{tl_version}

%description -n texlive-drm
The package provides access to the DRM (Don's Revised Modern) family of fonts,
which includes a variety of optical sizes in Roman (in four weights), italic,
and small caps, among other shapes, along with a set of symbols and ornaments.
It is intended to be a full-body text font, but its larger sizes can also be
used for simple display purposes, and its significant body of symbols can stand
on its own. It comes complete with textual ("old-style") and lining figures,
and even has small-caps figures. It also comes with extensible decorative rules
to be used with ornaments from itself or other fonts, along with an extremely
flexible ellipsis package.

%package -n texlive-droid
Summary:        LaTeX support for the Droid font families
Version:        svn54512
License:        LPPL-1.3c AND Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(droidsansmono.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(droid.sty) = %{tl_version}
Provides:       tex(droidsans.sty) = %{tl_version}
Provides:       tex(droidsansmono.sty) = %{tl_version}
Provides:       tex(droidserif.sty) = %{tl_version}

%description -n texlive-droid
The Droid typeface family was designed in the fall of 2006 by Steve Matteson,
as a commission from Google to create a set of system fonts for its Android
platform. The goal was to provide optimal quality and comfort on a mobile
handset when rendered in application menus, web browsers and for other screen
text. The Droid family consists of Droid Serif, Droid Sans and Droid Sans Mono
fonts, licensed under the Apache License Version 2.0. The bundle includes the
fonts in both TrueType and Adobe Type 1 formats. The package does not support
the Droid Pro family of fonts, available for purchase from the Ascender
foundry.

%package -n texlive-dsserif
Summary:        A double-struck serifed font for mathematical use
Version:        svn60898
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(dsserif.sty) = %{tl_version}

%description -n texlive-dsserif
DSSerif is a mathematical font package with double struck serifed digits, upper
and lower case letters, in regular and bold weights. The design was inspired by
the STIX double struck fonts, which are sans serif, but starting from a
Courier-like base.

%package -n texlive-duerer
Summary:        Computer Duerer fonts
Version:        svn20741
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-duerer
These fonts are designed for titling use, and consist of capital roman letters
only. Together with the normal set of base shapes, the family also offers an
informal shape. The distribution is as Metafont source. LaTeX support is
available in the duerer-latex bundle.

%package -n texlive-duerer-latex
Summary:        LaTeX support for the Duerer fonts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(duerer.sty) = %{tl_version}

%description -n texlive-duerer-latex
LaTeX support for Hoenig's Computer Duerer fonts, using their standard fontname
names.

%package -n texlive-dutchcal
Summary:        A reworking of ESSTIX13, adding a bold version
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(dutchcal.sty) = %{tl_version}

%description -n texlive-dutchcal
This package reworks the mathematical calligraphic font ESSTIX13, adding a bold
version. LaTeX support files are included. The new fonts may also be accessed
from the most recent version of mathalpha. The fonts themselves are subject to
the SIL OPEN FONT LICENSE, version 1.1.

%package -n texlive-ean
Summary:        Macros for making EAN barcodes
Version:        svn20851
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ean13.tex) = %{tl_version}
Provides:       tex(ean8.tex) = %{tl_version}

%description -n texlive-ean
Provides EAN-8 and EAN-13 forms. The package needs the ocr-b fonts; note that
the fonts are not available under a free licence, as the macros are.

%package -n texlive-ebgaramond
Summary:        LaTeX support for EBGaramond fonts
Version:        svn71069
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(ebgaramond.sty) = %{tl_version}

%description -n texlive-ebgaramond
EB Garamond is a revival by Georg Duffner of the 16th century fonts designed by
Claude Garamond. The LaTeX support package works for (pdf)LaTeX, XeLaTeX and
LuaLaTeX users; configuration files for use with microtype are provided.

%package -n texlive-ebgaramond-maths
Summary:        Limited LaTeX support for ebgaramond in maths
Version:        svn74169
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(svn-prov.sty)
Provides:       tex(ebgaramond-maths.sty) = %{tl_version}

%description -n texlive-ebgaramond-maths
This package provides some LaTeX support for the use of EBGaramond12 in
mathematics. It is based on, and requires, ebgaramond. The package was created
in response to a question at TeX-stackexchange. and tested in the form of an
answer in the same forum.

%package -n texlive-ecc
Summary:        Sources for the European Concrete fonts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ecc
The Metafont sources and TFM files of the European Concrete Fonts. This is the
T1-encoded extension of Knuth's Concrete fonts, including also the
corresponding text companion fonts. Adobe Type 1 versions of the fonts are
available as part of the cm-super font bundle.

%package -n texlive-eco
Summary:        Oldstyle numerals using EC fonts
Version:        svn29349
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(eco.sty) = %{tl_version}

%description -n texlive-eco
A set of font metric files and virtual fonts for using the EC fonts with
oldstyle numerals. These files can only be used together with the standard ec
fonts. The style file eco.sty is sufficient to use the eco fonts but if you
intend to use other font families as well, e.g., PostScript fonts, try altfont.

%package -n texlive-eczar
Summary:        A font family supporting Devanagari and Latin script
Version:        svn57716
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-eczar
rojhettaa sNsthecaa egjhaar haa yunikodd aadhaarit mukt ttNk aahe. hyaa ttNkaat
45+3 bhaassaa leNttin v devnaagrii lipiit purskRt kelyaa jaataat. vaibhv siNh
hyaaNnii hyaa ttNkaacaa abhiklp kelaa aahe v aajnyaavlii tsec nirmitii ddevhidd
brejhiinaa hyaaNnii kelii aahe. egzaar yh rozettaa dvaaraa prkaashit yunikodd
aadhaarit mukt ttNk hai / is ttNk dvaaraa 45+3 bhaassaaeN laittin tthaa
devnaagrii lipi meN purskRt kii jaatii hai / vaibhv siNh ne is kaa abhiklp
kiyaa hai aur aajnyaavli tthaa nirmiti ddevidd breziinaa dvaaraa kii gyii hai /
Eczar is an open-source type family published by Rosetta. The fonts support
over 45+3 languages in Latin and Devanagari scripts in 5 weights. These fonts
were designed by Vaibhav Singh, code and production are by David Brezina.

%package -n texlive-eiad
Summary:        Traditional style Irish fonts
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-eiad
In both lower and upper case 32 letters are defined (18 'plain' ones, 5 long
vowels and 9 aspirated consonants). The ligature 'agus' is also made available.
The remaining characters (digits, punctuation and accents) are inherited from
the Computer Modern family of fonts. The font definitions use code from the
sauter fonts, so those fonts have to be installed before using eiad. OT1*.fd
files are provided for use with LaTeX.

%package -n texlive-eiad-ltx
Summary:        LaTeX support for the eiad font
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eiad.sty) = %{tl_version}

%description -n texlive-eiad-ltx
The package provides macros to support use of the eiad fonts in OT1 encoding.
Also offered are a couple of Metafont files described in the font package, but
not provided there.

%package -n texlive-ektype-tanka
Summary:        Devanagari fonts by EkType
Version:        svn63255
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ektype-tanka
ek-ttaaiip sNsthecyaa kaahii utkRsstt devnaagrii ttNkaaNcaa sNgrh. ek-ttaaip
sNsthaa ke kii utkRsstt devnaagrii ttNkoN kaa sNgrh / . This package provides a
collection of some excellent Devanagari fonts by EkType: Mukta, Baloo, Modak,
and Jaini.

%package -n texlive-electrumadf
Summary:        Electrum ADF fonts collection
Version:        svn72484
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(electrum.sty) = %{tl_version}

%description -n texlive-electrumadf
Electrum ADF is a slab-serif font featuring optical and italic small-caps;
additional ligatures and an alternate Q; lining, hanging, inferior and superior
digits; and four weights. The fonts are provided in Adobe Type 1 format and the
support material enables use with LaTeX. Licence is mixed: LPPL for LaTeX
support; GPL with font exception for the fonts.

%package -n texlive-elvish
Summary:        Fonts for typesetting Tolkien Elvish scripts
Version:        svn15878
License:        LicenseRef-Elvish
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-elvish
The bundle provides fonts for Cirth (cirth.mf, etc.) and for Tengwar
(teng10.mf). The Tengwar fonts are supported by macros in teng.tex, or by the
(better documented) tengtex package.

%package -n texlive-epigrafica
Summary:        A Greek and Latin font
Version:        svn17210
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pxfonts.sty)
Provides:       tex(epigrafica.sty) = %{tl_version}

%description -n texlive-epigrafica
Epigrafica is forked from the development of the MgOpen font Cosmetica, which
is a similar design to Optima and includes Greek. Development has been
supported by the Laboratory of Digital Typography and Mathematical Software, of
the Department of Mathematics of the University of the Aegean, Greece.

%package -n texlive-epsdice
Summary:        A scalable dice "font"
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(epsdice.sty) = %{tl_version}

%description -n texlive-epsdice
The epsdice package defines a single command \epsdice that takes a numeric
argument (in the range 1-6), and selects a face image from a file that contains
each of the 6 possible die faces. The graphic file is provided in both
Encapsulated PostScript and PDF formats.

%package -n texlive-erewhon
Summary:        Font package derived from Heuristica and Utopia
Version:        svn75452
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(erewhon.sty) = %{tl_version}

%description -n texlive-erewhon
Erewhon is based on the Heuristica package, which is based in turn on Utopia.
Erewhon adds a number of new features -- small caps in all styles rather than
just regular, added figure styles (proportional, inferior, numerator,
denominator) and superior letters. The size is 6% smaller than Heuristica,
matching that of UtopiaStd.

%package -n texlive-erewhon-math
Summary:        Utopia based OpenType Math font
Version:        svn76878
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fourier-orns.sty)
Requires:       tex(iftex.sty)
Requires:       tex(realscripts.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(fourier-otf.sty) = %{tl_version}

%description -n texlive-erewhon-math
OpenType version of the fourier Type1 fonts designed by Michel Bovani.

%package -n texlive-esrelation
Summary:        Provides a symbol set for describing relations between ordered pairs
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(esrelation.sty) = %{tl_version}

%description -n texlive-esrelation
Around 2008, researcher Byron Cook and several colleagues began developing a
new set of interrelated algorithms capable of automatically reasoning about the
behavior of computer programs and other systems (such as biological systems,
circuit designs, etc). At the center of these algorithms were new ideas about
the relationships between structures expressible as mathematical sets and
relations. Using the language of mathematics and logic, the researchers
communicated these new results to others in their community via published
papers, research talks, etc. Unfortunately, they found the symbols already
available for reasoning about relations lacking (in contrast to sets, which
have a long-ago developed and robust symbol vocabulary). Early presentations
were unnecessarily cluttered. To more elegantly express these ideas around
relations, Cook recruited artist Tauba Auerbach to help develop a set of
symbols. This package provides an math symbol font for describing relations
between ordered pairs by using Metafont.

%package -n texlive-esstix
Summary:        PostScript versions of the ESSTIX, with macro support
Version:        svn22426
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(esstixbb.sty) = %{tl_version}
Provides:       tex(esstixcal.sty) = %{tl_version}
Provides:       tex(esstixfrak.sty) = %{tl_version}

%description -n texlive-esstix
These fonts represent translation to PostScript Type 1 of the ESSTIX fonts.
ESSTIX seem to have been a precursor to the STIX project, and were donated by
Elsevier to that project. The accompanying virtual fonts with customized
metrics and LaTeX support files allow their use as calligraphic, fraktur and
double-struck (blackboard bold) in maths mode.

%package -n texlive-esvect
Summary:        Vector arrows
Version:        svn32098
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(esvect.sty) = %{tl_version}

%description -n texlive-esvect
Write vectors using an arrow which differs from the Computer Modern one. You
have the choice between several kinds of arrows. The package consists of the
relevant Metafont code and a package to use it.

%package -n texlive-etbb
Summary:        An expansion of Edward Tufte's ET-Bembo family
Version:        svn69098
License:        MIT AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifetex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ETbb.sty) = %{tl_version}

%description -n texlive-etbb
Based on Daniel Benjamin Miller's XETBook, which expanded Tufte's ETBook, the
family name for the Bembo-like font family he commissioned for his books, ETbb
expands its features to include a full set of figure styles, small caps in all
styles, superior letters and figures, inferior figures, a new capital Sharp S
with small caps version, along with macros to activate these features in LaTeX.
Both otf and pfb are provided.

%package -n texlive-euler-math
Summary:        OpenType version of Hermann Zapf's Euler maths font
Version:        svn76681
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(euler-math.sty) = %{tl_version}
Provides:       tex(neo-euler.sty) = %{tl_version}

%description -n texlive-euler-math
Euler-Math.otf (formerly named 'Neo-Euler.otf') is an OpenType version of
Hermann Zapf's Euler maths font. It is the continuation of the Euler project
initiated by Khaled Hosny in 2009 and abandoned in 2016. A style file
euler-math.sty is provided as a replacement of the eulervm package for LuaLaTeX
and XeLaTeX users.

%package -n texlive-eulervm
Summary:        Euler virtual math fonts
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eulervm.sty) = %{tl_version}

%description -n texlive-eulervm
The well-known Euler fonts are suitable for typesetting mathematics in
conjunction with a variety of text fonts which do not provide mathematical
character sets of their own. Euler-VM is a set of virtual mathematics fonts
based on Euler and CM. This approach has several advantages over immediately
using the real Euler fonts: Most noticeably, less TeX resources are consumed,
the quality of various math symbols is improved and a usable \hslash symbol can
be provided. The virtual fonts are accompanied by a LaTeX package which makes
them easy to use, particularly in conjunction with Type1 PostScript text fonts.
They are compatible with amsmath. A package option allows the fonts to be
loaded at 95% of their nominal size, thus blending better with certain text
fonts, e.g., Minion.

%package -n texlive-euxm
Summary:        Extended Euler by DEK
Version:        svn54074
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-euxm
Includes two additional characters needed for Concrete Math (ca. 1991).

%package -n texlive-fbb
Summary:        A free Bembo-like font
Version:        svn55728
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifetex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(fbb.sty) = %{tl_version}

%description -n texlive-fbb
The package provides a Bembo-like font package based on Cardo but with many
modifications, adding Bold Italic, small caps in all styles, six figure choices
in all styles, updated kerning tables, added figure tables and corrected
f-ligatures. Both OpenType and Adobe Type 1 versions are provided; all
necessary support files are provided. The font works well with newtxmath's
libertine option.

%package -n texlive-fdsymbol
Summary:        A maths symbol font
Version:        svn74247
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(fdsymbol.sty) = %{tl_version}

%description -n texlive-fdsymbol
FdSymbol is a maths symbol font, designed as a companion to the Fedra family by
Typotheque, but it might also fit other contemporary typefaces.

%package -n texlive-fetamont
Summary:        Extended version of Knuth's logo typeface
Version:        svn43812
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fetamont.sty) = %{tl_version}

%description -n texlive-fetamont
The fetamont typeface was designed in Metafont and extends the Logo fonts to
complete the T1 encoding. The designs of the glyphs A, E, F, M, N, O, P, S and
T are based on the Metafont constructions by D. E. Knuth. The glyphs Y and 1
imitate the shapes of the corresponding glyphs in the METATYPE1 logo.

%package -n texlive-feyn
Summary:        A font for in-text Feynman diagrams
Version:        svn63945
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(feyn.sty) = %{tl_version}

%description -n texlive-feyn
Feyn may be used to produce relatively simple Feynman diagrams within equations
in a LaTeX document. While the feynmf package is good at drawing large diagrams
for figures, the present package and its fonts allow diagrams within equations
or text, at a matching size. The fonts are distributed as Metafont source, and
macros for their use are also provided.

%package -n texlive-fge
Summary:        A font for Frege's Grundgesetze der Arithmetik
Version:        svn71737
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fge.sty) = %{tl_version}

%description -n texlive-fge
The fonts are provided as Metafont source and Adobe Type 1 (pfb) files. A small
LaTeX package (fge) is included.

%package -n texlive-fira
Summary:        Fira fonts with LaTeX support
Version:        svn64422
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(FiraMono.sty) = %{tl_version}
Provides:       tex(FiraSans.sty) = %{tl_version}

%description -n texlive-fira
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Fira Sans and Fira Mono families of fonts designed by Erik Spiekermann and
Ralph du Carrois of Carrois Type Design. Fira Sans is available in eleven
weights with corresponding italics: light, regular, medium, bold, ...

%package -n texlive-firamath
Summary:        Fira sans serif font with Unicode math support
Version:        svn56672
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-firamath
Fira Math is a sans-serif font with Unicode math support. The design of this
font is based on Fira Sans and FiraGO. Fira Math is distributed in OpenType
format and can be used with the unicode-math package under XeLaTeX or LuaLaTeX.
More support is offered by the firamath-otf package.

%package -n texlive-firamath-otf
Summary:        Use OpenType math font Fira Math
Version:        svn68233
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-firamath
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xfakebold.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(firamath-otf.sty) = %{tl_version}

%description -n texlive-firamath-otf
The package offers XeTeX/LuaTeX support for the Sans Serif OpenType Fira Math
Font.

%package -n texlive-foekfont
Summary:        The title font of the Mads Fok magazine
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(foekfont.sty) = %{tl_version}

%description -n texlive-foekfont
The bundle provides an Adobe Type 1 font, and LaTeX support for its use. The
magazine web site shows the font in use in a few places.

%package -n texlive-fonetika
Summary:        Support for the Danish "Dania" phonetic system
Version:        svn21326
License:        GPL-1.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(fonetika.sty) = %{tl_version}

%description -n texlive-fonetika
Fonetika Dania is a font bundle with a serif font and a sans serif font for the
danish phonetic system Dania. Both fonts exist in regular and bold weights.
LaTeX support is provided. The fonts are based on URW Palladio and Iwona
Condensed, and were created using FontForge.

%package -n texlive-fontawesome
Summary:        Font containing web-related icons
Version:        svn48145
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Provides:       tex(fontawesome.sty) = %{tl_version}
Provides:       tex(fontawesomesymbols-generic.tex) = %{tl_version}
Provides:       tex(fontawesomesymbols-pdftex.tex) = %{tl_version}
Provides:       tex(fontawesomesymbols-xeluatex.tex) = %{tl_version}

%description -n texlive-fontawesome
The package offers access to the large number of web-related icons provided by
the included font. The package requires the package, fontspec, if run with
XeTeX or LuaTeX.

%package -n texlive-fontawesome5
Summary:        Font Awesome 5 with LaTeX support
Version:        svn63207
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexbase.sty)
Requires:       tex(xparse.sty)
Provides:       tex(fontawesome5-generic-helper.sty) = %{tl_version}
Provides:       tex(fontawesome5-mapping.def) = %{tl_version}
Provides:       tex(fontawesome5-utex-helper.sty) = %{tl_version}
Provides:       tex(fontawesome5.sty) = %{tl_version}

%description -n texlive-fontawesome5
This package provides LaTeX support for the included "Font Awesome 5 Free" icon
set. These icons were designed by Fort Awesome and released under the SIL OFL
1.1 license. The commercial "Pro" version is also supported, if it is installed
and XeLaTeX or LuaLaTeX is used.

%package -n texlive-fontawesome6
Summary:        Font Awesome 6 with LaTeX support
Version:        svn76339
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexbase.sty)
Requires:       tex(xparse.sty)
Provides:       tex(fontawesome6-generic-helper.sty) = %{tl_version}
Provides:       tex(fontawesome6-mapping.def) = %{tl_version}
Provides:       tex(fontawesome6-utex-helper.sty) = %{tl_version}
Provides:       tex(fontawesome6.sty) = %{tl_version}

%description -n texlive-fontawesome6
This package provides LaTeX support for the included "Font Awesome 6 Free" icon
set. These icons were designed by Fort Awesome and released under the SIL OFL
1.1 license. The commercial "Pro" version is also supported, if it is installed
and XeLaTeX or LuaLaTeX is used. For this font you need a paid license, for
more information visit Fort Awesome Pro. More information about Font Awesome is
available at Fort Awesome. To use an icon after the package is loaded, just
enter the name of the icon in CamelCase prefixed with \fa, for example
\faAddressBook for the address-book icon. The TeX files are derived from the
Font Awesome 5package, are maintained by Daniel Nagel and are released under
the LaTeX Project Public License version 1.3c. All included fonts are provided
by Fort Awesome under the SIL OFL 1.1 license This package is not an official
Fort Awesome project. For bug reports, please open an issue at
https://github.com/braniii/fontawesome.

%package -n texlive-fontawesome7
Summary:        Font Awesome 7 with LaTeX support
Version:        svn76735
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexbase.sty)
Requires:       tex(xparse.sty)
Provides:       tex(fontawesome7-generic-helper.sty) = %{tl_version}
Provides:       tex(fontawesome7-mapping.def) = %{tl_version}
Provides:       tex(fontawesome7-utex-helper.sty) = %{tl_version}
Provides:       tex(fontawesome7.sty) = %{tl_version}

%description -n texlive-fontawesome7
This package provides LaTeX support for the included "Font Awesome 7 Free" icon
set. These icons were designed by Fort Awesome and released under the SIL OFL
1.1 license. The commercial "Pro" version has only preliminary alpha support
for now, if it is installed and XeLaTeX or LuaLaTeX is used. For this font you
need a paid license, for more information visit Fort Awesome Pro. More
information about Font Awesome is available at Fort Awesome. To use an icon
after the package is loaded, just enter the name of the icon in CamelCase
prefixed with \fa, for example \faAddressBook for the address-book icon. The
TeX files are derived from the Font Awesome 5package, are maintained by Daniel
Nagel and are released under the LaTeX Project Public License version 1.3c. All
included fonts are provided by Fort Awesome under the SIL OFL 1.1 license This
package is not an official Fort Awesome project. For bug reports, please open
an issue at https://github.com/braniii/fontawesome.

%package -n texlive-fontawesomescaled
Summary:        Additional macros for fontawesome icons
Version:        svn75980
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontawesome.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(fontawesomescaled.sty) = %{tl_version}

%description -n texlive-fontawesomescaled
This package provides additional macros for fontawesome icons with custom scale
or alias creation: \faIconScaled{} for \faIcon{} \faScaled{} for \fa
\CreateAliasFa for alias

%package -n texlive-fontmfizz
Summary:        Font Mfizz icons for use in LaTeX
Version:        svn43546
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(fontmfizz.sty) = %{tl_version}

%description -n texlive-fontmfizz
The MFizz font provides scalable vector icons representing programming
languages, operating systems, software engineering, and technology. It can be
seen as an extension to FontAwesome. This package requires the fontspec package
and either the Xe(La)TeX or Lua(La)TeX engine to load the included ttf font.

%package -n texlive-fonts-churchslavonic
Summary:        Fonts for typesetting in Church Slavonic language
Version:        svn67473
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fonts-churchslavonic
The package provides Unicode-encoded OpenType fonts for Church Slavonic which
are intended for Unicode TeX engines only.

%package -n texlive-fontscripts
Summary:        Font encodings, metrics and Lua script fragments for font creation
Version:        svn74247
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fntbuild-regression-test.tex) = %{tl_version}
Provides:       tex(fntbuild-tables.tex) = %{tl_version}

%description -n texlive-fontscripts
Font encodings, metrics and Lua script fragments for generating font support
packages for 8-bit engines with l3build. Optional template-based system enables
the automatic generation of font tables and l3build tests. Easy addition of
variable scaling to fd files (unsupported by some tools). Primarily designed
for fontinst, but can be adapted for use with other programmes. Default
configuration is intended to be cross-platform and require only tools included
in TeX Live, but the documentation includes a simple adaption for integration
with FontForge and GNU make.

%package -n texlive-forum
Summary:        Forum fonts with LaTeX support
Version:        svn64566
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(forum.sty) = %{tl_version}

%description -n texlive-forum
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Forum font, designed by Denis Masharov. Forum has antique, classic "Roman"
proportions. It can be used to set body texts and works well in titles and
headlines too. It is truly multilingual, with glyphs for Central and Eastern
Europe, Baltics, Cyrillic and Asian Cyrillic communities. There is currently
just a regular weight and an artificially emboldened bold.

%package -n texlive-fourier
Summary:        Using Utopia fonts in LaTeX documents
Version:        svn72243
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(fourier-orns.sty) = %{tl_version}
Provides:       tex(fourier.sty) = %{tl_version}

%description -n texlive-fourier
Fourier-GUTenberg is a LaTeX typesetting system which uses Adobe Utopia as its
standard base font. Fourier-GUTenberg provides all complementary typefaces
needed to allow Utopia based TeX typesetting, including an extensive
mathematics set and several other symbols. The system is absolutely
stand-alone: apart from Utopia and Fourier, no other typefaces are required.
The fourier fonts will also work with Adobe Utopia Expert fonts, which are only
available for purchase. Utopia is a registered trademark of Adobe Systems
Incorporated.

%package -n texlive-fouriernc
Summary:        Use New Century Schoolbook text with Fourier maths fonts
Version:        svn29646
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fourier.sty)
Provides:       tex(fouriernc.sty) = %{tl_version}

%description -n texlive-fouriernc
This package provides a LaTeX mathematics font setup for use with New Century
Schoolbook text. In order to use it you need to have the Fourier-GUTenberg
fonts installed.

%package -n texlive-frcursive
Summary:        French cursive hand fonts
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(frcursive.sty) = %{tl_version}

%description -n texlive-frcursive
A hand-writing font in the style of the French academic running-hand. The font
was written in Metafont and has been converted to Adobe Type 1 format. LaTeX
support (NFSS fd files, and a package) and font maps are provided.

%package -n texlive-frederika2016
Summary:        An OpenType Greek calligraphy font
Version:        svn42157
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-frederika2016
Frederika2016 is an attempt to digitize Hermann Zapf's Frederika font. The font
is the Greek companion of Virtuosa by the same designer. This font is a
calligraphy font and this is an initial release.

%package -n texlive-frimurer
Summary:        Access to the 'frimurer' cipher for use with LaTeX
Version:        svn56704
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(frimurer.sty) = %{tl_version}

%description -n texlive-frimurer
This package provides access to the 'frimurer' cipher for use with LaTeX.

%package -n texlive-garamond-libre
Summary:        The Garamond Libre font face
Version:        svn71058
License:        MIT AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(garamondlibre.sty) = %{tl_version}

%description -n texlive-garamond-libre
Garamond Libre is a free and open-source old-style font family. It is a "true
Garamond," i.e., it is based off the designs of 16th-century French engraver
Claude Garamond (also spelled Garamont). The Roman design is Garamond's; the
italics are from a design by Robert Granjon. The upright Greek font is after a
design by Firmin Didot; the "italic" Greek font is after a design by Alexander
Wilson. The font family includes support for Latin, Greek (monotonic and
polytonic) and Cyrillic scripts, as well as small capitals, old-style figures,
superior and inferior figures, historical ligatures, Byzantine musical symbols,
the IPA and swash capitals.

%package -n texlive-garamond-math
Summary:        An OTF math font matching EB Garamond
Version:        svn61481
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-garamond-math
Garamond-Math is an open type math font matching EB Garamond (Octavio Pardo)
and EB Garamond (Georg Mayr-Duffner). Many mathematical symbols are derived
from other fonts, others are made from scratch. The metric is generated with a
Python script. Issues, bug reports and other contributions are welcome.

%package -n texlive-gelasio
Summary:        LaTeX support for the Gelasio family of fonts
Version:        svn71047
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(gelasio.sty) = %{tl_version}

%description -n texlive-gelasio
This package provides (pdf)LaTeX, XeLaTeX and LuaLaTeX support for the Gelasio
family of fonts designed by Eben Sorkin to be metric-compatible with Georgia in
its Regular and Bold weights. Medium and SemiBold weights have been added.

%package -n texlive-gelasiomath
Summary:        Math and small cap additions to Gelasio fonts
Version:        svn73362
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(newtx.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(gelasiomath.sty) = %{tl_version}

%description -n texlive-gelasiomath
The package offers math support for the gelasio package, using symbols from
newtxmath, Roman math letters from Gelasio and Greek math letters based on
XCharter Greek. Also added small caps based on XCharter small caps and other
minor features to Gelasio.

%package -n texlive-genealogy
Summary:        A compilation genealogy font
Version:        svn25112
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-genealogy
A simple compilation of the genealogical symbols found in the wasy and gen
fonts, adding the male and female symbols to Knuth's 'gen' font, and so
avoiding loading two fonts when you need only genealogical symbols. The font is
distributed as Metafont source.

%package -n texlive-gentium-otf
Summary:        Support Gentium fonts for LuaLaTeX and XeLaTeX
Version:        svn75790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(gentium-otf.sty) = %{tl_version}

%description -n texlive-gentium-otf
This package supports the free TrueType Gentium fonts from the gentium-sil
package and defines missing typefaces. All font features are available via
special macros. The package works only for LuaLaTeX/XeLaTeX.

%package -n texlive-gentium-sil
Summary:        A complete Greek font with Latin and Cyrillic, too
Version:        svn75783
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gentium-sil
This is a redistribution of the original Gentium and GentiumBook release from
SIL, not altered in any way. Gentium is a typeface family designed to enable
the diverse ethnic groups around the world who use the Latin, Cyrillic and
Greek scripts to produce readable, high-quality publications. The Gentium
family includes a complete Greek font, supporting both monotonic and polytonic
forms. While some Greek characters do closely resemble Latin ones, it is a
separate design that embraces the robust, distinctive character of the Greek
script, but does so within the design context of the whole typeface. As a
result, the two scripts can be successfully mixed in a paragraph or page of
text.

%package -n texlive-gfsartemisia
Summary:        A modern Greek font design
Version:        svn19469
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(euler.sty)
Requires:       tex(txfonts.sty)
Provides:       tex(gfsartemisia-euler.sty) = %{tl_version}
Provides:       tex(gfsartemisia.sty) = %{tl_version}

%description -n texlive-gfsartemisia
GFS Artemisia is a relatively modern font, designed as a 'general purpose' font
in the same sense as Times is nowadays treated. The present version has been
provided by the Greek Font Society. The font supports the Greek and Latin
alphabets. LaTeX support is provided, using the OT1, T1 and LGR encodings.

%package -n texlive-gfsbodoni
Summary:        A Greek and Latin font based on Bodoni
Version:        svn28484
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfsbodoni.sty) = %{tl_version}

%description -n texlive-gfsbodoni
Bodoni's Greek fonts in the 18th century broke, for the first time, with the
Byzantine cursive tradition of Greek fonts. GFS Bodoni resurrects his work for
general use. The font family supports both Greek and Latin letters. LaTeX
support of the fonts is provided, offering OT1, T1 and LGR encodings. The fonts
themselves are provided in Adobe Type 1 and OpenType formats.

%package -n texlive-gfscomplutum
Summary:        A Greek font with a long history
Version:        svn19469
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfscomplutum.sty) = %{tl_version}

%description -n texlive-gfscomplutum
GFS Complutum derives, via a long development, from a minuscule-only font cut
in the 16th century. An unsatisfactory set of majuscules were added in the
early 20th century, but its author died before he could complete the revival of
the font. The Greek Font Society has released this version, which has a new set
of majuscules.

%package -n texlive-gfsdidot
Summary:        A Greek font based on Didot's work
Version:        svn69112
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(pxfonts.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(gfsdidot.sty) = %{tl_version}
Provides:       tex(testDidot.sty) = %{tl_version}

%description -n texlive-gfsdidot
The design of Didot's 1805 Greek typeface was influenced by the neoclassical
ideals of the late 18th century. The font was brought to Greece at the time of
the 1821 Greek Revolution, by Didot's son, and was very widely used. The
present version is provided by the Greek Font Society. The font supports the
Greek alphabet, and is accompanied by a matching Latin alphabet based on Zapf's
Palatino. LaTeX support is provided, using the OT1, T1, TS1, and LGR encodings.

%package -n texlive-gfsdidotclassic
Summary:        The classic version of GFSDidot
Version:        svn52778
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gfsdidotclassic
The classic version of GFSDidot provided for Unicode TeX engines.

%package -n texlive-gfsneohellenic
Summary:        A font in the Neo-Hellenic style
Version:        svn63944
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfsneohellenic.sty) = %{tl_version}

%description -n texlive-gfsneohellenic
The NeoHellenic style evolved in academic circles in the 19th and 20th century;
the present font follows a cut commissioned from Monotype in 1927. The present
version was provided by the Greek Font Society. The font supports both Greek
and Latin characters, and has been adjusted to work well with the cmbright
fonts for mathematics support. LaTeX support of the fonts is provided, offering
OT1, T1 and LGR encodings.

%package -n texlive-gfsneohellenicmath
Summary:        A math font in the Neo-Hellenic style
Version:        svn63928
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(gfsneohellenicot.sty) = %{tl_version}

%description -n texlive-gfsneohellenicmath
The GFSNeohellenic font, a historic font first designed by Victor Scholderer,
and digitized by George Matthiopoulos of the Greek Font Society (GFS), now has
native support for Mathematics. The project was commissioned to GFS by the
Department of Mathematics of the University of the Aegean, Samos, Greece. The
Math Table was constructed by the Mathematics Professor A. Tsolomitis. A useful
application is in beamer documents since this is a Sans Math font. The
GFSNeohellenic fontfamily supports many languages (including Greek), and it is
distributed (both text and math) under the OFL license.

%package -n texlive-gfssolomos
Summary:        A Greek-alphabet font
Version:        svn18651
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfssolomos.sty) = %{tl_version}

%description -n texlive-gfssolomos
Solomos is a font which traces its descent from a calligraphically-inspired
font of the mid-19th century. LaTeX support, for use with the LGR encoding
only, is provided.

%package -n texlive-gillcm
Summary:        Alternative unslanted italic Computer Modern fonts
Version:        svn19878
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gillcm.sty) = %{tl_version}

%description -n texlive-gillcm
This is a demonstration of the use of virtual fonts for unusual effects: the
package implements an old idea of Eric Gill. The package was written for the
author's talk at TUG 2010.

%package -n texlive-gillius
Summary:        Gillius fonts with LaTeX support
Version:        svn64865
License:        GPL-2.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(gillius.sty) = %{tl_version}
Provides:       tex(gillius2.sty) = %{tl_version}

%description -n texlive-gillius
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Gillius and Gillius No. 2 families of sans serif fonts and condensed versions
of them, designed by Hirwen Harendal. According to the designer, the fonts were
inspired by Gill Sans.

%package -n texlive-gnu-freefont
Summary:        A Unicode font, with rather wide coverage
Version:        svn68624
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gnu-freefont
The package provides a set of outline (i.e. OpenType) fonts covering as much as
possible of the Unicode character set. The set consists of three typefaces: one
monospaced and two proportional (one with uniform and one with modulated
stroke).

%package -n texlive-gofonts
Summary:        GoSans and GoMono fonts with LaTeX support
Version:        svn64358
License:        BSD-3-Clause AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(GoMono.sty) = %{tl_version}
Provides:       tex(GoSans.sty) = %{tl_version}

%description -n texlive-gofonts
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
GoSans and GoMono families of fonts designed by the Bigelow & Holmes foundry
for the Go project. GoSans is available in three weights: Regular, Medium, and
Bold (with corresponding italics). GoMono is available in regular and bold,
with italics. Notes on the design may be found at
https://blog.golang.org/go-fonts.

%package -n texlive-gothic
Summary:        A collection of old German-style fonts
Version:        svn49869
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gothic
A collection of fonts that reproduce those used in "old German" printing and
handwriting. The set comprises Gothic, Schwabacher and Fraktur fonts, a pair of
handwriting fonts, Sutterlin and Schwell, and a font containing decorative
initials. In addition, there are two re-encoding packages for Haralambous's
fonts, providing T1, using virtual fonts, and OT1 and T1, using Metafont.

%package -n texlive-greenpoint
Summary:        The Green Point logo
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-greenpoint
A Metafont-implementation of the logo commonly known as 'Der Grune Punkt' ('The
Green Point'). In Austria, it can be found on nearly every bottle. It should
not be confused with the 'Recycle'-logo, implemented by Ian Green.

%package -n texlive-grotesq
Summary:        URW Grotesq font pack for LaTeX
Version:        svn35859
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-grotesq
The directory contains a copy of the Type 1 font "URW Grotesq 2031 Bold'
released under the GPL by URW, with supporting files for use with (La)TeX.

%package -n texlive-gudea
Summary:        The Gudea font face with support for LaTeX and pdfLaTeX
Version:        svn57359
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(Gudea.sty) = %{tl_version}

%description -n texlive-gudea
This package provides the Gudea family of fonts designed by Agustina Mingote,
with support for LaTeX and pdfLaTeX.

%package -n texlive-hacm
Summary:        Font support for the Arka language
Version:        svn27671
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hacm.sty) = %{tl_version}

%description -n texlive-hacm
The package supports typesetting hacm, the alphabet of the constructed language
Arka. The bundle provides nine official fonts, in Adobe Type 1 format.

%package -n texlive-hamnosys
Summary:        A font for sign languages
Version:        svn61941
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(ucharclasses.sty)
Provides:       tex(hamnosys.sty) = %{tl_version}

%description -n texlive-hamnosys
The Hamburg Notation System, HamNoSys for short, is a system for the phonetic
transcription of signed languages. This package makes HamNoSys available in
XeLaTeX and LuaLaTeX. The package provides a Unicode font for rendering
HamNoSys symbols as well as three methods for entering them.

%package -n texlive-hands
Summary:        Pointing hand font
Version:        svn13293
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hands
Provides right- and left-pointing hands in both black-on-white and
white-on-black realisation. The font is distributed as Metafont source.

%package -n texlive-hep-font
Summary:        Latin modern extended by computer modern
Version:        svn76220
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cfr-lm.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontsetup.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(microtype.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(silence.sty)
Requires:       tex(slantsc.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(units.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(hep-font.sty) = %{tl_version}

%description -n texlive-hep-font
The hep-font package loads standard font packages and extends the usual Latin
Modern implementations by replacing missing fonts with Computer Modern
counterparts. The package is loaded with \usepackage{hep-font}.

%package -n texlive-hep-math-font
Summary:        Extended Greek and sans-serif math
Version:        svn76220
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(MnSymbol.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amstext.sty)
Requires:       tex(bm.sty)
Requires:       tex(exscale.sty)
Requires:       tex(fixmath.sty)
Requires:       tex(iftex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(xstring.sty)
Provides:       tex(hep-math-font.sty) = %{tl_version}

%description -n texlive-hep-math-font
The hep-math-font package adjust the math fonts to be sans-serif if the
document is sans-serif. Additionally Greek letters are redefined to be always
italic and upright in math and text mode respectively. Some math font macros
are adjusted to give more consistently the naively expected results. The
package is loaded with \usepackage{hep-math-font}.

%package -n texlive-heros-otf
Summary:        Using the OpenType fonts TeX Gyre Heros>
Version:        svn64695
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(heros-otf.sty) = %{tl_version}

%description -n texlive-heros-otf
This package can only be used with LuaLaTeX or XeLaTeX. It does the font
setting for the OpenType font 'TeX Gyre Heros'. The condensed versions of the
fonts are also supported. The missing typefaces for slanted text are also
defined.

%package -n texlive-heuristica
Summary:        Fonts extending Utopia, with LaTeX support files
Version:        svn69649
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(heuristica.sty) = %{tl_version}

%description -n texlive-heuristica
The fonts extend the utopia set with Cyrillic glyphs, additional figure styles,
ligatures and Small Caps in Regular style only. Macro support, and maths fonts
that match the Utopia family, are provided by the Fourier and the Mathdesign
font packages.

%package -n texlive-hfbright
Summary:        The hfbright fonts
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hfbright
These are Adobe Type 1 versions of the OT1-encoded and maths parts of the
Computer Modern Bright fonts.

%package -n texlive-hfoldsty
Summary:        Old style numerals with EC fonts
Version:        svn29349
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fix-cm.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(hfoldsty.sty) = %{tl_version}

%description -n texlive-hfoldsty
The hfoldsty package provides virtual fonts for using oldstyle (0123456789)
figures with the European Computer Modern fonts. It does a similar job as the
eco package by Sebastian Kirsch but includes a couple of improvements, i.e.,
better kerning with guillemets, and support for character protruding using the
pdfcprot package.

%package -n texlive-hindmadurai
Summary:        The HindMadurai font face with support for LaTeX and pdfLaTeX
Version:        svn57360
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(HindMadurai.sty) = %{tl_version}

%description -n texlive-hindmadurai
This package provides the HindMadurai family of fonts designed by the Indian
Type Foundry, with support for LaTeX and pdfLaTeX.

%package -n texlive-ibarra
Summary:        LaTeX support for the Ibarra Real Nova family of fonts
Version:        svn71059
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(ibarra.sty) = %{tl_version}

%description -n texlive-ibarra
The Ibarra Real Nova is a revival of a typeface designed by Geronimo Gil for
the publication of Don Quixote for the Real Academia de la Lengua in 1780.
Joaquin Ibarra was the printer.

%package -n texlive-ifsym
Summary:        A collection of symbols
Version:        svn24868
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Provides:       tex(ifsym.sty) = %{tl_version}

%description -n texlive-ifsym
A set of symbol fonts, written in Metafont, offering (respectively) clock-face
symbols, geometrical symbols, weather symbols, mountaineering symbols,
electronic circuit symbols and a set of miscellaneous symbols. A LaTeX package
is provided, that allows the user to load only those symbols needed in a
document.

%package -n texlive-imfellenglish
Summary:        IM Fell English fonts with LaTeX support
Version:        svn64568
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(imfellEnglish.sty) = %{tl_version}

%description -n texlive-imfellenglish
Igino Marini has implemented digital revivals of fonts bequeathed to Oxford
University by Dr. John Fell, Bishop of Oxford and Dean of Christ Church in
1686. This package provides the English family, consisting of Roman, Italic and
Small-Cap fonts.

%package -n texlive-inconsolata
Summary:        A monospaced font, with support files for use with TeX
Version:        svn54512
License:        OFL-1.1 AND Apache-2.0 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(textcomp.sty)
Requires:       tex(upquote.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(inconsolata.sty) = %{tl_version}
Provides:       tex(zi4.sty) = %{tl_version}

%description -n texlive-inconsolata
Inconsolata is a monospaced font designed by Raph Levien. This package contains
the font (in both Adobe Type 1 and OpenType formats) in regular and bold
weights, with additional glyphs and options to control slashed zero, upright
quotes and a shapelier lower-case L, plus metric files for use with TeX, and
LaTeX font definition and other relevant files.

%package -n texlive-inconsolata-nerd-font
Summary:        Inconsolata Nerd Font with support for XeLaTeX or LuaLaTeX
Version:        svn76924
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(inconsolata-nerd-font.sty) = %{tl_version}

%description -n texlive-inconsolata-nerd-font
Inconsolata is a monospaced font designed by Raph Levien. It is already
available via the inconsolata package. However, that package provides a pretty
old version of the font. Additionally, the Nerd Font project extended the font
by a huge amount of additional glyphs. This package provides the Inconsolata
Nerd Font in .ttf format as well as a convenient interface to load the font for
the XeTeX and LuaTeX engines.

%package -n texlive-initials
Summary:        Adobe Type 1 decorative initial fonts
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-initials
For each font, at least a .pfb and a .tfm file is provided, with an .fd file
for use with LaTeX.

%package -n texlive-inriafonts
Summary:        Inria fonts with LaTeX support
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(InriaSans.sty) = %{tl_version}
Provides:       tex(InriaSerif.sty) = %{tl_version}

%description -n texlive-inriafonts
Inria is a free font designed by Black[Foundry] for Inria research institute.
The font is available for free. It comes as Serif and Sans Serif, each with
three weights and matching italics. Using these fonts with XeLaTeX and LuaLaTeX
is easy using the fontspec package; we refer to the documentation of fontspec
for more information. The present package provides a way of using them with
LaTeX and pdfLaTeX: it provides two style files, InriaSerif.sty and
InriaSans.sty, together with the PostScript version of the fonts and their
associated files. These were created using autoinst.

%package -n texlive-inter
Summary:        The inter font face with support for LaTeX, XeLaTeX, and LuaLaTeX
Version:        svn68966
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(inter.sty) = %{tl_version}

%description -n texlive-inter
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Inter Sans family of fonts (version 3.015), designed by Rasmus Andersson. Inter
is a typeface specially designed for user interfaces with focus on high
legibility of small-to-medium sized text on computer screens. The family
features a tall x-height to aid in readability of mixed-case and lower-case
text.

%package -n texlive-ipaex-type1
Summary:        IPAex fonts converted to Type-1 format Unicode subfonts
Version:        svn47700
License:        IPA
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ipaex-type1.sty) = %{tl_version}

%description -n texlive-ipaex-type1
The package contains the IPAex Fonts converted into Unicode subfonts in Type1
format, which is most suitable for use with the CJK package. Font conversion
was done with ttf2pt1.

%package -n texlive-iwona
Summary:        A two-element sans-serif font
Version:        svn19611
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(iwona-math.tex) = %{tl_version}
Provides:       tex(iwona.sty) = %{tl_version}

%description -n texlive-iwona
Iwona is a two-element sans-serif typeface. It was created as an alternative
version of the Kurier typeface, which was designed in 1975 for a diploma in
typeface design at the Warsaw Academy of Fine Arts under the supervision of
Roman Tomaszewski. This distribution contains a significantly extended set of
characters covering the following modern alphabets: latin (including
Vietnamese), Cyrillic and Greek as well as a number of additional symbols
(including mathematical symbols). The fonts are prepared in Type 1 and OpenType
formats. For use with TeX the following encoding files have been prepared: T1
(ec), T2 (abc), and OT2--Cyrillic, T5 (Vietnamese), OT4, QX, texansi and
nonstandard (IL2 for the Czech fonts), as well as supporting macros and files
defining fonts for LaTeX.

%package -n texlive-jablantile
Summary:        Metafont version of tiles in the style of Slavik Jablan
Version:        svn16364
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jablantile
This is a small Metafont font to implement the modular tiles described by
Slavik Jablan. For an outline of the theoretical structure of the tiles, see
(for example) Jablan's JMM 2006 Exhibit.

%package -n texlive-jamtimes
Summary:        Expanded Times Roman fonts
Version:        svn20408
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(eucal.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(jamtimes.sty) = %{tl_version}

%description -n texlive-jamtimes
The package offers LaTeX support for the expanded Times Roman font, which has
been used for many years in the Journal d'Analyse Mathematique. Mathematics
support is based on the Belleek fonts.

%package -n texlive-jetbrainsmono-otf
Summary:        Package (or only fontspec config files) support for the OpenType font JetBrains
Version:        svn73401
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(jetbrainsmono-otf.sty) = %{tl_version}

%description -n texlive-jetbrainsmono-otf
Support for the OpenType font JetBrainsMono (so with LuaLaTeX/XeTeX and
fontspec),with or without ligatures, and with weights versions. jetbrainsmono
or jetbrainscode for regular version, jetbrainsmono-medium or
jetbrainscode-medium for medium version, jetbrainsmono-light or
jetbrainscode-light for light version, jetbrainsmono-extralight or
jetbrainscode-extralight for extralight version, jetbrainsmono-thin or
jetbrainscode-thin for thin version.

%package -n texlive-josefin
Summary:        Josefin fonts with LaTeX support
Version:        svn64569
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(josefin.sty) = %{tl_version}

%description -n texlive-josefin
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Josefin Sans family of fonts, designed by Santiago Orozco of the Typemade
foundry in Monterey, Mexico. Josefin Sans is available in seven weights, with
corresponding italics.

%package -n texlive-juliamono
Summary:        Support for the TrueType font JuliaMono
Version:        svn76734
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(juliamono.sty) = %{tl_version}

%description -n texlive-juliamono
JuliaMono is a monospaced font for scientific and technical computing. There
are font files for Regular, Italic, Bold and BoldItalic in light, medium, black
and extra bold version. There are more than 12 thousand glyphs in every font
file.

%package -n texlive-junicode
Summary:        A TrueType and OpenType font family for mediaevalists
Version:        svn76210
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(junicode.sty) = %{tl_version}

%description -n texlive-junicode
Junicode is a TrueType/OpenType font family with many features for antiquarians
(especially medievalists) based on typefaces used by the Oxford Press in the
late 17th and early 18th centuries. It works well with Lua(La)TeX or Xe(La)TeX,
but the basic textual features are also available with (pdf)LaTeX.

%package -n texlive-junicodevf
Summary:        A TrueType variable font family for mediaevalists
Version:        svn76209
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(junicodevf.sty) = %{tl_version}

%description -n texlive-junicodevf
This package supports the Junicode variable fonts for LuaLaTeX. The Junicode
font is primarily for scholars and students of the Middle Ages, but it serves
users with a wide variety of interests. It tracks the development of the
Medieval Unicode Font Initiative (MUFI), with its wealth of specialized
medieval characters, but it also provides many OpenType features that allow
users to access MUFI characters in accessible ways.

%package -n texlive-kixfont
Summary:        A font for KIX codes
Version:        svn18488
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-kixfont
The KIX code is a barcode-like format used by the Dutch PTT to encode country
codes, zip codes and street numbers in a machine-readable format. If printed
below the address line on bulk mailings, a discount can be obtained. The font
is distributed in Metafont format, and covers the numbers and upper-case
letters.

%package -n texlive-kpfonts
Summary:        A complete set of fonts for text and mathematics
Version:        svn72680
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kpfonts-otf.sty)
Provides:       tex(kpfonts.sty) = %{tl_version}

%description -n texlive-kpfonts
The family contains text fonts in roman, sans-serif and monospaced shapes, with
true small caps and old-style numbers; the package offers full support of the
textcomp package. The mathematics fonts include all the AMS fonts, in both
normal and bold weights. Each of the font types is available in two main
versions: default and 'light'. Each version is available in four variants:
default; oldstyle numbers; oldstyle numbers with old ligatures such as ct and
st, and long-tailed capital Q; and veryoldstyle with long s. Other variants
include small caps as default or 'large small caps', and for mathematics both
upright and slanted shapes for Greek letters, as well as default and narrow
versions of multiple integrals. The fonts were originally derived from URW
Palladio (with URW's agreement) though the fonts are very clearly different in
appearance from their parent.

%package -n texlive-kpfonts-otf
Summary:        OpenType versions of the kpfonts (Type1) designed by Christophe Caignaert
Version:        svn76746
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(realscripts.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(kpfonts-otf.sty) = %{tl_version}

%description -n texlive-kpfonts-otf
This bundle provides OpenType versions of the Type1 Kp-fonts designed by
Christophe Caignaert. It is usable with LuaTeX or XeTeX engines only. It
consists of sixteen Text fonts (eight Serif, four Sans-Serif, four Monotype)
and six Math fonts. Serif and Sans-Serif families have small caps available in
two sizes (SmallCaps and PetitesCaps), upper and lowercase digits, real
superscripts and subscripts; ancient ligatures (ct and st), ancient long-s and
a long-tailed capital Q are available via font features. Math fonts cover all
usual symbols including AMS'; a full list of available symbols is provided, see
the 'List of glyphs'.

%package -n texlive-kurier
Summary:        A two-element sans-serif typeface
Version:        svn19612
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(kurier-math.tex) = %{tl_version}
Provides:       tex(kurier.sty) = %{tl_version}

%description -n texlive-kurier
Kurier is a two-element sans-serif typeface. It was designed for a diploma in
typeface design at the Warsaw Academy of Fine Arts under the supervision of
Roman Tomaszewski. This distribution contains a significantly extended set of
characters covering the following modern alphabets: latin (including
Vietnamese), Cyrillic and Greek as well as a number of additional symbols
(including mathematical symbols). The fonts are prepared in Type 1 and OpenType
formats. For use with TeX the following encoding files have been prepared: T1
(ec), T2 (abc), and OT2--Cyrillic, T5 (Vietnamese), OT4, QX, texansi
and--nonstandard (IL2 for the Czech fonts), as well as supporting macros and
files defining fonts for LaTeX.

%package -n texlive-lato
Summary:        Lato font family and LaTeX support
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(lato.sty) = %{tl_version}

%description -n texlive-lato
Lato is a sanserif typeface family designed in the Summer 2010 by Warsaw-based
designer Lukasz Dziedzic for the tyPoland foundry. This font, which includes
five weights (hairline, light, regular, bold and black), is available from the
Google Font Directory as TrueType files under the Open Font License version
1.1. The package provides support for this font in LaTeX. It includes the
original TrueType fonts, as well as Type 1 versions, converted for this package
using FontForge for full support with Dvips.

%package -n texlive-lete-sans-math
Summary:        Lato-based OpenType Math font for LuaTeX and XeTeX
Version:        svn76200
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(lete-sans-math.sty) = %{tl_version}

%description -n texlive-lete-sans-math
This package provides a Unicode Math font LeteSansMath.otf meant to be used
together with Lato sans-serif TrueType Text fonts in LuaLaTeX or XeLaTeX
documents. Note: "Lato" means "Summer" in Polish, same as "l'ete" in French.

%package -n texlive-lexend
Summary:        The Lexend fonts for XeLaTeX and LuaLaTeX through fontspec
Version:        svn57564
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(lexend.sty) = %{tl_version}

%description -n texlive-lexend
The purpose of this package is pretty straightforward: The Lexend font
collection has been designed by Dr. Bonnie Shaver-Troup and Thomas Jockin to
make reading easier for everyone. Now my goal is to bring this wonderful
collection to the world of LaTeX.

%package -n texlive-lfb
Summary:        A Greek font with normal and bold variants
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lfb
This is a Greek font written in Metafont, with inspiration from the Bodoni
typefaces in old books. It is stylistically a little more exotic than the
standard textbook Greek fonts, particularly in glyphs like the lowercase rho
and kappa. It aims for a rather calligraphic feel, but seems to blend well with
Computer Modern. There is a ligature scheme which automatically inserts the
breathings required for ancient texts, making the input text more readable than
in some schemes.

%package -n texlive-libertine
Summary:        Use of Linux Libertine and Biolinum fonts with LaTeX
Version:        svn73037
License:        GPL-2.0-or-later AND OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fontaxes
Requires:       texlive-iftex
Requires:       texlive-mweights
Requires:       texlive-xkeyval
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(LKey.tex) = %{tl_version}
Provides:       tex(LinBiolinum_K.tex) = %{tl_version}
Provides:       tex(LinBiolinum_R.tex) = %{tl_version}
Provides:       tex(LinLibertine_I.tex) = %{tl_version}
Provides:       tex(LinLibertine_R.tex) = %{tl_version}
Provides:       tex(biolinum.sty) = %{tl_version}
Provides:       tex(libertine.sty) = %{tl_version}
Provides:       tex(libertineMono.sty) = %{tl_version}
Provides:       tex(libertineRoman.sty) = %{tl_version}

%description -n texlive-libertine
The package provides the Libertine and Biolinum fonts in both Type 1 and OTF
styles, together with support macros for their use. Monospaced and display
fonts, and the "keyboard" set are also included, in OTF style, only. The
mweights package is used to manage the selection of font weights. The package
supersedes both the libertineotf and the libertine-legacy packages.

%package -n texlive-libertinegc
Summary:        Libertine add-on to support Greek and Cyrillic
Version:        svn44616
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(libertine.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(libertinegc.sty) = %{tl_version}

%description -n texlive-libertinegc
The package provides LaTeX support files to access the Greek and Cyrillic
glyphs in LinuxLibertine. It functions as an add-on to the libertine package,
using filenames and macro names that are compatible with that package.
Supported encodings: LGR, T2A, T2B, T2C, OT2.

%package -n texlive-libertinus
Summary:        Wrapper to use the correct libertinus package according to the used TeX engine
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(libertinus.sty) = %{tl_version}

%description -n texlive-libertinus
This package is only a wrapper for the two packages libertinus-type1 (pdfLaTeX)
and libertinus-otf (LuaLaTeX/XeLaTeX). The Libertinus fonts are similar to
Libertine and Biolinum, but come with math symbols.

%package -n texlive-libertinus-fonts
Summary:        The Libertinus font family
Version:        svn72484
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-libertinus-fonts
This is a fork of the Linux Libertine and Linux Biolinum fonts that started as
an OpenType math companion of the Libertine font family, but grown as a full
fork to address some of the bugs in the fonts. The family consists of:
Libertinus Serif: forked from Linux Libertine. Libertinus Sans: forked from
Linux Biolinum. Libertinus Mono: forked from Linux Libertine Mono. Libertinus
Math: an OpenType math font for use in OpenType math-capable applications like
LuaTeX, XeTeX or MS Word 2007+.

%package -n texlive-libertinus-otf
Summary:        Support for Libertinus OpenType
Version:        svn77115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(libertinus-otf.sty) = %{tl_version}

%description -n texlive-libertinus-otf
This package offers LuaLaTeX/XeLaTeX support for the Libertinus OpenType fonts
maintained by Khaled Hosny. Missing fonts are defined via several font feature
settings. The Libertinus fonts are similar to Libertine and Biolinum, but come
with math symbols.

%package -n texlive-libertinus-type1
Summary:        Support for using Libertinus fonts with LaTeX/pdfLaTeX
Version:        svn76891
License:        GPL-2.0-only AND OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(libertinus-type1.sty) = %{tl_version}

%description -n texlive-libertinus-type1
This package provides support for use of Libertinus fonts with traditional
processing engines (LaTeX with dvips or dvipdfmx, or pdfLaTeX).

%package -n texlive-libertinust1math
Summary:        A Type 1 font and LaTeX support for Libertinus Math
Version:        svn71428
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(libertinust1math.sty) = %{tl_version}

%description -n texlive-libertinust1math
The package provides a Type1 version of Libertinus Math, with a number of
additions and changes, plus LaTeX support files that allow it to serve as a
math accompaniment to Libertine under LaTeX. In addition, with option sansmath,
it can function as a standalone math font with sans serif Roman and Greek
letters.

%package -n texlive-librebaskerville
Summary:        The Libre Baskerville family of fonts with LaTeX support
Version:        svn64421
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(librebaskerville.sty) = %{tl_version}

%description -n texlive-librebaskerville
This package provides the Libre Baskerville family of fonts, designed by Pablo
Impallari, for use with LaTeX, pdfLaTeX, XeLaTeX or LuaLaTeX. It is primarily
intended to be a web font but is also attractive as a text font. A BoldItalic
variant has been artificially generated.

%package -n texlive-librebodoni
Summary:        Libre Bodoni fonts with LaTeX support
Version:        svn64431
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(LibreBodoni.sty) = %{tl_version}

%description -n texlive-librebodoni
The Libre Bodoni fonts are designed by Pablo Impallari and Rodrigo Fuenzalida,
based on the 19th century Morris Fuller Benton's.

%package -n texlive-librecaslon
Summary:        Libre Caslon fonts, with LaTeX support
Version:        svn64432
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(librecaslon.sty) = %{tl_version}

%description -n texlive-librecaslon
The Libre Caslon fonts are designed by Pablo Impallari. Although they have been
designed for use as web fonts, they work well as conventional text fonts. An
artificially generated BoldItalic variant has been added.

%package -n texlive-librefranklin
Summary:        LaTeX support for the Libre-Franklin family of fonts
Version:        svn64441
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(librefranklin.sty) = %{tl_version}

%description -n texlive-librefranklin
Libre Franklin is an interpretation and expansion based on the 1912 Morris
Fuller Benton's classic, designed by Pablo Impallari, Rodrigo Fuenzalida and
Nhung Nguyen.

%package -n texlive-libris
Summary:        Libris ADF fonts, with LaTeX support
Version:        svn72484
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(libris.sty) = %{tl_version}

%description -n texlive-libris
LibrisADF is a sans-serif family designed to mimic Lydian. The bundle includes:
fonts, in Adobe Type 1, TrueType and OpenType formats, and LaTeX support
macros, for use with the Type 1 versions of the fonts. The LaTeX macros depend
on the nfssext-cfr bundle. GPL licensing applies the fonts themselves; the
support macros are distributed under LPPL licensing.

%package -n texlive-lineara
Summary:        Linear A script fonts
Version:        svn63169
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(linearA.sty) = %{tl_version}

%description -n texlive-lineara
The linearA package provides a simple interface to two fonts which include all
known symbols, simple and complex, of the Linear A script. This way one can
easily replicate Linear A "texts" using modern typographic technology. Note
that the Linear A script has not been deciphered yet and probably never will be
deciphered.

%package -n texlive-linguisticspro
Summary:        LinguisticsPro fonts with LaTeX support
Version:        svn64858
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(linguisticspro.sty) = %{tl_version}

%description -n texlive-linguisticspro
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
LinguisticsPro family of fonts. This family is derived from the Utopia Nova
font family, by Andreas Nolda.

%package -n texlive-lobster2
Summary:        Lobster Two fonts, with support for all LaTeX engines
Version:        svn64442
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(LobsterTwo.sty) = %{tl_version}

%description -n texlive-lobster2
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Lobster Two family of fonts, designed by Pablo Impallari. This is a family of
script fonts with many ligatures and terminal forms; for the best results, use
XeLaTeX or LuaLaTeX. There are two weights and italic variants for both.

%package -n texlive-logix
Summary:        Supplement to the Unicode math symbols
Version:        svn63688
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(arydshln.sty)
Requires:       tex(iftex.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(logix.sty) = %{tl_version}

%description -n texlive-logix
The package provides a Unicode font with over 4,000 symbols to supplement the
Unicode math symbols. It is compatible with and complements the AMS STIX2 math
fonts, but focuses on new symbols and symbol variants more suited to work in
logic.

%package -n texlive-luciole
Summary:        Luciole OpenType fonts for LuaTeX and XeTeX
Version:        svn76679
License:        CC-BY-4.0 AND OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(luciole-math.sty) = %{tl_version}

%description -n texlive-luciole
This package provides four Unicode Math text fonts Luciole-*.ttf and a
companion math font Luciole-Math.otf. These have been developed explicitly for
visually impaired people and are the result of a two-year collaboration between
the Centre Technique Regional pour la Deficience Visuelle (the Regional
Technical Center for Visual Impairment) and the type-design studio
typographies.fr. This project received a grant from the Swiss Ceres Foundation
and support from the DIPHE laboratory at the Universite Lumiere Lyon 2.

%package -n texlive-luwiantype
Summary:        Typesetting package for Hieroglyphic Luwian
Version:        svn73719
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(moresize.sty)
Requires:       tex(stackengine.sty)
Provides:       tex(luwiantype.sty) = %{tl_version}

%description -n texlive-luwiantype
This package allows for typing in Hieroglyphic Luwian in LaTeX documents, using
relatively simple commands based on the Latin transcriptions of the various
signs. It also includes some formatting commands designed to allow
boustrophedon and columns, as well as shorthands for symbols commonly used in
transcriptions.

%package -n texlive-lxfonts
Summary:        Set of slide fonts based on CM
Version:        svn73728
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(lxfonts.sty) = %{tl_version}

%description -n texlive-lxfonts
The bundle contains the traditional slides fonts revised to be completely
usable both as text fonts and mathematics fonts; they are fully integrated with
the new operators, letters, symbols and extensible delimiter fonts, as well as
with the AMS fonts, all redone with the same stylistic parameters.

%package -n texlive-ly1
Summary:        Support for LY1 LaTeX encoding
Version:        svn63565
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(ly1enc.def) = %{tl_version}
Provides:       tex(texnansi.sty) = %{tl_version}
Provides:       tex(texnansi.tex) = %{tl_version}

%description -n texlive-ly1
The Y&Y 'texnansi' (TeX and ANSI, for Microsoft interpretations of ANSI
standards) encoding lives on, even after the decease of the company; it is
known in the LaTeX scheme of things as LY1 encoding. This bundle includes
metrics and LaTeX macros to use the basic three (Times, Helvetica and Courier)
Adobe Type 1 fonts in LaTeX using LY1 encoding.

%package -n texlive-lydtype
Summary:        Typing in the Lydian alphabet
Version:        svn76924
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(lydtype.sty) = %{tl_version}

%description -n texlive-lydtype
This package aims to allow platform-agnostic typing in the Lydian alphabet
using LaTeX, in particular as a way to deal with the fact that Overleaf does
not support direct input of certain characters outside of a given Unicode
range. The package was developed for use with LuaLaTeX and XeLaTeX,
functionality with other compilers is not guaranteed. The package includes the
Noto Sans Lydian font as developed by Google.

%package -n texlive-magra
Summary:        The Magra font face with support for LaTeX and pdfLaTeX
Version:        svn57373
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(Magra.sty) = %{tl_version}

%description -n texlive-magra
This package provides the Magra family of fonts designed by FontFuror, with
support for LaTeX and pdfLaTeX.

%package -n texlive-marcellus
Summary:        Marcellus fonts with LaTeX support
Version:        svn64451
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(marcellus.sty) = %{tl_version}

%description -n texlive-marcellus
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Marcellus family of fonts, designed by Brian J. Bonislawsky. Marcellus is a
flared-serif family, inspired by classic Roman inscription letterforms. There
is currently just a regular weight and small-caps. The regular weight will be
silently substituted for bold.

%package -n texlive-mathabx
Summary:        Three series of mathematical symbols
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mathabx.sty) = %{tl_version}
Provides:       tex(mathabx.tex) = %{tl_version}

%description -n texlive-mathabx
Mathabx is a set of 3 mathematical symbols font series: matha, mathb and mathx.
They are defined by Metafont code and should be of reasonable quality (bitmap
output). Things change from time to time, so there is no claim of stability
(encoding, metrics, design). The package includes Plain TeX and LaTeX support
macros. A version of the fonts, in Adobe Type 1 format, is also available.

%package -n texlive-mathabx-type1
Summary:        Outline version of the mathabx fonts
Version:        svn21129
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-mathabx

%description -n texlive-mathabx-type1
This is an Adobe Type 1 outline version of the mathabx fonts.

%package -n texlive-mathdesign
Summary:        Mathematical fonts to fit with particular text fonts
Version:        svn31639
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(mathdesign.sty) = %{tl_version}
Provides:       tex(mdbch.sty) = %{tl_version}
Provides:       tex(mdfont.def) = %{tl_version}
Provides:       tex(mdici.sty) = %{tl_version}
Provides:       tex(mdpgd.sty) = %{tl_version}
Provides:       tex(mdpus.sty) = %{tl_version}
Provides:       tex(mdput.sty) = %{tl_version}
Provides:       tex(mdsffont.def) = %{tl_version}
Provides:       tex(mdttfont.def) = %{tl_version}
Provides:       tex(mdugm.sty) = %{tl_version}

%description -n texlive-mathdesign
The Math Design project offers free mathematical fonts that match with existing
text fonts. To date, three free font families are available: Adobe Utopia, URW
Garamond and Bitstream Charter. Three commercial fonts are also supported:
Adobe Garamond Pro, Adobe UtopiaStd and ITC Charter. Mathdesign covers the
whole LaTeX glyph set, including AMS symbols and some extra. Both roman and
bold versions of these symbols can be used. Moreover you can choose between
three greek fonts (two of them created by the Greek Font Society).

%package -n texlive-mdputu
Summary:        Upright digits in Adobe Utopia Italic
Version:        svn20298
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mdputu.sty) = %{tl_version}

%description -n texlive-mdputu
The Annals of Mathematics uses italics for theorems. However, slanted digits
and parentheses look disturbing when surrounded by (upright) mathematics. This
package provides virtual fonts with italics and upright digits and punctuation,
as an extension to Mathdesign's Utopia bundle.

%package -n texlive-mdsymbol
Summary:        Symbol fonts to match Adobe Myriad Pro
Version:        svn28399
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fltpoint.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(mdsymbol.sty) = %{tl_version}

%description -n texlive-mdsymbol
The package provides a font of mathematical symbols, MyriadPro The font is
designed as a companion to Adobe Myriad Pro, but it might also fit well with
other contemporary typefaces.

%package -n texlive-merriweather
Summary:        Merriweather and MerriweatherSans fonts, with LaTeX support
Version:        svn75301
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(merriweather.sty) = %{tl_version}

%description -n texlive-merriweather
This package provides the Merriweather and MerriweatherSans families of fonts,
designed by Eben Sorkin, with support for LaTeX, pdfLaTeX, XeLaTeX, and
LuaLaTeX. Merriweather features a very large x height, slightly condensed
letterforms, a mild diagonal stress, sturdy serifs and open forms. The Sans
family closely harmonizes with the weights and styles of the serif family.
There are four weights and italics for each.

%package -n texlive-metsymb
Summary:        The package provides dedicated TeX commands to generate (vectorial) meteorological symbols
Version:        svn68175
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(metsymb.sty) = %{tl_version}

%description -n texlive-metsymb
The metsymb package introduces commands to generate official meteorological
symbols with vectorial quality. These include: oktas (\zerookta, \oneokta,
\twooktas, \ldots), cloud genera (\cirrus, \cirrostratus, \nimbostratus, ...),
and C_L / C_M / C_H cloud codes (\clIII, \cmVI, \chIX, ...). Individual symbols
are designed using TikZ. They are then bundled into a dedicated font with
FontForge, and eventually tied to dedicted LaTeX commands. The metsymb OpenType
font is a side-product that can be used on its own. This package essentially
introduces a new font in which each symbol is assigned to a glyph, which can
then be called individually from LaTeX documents via dedicated commands.

%package -n texlive-mfb-oldstyle
Summary:        MFB Oldstyle serif fonts
Version:        svn71982
License:        CC0-1.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(mfb-oldstyle.sty) = %{tl_version}

%description -n texlive-mfb-oldstyle
Oldstyle is a serif font family designed for body text. This typeface was
originally designed by Morris Fuller Benton and released by American Type
Founders in 1909 as Century Oldstyle. The family contains three fonts: regular,
italic and bold. (Currently, no bold italic font is provided.) Superior and
inferior figures are available for all fonts in the family. Small capitals and
old-style figures are available only for the regular font.

%package -n texlive-miama
Summary:        The Miama Nueva handwriting font with LaTeX support
Version:        svn73481
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(miama.sty) = %{tl_version}

%description -n texlive-miama
Miama Nueva is a handwriting / script font with over 1300 glyphs that supports
latin, cyrillic, and greek. It comes complete with LaTeX support.

%package -n texlive-mintspirit
Summary:        LaTeX support for MintSpirit font families
Version:        svn64461
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(mintspirit.sty) = %{tl_version}
Provides:       tex(mintspirit2.sty) = %{tl_version}

%description -n texlive-mintspirit
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
MintSpirit and MintSpiritNo2 families of fonts, designed by Hirwen Harendal.
MintSpirit was originally designed for use as a system font on a Linux Mint
system. The No. 2 variant provides more conventional shapes for some glyphs.

%package -n texlive-missaali
Summary:        A late medieval OpenType textura font
Version:        svn61719
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accsupp.sty)
Requires:       tex(calc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multicol.sty)
Provides:       tex(missaali.sty) = %{tl_version}

%description -n texlive-missaali
This package contains the free OpenType Textura font Missaali and a style file
for using it with XeLaTeX. Textura is a typeface based on the textus quadratus
form of the textualis formata that late medieval scribes used for the most
valuable manuscripts. The font Missaali is based on Textura that German printer
Bartholomew Ghotan used for printing missals and psalters in the 1480s. This
font has two intended use cases: as a Gothic display font; and for emulating
late-medieval manuscripts. In addition to the basic textura letters, the font
contains a large number of abbreviation sigla as well as a set of Lombardic
initials. As modern typesetting algorithms are not intended for creating 15th
century style layout, the package contains a XeLaTeX style file that makes it
easier to achieve the classic incunabula look.

%package -n texlive-mlmodern
Summary:        A blacker Type 1 version of Computer Modern, with multilingual support
Version:        svn57458
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mlmodern.sty) = %{tl_version}

%description -n texlive-mlmodern
MLModern is a text and math font family with (La)TeX support, based on the
design of Donald Knuth's Computer Modern and the Latin Modern project. It
avoids the spindliness of most other Type 1 versions of Computer Modern.

%package -n texlive-mnsymbol
Summary:        Mathematical symbol font for Adobe MinionPro
Version:        svn18651
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(eufrak.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(MnSymbol.sty) = %{tl_version}

%description -n texlive-mnsymbol
MnSymbol is a symbol font family, designed to be used in conjunction with Adobe
Minion Pro (via the MinionPro package). Almost all of LaTeX and AMS
mathematical symbols are provided; remaining coverage is available from the
MinionPro font with the MinionPro package. The fonts are available both as
Metafont source and as Adobe Type 1 format, and a comprehensive support package
is provided. While the fonts were designed to fit with Minon Pro, the design
should fit well with other renaissance or baroque faces: indeed, it will
probably work with most fonts that are neither too wide nor too thin, for
example Palatino or Times; it is known to look good with Sabon. There is no
package designed to configure its use with any font other than Minion Pro, but
(for example) simply loading mnsymbol after mathpazo will probably do what is
needed.

%package -n texlive-monaspace-otf
Summary:        OpenType MonaSpace fonts with fontspec support
Version:        svn77006
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(monaspace-otf.sty) = %{tl_version}

%description -n texlive-monaspace-otf
This package provides the OpenType MonaSpace fonts with fontspec support for
LuaLaTeX and XeTeX, with or without ligatures. The fonts come in five styles
(Argon, Krypton, Neon, Radon, Xenon) and five weights (ExtraLight, Light,
Regular, Medium, SemiBold), and with healing support. See
https://monaspace.githubnext.com for further information.

%package -n texlive-montserrat
Summary:        Montserrat sans serif, otf and pfb, with LaTeX support files
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(montserrat.sty) = %{tl_version}

%description -n texlive-montserrat
Montserrat is a geometric sans-serif typeface designed by Julieta Ulanovsky,
inspired by posters and signage from her historical Buenos Aires neighborhood
of the same name. It is rather close in spirit to Gotham and Proxima Nova, but
has its own individual appearance -- more informal, less extended, and more
idiosyncratic. It is provided in a total of nine different weights, each having
eight figure styles and small caps in both upright and italic shapes. There are
two quite different versions that don't fit into the usual LaTeX
classifications. The version having the appellation "Alternates" has letter
shapes that are much more rounded than the default version, reflecting the
signage in the neighborhood of Montserrat.

%package -n texlive-mpfonts
Summary:        Computer Modern Type 3 fonts converted using MetaPost
Version:        svn54512
License:        Knuth-CTAN AND LPPL-1.3c AND OFL-1.1 AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpfonts
The Computer Modern fonts are available in Type 1 format, but these renditions
are somewhat thin and spindly, and produce much lighter results than the
originals. It is alternatively possible to use Metafont bitmaps, but this has
its disadvantages in comparison with vector fonts. These fonts are conversions
to Type 3 fonts, done entirely in MetaPost; they are vector fonts which are a
direct conversion from the original Metafont files, so they are the design most
authentic to the originals. However, these fonts, because they are PostScript
Type 3 fonts, are not suitable for on-screen reading, and should probably only
be used for printing. Note: do NOT add the map file to updmap!

%package -n texlive-mweights
Summary:        Support for multiple-weight font packages
Version:        svn53520
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mweights.sty) = %{tl_version}

%description -n texlive-mweights
Many font families available for use with LaTeX are available at multiple
weights. Many Type 1-oriented support packages for such fonts re-define the
standard \mddefault or \bfdefault macros. This can create difficulties if the
weight desired for one font family isn't available for another font family, or
if it differs from the weight desired for another font family. The package
provides a solution to these difficulties.

%package -n texlive-newcomputermodern
Summary:        Computer Modern fonts including matching non-latin alphabets
Version:        svn77296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(newcomputermodern.sty) = %{tl_version}

%description -n texlive-newcomputermodern
This is a new assembly of Computer Modern fonts including extensions in many
directions for both Latin based languages, non-Latin based languages and
Mathematics, all compatible in style to CM fonts. In addition to the Regular
weight of Computer Modern, it provides a Book weight for heavier printing.

%package -n texlive-newpx
Summary:        Alternative uses of the PX fonts, with improved metrics
Version:        svn76713
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(centernot.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(newpx-subs.tex) = %{tl_version}
Provides:       tex(newpx.sty) = %{tl_version}
Provides:       tex(newpxmath.sty) = %{tl_version}
Provides:       tex(newpxtext.sty) = %{tl_version}

%description -n texlive-newpx
This package, initially based on pxfonts, provides many fixes and enhancements
to that package, and splits it in two parts (newpxtext and newpxmath) which may
be run independently of one another. It provides scaling, improved metrics, and
other options. For proper operation, the packages require that the packages
newtxmath, pxfonts, and TeXGyrePagella be installed and their map files
enabled.

%package -n texlive-newtx
Summary:        Alternative uses of the TX fonts, with improved metrics
Version:        svn73393
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-kastrup
Requires:       tex(amsmath.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(centernot.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(newtx-ebgaramond-subs.tex) = %{tl_version}
Provides:       tex(newtx-libertine-subs.tex) = %{tl_version}
Provides:       tex(newtx-subs.tex) = %{tl_version}
Provides:       tex(newtx.sty) = %{tl_version}
Provides:       tex(newtxmath.sty) = %{tl_version}
Provides:       tex(newtxtext.sty) = %{tl_version}

%description -n texlive-newtx
The bundle splits txfonts.sty (from the TX fonts distribution) into two
independent packages, newtxtext.sty and newtxmath.sty, each with fixes and
enhancements. newtxmath's metrics have been re-evaluated to provide a less
tight appearance, and to provide a libertine option that substitutes Libertine
italic and Greek letter for the existing math italic and Greek glyphs, making a
mathematics package that matches Libertine text quite well. newtxmath can also
use the maths italic font provided with the garamondx package, thus offering a
garamond-alike text-with-maths combination.

%package -n texlive-newtxsf
Summary:        Sans-math fonts for use with newtx
Version:        svn69597
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(newtxsf.sty) = %{tl_version}

%description -n texlive-newtxsf
The package provides a maths support that amounts to modifications of the STIX
sans serif Roman and Greek letters with most symbols taken from newtxmath
(which must of course be installed and its map file enabled).

%package -n texlive-newtxtt
Summary:        Enhancement of typewriter fonts from newtx
Version:        svn70620
License:        GPL-3.0-only AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(newtxtt.sty) = %{tl_version}

%description -n texlive-newtxtt
The package provides enhanced fonts with LaTeX support files providing access
to the typewriter fonts from newtx. Regular and bold weights, slanted variants
and a choice of four different styles for zero.

%package -n texlive-niceframe-type1
Summary:        Type 1 versions of the fonts recommended in niceframe
Version:        svn71849
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-niceframe-type1
The bundle provides Adobe Type 1 versions of the fonts bbding10, dingbat,
karta15, umranda and umrandb.

%package -n texlive-nimbus15
Summary:        Support files for Nimbus 2015 Core fonts
Version:        svn72894
License:        AGPL-3.0-or-later WITH PS-or-PDF-font-exception-20170817 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fontools
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(nimbusmono.sty) = %{tl_version}
Provides:       tex(nimbusmononarrow.sty) = %{tl_version}
Provides:       tex(nimbussans.sty) = %{tl_version}
Provides:       tex(nimbusserif.sty) = %{tl_version}

%description -n texlive-nimbus15
The Nimbus 2015 Core fonts added Greek and Cyrillic glyphs. This package may be
best suited as an add-on to the comprehensive Times package, providing support
for Greek and Cyrillic. A new intermediate weight of NimbusMono (AKA Courier)
is provided, along with a narrower version which may be useful for rendering
code.

%package -n texlive-nkarta
Summary:        A "new" version of the karta cartographic fonts
Version:        svn16437
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nkarta
A development of the karta font, offering more mathematical stability in
Metafont. A version that will produce the glyphs as Encapsulated PostScript,
using MetaPost, is also provided.

%package -n texlive-noto
Summary:        Support for Noto fonts
Version:        svn64351
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(noto-mono.sty) = %{tl_version}
Provides:       tex(noto-sans.sty) = %{tl_version}
Provides:       tex(noto-serif.sty) = %{tl_version}
Provides:       tex(noto.sty) = %{tl_version}

%description -n texlive-noto
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
NotoSerif, NotoSans and NotoSansMono families of fonts, designed by Steve
Matteson for Google.

%package -n texlive-noto-emoji
Summary:        Noto Emoji fonts
Version:        svn62950
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-noto-emoji
Noto Color Emoji supports all emoji defined in the latest Unicode version.

%package -n texlive-notomath
Summary:        Math support for Noto fonts
Version:        svn71429
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(noto-mono.sty)
Requires:       tex(noto-sans.sty)
Requires:       tex(noto-serif.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(notomath.sty) = %{tl_version}

%description -n texlive-notomath
Math support via newtxmath for Google's NotoSerif and NotoSans. (Regular and
Bold weights only.)

%package -n texlive-nunito
Summary:        The Nunito font face with support for LaTeX and pdfLaTeX
Version:        svn57429
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(nunito.sty) = %{tl_version}

%description -n texlive-nunito
This package provides LaTeX and pdfLaTeX support for the Nunito family of
fonts, designed by Vernon Adams, Cyreal.

%package -n texlive-obnov
Summary:        Obyknovennaya Novaya fonts
Version:        svn33355
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-obnov
The Obyknovennaya Novaya (Ordinary New Face) typeface was widely used in the
USSR for scientific and technical publications, as well as textbooks. The fonts
are encoded to KOI8-R (which is a long-established Russian font encoding,
rather than a TeX/LaTeX encoding). To use the fonts, the user needs Cyrillic
font support.

%package -n texlive-ocherokee
Summary:        LaTeX Support for the Cherokee language
Version:        svn25689
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lchenc.def) = %{tl_version}
Provides:       tex(ocherokee.sty) = %{tl_version}

%description -n texlive-ocherokee
Macros and Type 1 fonts for Typesetting the Cherokee language with the Omega
version of LaTeX (known as Lambda).

%package -n texlive-ocr-b
Summary:        Fonts for OCR-B
Version:        svn20852
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ocr-b
Metafont source for OCR-B at several sizes.

%package -n texlive-ocr-b-outline
Summary:        OCR-B fonts in Type 1 and OpenType
Version:        svn20969
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ocr-b-outline
The package contains OCR-B fonts in Type1 and OpenType formats. They were
generated from the Metafont sources of the OCR-B fonts. The metric files are
not included here, so that original ocr-b package should also be installed.

%package -n texlive-ogham
Summary:        Fonts for typesetting Ogham script
Version:        svn24876
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ogham
The font provides the Ogham alphabet, which is found on a number of Irish and
Pictish carvings dating from the 4th century AD. The font is distributed as
Metafont source, which has been patched (with the author's permission) for
stability at different output device resolutions. (Thanks are due to Peter
Flynn and Dan Luecking.)

%package -n texlive-oinuit
Summary:        LaTeX Support for the Inuktitut Language
Version:        svn28668
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(litenc.def) = %{tl_version}
Provides:       tex(oinuit.sty) = %{tl_version}

%description -n texlive-oinuit
The package provides a set of Lambda (Omega LaTeX) typesetting tools for the
Inuktitut language. Five different input methods are supported and with the
necessary fonts are also provided.

%package -n texlive-old-arrows
Summary:        Computer Modern old-style arrows with smaller arrowheads
Version:        svn42872
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(old-arrows.sty) = %{tl_version}

%description -n texlive-old-arrows
This package provides Computer Modern old-style arrows with smaller arrowheads,
associated with the usual LaTeX commands. It can be used in documents that
contain other amssymb arrow characters that also have small arrowheads. It is
also possible to use the usual new-style Computer Modern arrows together with
the old-style ones.

%package -n texlive-oldlatin
Summary:        Compute Modern-like font with long s
Version:        svn17932
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-oldlatin
Metafont sources modified from Computer Modern in order to generate "long s"
which was used in old text.

%package -n texlive-oldstandard
Summary:        OldStandard fonts with LaTeX support
Version:        svn70421
License:        OFL-1.1 AND LPPL-1.3c AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(OldStandard.sty) = %{tl_version}

%description -n texlive-oldstandard
Old Standard is designed to reproduce the actual printing style of the early
20th century, reviving a specific type of Modern (classicist) style of serif
typefaces, very commonly used in various editions of the late 19th and early
20th century, but almost completely abandoned later. The font supports
typesetting of Old and Middle English, Old Icelandic, Cyrillic (with historical
characters, extensions for Old Slavonic and localised forms), Gothic
transliterations, critical editions of Classical Greek and Latin, and many
more. This package works with TeX engines that directly support OpenType
features, such as XeTeX and LuaTeX, as well as traditional engines such as TeX
and pdfTeX.

%package -n texlive-opensans
Summary:        The Open Sans font family, and LaTeX support
Version:        svn54512
License:        Apache-2.0 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(opensans.sty) = %{tl_version}

%description -n texlive-opensans
Open Sans is a humanist sans serif typeface designed by Steve Matteson; the
font is available from the Google Font Directory as TrueType files licensed
under the Apache License version 2.0. The package provides support for this
font family in LaTeX. It includes the original TrueType fonts, as well as Type
1 versions, converted for this package using FontForge for full support with
dvips

%package -n texlive-orkhun
Summary:        A font for orkhun script
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-orkhun
The font covers an old Turkic script. It is provided as Metafont source.

%package -n texlive-oswald
Summary:        The Oswald family of fonts with support for LaTeX and pdfLaTeX
Version:        svn60784
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(Oswald.sty) = %{tl_version}

%description -n texlive-oswald
This package provides the Oswald family of fonts, designed by Vernon Adams,
Kalapi Gajjar, Cyreal, with support for LaTeX and pdfLaTeX.

%package -n texlive-overlock
Summary:        Overlock sans fonts with LaTeX support
Version:        svn64495
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(overlock.sty) = %{tl_version}

%description -n texlive-overlock
The package provides the Overlock and OverlockSC families of fonts, designed by
Dario Manuel Muhafara of the TIPO foundry (http://www.tipo.net.ar), "rounded"
sans-serif fonts in three weights (Regular, Bold, Black) with italic variants
for each of them. There are also small-caps and old-style figures in the
Regular weight.

%package -n texlive-pacioli
Summary:        Fonts designed by Fra Luca de Pacioli in 1497
Version:        svn24947
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pacioli.sty) = %{tl_version}

%description -n texlive-pacioli
Pacioli was a c.15 mathematician, and his font was designed according to 'the
divine proportion'. The font is uppercase letters together with punctuation and
some analphabetics; no lowercase or digits. The Metafont source is distributed
in a .dtx file, together with LaTeX support.

%package -n texlive-pagella-otf
Summary:        Using the OpenType fonts TeX Gyre Pagella
Version:        svn64705
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(pagella-otf.sty) = %{tl_version}

%description -n texlive-pagella-otf
This package can only be used with LuaLaTeX or XeLaTeX. It does the font
setting for the OpenType font 'TeX Gyre Pagella' for text and math. The missing
typefaces like bold math and slanted text are also defined

%package -n texlive-paratype
Summary:        LaTeX support for free fonts by ParaType
Version:        svn68624
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(PTMono.sty) = %{tl_version}
Provides:       tex(PTSans.sty) = %{tl_version}
Provides:       tex(PTSansCaption.sty) = %{tl_version}
Provides:       tex(PTSansNarrow.sty) = %{tl_version}
Provides:       tex(PTSerif.sty) = %{tl_version}
Provides:       tex(PTSerifCaption.sty) = %{tl_version}
Provides:       tex(paratype.sty) = %{tl_version}

%description -n texlive-paratype
The package offers LaTeX support for the fonts PT Sans, PT Serif and PT Mono
developed by ParaType for the project "Public Types of Russian Federation", and
released under an open user license. The fonts themselves are provided in both
the TrueType and Type 1 formats, both created by ParaType). The fonts provide
encodings OT1, T1, IL2, TS1, T2* and X2. The package provides a convenient
replacement of the two packages ptsans and ptserif.

%package -n texlive-pennstander-otf
Summary:        OpenType versions of the pennstander fonts (with math support)
Version:        svn77285
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(pennstander-otf.sty) = %{tl_version}

%description -n texlive-pennstander-otf
This bundle provides OpenType versions Pennstander fonts designed by Julius
Ross. It is usable with LuaTeX or XeTeX engines only.

%package -n texlive-phaistos
Summary:        Disk of Phaistos font
Version:        svn18651
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(phaistos.sty) = %{tl_version}

%description -n texlive-phaistos
A font that contains all the symbols of the famous Disc of Phaistos, together
with a LaTeX package. The disc was 'printed' by stamping the wet clay with some
sort of punches, probably around 1700 BCE. The font is available in Adobe Type
1 and OpenType formats (the latter using the Unicode positions for the
symbols). There are those who believe that this Cretan script was used to
'write' Greek (it is known, for example, that the rather later Cretan Linear B
script was used to write Greek), but arguments for other languages have been
presented.

%package -n texlive-phonetic
Summary:        Metafont Phonetic fonts, based on Computer Modern
Version:        svn56468
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(phonetic.sty) = %{tl_version}

%description -n texlive-phonetic
The fonts are based on Computer Modern, and specified in Metafont. Macros for
the fonts' use are provided, both for LaTeX 2.09 and for current LaTeX.

%package -n texlive-pigpen
Summary:        A font for the pigpen (or masonic) cipher
Version:        svn69687
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pigpen.sty) = %{tl_version}
Provides:       tex(pigpen.tex) = %{tl_version}

%description -n texlive-pigpen
The Pigpen cipher package provides the font and the necessary wrappers (style
file, etc.) in order to write Pigpen ciphers, a simple substitution cipher. The
package provides a font (available both as Metafont source, and as an Adobe
Type 1 file), and macros for its use.

%package -n texlive-playfair
Summary:        Playfair Display fonts with LaTeX support
Version:        svn64857
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(PlayfairDisplay.sty) = %{tl_version}

%description -n texlive-playfair
This package provides the PlayFairDisplay family of fonts, designed by Claus
Eggers Sorensen, for use with LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX.
PlayFairDisplay is well suited for titling and headlines. It has an extra large
x-height and short descenders. It can be set with no leading if space is tight,
for instance in news headlines, or for stylistic effect in titles. Capitals are
extra short, and only very slightly heavier than the lowercase characters. This
helps achieve a more even typographical colour when typesetting proper nouns
and initialisms.

%package -n texlive-plex
Summary:        Support for IBM Plex fonts
Version:        svn77018
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(plex-mono.sty) = %{tl_version}
Provides:       tex(plex-sans.sty) = %{tl_version}
Provides:       tex(plex-serif.sty) = %{tl_version}

%description -n texlive-plex
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the IBM
Plex families of fonts. Serif, Sans and Mono families are available in eight
weights: Regular, Light, ExtraLight, Thin, Bold, Text, Medium and SemiBold
(with corresponding italics).

%package -n texlive-plex-otf
Summary:        Support for the OpenType font IBM Plex
Version:        svn74719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(plex-otf.sty) = %{tl_version}

%description -n texlive-plex-otf
This package supports the free otf fonts from the IBM Plex project which are
available from GitHub or already part of your system (Windows/Linux/...). This
package supports only XeLaTeX or LuaLaTeX; for pdfLaTeX use plex-mono.sty,
plex-sans.sty, and/or plex-serif.sty from the plex package.

%package -n texlive-plimsoll
Summary:        Fonts with the Plimsoll symbol and LaTeX support
Version:        svn56605
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(plimsoll.sty) = %{tl_version}

%description -n texlive-plimsoll
This package provides access to the Plimsoll symbol for use with LaTeX. The
Plimsoll symbol is sometimes used in chemistry for denoting standard states and
values. The LaTeX package provides access to this notation as well. The syntax
for denoting the standard state is the same as suggested in the Comprehensive
LaTeX Symbol List for emulating the Plimsoll mark.

%package -n texlive-poiretone
Summary:        PoiretOne family of fonts with LaTeX support
Version:        svn64856
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(PoiretOne.sty) = %{tl_version}

%description -n texlive-poiretone
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
PoiretOne family of fonts, designed by Denis Masharov. PoiretOne is a
decorative geometric grotesque with a hint of Art Deco and constructivism.
There is currently just a regular weight and an artificially emboldened bold.

%package -n texlive-poltawski
Summary:        Antykwa Poltawskiego Family of Fonts
Version:        svn67718
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(antpolt.sty) = %{tl_version}

%description -n texlive-poltawski
The package contains the Antykwa Poltawskiego family of fonts in the PostScript
Type 1 and OpenType formats. The original font was designed in the twenties of
the XX century by the Polish typographer Adam Poltawski(1881-1952). Following
the route set out by the Latin Modern and TeX Gyre projects
(https://www.gust.org.pl/projects/e-foundry), the Antykwa Poltawskiego
digitisation project aims at providing a rich collection of diacritical
characters in the attempt to cover as many Latin-based scripts as possible. To
our knowledge, the repertoire of characters covers all European languages as
well as some other Latin-based alphabets such as Vietnamese and Navajo; at the
request of users, recent extensions (following the enhancement of the Latin
Modern collection) provide glyphs sufficient for typesetting of romanized
transliterations of Arabic and Sanskrit scripts. The Antykwa Poltawskiego
family consists of 4 weights (light, normal, medium, bold), each having upright
and italic forms and one of 5 design sizes: 6, 8, 10, 12 and 17pt. Altogether,
the collection comprises 40 font files, containing the same repertoire of 1126
characters. The preliminary version of Antykwa Poltawskiego (antp package)
released in 2000 is rendered obsolete by this package.

%package -n texlive-prodint
Summary:        A font that provides the product integral symbol
Version:        svn21893
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(prodint.sty) = %{tl_version}

%description -n texlive-prodint
Product integrals are to products, as integrals are to sums. They have been
around for more than a hundred years, they have not become part of the standard
mathematician's toolbox, possibly because no-one invented the right
mathematical symbol for them. The authors have remedied that situation by
proposing the symbol and providing this font.

%package -n texlive-punk
Summary:        Donald Knuth's punk font
Version:        svn27388
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-punk
A response to the assertion in a lecture that "typography tends to lag behind
other stylistic changes by about 10 years". Knuth felt it was (in 1988) time to
design a replacement for his designs of the 1970s, and came up with this font!
The fonts are distributed as Metafont source. The package offers LaTeX support
by Rohit Grover, from an original by Sebastian Rahtz, which is slightly odd in
claiming that the fonts are T1-encoded. A (possibly) more rational support
package is to be found in punk-latex

%package -n texlive-punk-latex
Summary:        LaTeX support for punk fonts
Version:        svn27389
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(punk.sty) = %{tl_version}

%description -n texlive-punk-latex
The package and .fd file provide support for Knuth's punk fonts. That bundle
also offers support within LaTeX; the present package is to be preferred.

%package -n texlive-punknova
Summary:        OpenType version of Knuth's Punk font
Version:        svn24649
License:        LicenseRef-Punknova
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-punknova
The font was generated from a MetaPost version of the sources of the 'original'
punk font. Knuth's original fonts generated different shapes at random. This
isn't actually possible in an OpenType font; rather, the font contains several
variants of each glyph, and uses the OpenType randomize function to select a
variant for each invocation.

%package -n texlive-pxtxalfa
Summary:        Virtual maths alphabets based on pxfonts and txfonts
Version:        svn60847
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(px-ds.sty) = %{tl_version}
Provides:       tex(pxtx-cal.sty) = %{tl_version}
Provides:       tex(pxtx-frak.sty) = %{tl_version}
Provides:       tex(tx-ds.sty) = %{tl_version}
Provides:       tex(tx-of.sty) = %{tl_version}

%description -n texlive-pxtxalfa
The package provides virtual math alphabets based on pxfonts and txfonts, with
LaTeX support files and adjusted metrics. The mathalpha package offers support
for this collection.

%package -n texlive-qualitype
Summary:        The QualiType font collection
Version:        svn54512
License:        OFL-1.1 AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-qualitype
These 45 fonts were created by QualiType. With the kind permisison of John
Colletti, these fonts have been released as free and open-source.

%package -n texlive-quattrocento
Summary:        Quattrocento and Quattrocento Sans fonts with LaTeX support
Version:        svn64372
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(quattrocento.sty) = %{tl_version}

%description -n texlive-quattrocento
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Quattrocento and Quattrocento Sans families of fonts, designed by Pablo
Impallari; the fonts themselves are also provided, in both TrueType and Type1
format. Quattrocento is a classic typeface with wide and open letterforms, and
great x-height, which makes it very legible for body text at small sizes. Tiny
details that only show up at bigger sizes make it also great for display use.
Quattrocento Sans is the perfect sans-serif companion for Quattrocento.

%package -n texlive-raleway
Summary:        Use Raleway with TeX(-alike) systems
Version:        svn74901
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(raleway-type1-autoinst.sty) = %{tl_version}
Provides:       tex(raleway.sty) = %{tl_version}

%description -n texlive-raleway
The package provides the Raleway family in an easy to use way. For XeLaTeX and
LuaLaTeX users the original OpenType fonts are used. The entire font family is
included.

%package -n texlive-recycle
Summary:        A font providing the "recyclable" logo
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(recycle.sty) = %{tl_version}

%description -n texlive-recycle
This single-character font is provided as Metafont source, and in Adobe Type 1
format. It is accompanied by a trivial LaTeX package to use the logo at various
sizes.

%package -n texlive-rit-fonts
Summary:        Malayalam fonts by Rachana Institute of Typography (RIT)
Version:        svn74984
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(rit-fonts.sty) = %{tl_version}

%description -n texlive-rit-fonts
The RIT font collection provides versions of 17 font families in Malayalam (the
language spoken in the southern Indian state of Kerala) script in TrueType and
WOFF2 formats. The fonts are: RIT Ala RIT Chingam RIT Ezhuthu RIT Indira RIT
Karuna RIT Keralayeeam RIT Keram RIT Kutty RIT Lasya RIT Lekha RIT MeeraNew RIT
Panmana RIT Rachana RIT Sundar RIT TN Joy RIT Thaara RIT Uroob A LaTeX package
rit-fonts.sty that will help users to make use of these Unicode-compliant fonts
in LaTeX documents with XeTeX or LuaTeX is also provided.

%package -n texlive-roboto
Summary:        Support for the Roboto family of fonts
Version:        svn64350
License:        Apache-2.0 AND OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(roboto-mono.sty) = %{tl_version}
Provides:       tex(roboto-serif.sty) = %{tl_version}
Provides:       tex(roboto.sty) = %{tl_version}

%description -n texlive-roboto
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Roboto Sans, Roboto Condensed, Roboto Mono, Roboto Slab and Roboto Serif
families of fonts, designed by Christian Robertson and Greg Gazdowicz for
Google.

%package -n texlive-romandeadf
Summary:        Romande ADF fonts and LaTeX support
Version:        svn72484
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(romande.sty) = %{tl_version}

%description -n texlive-romandeadf
Romande ADF is a serif font family with oldstyle figures, designed as a
substitute for Times, Tiffany or Caslon. The family currently includes upright,
italic and small-caps shapes in each of regular and demi-bold weights and an
italic script in regular. The support package renames the fonts according to
the Karl Berry fontname scheme and defines four families. Two of these
primarily provide access to the "standard" or default characters while the
"alternate" families support alternate characters, additional ligatures and the
long s. The included package files provide access to these features in LaTeX as
explained in the documentation. The LaTeX support requires the nfssext-cfr and
the xkeyval packages.

%package -n texlive-rosario
Summary:        Using the free Rosario fonts with LaTeX
Version:        svn51688
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mweights.sty)
Provides:       tex(Rosario.sty) = %{tl_version}

%description -n texlive-rosario
The package provides the files required to use the Rosario fonts with LaTeX.
Rosario is a set of four fonts provided by Hector Gatti, Adobe Typekit &
Omnibus-Type Team under the Open Font License (OFL), version 1.1. The fonts are
copyright (c) 2012-2015, Omnibus-Type.

%package -n texlive-rsfso
Summary:        A mathematical calligraphic font based on rsfs
Version:        svn60849
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(rsfso.sty) = %{tl_version}

%description -n texlive-rsfso
The package provides virtual fonts and LaTeX support files for mathematical
calligraphic fonts based on the rsfs Adobe Type 1 fonts (which must also be
present for successful installation, with the slant substantially reduced. The
output is quite similar to that from the Adobe Mathematical Pi script font.

%package -n texlive-ruscap
Summary:        A Metafont for rustic capitals
Version:        svn71123
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ruscap
This package contains the source for ruscap: a font for rustic capitals -- an
ancient Roman calligraphic script -- created with Metafont.

%package -n texlive-sansmathaccent
Summary:        Correct placement of accents in sans-serif maths
Version:        svn53628
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(scrlfile.sty)
Provides:       tex(sansmathaccent.sty) = %{tl_version}

%description -n texlive-sansmathaccent
Sans serif maths (produced by the beamer class or the sfmath package) often has
accents positioned incorrectly. This package fixes the positioning of such
accents when the default font (cmssi) is used for sans serif maths. It will
have no effect if used in a document that does not use the beamer class or the
sfmath package.

%package -n texlive-sansmathfonts
Summary:        Extended Computer Modern sans serif fonts
Version:        svn72563
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sansmathfonts.sty) = %{tl_version}

%description -n texlive-sansmathfonts
Sans serif small caps and math fonts for use with Computer Modern.

%package -n texlive-sauter
Summary:        Wide range of design sizes for CM fonts
Version:        svn13293
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sauter
Extensions, originally to the CM fonts, providing a parameterization scheme to
build Metafont fonts at true design sizes, for a large range of sizes. The
scheme has now been extended to a range of other fonts, including the AMS
fonts, bbm, bbold, rsfs and wasy fonts.

%package -n texlive-sauterfonts
Summary:        Use Sauter's fonts in LaTeX
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sbbm.sty) = %{tl_version}
Provides:       tex(sexscale.sty) = %{tl_version}

%description -n texlive-sauterfonts
The package provides font definition files (plus a replacement for the package
exscale) to access many of the fonts in Sauter's collection. These fonts are
available in all point sizes and look nicer for such "intermediate" document
sizes as 11pt. Also included is the package sbbm, an alternative to access the
bbm fonts.

%package -n texlive-schola-otf
Summary:        Using the OpenType fonts TeX Gyre schola
Version:        svn64734
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(schola-otf.sty) = %{tl_version}

%description -n texlive-schola-otf
This package can only be used with LuaLaTeX or XeLaTeX. It does the font
setting for the OpenType font TeX Gyre Schola for text and math. The missing
typefaces like bold math and slanted text are also defined

%package -n texlive-scholax
Summary:        Extension of TeXGyreSchola (New Century Schoolbook) with math support
Version:        svn61836
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(newtx-nc-subs.tex) = %{tl_version}
Provides:       tex(newtx-ncf-subs.tex) = %{tl_version}
Provides:       tex(scholax.sty) = %{tl_version}

%description -n texlive-scholax
This package contains an extension of TeXGyreSchola with extensive superiors,
inferior figures, upright punctuation glyphs added to the Italic face for a
theorem font, plus slanted and bold slanted faces. Math support is provided by
one of two options to newtxmath, one of which uses an adaptation of the fourier
math Greek letters.

%package -n texlive-schulschriften
Summary:        German "school scripts" from Suetterlin to the present day
Version:        svn59388
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(eepic.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(latexsym.sty)
Provides:       tex(schulschriften_lin.sty) = %{tl_version}
Provides:       tex(schulschriften_ltx.sty) = %{tl_version}
Provides:       tex(wedn.sty) = %{tl_version}
Provides:       tex(wela.sty) = %{tl_version}
Provides:       tex(wesa.sty) = %{tl_version}
Provides:       tex(wesu.sty) = %{tl_version}
Provides:       tex(weva.sty) = %{tl_version}

%description -n texlive-schulschriften
Das Paket enthalt im wesentlichen die Metafont-Quellfiles fur die folgenden
Schulausgangsschriften: Suetterlinschrift, Deutsche Normalschrift, Lateinische
Ausgangsschrift, Schulausgangsschrift, Vereinfachte Ausgangsschrift. Damit ist
es moglich, beliebige deutsche Texte in diesen Schreibschriften zu schreiben.

%package -n texlive-semaphor
Summary:        Semaphore alphabet font
Version:        svn18651
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(semaf.tex) = %{tl_version}
Provides:       tex(t-type-semaf.tex) = %{tl_version}

%description -n texlive-semaphor
These fonts represent semaphore in a highly schematic, but very clear, fashion.
The fonts are provided as Metafont source, and in both OpenType and Adobe Type
1 formats.

%package -n texlive-shobhika
Summary:        An OpenType Devanagari font designed for scholars
Version:        svn50555
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-shobhika
This package provides a free, open source, Unicode compliant, OpenType font
with support for Devanagari, Latin, and Cyrillic scripts. It is available in
two weights--regular and bold. The font is designed with over 1600 Devanagari
glyphs, including support for over 1100 conjunct consonants, as well as vedic
accents. The Latin component of the font not only supports a wide range of
characters required for Roman transliteration of Sanskrit, but also provides a
subset of regularly used mathematical symbols for scholars working with
scientific and technical documents. The project has been launched under the
auspices of the Science and Heritage Initiative (SandHI) at IIT Bombay, and
builds upon the following two fonts for its Devanagari and Latin components
respectively: (i) Yashomudra by Rajya Marathi Vikas Samstha, and (ii) PT Serif
by ParaType. We would like to thank both these organisations for releasing
their fonts under the SIL Open Font Licence, which has enabled us to create
Shobhika.

%package -n texlive-simpleicons
Summary:        Simple Icons for LaTeX
Version:        svn77382
License:        CC0-1.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Provides:       tex(simpleicons.sty) = %{tl_version}
Provides:       tex(simpleiconsglyphs-pdftex.tex) = %{tl_version}
Provides:       tex(simpleiconsglyphs-xeluatex.tex) = %{tl_version}

%description -n texlive-simpleicons
Similar to FontAwesome icons being provided on LaTeX by the fontawesome
package, this package aims to do the same with Simple Icons. For reference,
visit their website: https://simpleicons.org/.

%package -n texlive-skull
Summary:        A font to draw a skull
Version:        svn51907
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(skull.sty) = %{tl_version}

%description -n texlive-skull
The font (defined in Metafont) defines a single character, a black solid skull.
A package is supplied to make this character available as a symbol in maths
mode.

%package -n texlive-sourcecodepro
Summary:        Use SourceCodePro with TeX(-alike) systems
Version:        svn74885
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(sourcecodepro-type1-autoinst.sty) = %{tl_version}
Provides:       tex(sourcecodepro.sty) = %{tl_version}

%description -n texlive-sourcecodepro
The font is an open-source Monospaced development from Adobe. The package
provides fonts (in both Adobe Type 1 and OpenType formats) and macros
supporting their use in LaTeX (Type 1) and XeLaTeX/LuaLaTeX (OTF).

%package -n texlive-sourcesanspro
Summary:        Use SourceSansPro with TeX(-alike) systems
Version:        svn54892
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(sourcesanspro-type1-autoinst.sty) = %{tl_version}
Provides:       tex(sourcesanspro.sty) = %{tl_version}

%description -n texlive-sourcesanspro
The font is an open-source Sans-Serif development from Adobe. The package
provides fonts (in both Adobe Type 1 and OpenType formats) and macros
supporting their use in LaTeX (Type 1) and XeLaTeX/LuaLaTeX (OTF).

%package -n texlive-sourceserifpro
Summary:        Use SourceSerifPro with TeX(-alike) systems
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(sourceserifpro-type1-autoinst.sty) = %{tl_version}
Provides:       tex(sourceserifpro.sty) = %{tl_version}

%description -n texlive-sourceserifpro
This package provides Source Serif Pro for LaTeX. It includes both Type1 and
OpenType fonts and selects the latter when using XeLaTeX or LuaLaTeX.

%package -n texlive-spectral
Summary:        Spectral fonts with LaTeX support
Version:        svn64528
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(spectral.sty) = %{tl_version}

%description -n texlive-spectral
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
Spectral family of fonts, designed by Jean-Baptiste Levee at the Production
Type digital type design agency. Spectral is a new and versatile serif face
available in seven weights of roman and italic, with small caps.

%package -n texlive-splentinex
Summary:        Splentinex fonts
Version:        svn76841
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(splentinex.sty) = %{tl_version}

%description -n texlive-splentinex
This is a serif font family designed for body text. This typeface design was
originally crated by Frank Pierpont and Fritz Stelzer in 1913 and released by
Monotype as Plantin. In 2025, Ben Byram-Wigfield created Splentino, a new
digitization of the Plantin design, for inclusion with the music software
Dorico. Splentinex is a modified repackaging of Splentino.

%package -n texlive-srbtiks
Summary:        Font STIX2 for Serbian and Macedonian
Version:        svn63308
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(srbtiks.sty) = %{tl_version}

%description -n texlive-srbtiks
The srbtiks package is the extension of the stix2-type1 package that enables
usage of the STIX2 font in LaTeX for the Serbian and Macedonian languages
(therefore, it is required to have the stix2-type1 package installed).

%package -n texlive-starfont
Summary:        The StarFont Sans astrological font
Version:        svn19982
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(starfont.sty) = %{tl_version}

%description -n texlive-starfont
The package contains StarFontSans and StarFontSerif, two public-domain
astrological fonts designed by Anthony I.P. Owen, and the appropriate macros to
use them with TeX and LaTeX. The fonts are supplied both in the original
TrueType Format and in Adobe Type 1 format.

%package -n texlive-staves
Summary:        Typeset Icelandic staves and runic letters
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(staves.sty) = %{tl_version}

%description -n texlive-staves
This package contains all the necessary tools to typeset the "magical"
Icelandic staves plus the runic letters used in Iceland. Included are a font in
Adobe Type 1 format and LaTeX support.

%package -n texlive-step
Summary:        A free Times-like font
Version:        svn57307
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(step.sty) = %{tl_version}

%description -n texlive-step
The STEP fonts are a free Times-like (i.e., Times replacement) font family,
implementing a design first created for The Times of London in 1932. These
fonts are meant to be compatible in design with Adobe's digitization of
Linotype Times, commonly used in publishing. The fonts were forked from
XITS/STIX and Type 1 support is provided for legacy TeX engines.

%package -n texlive-stepgreek
Summary:        A free Times/Elsevier-style Greek font
Version:        svn57074
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-stepgreek
This is a beta version of the STEP Greek font. Only a regular face is available
at present, though there are plans to add italic, bold and bold italic in the
future. The font only supports LGR in TeX and is meant to serve as a Greek
complement to a Times-like font such as STEP. The font supports polytonic
Greek.

%package -n texlive-stickstoo
Summary:        A reworking of STIX2
Version:        svn72368
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(stickstootext.sty) = %{tl_version}

%description -n texlive-stickstoo
SticksToo is a reworking of the STIX2 fonts with support files focussing on
enhancements of support for LaTeX users wishing to be able to access more of
its features. A companion addition to the newtxmath package (version 1.55)
provides a matching math package using STIX2 letters (Roman and Greek) with
newtxmath symbols.

%package -n texlive-stix
Summary:        OpenType Unicode maths fonts
Version:        svn54512
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(textcomp.sty)
Provides:       tex(stix.sty) = %{tl_version}

%description -n texlive-stix
The STIX fonts are a suite of unicode OpenType fonts containing a complete set
of mathematical glyphs. As of April 2018 this package is considered obsolete.
See stix2-otf and stix2-type1 instead.

%package -n texlive-stix2-otf
Summary:        OpenType Unicode text and maths fonts
Version:        svn58735
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-stix2-otf
The Scientific and Technical Information eXchange (STIX) fonts are intended to
satisfy the demanding needs of authors, publishers, printers, and others
working in the scientific, medical, and technical fields. They combine a
comprehensive Unicode-based collection of mathematical symbols and alphabets
with a set of text faces suitable for professional publishing. The fonts are
available royalty-free under the SIL Open Font License.

%package -n texlive-stix2-type1
Summary:        Type1 versions of the STIX Two OpenType fonts
Version:        svn57448
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(textcomp.sty)
Provides:       tex(stix2.sty) = %{tl_version}

%description -n texlive-stix2-type1
The stix2 package provides minimal support for using the STIX Two fonts with
versions of TeX that are limited to TFM files, Type 1 PostScript fonts, and
8-bit font encodings. Version 2.0.0 of the STIX fonts are being released in
this format in hopes of easing the transition from legacy TeX engines to modern
fully Unicode-compatible systems. The Type 1 versions are merely a repackaging
of the original OpenType versions and should not be viewed as independent
entities. Some glyphs that are traditionally available in TeX math fonts are
not yet available in the STIX Two OpenType fonts. In such cases, we have chosen
to omit them from the stix2 package rather than create incompatibilities
between the OpenType and Type 1 versions. In addition, while development of the
OpenType versions is ongoing, no further updates are planned to the Type 1
versions of the fonts.

%package -n texlive-superiors
Summary:        Attach superior figures to a font family
Version:        svn69387
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(trace.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(superiors.sty) = %{tl_version}

%description -n texlive-superiors
The package allows the attachment of an arbitrary superior figures font to a
font family that lacks one. (Superior figures are commonly used as footnote
markers.)

%package -n texlive-svrsymbols
Summary:        A font with symbols for use in physics texts
Version:        svn50019
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(svrsymbols.sty) = %{tl_version}

%description -n texlive-svrsymbols
The svrsymbols package is a LaTeX interface to the SVRsymbols font. The glyphs
of this font are ideograms that have been designed for use in physics texts.
Some symbols are standard and some are entirely new.

%package -n texlive-symbats3
Summary:        Macros to use the Symbats3 dingbats fonts
Version:        svn63833
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fontspec.sty)
Provides:       tex(symbats3.sty) = %{tl_version}

%description -n texlive-symbats3
This package makes available for LaTeX the glyphs in Feorag's OpenType Symbats3
neopagan dingbats fonts.

%package -n texlive-tapir
Summary:        A simple geometrical font
Version:        svn20484
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tapir
Tapir is a simple geometrical font mostly created of line and circular segments
with constant thickness. The font is available as Metafont source and in Adobe
Type 1 format. The character set contains all characters in the range 0-127 (as
in cmr10), accented characters used in the Czech, Slovak and Polish languages.

%package -n texlive-tempora
Summary:        Greek and Cyrillic to accompany Times
Version:        svn39596
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tempora.sty) = %{tl_version}

%description -n texlive-tempora
This package, derived from TemporaLGCUni by Alexej Kryukov, is meant as a
companion to Times text font packages, providing Greek and Cyrillic in matching
weights and styles. OpenType and Type1 fonts are provided, with LaTeX support
files giving essentially complete LGR coverage of monotonic, polytonic and
ancient Greek, and almost full T2A coverage of Cyrillic.

%package -n texlive-tengwarscript
Summary:        LaTeX support for using Tengwar fonts
Version:        svn34594
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp-basic.sty)
Requires:       tex(fp-snap.sty)
Provides:       tex(tengwarscript.sty) = %{tl_version}

%description -n texlive-tengwarscript
The package provides "mid-level" access to tengwar fonts, providing good
quality output. Each tengwar sign is represented by a command, which will place
the sign nicely in relation to previous signs. A transcription package is
available from the package's home page: writing all those tengwar commands
would quickly become untenable. The package supports the use of a wide variety
of tengwar fonts that are available from the net; metric and map files are
provided for all the supported fonts.

%package -n texlive-termes-otf
Summary:        Using the OpenType fonts TeX Gyre Termes
Version:        svn64733
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(termes-otf.sty) = %{tl_version}

%description -n texlive-termes-otf
This package provides the OpenType version of the TeX Gyre Termes font,
including text and math fonts. The package needs LuaLaTeX or XeLaTeX. The
missing typefaces like bold math and slanted text are also defined.

%package -n texlive-tfrupee
Summary:        A font offering the new (Indian) Rupee symbol
Version:        svn20770
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tfrupee.sty) = %{tl_version}

%description -n texlive-tfrupee
The package provides LaTeX support for the (Indian) Rupee symbol font, created
by TechFat. The original font has been converted to Adobe Type 1 format, and
simple LaTeX support written for its use.

%package -n texlive-theanodidot
Summary:        TheanoDidot fonts with LaTeX support
Version:        svn64518
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(TheanoDidot.sty) = %{tl_version}

%description -n texlive-theanodidot
This package provides the TheanoDidot font designed by Alexey Kryukov, in both
TrueType and Type1 formats, with support for both traditional and modern LaTeX
processors. An artificially-emboldened variant has been provided but there are
no italic variants. The package is named after Theano, a famous Ancient Greek
woman philosopher, who was first a student of Pythagoras, and supposedly became
his wife. The Didot family were active as designers for about 100 years in the
18th and 19th centuries. They were printers, publishers, typeface designers,
inventors and intellectuals. Around 1800 the Didot family owned the most
important print shop and font foundry in France. Pierre Didot, the printer,
published a document with the typefaces of his brother, Firmin Didot, the
typeface designer. The strong clear forms of this alphabet display objective,
rational characteristics and are representative of the time and philosophy of
the Enlightenment.

%package -n texlive-theanomodern
Summary:        Theano Modern fonts with LaTeX support
Version:        svn64520
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(TheanoModern.sty) = %{tl_version}

%description -n texlive-theanomodern
This package provides the TheanoModern font designed by Alexey Kryukov, in both
TrueType and Type1 formats, with support for both traditional and modern LaTeX
processors. An artificially-emboldened variant has been provided but there are
no italic variants. The package is named after Theano, a famous Ancient Greek
woman philosopher, who was first a student of Pythagoras, and supposedly became
his wife.

%package -n texlive-theanooldstyle
Summary:        Theano OldStyle fonts with LaTeX support
Version:        svn64519
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(TheanoOldStyle.sty) = %{tl_version}

%description -n texlive-theanooldstyle
This package provides the Theano OldStyle font designed by Alexey Kryukov, in
both TrueType and Type1 formats, with support for both traditional and modern
LaTeX processors. An artificially-emboldened variant has been provided but
there are no italic variants. The package is named after Theano, a famous
Ancient Greek woman philosopher, who was first a student of Pythagoras, and
supposedly became his wife.

%package -n texlive-tinos
Summary:        Tinos fonts with LaTeX support
Version:        svn68950
License:        Apache-2.0 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(tinos.sty) = %{tl_version}

%description -n texlive-tinos
Tinos, designed by Steve Matteson, is an innovative, refreshing serif design
that is metrically compatible with Times New Roman.

%package -n texlive-tpslifonts
Summary:        A LaTeX package for configuring presentation fonts
Version:        svn42428
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cmbright.sty)
Requires:       tex(eulervm.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(tpslifonts.sty) = %{tl_version}

%description -n texlive-tpslifonts
This package aims to improve of font readability in presentations, especially
with maths. The standard cm maths fonts at large design sizes are difficult to
read from far away, especially at low resolutions and low contrast color
choice. Using this package leads to much better overall readability of some
font combinations. The package offers a couple of 'harmonising' combinations of
text and maths fonts from the (distant) relatives of computer modern fonts,
with a couple of extras for optimising readability. Text fonts from computer
modern roman, computer modern sans serif, SliTeX computer modern sans serif,
computer modern bright, or concrete roman are available, in addition to maths
fonts from computer modern maths, computer modern bright maths, or Euler fonts.
The package is part of the TeXPower bundle.

%package -n texlive-trajan
Summary:        Fonts from the Trajan column in Rome
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(trajan.sty) = %{tl_version}

%description -n texlive-trajan
Provides fonts (both as Metafont source and in Adobe Type 1 format) based on
the capitals carved on the Trajan column in Rome in 114 AD, together with
macros to access the fonts. Many typographers think these rank first among the
Roman's artistic legacy. The font is uppercase letters together with some
punctuation and analphabetics; no lowercase or digits.

%package -n texlive-twemoji-colr
Summary:        Twemoji font in COLR/CPAL layered format
Version:        svn75301
License:        CC-BY-SA-4.0 AND Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-twemoji-colr
This is a COLR/CPAL-based color OpenType font from the Twemoji collection of
emoji images.

%package -n texlive-txfontsb
Summary:        Extensions to txfonts, using GNU Freefont
Version:        svn54512
License:        GPL-2.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(txfonts.sty)
Provides:       tex(txfontsb.sty) = %{tl_version}

%description -n texlive-txfontsb
A set of fonts that extend the txfonts bundle with small caps and old style
numbers, together with Greek support. The extensions are made with
modifications of the GNU Freefont.

%package -n texlive-txuprcal
Summary:        Upright calligraphic font based on TX calligraphic
Version:        svn76924
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(txuprcal.sty) = %{tl_version}

%description -n texlive-txuprcal
This small package provides a means of loading as \mathcal upright versions of
the calligraphic fonts from the TX font package. A scaled option to provided to
allow arbitrary scaling.

%package -n texlive-typicons
Summary:        Font containing a set of web-related icons
Version:        svn37623
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(typicons.sty) = %{tl_version}

%description -n texlive-typicons
This package grants access to 336 web-related icons provided by the included
"Typicons" free font, designed by Stephen Hutchings and released under the SIL
Open Font License. See http://www.typicons.com for more details about the font
itself. This package requires the fontspec package and either the Xe(La)TeX or
Lua(La)TeX engine to load the included ttf font. Once the package is loaded,
icons can be accessed through the general \ticon command, which takes as
argument the name of the desired icon, or through direct commands specific to
each icon. The full list of icon designs, names and direct commands is
showcased in the manual.

%package -n texlive-umtypewriter
Summary:        Fonts to typeset with the xgreek package
Version:        svn64443
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-umtypewriter
The UMTypewriter font family is a monospaced font family that was built from
glyphs from the CB Greek fonts, the CyrTUG Cyrillic alphabet fonts ("LH"), and
the standard Computer Modern font family. It contains four OpenType fonts which
are required for use of the xgreek package for XeLaTeX.

%package -n texlive-universa
Summary:        Herbert Bayer's 'universal' font
Version:        svn51984
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(uni.sty) = %{tl_version}

%description -n texlive-universa
An implementation of the "universal" font by Herbert Bayer of the Bauhaus
school. The Metafont sources of the fonts, and their LaTeX support, are all
supplied in a LaTeX documented source (.dtx) file.

%package -n texlive-universalis
Summary:        Universalis font, with support
Version:        svn64505
License:        GPL-2.0-or-later AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(UniversalisADFStd.sty) = %{tl_version}
Provides:       tex(universalis.sty) = %{tl_version}

%description -n texlive-universalis
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the
UniversalisADFStd family of fonts, designed by Hirwin Harendal. The font is
suitable as an alternative to fonts such as Adrian Frutiger's Univers and
Frutiger.

%package -n texlive-uppunctlm
Summary:        Always keep upright shape for some punctuation marks and Arabic numerals
Version:        svn42334
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(uppunctlm.sty) = %{tl_version}

%description -n texlive-uppunctlm
The package provides a mechanism to keep punctuation always in upright shape
even if italic was specified. It is directed to Latin Modern fonts, and
provides .tfm, .vf, .fd, and .sty files. Here a list of punctuation characters
always presented in upright shapes: comma, period, semicolon, colon,
parentheses, square brackets, and Arabic numerals.

%package -n texlive-urwchancal
Summary:        Use URW's clone of Zapf Chancery as a maths alphabet
Version:        svn21701
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(urwchancal.sty) = %{tl_version}

%description -n texlive-urwchancal
The package allows (the URW clone of) Zapf Chancery to function as a maths
alphabet, the target of \mathcal or \mathscr, with accents appearing where they
should, and other spacing parameters set to reasonable (not very tight) values.
The font itself may be found in the URW basic fonts collection. This package
supersedes the pzccal package.

%package -n texlive-venturisadf
Summary:        Venturis ADF fonts collection
Version:        svn72484
License:        LicenseRef-Utopia
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(venturis.sty) = %{tl_version}
Provides:       tex(venturis2.sty) = %{tl_version}
Provides:       tex(venturisold.sty) = %{tl_version}

%description -n texlive-venturisadf
Serif and sans serif complete text font families, in both Adobe Type 1 and
OpenType formats for publication. The family is based on Utopia family, and has
been modified and developed by the Arkandis Digital foundry. Support for using
the fonts, in LaTeX, is also provided (and makes use of the nfssext-cfr
package).

%package -n texlive-wsuipa
Summary:        International Phonetic Alphabet fonts
Version:        svn25469
License:        LicenseRef-Utopia
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ipa.sty) = %{tl_version}
Provides:       tex(ipalmacs.sty) = %{tl_version}

%description -n texlive-wsuipa
The package provides a 7-bit IPA font, as Metafont source, and macros for
support under TeXt1 and LaTeX. The fonts (and macros) are now largely
superseded by the tipa fonts.

%package -n texlive-xcharter
Summary:        Extension of Bitstream Charter fonts
Version:        svn71564
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(realscripts.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcharter-otf.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(XCharter.sty) = %{tl_version}
Provides:       tex(newtx-xcharter-subs.tex) = %{tl_version}
Provides:       tex(t2asrbenc.def) = %{tl_version}

%description -n texlive-xcharter
The package presents an extension of Bitstream Charter, which provides small
caps, oldstyle figures and superior figures in all four styles, accompanied by
LaTeX font support files. The fonts themselves are provided in both Adobe Type
1 and OTF formats, with supporting files as necessary.

%package -n texlive-xcharter-math
Summary:        XCharter-based OpenType Math font for LuaTeX and XeTeX
Version:        svn76745
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(realscripts.sty)
Requires:       tex(unicode-math.sty)
Provides:       tex(xcharter-otf.sty) = %{tl_version}

%description -n texlive-xcharter-math
This package provides an Unicode Math font XCharter-Math.otf meant to be used
together with XCharter Opentype Text fonts (extension of Bitstream Charter) in
LuaLaTeX or XeLaTeX documents.

%package -n texlive-xits
Summary:        A Scientific Times-like font with support for mathematical typesetting
Version:        svn55730
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xits
XITS is a Times-like font for scientific typesetting with proper mathematical
support for modern, Unicode and OpenType capable TeX engines, namely LuaTeX and
XeTeX. For use with LuaLaTeX or XeLaTeX, support is available from the fontspec
and unicode-math packages.

%package -n texlive-yfonts
Summary:        Support for old German fonts
Version:        svn50755
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(yfonts.sty) = %{tl_version}

%description -n texlive-yfonts
A LaTeX interface to the old-german fonts designed by Yannis Haralambous:
Gothic, Schwabacher, Fraktur and the baroque initials.

%package -n texlive-yfonts-otf
Summary:        OpenType version of the Old German fonts designed by Yannis Haralambous
Version:        svn76885
License:        OFL-1.1 AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Provides:       tex(oldgerm-otf.sty) = %{tl_version}
Provides:       tex(yfonts-otf.sty) = %{tl_version}

%description -n texlive-yfonts-otf
This is an OpenType version of the Old German fonts yfrak, ygoth, yswab
designed by Yannis Haralambous in Metafont. The OpenType features make it
easier to deal with the long/round s and with older forms of umlauts (small e
over the letter). A style file yfonts-otf.sty is provided as a replacement, for
LuaLaTeX and XeLaTeX, of yfonts.sty or oldgerm.sty.

%package -n texlive-yfonts-t1
Summary:        Old German-style fonts, in Adobe type 1 format
Version:        svn36013
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-yfonts-t1
This package comprises type 1 versions of the Gothic, Schwabacher and Fraktur
fonts of Yannis Haralambous' set of old German fonts.

%package -n texlive-yinit-otf
Summary:        OTF conversion of Yannis Haralambous' Old German decorative initials
Version:        svn40207
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-yinit-otf
This package is a conversion of the yinit font into OTF. Original Metafont
files for yinit are in the yinit package.

%package -n texlive-ysabeau
Summary:        Ysabeau fonts with LaTeX support for traditional TeX engines
Version:        svn77373
License:        OFL-1.1 AND WTFPL AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ysabeau.sty) = %{tl_version}

%description -n texlive-ysabeau
Ysabeau is a free type family. It combines the time-honored and supremely
readable letterforms of the Garamond legacy with the clean crispness of a
low-contrast sans serif, rendering it well suited for body copy as well as
display. This package provides LaTeX font support for traditional TeX engines
(pdfTeX, dvips, and so on). For XeTeX or LuaTeX users, OpenType and TrueType
fonts are provided only to use with the fontspec package.

%package -n texlive-zlmtt
Summary:        Use Latin Modern Typewriter fonts
Version:        svn64076
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(mweights.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(zlmtt.sty) = %{tl_version}

%description -n texlive-zlmtt
The package allows selection of Latin Modern Typewriter fonts with scaling and
access to all its features.


%prep
# Extract license files
tar -xf %{SOURCE1}

# Copy special license file for yfonts-t1
cp %{SOURCE826} .

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

mkdir -p %{buildroot}%{_datadir}/fonts
mkdir -p %{buildroot}%{_datadir}/appdata

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
tar -xf %{SOURCE631} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE632} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE633} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE634} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE635} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE636} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE637} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE638} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE639} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE640} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE641} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE642} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE643} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE644} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE645} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE646} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE647} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE648} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE649} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE650} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE651} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE652} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE653} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE654} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE655} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE656} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE657} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE658} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE659} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE660} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE661} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE662} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE663} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE664} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE665} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE666} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE667} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE668} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE669} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE670} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE671} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE672} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE673} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE674} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE675} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE676} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE677} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE678} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE679} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE680} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE681} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE682} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE683} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE684} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE685} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE686} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE687} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE688} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE689} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE690} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE691} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE692} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE693} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE694} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE695} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE696} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE697} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE698} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE699} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE700} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE701} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE702} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE703} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE704} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE705} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE706} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE707} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE708} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE709} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE710} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE711} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE712} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE713} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE714} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE715} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE716} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE717} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE718} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE719} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE720} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE721} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE722} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE723} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE724} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE725} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE726} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE727} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE728} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE729} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE730} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE731} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE732} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE733} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE734} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE735} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE736} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE737} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE738} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE739} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE740} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE741} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE742} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE743} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE744} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE745} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE746} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE747} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE748} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE749} -C %{buildroot}%{_texmf_main}

# Install AppStream metadata for font components
cp %{SOURCE750} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE751} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE752} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE753} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE754} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE755} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE756} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE757} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE758} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE759} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE760} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE761} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE762} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE763} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE764} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE765} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE766} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE767} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE768} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE769} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE770} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE771} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE772} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE773} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE774} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE775} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE776} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE777} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE778} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE779} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE780} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE781} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE782} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE783} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE784} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE785} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE786} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE787} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE788} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE789} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE790} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE791} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE792} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE793} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE794} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE795} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE796} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE797} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE798} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE799} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE800} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE801} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE802} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE803} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE804} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE805} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE806} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE807} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE808} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE809} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE810} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE811} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE812} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE813} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE814} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE815} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE816} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE817} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE818} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE819} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE820} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE821} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE822} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE823} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE824} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE825} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/algolrevived %{buildroot}%{_datadir}/fonts/algolrevived
ln -sf %{_texmf_main}/fonts/opentype/public/almfixed %{buildroot}%{_datadir}/fonts/almfixed
ln -sf %{_texmf_main}/fonts/opentype/public/antt %{buildroot}%{_datadir}/fonts/antt
ln -sf %{_texmf_main}/fonts/opentype/omnibus-type/asapsym %{buildroot}%{_datadir}/fonts/asapsym
ln -sf %{_texmf_main}/fonts/opentype/public/baskervaldx %{buildroot}%{_datadir}/fonts/baskervaldx
ln -sf %{_texmf_main}/fonts/opentype/public/baskervillef %{buildroot}%{_datadir}/fonts/baskervillef
ln -sf %{_texmf_main}/fonts/opentype/arkandis/berenisadf %{buildroot}%{_datadir}/fonts/berenisadf
ln -sf %{_texmf_main}/fonts/opentype/public/beuron %{buildroot}%{_datadir}/fonts/beuron
ln -sf %{_texmf_main}/fonts/opentype/impallari/cabin %{buildroot}%{_datadir}/fonts/cabin
ln -sf %{_texmf_main}/fonts/opentype/public/ccicons %{buildroot}%{_datadir}/fonts/ccicons
ln -sf %{_texmf_main}/fonts/opentype/public/chivo %{buildroot}%{_datadir}/fonts/chivo
ln -sf %{_texmf_main}/fonts/opentype/public/clara %{buildroot}%{_datadir}/fonts/clara
ln -sf %{_texmf_main}/fonts/opentype/public/cm-unicode %{buildroot}%{_datadir}/fonts/cm-unicode
ln -sf %{_texmf_main}/fonts/opentype/public/cochineal %{buildroot}%{_datadir}/fonts/cochineal
ln -sf %{_texmf_main}/fonts/opentype/public/coelacanth %{buildroot}%{_datadir}/fonts/coelacanth
ln -sf %{_texmf_main}/fonts/opentype/rozynski/comicneue %{buildroot}%{_datadir}/fonts/comicneue
ln -sf %{_texmf_main}/fonts/opentype/public/countriesofeurope %{buildroot}%{_datadir}/fonts/countriesofeurope
ln -sf %{_texmf_main}/fonts/opentype/kosch/crimson %{buildroot}%{_datadir}/fonts/crimson
ln -sf %{_texmf_main}/fonts/opentype/public/cyklop %{buildroot}%{_datadir}/fonts/cyklop
ln -sf %{_texmf_main}/fonts/opentype/public/dantelogo %{buildroot}%{_datadir}/fonts/dantelogo
ln -sf %{_texmf_main}/fonts/opentype/public/domitian %{buildroot}%{_datadir}/fonts/domitian
ln -sf %{_texmf_main}/fonts/opentype/public/drm %{buildroot}%{_datadir}/fonts/drm
ln -sf %{_texmf_main}/fonts/opentype/public/erewhon %{buildroot}%{_datadir}/fonts/erewhon
ln -sf %{_texmf_main}/fonts/opentype/public/erewhon-math %{buildroot}%{_datadir}/fonts/erewhon-math
ln -sf %{_texmf_main}/fonts/opentype/public/etbb %{buildroot}%{_datadir}/fonts/etbb
ln -sf %{_texmf_main}/fonts/opentype/public/fbb %{buildroot}%{_datadir}/fonts/fbb
ln -sf %{_texmf_main}/fonts/opentype/public/fdsymbol %{buildroot}%{_datadir}/fonts/fdsymbol
ln -sf %{_texmf_main}/fonts/opentype/public/fetamont %{buildroot}%{_datadir}/fonts/fetamont
ln -sf %{_texmf_main}/fonts/opentype/public/firamath %{buildroot}%{_datadir}/fonts/firamath
ln -sf %{_texmf_main}/fonts/opentype/public/fonts-churchslavonic %{buildroot}%{_datadir}/fonts/fonts-churchslavonic
ln -sf %{_texmf_main}/fonts/opentype/public/forum %{buildroot}%{_datadir}/fonts/forum
ln -sf %{_texmf_main}/fonts/opentype/public/fourier %{buildroot}%{_datadir}/fonts/fourier
ln -sf %{_texmf_main}/fonts/opentype/public/frederika2016 %{buildroot}%{_datadir}/fonts/frederika2016
ln -sf %{_texmf_main}/fonts/opentype/public/garamond-libre %{buildroot}%{_datadir}/fonts/garamond-libre
ln -sf %{_texmf_main}/fonts/opentype/public/garamond-math %{buildroot}%{_datadir}/fonts/garamond-math
ln -sf %{_texmf_main}/fonts/opentype/public/gnu-freefont %{buildroot}%{_datadir}/fonts/gnu-freefont
ln -sf %{_texmf_main}/fonts/opentype/iginomarini/imfellenglish %{buildroot}%{_datadir}/fonts/imfellenglish
ln -sf %{_texmf_main}/fonts/opentype/public/inriafonts %{buildroot}%{_datadir}/fonts/inriafonts
ln -sf %{_texmf_main}/fonts/opentype/nowacki/iwona %{buildroot}%{_datadir}/fonts/iwona
ln -sf %{_texmf_main}/fonts/opentype/nowacki/kurier %{buildroot}%{_datadir}/fonts/kurier
ln -sf %{_texmf_main}/fonts/opentype/public/libertinus-fonts %{buildroot}%{_datadir}/fonts/libertinus-fonts
ln -sf %{_texmf_main}/fonts/opentype/impallari/librebodoni %{buildroot}%{_datadir}/fonts/librebodoni
ln -sf %{_texmf_main}/fonts/opentype/impallari/librecaslon %{buildroot}%{_datadir}/fonts/librecaslon
ln -sf %{_texmf_main}/fonts/opentype/impallari/librefranklin %{buildroot}%{_datadir}/fonts/librefranklin
ln -sf %{_texmf_main}/fonts/opentype/public/linguisticspro %{buildroot}%{_datadir}/fonts/linguisticspro
ln -sf %{_texmf_main}/fonts/opentype/impallari/lobster2 %{buildroot}%{_datadir}/fonts/lobster2
ln -sf %{_texmf_main}/fonts/opentype/public/logix %{buildroot}%{_datadir}/fonts/logix
ln -sf %{_texmf_main}/fonts/opentype/public/mdsymbol %{buildroot}%{_datadir}/fonts/mdsymbol
ln -sf %{_texmf_main}/fonts/opentype/public/miama %{buildroot}%{_datadir}/fonts/miama
ln -sf %{_texmf_main}/fonts/opentype/arkandis/mintspirit %{buildroot}%{_datadir}/fonts/mintspirit
ln -sf %{_texmf_main}/fonts/opentype/public/missaali %{buildroot}%{_datadir}/fonts/missaali
ln -sf %{_texmf_main}/fonts/opentype/public/mnsymbol %{buildroot}%{_datadir}/fonts/mnsymbol
ln -sf %{_texmf_main}/fonts/opentype/public/newcomputermodern %{buildroot}%{_datadir}/fonts/newcomputermodern
ln -sf %{_texmf_main}/fonts/opentype/public/newpx %{buildroot}%{_datadir}/fonts/newpx
ln -sf %{_texmf_main}/fonts/opentype/public/newtx %{buildroot}%{_datadir}/fonts/newtx
ln -sf %{_texmf_main}/fonts/opentype/public/nimbus15 %{buildroot}%{_datadir}/fonts/nimbus15
ln -sf %{_texmf_main}/fonts/opentype/public/ocr-b-outline %{buildroot}%{_datadir}/fonts/ocr-b-outline
ln -sf %{_texmf_main}/fonts/opentype/tipo/overlock %{buildroot}%{_datadir}/fonts/overlock
ln -sf %{_texmf_main}/fonts/opentype/public/phaistos %{buildroot}%{_datadir}/fonts/phaistos
ln -sf %{_texmf_main}/fonts/opentype/public/playfair %{buildroot}%{_datadir}/fonts/playfair
ln -sf %{_texmf_main}/fonts/opentype/gust/poltawski %{buildroot}%{_datadir}/fonts/poltawski
ln -sf %{_texmf_main}/fonts/opentype/public/punknova %{buildroot}%{_datadir}/fonts/punknova
ln -sf %{_texmf_main}/fonts/opentype/public/qualitype %{buildroot}%{_datadir}/fonts/qualitype
ln -sf %{_texmf_main}/fonts/opentype/public/rosario %{buildroot}%{_datadir}/fonts/rosario
ln -sf %{_texmf_main}/fonts/opentype/public/scholax %{buildroot}%{_datadir}/fonts/scholax
ln -sf %{_texmf_main}/fonts/opentype/public/semaphor %{buildroot}%{_datadir}/fonts/semaphor
ln -sf %{_texmf_main}/fonts/opentype/public/step %{buildroot}%{_datadir}/fonts/step
ln -sf %{_texmf_main}/fonts/opentype/public/svrsymbols %{buildroot}%{_datadir}/fonts/svrsymbols
ln -sf %{_texmf_main}/fonts/opentype/public/tempora %{buildroot}%{_datadir}/fonts/tempora
ln -sf %{_texmf_main}/fonts/opentype/public/txfontsb %{buildroot}%{_datadir}/fonts/txfontsb
ln -sf %{_texmf_main}/fonts/opentype/public/umtypewriter %{buildroot}%{_datadir}/fonts/umtypewriter
ln -sf %{_texmf_main}/fonts/opentype/arkandis/universalis %{buildroot}%{_datadir}/fonts/universalis
ln -sf %{_texmf_main}/fonts/opentype/public/xcharter %{buildroot}%{_datadir}/fonts/xcharter
ln -sf %{_texmf_main}/fonts/opentype/public/xits %{buildroot}%{_datadir}/fonts/xits
ln -sf %{_texmf_main}/fonts/opentype/public/yinit-otf %{buildroot}%{_datadir}/fonts/yinit-otf

# Apply droid patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-droid-fixmono.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Rename .map files to .oldmap to avoid updmap-sys
mv %{buildroot}%{_texmf_main}/fonts/map/dvips/mpfonts/mpfonts.map %{buildroot}%{_texmf_main}/fonts/map/dvips/mpfonts/mpfonts.oldmap

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-aboensis
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/aboensis/
%{_texmf_main}/tex/latex/aboensis/
%doc %{_texmf_main}/doc/fonts/aboensis/

%files -n texlive-academicons
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/academicons/
%{_texmf_main}/fonts/map/dvips/academicons/
%{_texmf_main}/fonts/opentype/public/academicons/
%{_texmf_main}/fonts/tfm/public/academicons/
%{_texmf_main}/fonts/truetype/public/academicons/
%{_texmf_main}/fonts/type1/public/academicons/
%{_texmf_main}/tex/generic/academicons/
%doc %{_texmf_main}/doc/fonts/academicons/

%files -n texlive-accanthis
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/accanthis/
%{_texmf_main}/fonts/map/dvips/accanthis/
%{_texmf_main}/fonts/opentype/arkandis/accanthis/
%{_texmf_main}/fonts/tfm/arkandis/accanthis/
%{_texmf_main}/fonts/type1/arkandis/accanthis/
%{_texmf_main}/fonts/vf/arkandis/accanthis/
%{_texmf_main}/tex/latex/accanthis/
%doc %{_texmf_main}/doc/fonts/accanthis/

%files -n texlive-adforn
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/arkandis/adforn/
%{_texmf_main}/fonts/enc/dvips/adforn/
%{_texmf_main}/fonts/map/dvips/adforn/
%{_texmf_main}/fonts/tfm/arkandis/adforn/
%{_texmf_main}/fonts/type1/arkandis/adforn/
%{_texmf_main}/tex/latex/adforn/
%doc %{_texmf_main}/doc/fonts/adforn/

%files -n texlive-adfsymbols
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/arkandis/adfsymbols/
%{_texmf_main}/fonts/enc/dvips/adfsymbols/
%{_texmf_main}/fonts/map/dvips/adfsymbols/
%{_texmf_main}/fonts/tfm/arkandis/adfsymbols/
%{_texmf_main}/fonts/type1/arkandis/adfsymbols/
%{_texmf_main}/tex/latex/adfsymbols/
%doc %{_texmf_main}/doc/fonts/adfsymbols/

%files -n texlive-aesupp
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/aesupp/
%{_texmf_main}/fonts/map/dvips/aesupp/
%{_texmf_main}/fonts/opentype/public/aesupp/
%{_texmf_main}/fonts/tfm/public/aesupp/
%{_texmf_main}/fonts/type1/public/aesupp/
%{_texmf_main}/tex/latex/aesupp/
%doc %{_texmf_main}/doc/fonts/aesupp/

%files -n texlive-alegreya
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/alegreya/
%{_texmf_main}/fonts/map/dvips/alegreya/
%{_texmf_main}/fonts/opentype/huerta/alegreya/
%{_texmf_main}/fonts/tfm/huerta/alegreya/
%{_texmf_main}/fonts/type1/huerta/alegreya/
%{_texmf_main}/fonts/vf/huerta/alegreya/
%{_texmf_main}/tex/latex/alegreya/
%doc %{_texmf_main}/doc/fonts/alegreya/

%files -n texlive-alfaslabone
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/alfaslabone/
%{_texmf_main}/fonts/map/dvips/alfaslabone/
%{_texmf_main}/fonts/opentype/public/alfaslabone/
%{_texmf_main}/fonts/tfm/public/alfaslabone/
%{_texmf_main}/fonts/type1/public/alfaslabone/
%{_texmf_main}/fonts/vf/public/alfaslabone/
%{_texmf_main}/tex/latex/alfaslabone/
%doc %{_texmf_main}/doc/fonts/alfaslabone/

%files -n texlive-algolrevived
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/algolrevived/
%{_texmf_main}/fonts/map/dvips/algolrevived/
%{_texmf_main}/fonts/opentype/public/algolrevived/
%{_texmf_main}/fonts/tfm/public/algolrevived/
%{_texmf_main}/fonts/type1/public/algolrevived/
%{_texmf_main}/fonts/vf/public/algolrevived/
%{_texmf_main}/tex/latex/algolrevived/
%doc %{_texmf_main}/doc/fonts/algolrevived/
%{_datadir}/fonts/algolrevived
%{_datadir}/appdata/algolrevived.metainfo.xml

%files -n texlive-allrunes
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/allrunes/
%{_texmf_main}/fonts/source/public/allrunes/
%{_texmf_main}/fonts/type1/public/allrunes/
%{_texmf_main}/tex/latex/allrunes/
%doc %{_texmf_main}/doc/fonts/allrunes/

%files -n texlive-almendra
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/almendra/
%{_texmf_main}/fonts/map/dvips/almendra/
%{_texmf_main}/fonts/tfm/public/almendra/
%{_texmf_main}/fonts/truetype/public/almendra/
%{_texmf_main}/fonts/type1/public/almendra/
%{_texmf_main}/fonts/vf/public/almendra/
%{_texmf_main}/tex/latex/almendra/
%doc %{_texmf_main}/doc/fonts/almendra/

%files -n texlive-almfixed
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/almfixed/
%{_texmf_main}/fonts/truetype/public/almfixed/
%doc %{_texmf_main}/doc/fonts/almfixed/
%{_datadir}/fonts/almfixed
%{_datadir}/appdata/almfixed.metainfo.xml

%files -n texlive-andika
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/andika/
%{_texmf_main}/fonts/map/dvips/andika/
%{_texmf_main}/fonts/tfm/SIL/andika/
%{_texmf_main}/fonts/truetype/SIL/andika/
%{_texmf_main}/fonts/type1/SIL/andika/
%{_texmf_main}/fonts/vf/SIL/andika/
%{_texmf_main}/tex/latex/andika/
%doc %{_texmf_main}/doc/fonts/andika/

%files -n texlive-anonymouspro
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/anonymouspro/
%{_texmf_main}/fonts/enc/dvips/anonymouspro/
%{_texmf_main}/fonts/map/dvips/anonymouspro/
%{_texmf_main}/fonts/tfm/public/anonymouspro/
%{_texmf_main}/fonts/truetype/public/anonymouspro/
%{_texmf_main}/fonts/type1/public/anonymouspro/
%{_texmf_main}/fonts/vf/public/anonymouspro/
%{_texmf_main}/tex/latex/anonymouspro/
%doc %{_texmf_main}/doc/fonts/anonymouspro/

%files -n texlive-antiqua
%license gpl2.txt
%{_texmf_main}/fonts/afm/urw/antiqua/
%{_texmf_main}/fonts/map/dvips/antiqua/
%{_texmf_main}/fonts/map/vtex/antiqua/
%{_texmf_main}/fonts/tfm/urw/antiqua/
%{_texmf_main}/fonts/type1/urw/antiqua/
%{_texmf_main}/fonts/vf/urw/antiqua/
%{_texmf_main}/tex/latex/antiqua/
%doc %{_texmf_main}/doc/fonts/antiqua/

%files -n texlive-antt
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/antt/
%{_texmf_main}/fonts/enc/dvips/antt/
%{_texmf_main}/fonts/map/dvips/antt/
%{_texmf_main}/fonts/opentype/public/antt/
%{_texmf_main}/fonts/tfm/public/antt/
%{_texmf_main}/fonts/type1/public/antt/
%{_texmf_main}/tex/latex/antt/
%{_texmf_main}/tex/plain/antt/
%doc %{_texmf_main}/doc/fonts/antt/
%doc %{_texmf_main}/doc/latex/antt/
%{_datadir}/fonts/antt
%{_datadir}/appdata/antt.metainfo.xml

%files -n texlive-archaic
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/archaic/
%{_texmf_main}/fonts/map/dvips/archaic/
%{_texmf_main}/fonts/source/public/archaic/
%{_texmf_main}/fonts/tfm/public/archaic/
%{_texmf_main}/fonts/type1/public/archaic/
%{_texmf_main}/tex/latex/archaic/
%doc %{_texmf_main}/doc/fonts/archaic/

%files -n texlive-archivo
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/archivo/
%{_texmf_main}/fonts/map/dvips/archivo/
%{_texmf_main}/fonts/opentype/public/archivo/
%{_texmf_main}/fonts/tfm/public/archivo/
%{_texmf_main}/fonts/type1/public/archivo/
%{_texmf_main}/fonts/vf/public/archivo/
%{_texmf_main}/tex/latex/archivo/
%doc %{_texmf_main}/doc/fonts/archivo/

%files -n texlive-arev
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/arev/
%{_texmf_main}/fonts/enc/dvips/arev/
%{_texmf_main}/fonts/map/dvips/arev/
%{_texmf_main}/fonts/tfm/public/arev/
%{_texmf_main}/fonts/type1/public/arev/
%{_texmf_main}/fonts/vf/public/arev/
%{_texmf_main}/tex/latex/arev/
%doc %{_texmf_main}/doc/fonts/arev/

%files -n texlive-arimo
%license apache2.txt
%{_texmf_main}/fonts/enc/dvips/arimo/
%{_texmf_main}/fonts/map/dvips/arimo/
%{_texmf_main}/fonts/tfm/google/arimo/
%{_texmf_main}/fonts/truetype/google/arimo/
%{_texmf_main}/fonts/type1/google/arimo/
%{_texmf_main}/fonts/vf/google/arimo/
%{_texmf_main}/tex/latex/arimo/
%doc %{_texmf_main}/doc/fonts/arimo/

%files -n texlive-arsenal
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/arsenal/
%{_texmf_main}/tex/latex/arsenal/
%doc %{_texmf_main}/doc/fonts/arsenal/

%files -n texlive-arsenal-math
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/arsenal-math/
%{_texmf_main}/fonts/source/public/arsenal-math/
%{_texmf_main}/tex/latex/arsenal-math/
%doc %{_texmf_main}/doc/fonts/arsenal-math/

%files -n texlive-arvo
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/arvo/
%{_texmf_main}/fonts/map/dvips/arvo/
%{_texmf_main}/fonts/tfm/public/arvo/
%{_texmf_main}/fonts/truetype/public/arvo/
%{_texmf_main}/fonts/vf/public/arvo/
%{_texmf_main}/tex/latex/arvo/
%doc %{_texmf_main}/doc/fonts/arvo/

%files -n texlive-asana-math
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/asana-math/
%{_texmf_main}/fonts/truetype/public/asana-math/
%doc %{_texmf_main}/doc/fonts/asana-math/

%files -n texlive-asapsym
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/omnibus-type/asapsym/
%{_texmf_main}/tex/generic/asapsym/
%{_texmf_main}/tex/latex/asapsym/
%{_texmf_main}/tex/plain/asapsym/
%doc %{_texmf_main}/doc/fonts/asapsym/
%{_datadir}/fonts/asapsym
%{_datadir}/appdata/asapsym.metainfo.xml

%files -n texlive-ascii-font
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/ascii-font/
%{_texmf_main}/fonts/tfm/public/ascii-font/
%{_texmf_main}/fonts/type1/public/ascii-font/
%{_texmf_main}/tex/latex/ascii-font/
%doc %{_texmf_main}/doc/fonts/ascii-font/

%files -n texlive-aspectratio
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/aspectratio/
%{_texmf_main}/fonts/source/public/aspectratio/
%{_texmf_main}/fonts/tfm/public/aspectratio/
%{_texmf_main}/fonts/type1/public/aspectratio/
%{_texmf_main}/tex/latex/aspectratio/
%doc %{_texmf_main}/doc/latex/aspectratio/

%files -n texlive-astro
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/astro/
%{_texmf_main}/fonts/tfm/public/astro/
%doc %{_texmf_main}/doc/fonts/astro/

%files -n texlive-atkinson
%license other-free.txt
%{_texmf_main}/fonts/enc/dvips/atkinson/
%{_texmf_main}/fonts/map/dvips/atkinson/
%{_texmf_main}/fonts/opentype/public/atkinson/
%{_texmf_main}/fonts/tfm/public/atkinson/
%{_texmf_main}/fonts/type1/public/atkinson/
%{_texmf_main}/fonts/vf/public/atkinson/
%{_texmf_main}/tex/latex/atkinson/
%doc %{_texmf_main}/doc/fonts/atkinson/

%files -n texlive-augie
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/augie/
%{_texmf_main}/fonts/map/dvips/augie/
%{_texmf_main}/fonts/tfm/public/augie/
%{_texmf_main}/fonts/type1/public/augie/
%{_texmf_main}/fonts/vf/public/augie/
%{_texmf_main}/tex/latex/augie/
%doc %{_texmf_main}/doc/latex/augie/

%files -n texlive-auncial-new
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/auncial-new/
%{_texmf_main}/fonts/map/dvips/auncial-new/
%{_texmf_main}/fonts/tfm/public/auncial-new/
%{_texmf_main}/fonts/type1/public/auncial-new/
%{_texmf_main}/tex/latex/auncial-new/
%doc %{_texmf_main}/doc/fonts/auncial-new/

%files -n texlive-aurical
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/aurical/
%{_texmf_main}/fonts/map/dvips/aurical/
%{_texmf_main}/fonts/source/public/aurical/
%{_texmf_main}/fonts/tfm/public/aurical/
%{_texmf_main}/fonts/type1/public/aurical/
%{_texmf_main}/tex/latex/aurical/
%doc %{_texmf_main}/doc/latex/aurical/

%files -n texlive-b1encoding
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/b1encoding/
%{_texmf_main}/tex/latex/b1encoding/
%doc %{_texmf_main}/doc/latex/b1encoding/

%files -n texlive-bahaistar
%license mit.txt
%{_texmf_main}/fonts/source/public/bahaistar/
%{_texmf_main}/fonts/tfm/public/bahaistar/
%{_texmf_main}/tex/latex/bahaistar/
%doc %{_texmf_main}/doc/fonts/bahaistar/

%files -n texlive-barcodes
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/barcodes/
%{_texmf_main}/fonts/tfm/public/barcodes/
%{_texmf_main}/tex/latex/barcodes/
%doc %{_texmf_main}/doc/latex/barcodes/

%files -n texlive-baskervaldadf
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/baskervaldadf/
%{_texmf_main}/fonts/enc/dvips/baskervaldadf/
%{_texmf_main}/fonts/map/dvips/baskervaldadf/
%{_texmf_main}/fonts/tfm/public/baskervaldadf/
%{_texmf_main}/fonts/type1/public/baskervaldadf/
%{_texmf_main}/fonts/vf/public/baskervaldadf/
%{_texmf_main}/tex/latex/baskervaldadf/
%doc %{_texmf_main}/doc/fonts/baskervaldadf/

%files -n texlive-baskervaldx
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/baskervaldx/
%{_texmf_main}/fonts/enc/dvips/baskervaldx/
%{_texmf_main}/fonts/map/dvips/baskervaldx/
%{_texmf_main}/fonts/opentype/public/baskervaldx/
%{_texmf_main}/fonts/tfm/public/baskervaldx/
%{_texmf_main}/fonts/type1/public/baskervaldx/
%{_texmf_main}/fonts/vf/public/baskervaldx/
%{_texmf_main}/tex/latex/baskervaldx/
%doc %{_texmf_main}/doc/fonts/baskervaldx/
%{_datadir}/fonts/baskervaldx
%{_datadir}/appdata/baskervaldx.metainfo.xml

%files -n texlive-baskervillef
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/baskervillef/
%{_texmf_main}/fonts/map/dvips/baskervillef/
%{_texmf_main}/fonts/opentype/public/baskervillef/
%{_texmf_main}/fonts/tfm/public/baskervillef/
%{_texmf_main}/fonts/type1/public/baskervillef/
%{_texmf_main}/fonts/vf/public/baskervillef/
%{_texmf_main}/tex/latex/baskervillef/
%doc %{_texmf_main}/doc/fonts/baskervillef/
%{_datadir}/fonts/baskervillef
%{_datadir}/appdata/baskervillef.metainfo.xml

%files -n texlive-bbding
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/bbding/
%{_texmf_main}/fonts/tfm/public/bbding/
%{_texmf_main}/tex/latex/bbding/
%doc %{_texmf_main}/doc/latex/bbding/

%files -n texlive-bbm
%license other-free.txt
%{_texmf_main}/fonts/source/public/bbm/
%{_texmf_main}/fonts/tfm/public/bbm/
%doc %{_texmf_main}/doc/fonts/bbm/

%files -n texlive-bbm-macros
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bbm-macros/
%doc %{_texmf_main}/doc/latex/bbm-macros/

%files -n texlive-bbold
%license bsd.txt
%{_texmf_main}/fonts/source/public/bbold/
%{_texmf_main}/fonts/tfm/public/bbold/
%{_texmf_main}/tex/latex/bbold/
%doc %{_texmf_main}/doc/latex/bbold/

%files -n texlive-bbold-type1
%license other-free.txt
%{_texmf_main}/fonts/afm/public/bbold-type1/
%{_texmf_main}/fonts/map/dvips/bbold-type1/
%{_texmf_main}/fonts/type1/public/bbold-type1/
%doc %{_texmf_main}/doc/fonts/bbold-type1/

%files -n texlive-bboldx
%license other-free.txt
%{_texmf_main}/fonts/afm/public/bboldx/
%{_texmf_main}/fonts/enc/dvips/bboldx/
%{_texmf_main}/fonts/map/dvips/bboldx/
%{_texmf_main}/fonts/tfm/public/bboldx/
%{_texmf_main}/fonts/type1/public/bboldx/
%{_texmf_main}/tex/latex/bboldx/
%doc %{_texmf_main}/doc/fonts/bboldx/

%files -n texlive-belleek
%license pd.txt
%{_texmf_main}/fonts/map/dvips/belleek/
%{_texmf_main}/fonts/truetype/public/belleek/
%{_texmf_main}/fonts/type1/public/belleek/
%doc %{_texmf_main}/doc/fonts/belleek/

%files -n texlive-bera
%{_texmf_main}/fonts/afm/public/bera/
%{_texmf_main}/fonts/map/dvips/bera/
%{_texmf_main}/fonts/tfm/public/bera/
%{_texmf_main}/fonts/type1/public/bera/
%{_texmf_main}/fonts/vf/public/bera/
%{_texmf_main}/tex/latex/bera/
%doc %{_texmf_main}/doc/fonts/bera/

%files -n texlive-berenisadf
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/arkandis/berenisadf/
%{_texmf_main}/fonts/enc/dvips/berenisadf/
%{_texmf_main}/fonts/map/dvips/berenisadf/
%{_texmf_main}/fonts/opentype/arkandis/berenisadf/
%{_texmf_main}/fonts/tfm/arkandis/berenisadf/
%{_texmf_main}/fonts/type1/arkandis/berenisadf/
%{_texmf_main}/tex/latex/berenisadf/
%doc %{_texmf_main}/doc/fonts/berenisadf/
%{_datadir}/fonts/berenisadf
%{_datadir}/appdata/berenisadf.metainfo.xml

%files -n texlive-beuron
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/beuron/
%{_texmf_main}/fonts/opentype/public/beuron/
%{_texmf_main}/fonts/source/public/beuron/
%{_texmf_main}/fonts/tfm/public/beuron/
%{_texmf_main}/fonts/type1/public/beuron/
%{_texmf_main}/tex/latex/beuron/
%doc %{_texmf_main}/doc/fonts/beuron/
%{_datadir}/fonts/beuron
%{_datadir}/appdata/beuron.metainfo.xml

%files -n texlive-bguq
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/bguq/
%{_texmf_main}/fonts/source/public/bguq/
%{_texmf_main}/fonts/tfm/public/bguq/
%{_texmf_main}/fonts/type1/public/bguq/
%{_texmf_main}/tex/latex/bguq/
%doc %{_texmf_main}/doc/fonts/bguq/

%files -n texlive-bitter
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/bitter/
%{_texmf_main}/fonts/map/dvips/bitter/
%{_texmf_main}/fonts/tfm/huerta/bitter/
%{_texmf_main}/fonts/truetype/huerta/bitter/
%{_texmf_main}/fonts/type1/huerta/bitter/
%{_texmf_main}/fonts/vf/huerta/bitter/
%{_texmf_main}/tex/latex/bitter/
%doc %{_texmf_main}/doc/fonts/bitter/

%files -n texlive-blacklettert1
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/blacklettert1/
%{_texmf_main}/fonts/vf/public/blacklettert1/
%{_texmf_main}/tex/latex/blacklettert1/
%doc %{_texmf_main}/doc/fonts/blacklettert1/

%files -n texlive-boisik
%license gpl2.txt
%{_texmf_main}/fonts/source/public/boisik/
%{_texmf_main}/fonts/tfm/public/boisik/
%{_texmf_main}/tex/latex/boisik/
%doc %{_texmf_main}/doc/fonts/boisik/

%files -n texlive-bonum-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bonum-otf/
%doc %{_texmf_main}/doc/fonts/bonum-otf/

%files -n texlive-bookhands
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/bookhands/
%{_texmf_main}/fonts/map/dvips/bookhands/
%{_texmf_main}/fonts/source/public/bookhands/
%{_texmf_main}/fonts/tfm/public/bookhands/
%{_texmf_main}/fonts/type1/public/bookhands/
%{_texmf_main}/tex/latex/bookhands/
%doc %{_texmf_main}/doc/fonts/bookhands/

%files -n texlive-boondox
%license ofl.txt
%{_texmf_main}/fonts/map/dvips/boondox/
%{_texmf_main}/fonts/tfm/public/boondox/
%{_texmf_main}/fonts/type1/public/boondox/
%{_texmf_main}/fonts/vf/public/boondox/
%{_texmf_main}/tex/latex/boondox/
%doc %{_texmf_main}/doc/fonts/boondox/

%files -n texlive-braille
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/braille/
%doc %{_texmf_main}/doc/latex/braille/

%files -n texlive-brushscr
%license pd.txt
%{_texmf_main}/dvips/brushscr/
%{_texmf_main}/fonts/afm/public/brushscr/
%{_texmf_main}/fonts/map/dvips/brushscr/
%{_texmf_main}/fonts/tfm/public/brushscr/
%{_texmf_main}/fonts/type1/public/brushscr/
%{_texmf_main}/fonts/vf/public/brushscr/
%{_texmf_main}/tex/latex/brushscr/
%doc %{_texmf_main}/doc/fonts/brushscr/

%files -n texlive-cabin
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/cabin/
%{_texmf_main}/fonts/map/dvips/cabin/
%{_texmf_main}/fonts/opentype/impallari/cabin/
%{_texmf_main}/fonts/tfm/impallari/cabin/
%{_texmf_main}/fonts/type1/impallari/cabin/
%{_texmf_main}/fonts/vf/impallari/cabin/
%{_texmf_main}/tex/latex/cabin/
%doc %{_texmf_main}/doc/fonts/cabin/
%{_datadir}/fonts/cabin
%{_datadir}/appdata/cabin.metainfo.xml

%files -n texlive-caladea
%license apache2.txt
%{_texmf_main}/fonts/enc/dvips/caladea/
%{_texmf_main}/fonts/map/dvips/caladea/
%{_texmf_main}/fonts/tfm/huerta/caladea/
%{_texmf_main}/fonts/truetype/huerta/caladea/
%{_texmf_main}/fonts/type1/huerta/caladea/
%{_texmf_main}/fonts/vf/huerta/caladea/
%{_texmf_main}/tex/latex/caladea/
%doc %{_texmf_main}/doc/fonts/caladea/

%files -n texlive-calligra
%license other-free.txt
%{_texmf_main}/fonts/source/public/calligra/
%{_texmf_main}/fonts/tfm/public/calligra/
%doc %{_texmf_main}/doc/latex/calligra/

%files -n texlive-calligra-type1
%license other-free.txt
%{_texmf_main}/fonts/afm/public/calligra-type1/
%{_texmf_main}/fonts/map/dvips/calligra-type1/
%{_texmf_main}/fonts/type1/public/calligra-type1/
%doc %{_texmf_main}/doc/fonts/calligra-type1/

%files -n texlive-cantarell
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/cantarell/
%{_texmf_main}/fonts/map/dvips/cantarell/
%{_texmf_main}/fonts/opentype/gnome/cantarell/
%{_texmf_main}/fonts/tfm/gnome/cantarell/
%{_texmf_main}/fonts/type1/gnome/cantarell/
%{_texmf_main}/fonts/vf/gnome/cantarell/
%{_texmf_main}/tex/latex/cantarell/
%doc %{_texmf_main}/doc/fonts/cantarell/

%files -n texlive-carlito
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/carlito/
%{_texmf_main}/fonts/map/dvips/carlito/
%{_texmf_main}/fonts/tfm/google/carlito/
%{_texmf_main}/fonts/truetype/google/carlito/
%{_texmf_main}/fonts/type1/google/carlito/
%{_texmf_main}/fonts/vf/google/carlito/
%{_texmf_main}/tex/latex/carlito/
%doc %{_texmf_main}/doc/fonts/carlito/

%files -n texlive-carolmin-ps
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/carolmin-ps/
%{_texmf_main}/fonts/map/dvips/carolmin-ps/
%{_texmf_main}/fonts/type1/public/carolmin-ps/
%doc %{_texmf_main}/doc/fonts/carolmin-ps/

%files -n texlive-cascadia-code
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/cascadia-code/
%{_texmf_main}/fonts/map/dvips/cascadia-code/
%{_texmf_main}/fonts/opentype/public/cascadia-code/
%{_texmf_main}/fonts/tfm/public/cascadia-code/
%{_texmf_main}/fonts/type1/public/cascadia-code/
%{_texmf_main}/fonts/vf/public/cascadia-code/
%{_texmf_main}/tex/latex/cascadia-code/
%doc %{_texmf_main}/doc/fonts/cascadia-code/

%files -n texlive-cascadiamono-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cascadiamono-otf/
%doc %{_texmf_main}/doc/fonts/cascadiamono-otf/

%files -n texlive-ccicons
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/ccicons/
%{_texmf_main}/fonts/map/dvips/ccicons/
%{_texmf_main}/fonts/opentype/public/ccicons/
%{_texmf_main}/fonts/tfm/public/ccicons/
%{_texmf_main}/fonts/type1/public/ccicons/
%{_texmf_main}/tex/latex/ccicons/
%doc %{_texmf_main}/doc/fonts/ccicons/
%doc %{_texmf_main}/doc/latex/ccicons/
%{_datadir}/fonts/ccicons
%{_datadir}/appdata/ccicons.metainfo.xml

%files -n texlive-cfr-initials
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cfr-initials/
%doc %{_texmf_main}/doc/latex/cfr-initials/

%files -n texlive-cfr-lm
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/cfr-lm/
%{_texmf_main}/fonts/map/dvips/cfr-lm/
%{_texmf_main}/fonts/tfm/public/cfr-lm/
%{_texmf_main}/fonts/vf/public/cfr-lm/
%{_texmf_main}/tex/latex/cfr-lm/
%doc %{_texmf_main}/doc/fonts/cfr-lm/

%files -n texlive-charissil
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/charissil/
%{_texmf_main}/fonts/map/dvips/charissil/
%{_texmf_main}/fonts/tfm/SIL/charissil/
%{_texmf_main}/fonts/truetype/SIL/charissil/
%{_texmf_main}/fonts/type1/SIL/charissil/
%{_texmf_main}/fonts/vf/SIL/charissil/
%{_texmf_main}/tex/latex/charissil/
%doc %{_texmf_main}/doc/fonts/charissil/

%files -n texlive-cherokee
%license other-free.txt
%{_texmf_main}/fonts/source/public/cherokee/
%{_texmf_main}/fonts/tfm/public/cherokee/
%{_texmf_main}/tex/latex/cherokee/
%doc %{_texmf_main}/doc/fonts/cherokee/

%files -n texlive-chivo
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/chivo/
%{_texmf_main}/fonts/map/dvips/chivo/
%{_texmf_main}/fonts/opentype/public/chivo/
%{_texmf_main}/fonts/tfm/public/chivo/
%{_texmf_main}/fonts/type1/public/chivo/
%{_texmf_main}/fonts/vf/public/chivo/
%{_texmf_main}/tex/latex/chivo/
%doc %{_texmf_main}/doc/fonts/chivo/
%{_datadir}/fonts/chivo
%{_datadir}/appdata/chivo.metainfo.xml

%files -n texlive-cinzel
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/cinzel/
%{_texmf_main}/fonts/map/dvips/cinzel/
%{_texmf_main}/fonts/tfm/ndiscovered/cinzel/
%{_texmf_main}/fonts/truetype/ndiscovered/cinzel/
%{_texmf_main}/fonts/type1/ndiscovered/cinzel/
%{_texmf_main}/fonts/vf/ndiscovered/cinzel/
%{_texmf_main}/tex/latex/cinzel/
%doc %{_texmf_main}/doc/fonts/cinzel/

%files -n texlive-clara
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/clara/
%{_texmf_main}/fonts/map/dvips/clara/
%{_texmf_main}/fonts/opentype/public/clara/
%{_texmf_main}/fonts/tfm/public/clara/
%{_texmf_main}/fonts/type1/public/clara/
%{_texmf_main}/fonts/vf/public/clara/
%{_texmf_main}/tex/latex/clara/
%doc %{_texmf_main}/doc/fonts/clara/
%{_datadir}/fonts/clara
%{_datadir}/appdata/clara.metainfo.xml

%files -n texlive-clearsans
%license apache2.txt
%{_texmf_main}/fonts/enc/dvips/clearsans/
%{_texmf_main}/fonts/map/dvips/clearsans/
%{_texmf_main}/fonts/tfm/intel/clearsans/
%{_texmf_main}/fonts/truetype/intel/clearsans/
%{_texmf_main}/fonts/type1/intel/clearsans/
%{_texmf_main}/fonts/vf/intel/clearsans/
%{_texmf_main}/tex/latex/clearsans/
%doc %{_texmf_main}/doc/fonts/clearsans/

%files -n texlive-cm-lgc
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/cm-lgc/
%{_texmf_main}/fonts/enc/dvips/cm-lgc/
%{_texmf_main}/fonts/map/dvips/cm-lgc/
%{_texmf_main}/fonts/ofm/public/cm-lgc/
%{_texmf_main}/fonts/ovf/public/cm-lgc/
%{_texmf_main}/fonts/tfm/public/cm-lgc/
%{_texmf_main}/fonts/type1/public/cm-lgc/
%{_texmf_main}/fonts/vf/public/cm-lgc/
%{_texmf_main}/tex/latex/cm-lgc/
%doc %{_texmf_main}/doc/fonts/cm-lgc/

%files -n texlive-cm-mf-extra-bold
%license gpl2.txt
%{_texmf_main}/fonts/source/public/cm-mf-extra-bold/
%{_texmf_main}/fonts/tfm/public/cm-mf-extra-bold/

%files -n texlive-cm-unicode
%license ofl.txt
%{_texmf_main}/fonts/afm/public/cm-unicode/
%{_texmf_main}/fonts/enc/dvips/cm-unicode/
%{_texmf_main}/fonts/map/dvips/cm-unicode/
%{_texmf_main}/fonts/opentype/public/cm-unicode/
%{_texmf_main}/fonts/type1/public/cm-unicode/
%doc %{_texmf_main}/doc/fonts/cm-unicode/
%{_datadir}/fonts/cm-unicode
%{_datadir}/appdata/cm-unicode.metainfo.xml

%files -n texlive-cmathbb
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/cmathbb/
%{_texmf_main}/fonts/map/dvips/cmathbb/
%{_texmf_main}/fonts/tfm/public/cmathbb/
%{_texmf_main}/fonts/type1/public/cmathbb/
%{_texmf_main}/fonts/vf/public/cmathbb/
%{_texmf_main}/tex/latex/cmathbb/
%doc %{_texmf_main}/doc/fonts/cmathbb/

%files -n texlive-cmbright
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/cmbright/
%{_texmf_main}/fonts/tfm/public/cmbright/
%{_texmf_main}/tex/latex/cmbright/
%doc %{_texmf_main}/doc/fonts/cmbright/
%doc %{_texmf_main}/doc/latex/cmbright/

%files -n texlive-cmexb
%license pd.txt
%{_texmf_main}/fonts/map/dvips/cmexb/
%{_texmf_main}/fonts/tfm/public/cmexb/
%{_texmf_main}/fonts/type1/public/cmexb/
%doc %{_texmf_main}/doc/fonts/cmexb/

%files -n texlive-cmll
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/cmll/
%{_texmf_main}/fonts/source/public/cmll/
%{_texmf_main}/fonts/tfm/public/cmll/
%{_texmf_main}/fonts/type1/public/cmll/
%{_texmf_main}/tex/latex/cmll/
%doc %{_texmf_main}/doc/fonts/cmll/

%files -n texlive-cmpica
%license pd.txt
%{_texmf_main}/fonts/source/public/cmpica/
%{_texmf_main}/fonts/tfm/public/cmpica/
%doc %{_texmf_main}/doc/latex/cmpica/

%files -n texlive-cmsrb
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/cmsrb/
%{_texmf_main}/fonts/enc/dvips/cmsrb/
%{_texmf_main}/fonts/map/dvips/cmsrb/
%{_texmf_main}/fonts/tfm/public/cmsrb/
%{_texmf_main}/fonts/type1/public/cmsrb/
%{_texmf_main}/fonts/vf/public/cmsrb/
%{_texmf_main}/tex/latex/cmsrb/
%doc %{_texmf_main}/doc/fonts/cmsrb/

%files -n texlive-cmtiup
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/cmtiup/
%{_texmf_main}/fonts/tfm/public/cmtiup/
%{_texmf_main}/fonts/vf/public/cmtiup/
%{_texmf_main}/tex/latex/cmtiup/
%doc %{_texmf_main}/doc/latex/cmtiup/

%files -n texlive-cmupint
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/cmupint/
%{_texmf_main}/fonts/map/dvips/cmupint/
%{_texmf_main}/fonts/source/public/cmupint/
%{_texmf_main}/fonts/tfm/public/cmupint/
%{_texmf_main}/fonts/type1/public/cmupint/
%{_texmf_main}/tex/latex/cmupint/
%doc %{_texmf_main}/doc/fonts/cmupint/

%files -n texlive-cochineal
%license ofl.txt
%{_texmf_main}/fonts/afm/public/cochineal/
%{_texmf_main}/fonts/enc/dvips/cochineal/
%{_texmf_main}/fonts/map/dvips/cochineal/
%{_texmf_main}/fonts/opentype/public/cochineal/
%{_texmf_main}/fonts/tfm/public/cochineal/
%{_texmf_main}/fonts/type1/public/cochineal/
%{_texmf_main}/fonts/vf/public/cochineal/
%{_texmf_main}/tex/latex/cochineal/
%doc %{_texmf_main}/doc/fonts/cochineal/
%{_datadir}/fonts/cochineal
%{_datadir}/appdata/cochineal.metainfo.xml

%files -n texlive-coelacanth
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/coelacanth/
%{_texmf_main}/fonts/map/dvips/coelacanth/
%{_texmf_main}/fonts/opentype/public/coelacanth/
%{_texmf_main}/fonts/tfm/public/coelacanth/
%{_texmf_main}/fonts/type1/public/coelacanth/
%{_texmf_main}/fonts/vf/public/coelacanth/
%{_texmf_main}/tex/latex/coelacanth/
%doc %{_texmf_main}/doc/fonts/coelacanth/
%{_datadir}/fonts/coelacanth
%{_datadir}/appdata/coelacanth.metainfo.xml

%files -n texlive-comfortaa
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/comfortaa/
%{_texmf_main}/fonts/map/dvips/comfortaa/
%{_texmf_main}/fonts/tfm/aajohan/comfortaa/
%{_texmf_main}/fonts/truetype/aajohan/comfortaa/
%{_texmf_main}/fonts/type1/aajohan/comfortaa/
%{_texmf_main}/fonts/vf/aajohan/comfortaa/
%{_texmf_main}/tex/latex/comfortaa/
%doc %{_texmf_main}/doc/fonts/comfortaa/

%files -n texlive-comicneue
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/comicneue/
%{_texmf_main}/fonts/map/dvips/comicneue/
%{_texmf_main}/fonts/opentype/rozynski/comicneue/
%{_texmf_main}/fonts/tfm/rozynski/comicneue/
%{_texmf_main}/fonts/type1/rozynski/comicneue/
%{_texmf_main}/fonts/vf/rozynski/comicneue/
%{_texmf_main}/tex/latex/comicneue/
%doc %{_texmf_main}/doc/latex/comicneue/
%{_datadir}/fonts/comicneue
%{_datadir}/appdata/comicneue.metainfo.xml

%files -n texlive-concmath-fonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/concmath-fonts/
%{_texmf_main}/fonts/tfm/public/concmath-fonts/
%doc %{_texmf_main}/doc/fonts/concmath-fonts/

%files -n texlive-concmath-otf
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/concmath-otf/
%{_texmf_main}/tex/latex/concmath-otf/
%doc %{_texmf_main}/doc/fonts/concmath-otf/

%files -n texlive-cookingsymbols
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/cookingsymbols/
%{_texmf_main}/fonts/tfm/public/cookingsymbols/
%{_texmf_main}/tex/latex/cookingsymbols/
%doc %{_texmf_main}/doc/latex/cookingsymbols/

%files -n texlive-cooperhewitt
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/cooperhewitt/
%{_texmf_main}/fonts/map/dvips/cooperhewitt/
%{_texmf_main}/fonts/opentype/public/cooperhewitt/
%{_texmf_main}/fonts/tfm/public/cooperhewitt/
%{_texmf_main}/fonts/type1/public/cooperhewitt/
%{_texmf_main}/fonts/vf/public/cooperhewitt/
%{_texmf_main}/tex/latex/cooperhewitt/
%doc %{_texmf_main}/doc/fonts/cooperhewitt/

%files -n texlive-cormorantgaramond
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/cormorantgaramond/
%{_texmf_main}/fonts/map/dvips/cormorantgaramond/
%{_texmf_main}/fonts/tfm/catharsis/cormorantgaramond/
%{_texmf_main}/fonts/truetype/catharsis/cormorantgaramond/
%{_texmf_main}/fonts/type1/catharsis/cormorantgaramond/
%{_texmf_main}/fonts/vf/catharsis/cormorantgaramond/
%{_texmf_main}/tex/latex/cormorantgaramond/
%doc %{_texmf_main}/doc/fonts/cormorantgaramond/

%files -n texlive-countriesofeurope
%license ofl.txt
%{_texmf_main}/fonts/afm/public/countriesofeurope/
%{_texmf_main}/fonts/enc/dvips/countriesofeurope/
%{_texmf_main}/fonts/map/dvips/countriesofeurope/
%{_texmf_main}/fonts/opentype/public/countriesofeurope/
%{_texmf_main}/fonts/tfm/public/countriesofeurope/
%{_texmf_main}/fonts/type1/public/countriesofeurope/
%{_texmf_main}/tex/latex/countriesofeurope/
%doc %{_texmf_main}/doc/fonts/countriesofeurope/
%{_datadir}/fonts/countriesofeurope
%{_datadir}/appdata/countriesofeurope.metainfo.xml

%files -n texlive-courier-scaled
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/courier-scaled/
%doc %{_texmf_main}/doc/fonts/courier-scaled/

%files -n texlive-courierten
%license mit.txt
%{_texmf_main}/fonts/enc/dvips/courierten/
%{_texmf_main}/fonts/map/dvips/courierten/
%{_texmf_main}/fonts/opentype/public/courierten/
%{_texmf_main}/fonts/tfm/public/courierten/
%{_texmf_main}/fonts/type1/public/courierten/
%{_texmf_main}/fonts/vf/public/courierten/
%{_texmf_main}/tex/latex/courierten/
%doc %{_texmf_main}/doc/fonts/courierten/

%files -n texlive-crimson
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/crimson/
%{_texmf_main}/fonts/map/dvips/crimson/
%{_texmf_main}/fonts/opentype/kosch/crimson/
%{_texmf_main}/fonts/tfm/kosch/crimson/
%{_texmf_main}/fonts/type1/kosch/crimson/
%{_texmf_main}/fonts/vf/kosch/crimson/
%{_texmf_main}/tex/latex/crimson/
%doc %{_texmf_main}/doc/fonts/crimson/
%{_datadir}/fonts/crimson
%{_datadir}/appdata/crimson.metainfo.xml

%files -n texlive-crimsonpro
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/crimsonpro/
%{_texmf_main}/fonts/map/dvips/crimsonpro/
%{_texmf_main}/fonts/tfm/public/crimsonpro/
%{_texmf_main}/fonts/truetype/public/crimsonpro/
%{_texmf_main}/fonts/type1/public/crimsonpro/
%{_texmf_main}/fonts/vf/public/crimsonpro/
%{_texmf_main}/tex/latex/crimsonpro/
%doc %{_texmf_main}/doc/fonts/crimsonpro/

%files -n texlive-cryst
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/cryst/
%{_texmf_main}/fonts/source/public/cryst/
%{_texmf_main}/fonts/tfm/public/cryst/
%{_texmf_main}/fonts/type1/public/cryst/
%doc %{_texmf_main}/doc/latex/cryst/

%files -n texlive-cuprum
%license ofl.txt
%{_texmf_main}/fonts/map/dvips/cuprum/
%{_texmf_main}/fonts/tfm/public/cuprum/
%{_texmf_main}/fonts/truetype/public/cuprum/
%{_texmf_main}/tex/latex/cuprum/
%doc %{_texmf_main}/doc/fonts/cuprum/

%files -n texlive-cyklop
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/cyklop/
%{_texmf_main}/fonts/enc/dvips/cyklop/
%{_texmf_main}/fonts/map/dvips/cyklop/
%{_texmf_main}/fonts/opentype/public/cyklop/
%{_texmf_main}/fonts/tfm/public/cyklop/
%{_texmf_main}/fonts/type1/public/cyklop/
%{_texmf_main}/tex/latex/cyklop/
%doc %{_texmf_main}/doc/fonts/cyklop/
%{_datadir}/fonts/cyklop
%{_datadir}/appdata/cyklop.metainfo.xml

%files -n texlive-cyrillic-modern
%license ofl.txt
%{_texmf_main}/dvips/cyrillic-modern/
%{_texmf_main}/fonts/afm/public/cyrillic-modern/
%{_texmf_main}/fonts/enc/dvips/cyrillic-modern/
%{_texmf_main}/fonts/map/dvips/cyrillic-modern/
%{_texmf_main}/fonts/opentype/public/cyrillic-modern/
%{_texmf_main}/fonts/tfm/public/cyrillic-modern/
%{_texmf_main}/fonts/type1/public/cyrillic-modern/
%{_texmf_main}/tex/latex/cyrillic-modern/
%doc %{_texmf_main}/doc/fonts/cyrillic-modern/

%files -n texlive-dancers
%license other-free.txt
%{_texmf_main}/fonts/source/public/dancers/
%{_texmf_main}/fonts/tfm/public/dancers/

%files -n texlive-dantelogo
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/dantelogo/
%{_texmf_main}/fonts/map/dvips/dantelogo/
%{_texmf_main}/fonts/opentype/public/dantelogo/
%{_texmf_main}/fonts/tfm/public/dantelogo/
%{_texmf_main}/fonts/type1/public/dantelogo/
%{_texmf_main}/fonts/vf/public/dantelogo/
%{_texmf_main}/tex/latex/dantelogo/
%doc %{_texmf_main}/doc/fonts/dantelogo/
%{_datadir}/fonts/dantelogo
%{_datadir}/appdata/dantelogo.metainfo.xml

%files -n texlive-dejavu
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/dejavu/
%{_texmf_main}/fonts/enc/dvips/dejavu/
%{_texmf_main}/fonts/map/dvips/dejavu/
%{_texmf_main}/fonts/tfm/public/dejavu/
%{_texmf_main}/fonts/truetype/public/dejavu/
%{_texmf_main}/fonts/type1/public/dejavu/
%{_texmf_main}/fonts/vf/public/dejavu/
%{_texmf_main}/tex/latex/dejavu/
%doc %{_texmf_main}/doc/fonts/dejavu/

%files -n texlive-dejavu-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dejavu-otf/
%doc %{_texmf_main}/doc/fonts/dejavu-otf/

%files -n texlive-dice
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/dice/
%{_texmf_main}/fonts/tfm/public/dice/
%doc %{_texmf_main}/doc/fonts/dice/

%files -n texlive-dictsym
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/dictsym/
%{_texmf_main}/fonts/map/dvips/dictsym/
%{_texmf_main}/fonts/map/vtex/dictsym/
%{_texmf_main}/fonts/tfm/public/dictsym/
%{_texmf_main}/fonts/type1/public/dictsym/
%{_texmf_main}/tex/latex/dictsym/
%doc %{_texmf_main}/doc/fonts/dictsym/

%files -n texlive-dingbat
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/dingbat/
%{_texmf_main}/fonts/tfm/public/dingbat/
%{_texmf_main}/tex/latex/dingbat/
%doc %{_texmf_main}/doc/fonts/dingbat/

%files -n texlive-domitian
%license other-free.txt
%{_texmf_main}/fonts/enc/dvips/domitian/
%{_texmf_main}/fonts/map/dvips/domitian/
%{_texmf_main}/fonts/opentype/public/domitian/
%{_texmf_main}/fonts/tfm/public/domitian/
%{_texmf_main}/fonts/type1/public/domitian/
%{_texmf_main}/fonts/vf/public/domitian/
%{_texmf_main}/tex/latex/domitian/
%doc %{_texmf_main}/doc/fonts/domitian/
%{_datadir}/fonts/domitian
%{_datadir}/appdata/domitian.metainfo.xml

%files -n texlive-doublestroke
%license other-free.txt
%{_texmf_main}/fonts/map/dvips/doublestroke/
%{_texmf_main}/fonts/source/public/doublestroke/
%{_texmf_main}/fonts/tfm/public/doublestroke/
%{_texmf_main}/fonts/type1/public/doublestroke/
%{_texmf_main}/tex/latex/doublestroke/
%doc %{_texmf_main}/doc/fonts/doublestroke/

%files -n texlive-doulossil
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/doulossil/
%doc %{_texmf_main}/doc/fonts/doulossil/

%files -n texlive-dozenal
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/dozenal/
%{_texmf_main}/fonts/map/dvips/dozenal/
%{_texmf_main}/fonts/source/public/dozenal/
%{_texmf_main}/fonts/tfm/public/dozenal/
%{_texmf_main}/fonts/type1/public/dozenal/
%{_texmf_main}/tex/latex/dozenal/
%doc %{_texmf_main}/doc/fonts/dozenal/

%files -n texlive-drm
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/drm/
%{_texmf_main}/fonts/map/dvips/drm/
%{_texmf_main}/fonts/opentype/public/drm/
%{_texmf_main}/fonts/source/public/drm/
%{_texmf_main}/fonts/tfm/public/drm/
%{_texmf_main}/fonts/type1/public/drm/
%{_texmf_main}/tex/latex/drm/
%doc %{_texmf_main}/doc/fonts/drm/
%{_datadir}/fonts/drm
%{_datadir}/appdata/drm.metainfo.xml

%files -n texlive-droid
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/droid/
%{_texmf_main}/fonts/map/dvips/droid/
%{_texmf_main}/fonts/tfm/ascender/droid/
%{_texmf_main}/fonts/truetype/ascender/droid/
%{_texmf_main}/fonts/type1/ascender/droid/
%{_texmf_main}/fonts/vf/ascender/droid/
%{_texmf_main}/tex/latex/droid/
%doc %{_texmf_main}/doc/fonts/droid/

%files -n texlive-dsserif
%license ofl.txt
%{_texmf_main}/fonts/afm/public/dsserif/
%{_texmf_main}/fonts/map/dvips/dsserif/
%{_texmf_main}/fonts/tfm/public/dsserif/
%{_texmf_main}/fonts/type1/public/dsserif/
%{_texmf_main}/tex/latex/dsserif/
%doc %{_texmf_main}/doc/fonts/dsserif/

%files -n texlive-duerer
%license pd.txt
%{_texmf_main}/fonts/source/public/duerer/
%{_texmf_main}/fonts/tfm/public/duerer/
%doc %{_texmf_main}/doc/fonts/duerer/

%files -n texlive-duerer-latex
%license gpl2.txt
%{_texmf_main}/tex/latex/duerer-latex/
%doc %{_texmf_main}/doc/latex/duerer-latex/

%files -n texlive-dutchcal
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/dutchcal/
%{_texmf_main}/fonts/map/dvips/dutchcal/
%{_texmf_main}/fonts/tfm/public/dutchcal/
%{_texmf_main}/fonts/type1/public/dutchcal/
%{_texmf_main}/fonts/vf/public/dutchcal/
%{_texmf_main}/tex/latex/dutchcal/
%doc %{_texmf_main}/doc/fonts/dutchcal/

%files -n texlive-ean
%license gpl2.txt
%{_texmf_main}/tex/generic/ean/
%doc %{_texmf_main}/doc/generic/ean/

%files -n texlive-ebgaramond
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/ebgaramond/
%{_texmf_main}/fonts/map/dvips/ebgaramond/
%{_texmf_main}/fonts/opentype/public/ebgaramond/
%{_texmf_main}/fonts/tfm/public/ebgaramond/
%{_texmf_main}/fonts/type1/public/ebgaramond/
%{_texmf_main}/fonts/vf/public/ebgaramond/
%{_texmf_main}/tex/latex/ebgaramond/
%doc %{_texmf_main}/doc/fonts/ebgaramond/

%files -n texlive-ebgaramond-maths
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/ebgaramond-maths/
%{_texmf_main}/fonts/map/dvips/ebgaramond-maths/
%{_texmf_main}/fonts/tfm/public/ebgaramond-maths/
%{_texmf_main}/tex/latex/ebgaramond-maths/
%doc %{_texmf_main}/doc/fonts/ebgaramond-maths/

%files -n texlive-ecc
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/ecc/
%{_texmf_main}/fonts/tfm/public/ecc/
%doc %{_texmf_main}/doc/fonts/ecc/

%files -n texlive-eco
%license gpl2.txt
%{_texmf_main}/fonts/tfm/public/eco/
%{_texmf_main}/fonts/vf/public/eco/
%{_texmf_main}/tex/latex/eco/
%doc %{_texmf_main}/doc/fonts/eco/

%files -n texlive-eczar
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/eczar/
%doc %{_texmf_main}/doc/fonts/eczar/

%files -n texlive-eiad
%license pd.txt
%{_texmf_main}/fonts/source/public/eiad/
%{_texmf_main}/fonts/tfm/public/eiad/
%{_texmf_main}/tex/latex/eiad/
%doc %{_texmf_main}/doc/fonts/eiad/

%files -n texlive-eiad-ltx
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/eiad-ltx/
%{_texmf_main}/tex/latex/eiad-ltx/
%doc %{_texmf_main}/doc/latex/eiad-ltx/

%files -n texlive-ektype-tanka
%license lppl1.3c.txt
%{_texmf_main}/fonts/truetype/public/ektype-tanka/
%doc %{_texmf_main}/doc/fonts/ektype-tanka/

%files -n texlive-electrumadf
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/electrumadf/
%{_texmf_main}/fonts/enc/dvips/electrumadf/
%{_texmf_main}/fonts/map/dvips/electrumadf/
%{_texmf_main}/fonts/tfm/public/electrumadf/
%{_texmf_main}/fonts/type1/public/electrumadf/
%{_texmf_main}/fonts/vf/public/electrumadf/
%{_texmf_main}/tex/latex/electrumadf/
%doc %{_texmf_main}/doc/fonts/electrumadf/

%files -n texlive-elvish
%license other-free.txt
%{_texmf_main}/fonts/source/public/elvish/
%{_texmf_main}/fonts/tfm/public/elvish/
%doc %{_texmf_main}/doc/fonts/elvish/

%files -n texlive-epigrafica
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/epigrafica/
%{_texmf_main}/fonts/enc/dvips/epigrafica/
%{_texmf_main}/fonts/map/dvips/epigrafica/
%{_texmf_main}/fonts/tfm/public/epigrafica/
%{_texmf_main}/fonts/type1/public/epigrafica/
%{_texmf_main}/fonts/vf/public/epigrafica/
%{_texmf_main}/tex/latex/epigrafica/
%doc %{_texmf_main}/doc/fonts/epigrafica/

%files -n texlive-epsdice
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/epsdice/
%doc %{_texmf_main}/doc/latex/epsdice/

%files -n texlive-erewhon
%license ofl.txt
%{_texmf_main}/fonts/afm/public/erewhon/
%{_texmf_main}/fonts/enc/dvips/erewhon/
%{_texmf_main}/fonts/map/dvips/erewhon/
%{_texmf_main}/fonts/opentype/public/erewhon/
%{_texmf_main}/fonts/tfm/public/erewhon/
%{_texmf_main}/fonts/type1/public/erewhon/
%{_texmf_main}/fonts/vf/public/erewhon/
%{_texmf_main}/tex/latex/erewhon/
%doc %{_texmf_main}/doc/fonts/erewhon/
%{_datadir}/fonts/erewhon
%{_datadir}/appdata/erewhon.metainfo.xml

%files -n texlive-erewhon-math
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/erewhon-math/
%{_texmf_main}/tex/latex/erewhon-math/
%doc %{_texmf_main}/doc/fonts/erewhon-math/
%{_datadir}/fonts/erewhon-math
%{_datadir}/appdata/erewhon-math.metainfo.xml

%files -n texlive-esrelation
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/esrelation/
%{_texmf_main}/fonts/source/public/esrelation/
%{_texmf_main}/fonts/tfm/public/esrelation/
%{_texmf_main}/fonts/type1/public/esrelation/
%{_texmf_main}/tex/latex/esrelation/
%doc %{_texmf_main}/doc/fonts/esrelation/

%files -n texlive-esstix
%license ofl.txt
%{_texmf_main}/fonts/afm/esstix/
%{_texmf_main}/fonts/map/dvips/esstix/
%{_texmf_main}/fonts/tfm/public/esstix/
%{_texmf_main}/fonts/type1/public/esstix/
%{_texmf_main}/fonts/vf/public/esstix/
%{_texmf_main}/tex/latex/esstix/
%doc %{_texmf_main}/doc/fonts/esstix/

%files -n texlive-esvect
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/esvect/
%{_texmf_main}/fonts/source/public/esvect/
%{_texmf_main}/fonts/tfm/public/esvect/
%{_texmf_main}/fonts/type1/public/esvect/
%{_texmf_main}/tex/latex/esvect/
%doc %{_texmf_main}/doc/latex/esvect/

%files -n texlive-etbb
%license mit.txt
%{_texmf_main}/fonts/afm/public/etbb/
%{_texmf_main}/fonts/enc/dvips/etbb/
%{_texmf_main}/fonts/map/dvips/etbb/
%{_texmf_main}/fonts/opentype/public/etbb/
%{_texmf_main}/fonts/tfm/public/etbb/
%{_texmf_main}/fonts/type1/public/etbb/
%{_texmf_main}/fonts/vf/public/etbb/
%{_texmf_main}/tex/latex/etbb/
%doc %{_texmf_main}/doc/fonts/etbb/
%{_datadir}/fonts/etbb
%{_datadir}/appdata/etbb.metainfo.xml

%files -n texlive-euler-math
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/euler-math/
%{_texmf_main}/tex/latex/euler-math/
%doc %{_texmf_main}/doc/fonts/euler-math/

%files -n texlive-eulervm
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/eulervm/
%{_texmf_main}/fonts/vf/public/eulervm/
%{_texmf_main}/tex/latex/eulervm/
%doc %{_texmf_main}/doc/latex/eulervm/

%files -n texlive-euxm
%license other-free.txt
%{_texmf_main}/fonts/source/public/euxm/
%{_texmf_main}/fonts/tfm/public/euxm/

%files -n texlive-fbb
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/fbb/
%{_texmf_main}/fonts/map/dvips/fbb/
%{_texmf_main}/fonts/opentype/public/fbb/
%{_texmf_main}/fonts/tfm/public/fbb/
%{_texmf_main}/fonts/type1/public/fbb/
%{_texmf_main}/fonts/vf/public/fbb/
%{_texmf_main}/tex/latex/fbb/
%doc %{_texmf_main}/doc/fonts/fbb/
%{_datadir}/fonts/fbb
%{_datadir}/appdata/fbb.metainfo.xml

%files -n texlive-fdsymbol
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/fdsymbol/
%{_texmf_main}/fonts/map/dvips/fdsymbol/
%{_texmf_main}/fonts/opentype/public/fdsymbol/
%{_texmf_main}/fonts/source/public/fdsymbol/
%{_texmf_main}/fonts/tfm/public/fdsymbol/
%{_texmf_main}/fonts/type1/public/fdsymbol/
%{_texmf_main}/tex/latex/fdsymbol/
%doc %{_texmf_main}/doc/fonts/fdsymbol/
%doc %{_texmf_main}/doc/latex/fdsymbol/
%{_datadir}/fonts/fdsymbol
%{_datadir}/appdata/fdsymbol.metainfo.xml

%files -n texlive-fetamont
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/fetamont/
%{_texmf_main}/fonts/map/dvips/fetamont/
%{_texmf_main}/fonts/opentype/public/fetamont/
%{_texmf_main}/fonts/source/public/fetamont/
%{_texmf_main}/fonts/tfm/public/fetamont/
%{_texmf_main}/fonts/type1/public/fetamont/
%{_texmf_main}/metapost/fetamont/
%{_texmf_main}/tex/latex/fetamont/
%doc %{_texmf_main}/doc/fonts/fetamont/
%{_datadir}/fonts/fetamont
%{_datadir}/appdata/fetamont.metainfo.xml

%files -n texlive-feyn
%license bsd2.txt
%{_texmf_main}/fonts/source/public/feyn/
%{_texmf_main}/fonts/tfm/public/feyn/
%{_texmf_main}/tex/latex/feyn/
%doc %{_texmf_main}/doc/fonts/feyn/

%files -n texlive-fge
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/fge/
%{_texmf_main}/fonts/source/public/fge/
%{_texmf_main}/fonts/tfm/public/fge/
%{_texmf_main}/fonts/type1/public/fge/
%{_texmf_main}/tex/latex/fge/
%doc %{_texmf_main}/doc/fonts/fge/

%files -n texlive-fira
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/fira/
%{_texmf_main}/fonts/map/dvips/fira/
%{_texmf_main}/fonts/opentype/public/fira/
%{_texmf_main}/fonts/tfm/public/fira/
%{_texmf_main}/fonts/type1/public/fira/
%{_texmf_main}/fonts/vf/public/fira/
%{_texmf_main}/tex/latex/fira/
%doc %{_texmf_main}/doc/fonts/fira/

%files -n texlive-firamath
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/firamath/
%doc %{_texmf_main}/doc/fonts/firamath/
%{_datadir}/fonts/firamath
%{_datadir}/appdata/firamath.metainfo.xml

%files -n texlive-firamath-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/firamath-otf/
%doc %{_texmf_main}/doc/fonts/firamath-otf/

%files -n texlive-foekfont
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/foekfont/
%{_texmf_main}/fonts/tfm/public/foekfont/
%{_texmf_main}/fonts/type1/public/foekfont/
%{_texmf_main}/tex/latex/foekfont/
%doc %{_texmf_main}/doc/latex/foekfont/

%files -n texlive-fonetika
%license gpl.txt
%{_texmf_main}/fonts/afm/public/fonetika/
%{_texmf_main}/fonts/map/dvips/fonetika/
%{_texmf_main}/fonts/tfm/public/fonetika/
%{_texmf_main}/fonts/truetype/public/fonetika/
%{_texmf_main}/fonts/type1/public/fonetika/
%{_texmf_main}/tex/latex/fonetika/
%doc %{_texmf_main}/doc/fonts/fonetika/

%files -n texlive-fontawesome
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/fontawesome/
%{_texmf_main}/fonts/map/dvips/fontawesome/
%{_texmf_main}/fonts/opentype/public/fontawesome/
%{_texmf_main}/fonts/tfm/public/fontawesome/
%{_texmf_main}/fonts/type1/public/fontawesome/
%{_texmf_main}/tex/latex/fontawesome/
%doc %{_texmf_main}/doc/fonts/fontawesome/

%files -n texlive-fontawesome5
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/fontawesome5/
%{_texmf_main}/fonts/map/dvips/fontawesome5/
%{_texmf_main}/fonts/opentype/public/fontawesome5/
%{_texmf_main}/fonts/tfm/public/fontawesome5/
%{_texmf_main}/fonts/type1/public/fontawesome5/
%{_texmf_main}/tex/latex/fontawesome5/
%doc %{_texmf_main}/doc/fonts/fontawesome5/

%files -n texlive-fontawesome6
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/fontawesome6/
%{_texmf_main}/fonts/map/dvips/fontawesome6/
%{_texmf_main}/fonts/opentype/public/fontawesome6/
%{_texmf_main}/fonts/tfm/public/fontawesome6/
%{_texmf_main}/fonts/type1/public/fontawesome6/
%{_texmf_main}/tex/latex/fontawesome6/
%doc %{_texmf_main}/doc/fonts/fontawesome6/

%files -n texlive-fontawesome7
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/fontawesome7/
%{_texmf_main}/fonts/map/dvips/fontawesome7/
%{_texmf_main}/fonts/opentype/public/fontawesome7/
%{_texmf_main}/fonts/tfm/public/fontawesome7/
%{_texmf_main}/fonts/type1/public/fontawesome7/
%{_texmf_main}/tex/latex/fontawesome7/
%doc %{_texmf_main}/doc/fonts/fontawesome7/

%files -n texlive-fontawesomescaled
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fontawesomescaled/
%doc %{_texmf_main}/doc/latex/fontawesomescaled/

%files -n texlive-fontmfizz
%license mit.txt
%{_texmf_main}/fonts/truetype/public/fontmfizz/
%{_texmf_main}/tex/latex/fontmfizz/
%doc %{_texmf_main}/doc/fonts/fontmfizz/

%files -n texlive-fonts-churchslavonic
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/fonts-churchslavonic/
%doc %{_texmf_main}/doc/fonts/fonts-churchslavonic/
%{_datadir}/fonts/fonts-churchslavonic
%{_datadir}/appdata/fonts-churchslavonic.metainfo.xml

%files -n texlive-fontscripts
%license lppl1.3c.txt
%{_texmf_main}/scripts/fontscripts/
%{_texmf_main}/tex/fontinst/fontscripts/
%{_texmf_main}/tex/latex/fontscripts/
%doc %{_texmf_main}/doc/latex/fontscripts/

%files -n texlive-forum
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/forum/
%{_texmf_main}/fonts/map/dvips/forum/
%{_texmf_main}/fonts/opentype/public/forum/
%{_texmf_main}/fonts/tfm/public/forum/
%{_texmf_main}/fonts/type1/public/forum/
%{_texmf_main}/fonts/vf/public/forum/
%{_texmf_main}/tex/latex/forum/
%doc %{_texmf_main}/doc/fonts/forum/
%{_datadir}/fonts/forum
%{_datadir}/appdata/forum.metainfo.xml

%files -n texlive-fourier
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/fourier/
%{_texmf_main}/fonts/map/dvips/fourier/
%{_texmf_main}/fonts/opentype/public/fourier/
%{_texmf_main}/fonts/tfm/public/fourier/
%{_texmf_main}/fonts/type1/public/fourier/
%{_texmf_main}/fonts/vf/public/fourier/
%{_texmf_main}/tex/latex/fourier/
%doc %{_texmf_main}/doc/fonts/fourier/
%{_datadir}/fonts/fourier
%{_datadir}/appdata/fourier.metainfo.xml

%files -n texlive-fouriernc
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/fouriernc/
%{_texmf_main}/fonts/tfm/public/fouriernc/
%{_texmf_main}/fonts/vf/public/fouriernc/
%{_texmf_main}/tex/latex/fouriernc/
%doc %{_texmf_main}/doc/fonts/fouriernc/

%files -n texlive-frcursive
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/frcursive/
%{_texmf_main}/fonts/source/public/frcursive/
%{_texmf_main}/fonts/tfm/public/frcursive/
%{_texmf_main}/fonts/type1/public/frcursive/
%{_texmf_main}/tex/latex/frcursive/
%doc %{_texmf_main}/doc/fonts/frcursive/

%files -n texlive-frederika2016
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/frederika2016/
%doc %{_texmf_main}/doc/fonts/frederika2016/
%{_datadir}/fonts/frederika2016
%{_datadir}/appdata/frederika2016.metainfo.xml

%files -n texlive-frimurer
%license gpl3.txt
%{_texmf_main}/fonts/afm/public/frimurer/
%{_texmf_main}/fonts/enc/dvips/frimurer/
%{_texmf_main}/fonts/tfm/public/frimurer/
%{_texmf_main}/fonts/type1/public/frimurer/
%{_texmf_main}/tex/latex/frimurer/
%doc %{_texmf_main}/doc/fonts/frimurer/

%files -n texlive-garamond-libre
%license mit.txt
%{_texmf_main}/fonts/enc/dvips/garamond-libre/
%{_texmf_main}/fonts/map/dvips/garamond-libre/
%{_texmf_main}/fonts/opentype/public/garamond-libre/
%{_texmf_main}/fonts/tfm/public/garamond-libre/
%{_texmf_main}/fonts/type1/public/garamond-libre/
%{_texmf_main}/fonts/vf/public/garamond-libre/
%{_texmf_main}/tex/latex/garamond-libre/
%doc %{_texmf_main}/doc/fonts/garamond-libre/
%{_datadir}/fonts/garamond-libre
%{_datadir}/appdata/garamond-libre.metainfo.xml

%files -n texlive-garamond-math
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/garamond-math/
%doc %{_texmf_main}/doc/fonts/garamond-math/
%{_datadir}/fonts/garamond-math
%{_datadir}/appdata/garamond-math.metainfo.xml

%files -n texlive-gelasio
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/gelasio/
%{_texmf_main}/fonts/map/dvips/gelasio/
%{_texmf_main}/fonts/opentype/sorkin/gelasio/
%{_texmf_main}/fonts/tfm/sorkin/gelasio/
%{_texmf_main}/fonts/type1/sorkin/gelasio/
%{_texmf_main}/fonts/vf/sorkin/gelasio/
%{_texmf_main}/tex/latex/gelasio/
%doc %{_texmf_main}/doc/fonts/gelasio/

%files -n texlive-gelasiomath
%license ofl.txt
%{_texmf_main}/fonts/map/dvips/gelasiomath/
%{_texmf_main}/fonts/tfm/public/gelasiomath/
%{_texmf_main}/fonts/type1/public/gelasiomath/
%{_texmf_main}/fonts/vf/public/gelasiomath/
%{_texmf_main}/tex/latex/gelasiomath/
%doc %{_texmf_main}/doc/fonts/gelasiomath/

%files -n texlive-genealogy
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/genealogy/
%{_texmf_main}/fonts/tfm/public/genealogy/
%doc %{_texmf_main}/doc/fonts/genealogy/

%files -n texlive-gentium-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gentium-otf/
%doc %{_texmf_main}/doc/fonts/gentium-otf/

%files -n texlive-gentium-sil
%license ofl.txt
%{_texmf_main}/fonts/opentype/SIL/gentium-sil/
%{_texmf_main}/fonts/truetype/SIL/gentium-sil/
%doc %{_texmf_main}/doc/fonts/gentium-sil/

%files -n texlive-gfsartemisia
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/gfsartemisia/
%{_texmf_main}/fonts/enc/dvips/gfsartemisia/
%{_texmf_main}/fonts/map/dvips/gfsartemisia/
%{_texmf_main}/fonts/opentype/public/gfsartemisia/
%{_texmf_main}/fonts/tfm/public/gfsartemisia/
%{_texmf_main}/fonts/type1/public/gfsartemisia/
%{_texmf_main}/fonts/vf/public/gfsartemisia/
%{_texmf_main}/tex/latex/gfsartemisia/
%doc %{_texmf_main}/doc/fonts/gfsartemisia/

%files -n texlive-gfsbodoni
%license ofl.txt
%{_texmf_main}/fonts/afm/public/gfsbodoni/
%{_texmf_main}/fonts/enc/dvips/gfsbodoni/
%{_texmf_main}/fonts/map/dvips/gfsbodoni/
%{_texmf_main}/fonts/opentype/public/gfsbodoni/
%{_texmf_main}/fonts/tfm/public/gfsbodoni/
%{_texmf_main}/fonts/type1/public/gfsbodoni/
%{_texmf_main}/fonts/vf/public/gfsbodoni/
%{_texmf_main}/tex/latex/gfsbodoni/
%doc %{_texmf_main}/doc/fonts/gfsbodoni/

%files -n texlive-gfscomplutum
%license ofl.txt
%{_texmf_main}/fonts/afm/public/gfscomplutum/
%{_texmf_main}/fonts/enc/dvips/gfscomplutum/
%{_texmf_main}/fonts/map/dvips/gfscomplutum/
%{_texmf_main}/fonts/opentype/public/gfscomplutum/
%{_texmf_main}/fonts/tfm/public/gfscomplutum/
%{_texmf_main}/fonts/type1/public/gfscomplutum/
%{_texmf_main}/fonts/vf/public/gfscomplutum/
%{_texmf_main}/tex/latex/gfscomplutum/
%doc %{_texmf_main}/doc/fonts/gfscomplutum/

%files -n texlive-gfsdidot
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/gfsdidot/
%{_texmf_main}/fonts/enc/dvips/gfsdidot/
%{_texmf_main}/fonts/map/dvips/gfsdidot/
%{_texmf_main}/fonts/opentype/public/gfsdidot/
%{_texmf_main}/fonts/tfm/public/gfsdidot/
%{_texmf_main}/fonts/type1/public/gfsdidot/
%{_texmf_main}/fonts/vf/public/gfsdidot/
%{_texmf_main}/tex/latex/gfsdidot/
%doc %{_texmf_main}/doc/fonts/gfsdidot/

%files -n texlive-gfsdidotclassic
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/gfsdidotclassic/
%doc %{_texmf_main}/doc/fonts/gfsdidotclassic/

%files -n texlive-gfsneohellenic
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/gfsneohellenic/
%{_texmf_main}/fonts/enc/dvips/gfsneohellenic/
%{_texmf_main}/fonts/map/dvips/gfsneohellenic/
%{_texmf_main}/fonts/opentype/public/gfsneohellenic/
%{_texmf_main}/fonts/tfm/public/gfsneohellenic/
%{_texmf_main}/fonts/type1/public/gfsneohellenic/
%{_texmf_main}/fonts/vf/public/gfsneohellenic/
%{_texmf_main}/tex/latex/gfsneohellenic/
%doc %{_texmf_main}/doc/fonts/gfsneohellenic/

%files -n texlive-gfsneohellenicmath
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/gfsneohellenicmath/
%{_texmf_main}/tex/latex/gfsneohellenicmath/
%doc %{_texmf_main}/doc/fonts/gfsneohellenicmath/

%files -n texlive-gfssolomos
%license ofl.txt
%{_texmf_main}/fonts/afm/public/gfssolomos/
%{_texmf_main}/fonts/enc/dvips/gfssolomos/
%{_texmf_main}/fonts/map/dvips/gfssolomos/
%{_texmf_main}/fonts/opentype/public/gfssolomos/
%{_texmf_main}/fonts/tfm/public/gfssolomos/
%{_texmf_main}/fonts/type1/public/gfssolomos/
%{_texmf_main}/fonts/vf/public/gfssolomos/
%{_texmf_main}/tex/latex/gfssolomos/
%doc %{_texmf_main}/doc/fonts/gfssolomos/

%files -n texlive-gillcm
%license bsd.txt
%{_texmf_main}/fonts/map/dvips/gillcm/
%{_texmf_main}/fonts/tfm/public/gillcm/
%{_texmf_main}/fonts/vf/public/gillcm/
%{_texmf_main}/tex/latex/gillcm/
%doc %{_texmf_main}/doc/latex/gillcm/

%files -n texlive-gillius
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/gillius/
%{_texmf_main}/fonts/map/dvips/gillius/
%{_texmf_main}/fonts/opentype/arkandis/gillius/
%{_texmf_main}/fonts/tfm/arkandis/gillius/
%{_texmf_main}/fonts/type1/arkandis/gillius/
%{_texmf_main}/fonts/vf/arkandis/gillius/
%{_texmf_main}/tex/latex/gillius/
%doc %{_texmf_main}/doc/fonts/gillius/

%files -n texlive-gnu-freefont
%license gpl3.txt
%{_texmf_main}/fonts/opentype/public/gnu-freefont/
%{_texmf_main}/fonts/truetype/public/gnu-freefont/
%doc %{_texmf_main}/doc/fonts/gnu-freefont/
%{_datadir}/fonts/gnu-freefont
%{_datadir}/appdata/gnu-freefont.metainfo.xml

%files -n texlive-gofonts
%license bsd.txt
%{_texmf_main}/fonts/enc/dvips/gofonts/
%{_texmf_main}/fonts/map/dvips/gofonts/
%{_texmf_main}/fonts/tfm/bh/gofonts/
%{_texmf_main}/fonts/truetype/bh/gofonts/
%{_texmf_main}/fonts/type1/bh/gofonts/
%{_texmf_main}/fonts/vf/bh/gofonts/
%{_texmf_main}/tex/latex/gofonts/
%doc %{_texmf_main}/doc/fonts/gofonts/

%files -n texlive-gothic
%license pd.txt
%{_texmf_main}/fonts/source/public/gothic/
%{_texmf_main}/fonts/tfm/public/gothic/
%doc %{_texmf_main}/doc/fonts/gothic/

%files -n texlive-greenpoint
%license gpl2.txt
%{_texmf_main}/fonts/source/public/greenpoint/
%{_texmf_main}/fonts/tfm/public/greenpoint/
%doc %{_texmf_main}/doc/fonts/greenpoint/

%files -n texlive-grotesq
%license gpl2.txt
%{_texmf_main}/fonts/afm/urw/grotesq/
%{_texmf_main}/fonts/map/dvips/grotesq/
%{_texmf_main}/fonts/tfm/urw/grotesq/
%{_texmf_main}/fonts/type1/urw/grotesq/
%{_texmf_main}/fonts/vf/urw/grotesq/
%{_texmf_main}/tex/latex/grotesq/
%doc %{_texmf_main}/doc/fonts/grotesq/

%files -n texlive-gudea
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/gudea/
%{_texmf_main}/fonts/map/dvips/gudea/
%{_texmf_main}/fonts/tfm/public/gudea/
%{_texmf_main}/fonts/type1/public/gudea/
%{_texmf_main}/fonts/vf/public/gudea/
%{_texmf_main}/tex/latex/gudea/
%doc %{_texmf_main}/doc/fonts/gudea/

%files -n texlive-hacm
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/hacm/
%{_texmf_main}/fonts/tfm/public/hacm/
%{_texmf_main}/fonts/type1/public/hacm/
%{_texmf_main}/fonts/vf/public/hacm/
%{_texmf_main}/tex/latex/hacm/
%doc %{_texmf_main}/doc/fonts/hacm/

%files -n texlive-hamnosys
%license lppl1.3c.txt
%{_texmf_main}/fonts/truetype/public/hamnosys/
%{_texmf_main}/tex/latex/hamnosys/
%doc %{_texmf_main}/doc/fonts/hamnosys/

%files -n texlive-hands
%license pd.txt
%{_texmf_main}/fonts/source/public/hands/
%{_texmf_main}/fonts/tfm/public/hands/

%files -n texlive-hep-font
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hep-font/
%doc %{_texmf_main}/doc/fonts/hep-font/

%files -n texlive-hep-math-font
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hep-math-font/
%doc %{_texmf_main}/doc/fonts/hep-math-font/

%files -n texlive-heros-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/heros-otf/
%doc %{_texmf_main}/doc/fonts/heros-otf/

%files -n texlive-heuristica
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/heuristica/
%{_texmf_main}/fonts/map/dvips/heuristica/
%{_texmf_main}/fonts/opentype/public/heuristica/
%{_texmf_main}/fonts/tfm/public/heuristica/
%{_texmf_main}/fonts/type1/public/heuristica/
%{_texmf_main}/fonts/vf/public/heuristica/
%{_texmf_main}/tex/latex/heuristica/
%doc %{_texmf_main}/doc/fonts/heuristica/

%files -n texlive-hfbright
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/hfbright/
%{_texmf_main}/fonts/enc/dvips/hfbright/
%{_texmf_main}/fonts/map/dvips/hfbright/
%{_texmf_main}/fonts/type1/public/hfbright/
%doc %{_texmf_main}/doc/fonts/hfbright/

%files -n texlive-hfoldsty
%license gpl2.txt
%{_texmf_main}/fonts/tfm/public/hfoldsty/
%{_texmf_main}/fonts/vf/public/hfoldsty/
%{_texmf_main}/tex/latex/hfoldsty/
%doc %{_texmf_main}/doc/fonts/hfoldsty/

%files -n texlive-hindmadurai
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/hindmadurai/
%{_texmf_main}/fonts/map/dvips/hindmadurai/
%{_texmf_main}/fonts/opentype/public/hindmadurai/
%{_texmf_main}/fonts/tfm/public/hindmadurai/
%{_texmf_main}/fonts/type1/public/hindmadurai/
%{_texmf_main}/fonts/vf/public/hindmadurai/
%{_texmf_main}/tex/latex/hindmadurai/
%doc %{_texmf_main}/doc/fonts/hindmadurai/

%files -n texlive-ibarra
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/ibarra/
%{_texmf_main}/fonts/map/dvips/ibarra/
%{_texmf_main}/fonts/tfm/public/ibarra/
%{_texmf_main}/fonts/truetype/public/ibarra/
%{_texmf_main}/fonts/type1/public/ibarra/
%{_texmf_main}/fonts/vf/public/ibarra/
%{_texmf_main}/tex/latex/ibarra/
%doc %{_texmf_main}/doc/fonts/ibarra/
%{_datadir}/appdata/ibarra.metainfo.xml

%files -n texlive-ifsym
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/ifsym/
%{_texmf_main}/fonts/tfm/public/ifsym/
%{_texmf_main}/tex/latex/ifsym/
%doc %{_texmf_main}/doc/fonts/ifsym/

%files -n texlive-imfellenglish
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/imfellenglish/
%{_texmf_main}/fonts/map/dvips/imfellenglish/
%{_texmf_main}/fonts/opentype/iginomarini/imfellenglish/
%{_texmf_main}/fonts/tfm/iginomarini/imfellenglish/
%{_texmf_main}/fonts/type1/iginomarini/imfellenglish/
%{_texmf_main}/fonts/vf/iginomarini/imfellenglish/
%{_texmf_main}/tex/latex/imfellenglish/
%doc %{_texmf_main}/doc/fonts/imfellenglish/
%{_datadir}/fonts/imfellenglish
%{_datadir}/appdata/imfellenglish.metainfo.xml

%files -n texlive-inconsolata
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/inconsolata/
%{_texmf_main}/fonts/map/dvips/inconsolata/
%{_texmf_main}/fonts/opentype/public/inconsolata/
%{_texmf_main}/fonts/tfm/public/inconsolata/
%{_texmf_main}/fonts/type1/public/inconsolata/
%{_texmf_main}/tex/latex/inconsolata/
%doc %{_texmf_main}/doc/fonts/inconsolata/

%files -n texlive-inconsolata-nerd-font
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/inconsolata-nerd-font/
%{_texmf_main}/tex/latex/inconsolata-nerd-font/
%doc %{_texmf_main}/doc/fonts/inconsolata-nerd-font/

%files -n texlive-initials
%license lppl1.3c.txt
%{_texmf_main}/dvips/initials/
%{_texmf_main}/fonts/afm/public/initials/
%{_texmf_main}/fonts/map/dvips/initials/
%{_texmf_main}/fonts/tfm/public/initials/
%{_texmf_main}/fonts/type1/public/initials/
%{_texmf_main}/tex/latex/initials/
%doc %{_texmf_main}/doc/fonts/initials/

%files -n texlive-inriafonts
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/inriafonts/
%{_texmf_main}/fonts/map/dvips/inriafonts/
%{_texmf_main}/fonts/opentype/public/inriafonts/
%{_texmf_main}/fonts/tfm/public/inriafonts/
%{_texmf_main}/fonts/truetype/public/inriafonts/
%{_texmf_main}/fonts/type1/public/inriafonts/
%{_texmf_main}/fonts/vf/public/inriafonts/
%{_texmf_main}/tex/latex/inriafonts/
%doc %{_texmf_main}/doc/fonts/inriafonts/
%{_datadir}/fonts/inriafonts
%{_datadir}/appdata/inriafonts.metainfo.xml

%files -n texlive-inter
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/inter/
%{_texmf_main}/fonts/map/dvips/inter/
%{_texmf_main}/fonts/opentype/public/inter/
%{_texmf_main}/fonts/tfm/public/inter/
%{_texmf_main}/fonts/type1/public/inter/
%{_texmf_main}/fonts/vf/public/inter/
%{_texmf_main}/tex/latex/inter/
%doc %{_texmf_main}/doc/fonts/inter/

%files -n texlive-ipaex-type1
%license other-free.txt
%{_texmf_main}/fonts/enc/dvips/ipaex-type1/
%{_texmf_main}/fonts/map/dvips/ipaex-type1/
%{_texmf_main}/fonts/tfm/public/ipaex-type1/
%{_texmf_main}/fonts/type1/public/ipaex-type1/
%{_texmf_main}/tex/latex/ipaex-type1/
%doc %{_texmf_main}/doc/fonts/ipaex-type1/

%files -n texlive-iwona
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/nowacki/iwona/
%{_texmf_main}/fonts/enc/dvips/iwona/
%{_texmf_main}/fonts/map/dvips/iwona/
%{_texmf_main}/fonts/opentype/nowacki/iwona/
%{_texmf_main}/fonts/tfm/nowacki/iwona/
%{_texmf_main}/fonts/type1/nowacki/iwona/
%{_texmf_main}/tex/latex/iwona/
%{_texmf_main}/tex/plain/iwona/
%doc %{_texmf_main}/doc/fonts/iwona/
%{_datadir}/fonts/iwona
%{_datadir}/appdata/iwona.metainfo.xml

%files -n texlive-jablantile
%license pd.txt
%{_texmf_main}/fonts/source/public/jablantile/
%doc %{_texmf_main}/doc/fonts/jablantile/

%files -n texlive-jamtimes
%license bsd.txt
%{_texmf_main}/fonts/map/dvips/jamtimes/
%{_texmf_main}/fonts/tfm/public/jamtimes/
%{_texmf_main}/fonts/vf/public/jamtimes/
%{_texmf_main}/tex/latex/jamtimes/
%doc %{_texmf_main}/doc/latex/jamtimes/

%files -n texlive-jetbrainsmono-otf
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/SIL/jetbrainsmono-otf/
%{_texmf_main}/tex/latex/jetbrainsmono-otf/
%doc %{_texmf_main}/doc/fonts/jetbrainsmono-otf/

%files -n texlive-josefin
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/josefin/
%{_texmf_main}/fonts/map/dvips/josefin/
%{_texmf_main}/fonts/tfm/public/josefin/
%{_texmf_main}/fonts/truetype/public/josefin/
%{_texmf_main}/fonts/type1/public/josefin/
%{_texmf_main}/fonts/vf/public/josefin/
%{_texmf_main}/tex/latex/josefin/
%doc %{_texmf_main}/doc/fonts/josefin/

%files -n texlive-juliamono
%license lppl1.3c.txt
%{_texmf_main}/fonts/truetype/public/juliamono/
%{_texmf_main}/tex/latex/juliamono/
%doc %{_texmf_main}/doc/fonts/juliamono/

%files -n texlive-junicode
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/junicode/
%{_texmf_main}/fonts/map/dvips/junicode/
%{_texmf_main}/fonts/opentype/public/junicode/
%{_texmf_main}/fonts/tfm/public/junicode/
%{_texmf_main}/fonts/type1/public/junicode/
%{_texmf_main}/fonts/vf/public/junicode/
%{_texmf_main}/tex/latex/junicode/
%doc %{_texmf_main}/doc/fonts/junicode/

%files -n texlive-junicodevf
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/junicodevf/
%{_texmf_main}/tex/lualatex/junicodevf/
%doc %{_texmf_main}/doc/fonts/junicodevf/

%files -n texlive-kixfont
%{_texmf_main}/fonts/source/public/kixfont/
%{_texmf_main}/fonts/tfm/public/kixfont/
%doc %{_texmf_main}/doc/fonts/kixfont/

%files -n texlive-kpfonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/kpfonts/
%{_texmf_main}/fonts/enc/dvips/kpfonts/
%{_texmf_main}/fonts/map/dvips/kpfonts/
%{_texmf_main}/fonts/tfm/public/kpfonts/
%{_texmf_main}/fonts/type1/public/kpfonts/
%{_texmf_main}/fonts/vf/public/kpfonts/
%{_texmf_main}/tex/latex/kpfonts/
%doc %{_texmf_main}/doc/fonts/kpfonts/

%files -n texlive-kpfonts-otf
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/kpfonts-otf/
%{_texmf_main}/tex/latex/kpfonts-otf/
%doc %{_texmf_main}/doc/fonts/kpfonts-otf/

%files -n texlive-kurier
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/nowacki/kurier/
%{_texmf_main}/fonts/enc/dvips/kurier/
%{_texmf_main}/fonts/map/dvips/kurier/
%{_texmf_main}/fonts/opentype/nowacki/kurier/
%{_texmf_main}/fonts/tfm/nowacki/kurier/
%{_texmf_main}/fonts/type1/nowacki/kurier/
%{_texmf_main}/tex/latex/kurier/
%{_texmf_main}/tex/plain/kurier/
%doc %{_texmf_main}/doc/fonts/kurier/
%{_datadir}/fonts/kurier
%{_datadir}/appdata/kurier.metainfo.xml

%files -n texlive-lato
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/lato/
%{_texmf_main}/fonts/map/dvips/lato/
%{_texmf_main}/fonts/tfm/typoland/lato/
%{_texmf_main}/fonts/truetype/typoland/lato/
%{_texmf_main}/fonts/type1/typoland/lato/
%{_texmf_main}/fonts/vf/typoland/lato/
%{_texmf_main}/tex/latex/lato/
%doc %{_texmf_main}/doc/fonts/lato/

%files -n texlive-lete-sans-math
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/lete-sans-math/
%{_texmf_main}/tex/latex/lete-sans-math/
%doc %{_texmf_main}/doc/fonts/lete-sans-math/

%files -n texlive-lexend
%license lppl1.3c.txt
%{_texmf_main}/fonts/truetype/public/lexend/
%{_texmf_main}/tex/latex/lexend/
%doc %{_texmf_main}/doc/fonts/lexend/

%files -n texlive-lfb
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/lfb/
%{_texmf_main}/fonts/tfm/public/lfb/
%doc %{_texmf_main}/doc/fonts/lfb/

%files -n texlive-libertine
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/libertine/
%{_texmf_main}/fonts/map/dvips/libertine/
%{_texmf_main}/fonts/opentype/public/libertine/
%{_texmf_main}/fonts/tfm/public/libertine/
%{_texmf_main}/fonts/type1/public/libertine/
%{_texmf_main}/fonts/vf/public/libertine/
%{_texmf_main}/tex/latex/libertine/
%doc %{_texmf_main}/doc/fonts/libertine/

%files -n texlive-libertinegc
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/libertinegc/
%{_texmf_main}/fonts/map/dvips/libertinegc/
%{_texmf_main}/fonts/tfm/public/libertinegc/
%{_texmf_main}/tex/latex/libertinegc/
%doc %{_texmf_main}/doc/fonts/libertinegc/

%files -n texlive-libertinus
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/libertinus/
%doc %{_texmf_main}/doc/fonts/libertinus/

%files -n texlive-libertinus-fonts
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/libertinus-fonts/
%doc %{_texmf_main}/doc/fonts/libertinus-fonts/
%{_datadir}/fonts/libertinus-fonts
%{_datadir}/appdata/libertinus-fonts.metainfo.xml

%files -n texlive-libertinus-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/libertinus-otf/
%doc %{_texmf_main}/doc/fonts/libertinus-otf/

%files -n texlive-libertinus-type1
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/libertinus-type1/
%{_texmf_main}/fonts/map/dvips/libertinus-type1/
%{_texmf_main}/fonts/tfm/public/libertinus-type1/
%{_texmf_main}/fonts/type1/public/libertinus-type1/
%{_texmf_main}/fonts/vf/public/libertinus-type1/
%{_texmf_main}/tex/latex/libertinus-type1/
%doc %{_texmf_main}/doc/fonts/libertinus-type1/

%files -n texlive-libertinust1math
%license ofl.txt
%{_texmf_main}/fonts/afm/public/libertinust1math/
%{_texmf_main}/fonts/enc/dvips/libertinust1math/
%{_texmf_main}/fonts/map/dvips/libertinust1math/
%{_texmf_main}/fonts/tfm/public/libertinust1math/
%{_texmf_main}/fonts/type1/public/libertinust1math/
%{_texmf_main}/fonts/vf/public/libertinust1math/
%{_texmf_main}/tex/latex/libertinust1math/
%doc %{_texmf_main}/doc/fonts/libertinust1math/

%files -n texlive-librebaskerville
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/librebaskerville/
%{_texmf_main}/fonts/map/dvips/librebaskerville/
%{_texmf_main}/fonts/tfm/impallari/librebaskerville/
%{_texmf_main}/fonts/truetype/impallari/librebaskerville/
%{_texmf_main}/fonts/type1/impallari/librebaskerville/
%{_texmf_main}/fonts/vf/impallari/librebaskerville/
%{_texmf_main}/tex/latex/librebaskerville/
%doc %{_texmf_main}/doc/fonts/librebaskerville/

%files -n texlive-librebodoni
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/librebodoni/
%{_texmf_main}/fonts/map/dvips/librebodoni/
%{_texmf_main}/fonts/opentype/impallari/librebodoni/
%{_texmf_main}/fonts/tfm/impallari/librebodoni/
%{_texmf_main}/fonts/type1/impallari/librebodoni/
%{_texmf_main}/fonts/vf/impallari/librebodoni/
%{_texmf_main}/tex/latex/librebodoni/
%doc %{_texmf_main}/doc/fonts/librebodoni/
%{_datadir}/fonts/librebodoni
%{_datadir}/appdata/librebodoni.metainfo.xml

%files -n texlive-librecaslon
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/librecaslon/
%{_texmf_main}/fonts/map/dvips/librecaslon/
%{_texmf_main}/fonts/opentype/impallari/librecaslon/
%{_texmf_main}/fonts/tfm/impallari/librecaslon/
%{_texmf_main}/fonts/type1/impallari/librecaslon/
%{_texmf_main}/fonts/vf/impallari/librecaslon/
%{_texmf_main}/tex/latex/librecaslon/
%doc %{_texmf_main}/doc/fonts/librecaslon/
%{_datadir}/fonts/librecaslon
%{_datadir}/appdata/librecaslon.metainfo.xml

%files -n texlive-librefranklin
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/librefranklin/
%{_texmf_main}/fonts/map/dvips/librefranklin/
%{_texmf_main}/fonts/opentype/impallari/librefranklin/
%{_texmf_main}/fonts/tfm/impallari/librefranklin/
%{_texmf_main}/fonts/type1/impallari/librefranklin/
%{_texmf_main}/fonts/vf/impallari/librefranklin/
%{_texmf_main}/tex/latex/librefranklin/
%doc %{_texmf_main}/doc/fonts/librefranklin/
%{_datadir}/fonts/librefranklin
%{_datadir}/appdata/librefranklin.metainfo.xml

%files -n texlive-libris
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/libris/
%{_texmf_main}/fonts/enc/dvips/libris/
%{_texmf_main}/fonts/map/dvips/libris/
%{_texmf_main}/fonts/tfm/public/libris/
%{_texmf_main}/fonts/type1/public/libris/
%{_texmf_main}/fonts/vf/public/libris/
%{_texmf_main}/tex/latex/libris/
%doc %{_texmf_main}/doc/fonts/libris/

%files -n texlive-lineara
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/lineara/
%{_texmf_main}/fonts/map/dvips/lineara/
%{_texmf_main}/fonts/tfm/public/lineara/
%{_texmf_main}/fonts/type1/public/lineara/
%{_texmf_main}/tex/latex/lineara/
%doc %{_texmf_main}/doc/fonts/lineara/

%files -n texlive-linguisticspro
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/linguisticspro/
%{_texmf_main}/fonts/map/dvips/linguisticspro/
%{_texmf_main}/fonts/opentype/public/linguisticspro/
%{_texmf_main}/fonts/tfm/public/linguisticspro/
%{_texmf_main}/fonts/type1/public/linguisticspro/
%{_texmf_main}/fonts/vf/public/linguisticspro/
%{_texmf_main}/tex/latex/linguisticspro/
%doc %{_texmf_main}/doc/fonts/linguisticspro/
%{_datadir}/fonts/linguisticspro
%{_datadir}/appdata/linguisticspro.metainfo.xml

%files -n texlive-lobster2
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/lobster2/
%{_texmf_main}/fonts/map/dvips/lobster2/
%{_texmf_main}/fonts/opentype/impallari/lobster2/
%{_texmf_main}/fonts/tfm/impallari/lobster2/
%{_texmf_main}/fonts/type1/impallari/lobster2/
%{_texmf_main}/fonts/vf/impallari/lobster2/
%{_texmf_main}/tex/latex/lobster2/
%doc %{_texmf_main}/doc/fonts/lobster2/
%{_datadir}/fonts/lobster2
%{_datadir}/appdata/lobster2.metainfo.xml

%files -n texlive-logix
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/logix/
%{_texmf_main}/fonts/truetype/public/logix/
%{_texmf_main}/tex/latex/logix/
%doc %{_texmf_main}/doc/fonts/logix/
%{_datadir}/fonts/logix
%{_datadir}/appdata/logix.metainfo.xml

%files -n texlive-luciole
%license cc-by-4.txt
%{_texmf_main}/fonts/opentype/public/luciole/
%{_texmf_main}/fonts/truetype/public/luciole/
%{_texmf_main}/tex/latex/luciole/
%doc %{_texmf_main}/doc/fonts/luciole/

%files -n texlive-luwiantype
%license lppl1.3c.txt
%{_texmf_main}/fonts/truetype/public/luwiantype/
%{_texmf_main}/tex/latex/luwiantype/
%doc %{_texmf_main}/doc/fonts/luwiantype/

%files -n texlive-lxfonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/lxfonts/
%{_texmf_main}/fonts/source/public/lxfonts/
%{_texmf_main}/fonts/tfm/public/lxfonts/
%{_texmf_main}/fonts/type1/public/lxfonts/
%{_texmf_main}/tex/latex/lxfonts/
%doc %{_texmf_main}/doc/fonts/lxfonts/

%files -n texlive-ly1
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/ly1/
%{_texmf_main}/fonts/map/dvips/ly1/
%{_texmf_main}/fonts/tfm/adobe/ly1/
%{_texmf_main}/fonts/vf/adobe/ly1/
%{_texmf_main}/tex/latex/ly1/
%{_texmf_main}/tex/plain/ly1/
%doc %{_texmf_main}/doc/latex/ly1/

%files -n texlive-lydtype
%license lppl1.3c.txt
%{_texmf_main}/fonts/truetype/public/lydtype/
%{_texmf_main}/tex/latex/lydtype/
%doc %{_texmf_main}/doc/fonts/lydtype/

%files -n texlive-magra
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/magra/
%{_texmf_main}/fonts/map/dvips/magra/
%{_texmf_main}/fonts/tfm/public/magra/
%{_texmf_main}/fonts/type1/public/magra/
%{_texmf_main}/fonts/vf/public/magra/
%{_texmf_main}/tex/latex/magra/
%doc %{_texmf_main}/doc/fonts/magra/

%files -n texlive-marcellus
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/marcellus/
%{_texmf_main}/fonts/map/dvips/marcellus/
%{_texmf_main}/fonts/tfm/public/marcellus/
%{_texmf_main}/fonts/truetype/public/marcellus/
%{_texmf_main}/fonts/type1/public/marcellus/
%{_texmf_main}/fonts/vf/public/marcellus/
%{_texmf_main}/tex/latex/marcellus/
%doc %{_texmf_main}/doc/fonts/marcellus/

%files -n texlive-mathabx
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/mathabx/
%{_texmf_main}/fonts/tfm/public/mathabx/
%{_texmf_main}/tex/generic/mathabx/
%doc %{_texmf_main}/doc/fonts/mathabx/

%files -n texlive-mathabx-type1
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/mathabx-type1/
%{_texmf_main}/fonts/type1/public/mathabx-type1/
%doc %{_texmf_main}/doc/fonts/mathabx-type1/

%files -n texlive-mathdesign
%license gpl2.txt
%{_texmf_main}/dvips/mathdesign/
%{_texmf_main}/fonts/enc/dvips/mathdesign/
%{_texmf_main}/fonts/map/dvips/mathdesign/
%{_texmf_main}/fonts/tfm/public/mathdesign/
%{_texmf_main}/fonts/type1/public/mathdesign/
%{_texmf_main}/fonts/vf/public/mathdesign/
%{_texmf_main}/tex/latex/mathdesign/
%doc %{_texmf_main}/doc/fonts/mathdesign/

%files -n texlive-mdputu
%license bsd.txt
%{_texmf_main}/fonts/tfm/public/mdputu/
%{_texmf_main}/fonts/vf/public/mdputu/
%{_texmf_main}/tex/latex/mdputu/
%doc %{_texmf_main}/doc/latex/mdputu/

%files -n texlive-mdsymbol
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/mdsymbol/
%{_texmf_main}/fonts/map/dvips/mdsymbol/
%{_texmf_main}/fonts/opentype/public/mdsymbol/
%{_texmf_main}/fonts/source/public/mdsymbol/
%{_texmf_main}/fonts/tfm/public/mdsymbol/
%{_texmf_main}/fonts/type1/public/mdsymbol/
%{_texmf_main}/tex/latex/mdsymbol/
%doc %{_texmf_main}/doc/fonts/mdsymbol/
%doc %{_texmf_main}/doc/latex/mdsymbol/
%{_datadir}/fonts/mdsymbol
%{_datadir}/appdata/mdsymbol.metainfo.xml

%files -n texlive-merriweather
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/merriweather/
%{_texmf_main}/fonts/map/dvips/merriweather/
%{_texmf_main}/fonts/opentype/sorkin/merriweather/
%{_texmf_main}/fonts/tfm/sorkin/merriweather/
%{_texmf_main}/fonts/type1/sorkin/merriweather/
%{_texmf_main}/fonts/vf/sorkin/merriweather/
%{_texmf_main}/tex/latex/merriweather/
%doc %{_texmf_main}/doc/fonts/merriweather/

%files -n texlive-metsymb
%license bsd.txt
%{_texmf_main}/fonts/afm/public/metsymb/
%{_texmf_main}/fonts/enc/dvips/metsymb/
%{_texmf_main}/fonts/map/dvips/metsymb/
%{_texmf_main}/fonts/opentype/public/metsymb/
%{_texmf_main}/fonts/tfm/public/metsymb/
%{_texmf_main}/fonts/type1/public/metsymb/
%{_texmf_main}/tex/latex/metsymb/
%doc %{_texmf_main}/doc/fonts/metsymb/

%files -n texlive-mfb-oldstyle
%license cc-zero-1.txt
%{_texmf_main}/fonts/enc/dvips/mfb-oldstyle/
%{_texmf_main}/fonts/map/dvips/mfb-oldstyle/
%{_texmf_main}/fonts/opentype/public/mfb-oldstyle/
%{_texmf_main}/fonts/tfm/public/mfb-oldstyle/
%{_texmf_main}/fonts/type1/public/mfb-oldstyle/
%{_texmf_main}/fonts/vf/public/mfb-oldstyle/
%{_texmf_main}/tex/latex/mfb-oldstyle/
%doc %{_texmf_main}/doc/fonts/mfb-oldstyle/

%files -n texlive-miama
%license ofl.txt
%{_texmf_main}/fonts/afm/public/miama/
%{_texmf_main}/fonts/enc/dvips/miama/
%{_texmf_main}/fonts/map/dvips/miama/
%{_texmf_main}/fonts/opentype/public/miama/
%{_texmf_main}/fonts/tfm/public/miama/
%{_texmf_main}/fonts/type1/public/miama/
%{_texmf_main}/tex/latex/miama/
%doc %{_texmf_main}/doc/fonts/miama/
%{_datadir}/fonts/miama
%{_datadir}/appdata/miama.metainfo.xml

%files -n texlive-mintspirit
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/mintspirit/
%{_texmf_main}/fonts/map/dvips/mintspirit/
%{_texmf_main}/fonts/opentype/arkandis/mintspirit/
%{_texmf_main}/fonts/tfm/arkandis/mintspirit/
%{_texmf_main}/fonts/type1/arkandis/mintspirit/
%{_texmf_main}/fonts/vf/arkandis/mintspirit/
%{_texmf_main}/tex/latex/mintspirit/
%doc %{_texmf_main}/doc/fonts/mintspirit/
%{_datadir}/fonts/mintspirit
%{_datadir}/appdata/mintspirit.metainfo.xml

%files -n texlive-missaali
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/missaali/
%{_texmf_main}/tex/latex/missaali/
%doc %{_texmf_main}/doc/fonts/missaali/
%{_datadir}/fonts/missaali
%{_datadir}/appdata/missaali.metainfo.xml

%files -n texlive-mlmodern
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/mlmodern/
%{_texmf_main}/fonts/tfm/public/mlmodern/
%{_texmf_main}/fonts/type1/public/mlmodern/
%{_texmf_main}/tex/latex/mlmodern/
%doc %{_texmf_main}/doc/fonts/mlmodern/

%files -n texlive-mnsymbol
%license pd.txt
%{_texmf_main}/fonts/enc/dvips/mnsymbol/
%{_texmf_main}/fonts/map/dvips/mnsymbol/
%{_texmf_main}/fonts/map/vtex/mnsymbol/
%{_texmf_main}/fonts/opentype/public/mnsymbol/
%{_texmf_main}/fonts/source/public/mnsymbol/
%{_texmf_main}/fonts/tfm/public/mnsymbol/
%{_texmf_main}/fonts/type1/public/mnsymbol/
%{_texmf_main}/tex/latex/mnsymbol/
%doc %{_texmf_main}/doc/latex/mnsymbol/
%{_datadir}/fonts/mnsymbol
%{_datadir}/appdata/mnsymbol.metainfo.xml

%files -n texlive-monaspace-otf
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/monaspace-otf/
%{_texmf_main}/tex/latex/monaspace-otf/
%doc %{_texmf_main}/doc/fonts/monaspace-otf/

%files -n texlive-montserrat
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/montserrat/
%{_texmf_main}/fonts/map/dvips/montserrat/
%{_texmf_main}/fonts/opentype/public/montserrat/
%{_texmf_main}/fonts/tfm/public/montserrat/
%{_texmf_main}/fonts/type1/public/montserrat/
%{_texmf_main}/fonts/vf/public/montserrat/
%{_texmf_main}/tex/latex/montserrat/
%doc %{_texmf_main}/doc/fonts/montserrat/

%files -n texlive-mpfonts
%license knuth.txt
%{_texmf_main}/fonts/map/dvips/mpfonts/
%{_texmf_main}/fonts/type3/mpfonts/
%doc %{_texmf_main}/doc/fonts/mpfonts/

%files -n texlive-mweights
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mweights/
%doc %{_texmf_main}/doc/latex/mweights/

%files -n texlive-newcomputermodern
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/newcomputermodern/
%{_texmf_main}/tex/latex/newcomputermodern/
%doc %{_texmf_main}/doc/fonts/newcomputermodern/
%{_datadir}/fonts/newcomputermodern
%{_datadir}/appdata/newcomputermodern.metainfo.xml

%files -n texlive-newpx
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/newpx/
%{_texmf_main}/fonts/enc/dvips/newpx/
%{_texmf_main}/fonts/map/dvips/newpx/
%{_texmf_main}/fonts/opentype/public/newpx/
%{_texmf_main}/fonts/tfm/public/newpx/
%{_texmf_main}/fonts/type1/public/newpx/
%{_texmf_main}/fonts/vf/public/newpx/
%{_texmf_main}/tex/latex/newpx/
%doc %{_texmf_main}/doc/fonts/newpx/
%{_datadir}/fonts/newpx
%{_datadir}/appdata/newpx.metainfo.xml

%files -n texlive-newtx
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/newtx/
%{_texmf_main}/fonts/enc/dvips/newtx/
%{_texmf_main}/fonts/map/dvips/newtx/
%{_texmf_main}/fonts/opentype/public/newtx/
%{_texmf_main}/fonts/tfm/public/newtx/
%{_texmf_main}/fonts/type1/public/newtx/
%{_texmf_main}/fonts/vf/public/newtx/
%{_texmf_main}/tex/latex/newtx/
%doc %{_texmf_main}/doc/fonts/newtx/
%{_datadir}/fonts/newtx
%{_datadir}/appdata/newtx.metainfo.xml

%files -n texlive-newtxsf
%license ofl.txt
%{_texmf_main}/fonts/map/dvips/newtxsf/
%{_texmf_main}/fonts/tfm/public/newtxsf/
%{_texmf_main}/fonts/type1/public/newtxsf/
%{_texmf_main}/fonts/vf/public/newtxsf/
%{_texmf_main}/tex/latex/newtxsf/
%doc %{_texmf_main}/doc/fonts/newtxsf/

%files -n texlive-newtxtt
%license gpl3.txt
%{_texmf_main}/fonts/enc/dvips/newtxtt/
%{_texmf_main}/fonts/map/dvips/newtxtt/
%{_texmf_main}/fonts/tfm/public/newtxtt/
%{_texmf_main}/fonts/type1/public/newtxtt/
%{_texmf_main}/tex/latex/newtxtt/
%doc %{_texmf_main}/doc/fonts/newtxtt/

%files -n texlive-niceframe-type1
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/niceframe-type1/
%{_texmf_main}/fonts/map/dvips/niceframe-type1/
%{_texmf_main}/fonts/type1/public/niceframe-type1/
%doc %{_texmf_main}/doc/fonts/niceframe-type1/

%files -n texlive-nimbus15
%license other-free.txt
%{_texmf_main}/fonts/afm/public/nimbus15/
%{_texmf_main}/fonts/enc/dvips/nimbus15/
%{_texmf_main}/fonts/map/dvips/nimbus15/
%{_texmf_main}/fonts/opentype/public/nimbus15/
%{_texmf_main}/fonts/tfm/public/nimbus15/
%{_texmf_main}/fonts/type1/public/nimbus15/
%{_texmf_main}/fonts/vf/public/nimbus15/
%{_texmf_main}/tex/latex/nimbus15/
%doc %{_texmf_main}/doc/fonts/nimbus15/
%{_datadir}/fonts/nimbus15
%{_datadir}/appdata/nimbus15.metainfo.xml

%files -n texlive-nkarta
%license pd.txt
%{_texmf_main}/fonts/source/public/nkarta/
%{_texmf_main}/fonts/tfm/public/nkarta/
%{_texmf_main}/metapost/nkarta/
%doc %{_texmf_main}/doc/fonts/nkarta/

%files -n texlive-noto
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/noto/
%{_texmf_main}/fonts/map/dvips/noto/
%{_texmf_main}/fonts/tfm/google/noto/
%{_texmf_main}/fonts/truetype/google/noto/
%{_texmf_main}/fonts/type1/google/noto/
%{_texmf_main}/fonts/vf/google/noto/
%{_texmf_main}/tex/latex/noto/
%doc %{_texmf_main}/doc/fonts/noto/

%files -n texlive-noto-emoji
%license ofl.txt
%{_texmf_main}/fonts/truetype/google/noto-emoji/
%doc %{_texmf_main}/doc/fonts/noto-emoji/

%files -n texlive-notomath
%license ofl.txt
%{_texmf_main}/fonts/map/dvips/notomath/
%{_texmf_main}/fonts/tfm/public/notomath/
%{_texmf_main}/fonts/type1/public/notomath/
%{_texmf_main}/fonts/vf/public/notomath/
%{_texmf_main}/tex/latex/notomath/
%doc %{_texmf_main}/doc/fonts/notomath/

%files -n texlive-nunito
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/nunito/
%{_texmf_main}/fonts/map/dvips/nunito/
%{_texmf_main}/fonts/opentype/public/nunito/
%{_texmf_main}/fonts/tfm/public/nunito/
%{_texmf_main}/fonts/type1/public/nunito/
%{_texmf_main}/fonts/vf/public/nunito/
%{_texmf_main}/tex/latex/nunito/
%doc %{_texmf_main}/doc/fonts/nunito/

%files -n texlive-obnov
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/obnov/
%{_texmf_main}/fonts/tfm/public/obnov/
%{_texmf_main}/tex/latex/obnov/
%doc %{_texmf_main}/doc/fonts/obnov/

%files -n texlive-ocherokee
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/ocherokee/
%{_texmf_main}/fonts/map/dvips/ocherokee/
%{_texmf_main}/fonts/ofm/public/ocherokee/
%{_texmf_main}/fonts/ovf/public/ocherokee/
%{_texmf_main}/fonts/ovp/public/ocherokee/
%{_texmf_main}/fonts/tfm/public/ocherokee/
%{_texmf_main}/fonts/type1/public/ocherokee/
%{_texmf_main}/omega/ocp/ocherokee/
%{_texmf_main}/omega/otp/ocherokee/
%{_texmf_main}/tex/lambda/ocherokee/
%doc %{_texmf_main}/doc/omega/ocherokee/

%files -n texlive-ocr-b
%license other-free.txt
%{_texmf_main}/fonts/source/public/ocr-b/
%{_texmf_main}/fonts/tfm/public/ocr-b/
%doc %{_texmf_main}/doc/fonts/ocr-b/

%files -n texlive-ocr-b-outline
%license other-free.txt
%{_texmf_main}/fonts/map/dvips/ocr-b-outline/
%{_texmf_main}/fonts/opentype/public/ocr-b-outline/
%{_texmf_main}/fonts/type1/public/ocr-b-outline/
%doc %{_texmf_main}/doc/fonts/ocr-b-outline/
%{_datadir}/fonts/ocr-b-outline
%{_datadir}/appdata/ocr-b-outline.metainfo.xml

%files -n texlive-ogham
%license pd.txt
%{_texmf_main}/fonts/source/public/ogham/
%{_texmf_main}/fonts/tfm/public/ogham/
%doc %{_texmf_main}/doc/fonts/ogham/

%files -n texlive-oinuit
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/oinuit/
%{_texmf_main}/fonts/ofm/public/oinuit/
%{_texmf_main}/fonts/ovf/public/oinuit/
%{_texmf_main}/fonts/tfm/public/oinuit/
%{_texmf_main}/fonts/type1/public/oinuit/
%{_texmf_main}/omega/ocp/oinuit/
%{_texmf_main}/omega/otp/oinuit/
%{_texmf_main}/tex/lambda/oinuit/
%doc %{_texmf_main}/doc/fonts/oinuit/

%files -n texlive-old-arrows
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/old-arrows/
%{_texmf_main}/fonts/enc/dvips/old-arrows/
%{_texmf_main}/fonts/map/dvips/old-arrows/
%{_texmf_main}/fonts/tfm/public/old-arrows/
%{_texmf_main}/fonts/type1/public/old-arrows/
%{_texmf_main}/tex/latex/old-arrows/
%doc %{_texmf_main}/doc/fonts/old-arrows/

%files -n texlive-oldlatin
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/oldlatin/
%{_texmf_main}/fonts/tfm/public/oldlatin/
%doc %{_texmf_main}/doc/fonts/oldlatin/

%files -n texlive-oldstandard
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/oldstandard/
%{_texmf_main}/fonts/map/dvips/oldstandard/
%{_texmf_main}/fonts/opentype/public/oldstandard/
%{_texmf_main}/fonts/tfm/public/oldstandard/
%{_texmf_main}/fonts/type1/public/oldstandard/
%{_texmf_main}/fonts/vf/public/oldstandard/
%{_texmf_main}/tex/latex/oldstandard/
%doc %{_texmf_main}/doc/fonts/oldstandard/

%files -n texlive-opensans
%license apache2.txt
%{_texmf_main}/fonts/enc/dvips/opensans/
%{_texmf_main}/fonts/map/dvips/opensans/
%{_texmf_main}/fonts/tfm/ascender/opensans/
%{_texmf_main}/fonts/truetype/ascender/opensans/
%{_texmf_main}/fonts/type1/ascender/opensans/
%{_texmf_main}/fonts/vf/ascender/opensans/
%{_texmf_main}/tex/latex/opensans/
%doc %{_texmf_main}/doc/fonts/opensans/

%files -n texlive-orkhun
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/orkhun/
%{_texmf_main}/fonts/tfm/public/orkhun/
%doc %{_texmf_main}/doc/fonts/orkhun/

%files -n texlive-oswald
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/oswald/
%{_texmf_main}/fonts/map/dvips/oswald/
%{_texmf_main}/fonts/tfm/public/oswald/
%{_texmf_main}/fonts/type1/public/oswald/
%{_texmf_main}/fonts/vf/public/oswald/
%{_texmf_main}/tex/latex/oswald/
%doc %{_texmf_main}/doc/fonts/oswald/

%files -n texlive-overlock
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/overlock/
%{_texmf_main}/fonts/map/dvips/overlock/
%{_texmf_main}/fonts/opentype/tipo/overlock/
%{_texmf_main}/fonts/tfm/tipo/overlock/
%{_texmf_main}/fonts/type1/tipo/overlock/
%{_texmf_main}/fonts/vf/tipo/overlock/
%{_texmf_main}/tex/latex/overlock/
%doc %{_texmf_main}/doc/fonts/overlock/
%{_datadir}/fonts/overlock
%{_datadir}/appdata/overlock.metainfo.xml

%files -n texlive-pacioli
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/pacioli/
%{_texmf_main}/fonts/tfm/public/pacioli/
%{_texmf_main}/tex/latex/pacioli/
%doc %{_texmf_main}/doc/fonts/pacioli/

%files -n texlive-pagella-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pagella-otf/
%doc %{_texmf_main}/doc/fonts/pagella-otf/

%files -n texlive-paratype
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/paratype/ptmono/
%{_texmf_main}/fonts/afm/paratype/ptsans/
%{_texmf_main}/fonts/afm/paratype/ptserif/
%{_texmf_main}/fonts/enc/dvips/paratype/
%{_texmf_main}/fonts/map/dvips/paratype/
%{_texmf_main}/fonts/tfm/paratype/ptmono/
%{_texmf_main}/fonts/tfm/paratype/ptsans/
%{_texmf_main}/fonts/tfm/paratype/ptserif/
%{_texmf_main}/fonts/truetype/paratype/ptmono/
%{_texmf_main}/fonts/truetype/paratype/ptsans/
%{_texmf_main}/fonts/truetype/paratype/ptserif/
%{_texmf_main}/fonts/type1/paratype/ptmono/
%{_texmf_main}/fonts/type1/paratype/ptsans/
%{_texmf_main}/fonts/type1/paratype/ptserif/
%{_texmf_main}/fonts/vf/paratype/ptmono/
%{_texmf_main}/fonts/vf/paratype/ptsans/
%{_texmf_main}/fonts/vf/paratype/ptserif/
%{_texmf_main}/tex/latex/paratype/
%doc %{_texmf_main}/doc/fonts/paratype/

%files -n texlive-pennstander-otf
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/pennstander-otf/
%{_texmf_main}/fonts/truetype/public/pennstander-otf/
%{_texmf_main}/tex/latex/pennstander-otf/
%doc %{_texmf_main}/doc/fonts/pennstander-otf/

%files -n texlive-phaistos
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/phaistos/
%{_texmf_main}/fonts/map/dvips/phaistos/
%{_texmf_main}/fonts/opentype/public/phaistos/
%{_texmf_main}/fonts/tfm/public/phaistos/
%{_texmf_main}/fonts/type1/public/phaistos/
%{_texmf_main}/tex/latex/phaistos/
%doc %{_texmf_main}/doc/fonts/phaistos/
%{_datadir}/fonts/phaistos
%{_datadir}/appdata/phaistos.metainfo.xml

%files -n texlive-phonetic
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/phonetic/
%{_texmf_main}/fonts/tfm/public/phonetic/
%{_texmf_main}/tex/latex/phonetic/
%doc %{_texmf_main}/doc/fonts/phonetic/

%files -n texlive-pigpen
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/pigpen/
%{_texmf_main}/fonts/source/public/pigpen/
%{_texmf_main}/fonts/tfm/public/pigpen/
%{_texmf_main}/fonts/type1/public/pigpen/
%{_texmf_main}/tex/latex/pigpen/
%doc %{_texmf_main}/doc/fonts/pigpen/

%files -n texlive-playfair
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/playfair/
%{_texmf_main}/fonts/map/dvips/playfair/
%{_texmf_main}/fonts/opentype/public/playfair/
%{_texmf_main}/fonts/tfm/public/playfair/
%{_texmf_main}/fonts/type1/public/playfair/
%{_texmf_main}/fonts/vf/public/playfair/
%{_texmf_main}/tex/latex/playfair/
%doc %{_texmf_main}/doc/fonts/playfair/
%{_datadir}/fonts/playfair
%{_datadir}/appdata/playfair.metainfo.xml

%files -n texlive-plex
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/plex/
%{_texmf_main}/fonts/map/dvips/plex/
%{_texmf_main}/fonts/opentype/ibm/plex/
%{_texmf_main}/fonts/tfm/ibm/plex/
%{_texmf_main}/fonts/type1/ibm/plex/
%{_texmf_main}/fonts/vf/ibm/plex/
%{_texmf_main}/tex/latex/plex/
%doc %{_texmf_main}/doc/fonts/plex/

%files -n texlive-plex-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/plex-otf/
%doc %{_texmf_main}/doc/fonts/plex-otf/

%files -n texlive-plimsoll
%license gpl3.txt
%{_texmf_main}/fonts/afm/public/plimsoll/
%{_texmf_main}/fonts/enc/dvips/plimsoll/
%{_texmf_main}/fonts/map/dvips/plimsoll/
%{_texmf_main}/fonts/tfm/public/plimsoll/
%{_texmf_main}/fonts/type1/public/plimsoll/
%{_texmf_main}/tex/latex/plimsoll/
%doc %{_texmf_main}/doc/fonts/plimsoll/

%files -n texlive-poiretone
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/poiretone/
%{_texmf_main}/fonts/map/dvips/poiretone/
%{_texmf_main}/fonts/tfm/public/poiretone/
%{_texmf_main}/fonts/truetype/public/poiretone/
%{_texmf_main}/fonts/type1/public/poiretone/
%{_texmf_main}/fonts/vf/public/poiretone/
%{_texmf_main}/tex/latex/poiretone/
%doc %{_texmf_main}/doc/fonts/poiretone/

%files -n texlive-poltawski
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/gust/poltawski/
%{_texmf_main}/fonts/enc/dvips/poltawski/
%{_texmf_main}/fonts/map/dvips/poltawski/
%{_texmf_main}/fonts/opentype/gust/poltawski/
%{_texmf_main}/fonts/tfm/gust/poltawski/
%{_texmf_main}/fonts/type1/gust/poltawski/
%{_texmf_main}/tex/latex/poltawski/
%doc %{_texmf_main}/doc/fonts/poltawski/
%{_datadir}/fonts/poltawski
%{_datadir}/appdata/poltawski.metainfo.xml

%files -n texlive-prodint
%license ofl.txt
%{_texmf_main}/fonts/afm/public/prodint/
%{_texmf_main}/fonts/map/dvips/prodint/
%{_texmf_main}/fonts/tfm/public/prodint/
%{_texmf_main}/fonts/type1/public/prodint/
%{_texmf_main}/tex/latex/prodint/
%doc %{_texmf_main}/doc/fonts/prodint/

%files -n texlive-punk
%license knuth.txt
%{_texmf_main}/fonts/source/public/punk/
%{_texmf_main}/fonts/tfm/public/punk/
%doc %{_texmf_main}/doc/fonts/punk/

%files -n texlive-punk-latex
%license gpl2.txt
%{_texmf_main}/tex/latex/punk-latex/
%doc %{_texmf_main}/doc/latex/punk-latex/

%files -n texlive-punknova
%license other-free.txt
%{_texmf_main}/fonts/opentype/public/punknova/
%doc %{_texmf_main}/doc/fonts/punknova/
%{_datadir}/fonts/punknova
%{_datadir}/appdata/punknova.metainfo.xml

%files -n texlive-pxtxalfa
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/pxtxalfa/
%{_texmf_main}/fonts/vf/public/pxtxalfa/
%{_texmf_main}/tex/latex/pxtxalfa/
%doc %{_texmf_main}/doc/fonts/pxtxalfa/

%files -n texlive-qualitype
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/qualitype/
%doc %{_texmf_main}/doc/fonts/qualitype/
%{_datadir}/fonts/qualitype
%{_datadir}/appdata/qualitype.metainfo.xml

%files -n texlive-quattrocento
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/quattrocento/
%{_texmf_main}/fonts/map/dvips/quattrocento/
%{_texmf_main}/fonts/tfm/impallari/quattrocento/
%{_texmf_main}/fonts/truetype/impallari/quattrocento/
%{_texmf_main}/fonts/type1/impallari/quattrocento/
%{_texmf_main}/fonts/vf/impallari/quattrocento/
%{_texmf_main}/tex/latex/quattrocento/
%doc %{_texmf_main}/doc/fonts/quattrocento/

%files -n texlive-raleway
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/raleway/
%{_texmf_main}/fonts/map/dvips/raleway/
%{_texmf_main}/fonts/opentype/impallari/raleway/
%{_texmf_main}/fonts/tfm/impallari/raleway/
%{_texmf_main}/fonts/type1/impallari/raleway/
%{_texmf_main}/fonts/vf/impallari/raleway/
%{_texmf_main}/tex/latex/raleway/
%doc %{_texmf_main}/doc/latex/raleway/

%files -n texlive-recycle
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/recycle/
%{_texmf_main}/fonts/source/public/recycle/
%{_texmf_main}/fonts/tfm/public/recycle/
%{_texmf_main}/fonts/type1/public/recycle/
%{_texmf_main}/tex/latex/recycle/
%doc %{_texmf_main}/doc/fonts/recycle/

%files -n texlive-rit-fonts
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/rit-fonts/
%{_texmf_main}/fonts/truetype/public/rit-fonts/
%{_texmf_main}/tex/latex/rit-fonts/
%doc %{_texmf_main}/doc/fonts/rit-fonts/

%files -n texlive-roboto
%license apache2.txt
%{_texmf_main}/fonts/enc/dvips/roboto/
%{_texmf_main}/fonts/map/dvips/roboto/
%{_texmf_main}/fonts/opentype/google/roboto/
%{_texmf_main}/fonts/tfm/google/roboto/
%{_texmf_main}/fonts/type1/google/roboto/
%{_texmf_main}/fonts/vf/google/roboto/
%{_texmf_main}/tex/latex/roboto/
%doc %{_texmf_main}/doc/fonts/roboto/

%files -n texlive-romandeadf
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/romandeadf/
%{_texmf_main}/fonts/enc/dvips/romandeadf/
%{_texmf_main}/fonts/map/dvips/romandeadf/
%{_texmf_main}/fonts/tfm/public/romandeadf/
%{_texmf_main}/fonts/type1/public/romandeadf/
%{_texmf_main}/fonts/vf/public/romandeadf/
%{_texmf_main}/tex/latex/romandeadf/
%doc %{_texmf_main}/doc/fonts/romandeadf/

%files -n texlive-rosario
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/rosario/
%{_texmf_main}/fonts/map/dvips/rosario/
%{_texmf_main}/fonts/opentype/public/rosario/
%{_texmf_main}/fonts/tfm/public/rosario/
%{_texmf_main}/fonts/type1/public/rosario/
%{_texmf_main}/fonts/vf/public/rosario/
%{_texmf_main}/tex/latex/rosario/
%doc %{_texmf_main}/doc/fonts/rosario/
%{_datadir}/fonts/rosario
%{_datadir}/appdata/rosario.metainfo.xml

%files -n texlive-rsfso
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/rsfso/
%{_texmf_main}/fonts/tfm/public/rsfso/
%{_texmf_main}/fonts/vf/public/rsfso/
%{_texmf_main}/tex/latex/rsfso/
%doc %{_texmf_main}/doc/fonts/rsfso/

%files -n texlive-ruscap
%license ofl.txt
%{_texmf_main}/fonts/source/public/ruscap/
%{_texmf_main}/fonts/tfm/public/ruscap/
%doc %{_texmf_main}/doc/fonts/ruscap/

%files -n texlive-sansmathaccent
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/sansmathaccent/
%{_texmf_main}/fonts/tfm/public/sansmathaccent/
%{_texmf_main}/fonts/vf/public/sansmathaccent/
%{_texmf_main}/tex/latex/sansmathaccent/
%doc %{_texmf_main}/doc/fonts/sansmathaccent/

%files -n texlive-sansmathfonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/sansmathfonts/
%{_texmf_main}/fonts/source/public/sansmathfonts/
%{_texmf_main}/fonts/tfm/public/sansmathfonts/
%{_texmf_main}/fonts/type1/public/sansmathfonts/
%{_texmf_main}/fonts/vf/public/sansmathfonts/
%{_texmf_main}/tex/latex/sansmathfonts/
%doc %{_texmf_main}/doc/fonts/sansmathfonts/

%files -n texlive-sauter
%license gpl2.txt
%{_texmf_main}/fonts/source/public/sauter/

%files -n texlive-sauterfonts
%license gpl2.txt
%{_texmf_main}/tex/latex/sauterfonts/
%doc %{_texmf_main}/doc/latex/sauterfonts/

%files -n texlive-schola-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/schola-otf/
%doc %{_texmf_main}/doc/fonts/schola-otf/

%files -n texlive-scholax
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/scholax/
%{_texmf_main}/fonts/enc/dvips/scholax/
%{_texmf_main}/fonts/map/dvips/scholax/
%{_texmf_main}/fonts/opentype/public/scholax/
%{_texmf_main}/fonts/tfm/public/scholax/
%{_texmf_main}/fonts/type1/public/scholax/
%{_texmf_main}/fonts/vf/public/scholax/
%{_texmf_main}/tex/latex/scholax/
%doc %{_texmf_main}/doc/fonts/scholax/
%{_datadir}/fonts/scholax
%{_datadir}/appdata/scholax.metainfo.xml

%files -n texlive-schulschriften
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/schulschriften/
%{_texmf_main}/fonts/tfm/public/schulschriften/
%{_texmf_main}/tex/latex/schulschriften/
%doc %{_texmf_main}/doc/fonts/schulschriften/

%files -n texlive-semaphor
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/semaphor/
%{_texmf_main}/fonts/enc/dvips/semaphor/
%{_texmf_main}/fonts/map/dvips/semaphor/
%{_texmf_main}/fonts/opentype/public/semaphor/
%{_texmf_main}/fonts/source/public/semaphor/
%{_texmf_main}/fonts/tfm/public/semaphor/
%{_texmf_main}/fonts/type1/public/semaphor/
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/latex/semaphor/
%{_texmf_main}/tex/plain/semaphor/
%doc %{_texmf_main}/doc/fonts/semaphor/
%{_datadir}/fonts/semaphor
%{_datadir}/appdata/semaphor.metainfo.xml

%files -n texlive-shobhika
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/shobhika/
%doc %{_texmf_main}/doc/fonts/shobhika/

%files -n texlive-simpleicons
%license cc-zero-1.txt
%{_texmf_main}/fonts/enc/dvips/simpleicons/
%{_texmf_main}/fonts/map/dvips/simpleicons/
%{_texmf_main}/fonts/opentype/public/simpleicons/
%{_texmf_main}/fonts/tfm/public/simpleicons/
%{_texmf_main}/fonts/type1/public/simpleicons/
%{_texmf_main}/tex/latex/simpleicons/
%doc %{_texmf_main}/doc/fonts/simpleicons/

%files -n texlive-skull
%license gpl2.txt
%{_texmf_main}/fonts/source/public/skull/
%{_texmf_main}/fonts/tfm/public/skull/
%{_texmf_main}/tex/latex/skull/

%files -n texlive-sourcecodepro
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/sourcecodepro/
%{_texmf_main}/fonts/map/dvips/sourcecodepro/
%{_texmf_main}/fonts/opentype/adobe/sourcecodepro/
%{_texmf_main}/fonts/tfm/adobe/sourcecodepro/
%{_texmf_main}/fonts/type1/adobe/sourcecodepro/
%{_texmf_main}/fonts/vf/adobe/sourcecodepro/
%{_texmf_main}/tex/latex/sourcecodepro/
%doc %{_texmf_main}/doc/latex/sourcecodepro/

%files -n texlive-sourcesanspro
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/sourcesanspro/
%{_texmf_main}/fonts/map/dvips/sourcesanspro/
%{_texmf_main}/fonts/opentype/adobe/sourcesanspro/
%{_texmf_main}/fonts/tfm/adobe/sourcesanspro/
%{_texmf_main}/fonts/type1/adobe/sourcesanspro/
%{_texmf_main}/fonts/vf/adobe/sourcesanspro/
%{_texmf_main}/tex/latex/sourcesanspro/
%doc %{_texmf_main}/doc/latex/sourcesanspro/

%files -n texlive-sourceserifpro
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/sourceserifpro/
%{_texmf_main}/fonts/map/dvips/sourceserifpro/
%{_texmf_main}/fonts/opentype/adobe/sourceserifpro/
%{_texmf_main}/fonts/tfm/adobe/sourceserifpro/
%{_texmf_main}/fonts/type1/adobe/sourceserifpro/
%{_texmf_main}/fonts/vf/adobe/sourceserifpro/
%{_texmf_main}/tex/latex/sourceserifpro/
%doc %{_texmf_main}/doc/latex/sourceserifpro/

%files -n texlive-spectral
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/spectral/
%{_texmf_main}/fonts/map/dvips/spectral/
%{_texmf_main}/fonts/tfm/production/spectral/
%{_texmf_main}/fonts/truetype/production/spectral/
%{_texmf_main}/fonts/type1/production/spectral/
%{_texmf_main}/fonts/vf/production/spectral/
%{_texmf_main}/tex/latex/spectral/
%doc %{_texmf_main}/doc/fonts/spectral/

%files -n texlive-splentinex
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/splentinex/
%{_texmf_main}/fonts/map/dvips/splentinex/
%{_texmf_main}/fonts/opentype/public/splentinex/
%{_texmf_main}/fonts/tfm/public/splentinex/
%{_texmf_main}/fonts/type1/public/splentinex/
%{_texmf_main}/fonts/vf/public/splentinex/
%{_texmf_main}/tex/latex/splentinex/
%doc %{_texmf_main}/doc/fonts/splentinex/

%files -n texlive-srbtiks
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/srbtiks/
%{_texmf_main}/fonts/map/dvips/srbtiks/
%{_texmf_main}/fonts/tfm/public/srbtiks/
%{_texmf_main}/fonts/vf/public/srbtiks/
%{_texmf_main}/tex/latex/srbtiks/
%doc %{_texmf_main}/doc/fonts/srbtiks/

%files -n texlive-starfont
%license pd.txt
%{_texmf_main}/fonts/afm/public/starfont/
%{_texmf_main}/fonts/map/dvips/starfont/
%{_texmf_main}/fonts/tfm/public/starfont/
%{_texmf_main}/fonts/type1/public/starfont/
%{_texmf_main}/tex/latex/starfont/
%doc %{_texmf_main}/doc/fonts/starfont/

%files -n texlive-staves
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/staves/
%{_texmf_main}/fonts/tfm/public/staves/
%{_texmf_main}/fonts/type1/public/staves/
%{_texmf_main}/tex/latex/staves/
%doc %{_texmf_main}/doc/fonts/staves/

%files -n texlive-step
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/step/
%{_texmf_main}/fonts/map/dvips/step/
%{_texmf_main}/fonts/opentype/public/step/
%{_texmf_main}/fonts/tfm/public/step/
%{_texmf_main}/fonts/type1/public/step/
%{_texmf_main}/fonts/vf/public/step/
%{_texmf_main}/tex/latex/step/
%doc %{_texmf_main}/doc/fonts/step/
%{_datadir}/fonts/step
%{_datadir}/appdata/step.metainfo.xml

%files -n texlive-stepgreek
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/stepgreek/
%{_texmf_main}/fonts/map/dvips/stepgreek/
%{_texmf_main}/fonts/tfm/public/stepgreek/
%{_texmf_main}/fonts/type1/public/stepgreek/
%{_texmf_main}/fonts/vf/public/stepgreek/
%{_texmf_main}/tex/latex/stepgreek/
%doc %{_texmf_main}/doc/fonts/stepgreek/

%files -n texlive-stickstoo
%license ofl.txt
%{_texmf_main}/fonts/afm/public/stickstoo/
%{_texmf_main}/fonts/enc/dvips/stickstoo/
%{_texmf_main}/fonts/map/dvips/stickstoo/
%{_texmf_main}/fonts/tfm/public/stickstoo/
%{_texmf_main}/fonts/type1/public/stickstoo/
%{_texmf_main}/fonts/vf/public/stickstoo/
%{_texmf_main}/tex/latex/stickstoo/
%doc %{_texmf_main}/doc/fonts/stickstoo/

%files -n texlive-stix
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/stix/
%{_texmf_main}/fonts/map/dvips/stix/
%{_texmf_main}/fonts/opentype/public/stix/
%{_texmf_main}/fonts/tfm/public/stix/
%{_texmf_main}/fonts/type1/public/stix/
%{_texmf_main}/fonts/vf/public/stix/
%{_texmf_main}/tex/latex/stix/
%doc %{_texmf_main}/doc/fonts/stix/

%files -n texlive-stix2-otf
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/stix2-otf/
%doc %{_texmf_main}/doc/fonts/stix2-otf/

%files -n texlive-stix2-type1
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/stix2-type1/
%{_texmf_main}/fonts/map/dvips/stix2-type1/
%{_texmf_main}/fonts/tfm/public/stix2-type1/
%{_texmf_main}/fonts/type1/public/stix2-type1/
%{_texmf_main}/tex/latex/stix2-type1/
%doc %{_texmf_main}/doc/fonts/stix2-type1/

%files -n texlive-superiors
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/superiors/
%doc %{_texmf_main}/doc/latex/superiors/

%files -n texlive-svrsymbols
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/svrsymbols/
%{_texmf_main}/fonts/map/dvips/svrsymbols/
%{_texmf_main}/fonts/opentype/public/svrsymbols/
%{_texmf_main}/fonts/tfm/public/svrsymbols/
%{_texmf_main}/fonts/type1/public/svrsymbols/
%{_texmf_main}/tex/latex/svrsymbols/
%doc %{_texmf_main}/doc/fonts/svrsymbols/
%{_datadir}/fonts/svrsymbols
%{_datadir}/appdata/svrsymbols.metainfo.xml

%files -n texlive-symbats3
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/symbats3/
%doc %{_texmf_main}/doc/fonts/symbats3/

%files -n texlive-tapir
%license gpl2.txt
%{_texmf_main}/fonts/source/public/tapir/
%{_texmf_main}/fonts/type1/public/tapir/
%doc %{_texmf_main}/doc/fonts/tapir/

%files -n texlive-tempora
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/tempora/
%{_texmf_main}/fonts/enc/dvips/tempora/
%{_texmf_main}/fonts/map/dvips/tempora/
%{_texmf_main}/fonts/opentype/public/tempora/
%{_texmf_main}/fonts/tfm/public/tempora/
%{_texmf_main}/fonts/type1/public/tempora/
%{_texmf_main}/fonts/vf/public/tempora/
%{_texmf_main}/tex/latex/tempora/
%doc %{_texmf_main}/doc/fonts/tempora/
%{_datadir}/fonts/tempora
%{_datadir}/appdata/tempora.metainfo.xml

%files -n texlive-tengwarscript
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/tengwarscript/
%{_texmf_main}/fonts/map/dvips/tengwarscript/
%{_texmf_main}/fonts/tfm/public/tengwarscript/
%{_texmf_main}/fonts/vf/public/tengwarscript/
%{_texmf_main}/tex/latex/tengwarscript/
%doc %{_texmf_main}/doc/latex/tengwarscript/

%files -n texlive-termes-otf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/termes-otf/
%doc %{_texmf_main}/doc/fonts/termes-otf/

%files -n texlive-tfrupee
%license gpl3.txt
%{_texmf_main}/fonts/afm/public/tfrupee/
%{_texmf_main}/fonts/map/dvips/tfrupee/
%{_texmf_main}/fonts/tfm/public/tfrupee/
%{_texmf_main}/fonts/type1/public/tfrupee/
%{_texmf_main}/tex/latex/tfrupee/
%doc %{_texmf_main}/doc/fonts/tfrupee/

%files -n texlive-theanodidot
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/theanodidot/
%{_texmf_main}/fonts/map/dvips/theanodidot/
%{_texmf_main}/fonts/tfm/public/theanodidot/
%{_texmf_main}/fonts/truetype/public/theanodidot/
%{_texmf_main}/fonts/type1/public/theanodidot/
%{_texmf_main}/fonts/vf/public/theanodidot/
%{_texmf_main}/tex/latex/theanodidot/
%doc %{_texmf_main}/doc/fonts/theanodidot/

%files -n texlive-theanomodern
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/theanomodern/
%{_texmf_main}/fonts/map/dvips/theanomodern/
%{_texmf_main}/fonts/tfm/public/theanomodern/
%{_texmf_main}/fonts/truetype/public/theanomodern/
%{_texmf_main}/fonts/type1/public/theanomodern/
%{_texmf_main}/fonts/vf/public/theanomodern/
%{_texmf_main}/tex/latex/theanomodern/
%doc %{_texmf_main}/doc/fonts/theanomodern/

%files -n texlive-theanooldstyle
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/theanooldstyle/
%{_texmf_main}/fonts/map/dvips/theanooldstyle/
%{_texmf_main}/fonts/tfm/public/theanooldstyle/
%{_texmf_main}/fonts/truetype/public/theanooldstyle/
%{_texmf_main}/fonts/type1/public/theanooldstyle/
%{_texmf_main}/fonts/vf/public/theanooldstyle/
%{_texmf_main}/tex/latex/theanooldstyle/
%doc %{_texmf_main}/doc/fonts/theanooldstyle/

%files -n texlive-tinos
%license apache2.txt
%{_texmf_main}/fonts/enc/dvips/tinos/
%{_texmf_main}/fonts/map/dvips/tinos/
%{_texmf_main}/fonts/tfm/google/tinos/
%{_texmf_main}/fonts/truetype/google/tinos/
%{_texmf_main}/fonts/type1/google/tinos/
%{_texmf_main}/fonts/vf/google/tinos/
%{_texmf_main}/tex/latex/tinos/
%doc %{_texmf_main}/doc/fonts/tinos/

%files -n texlive-tpslifonts
%license gpl2.txt
%{_texmf_main}/tex/latex/tpslifonts/
%doc %{_texmf_main}/doc/latex/tpslifonts/

%files -n texlive-trajan
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/trajan/
%{_texmf_main}/fonts/map/dvips/trajan/
%{_texmf_main}/fonts/tfm/public/trajan/
%{_texmf_main}/fonts/type1/public/trajan/
%{_texmf_main}/tex/latex/trajan/
%doc %{_texmf_main}/doc/latex/trajan/

%files -n texlive-twemoji-colr
%license cc-by-sa-4.txt
%{_texmf_main}/fonts/truetype/public/twemoji-colr/
%doc %{_texmf_main}/doc/fonts/twemoji-colr/

%files -n texlive-txfontsb
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/txfontsb/
%{_texmf_main}/fonts/enc/dvips/txfontsb/
%{_texmf_main}/fonts/map/dvips/txfontsb/
%{_texmf_main}/fonts/opentype/public/txfontsb/
%{_texmf_main}/fonts/tfm/public/txfontsb/
%{_texmf_main}/fonts/type1/public/txfontsb/
%{_texmf_main}/fonts/vf/public/txfontsb/
%{_texmf_main}/tex/latex/txfontsb/
%doc %{_texmf_main}/doc/fonts/txfontsb/
%{_datadir}/fonts/txfontsb
%{_datadir}/appdata/txfontsb.metainfo.xml

%files -n texlive-txuprcal
%license gpl3.txt
%{_texmf_main}/fonts/map/dvips/txuprcal/
%{_texmf_main}/fonts/tfm/public/txuprcal/
%{_texmf_main}/fonts/type1/public/txuprcal/
%{_texmf_main}/tex/latex/txuprcal/
%doc %{_texmf_main}/doc/fonts/txuprcal/

%files -n texlive-typicons
%license lppl1.3c.txt
%{_texmf_main}/fonts/truetype/public/typicons/
%{_texmf_main}/tex/latex/typicons/
%doc %{_texmf_main}/doc/fonts/typicons/

%files -n texlive-umtypewriter
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/umtypewriter/
%doc %{_texmf_main}/doc/fonts/umtypewriter/
%{_datadir}/fonts/umtypewriter
%{_datadir}/appdata/umtypewriter.metainfo.xml

%files -n texlive-universa
%license gpl2.txt
%{_texmf_main}/fonts/source/public/universa/
%{_texmf_main}/fonts/tfm/public/universa/
%{_texmf_main}/tex/latex/universa/
%doc %{_texmf_main}/doc/fonts/universa/

%files -n texlive-universalis
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/universalis/
%{_texmf_main}/fonts/map/dvips/universalis/
%{_texmf_main}/fonts/opentype/arkandis/universalis/
%{_texmf_main}/fonts/tfm/arkandis/universalis/
%{_texmf_main}/fonts/type1/arkandis/universalis/
%{_texmf_main}/fonts/vf/arkandis/universalis/
%{_texmf_main}/tex/latex/universalis/
%doc %{_texmf_main}/doc/fonts/universalis/
%{_datadir}/fonts/universalis
%{_datadir}/appdata/universalis.metainfo.xml

%files -n texlive-uppunctlm
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/uppunctlm/
%{_texmf_main}/fonts/vf/public/uppunctlm/
%{_texmf_main}/tex/latex/uppunctlm/
%doc %{_texmf_main}/doc/fonts/uppunctlm/

%files -n texlive-urwchancal
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/urw/urwchancal/
%{_texmf_main}/fonts/vf/urw/urwchancal/
%{_texmf_main}/tex/latex/urwchancal/
%doc %{_texmf_main}/doc/fonts/urwchancal/

%files -n texlive-venturisadf
%{_texmf_main}/fonts/afm/public/venturisadf/
%{_texmf_main}/fonts/enc/dvips/venturisadf/
%{_texmf_main}/fonts/map/dvips/venturisadf/
%{_texmf_main}/fonts/opentype/public/venturisadf/
%{_texmf_main}/fonts/tfm/public/venturisadf/
%{_texmf_main}/fonts/type1/public/venturisadf/
%{_texmf_main}/fonts/vf/public/venturisadf/
%{_texmf_main}/tex/latex/venturisadf/
%doc %{_texmf_main}/doc/fonts/venturisadf/

%files -n texlive-wsuipa
%{_texmf_main}/fonts/source/public/wsuipa/
%{_texmf_main}/fonts/tfm/public/wsuipa/
%{_texmf_main}/tex/latex/wsuipa/
%doc %{_texmf_main}/doc/fonts/wsuipa/

%files -n texlive-xcharter
%license mit.txt
%{_texmf_main}/fonts/afm/public/xcharter/
%{_texmf_main}/fonts/enc/dvips/xcharter/
%{_texmf_main}/fonts/map/dvips/xcharter/
%{_texmf_main}/fonts/opentype/public/xcharter/
%{_texmf_main}/fonts/tfm/public/xcharter/
%{_texmf_main}/fonts/type1/public/xcharter/
%{_texmf_main}/fonts/vf/public/xcharter/
%{_texmf_main}/tex/latex/xcharter/
%doc %{_texmf_main}/doc/fonts/xcharter/
%{_datadir}/fonts/xcharter
%{_datadir}/appdata/xcharter.metainfo.xml

%files -n texlive-xcharter-math
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/xcharter-math/
%{_texmf_main}/tex/latex/xcharter-math/
%doc %{_texmf_main}/doc/fonts/xcharter-math/

%files -n texlive-xits
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/xits/
%doc %{_texmf_main}/doc/fonts/xits/
%{_datadir}/fonts/xits
%{_datadir}/appdata/xits.metainfo.xml

%files -n texlive-yfonts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/yfonts/
%doc %{_texmf_main}/doc/latex/yfonts/

%files -n texlive-yfonts-otf
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/yfonts-otf/
%{_texmf_main}/tex/latex/yfonts-otf/
%doc %{_texmf_main}/doc/fonts/yfonts-otf/

%files -n texlive-yfonts-t1
%license lppl1.3c.txt
%license yfonts-t1-license-email.pdf
%{_texmf_main}/dvips/yfonts-t1/
%{_texmf_main}/fonts/afm/public/yfonts-t1/
%{_texmf_main}/fonts/map/dvips/yfonts-t1/
%{_texmf_main}/fonts/type1/public/yfonts-t1/
%doc %{_texmf_main}/doc/fonts/yfonts-t1/

%files -n texlive-yinit-otf
%license pd.txt
%{_texmf_main}/fonts/opentype/public/yinit-otf/
%doc %{_texmf_main}/doc/fonts/yinit-otf/
%{_datadir}/fonts/yinit-otf
%{_datadir}/appdata/yinit-otf.metainfo.xml

%files -n texlive-ysabeau
%license ofl.txt
%{_texmf_main}/fonts/enc/dvips/ysabeau/
%{_texmf_main}/fonts/map/dvips/ysabeau/
%{_texmf_main}/fonts/opentype/public/ysabeau/
%{_texmf_main}/fonts/tfm/public/ysabeau/
%{_texmf_main}/fonts/truetype/public/ysabeau/
%{_texmf_main}/fonts/type1/public/ysabeau/
%{_texmf_main}/fonts/vf/public/ysabeau/
%{_texmf_main}/tex/latex/ysabeau/
%doc %{_texmf_main}/doc/fonts/ysabeau/

%files -n texlive-zlmtt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/zlmtt/
%doc %{_texmf_main}/doc/fonts/zlmtt/

%changelog
* Tue Jan 20 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77044-2
- fix licensing tags
- Validate AppData files

* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77044-1
- Update to svn77044
- update to latest component revisions
- fix descriptions, licensing

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75960-2
- regenerated, no longer get deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75960-1
- Update to TeX Live 2025
