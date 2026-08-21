%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: libreoffice-dictionaries
Summary: LibreOffice hunspell dictionaries
Version: 26.8.0.2
Release: 3%{?dist}
Source0: https://github.com/LibreOffice/dictionaries/archive/refs/tags/libreoffice-%{version}.tar.gz
URL: https://github.com/LibreOffice/dictionaries
# License tag is combined license of all binary subpackages
License: AGPL-3.0-only AND Apache-2.0 AND BSD-3-Clause AND (BSD-3-Clause OR CC-BY-3.0) AND BSD-3-Clause-Modification AND CC-BY-4.0 AND (CC-BY-4.0 or LGPL-3.0-only) AND CC-BY-SA-3.0 AND CC0-1.0 AND GFDL-1.2-invariants-or-later AND GPL-1.0-only AND (GPL-1.0-only OR LGPL-2.1-only) AND GPL-1.0-or-later AND GPL-2.0-only AND (GPL-2.0-only AND LGPL-2.1-only) AND (GPL-2.0-only OR GPL-3.0-only) AND (GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1) AND GPL-2.0-or-later AND (GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1) AND (GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 OR Apache-2.0 OR CC-BY-SA-4.0) AND GPL-3.0-only AND (GPL-3.0-only OR LGPL-2.1-only OR MPL-1.1) AND GPL-3.0-or-later AND (GPL-3.0-or-later OR LGPL-3.0-or-later OR MPL-1.1) AND (GPL-3.0-or-later OR LGPL-3.0-or-later OR MPL-2.0) AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-only AND MPL-1.1 AND LPPL-1.3c AND MPL-1.1 AND MPL-2.0 AND NTP
BuildArch: noarch

%description
LibreOffice hunspell dictionaries.

