%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-luatex
Epoch:          12
Version:        svn77516
Release:        2%{?dist}
Summary:        LuaTeX packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-luatex.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/addliga.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/addliga.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/addtoluatexpath.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/addtoluatexpath.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auto-pst-pdf-lua.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auto-pst-pdf-lua.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/barracuda.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/barracuda.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bezierplot.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bezierplot.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blopentype.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blopentype.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/char2path.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/char2path.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chickenize.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chickenize.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chinese-jfm.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chinese-jfm.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cloze.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cloze.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/combofont.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/combofont.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cstypo.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cstypo.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctablestack.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctablestack.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ekdosis.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ekdosis.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emoji.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emoji.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emojicite.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emojicite.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/enigma.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/enigma.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancymag.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancymag.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/farbe.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/farbe.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gitinfo-lua.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gitinfo-lua.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ideavault.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ideavault.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/innerscript.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/innerscript.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interpreter.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interpreter.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kanaparser.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kanaparser.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kkluaverb.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kkluaverb.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kkran.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kkran.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kksymbols.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kksymbols.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ligtype.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ligtype.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linebreaker.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linebreaker.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/longmath.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/longmath.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lparse.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lparse.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lt3luabridge.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lt3luabridge.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-placeholders.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-placeholders.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-tinyyaml.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-tinyyaml.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-typo.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-typo.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-uca.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-uca.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-ul.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-ul.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-visual-debug.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-visual-debug.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-widow-control.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-widow-control.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaaddplot.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaaddplot.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacas.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacas.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacensor.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacensor.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacode.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacode.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacolor.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacolor.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacomplex.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luacomplex.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luagcd.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luagcd.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luahttp.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luahttp.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luahyphenrules.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luahyphenrules.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaimageembed.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaimageembed.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaindex.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaindex.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luainputenc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luainputenc.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luakeys.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luakeys.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luakeyval.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luakeyval.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-math.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-math.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-truncate.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-truncate.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualibs.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualibs.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualinalg.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualinalg.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamathalign.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamathalign.doc.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamaths.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamaths.doc.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamml.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamml.doc.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamodulartables.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamodulartables.doc.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamplib.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luamplib.doc.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaoptions.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaoptions.doc.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luapackageloader.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luapackageloader.doc.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaplot.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaplot.doc.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaprogtable.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaprogtable.doc.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaquotes.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaquotes.doc.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luarandom.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luarandom.doc.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaset.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaset.doc.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatbls.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatbls.doc.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex-type-definitions.tar.xz
Source143:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex-type-definitions.doc.tar.xz
Source144:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex85.tar.xz
Source145:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex85.doc.tar.xz
Source146:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexbase.tar.xz
Source147:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexbase.doc.tar.xz
Source148:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexko.tar.xz
Source149:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexko.doc.tar.xz
Source150:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatextra.tar.xz
Source151:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatextra.doc.tar.xz
Source152:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatikz.tar.xz
Source153:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatikz.doc.tar.xz
Source154:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatruthtable.tar.xz
Source155:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatruthtable.doc.tar.xz
Source156:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luavlna.tar.xz
Source157:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luavlna.doc.tar.xz
Source158:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaxml.tar.xz
Source159:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaxml.doc.tar.xz
Source160:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lutabulartools.tar.xz
Source161:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lutabulartools.doc.tar.xz
Source162:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marginalia.tar.xz
Source163:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marginalia.doc.tar.xz
Source164:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim.tar.xz
Source165:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim.doc.tar.xz
Source166:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-math.tar.xz
Source167:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-math.doc.tar.xz
Source168:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-mp.tar.xz
Source169:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-mp.doc.tar.xz
Source170:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-pdf.tar.xz
Source171:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-pdf.doc.tar.xz
Source172:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-xmp.tar.xz
Source173:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-xmp.doc.tar.xz
Source174:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newpax.tar.xz
Source175:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newpax.doc.tar.xz
Source176:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nodetree.tar.xz
Source177:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nodetree.doc.tar.xz
Source178:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/odsfile.tar.xz
Source179:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/odsfile.doc.tar.xz
Source180:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parstat.tar.xz
Source181:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parstat.doc.tar.xz
Source182:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfarticle.tar.xz
Source183:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfarticle.doc.tar.xz
Source184:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfextra.tar.xz
Source185:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfextra.doc.tar.xz
Source186:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/penlight.tar.xz
Source187:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/penlight.doc.tar.xz
Source188:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/penlightplus.tar.xz
Source189:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/penlightplus.doc.tar.xz
Source190:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piton.tar.xz
Source191:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piton.doc.tar.xz
Source192:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/placeat.tar.xz
Source193:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/placeat.doc.tar.xz
Source194:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plantuml.tar.xz
Source195:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plantuml.doc.tar.xz
Source196:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pyluatex.tar.xz
Source197:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pyluatex.doc.tar.xz
Source198:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scikgtex.tar.xz
Source199:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scikgtex.doc.tar.xz
Source200:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seatingchart.tar.xz
Source201:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seatingchart.doc.tar.xz
Source202:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/selnolig.tar.xz
Source203:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/selnolig.doc.tar.xz
Source204:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/semesterplannerlua.tar.xz
Source205:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/semesterplannerlua.doc.tar.xz
Source206:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/showhyphenation.tar.xz
Source207:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/showhyphenation.doc.tar.xz
Source208:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/showkerning.tar.xz
Source209:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/showkerning.doc.tar.xz
Source210:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spacekern.tar.xz
Source211:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spacekern.doc.tar.xz
Source212:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spelling.tar.xz
Source213:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spelling.doc.tar.xz
Source214:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stricttex.tar.xz
Source215:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stricttex.doc.tar.xz
Source216:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sympycalc.tar.xz
Source217:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sympycalc.doc.tar.xz
Source218:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tango.tar.xz
Source219:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tango.doc.tar.xz
Source220:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/truthtable.tar.xz
Source221:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/truthtable.doc.tar.xz
Source222:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tsvtemplate.tar.xz
Source223:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tsvtemplate.doc.tar.xz
Source224:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typewriter.tar.xz
Source225:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typewriter.doc.tar.xz
Source226:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unibidi-lua.tar.xz
Source227:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unibidi-lua.doc.tar.xz
Source228:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uninormalize.tar.xz
Source229:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uninormalize.doc.tar.xz
Source230:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yamlvars.tar.xz
Source231:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yamlvars.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-addliga
Requires:       texlive-addtoluatexpath
Requires:       texlive-auto-pst-pdf-lua
Requires:       texlive-barracuda
Requires:       texlive-bezierplot
Requires:       texlive-blopentype
Requires:       texlive-char2path
Requires:       texlive-checkcites
Requires:       texlive-chickenize
Requires:       texlive-chinese-jfm
Requires:       texlive-cloze
Requires:       texlive-collection-basic
Requires:       texlive-combofont
Requires:       texlive-cstypo
Requires:       texlive-ctablestack
Requires:       texlive-ekdosis
Requires:       texlive-emoji
Requires:       texlive-emojicite
Requires:       texlive-enigma
Requires:       texlive-fancymag
Requires:       texlive-farbe
Requires:       texlive-gitinfo-lua
Requires:       texlive-ideavault
Requires:       texlive-innerscript
Requires:       texlive-interpreter
Requires:       texlive-kanaparser
Requires:       texlive-kkluaverb
Requires:       texlive-kkran
Requires:       texlive-kksymbols
Requires:       texlive-ligtype
Requires:       texlive-linebreaker
Requires:       texlive-longmath
Requires:       texlive-lparse
Requires:       texlive-lt3luabridge
Requires:       texlive-lua-placeholders
Requires:       texlive-lua-tinyyaml
Requires:       texlive-lua-typo
Requires:       texlive-lua-uca
Requires:       texlive-lua-ul
Requires:       texlive-lua-visual-debug
Requires:       texlive-lua-widow-control
Requires:       texlive-luaaddplot
Requires:       texlive-luacas
Requires:       texlive-luacensor
Requires:       texlive-luacode
Requires:       texlive-luacolor
Requires:       texlive-luacomplex
Requires:       texlive-luagcd
Requires:       texlive-luahttp
Requires:       texlive-luahyphenrules
Requires:       texlive-luaimageembed
Requires:       texlive-luaindex
Requires:       texlive-luainputenc
Requires:       texlive-luakeys
Requires:       texlive-luakeyval
Requires:       texlive-lualatex-math
Requires:       texlive-lualatex-truncate
Requires:       texlive-lualibs
Requires:       texlive-lualinalg
Requires:       texlive-luamathalign
Requires:       texlive-luamaths
Requires:       texlive-luamml
Requires:       texlive-luamodulartables
Requires:       texlive-luamplib
Requires:       texlive-luaoptions
Requires:       texlive-luaotfload
Requires:       texlive-luapackageloader
Requires:       texlive-luaplot
Requires:       texlive-luaprogtable
Requires:       texlive-luaquotes
Requires:       texlive-luarandom
Requires:       texlive-luaset
Requires:       texlive-luatbls
Requires:       texlive-luatex-type-definitions
Requires:       texlive-luatex85
Requires:       texlive-luatexbase
Requires:       texlive-luatexko
Requires:       texlive-luatextra
Requires:       texlive-luatikz
Requires:       texlive-luatruthtable
Requires:       texlive-luavlna
Requires:       texlive-luaxml
Requires:       texlive-lutabulartools
Requires:       texlive-marginalia
Requires:       texlive-minim
Requires:       texlive-minim-math
Requires:       texlive-minim-mp
Requires:       texlive-minim-pdf
Requires:       texlive-minim-xmp
Requires:       texlive-newpax
Requires:       texlive-nodetree
Requires:       texlive-odsfile
Requires:       texlive-optex
Requires:       texlive-parstat
Requires:       texlive-pdfarticle
Requires:       texlive-pdfextra
Requires:       texlive-penlight
Requires:       texlive-penlightplus
Requires:       texlive-piton
Requires:       texlive-placeat
Requires:       texlive-plantuml
Requires:       texlive-pyluatex
Requires:       texlive-scikgtex
Requires:       texlive-seatingchart
Requires:       texlive-selnolig
Requires:       texlive-semesterplannerlua
Requires:       texlive-showhyphenation
Requires:       texlive-showkerning
Requires:       texlive-spacekern
Requires:       texlive-spelling
Requires:       texlive-stricttex
Requires:       texlive-sympycalc
Requires:       texlive-tango
Requires:       texlive-texfindpkg
Requires:       texlive-truthtable
Requires:       texlive-tsvtemplate
Requires:       texlive-typewriter
Requires:       texlive-unibidi-lua
Requires:       texlive-uninormalize
Requires:       texlive-yamlvars

%description
Packages for LuaTeX, a TeX engine using Lua as an embedded scripting and
extension language, with native support for Unicode, OpenType/TrueType fonts,
and both PDF and DVI output. The LuaTeX engine itself (and plain formats) are
in collection-basic.


%package -n texlive-addliga
Summary:        Access basic ligatures in legacy TrueType fonts
Version:        svn50912
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(addliga.sty) = %{tl_version}

%description -n texlive-addliga
This small and simple package allows LuaLaTeX users to access basic ligatures
(ff, fi, ffi, fl, ffl) in legacy TrueType fonts (those lacking a liga table)
accessed via fontspec.

%package -n texlive-addtoluatexpath
Summary:        Add paths to Lua packages and input TeX files
Version:        svn73424
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Provides:       tex(addtoluatexpath.sty) = %{tl_version}

