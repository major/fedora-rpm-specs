%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-formatsextra
Epoch:          12
Version:        svn72250
Release:        4%{?dist}
Summary:        Additional formats

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-formatsextra.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antomega.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antomega.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lambda.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mxedruli.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mxedruli.doc.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/omega.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/omega.doc.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/otibet.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/otibet.doc.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/passivetex.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psizzl.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psizzl.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/startex.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/startex.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-aleph
Requires:       texlive-antomega
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-eplain
Requires:       texlive-hitex
Requires:       texlive-jadetex
Requires:       texlive-lambda
Requires:       texlive-lollipop
Requires:       texlive-mltex
Requires:       texlive-mxedruli
Requires:       texlive-omega
Requires:       texlive-omegaware
Requires:       texlive-otibet
Requires:       texlive-passivetex
Requires:       texlive-psizzl
Requires:       texlive-startex
Requires:       texlive-texsis
Requires:       texlive-xmltex

%description
Collected TeX `formats', i.e., large-scale macro packages designed to be dumped
into .fmt files -- excluding the most common ones, such as latex and context,
which have their own package(s). It also includes the Aleph engine and related
Omega formats and packages, and the HiTeX engine and related.


%package -n texlive-antomega
Summary:        Alternative language support for Omega/Lambda
Version:        svn21933
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-omega
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Provides:       tex(antomega.sty) = %{tl_version}
Provides:       tex(grhyph16.tex) = %{tl_version}
Provides:       tex(lgc0700.def) = %{tl_version}
Provides:       tex(lgrenc-antomega.def) = %{tl_version}
Provides:       tex(ograhyph4.tex) = %{tl_version}
Provides:       tex(ogrmhyph4.tex) = %{tl_version}
Provides:       tex(ogrphyph4.tex) = %{tl_version}
Provides:       tex(omega-english.ldf) = %{tl_version}
Provides:       tex(omega-french.ldf) = %{tl_version}
Provides:       tex(omega-german.ldf) = %{tl_version}
Provides:       tex(omega-greek.ldf) = %{tl_version}
Provides:       tex(omega-latin.ldf) = %{tl_version}
Provides:       tex(omega-latvian.ldf) = %{tl_version}
Provides:       tex(omega-polish.ldf) = %{tl_version}
Provides:       tex(omega-russian.ldf) = %{tl_version}
Provides:       tex(omega-spanish.ldf) = %{tl_version}
Provides:       tex(ruhyph16.tex) = %{tl_version}
Provides:       tex(t1enc-antomega.def) = %{tl_version}
Provides:       tex(t2aenc-antomega.def) = %{tl_version}
Provides:       tex(uni0100.def) = %{tl_version}
Provides:       tex(uni0370.def) = %{tl_version}
Provides:       tex(uni0400.def) = %{tl_version}
Provides:       tex(uni1f00.def) = %{tl_version}
Provides:       tex(ut1enc-antomega.def) = %{tl_version}

%description -n texlive-antomega
A language support package for Omega/Lambda. This replaces the original omega
package for use with Lambda, and provides extra facilities (including
Babel-like language switching, which eases porting of LaTeX documents to
Lambda).

%package -n texlive-lambda
Summary:        LaTeX for Omega and Aleph
Version:        svn45756
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(elhyph16.tex) = %{tl_version}
Provides:       tex(grcodes.tex) = %{tl_version}
Provides:       tex(grmhyph.tex) = %{tl_version}
Provides:       tex(lambda.tex) = %{tl_version}
Provides:       tex(lchenc.def) = %{tl_version}
Provides:       tex(ocherokee.sty) = %{tl_version}
Provides:       tex(odev.sty) = %{tl_version}
Provides:       tex(ojapan.sty) = %{tl_version}
Provides:       tex(omega.sty) = %{tl_version}
Provides:       tex(ut1enc.def) = %{tl_version}

%description -n texlive-lambda
LaTeX for Omega and Aleph

%package -n texlive-mxedruli
Summary:        A pair of fonts for different Georgian alphabets
Version:        svn71991
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mxedruli.sty) = %{tl_version}
Provides:       tex(xucuri.sty) = %{tl_version}

%description -n texlive-mxedruli
Two Georgian fonts, in both Metafont and Type 1 formats, which cover the
Mxedruli and the Xucuri alphabets.

%package -n texlive-omega
Summary:        A wide-character-set extension of TeX
Version:        svn33046
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bghyph.tex) = %{tl_version}
Provides:       tex(grlccode.tex) = %{tl_version}
Provides:       tex(lthyph.tex) = %{tl_version}
Provides:       tex(omega.tex) = %{tl_version}
Provides:       tex(srhyph.tex) = %{tl_version}

%description -n texlive-omega
A development of TeX, which deals in multi-octet Unicode characters, to enable
native treatment of a wide range of languages without changing character-set.
Work on Omega has ceased (the TeX Live package contains only support files);
its compatible successor is aleph, which is itself also in major maintenance
mode only. Ongoing projects developing Omega (and Aleph) ideas include Omega-2
and LuaTeX.

%package -n texlive-otibet
Summary:        Support for Tibetan using Omega
Version:        svn45777
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(otibet.sty) = %{tl_version}
Provides:       tex(otibet.tex) = %{tl_version}

%description -n texlive-otibet
support for Tibetan using Omega

%package -n texlive-passivetex
Summary:        Support package for XML/SGML typesetting
Version:        svn69742
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(bm.sty)
Requires:       tex(color.sty)
# Ignoring dependency on elfonts.sty - not part of TeX Live
Requires:       tex(eucal.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pifont.sty)
Requires:       tex(rotating.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(times.sty)
Requires:       tex(tipa.sty)
Requires:       tex(tone.sty)
Requires:       tex(ulem.sty)
Requires:       tex(url.sty)
Requires:       tex(wasysym.sty)
Provides:       tex(dummyels.sty) = %{tl_version}
Provides:       tex(fotex.sty) = %{tl_version}
Provides:       tex(mlnames.sty) = %{tl_version}
Provides:       tex(teixml.sty) = %{tl_version}
Provides:       tex(teixmlslides.sty) = %{tl_version}
Provides:       tex(ucharacters.sty) = %{tl_version}
Provides:       tex(unicode.sty) = %{tl_version}

%description -n texlive-passivetex
Packages providing XML parsing, UTF-8 parsing, Unicode entities, and common
formatting object definitions for jadetex.

%package -n texlive-psizzl
Summary:        A TeX format for physics papers
Version:        svn69742
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mypsizzl.tex) = %{tl_version}
Provides:       tex(psizzl.tex) = %{tl_version}

%description -n texlive-psizzl
PSIZZL is a TeX format for physics papers written at SLAC and used at several
other places. It dates from rather early in the development of TeX82; as a
result, some of the descriptions of limitations look rather quaint to modern
eyes.

%package -n texlive-startex
Summary:        An XML-inspired format for student use
Version:        svn69742
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(startex.tex) = %{tl_version}

%description -n texlive-startex
A TeX format designed to help students write short reports and essays. It
provides the user with a suitable set of commands for such a task. It is also
more robust than plain TeX and LaTeX.


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-antomega
%license lppl1.3c.txt
%{_texmf_main}/omega/ocp/antomega/
%{_texmf_main}/omega/otp/antomega/
%{_texmf_main}/tex/lambda/antomega/
%doc %{_texmf_main}/doc/omega/antomega/

%files -n texlive-lambda
%license lppl1.3c.txt
%{_texmf_main}/tex/lambda/base/
%{_texmf_main}/tex/lambda/config/

%files -n texlive-mxedruli
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/mxedruli/
%{_texmf_main}/fonts/map/dvips/mxedruli/
%{_texmf_main}/fonts/source/public/mxedruli/
%{_texmf_main}/fonts/tfm/public/mxedruli/
%{_texmf_main}/fonts/type1/public/mxedruli/
%{_texmf_main}/tex/latex/mxedruli/
%doc %{_texmf_main}/doc/fonts/mxedruli/

%files -n texlive-omega
%license gpl2.txt
%{_texmf_main}/dvips/omega/
%{_texmf_main}/fonts/afm/public/omega/
%{_texmf_main}/fonts/map/dvips/omega/
%{_texmf_main}/fonts/ofm/public/omega/
%{_texmf_main}/fonts/ovf/public/omega/
%{_texmf_main}/fonts/ovp/public/omega/
%{_texmf_main}/fonts/tfm/public/omega/
%{_texmf_main}/fonts/type1/public/omega/
%{_texmf_main}/omega/ocp/char2uni/
%{_texmf_main}/omega/ocp/misc/
%{_texmf_main}/omega/ocp/omega/
%{_texmf_main}/omega/ocp/uni2char/
%{_texmf_main}/omega/otp/char2uni/
%{_texmf_main}/omega/otp/misc/
%{_texmf_main}/omega/otp/omega/
%{_texmf_main}/omega/otp/uni2char/
%{_texmf_main}/tex/generic/encodings/
%{_texmf_main}/tex/generic/omegahyph/
%{_texmf_main}/tex/plain/omega/
%doc %{_texmf_main}/doc/omega/base/

%files -n texlive-otibet
%license lppl1.3c.txt
%{_texmf_main}/fonts/ofm/public/otibet/
%{_texmf_main}/fonts/ovf/public/otibet/
%{_texmf_main}/fonts/ovp/public/otibet/
%{_texmf_main}/fonts/source/public/otibet/
%{_texmf_main}/fonts/tfm/public/otibet/
%{_texmf_main}/omega/ocp/otibet/
%{_texmf_main}/omega/otp/otibet/
%{_texmf_main}/tex/latex/otibet/
%doc %{_texmf_main}/doc/latex/otibet/

%files -n texlive-passivetex
%license mit.txt
%{_texmf_main}/tex/xmltex/passivetex/

%files -n texlive-psizzl
%license lppl1.3c.txt
%{_texmf_main}/tex/psizzl/base/
%{_texmf_main}/tex/psizzl/config/
%doc %{_texmf_main}/doc/otherformats/psizzl/

%files -n texlive-startex
%license pd.txt
%{_texmf_main}/makeindex/startex/
%{_texmf_main}/tex/startex/
%doc %{_texmf_main}/doc/otherformats/startex/

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn72250-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn72250-3
- fix license tags
- fix descriptions
- capitalize summaries

* Thu Oct 09 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72250-2
- regenerate, no deps from docs

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72250-1
- Update to TeX Live 2025