%{lua:
-- template for libreoffice-dict-<lang>
install_cmds = ""  -- global: populated by defdict(), consumed in %install

local dest = rpm.expand("%{buildroot}%{_datadir}/%{dict_dirname}")

local function defdict(d)
local templ = [[
%package -n libreoffice-dict-%{_lang}
Summary: %{_langengname} hunspell dictionary
%{?_license_tag}
Requires: hunspell-filesystem
Conflicts: hunspell-%{_conflicts}

%description -n libreoffice-dict-%{_lang}
%{_langengname} hunspell dictionary

%files -n libreoffice-dict-%{_lang}
%{?_doc}
%{?_license_file}
%{_datadir}/%{dict_dirname}/%{_filesglob}
%{?_filesglob2:%{_datadir}/%{dict_dirname}/%{_filesglob2}}
]]
  local filebase = d.cp_dir or d.lang:gsub("-", "_")
  local srcdir = d.srcdir or filebase
  local docdir = srcdir:gsub("/.*$", "")
  rpm.define("_lang "        .. d.lang)
  rpm.define("_langengname " .. d.langengname)
  rpm.define("_conflicts "   .. (d.conflicts or d.lang))
  rpm.define("_supplements " .. (d.supplements or d.lang))
  rpm.define("_filesglob "   .. filebase .. ".*")
  if d.filesglob2 then
    rpm.define("_filesglob2 " .. d.filesglob2)
  end
  if d.license then
    rpm.define("_license_tag License: " .. d.license)
  end
  if d.doc then
    rpm.define("_doc %%doc " .. d.doc:gsub("(%S+)", docdir .. "/%1"))
  end
  if d.license_file then
    rpm.define("_license_file %%license " .. d.license_file:gsub("(%S+)", docdir .. "/%1"))
  end
  print(rpm.expand(templ))
  rpm.undefine("_lang")
  rpm.undefine("_langengname")
  rpm.undefine("_conflicts")
  rpm.undefine("_supplements")
  rpm.undefine("_filesglob")
  rpm.undefine("_filesglob2")
  rpm.undefine("_license_tag")
  rpm.undefine("_doc")
  rpm.undefine("_license_file")

  if not d.cp_skip then
    install_cmds = install_cmds .. "cp -p " .. srcdir .. "/" .. filebase .. ".* " .. dest .. "\n"
  end
end

-- Lua array table for all available dictionary languages
-- lang is used for subpackage name generation
-- cp_dir is used for dictionary file names as well as upstream language directory name
-- cp_dir is skipped where lang value matches with cp_dir value
-- src_dir is used when upstream language directory name differs from cp_dir value
--
dicts = {
 { lang="af",  langengname="Afrikaans",         license="LGPL-2.1-or-later",
   doc="README_af_ZA.txt",                      cp_dir="af_ZA" },
 { lang="an",  langengname="Aragonese",         license="GPL-3.0-or-later OR LGPL-3.0-or-later OR MPL-1.1",
   license_file="LICENSES-en.txt",              cp_dir="an_ES" },
 { lang="ar",  langengname="Arabic",            license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="*.txt",                                 cp_dir="ar",
   filesglob2="ar_??.*", srcdir="ar", cp_skip=true },
 { lang="as",  langengname="Assamese",          license="GPL-3.0-only",
   doc="README_as_IN.txt",                      cp_dir="as_IN" },
 { lang="be",  langengname="Belarusian",        license="CC-BY-4.0 or LGPL-3.0-only",
   doc="README_be_BY.txt",                      cp_dir="be_BY",
   cp_skip=true },
 { lang="bg",  langengname="Bulgarian",         license="GPL-2.0-or-later",
   license_file="COPYING",                      cp_dir="bg_BG" },
 { lang="bo",  langengname="Tibetan",           license="CC0-1.0",
   doc="*.md" },
 { lang="br",  langengname="Breton",            license="LGPL-2.1-or-later",
   license_file="LICENSES-en.txt",              cp_dir="br_FR" },
 { lang="bs",  langengname="Bosnian",           license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README.txt",                            cp_dir="bs_BA" },
 { lang="bn_BD",  langengname="Bengali",        license="GPL-2.0-or-later",
   license_file="COPYING" },
 { lang="ca",  langengname="Catalan",           license="GPL-2.0-or-later AND LGPL-2.1-or-later",
   license_file="LICENSES-en.txt",              cp_dir="ca_??",
   srcdir="ca", cp_skip=true },
 { lang="ckb", langengname="Central Kurdish",   license="CC-BY-4.0",
   license_file="LICENSES-en.txt",              srcdir="ckb/dictionaries",
   filesglob2="ckb_IQ.*" },
 { lang="cs",  langengname="Czech",             license="GPL-1.0-or-later",
   doc="README_en.txt",                         cp_dir="cs_CZ" },
 { lang="da",  langengname="Danish",            license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README_da_DK.txt",                      cp_dir="da_DK" },
 { lang="de",  langengname="German",            license="GPL-2.0-or-later OR GPL-3.0-or-later",
   cp_dir="de_*", cp_skip=true },
 { lang="en-AU",  langengname="AU English",     license="NTP",
   doc="README_en_AU.txt",                      srcdir="en" },
 { lang="en-CA",  langengname="CA English",     license="NTP",
   doc="README_en_CA.txt",                      srcdir="en" },
 { lang="en-GB",  langengname="UK English",     license="LGPL-2.1-or-later",
   doc="README_en_GB.txt",                      srcdir="en" },
 { lang="en-US",  langengname="US English",     license="NTP",
   doc="README_en_US.txt",                      srcdir="en" },
 { lang="en-ZA",  langengname="ZA English",     license="LGPL-2.1-or-later",
   doc="README_en_ZA.txt",                      srcdir="en" },
 { lang="el",  langengname="Greek",             license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README_el_GR.txt",                      cp_dir="el_GR" },
 { lang="eo",  langengname="Esperanto",         license="GPL-2.0-or-later",
   license_file="license-en.txt" },
 { lang="es",  langengname="Spanish",           license="GPL-3.0-or-later OR LGPL-3.0-or-later OR MPL-1.1",
   doc="README_hunspell_es.txt",                cp_dir="es_*",
   srcdir="es", cp_skip=true },
 { lang="et",  langengname="Estonian",          license="LGPL-2.1-or-later",
   doc="README_et_EE.txt",                      cp_dir="et_EE" },
 { lang="fa",  langengname="Farsi",             license="Apache-2.0",
   doc="README_fa_IR.txt",                      cp_dir="fa-IR",
   srcdir="fa_IR", filesglob2="fa_IR.*" },
 { lang="fr",  langengname="French",            license="MPL-2.0",
   doc="dictionaries/README_dict_fr.txt",       cp_dir="fr_??",
   srcdir="fr_FR", cp_skip=true },
 { lang="gd",  langengname="Scots Gaelic",      license="GPL-3.0-or-later",
   doc="README_gd_GB.txt", license_file="LICENSES-en.txt", cp_dir="gd_GB" },
 { lang="gl",  langengname="Galician",          license="GPL-3.0-or-later",
   doc="README",                                cp_dir="gl_ES",
   srcdir="gl" },
-- discussion going on for license issue in https://bugs.documentfoundation.org/show_bug.cgi?id=171993
 { lang="gug", langengname="Guarani",           license="GFDL-1.2-invariants-or-later",
   doc="description/desc_en_US.txt",
   filesglob2="gug_PY.*" },
 { lang="gu",  langengname="Gujarati",          license="GPL-1.0-or-later",
   doc="README_gu_IN.txt",                      cp_dir="gu_IN" },
 { lang="he",  langengname="Hebrew",            license="AGPL-3.0-only",
   doc="README_he_IL.txt",                      cp_dir="he_IL" },
 { lang="hi",  langengname="Hindi",             license="GPL-2.0-or-later",
   doc="README_hi_IN.txt Copyright",            license_file="COPYING",
   cp_dir="hi_IN" },
 { lang="hr",  langengname="Croatian",          license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README_hr_HR.txt",                      cp_dir="hr_HR" },
 { lang="hu",  langengname="Hungarian",         license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README_hu_HU.txt",                      cp_dir="hu_HU" },
 { lang="id",  langengname="Indonesian",        license="LGPL-3.0-or-later",
   license_file="LICENSE-dict",                 cp_dir="id_ID",
   srcdir="id" },
 { lang="is",  langengname="Icelandic",         license="CC-BY-SA-3.0",
   license_file="license.txt",
   filesglob2="is_IS.*" },
 { lang="it",  langengname="Italian",           license="GPL-3.0-only",
   doc="README_it_IT.txt",                      cp_dir="it_??" },
 { lang="kmr", langengname="Kurdish",           license="GPL-3.0-or-later OR LGPL-3.0-or-later OR MPL-1.1",
   doc="README_kmr_Latn.txt license.txt",       cp_dir="kmr_Latn",
   filesglob2="ku_TR.*" },
 { lang="kn",  langengname="Kannada",           license="GPL-2.0-or-later",
   doc="README-kn_IN.txt",                      cp_dir="kn_IN" },
 { lang="ko",  langengname="Korean",            license="GPL-3.0-only",
   doc="README_ko_KR.txt",                      cp_dir="ko_KR" },
 { lang="lo",  langengname="Lao",               license="LGPL-2.1-or-later",
   doc="README_lo_LA.txt",                      cp_dir="lo_LA" },
 { lang="lt",  langengname="Lithuanian",        license="BSD-3-Clause",
   doc="README",                                license_file="COPYING",
   srcdir="lt_LT", filesglob2="lt_LT.*" },
 { lang="lv",  langengname="Latvian",           license="LGPL-2.1-or-later",
   doc="README_lv_LV.txt",                      cp_dir="lv_LV" },
 { lang="mn",  langengname="Mongolian",         license="LPPL-1.3c",
   doc="README_mn_MN.txt",                      license_file="lppl.txt",
   cp_dir="mn_MN" },
 { lang="mr",  langengname="Marathi",           license="GPL-2.0-or-later",
   license_file="COPYING",                      cp_dir="mr_IN" },
 { lang="ne",  langengname="Nepali",            license="LGPL-2.1-or-later",
   doc="README_ne_NP.txt",                      cp_dir="ne_NP" },
 { lang="nl",  langengname="Dutch",             license="BSD-3-Clause OR CC-BY-3.0",
   doc="README.md",                             license_file="LICENSE.txt",
   cp_dir="nl_NL" },
 { lang="nb",  langengname="Norwegian Bokmaal", license="GPL-2.0-or-later",
   cp_dir="nb_NO", srcdir="no" },
 { lang="nn",  langengname="Norwegian Nynorsk", license="GPL-2.0-or-later",
   cp_dir="nn_NO", srcdir="no" },
 { lang="oc",  langengname="Occitan",           license="GPL-2.0-or-later",
   license_file="LICENCES-??.txt",              cp_dir="oc_FR" },
-- discussion going on for license issue in https://bugs.documentfoundation.org/show_bug.cgi?id=171993
 { lang="or",  langengname="Odia",              license="GPL-2.0-or-later",
   cp_dir="or_IN" },
-- discussion going on for license issue in https://bugs.documentfoundation.org/show_bug.cgi?id=171993
 { lang="pa",  langengname="Punjabi",           license="GPL-2.0-or-later",
   cp_dir="pa_IN" },
 { lang="pl",  langengname="Polish",            license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 OR Apache-2.0 OR CC-BY-SA-4.0",
   doc="README_??.txt",                         cp_dir="pl_PL" },
 { lang="pt-BR", langengname="Brazilian Portuguese", license="LGPL-3.0-only OR MPL-1.1",
   supplements="pt_BR",                         doc="README_en.txt README_pt_BR.txt" },
 { lang="pt",  langengname="Portuguese",        license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README_pt_PT.txt",                      license_file="LICENSES.txt",
   cp_dir="pt_PT" },
 { lang="ro",  langengname="Romanian",          license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README_EN.txt",                         license_file="COPYING.*",
   cp_dir="ro_RO", srcdir="ro" },
 { lang="ru",  langengname="Russian",           license="BSD-3-Clause-Modification",
   doc="README_ru_RU.txt",                      cp_dir="ru_RU" },
-- discussion going on for license issue in https://bugs.documentfoundation.org/show_bug.cgi?id=171993
 { lang="sa",  langengname="Sanskrit",          license="GPL-2.0-or-later",
   cp_dir="sa_IN" },
 { lang="si",  langengname="Sinhalese",         license="GPL-3.0-or-later",
   license_file="LICENSES-en.txt",              cp_dir="si_LK" },
 { lang="sk",  langengname="Slovak",            license="GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1",
   doc="README_en.txt README_sk.txt",           license_file="LICENSE.txt",
   cp_dir="sk_SK" },
 { lang="sl",  langengname="Slovenian",         license="GPL-1.0-or-later OR LGPL-2.1-or-later",
   doc="README_sl_SI.txt",                      cp_dir="sl_SI" },
 { lang="sq",  langengname="Albanian",          license="GPL-2.0-or-later",
   doc="README.txt",                            cp_dir="sq_AL" },
 { lang="sr",  langengname="Serbian",           license="GPL-3.0-or-later OR LGPL-3.0-or-later OR MPL-2.0",
   doc="README.txt",                            cp_dir="sr_*",
   filesglob2="sh_??.*", srcdir="sr", cp_skip=true },
 { lang="sv",  langengname="Swedish",           license="LGPL-3.0-only",
   license_file="LICENSE_en_US.txt",            cp_dir="sv_SE",
   srcdir="sv_SE/dictionaries" },
 { lang="sw",  langengname="Swahili",           license="LGPL-2.1-or-later",
   doc="README_sw_TZ.txt",                      cp_dir="sw_TZ" },
 { lang="ta",  langengname="Tamil",             license="MPL-1.1",
   license_file="COPYING",                      cp_dir="ta_IN" },
 { lang="te",  langengname="Telugu",            license="GPL-2.0-or-later",
   doc="README_te_IN.txt",                      cp_dir="te_IN" },
 { lang="th",  langengname="Thai",              license="LGPL-2.1-or-later",
   doc="README_th_TH.txt",                      cp_dir="th_TH" },
 { lang="tr",  langengname="Turkish",           license="MPL-2.0",
   doc="README.txt",                            license_file="LICENSE",
   cp_dir="tr_TR" },
 { lang="uk",  langengname="Ukrainian",         license="MPL-1.1",
   doc="README_uk_UA.txt",                      cp_dir="uk_UA" },
 { lang="vi",  langengname="Vietnamese",        license="GPL-2.0-only",
   license_file="LICENSES-??.txt",              cp_dir="vi_VN",
   srcdir="vi" },
}

-- iterate over all the subpackage definitions
for i = 1, #dicts do
  defdict(dicts[i])
end
}

%prep
%autosetup -n dictionaries-libreoffice-%{version}

## Fix rpmlint issues with below conversion of files
iconv -f iso8859-1 -t utf-8 an_ES/LICENSES-en.txt > an_ES/LICENSES-en.txt.conv && mv -f an_ES/LICENSES-en.txt.conv an_ES/LICENSES-en.txt
iconv -f iso8859-1 -t utf-8 hi_IN/Copyright > hi_IN/Copyright.conv && mv -f hi_IN/Copyright.conv hi_IN/Copyright
iconv -f iso8859-1 -t utf-8 kmr_Latn/README_kmr_Latn.txt > kmr_Latn/README_kmr_Latn.txt.conv && mv -f kmr_Latn/README_kmr_Latn.txt.conv kmr_Latn/README_kmr_Latn.txt
iconv -f iso8859-1 -t utf-8 pt_PT/README_pt_PT.txt > pt_PT/README_pt_PT.txt.conv && mv -f pt_PT/README_pt_PT.txt.conv pt_PT/README_pt_PT.txt
iconv -f iso8859-1 -t utf-8 sw_TZ/README_sw_TZ.txt > sw_TZ/README_sw_TZ.txt.conv && mv -f sw_TZ/README_sw_TZ.txt.conv sw_TZ/README_sw_TZ.txt
iconv -f iso8859-1 -t utf-8 te_IN/README_te_IN.txt > te_IN/README_te_IN.txt.conv && mv -f te_IN/README_te_IN.txt.conv te_IN/README_te_IN.txt
sed -i 's/\r$//' an_ES/LICENSES-en.txt


%build
# nothing to build here

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
## common copy command for many subpackages are now part of install_cmds
%{lua: print(install_cmds) }

## Below languages are defining their own destination file names
## so they can't be minimized in macro

# ar
cp -p ar/ar.* %{buildroot}%{_datadir}/%{dict_dirname}/
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
ar_aliases="ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_TN ar_YE"
for lang in $ar_aliases; do
    ln -s ar.aff $lang.aff
    ln -s ar.dic $lang.dic
done
popd

# be
cp -p be_BY/be-official.aff %{buildroot}%{_datadir}/%{dict_dirname}/be_BY.aff
cp -p be_BY/be-official.dic %{buildroot}%{_datadir}/%{dict_dirname}/be_BY.dic

# ca
cp -p ca/dictionaries/ca.dic %{buildroot}%{_datadir}/%{dict_dirname}/ca_ES.dic
cp -p ca/dictionaries/ca.aff %{buildroot}%{_datadir}/%{dict_dirname}/ca_ES.aff
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
    ln -s ca_ES.aff $lang.aff
    ln -s ca_ES.dic $lang.dic
done
popd

# ckb
cp -p ckb/dictionaries/ckb.dic %{buildroot}%{_datadir}/%{dict_dirname}/ckb_IQ.dic
cp -p ckb/dictionaries/ckb.aff %{buildroot}%{_datadir}/%{dict_dirname}/ckb_IQ.aff

# de
cp -p de/de_AT_frami.aff %{buildroot}%{_datadir}/hunspell/de_AT.aff
cp -p de/de_AT_frami.dic %{buildroot}%{_datadir}/hunspell/de_AT.dic
cp -p de/de_CH_frami.aff %{buildroot}%{_datadir}/hunspell/de_CH.aff
cp -p de/de_CH_frami.dic %{buildroot}%{_datadir}/hunspell/de_CH.dic
cp -p de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_LI.aff
cp -p de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_LI.dic
cp -p de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_DE.aff
cp -p de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_DE.dic
cp -p de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_BE.aff
cp -p de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_BE.dic
cp -p de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_LU.aff
cp -p de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_LU.dic

# es (all variants in one subpackage)
cp -p es/es_*.* %{buildroot}%{_datadir}/%{dict_dirname}

# fa
cp -p fa_IR/fa-IR.dic %{buildroot}%{_datadir}/%{dict_dirname}/fa_IR.dic
cp -p fa_IR/fa-IR.aff %{buildroot}%{_datadir}/%{dict_dirname}/fa_IR.aff

# fr
cp -p fr_FR/dictionaries/fr.dic %{buildroot}%{_datadir}/%{dict_dirname}/fr_FR.dic
cp -p fr_FR/dictionaries/fr.aff %{buildroot}%{_datadir}/%{dict_dirname}/fr_FR.aff
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
    ln -s fr_FR.aff $lang.aff
    ln -s fr_FR.dic $lang.dic
done
popd

# gug
cp -p gug/gug.dic %{buildroot}%{_datadir}/%{dict_dirname}/gug_PY.dic
cp -p gug/gug.aff %{buildroot}%{_datadir}/%{dict_dirname}/gug_PY.aff

# is
cp -p is/is.dic %{buildroot}%{_datadir}/%{dict_dirname}/is_IS.dic
cp -p is/is.aff %{buildroot}%{_datadir}/%{dict_dirname}/is_IS.aff

# it
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s it_IT.aff $lang.aff
        ln -s it_IT.dic $lang.dic
done
popd

# kmr
cp -p kmr_Latn/kmr_Latn.dic %{buildroot}%{_datadir}/%{dict_dirname}/ku_TR.dic
cp -p kmr_Latn/kmr_Latn.aff %{buildroot}%{_datadir}/%{dict_dirname}/ku_TR.aff

# lt
cp -p lt_LT/lt.dic %{buildroot}%{_datadir}/%{dict_dirname}/lt_LT.dic
cp -p lt_LT/lt.aff %{buildroot}%{_datadir}/%{dict_dirname}/lt_LT.aff

# sr
cp -p sr/sr.dic %{buildroot}%{_datadir}/%{dict_dirname}/sr_RS.dic
cp -p sr/sr.aff %{buildroot}%{_datadir}/%{dict_dirname}/sr_RS.aff
cp -p sr/sr-Latn.dic %{buildroot}%{_datadir}/%{dict_dirname}/sr_RS@latin.dic
cp -p sr/sr-Latn.aff %{buildroot}%{_datadir}/%{dict_dirname}/sr_RS@latin.aff
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
sr_RS_aliases="sr_ME"
# bs_BA is now provided by upstream libreoffice dictionaries
sr_RS_latin_aliases="sh_ME sh_RS"
for lang in $sr_RS_aliases; do
    ln -s sr_RS.aff $lang.aff
    ln -s sr_RS.dic $lang.dic
done
for lang in $sr_RS_latin_aliases; do
    ln -s sr_RS@latin.aff $lang.aff
    ln -s sr_RS@latin.dic $lang.dic
done
popd

%changelog
* Wed Aug 12 2026 Parag Nemade <panemade AT redhat DOT com> - 26.8.0.2-3
- Add aliases for required languages

* Tue Aug 11 2026 Parag Nemade <panemade AT redhat DOT com> - 26.8.0.2-2
- Fix more dictionary file names

* Fri Aug 07 2026 Parag Nemade <panemade AT redhat DOT com> - 26.8.0.2-1
- Update to new upstream release 26.8.0.2

* Thu Aug 06 2026 Parag Nemade <panemade AT redhat DOT com> - 26.8.0.1-2
- Further minimize the spec file

* Tue Jul 21 2026 Parag Nemade <panemade AT redhat DOT com> - 26.8.0.1-1
- Update to new upstream release 26.8.0.1

* Tue Jul 07 2026 Parag Nemade <panemade AT redhat DOT com> - 26.2.5.1-3
- Consolidate all es-* subpackages into -es subpackage
- Add source rpm license tag as combined license of binary rpm packages

* Wed Jul 01 2026 Parag Nemade <panemade AT redhat DOT com> - 26.2.5.1-2
- Add bn_BD and en languages from upstream
- Remove Supplements: tag as its not needed

* Tue Jun 30 2026 Parag Nemade <panemade AT redhat DOT com> - 26.2.5.1-1
- Update to new upstream release 26.2.5.1

* Tue Jun 30 2026 Parag Nemade <panemade AT redhat DOT com> - 26.2.4.2-3
- Minimize SPEC file using Lua macro

* Thu Jun 04 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.4.2-2
- Added Conflicts: for Fedora packages

* Thu Jun 04 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.4.2-1
- Update to new upstream release 26.2.4.2
- Changed binary package names from hunspell-xx to libreoffice-dict-xx

* Tue May 19 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.4.1-1
- Update to new upstream release 26.2.4.1
- Added symlinks from Fedora packages

* Wed May 06 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.3.2-1
- Update to new upstream release 26.2.3.2

* Fri May 01 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.3.1-3
- Add all hunspell-es-* subpackages

* Tue Apr 28 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.3.1-2
- Fix some rpmlint issues

* Tue Apr 21 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.3.1-1
- Update to 26.2.3.1

* Tue Apr 14 2026 Parag Nemade <pnemade AT redhat DOT com> - 26.2.2.2-1
- Initial version
- New hunspell packages for languages an, bo, bs, ckb, gug, lo, sa
- Not packaged en dictionaries in this package, let it be independent package