%description -n texlive-addtoluatexpath
This package provides a convenient way to add input and Lua package paths in
your document. You may want this package, for example, if a .cls or .sty file
is located on a network or cloud storage drive.

%package -n texlive-auto-pst-pdf-lua
Summary:        Using LuaLaTeX together with PostScript code
Version:        svn66637
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-iftex
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(pst-pdf.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(auto-pst-pdf-lua.sty) = %{tl_version}

%description -n texlive-auto-pst-pdf-lua
This package is a slightly modified version of auto-pst-pdf by Will Robertson,
which itself is a wrapper for pst-pdf by Rolf Niepraschk. The package allows
the use of LuaLaTeX together with PostScript related code, eg. PSTricks. It
depends on ifpdf, ifluatex, ifplatform, and xkeyval.

%package -n texlive-barracuda
Summary:        Draw barcodes with Lua
Version:        svn63708
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(barracuda.sty) = %{tl_version}

%description -n texlive-barracuda
The barracuda library is a modular Lua package for drawing barcode symbols. It
provides modules for writing barcodes from a LuaTeX document. It is also
possible to use Barracuda with a standalone Lua interpreter to draw barcodes in
different graphic formats like SVG.

%package -n texlive-bezierplot
Summary:        Approximate smooth function graphs with cubic bezier splines for use with TikZ or MetaPost
Version:        svn72750
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(xparse.sty)
Provides:       tex(bezierplot.sty) = %{tl_version}

%description -n texlive-bezierplot
This package consists of a Lua program as well as a (Lua)LaTeX .sty file. Given
a smooth function, bezierplot returns a smooth bezier path written in TikZ
notation (which also matches MetaPost) that approximates the graph of the
function. For polynomial functions of degree [?] 3 and their inverses the
approximation is exact (up to numeric precision). bezierplot also finds special
points such as extreme points and inflection points and reduces the number of
used points.

%package -n texlive-blopentype
Summary:        A basic LuaTeX OpenType handler
Version:        svn69080
License:        LPPL-1.3c AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-gates
Requires:       texlive-texapi
Requires:       texlive-yax
Provides:       tex(blot-files.tex) = %{tl_version}
Provides:       tex(blot-fonts.tex) = %{tl_version}
Provides:       tex(blot-lua.tex) = %{tl_version}
Provides:       tex(blot.tex) = %{tl_version}

%description -n texlive-blopentype
This is a basic LuaTeX OpenType handler, based on Paul Isambert's PiTeX code.
It should work with Plain TeX at least.

%package -n texlive-char2path
Summary:        A LaTeX package that converts characters into TikZ paths
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Provides:       tex(char2path.sty) = %{tl_version}
Provides:       tex(ctp-lmm-alpha-caps.data.tex) = %{tl_version}
Provides:       tex(ctp-lmm-alpha-small.data.tex) = %{tl_version}
Provides:       tex(ctp-lmm-arabic.data.tex) = %{tl_version}
Provides:       tex(ctp-lmm-others.data.tex) = %{tl_version}
Provides:       tex(ctp-lmr-alpha-caps.data.tex) = %{tl_version}
Provides:       tex(ctp-lmr-alpha-small.data.tex) = %{tl_version}
Provides:       tex(ctp-lmr-arabic.data.tex) = %{tl_version}
Provides:       tex(ctp-lmr-others.data.tex) = %{tl_version}
Provides:       tex(ctp-lms-alpha-caps.data.tex) = %{tl_version}
Provides:       tex(ctp-lms-alpha-small.data.tex) = %{tl_version}
Provides:       tex(ctp-lms-arabic.data.tex) = %{tl_version}
Provides:       tex(ctp-lms-others.data.tex) = %{tl_version}

%description -n texlive-char2path
This TikZ-based LaTeX package provides an easy way to convert characters to
TikZ-paths representing these characters.

%package -n texlive-chickenize
Summary:        Use lua callbacks for "interesting" textual effects
Version:        svn57325
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chickenize.sty) = %{tl_version}
Provides:       tex(chickenize.tex) = %{tl_version}

%description -n texlive-chickenize
The package allows manipulations of any LuaTeX document (it is known to work
with Plain LuaTeX and LuaLaTeX). Most of the package's functions are merely for
fun or educational use, but some functions (for example, colorstretch for
visualising the badness and font expansion of each line, and letterspaceadjust
doing what its name says) could be useful in a "normal" LuaTeX document.

%package -n texlive-chinese-jfm
Summary:        Luatexja-jfm files for Chinese typesetting
Version:        svn57758
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-chinese-jfm
ChineseJFM is a series of luatexja-jfm files for better Chinese typesetting,
providing quanjiao, banjiao, and kaiming three styles and other fancy features.
It can be used for both horizontal and vertical writing mode in
Simplified/Traditional Chinese or Japanese fonts.

%package -n texlive-cloze
Summary:        A LuaLaTeX package for creating cloze texts
Version:        svn75681
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luakeys.sty)
Requires:       tex(setspace.sty)
Provides:       tex(cloze-doc.tex) = %{tl_version}
Provides:       tex(cloze.sty) = %{tl_version}
Provides:       tex(cloze.tex) = %{tl_version}

%description -n texlive-cloze
This is a LuaTeX or LuaLaTeX package for generating cloze texts. The main
feature of the package is that the formatting doesn't change when using the
hide and show options. There are the commands \cloze, \clozefix, \clozefil,
\clozenol, \clozestrike and the environments clozepar and clozebox to generate
cloze texts.

%package -n texlive-combofont
Summary:        Add NFSS-declarations of combo fonts to LuaLaTeX documents
Version:        svn51348
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xfp.sty)
Requires:       tex(xparse.sty)
Provides:       tex(combofont.sty) = %{tl_version}

%description -n texlive-combofont
This highly experimental package can be used to add NFSS-declarations of combo
fonts to LuaLaTeX documents. This package may disappear without notice, e.g. if
luaotfload changes in a way so that it no longer works, or if LuaTeX changes,
or if fontspec itself includes the code. It is also possible that the package's
syntax and commands may change in an incompatible way. So if you use it in a
production environment: You have been warned.

%package -n texlive-cstypo
Summary:        Czech typography rules enforced through LuaTeX hooks
Version:        svn41986
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Provides:       tex(cstypo-tex.tex) = %{tl_version}
Provides:       tex(cstypo.sty) = %{tl_version}

%description -n texlive-cstypo
This package provides macros that enforce basic Czech typography rules through
Lua hooks available in LuaTeX.

%package -n texlive-ctablestack
Summary:        Catcode table stable support
Version:        svn38514
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ctablestack.sty) = %{tl_version}

%description -n texlive-ctablestack
This package provides a method for defining category code table stacks in
LuaTeX. It builds on code provided by the 2015/10/01 release of LaTeX2e (also
available as ltluatex.sty for plain users). It is required by the luatexbase
package (v1.0 onward) which uses ctablestack to provide a back-compatibility
form of this concept.

%package -n texlive-ekdosis
Summary:        Typesetting TEI-xml compliant Critical Editions
Version:        svn69568
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(expkv-def.sty)
Requires:       tex(expkv-opt.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(iftex.sty)
Requires:       tex(keyfloat.sty)
Requires:       tex(lineno.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(luacode.sty)
Requires:       tex(paracol.sty)
Requires:       tex(parnotes.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(refcount.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(trivfloat.sty)
Requires:       tex(verse.sty)
Requires:       tex(zref-abspage.sty)
Requires:       tex(zref-user.sty)
Provides:       tex(ekdosis.sty) = %{tl_version}

%description -n texlive-ekdosis
ekdosis is a LuaLaTeX package designed for multilingual critical editions. It
can be used to typeset texts and different layers of critical notes in any
direction accepted by LuaTeX. Texts can be arranged in running paragraphs or on
facing pages, in any number of columns which in turn can be synchronized or
not. In addition to printed texts, ekdosis can convert .tex source files so as
to produce TEI xml-compliant critical editions. Database-driven encoding under
LaTeX then allows extraction of texts entered segment by segment according to
various criteria: main edited text, variant readings, translations or annotated
borrowings between texts.

%package -n texlive-emoji
Summary:        Emoji support in (Lua)LaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(emoji-table.def) = %{tl_version}
Provides:       tex(emoji.sty) = %{tl_version}

%description -n texlive-emoji
This package allows users to typeset emojis in LaTeX documents. It requires the
LuaHBTeX engine, which can be called by lualatex since TeX Live 2020, or
lualatex-dev in TeX Live 2019.

%package -n texlive-emojicite
Summary:        Add emojis to citations
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(emoji.sty)
Requires:       tex(natbib.sty)
Requires:       tex(xparse.sty)
Provides:       tex(emojicite.sty) = %{tl_version}

%description -n texlive-emojicite
This package adds emojis to citations.

%package -n texlive-enigma
Summary:        Encrypt documents with a three rotor Enigma
Version:        svn29802
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexbase.sty)
Provides:       tex(enigma.sty) = %{tl_version}
Provides:       tex(enigma.tex) = %{tl_version}

%description -n texlive-enigma
The package provides historical encryption (Enigma cipher) for LuaTeX-based
formats.

%package -n texlive-fancymag
Summary:        A LuaLaTeX package for academic magazines and scientific
Version:        svn75720
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(balance.sty)
Requires:       tex(calligra.sty)
Requires:       tex(caption.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(everypage-1x.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(lettrine.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pdfrender.sty)
Requires:       tex(shadowtext.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
Provides:       tex(fancymag.sty) = %{tl_version}

%description -n texlive-fancymag
fancymag is a LaTeX package designed to provide enhanced typographic styling
for academic and editorial documents. It integrates a selection of freely
licensed display fonts to help authors create visually appealing layouts for
magazines, scientific books, and other publication-quality material. The
package must be compiled with LuaLaTeX and depends on OpenType fonts included
in the package. To function correctly, the accompanying fonts/ and img/
directories must be present, as described in the documentation.

%package -n texlive-farbe
Summary:        Color management (conversion, names) for LuaTeX implemented in Lua
Version:        svn75449
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(farbe.sty) = %{tl_version}
Provides:       tex(farbe.tex) = %{tl_version}

%description -n texlive-farbe
This package is mainly a Lua library for converting and manipulating colors. It
is based on Lua module lua-color.

%package -n texlive-gitinfo-lua
Summary:        Display git project information in your LaTeX projects
Version:        svn72284
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfopts.sty)
Provides:       tex(gitinfo-lua.sty) = %{tl_version}

%description -n texlive-gitinfo-lua
This project aims to display git project information in PDF documents. It is
mostly written in Lua for executing the git commands, thereby making this
package only applicable for LuaLaTeX with shell escape enabled. If LuaLaTeX
isn't working for you, you could try gitinfo2 instead. For LaTeX, a set of
standard macros is provided for displaying basic information or setting the
project directory, and a set of advanced macros for formatting commits and
tags.

%package -n texlive-ideavault
Summary:        Idea (concept) management package
Version:        svn74773
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bookmark.sty)
Requires:       tex(luacode.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(needspace.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(ideavault.sty) = %{tl_version}

%description -n texlive-ideavault
This LuaLaTeX package provides tools for the management (i.e. creation and
printing) of ideas (i.e. pieces of LaTeX code representing concepts). It
supports dependencies, nested idea printing and tags, and can be useful for
writing rulebooks or handbooks with many definitions.

%package -n texlive-innerscript
Summary:        Small modifications to math formatting
Version:        svn75161
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(innerscript.sty) = %{tl_version}

%description -n texlive-innerscript
This package optionally modifies four aspects of TeX's automatic math
formatting to improve typesetting: (1) it adds extra space around relation and
operation symbols in superscripts and subscripts; (2) it removes extra space
around \left-\right delimiter pairs; (3) it adds extra space after right
delimiters in certain situations; and (4) it forces \left and \right delimiters
to completely cover their contents. Using LuaLaTeX is required.

%package -n texlive-interpreter
Summary:        Translate input files on the fly
Version:        svn27232
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(interpreter.sty) = %{tl_version}
Provides:       tex(interpreter.tex) = %{tl_version}

%description -n texlive-interpreter
The package preprocesses input files to a Lua(La)TeX run, on the fly. The user
defines Lua regular expressions to search for patterns and modify input lines
(or entire paragraphs) accordingly, before TeX reads the material. In this way,
documents may be prepared in a non-TeX language (e.g., some lightweight markup
language) and turned into 'proper' TeX for processing. The source of the
documentation is typed in such a lightweight language and is thus easily
readable in a text editor (the PDF file is also available, of course); the
transformation to TeX syntax via Interpreter's functions is explained in the
documentation itself. Interpreter is implemented using the author's gates (lua
version), and works for plain TeX and LaTeX, but not ConTeXt.

%package -n texlive-kanaparser
Summary:        Kana parser for LuaTeX
Version:        svn48052
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(kanaparser.tex) = %{tl_version}

%description -n texlive-kanaparser
The package provides a kana parser for LuaTeX. It is a set of 4 macros that
handle transliteration of text: from hiragana and katakana to Latin from Latin
and katakana to hiragana from Latin and hiragana to katakana It can be used to
write kana directly using only the ASCII character set or for education
purposes. The package has support for obsolete and rarely used syllables, some
only accessible via the provided toggle macro.

%package -n texlive-kkluaverb
Summary:        Provides a Lua-enhanced versatile \verb command
Version:        svn77516
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(KKluaverb.sty) = %{tl_version}

%description -n texlive-kkluaverb
This package provides a Lua-enhanced command similar to \verb, as well as an
environment similar to lstlisting. These can be safely used in the arguments of
arbitrary commands without breaking, and they work correctly in the table of
contents and indexes. The package also allows the creation of an arbitrary
number of text-replacement rules and color presets.

%package -n texlive-kkran
Summary:        Generate answer fields in tests and exams
Version:        svn77172
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(KKsymbols.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexja-fontspec.sty)
Requires:       tex(luatexja-preset.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(KKran.sty) = %{tl_version}

%description -n texlive-kkran
A Lua- and TikZ-based package created for the Japanese education sector. It
enables the arrangement of box-shaped answer fields in any desired combination
using simple commands. It also facilitates the easy creation of multiple-choice
answer sheets (mark sheets). Furthermore, it covers the functionality of
toggling the display of model answers (solutions) via an option, and even the
creation of grid-style answer fields (graph paper-like cells). The package name
originates from "Lan (:ran)", which means "a small piece of area", or "a small
space".

%package -n texlive-kksymbols
Summary:        LaTeX commands for enclosing characters in circles, squares, diamonds, or brackets
Version:        svn77427
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(luatexja-adjust.sty)
Requires:       tex(tikz.sty)
Provides:       tex(KKsymbols.sty) = %{tl_version}

%description -n texlive-kksymbols
This package offers LaTeX commands for enclosing characters in circles,
squares, diamonds, or brackets, with automatic scaling and baseline correction
to ensure correct appearance in both horizontal and vertical writing modes. The
package relies on TikZ and works only with LuaLaTeX.

%package -n texlive-ligtype
Summary:        Comprehensive ligature suppression functionalities
Version:        svn67601
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(ligtype.sty) = %{tl_version}

%description -n texlive-ligtype
This package suppresses inappropriate ligatures following specified rules. Both
font and user kerning are applied correctly, and f-glyphs are automatically
replaced with their short-arm variant (if available). Also there is an emphasis
on speed. By default the package applies German language ligature suppression
rules. With the help of options and macros it can be used for other languages
as well. The package requires LuaLaTeX.

%package -n texlive-linebreaker
Summary:        Prevent overflow boxes with LuaLaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexbase.sty)
Provides:       tex(linebreaker.sty) = %{tl_version}

%description -n texlive-linebreaker
This package tries to prevent overflow lines in paragraphs or boxes. It changes
LuaTeX's \linebreak callback and re-typesets the paragraph with increased
values of \tolerance and \emergencystretch until the overflow no longer
happens. If that doesn't help, it chooses the solution with the lowest badness.

%package -n texlive-longmath
Summary:        Nested delimiter groups extending over multiple array cells or lines
Version:        svn71709
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexbase.sty)
Provides:       tex(longmath.sty) = %{tl_version}

%description -n texlive-longmath
This package provides yet another solution to some well known typesetting
problems solved in a variety of ways: multi line formulas with paired and
nested delimiters. It tackles the problem at the Lua level, which has some
advantages over solutions implemented in TeX. In particular, the TeX code need
not be executed multiple times, and there is no interference between TeX
grouping and the nesting of delimiter groups. As a byproduct, delimiters can be
scaled in various ways, inner delimiters come in different flavours like
relational and binary operators, punctuation symbols etc., and outer delimiters
can be selected automatically according to the nesting level. Last but not
least, delimiter groups can even extend across several array cells or across
the whole document. A special environment is provided as well, which allows
multi line expressions to be placed inside a displayed equation and make TeX do
the line splitting and alignment.

%package -n texlive-lparse
Summary:        Parse macro arguments with Lua using xparse-like specification
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lparse.sty) = %{tl_version}
Provides:       tex(lparse.tex) = %{tl_version}

%description -n texlive-lparse
The name lparse is derived from xparse. The 'x' has been replaced by an 'l'
because this package only works with LuaTeX. 'l' stands for "Lua". Just as with
xparse, it is possible to use a special syntax consisting of single letters to
express the arguments of a macro. However, lparse is able to read arguments
regardless of the macro system used -- whether LaTeX, or ConTeXt, or even plain
TeX. Of course, LuaTeX must always be used as the engine.

%package -n texlive-lt3luabridge
Summary:        Execute Lua code in any TeX engine that exposes the shell
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lt3luabridge.sty) = %{tl_version}
Provides:       tex(lt3luabridge.tex) = %{tl_version}
Provides:       tex(t-lt3luabridge.tex) = %{tl_version}

%description -n texlive-lt3luabridge
This is an expl3(-generic) package for plain TeX, LaTeX, and ConTeXt that
allows you to execute Lua code in LuaTeX or any other TeX engine that exposes
the shell.

%package -n texlive-lua-placeholders
Summary:        Specifying placeholders for demonstration purposes
Version:        svn70850
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xspace.sty)
Provides:       tex(lua-placeholders.sty) = %{tl_version}

%description -n texlive-lua-placeholders
This package is meant for setting parameters in a LuaLaTeX document in a more
programmatic way with YAML. Parameters can be specified by adding a "recipe"
file. These recipe files describe the parameter's type, placeholders and/or
default values. From thereon, the placeholders can be displayed in the document
and an "example" document can be created. An "actual copy" document can be
created by loading additional "payload" files, which all must correspond to a
recipe file.

%package -n texlive-lua-tinyyaml
Summary:        A tiny YAML (subset) parser in pure Lua
Version:        svn73671
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lua-tinyyaml
This package provides a YAML (subset) parser written in pure Lua. It supports a
subset of the YAML 1.2 specifications. It is required by several other LuaTeX
packages including markdown and citeproc-lua.

%package -n texlive-lua-typo
Summary:        Highlighting typographical flaws with LuaLaTeX
Version:        svn77296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atveryend.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luacolor.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(lua-typo-2021-04-18.sty) = %{tl_version}
Provides:       tex(lua-typo-2023-03-08.sty) = %{tl_version}
Provides:       tex(lua-typo.sty) = %{tl_version}

%description -n texlive-lua-typo
Prints the list of pages on which typographical flaws were found (i.e. widows,
orphans, hyphenated words split across two pages, consecutive lines ending with
hyphens, paragraphs ending on too short or nearly full lines, homeoarchy, etc).
Customisable colours are used to highlight these flaws.

%package -n texlive-lua-uca
Summary:        Unicode Collation Algorithm library for Lua
Version:        svn74807
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lua-uca
The Lua-UCA library provides basic support for Unicode Collation Algorithm in
Lua. It can be used to sort arrays of strings according to rules of particular
languages. It can be used in other Lua projects that need to sort text in a
language dependent way, like indexing processors, bibliographic generators,
etc.

%package -n texlive-lua-ul
Summary:        Underlining for LuaLaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(luacolor.sty)
Provides:       tex(docstrip-luacode.sty) = %{tl_version}
Provides:       tex(lua-ul.sty) = %{tl_version}

%description -n texlive-lua-ul
This package provides underlining, strikethough, and highlighting using
features in LuaLaTeX which avoid the restrictions imposed by other methods. In
particular, kerning is not affected, the underlined text can use arbitrary
commands, hyphenation works etc. The package requires LuaTeX version [?]
1.12.0.

%package -n texlive-lua-visual-debug
Summary:        Visual debugging with LuaLaTeX
Version:        svn77207
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Provides:       tex(lua-visual-debug.sty) = %{tl_version}

%description -n texlive-lua-visual-debug
The package uses lua code to provide visible indications of boxes, glues, kerns
and penalties in the PDF output. The package is known to work in LaTeX and
Plain TeX documents.

%package -n texlive-lua-widow-control
Summary:        Automatically remove widows and orphans from any document
Version:        svn76924
License:        MPL-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(microtype.sty)
Provides:       tex(lua-widow-control-2022-02-22.sty) = %{tl_version}
Provides:       tex(lua-widow-control.sty) = %{tl_version}
Provides:       tex(lua-widow-control.tex) = %{tl_version}

%description -n texlive-lua-widow-control
Unmodified TeX has very few ways of preventing widows and orphans. In documents
with figures, section headings, and equations, TeX can stretch the vertical
glue between items in order to prevent widows and orphans, but many documents
have no figures or headings. TeX can also shorten the page by 1 line, but this
will give each page a different length which can make a document look uneven.
The typical solution is to strategically insert \looseness=1, but this requires
manual editing every time that the document is edited. Lua-widow-control is
essentially an automation of the \looseness method: it uses Lua callbacks to
find "stretchy" paragraphs, then it lengthens them to remove widows and
orphans. Lua-widow-control is compatible with all LuaTeX and LuaMetaTeX-based
formats. All that is required is to load the package at the start of your
document. To load: Plain LuaTeX: \input lua-widow-control LuaLaTeX:
\usepackage{lua-widow-control} ConTeXt: \usemodule[lua-widow-control] OpTeX:
\load[lua-widow-control]

%package -n texlive-luaaddplot
Summary:        An extension to pgfplots' \addplot macro
Version:        svn72350
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(luaaddplot.sty) = %{tl_version}
Provides:       tex(luaaddplot.tex) = %{tl_version}

%description -n texlive-luaaddplot
This package is an extension to pgfplots. It extends the \addplot macro by a
facility which allows modification of data files while they are read. With
luaaddplot it is no longer necessary to pre-process data files generated by
measuring devices with external scripts. This package can be used with plain
LuaTeX or LuaLaTeX.

%package -n texlive-luacas
Summary:        A computer algebra system for users of LuaLaTeX
Version:        svn67247
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(luacode.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(luacas.sty) = %{tl_version}

%description -n texlive-luacas
This package provides a portable computer algebra system capable of symbolic
computation, written entirely in Lua, designed for use in LuaLaTeX. Features
include: arbitrary-precision integer and rational arithmetic, factoring of
univariate polynomials over the rationals and finite fields, number theoretic
algorithms, symbolic differentiation and integration, and more. The target
audience for this package are mathematics students, instructors, and
professionals who would like some ability to perform basic symbolic
computations within LaTeX without the need for laborious and technical setup.

%package -n texlive-luacensor
Summary:        Securely redact sensitive information using Lua
Version:        svn71922
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accsupp.sty)
Requires:       tex(environ.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(luacode.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(luacensor.sty) = %{tl_version}

%description -n texlive-luacensor
This package provides simple tools for creating redacted Its tools are useful
for lawyers, workers in sensitive industries, and others who need to easily
produce both unrestricted versions of documents (for limited, secure release)
and restricted versions of documents (for general release) Redaction is done
both by hiding all characters and by slightly varying the length of strings to
prevent jigsaw identification. It also is friendly to screen readers by adding
alt-text indicating redacted content.

%package -n texlive-luacode
Summary:        Helper for executing lua code from within TeX
Version:        svn25193
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(luacode.sty) = %{tl_version}

%description -n texlive-luacode
Executing Lua code from within TeX with directlua can sometimes be tricky:
there is no easy way to use the percent character, counting backslashes may be
hard, and Lua comments don't work the way you expect. The package provides the
\luaexec command and the luacode(*) environments to help with these problems.

%package -n texlive-luacolor
Summary:        Color support based on LuaTeX's node attributes
Version:        svn67987
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(color.sty)
Provides:       tex(luacolor.sty) = %{tl_version}

%description -n texlive-luacolor
This package implements color support based on LuaTeX's node attributes.

%package -n texlive-luacomplex
Summary:        Operations on complex numbers inside LaTeX documents using Lua
Version:        svn68883
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luamaths.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luacomplex.sty) = %{tl_version}

%description -n texlive-luacomplex
The luacomplex package is developed to define complex numbers and perform basic
arithmetic on complex numbers in LaTeX. It also loads the luamathspackage. It
provides an easy way to define complex numbers and perform operations on
complex numbers. There is no particular environment for performing operations
on complex numbers. The package commands can be used in any environment
(including the mathematics environment). It is written in Lua, and the .tex
file is to be compiled with the LuaLaTeX engine.

%package -n texlive-luagcd
Summary:        Computation of gcd of integers inside LaTeX using Lua
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Provides:       tex(luagcd.sty) = %{tl_version}

%description -n texlive-luagcd
Using Lua, the luagcd package is developed to find the greatest common divisor
(gcd) of integers in LaTeX. The package provides commands to obtain
step-by-step computation of gcd of two integers by using the Euclidean
algorithm. In addition, the package has the command to express gcd of two
integers as a linear combination. The Bezout's Identity can be verified for any
two integers using commands in the package. No particular environment is
required for the use of commands in the package. It is written in Lua, and the
TeX file has to be compiled with the LuaLaTeX engine.

%package -n texlive-luahttp
Summary:        Compile-time internet-interactive PDF-documents using Lua and LuaTeX
Version:        svn67348
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(url.sty)
Requires:       tex(xparse.sty)
Provides:       tex(luahttp.sty) = %{tl_version}

%description -n texlive-luahttp
This small package provides five commands to make HTTP requests using Lua and
LuaTeX. Functionalities include API calls, fetch RSS feeds and the possibility
to include images using a link. These commands run during the compilation of
the PDF-Document and may require user interaction.

%package -n texlive-luahyphenrules
Summary:        Loading patterns in LuaLaTeX with language.dat
Version:        svn56200
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(luahyphenrules.sty) = %{tl_version}

%description -n texlive-luahyphenrules
Preloading hyphenation patterns (or 'hyphen rules.) into any format based upon
LuaTeX is not required in LuaTeX and recent releases of babel don't do it
anyway. This package is addressed to those who just want to select the
languages and load their patterns by means of `language.dat` without loading
`babel`.

%package -n texlive-luaimageembed
Summary:        Embed images as base64-encoded strings
Version:        svn50788
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Provides:       tex(luaimageembed.sty) = %{tl_version}

%description -n texlive-luaimageembed
This package allows to embed images directly as base64-encoded strings into an
LuaLaTeX document. This can be useful, e. g. to package a document with images
into a single TeX file, or with automatically generated graphics.

%package -n texlive-luaindex
Summary:        Create index using LuaLaTeX
Version:        svn25882
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase-compat.sty)
Requires:       tex(luatexbase-modutils.sty)
Requires:       tex(scrbase.sty)
Provides:       tex(luaindex.sty) = %{tl_version}

%description -n texlive-luaindex
Luaindex provides (yet another) index processor, written in Lua.

%package -n texlive-luainputenc
Summary:        Replacing inputenc for use in LuaTeX
Version:        svn75712
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(luatexbase.sty)
# Ignoring dependency on xetex-inputenc.sty - not part of TeX Live
Provides:       tex(luainputenc.sty) = %{tl_version}
Provides:       tex(lutf8.def) = %{tl_version}
Provides:       tex(lutf8x.def) = %{tl_version}

%description -n texlive-luainputenc
LuaTeX operates by default in UTF-8 input; thus LaTeX documents that need 8-bit
character-sets need special treatment. (In fact, LaTeX documents using UTF-8
with "traditional" -- 256-glyph -- fonts also need support from this package.)
The package, therefore, replaces the LaTeX standard inputenc for use under
LuaTeX. With a current LuaTeX, the package has the same behaviour with LuaTeX
as inputenc has under pdfTeX.

%package -n texlive-luakeys
Summary:        A Lua module for parsing key-value options
Version:        svn75824
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(luakeys-debug.sty) = %{tl_version}
Provides:       tex(luakeys-debug.tex) = %{tl_version}
Provides:       tex(luakeys.sty) = %{tl_version}
Provides:       tex(luakeys.tex) = %{tl_version}

%description -n texlive-luakeys
This package provides a Lua module that can parse key-value options like the
TeX packages keyval, kvsetkeys, kvoptions, xkeyval, pgfkeys etc. luakeys,
however, accomplishes this task entirely by using the Lua language and does not
rely on TeX. Therefore this package can only be used with the TeX engine
LuaTeX. Since luakeys uses LPeg, the parsing mechanism should be pretty robust.

%package -n texlive-luakeyval
Summary:        A minimal key/value system for LuaTeX based on token.scan_key_cs
Version:        svn76992
License:        0BSD
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-luakeyval
luakeyval is a Lua module that helps defining macros which accepts key/val
lists by scanning the input stream with token.scan_key_cs. This is helpfull for
creating use interface macros from within a Lua module.

%package -n texlive-lualatex-math
Summary:        Fixes for mathematics-related LuaLaTeX issues
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       texlive-filehook
Provides:       tex(lualatex-math.sty) = %{tl_version}

%description -n texlive-lualatex-math
The package patches a few commands of the LaTeX2e kernel and the amsmath and
mathtools packages to be more compatible with the LuaTeX engine. It is only
meaningful for LuaLaTeX documents containing mathematical formulas, and does
not exhibit any new functionality. The fixes are mostly moved from the
unicode-math package to this package since they are not directly related to
Unicode mathematics typesetting.

%package -n texlive-lualatex-truncate
Summary:        A wrapper for using the truncate package with LuaLaTeX
Version:        svn67201
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(truncate.sty)
Provides:       tex(lualatex-truncate.sty) = %{tl_version}

%description -n texlive-lualatex-truncate
This package provides a wrapper for the truncate package, thus fixing issues
related to LuaTeX's hyphenation algorithm.

%package -n texlive-lualibs
Summary:        Additional Lua functions for LuaTeX macro programmers
Version:        svn67994
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lualibs
Lualibs is a collection of Lua modules useful for general programming. The
bundle is based on lua modules shipped with ConTeXt, and made available in this
bundle for use independent of ConTeXt.

%package -n texlive-lualinalg
Summary:        A linear algebra package for LuaLaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luamaths.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(lualinalg.sty) = %{tl_version}

%description -n texlive-lualinalg
The lualinalg package is developed to perform operations on vectors and
matrices defined over the field of real or complex numbers inside LaTeX
documents. It provides flexible ways for defining and displaying vectors and
matrices. No particular environment of LaTeX is required to use commands in the
package. The package is written in Lua, and tex file is to be compiled with the
LuaLaTeX engine. The time required for calculations is not an issue while
compiling with LuaLaTeX. There is no need to install Lua on the user's system
as TeX distributions (TeX Live or MiKTeX) come bundled with LuaLaTeX. It may
also save users' efforts to copy vectors and matrices from other software
(which may not be in LaTeX-compatible format) and to use them in a tex file.
The vectors and matrices of reasonable size can be handled with ease. The
package can be modified or extended by writing custom Lua programs.

%package -n texlive-luamathalign
Summary:        More flexible alignment in amsmath environments
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(luamathalign.sty) = %{tl_version}

%description -n texlive-luamathalign
Allow aligning mathematical expressions on points where directly using & is not
possible, especially in nested macros or environments.

%package -n texlive-luamaths
Summary:        Provide standard mathematical operations inside LaTeX documents using Lua
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(luacode.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luamaths.sty) = %{tl_version}

%description -n texlive-luamaths
The luamaths package is developed to perform standard mathematical operations
inside LaTeX documents using Lua. It provides an easy way to perform standard
mathematical operations. There is no particular environment in the package for
performing mathematical operations. The package commands can be used in any
environment (including the mathematics environment). There is no need to
install Lua on users system as TeX distributions (TeX Live or MiKTeX) come
bundled with LuaLaTeX.

%package -n texlive-luamml
Summary:        Automatically generate MathML from LuaLaTeX math mode material
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(luamml-patches-amsmath.sty) = %{tl_version}
Provides:       tex(luamml-patches-kernel.sty) = %{tl_version}
Provides:       tex(luamml-pdf.sty) = %{tl_version}
Provides:       tex(luamml.sty) = %{tl_version}

%description -n texlive-luamml
LuaMML is an experimental package to automatically generate a MathML
representation of mathematical expressions written in LuaLaTeX documents. These
MathML representations can be used for improving accessibility or to ease
conversion into new output formats like HTML.

%package -n texlive-luamodulartables
Summary:        Generate modular addition and multiplication tables
Version:        svn68893
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luamodulartables.sty) = %{tl_version}

%description -n texlive-luamodulartables
This package is developed to generate modular addition and multiplication
tables for positive integers. It provides an easy way to generate modular
addition and modular multiplication tables for positive integers in LaTeX
documents. The commands in the package have optional arguments for the
formatting of tables. These commands can be used in an environment similar to a
tabular or array environment. The commands can also be used with the booktabs
package, which provides nice formatting of tables in LaTeX. It is written in
Lua, and TeX file is to be compiled with LuaLaTeX engine.

%package -n texlive-luamplib
Summary:        Use LuaTeX's built-in MetaPost interpreter
Version:        svn77524
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(luamplib.sty) = %{tl_version}

%description -n texlive-luamplib
The package enables the user to specify MetaPost diagrams (which may include
colour specifications from the color or xcolor packages) into a document, using
LuaTeX's built-in MetaPost library. The facility is only available in PDF mode.

%package -n texlive-luaoptions
Summary:        Option handling for LuaLaTeX packages
Version:        svn64870
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luaotfload.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luaoptions.sty) = %{tl_version}

%description -n texlive-luaoptions
This LuaLaTeX package provides extensive support for handling options, on
package level and locally. It allows the declaration of sets of options, along
with defaults, expected/allowed values and limited type checking. These options
can be enforced as package options, changed at any point during a document, or
overwritten locally by optional macro arguments. It is also possible to
instantiate an Options object as an independent Lua object, without linking it
to a package. Luaoptions can be used to enforce and prepopulate options, or it
can be used to simply handle the parsing of optional key=value arguments into
proper Lua tables.

%package -n texlive-luapackageloader
Summary:        Allow LuaTeX to load external Lua packages
Version:        svn54779
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-iftex
Requires:       tex(ifluatex.sty)
Provides:       tex(luapackageloader.sty) = %{tl_version}

%description -n texlive-luapackageloader
This package allows LuaTeX to load packages from the default package.path and
package.cpath locations. This could be useful to load external Lua modules,
including modules installed via LuaRocks. This package requires ifluatex.

%package -n texlive-luaplot
Summary:        Plotting graphs using Lua
Version:        svn68918
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luaplot.sty) = %{tl_version}

%description -n texlive-luaplot
This package uses Lua to plot graphs of real-valued functions of a real
variable in LaTeX. It furthermore makes use of the MetaPost system as well as
the luamplib and luacode packages. It provides an easy way for plotting graphs
of standard mathematical functions. There is no particular environment in the
package for plotting graphs. It also works inside LaTeX floating environments,
like tables and figures. The compilation time for plotting several graphs in
LaTeX using this package is significantly less with the LuaLaTeX engine. The
package is based on the core idea of loading mathematical functions inside Lua
and determining plot points using different methods available in Lua. After
determining plot points in Lua, two different approaches are used: Pass plot
points to the MetaPost system via luamplib. Pass plot points to the TikZ
package.

%package -n texlive-luaprogtable
Summary:        Programmable table interface for LuaLaTeX
Version:        svn56113
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xparse.sty)
Provides:       tex(luaprogtable.sty) = %{tl_version}

%description -n texlive-luaprogtable
This package allows you to modify a cell based on the contents of other cells
using LaTeX macros.

%package -n texlive-luaquotes
Summary:        Smart setting of quotation marks
Version:        svn65652
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(luacode.sty)
Provides:       tex(luaquotes.sty) = %{tl_version}

%description -n texlive-luaquotes
This package automatically generates quotation marks and punctuation depending
on the selected language.

%package -n texlive-luarandom
Summary:        Create lists of random numbers
Version:        svn68847
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(luacode.sty)
Provides:       tex(luarandom.sty) = %{tl_version}

%description -n texlive-luarandom
This package can create lists of random numbers for any given interval [a;b].
It is possible to get lists with or without multiple numbers. The random
generator will be initialized by the system time. The package can only be used
with LuaLaTeX!

%package -n texlive-luaset
Summary:        Set Operations inside LaTeX documents using Lua
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luamaths.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luaset.sty) = %{tl_version}

%description -n texlive-luaset
The luaset package is developed to define finite sets and perform operations on
them inside LaTeX documents. There is no particular environment in the package
for performing set operations. The package commands can be used in any
environment (including the mathematics environment). It is written in Lua, and
the .tex file is to be compiled with the LuaLaTeX engine. The time required for
operations on sets is not an issue while compiling with the LuaLaTeX engine.
There is no need to install Lua on the users system as TeX distributions (TeX
Live or MiKTeX) come bundled with LuaLaTeX.

%package -n texlive-luatbls
Summary:        Lua tables made accessible in LaTeX
Version:        svn73999
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Requires:       tex(luakeys.sty)
Requires:       tex(penlightplus.sty)
Provides:       tex(luatbls.sty) = %{tl_version}

%description -n texlive-luatbls
This package provides a LaTeX interface to create, modify, and use the Lua data
structure >>tables<<. Lua tables can be declared with the help of luakeys, and
this package provides facilities to set, get, check, iterate, apply, etc. to
the table.

%package -n texlive-luatex-type-definitions
Summary:        Type definitions for the Lua API of LuaTeX
Version:        svn75890
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-luatex-type-definitions
LuaTeX has a very large Lua API. This project tries to make this API accessible
in the text editor of your choice. This is made possible by the
lua-language-server -- a server that implements the Language Server Protocol
(LSP) for the Lua language. Features such as code completion, syntax
highlighting, and marking of warnings and errors should therefore not only be
possible in Visual Studio Code, but in a large number of editors that support
the LSP.

%package -n texlive-luatex85
Summary:        PdfTeX aliases for LuaTeX
Version:        svn41456
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(luatex85.sty) = %{tl_version}

%description -n texlive-luatex85
The package provides emulation of pdfTeX primitives for LuaTeX v0.85+.

%package -n texlive-luatexbase
Summary:        Basic resource management for LuaTeX code
Version:        svn52663
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-ctablestack
Requires:       tex(ctablestack.sty)
Provides:       tex(luatexbase-attr.sty) = %{tl_version}
Provides:       tex(luatexbase-cctb.sty) = %{tl_version}
Provides:       tex(luatexbase-compat.sty) = %{tl_version}
Provides:       tex(luatexbase-loader.sty) = %{tl_version}
Provides:       tex(luatexbase-mcb.sty) = %{tl_version}
Provides:       tex(luatexbase-modutils.sty) = %{tl_version}
Provides:       tex(luatexbase-regs.sty) = %{tl_version}
Provides:       tex(luatexbase.sty) = %{tl_version}

%description -n texlive-luatexbase
The LaTeX kernel (LaTeX2e 2015/10/01 onward) builds in support for LuaTeX
functionality, also available as ltluatex.tex for users of plain TeX and those
with older LaTeX kernel implementations. This support is based on ideas taken
from the original luatexbase package, but there are interface differences. This
'stub' package provides a compatibility layer to allow existing packages to
upgrade smoothly to the new support structure.

%package -n texlive-luatexko
Summary:        Typeset Korean with Lua(La)TeX
Version:        svn77490
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(kolabels-utf.sty)
Provides:       tex(luatexko.sty) = %{tl_version}

%description -n texlive-luatexko
This is a Lua(La)TeX macro package that supports typesetting Korean documents
including Old Hangul texts. As LuaTeX has opened up access to almost all the
hidden routines of TeX engine, users can obtain more beautiful outcome using
this package rather than other Hangul macros operating on other engines. LuaTeX
version 1.10+ and luaotfload version 2.96+ are required for this package to
run. This package also requires the cjk-ko package for its full functionality.

%package -n texlive-luatextra
Summary:        Additional macros for Plain TeX and LaTeX in LuaTeX
Version:        svn20747
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(metalogo.sty)
Provides:       tex(luatextra.sty) = %{tl_version}

%description -n texlive-luatextra
The package provides a coherent extended programming environment for use with
LuaTeX. It loads packages fontspec, luatexbase and lualibs, and provides
additional user-level features and goodies. The package is under development,
and its specification may be expected to change.

%package -n texlive-luatikz
Summary:        A 2D graphics library to draw TikZ graphics using the Lua programming language
Version:        svn73087
License:        LPPL-1.3c AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Provides:       tex(luatikz.sty) = %{tl_version}

%description -n texlive-luatikz
This package provides a comfort graphics library to work with graphic objects
as immutables in the Lua programming language. It writes code for the TikZ
package. It overloads operators, so you can use standard math expressions to
work with graphical objects. There probably isn't anything that couldn't been
done just as well with pgfmath and TikZ directly. However, if a graphic gets
more complicated, Lua may just be easier to work with as base.

%package -n texlive-luatruthtable
Summary:        Generate truth tables of boolean values in LuaLaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(luacode.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luatruthtable.sty) = %{tl_version}

%description -n texlive-luatruthtable
This package provides an easy way for generating truth tables of boolean values
in LuaLaTeX. The time required for operations is no issue while compiling with
LuaLaTeX. The package supports nesting of commands for multiple operations. It
can be modified or extended by writing custom lua programs. There is no need to
install lua on users system as TeX distributions (TeX Live or MiKTeX) come
bundled with LuaLaTeX.

%package -n texlive-luavlna
Summary:        Prevent line breaks after single letter words, units, or academic titles
Version:        svn76687
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(luavlna.sty) = %{tl_version}
Provides:       tex(luavlna.tex) = %{tl_version}

%description -n texlive-luavlna
In some languages, like Czech or Polish, there should be no single letter words
at the end of a line, according to typographical norms. This package handles
such situations using LuaTeX's callback mechanism. In doing this, the package
can detect languages used in the text and insert spaces only in parts of the
document where languages requiring this feature are used. Another feature of
this package is the inclusion of non-breakable space after initials (like in
personal names), after or before academic degrees, and between numbers and
units. The package supports both plain LuaTeX and LuaLaTeX. BTW: "vlna" is the
Czech word for "wave" or "curl" and also denotes the tilde which, in TeX, is
used for "unbreakable spaces".

%package -n texlive-luaxml
Summary:        Lua library for reading and serialising XML files
Version:        svn77537
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Provides:       tex(luaxml.sty) = %{tl_version}

%description -n texlive-luaxml
LuaXML is a pure Lua library for reading and serializing XML files. The current
release is aimed mainly at support for the odsfile package. The documentation
was created by automatic conversion of original documentation in the source
code.

%package -n texlive-lutabulartools
Summary:        Some useful LuaLaTeX-based tabular tools
Version:        svn73345
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(longtable.sty)
Requires:       tex(luacode.sty)
Requires:       tex(makecell.sty)
Requires:       tex(multirow.sty)
Requires:       tex(penlightplus.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(lutabulartools.sty) = %{tl_version}

%description -n texlive-lutabulartools
This package provides some useful commands for tabular matter. It uses LuaLaTeX
and offers the ability to combine the facilities of multirow and makecell with
an easy to use syntax. It also adds some enhanced rules for the booktabs
package.

%package -n texlive-marginalia
Summary:        Non-floating marginal content with automatic placement for LuaLaTeX
Version:        svn77235
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(marginalia.sty) = %{tl_version}

%description -n texlive-marginalia
This LuaLaTeX package allows the placement of marginal content anywhere,
without \marginpar's limits, and automatically adjusts positions to prevent
overlaps or content being pushed off the page, and offers key-value settings
that allow fine-grained customization.

%package -n texlive-minim
Summary:        A modern plain format for the LuaTeX engine
Version:        svn73816
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(minim-alloc.tex) = %{tl_version}
Provides:       tex(minim-doc.sty) = %{tl_version}
Provides:       tex(minim-etex.tex) = %{tl_version}
Provides:       tex(minim-lmodern.tex) = %{tl_version}
Provides:       tex(minim-pdfresources.tex) = %{tl_version}
Provides:       tex(minim-plain.tex) = %{tl_version}
Provides:       tex(minim.tex) = %{tl_version}

%description -n texlive-minim
This is a modern plain format for the LuaTeX engine, adding improved low-level
support for many LuaTeX extensions and newer PDF features. While it can be used
as drop-in replacement for plain TeX, it probably is most useful as a basis for
your own formats. Most features included in the format are provided by separate
packages that can be used on their own; see the packages minim-mp for mplib
(MetaPost) support minim-math for unicode mathematics minim-pdf for creating
Tagged PDF minim-xmp for XMP (metadata) inclusion This package contains only
their shared lowest-level programming interface, along with their combined
format.

%package -n texlive-minim-math
Summary:        Extensive maths for LuaTeX
Version:        svn73816
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(minim-math.tex) = %{tl_version}

%description -n texlive-minim-math
This package provides a simple and highly configurable way to use Unicode and
OpenType mathematics with simple LuaTeX, taking advantage of most of the
engine's new capabilities in mathematical typesetting. Also included are the
proper settings and definitions for almost all Unicode mathematical characters.

%package -n texlive-minim-mp
Summary:        Low-level mplib integration for LuaTeX
Version:        svn73816
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(minim-mp.sty) = %{tl_version}
Provides:       tex(minim-mp.tex) = %{tl_version}

%description -n texlive-minim-mp
This package offers low-level mplib integration for LuaLaTeX and plain LuaTeX.
It is designed with the purpose of being easy to extend. The use of multiple
simultaneous MetaPost instances is supported, as well as running TeX or lua
code from within MetaPost. With the included minim-mp and minim-lamp format
files, you can even use Lua(La)TeX as a stand-alone MetaPost compiler.

%package -n texlive-minim-pdf
Summary:        Low-level PDF integration for LuaTeX
Version:        svn74207
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(minim-pdf.tex) = %{tl_version}

%description -n texlive-minim-pdf
This package adds low-level support to plain LuaTeX for marking up the
structure of a PDF document. The implementation is rather basic, but should
allow you to make your PDFs fully PDF/A-compliant.

%package -n texlive-minim-xmp
Summary:        Embed XMP metadata in PDF with LuaTeX
Version:        svn73816
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(minim-xmp.tex) = %{tl_version}

%description -n texlive-minim-xmp
This package enables the inclusion of XMP (eXtensible Metadata Platform) data
in the pdf output generated by (plain) LuaTeX. The use of XMP is required by
PDF standards such as PDF/A.

%package -n texlive-newpax
Summary:        Experimental package to extract and reinsert PDF annotations
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(pdfmanagement.sty)
Provides:       tex(newpax.sty) = %{tl_version}

%description -n texlive-newpax
The package is based on the pax package from Heiko Oberdiek. It offers a
lua-based alternative to the java based pax.jar to extract the annotations from
a PDF. The resulting file can then be used together with pax.sty. It also
offers an extended style which works with all three major engines.

%package -n texlive-nodetree
Summary:        Visualize node lists in a tree view
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(nodetree-embed.sty) = %{tl_version}
Provides:       tex(nodetree.sty) = %{tl_version}
Provides:       tex(nodetree.tex) = %{tl_version}

%description -n texlive-nodetree
nodetree is a development package that visualizes the structure of node lists.
nodetree shows its debug information in the console output when you compile a
LuaTeX file. It uses a similar visual representation for node lists as the UNIX
tree command for a folder structure.

%package -n texlive-odsfile
Summary:        Read OpenDocument Spreadsheet documents as LaTeX tables
Version:        svn76707
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(odsfile.sty) = %{tl_version}

%description -n texlive-odsfile
The distribution includes a package and a lua library that can together read
OpenDocument spreadsheet documents as LaTeX tables. Cells in the tables may be
processed by LaTeX macros, so that (for example) the package may be used for
drawing some plots. The package uses lua's zip library.

%package -n texlive-parstat
Summary:        A Paragraph statistic package for OpTeX
Version:        svn77123
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-parstat
This is a package for the OpTeX format that counts glyphs and spaces on
paragraph lines. From these numbers a statistic is made, which is printed into
the logfile.

%package -n texlive-pdfarticle
Summary:        Class for pdf publications
Version:        svn51127
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pdfarticle
pdfArticle is simple document class dedicated for creating pdf documents with
LuaLaTeX.

%package -n texlive-pdfextra
Summary:        Extra PDF features for (Op)TeX
Version:        svn65184
License:        0BSD
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pdfextra.sty) = %{tl_version}
Provides:       tex(pdfextra.tex) = %{tl_version}

%description -n texlive-pdfextra
This package provides extra PDF features for OpTeX (or in limited form for
plain LuaTeX and LuaLaTeX). As a minimalistic format, OpTeX does not support
"advanced" features of the PDF file format in its base. This third party
package aims to provide them. Summary of supported features: insertion of
multimedia (audio, video, 3D), hyperlinks and other actions, triggering events,
transitions, attachments.

%package -n texlive-penlight
Summary:        Penlight Lua libraries made available to LuaLaTeX users
Version:        svn73362
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(penlight.sty) = %{tl_version}

%description -n texlive-penlight
This LuaLaTeX package provides a wrapper to use the penlight Lua libraries with
LuaLaTeX, with some extra functionality added.

%package -n texlive-penlightplus
Summary:        Additions to the Penlight Lua libraries
Version:        svn74000
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luakeys.sty)
Requires:       tex(penlight.sty)
Requires:       tex(tokcycle.sty)
Provides:       tex(penlightplus.sty) = %{tl_version}

%description -n texlive-penlightplus
This package extends the penlight package by adding useful functions for
interfacing with LaTeX.

%package -n texlive-piton
Summary:        Typeset computer listings with LPEG of LuaLaTeX
Version:        svn77302
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tcolorbox.sty)
Provides:       tex(piton.sty) = %{tl_version}

%description -n texlive-piton
This package uses the Lua library LPEG to typeset and highlight computer
listings in several languages. It requires the use of LuaLaTeX. It won't work
with XeLaTeX, nor pdfLaTeX.

%package -n texlive-placeat
Summary:        Absolute content positioning
Version:        svn45145
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xparse.sty)
Provides:       tex(placeat.sty) = %{tl_version}

%description -n texlive-placeat
The package provides commands so that the user of LuaLaTeX may position
arbitrary content at any position specified by absolute coordinates on the
page. The package draws a grid on each page of the document, to aid positioning
(the grid may be disabled, for 'final copy' using the command \placeatsetup).

%package -n texlive-plantuml
Summary:        Support for rendering UML diagrams using PlantUML
Version:        svn75196
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(luacode.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(pythontex.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(plantuml.sty) = %{tl_version}

%description -n texlive-plantuml
PlantUML is a program which transforms text into UML diagrams. This LaTeX
package allows for embedding PlantUML diagrams using the PlantUML source.
Currently, this project runs with LuaLaTeX only.

%package -n texlive-pyluatex
Summary:        Execute Python code on the fly in your LaTeX documents
Version:        svn76924
License:        MIT AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(pyluatex.sty) = %{tl_version}

%description -n texlive-pyluatex
PyLuaTeX allows you to execute Python code and to include the resulting output
in your LaTeX documents in a single compilation run. LaTeX documents must be
compiled with LuaLaTeX for this to work. PyLuaTeX runs a Python
InteractiveInterpreter (actually several if you use different sessions) in the
background for on-the-fly code execution. Python code from your LaTeX file is
sent to the background interpreter through a TCP socket. This approach allows
your Python code to be executed and the output to be integrated in your LaTeX
file in a single compilation run. No additional processing steps are needed. No
intermediate files have to be written. No placeholders have to be inserted.

%package -n texlive-scikgtex
Summary:        Mark research contributions in scientific documents and embed them in PDF metadata
Version:        svn66764
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(suffix.sty)
Provides:       tex(scikgtex.sty) = %{tl_version}

%description -n texlive-scikgtex
Scientific Knowledge Graph TeX (SciKgTeX) is a LuaLaTeX package which makes it
possible to annotate specific research contributions in scientific documents.
SciKGTeX will enrich the document by adding the marked contributions to PDF
metadata in a structured XMP format which can be picked up by search engines
and knowledge graphs.

%package -n texlive-seatingchart
Summary:        Generation of seating charts
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(luacode.sty)
Requires:       tex(tikz.sty)
Provides:       tex(seatingchart.sty) = %{tl_version}

%description -n texlive-seatingchart
This package enables the visualization of seating charts, whereby the seating
layouts (i.e. the arrangement of seats in a room) and the seating scheme (i.e.
the selection and labeling of occupied seats) can be controlled independently
of each other. The package should be considered experimental and requires
LuaLaTeX.

%package -n texlive-selnolig
Summary:        Selectively disable typographic ligatures
Version:        svn68747
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(selnolig-english-hyphex.sty) = %{tl_version}
Provides:       tex(selnolig-english-patterns.sty) = %{tl_version}
Provides:       tex(selnolig-german-hyphex.sty) = %{tl_version}
Provides:       tex(selnolig-german-patterns.sty) = %{tl_version}
Provides:       tex(selnolig.sty) = %{tl_version}

%description -n texlive-selnolig
The package suppresses typographic ligatures selectively, i.e., based on
predefined search patterns. The search patterns focus on ligatures deemed
inappropriate because they span morpheme boundaries. For example, the word
shelfful, which is mentioned in the TeXbook as a word for which the ff ligature
might be inappropriate, is automatically typeset as shelf\/ful rather than as
shel{ff}ul. For English and German language documents, the package provides
extensive rules for the selective suppression of so-called "common" ligatures.
These comprise the ff, fi, fl, ffi, and ffl ligatures as well as the ft and fft
ligatures. Other f-ligatures, such as fb, fh, fj and fk, are suppressed
globally, while exceptions are made for names and words of non-English/German
origin, such as Kafka and fjord. For English language documents, the package
further provides ligature suppression macros for a number of so-called
"discretionary" or "rare" ligatures such as ct, st, and sp. The package
requires use of a recent LuaLaTeX format (for example those from TeX Live 2012
or 2013, or MiKTeX 2.9).

%package -n texlive-semesterplannerlua
Summary:        Draw timetables and other organizational matters useful for planning a semester
Version:        svn71322
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontawesome.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(semesterplannerlua.sty) = %{tl_version}

%description -n texlive-semesterplannerlua
This LaTeX package provides commands to print timetables, lists of appointments
and exams. Also it is possible to draw calendars of specified ranges (and mark
dates which were previously listed). Drawing the timetable is based on TikZ,
which makes it very flexible.

%package -n texlive-showhyphenation
Summary:        Marking of hyphenation points
Version:        svn67602
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(showhyphenation.sty) = %{tl_version}

%description -n texlive-showhyphenation
The package shows the hyphenation points in the document by either inserting
small triangles below the baseline or by typesetting explicit hyphens. The
markers are correctly placed even within ligatures and their size adjusts to
the font size. By option the markers can be placed behind or in front of the
glyphs. The package requires LuaLaTeX.

%package -n texlive-showkerning
Summary:        Showing kerns in a document
Version:        svn67603
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(showkerning.sty) = %{tl_version}

%description -n texlive-showkerning
The package displays all kerning values in the form of colored bars directly at
the respective position in the document. Positive values are displayed in
green, negative values in red. The width of the bars corresponds exactly to the
respective kerning value. By option the bars can be placed behind or in front
of the glyphs. The package requires LuaLaTeX.

%package -n texlive-spacekern
Summary:        Kerning between words and against space
Version:        svn67604
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(spacekern.sty) = %{tl_version}

%description -n texlive-spacekern
This package provides two shorthands for typesetting breaking and non-breaking
small spaces, where both hyphenation and kerning against space are correctly
applied. Additionally, interword kerning can be applied.

%package -n texlive-spelling
Summary:        Support for spell-checking of LuaTeX documents
Version:        svn73571
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase-attr.sty)
Requires:       tex(luatexbase-mcb.sty)
Requires:       tex(luatexbase-modutils.sty)
Provides:       tex(spelling.sty) = %{tl_version}

%description -n texlive-spelling
The package aids spell-checking of TeX documents compiled with the LuaTeX
engine. It can give visual feedback in PDF output similar to WYSIWYG word
processors. The package relies on an external spell-checker application to
check spelling of a text file and to output a list of bad spellings. The
package should work with most spell-checkers, even dumb, TeX-unaware ones.

%package -n texlive-stricttex
Summary:        Strictly balanced brackets and numbers in command names
Version:        svn56320
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(stricttex.sty) = %{tl_version}

%description -n texlive-stricttex
This is a small, LuaLaTeX-only package providing you with three, sometimes
useful features: It allows you to make brackets [...] "strict", meaning that
each [ must be balanced by a ]. It allows you to use numbers in command names,
so that you can do stuff like \newcommand\pi12{\pi_{12}}. It allows you to use
numbers and primes in command names, so that you can do stuff like
\newcommand\pi'12{\pi '_{12}}.

%package -n texlive-sympycalc
Summary:        Work with SymPy and PyLuaTeX
Version:        svn73069
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xstring.sty)
Provides:       tex(SympyCalc.sty) = %{tl_version}

%description -n texlive-sympycalc
This package provides some commands (mostly for French users) to perform SymPy
commands and format the result with some adjustments in formatting: \sympycalc
to perform a generic SymPy command; \sympyfact or \sympydev to factor or
expand; \sympyderiv, \sympyprim or \sympyintegr to derive or integrate ;
\sympyreso to resolve equations ...

%package -n texlive-tango
Summary:        A LaTeX document class for math teachers
Version:        svn71825
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tango
Tango is a LaTeX document class for use by mathematics teachers. It requires
LuaLaTeX, some LaTeX packages (see the complete documentation for details), and
a recent version of LaTeX.

%package -n texlive-truthtable
Summary:        Automatically generate truth tables for given variables and statements
Version:        svn68300
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luacode.sty)
Provides:       tex(truthtable.sty) = %{tl_version}

%description -n texlive-truthtable
This LuaLaTeX package permits to automatically generate truth tables given a
table header. It supports a number of logical operations which can be combined
as needed. It is built upon the luacode package.

%package -n texlive-tsvtemplate
Summary:        Apply a template to a tsv file
Version:        svn65333
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Provides:       tex(tsvtemplate.sty) = %{tl_version}
Provides:       tex(tsvtemplate.tex) = %{tl_version}

%description -n texlive-tsvtemplate
This is a simple tsv (tab-separated values) reader for LuaLaTeX and plain
LuaTeX. It also supports (non-quoted) comma-separated values, or indeed values
separated by any character.

%package -n texlive-typewriter
Summary:        Typeset with a randomly variable monospace font
Version:        svn73877
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(typewriter.sty) = %{tl_version}

%description -n texlive-typewriter
The typewriter package uses the OpenType Computer Modern Unicode Typewriter
font, together with a LuaTeX virtual font setup that introduces random
variability in grey level and angle of each character. It was originally an
answer to a question on stackexchange.

%package -n texlive-unibidi-lua
Summary:        Unicode bidi algorithm implementation for various LuaTeX formats
Version:        svn77352
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(unibidi-lua.sty) = %{tl_version}
Provides:       tex(unibidi-lua.tex) = %{tl_version}

%description -n texlive-unibidi-lua
The package adopts the unicode bidi algorithm implementation provided in
ConTeXt, and adapts it to be used in OpTeX, LaTeX and Plain TeX . It works
under LuaTeX only.

%package -n texlive-uninormalize
Summary:        Unicode normalization support
Version:        svn57257
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Provides:       tex(uninormalize.sty) = %{tl_version}

%description -n texlive-uninormalize
This package provides Unicode normalization (useful for composed characters)
for LuaLaTeX.

%package -n texlive-yamlvars
Summary:        A YAML parser and tool for easy LaTeX definition creation
Version:        svn73922
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luakeys.sty)
Requires:       tex(penlightplus.sty)
Provides:       tex(yamlvars.sty) = %{tl_version}

%description -n texlive-yamlvars
This LuaLaTeX package provides a YAML parser and some functions to declare and
define LaTeX definitions using YAML files.


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

# move the luakeyval LICENSE file to 0bsd.txt in the topdir
mv %{buildroot}%{_texmf_main}/doc/luatex/luakeyval/LICENSE 0bsd-luakeyval.txt
# same for pdfextra but we can't reuse the file because copyright attribution matters here
mv %{buildroot}%{_texmf_main}/doc/optex/pdfextra/LICENSE 0bsd-pdfextra.txt

# minim is EUPL
mv %{buildroot}%{_texmf_main}/doc/luatex/minim/EUPL-1.2-EN.txt eupl-1.2-en.txt

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-addliga
%license pd.txt
%{_texmf_main}/tex/lualatex/addliga/
%doc %{_texmf_main}/doc/lualatex/addliga/

%files -n texlive-addtoluatexpath
%license mit.txt
%{_texmf_main}/tex/luatex/addtoluatexpath/
%doc %{_texmf_main}/doc/luatex/addtoluatexpath/

%files -n texlive-auto-pst-pdf-lua
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/auto-pst-pdf-lua/
%doc %{_texmf_main}/doc/latex/auto-pst-pdf-lua/

%files -n texlive-barracuda
%license gpl2.txt
%{_texmf_main}/scripts/barracuda/
%{_texmf_main}/tex/luatex/barracuda/
%doc %{_texmf_main}/doc/luatex/barracuda/

%files -n texlive-bezierplot
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/bezierplot/
%doc %{_texmf_main}/doc/lualatex/bezierplot/

%files -n texlive-blopentype
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/luatex/blopentype/
%doc %{_texmf_main}/doc/luatex/blopentype/

%files -n texlive-char2path
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/char2path/
%doc %{_texmf_main}/doc/latex/char2path/

%files -n texlive-chickenize
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/chickenize/
%doc %{_texmf_main}/doc/luatex/chickenize/

%files -n texlive-chinese-jfm
%license mit.txt
%{_texmf_main}/tex/luatex/chinese-jfm/
%doc %{_texmf_main}/doc/luatex/chinese-jfm/

%files -n texlive-cloze
%license lppl1.3c.txt
%{_texmf_main}/scripts/cloze/
%{_texmf_main}/tex/luatex/cloze/
%doc %{_texmf_main}/doc/luatex/cloze/

%files -n texlive-combofont
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/combofont/
%doc %{_texmf_main}/doc/lualatex/combofont/

%files -n texlive-cstypo
%license mit.txt
%{_texmf_main}/tex/lualatex/cstypo/
%{_texmf_main}/tex/luatex/cstypo/
%doc %{_texmf_main}/doc/lualatex/cstypo/

%files -n texlive-ctablestack
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/ctablestack/
%doc %{_texmf_main}/doc/luatex/ctablestack/

%files -n texlive-ekdosis
%license gpl3.txt
%license fdl.txt
%{_texmf_main}/tex/lualatex/ekdosis/
%doc %{_texmf_main}/doc/lualatex/ekdosis/

%files -n texlive-emoji
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/emoji/
%doc %{_texmf_main}/doc/latex/emoji/

%files -n texlive-emojicite
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/emojicite/
%doc %{_texmf_main}/doc/lualatex/emojicite/

%files -n texlive-enigma
%license bsd.txt
%{_texmf_main}/scripts/context/lua/
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/enigma/
%{_texmf_main}/tex/latex/enigma/
%{_texmf_main}/tex/plain/enigma/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-fancymag
%license lppl1.3c.txt
%license ofl.txt
%{_texmf_main}/tex/lualatex/fancymag/
%doc %{_texmf_main}/doc/lualatex/fancymag/

%files -n texlive-farbe
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/farbe/
%doc %{_texmf_main}/doc/luatex/farbe/

%files -n texlive-gitinfo-lua
%license lppl1.3c.txt
%{_texmf_main}/scripts/gitinfo-lua/
%{_texmf_main}/tex/lualatex/gitinfo-lua/
%doc %{_texmf_main}/doc/lualatex/gitinfo-lua/

%files -n texlive-ideavault
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/ideavault/
%doc %{_texmf_main}/doc/lualatex/ideavault/

%files -n texlive-innerscript
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/innerscript/
%doc %{_texmf_main}/doc/lualatex/innerscript/

%files -n texlive-interpreter
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/interpreter/
%doc %{_texmf_main}/doc/luatex/interpreter/

%files -n texlive-kanaparser
%license bsd.txt
%{_texmf_main}/tex/luatex/kanaparser/
%doc %{_texmf_main}/doc/luatex/kanaparser/

%files -n texlive-kkluaverb
%license mit.txt
%{_texmf_main}/tex/lualatex/kkluaverb/
%doc %{_texmf_main}/doc/lualatex/kkluaverb/

%files -n texlive-kkran
%license mit.txt
%{_texmf_main}/tex/latex/kkran/
%doc %{_texmf_main}/doc/latex/kkran/

%files -n texlive-kksymbols
%license mit.txt
%{_texmf_main}/tex/latex/kksymbols/
%doc %{_texmf_main}/doc/latex/kksymbols/

%files -n texlive-ligtype
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/ligtype/
%doc %{_texmf_main}/doc/lualatex/ligtype/

%files -n texlive-linebreaker
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/linebreaker/
%doc %{_texmf_main}/doc/lualatex/linebreaker/

%files -n texlive-longmath
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/longmath/
%doc %{_texmf_main}/doc/lualatex/longmath/

%files -n texlive-lparse
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/lparse/
%doc %{_texmf_main}/doc/luatex/lparse/

%files -n texlive-lt3luabridge
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/lt3luabridge/
%doc %{_texmf_main}/doc/generic/lt3luabridge/

%files -n texlive-lua-placeholders
%license lppl1.3c.txt
%{_texmf_main}/scripts/lua-placeholders/
%{_texmf_main}/tex/lualatex/lua-placeholders/
%doc %{_texmf_main}/doc/lualatex/lua-placeholders/

%files -n texlive-lua-tinyyaml
%license mit.txt
%{_texmf_main}/scripts/lua-tinyyaml/
%doc %{_texmf_main}/doc/luatex/lua-tinyyaml/

%files -n texlive-lua-typo
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/lua-typo/
%doc %{_texmf_main}/doc/lualatex/lua-typo/

%files -n texlive-lua-uca
%license mit.txt
%{_texmf_main}/scripts/lua-uca/
%doc %{_texmf_main}/doc/support/lua-uca/

%files -n texlive-lua-ul
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/lua-ul/
%doc %{_texmf_main}/doc/lualatex/lua-ul/

%files -n texlive-lua-visual-debug
%license mit.txt
%{_texmf_main}/tex/luatex/lua-visual-debug/
%doc %{_texmf_main}/doc/luatex/lua-visual-debug/

%files -n texlive-lua-widow-control
%license other-free.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/lualatex/lua-widow-control/
%{_texmf_main}/tex/luatex/lua-widow-control/
%{_texmf_main}/tex/optex/lua-widow-control/
%doc %{_texmf_main}/doc/luatex/lua-widow-control/

%files -n texlive-luaaddplot
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/luaaddplot/
%doc %{_texmf_main}/doc/luatex/luaaddplot/

%files -n texlive-luacas
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luacas/
%doc %{_texmf_main}/doc/lualatex/luacas/

%files -n texlive-luacensor
%license lppl1.3c.txt
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/luacensor/
%{_texmf_main}/tex/lualatex/luacensor/
%doc %{_texmf_main}/doc/lualatex/luacensor/

%files -n texlive-luacode
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luacode/
%doc %{_texmf_main}/doc/lualatex/luacode/

%files -n texlive-luacolor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/luacolor/
%doc %{_texmf_main}/doc/latex/luacolor/

%files -n texlive-luacomplex
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luacomplex/
%doc %{_texmf_main}/doc/lualatex/luacomplex/

%files -n texlive-luagcd
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luagcd/
%doc %{_texmf_main}/doc/lualatex/luagcd/

%files -n texlive-luahttp
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luahttp/
%doc %{_texmf_main}/doc/lualatex/luahttp/

%files -n texlive-luahyphenrules
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luahyphenrules/
%doc %{_texmf_main}/doc/lualatex/luahyphenrules/

%files -n texlive-luaimageembed
%license mit.txt
%{_texmf_main}/tex/lualatex/luaimageembed/
%doc %{_texmf_main}/doc/lualatex/luaimageembed/

%files -n texlive-luaindex
%license lppl1.3c.txt
%{_texmf_main}/scripts/luaindex/
%{_texmf_main}/tex/lualatex/luaindex/
%doc %{_texmf_main}/doc/lualatex/luaindex/

%files -n texlive-luainputenc
%license pd.txt
%{_texmf_main}/tex/lualatex/luainputenc/
%doc %{_texmf_main}/doc/lualatex/luainputenc/

%files -n texlive-luakeys
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/luakeys/
%doc %{_texmf_main}/doc/luatex/luakeys/

%files -n texlive-luakeyval
%license 0bsd-luakeyval.txt
%{_texmf_main}/tex/luatex/luakeyval/
%doc %{_texmf_main}/doc/luatex/luakeyval/

%files -n texlive-lualatex-math
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/lualatex-math/
%doc %{_texmf_main}/doc/lualatex/lualatex-math/

%files -n texlive-lualatex-truncate
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/lualatex-truncate/
%doc %{_texmf_main}/doc/lualatex/lualatex-truncate/

%files -n texlive-lualibs
%license gpl2.txt
%{_texmf_main}/tex/luatex/lualibs/
%doc %{_texmf_main}/doc/luatex/lualibs/

%files -n texlive-lualinalg
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/lualinalg/
%doc %{_texmf_main}/doc/lualatex/lualinalg/

%files -n texlive-luamathalign
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luamathalign/
%doc %{_texmf_main}/doc/lualatex/luamathalign/

%files -n texlive-luamaths
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luamaths/
%doc %{_texmf_main}/doc/lualatex/luamaths/

%files -n texlive-luamml
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luamml/
%doc %{_texmf_main}/doc/lualatex/luamml/

%files -n texlive-luamodulartables
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luamodulartables/
%doc %{_texmf_main}/doc/lualatex/luamodulartables/

%files -n texlive-luamplib
%license gpl2.txt
%{_texmf_main}/tex/luatex/luamplib/
%doc %{_texmf_main}/doc/luatex/luamplib/

%files -n texlive-luaoptions
%license mit.txt
%{_texmf_main}/tex/lualatex/luaoptions/
%doc %{_texmf_main}/doc/lualatex/luaoptions/

%files -n texlive-luapackageloader
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/luapackageloader/
%doc %{_texmf_main}/doc/luatex/luapackageloader/

%files -n texlive-luaplot
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luaplot/
%doc %{_texmf_main}/doc/lualatex/luaplot/

%files -n texlive-luaprogtable
%license mit.txt
%{_texmf_main}/tex/lualatex/luaprogtable/
%doc %{_texmf_main}/doc/lualatex/luaprogtable/

%files -n texlive-luaquotes
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luaquotes/
%doc %{_texmf_main}/doc/lualatex/luaquotes/

%files -n texlive-luarandom
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luarandom/
%doc %{_texmf_main}/doc/lualatex/luarandom/

%files -n texlive-luaset
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luaset/
%doc %{_texmf_main}/doc/lualatex/luaset/

%files -n texlive-luatbls
%license mit.txt
%{_texmf_main}/tex/lualatex/luatbls/
%doc %{_texmf_main}/doc/lualatex/luatbls/

%files -n texlive-luatex-type-definitions
%license gpl2.txt
%{_texmf_main}/tex/luatex/luatex-type-definitions/
%doc %{_texmf_main}/doc/luatex/luatex-type-definitions/

%files -n texlive-luatex85
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/luatex85/
%doc %{_texmf_main}/doc/generic/luatex85/

%files -n texlive-luatexbase
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/luatexbase/
%doc %{_texmf_main}/doc/luatex/luatexbase/

%files -n texlive-luatexko
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/luatexko/
%doc %{_texmf_main}/doc/luatex/luatexko/

%files -n texlive-luatextra
%license pd.txt
%{_texmf_main}/tex/lualatex/luatextra/
%doc %{_texmf_main}/doc/lualatex/luatextra/

%files -n texlive-luatikz
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/latex/luatikz/
%doc %{_texmf_main}/doc/latex/luatikz/

%files -n texlive-luatruthtable
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/luatruthtable/
%doc %{_texmf_main}/doc/lualatex/luatruthtable/

%files -n texlive-luavlna
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/luavlna/
%doc %{_texmf_main}/doc/luatex/luavlna/

%files -n texlive-luaxml
%license mit.txt
%{_texmf_main}/tex/luatex/luaxml/
%doc %{_texmf_main}/doc/luatex/luaxml/

%files -n texlive-lutabulartools
%license mit.txt
%{_texmf_main}/tex/luatex/lutabulartools/
%doc %{_texmf_main}/doc/luatex/lutabulartools/

%files -n texlive-marginalia
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/marginalia/
%doc %{_texmf_main}/doc/lualatex/marginalia/

%files -n texlive-minim
%license eupl-1.2-en.txt
%{_texmf_main}/tex/luatex/minim/
%doc %{_texmf_main}/doc/luatex/minim/

%files -n texlive-minim-math
%license eupl-1.2-en.txt
%{_texmf_main}/tex/luatex/minim-math/
%doc %{_texmf_main}/doc/luatex/minim-math/

%files -n texlive-minim-mp
%license eupl-1.2-en.txt
%{_texmf_main}/metapost/minim-mp/
%{_texmf_main}/tex/luatex/minim-mp/
%doc %{_texmf_main}/doc/luatex/minim-mp/

%files -n texlive-minim-pdf
%license eupl-1.2-en.txt
%{_texmf_main}/tex/luatex/minim-pdf/
%doc %{_texmf_main}/doc/luatex/minim-pdf/

%files -n texlive-minim-xmp
%license eupl-1.2-en.txt
%{_texmf_main}/tex/luatex/minim-xmp/
%doc %{_texmf_main}/doc/luatex/minim-xmp/

%files -n texlive-newpax
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/newpax/
%doc %{_texmf_main}/doc/latex/newpax/

%files -n texlive-nodetree
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/nodetree/
%doc %{_texmf_main}/doc/luatex/nodetree/

%files -n texlive-odsfile
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/odsfile/
%doc %{_texmf_main}/doc/lualatex/odsfile/

%files -n texlive-parstat
%license lppl1.3c.txt
%{_texmf_main}/tex/optex/parstat/
%doc %{_texmf_main}/doc/optex/parstat/

%files -n texlive-pdfarticle
%license mit.txt
%{_texmf_main}/tex/lualatex/pdfarticle/
%doc %{_texmf_main}/doc/lualatex/pdfarticle/

%files -n texlive-pdfextra
%license 0bsd-pdfextra.txt
%{_texmf_main}/tex/luatex/pdfextra/
%{_texmf_main}/tex/optex/pdfextra/
%doc %{_texmf_main}/doc/optex/pdfextra/

%files -n texlive-penlight
%license mit.txt
%{_texmf_main}/tex/luatex/penlight/
%doc %{_texmf_main}/doc/luatex/penlight/

%files -n texlive-penlightplus
%license mit.txt
%{_texmf_main}/tex/luatex/penlightplus/
%doc %{_texmf_main}/doc/luatex/penlightplus/

%files -n texlive-piton
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/piton/
%doc %{_texmf_main}/doc/lualatex/piton/

%files -n texlive-placeat
%license lppl1.3c.txt
%{_texmf_main}/scripts/placeat/
%{_texmf_main}/tex/lualatex/placeat/
%doc %{_texmf_main}/doc/lualatex/placeat/

%files -n texlive-plantuml
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/plantuml/
%doc %{_texmf_main}/doc/lualatex/plantuml/

%files -n texlive-pyluatex
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/pyluatex/
%doc %{_texmf_main}/doc/lualatex/pyluatex/

%files -n texlive-scikgtex
%license mit.txt
%{_texmf_main}/tex/lualatex/scikgtex/
%doc %{_texmf_main}/doc/lualatex/scikgtex/

%files -n texlive-seatingchart
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/seatingchart/
%doc %{_texmf_main}/doc/lualatex/seatingchart/

%files -n texlive-selnolig
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/selnolig/
%doc %{_texmf_main}/doc/lualatex/selnolig/

%files -n texlive-semesterplannerlua
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/semesterplannerlua/
%doc %{_texmf_main}/doc/lualatex/semesterplannerlua/

%files -n texlive-showhyphenation
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/showhyphenation/
%doc %{_texmf_main}/doc/lualatex/showhyphenation/

%files -n texlive-showkerning
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/showkerning/
%doc %{_texmf_main}/doc/lualatex/showkerning/

%files -n texlive-spacekern
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/spacekern/
%doc %{_texmf_main}/doc/lualatex/spacekern/

%files -n texlive-spelling
%license lppl1.3c.txt
%{_texmf_main}/scripts/spelling/
%{_texmf_main}/tex/luatex/spelling/
%doc %{_texmf_main}/doc/luatex/spelling/

%files -n texlive-stricttex
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/stricttex/
%doc %{_texmf_main}/doc/lualatex/stricttex/

%files -n texlive-sympycalc
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/sympycalc/
%doc %{_texmf_main}/doc/lualatex/sympycalc/

%files -n texlive-tango
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/tango/
%doc %{_texmf_main}/doc/lualatex/tango/

%files -n texlive-truthtable
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/truthtable/
%doc %{_texmf_main}/doc/lualatex/truthtable/

%files -n texlive-tsvtemplate
%license other-free.txt
%{_texmf_main}/tex/luatex/tsvtemplate/
%doc %{_texmf_main}/doc/luatex/tsvtemplate/

%files -n texlive-typewriter
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/typewriter/
%doc %{_texmf_main}/doc/lualatex/typewriter/

%files -n texlive-unibidi-lua
%license gpl2.txt
%{_texmf_main}/tex/luatex/unibidi-lua/
%doc %{_texmf_main}/doc/luatex/unibidi-lua/

%files -n texlive-uninormalize
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/uninormalize/
%doc %{_texmf_main}/doc/lualatex/uninormalize/

%files -n texlive-yamlvars
%license mit.txt
%{_texmf_main}/tex/lualatex/yamlvars/
%doc %{_texmf_main}/doc/lualatex/yamlvars/

%changelog
* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77516-2
- Update to svn77516
- fix licensing files
- update luaxml luatexko luamplib

* Fri Jan 23 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77106-1
- Update to svn77106
- description fixes
- licensing fixes
- manual license handling (be careful with minim)
- updated components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75911-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75911-1
- Update to TeX Live 2025
