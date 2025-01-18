Name:           asymptote
Version:        2.89
Release:        5%{?dist}
Summary:        Descriptive vector graphics language

# LGPL-3.0-or-later: the project as a whole
# LGPL-2.0-only:
# - tr.{cc,h}
# LGPL-2.0-or-later:
# - rounding.h
# LGPL-2.1-or-later:
# - getopt.h
# - examples/cpkcolors.asy
# GPL-2.0-or-later:
# - doc/asy-latex.dtx
# - doc/asymptote.sty
# GPL-3.0-or-later WITH Bison-exception-2.2:
# - camp.tab.{cc,h}
# Apache-2.0:
# - base/smoothcontour3.asy
# - LspCpp/src/jsonrpc/Context.cpp
# - LspCpp/src/jsonrpc/RemoteEndPoint.cpp
# - LspCpp/src/lsp/Markup.cpp
# - LspCpp/include/LibLsp/JsonRpc/Context.h
# - LspCpp/include/LibLsp/JsonRpc/ScopeExit.h
# - LspCpp/include/LibLsp/JsonRpc/future.h
# - LspCpp/include/LibLsp/JsonRpc/traits.h
# BSL-1.0:
# - LspCpp/include/LibLsp/JsonRpc/macro_map.h
# MIT:
# - LspCpp (except for the Apache-2.0 and BSL-1.0 files above)
# - base/lmfit.asy
# - gl-matrix-2.4.0-pruned
# BSD-3-Clause:
# - cudareflect/tinyexr
License:        LGPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND Apache-2.0 AND BSL-1.0 AND MIT AND BSD-3-Clause
URL:            https://asymptote.sourceforge.io/
Source0:        https://download.sourceforge.net/sourceforge/asymptote/asymptote-%{version}.src.tgz
Source1:        io.github.vectorgraphics.asymptote.desktop
Source2:        io.github.vectorgraphics.asymptote.metainfo.xml
Patch0:         asymptote-2.84-settings.patch
# This doesn't need to go upstream. We put the info file in the topdir, not a subdir, so we need this fix.
Patch1:         asymptote-2.73-info-path-fix.patch
# Link with flexiblas instead of gslcblas
Patch2:         asymptote-2.89-flexiblas.patch
# Unbundle glew
Patch3:         asymptote-2.89-unbundle-glew.patch

BuildRequires:  gcc-c++
BuildRequires:  bison, flex
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  fftw-devel >= 3.0
BuildRequires:  gc-devel >= 6.8
BuildRequires:  gsl-devel
BuildRequires:  flexiblas-devel
BuildRequires:  tex(latex) tex(epsf.tex)
BuildRequires:  tex(cm-super-t1.enc)
BuildRequires:  tex(media9.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  texlive-dvisvgm
BuildRequires:  ghostscript >= 9.55
BuildRequires:  texinfo-tex
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  libglvnd-devel
BuildRequires:  emacs
BuildRequires:  libtirpc-devel
BuildRequires:  eigen3-static
BuildRequires:  libcurl-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glm-devel
BuildRequires:  boost-devel, rapidjson-devel
BuildRequires:  cmake, make, python3-qt5

Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       hicolor-icon-theme
Requires:       librsvg2-tools
Requires:       tex(latex)
Requires:       texlive-dvisvgm
Requires:       python3-qt5
Requires:       python3-cson
Requires:       python3-numpy
Recommends:     evince, xdg-utils

Provides:       bundled(LspCpp) = 1.0.0
Provides:       bundled(gl-matrix) = 2.4.0
Provides:       bundled(tinyexr) = 1.0.1

%global texpkgdir   %{_texmf}/tex/latex/%{name}

%description
Asymptote is a powerful descriptive vector graphics language for technical
drawings, inspired by MetaPost but with an improved C++-like syntax.
Asymptote provides for figures the same high-quality level of typesetting
that LaTeX does for scientific text.

%prep
%setup -q
%patch -P0 -p1 -b .settings
%patch -P1 -p1 -b .path-fix
%patch -P2 -p1 -b .flexiblas
%patch -P3 -p1 -b .glew
sed -i 's/\r//' doc/CAD1.asy

# Make sure the bundled glew cannot be used
rm -rf GL

# convert to UTF-8
iconv -f iso-8859-1 -t utf-8 -o examples/interpolate1.asy{.utf8,}
mv examples/interpolate1.asy{.utf8,}
autoreconf -i

%build
export CPPFLAGS='-I%{_includedir}/eigen3 -I%{_includedir}/tirpc'
export LIBS='-lflexiblas '
%configure --enable-gc=system --with-docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}/} --with-latex=%{_texmf}/tex/latex --with-context=%{_texmf}/tex/context/ --enable-lsp --enable-offscreen
%make_build
cd doc/
make all

# Generate an SVG icon
../asy -dir ../base -config "" -render=0 -f svg -o icon icon.asy

%install
%make_install 

install -p -m 644 BUGS ChangeLog README ReleaseNotes TODO \
    %{buildroot}%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# Emacs files
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/*.el %{buildroot}%{_emacs_sitelispdir}/%{name}
mv %{buildroot}%{_emacs_sitelispdir}/%{name}/asy-init.el %{buildroot}%{_emacs_sitestartdir}
for i in %{buildroot}%{_emacs_sitelispdir}/%{name}/*.el; do
   %{_emacs_bytecompile} $i
done

# Vim syntax file(s)
install -dm 755 %{buildroot}%{_datadir}/vim/vimfiles/syntax
pushd %{buildroot}%{_datadir}/vim/vimfiles/syntax
ln -s ../../../%{name}/asy.vim .
popd
install -dm 755 %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
pushd %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
ln -s ../../../%{name}/asy_filetype.vim .
popd

# Move info file
mv %{buildroot}%{_infodir}/asymptote/asymptote.info %{buildroot}%{_infodir}/asymptote.info

# Copy icon to scalable icon dir
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p doc/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/asy.svg

# Install the desktop file
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/io.github.vectorgraphics.asymptote.metainfo.xml

# Clean up symlink
rm -rf %{buildroot}%{_bindir}/xasy
cd %{buildroot}%{_bindir}
ln -s ../share/%{name}/GUI/xasy.py xasy

# Fix executable bits
chmod 755 %{buildroot}%{_datadir}/%{name}/{asy-kate.sh,asymptote.py}

%files
%doc %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}/}
%license LICENSE LICENSE.LESSER
%{_bindir}/*
%{_datadir}/%{name}/
%{texpkgdir}/
%{_texmf}/tex/context/
%{_mandir}/man1/*.1*
%{_infodir}/*.info*
%{_datadir}/vim/vimfiles/syntax/asy.vim
%{_datadir}/vim/vimfiles/ftdetect/asy_filetype.vim
%{_datadir}/icons/hicolor/scalable/apps/asy.svg
%{_datadir}/applications/io.github.vectorgraphics.asymptote.desktop
%{_metainfodir}/io.github.vectorgraphics.asymptote.metainfo.xml
%{_emacs_sitestartdir}/*.el
%{_emacs_sitelispdir}/%{name}/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.89-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Jerry James <loganjerry@gmail.com> - 2.89-4
- Fix eigen3, libtirpc, and gsl detection

* Wed Jul 17 2024 Jerry James <loganjerry@gmail.com> - 2.89-3
- Reenable offscreen rendering
- Unbundle glew

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Tom Callaway <spot@fedoraproject.org> - 2.89-1
- update to 2.89
- disable offscreen rendering because it doesn't build with libOSMesa and I cannot see why

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.86-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 2.86-3
- Rebuilt for Boost 1.83

* Mon Aug 28 2023 Jerry James <loganjerry@gmail.com> - 2.86-2
- BR eigen3-devel for Schur decomposition support
- BR libcurl-devel for URL support in the parser
- BR libsigsegv-devel for the stack overflow handler
- Configure with --enable-offscreen, which requires libOSMesa again
- Remove unneeded sources and patches, renumber patches
- Link with flexiblas instead of gslcblas
- Clean up desktop file and add metainfo file
- Remove all traces of XEmacs
- R librsvg2-tools for rsvg-convert
- Add more SPDX license info; use the %%license macro
- Minor spec file cleanups

* Thu Aug  3 2023 Tom Callaway <spot@fedoraproject.org> - 2.86-1
- update to 2.86
- update license tag

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.85-2
- Rebuilt for Boost 1.81

* Thu Feb  9 2023 Tom Callaway <spot@fedoraproject.org> - 2.85-1
- update to 2.85

* Fri Jan 27 2023 Tom Callaway <spot@fedoraproject.org> - 2.84-1
- update to 2.84
- add upstream patch to fix headless Xvfb use case

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Tom Callaway <spot@fedoraproject.org> - 2.83-1
- update to 2.83

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.81-3
- Rebuild for gsl-2.7.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun  1 2022 Tom Callaway <spot@fedoraproject.org> - 2.81-1
- update to 2.81

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.75-4
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Tom Callaway <spot@fedoraproject.org> - 2.75-2
- replace unused BR: mesa-libOSMesa-devel with correct libglvnd-devel

* Tue Jan 11 2022 Tom Callaway <spot@fedoraproject.org> - 2.75-1
- update to 2.75

* Mon Jan  3 2022 Tom Callaway <spot@fedoraproject.org> - 2.74-1
- update to 2.74

* Wed Dec 29 2021 Tom Callaway <spot@fedoraproject.org> - 2.73-1
- update to 2.73

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 2.70-5
- Drop XEmacs support in F36 and later
- Rationalize ownership of (X)Emacs directories

* Thu Jul 29 2021 Tom Callaway <spot@fedoraproject.org> - 2.70-4
- drop obsolete tex(pdftex.map) BR

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Richard Lescak <rlescak@redhat.com> - 2.70-2
- remove old '.setdpfwrite' from ghostscript call in dvipdf(#1968328)

* Mon Mar 15 2021 Tom Callaway <spot@fedoraproject.org> - 2.70-1
- update to 2.70

* Fri Feb 19 2021 Tom Callaway <spot@fedoraproject.org> - 2.69-1
- update to 2.69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Tom Callaway <spot@fedoraproject.org> - 2.68-1
- update to 2.68

* Mon Oct 26 2020 Tom Callaway <spot@fedoraproject.org> - 2.67-4
- applied upstream patch to fix ghostscript problem in better way

* Fri Oct  2 2020 Tom Callaway <spot@fedoraproject.org> - 2.67-3
- apply patch to fix asy with ghostscript 9.53.* or newer

* Fri Oct  2 2020 Tom Callaway <spot@fedoraproject.org> - 2.67-2
- improve vim packaging (bz1884684)

* Thu Aug  6 2020 Tom Callaway <spot@fedoraproject.org> - 2.67-1
- update to 2.67

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  9 2020 Tom Callaway <spot@fedoraproject.org> - 2.66-1
- update to 2.66

* Thu Mar 26 2020 Tom Callaway <spot@fedoraproject.org> - 2.65-1
- update to 2.65

* Wed Mar 11 2020 Tom Callaway <spot@fedoraproject.org> - 2.64-1
- update to 2.64

* Tue Mar  3 2020 Tom Callaway <spot@fedoraproject.org> - 2.63-1
- updaee to 2.63

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Tom Callaway <spot@fedoraproject.org> - 2.62-1
- update to 2.62

* Mon Nov 18 2019 Tom Callaway <spot@fedoraproject.org> - 2.61-1
- update to 2.61

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 2.60-1
- update to 2.60

* Mon Nov  4 2019 Tom Callaway <spot@fedoraproject.org> - 2.59-2
- drop chromium dependency, switch to xdg-utils (xdg-open)

* Mon Oct 21 2019 Tom Callaway <spot@fedoraproject.org> - 2.59-1
- update to 2.59

* Wed Oct 16 2019 Tom Callaway <spot@fedoraproject.org> - 2.58-1
- update to 2.58

* Wed Oct 16 2019 Tom Callaway <spot@fedoraproject.org> - 2.57-1
- update to 2.57

* Tue Oct 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.55-2
- Rebuilt for new freeglut.

* Mon Sep 30 2019 Tom Callaway <spot@fedoraproject.org> - 2.55-1
- update to 2.55
- fix missing numpy dependendency
- add recommends for tools configured in settings

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.52-2
- Rebuilt for GSL 2.6.

* Sat Aug 10 2019 Tom Callaway <spot@fedoraproject.org> - 2.52-1
- update to 2.52

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Tom Callaway <spot@fedoraproject.org> - 2.48-1
- update to 2.48

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.47-4
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  2 2019 Tom Callaway <spot@fedoraproject.org> - 2.47-2
- fix xasy python deps

* Wed Sep  5 2018 Tom Callaway <spot@fedoraproject.org> - 2.47-1
- update to 2.47

* Mon Jul 30 2018 Tom Callaway <spot@fedoraproject.org> - 2.46-1
- update to 2.46

* Tue Jul 24 2018 Tom Callaway <spot@fedoraproject.org> - 2.45-1
- update to 2.45

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 2.44-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Apr 16 2018 Tom Callaway <spot@fedoraproject.org> - 2.44-1
- update to 2.44

* Mon Apr 16 2018 Tom Callaway <spot@fedoraproject.org> - 2.43-1
- update to 2.43

* Fri Mar 30 2018 Tom Callaway <spot@fedoraproject.org> - 2.41-3
- fix issue uncovered by gcc8, thanks to John Bowman and Mamoru Tasaka
- apply segfault fix from upstream
- use libtirpc to enable rpc support
- Resolves FTBFS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Tom Callaway <spot@fedoraproject.org> - 2.41-1
- update to 2.41

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Mar 10 2017 Tom Callaway <spot@fedoraproject.org> - 2.40-1
- update to 2.40

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.38-2
- Rebuild for readline 7.x

* Fri May 13 2016 Tom Callaway <spot@fedoraproject.org> - 2.38-1
- update to 2.38

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.36-2
- Rebuild for gsl 2.1

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> 2.35-5
- spec file cleanup

* Sat Nov 14 2015 Orion Poplawski <orion@cora.nwra.com> 2.35-4
- Add upstream patch for gsl 2 support

* Tue Jun 23 2015 Tom Callaway <spot@fedoraproject.org> 2.35-3
- drop emacs/xemacs subpackages (bz1234576)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Tom Callaway <spot@fedoraproject.org> 2.35-1
- update to 2.35

* Mon May 18 2015 Tom Callaway <spot@fedoraproject.org> 2.34-1
- update to 2.34

* Mon May 11 2015 Tom Callaway <spot@fedoraproject.org> 2.33-1
- update to 2.33

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.32-6
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan  7 2015 Tom Callaway <spot@fedoraproject.org> 2.32-5
- actually apply fix

* Tue Jan  6 2015 Tom Callaway <spot@fedoraproject.org> 2.32-4
- use eps2write instead of epswrite (upstream bug 180)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Tom Callaway <spot@fedoraproject.org> - 2.32-1
- update to 2.32

* Sun May 18 2014 Tom Callaway <spot@fedoraproject.org> - 2.31-1
- 2.31

* Fri May 16 2014 Tom Callaway <spot@fedoraproject.org> - 2.29-1
- update to 2.29

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 2.28-1
- update to 2.28

* Tue Apr 22 2014 Tom Callaway <spot@fedoraproject.org> - 2.25-1
- update to 2.25

* Wed Aug 14 2013 Tom Callaway <spot@fedoraproject.org> - 2.24-2
- use unversioned docdir macros

* Wed Aug 14 2013 Tom Callaway <spot@fedoraproject.org> - 2.24-1
- update to 2.24

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Tom Callaway <spot@fedoraproject.org> - 2.23-1
- update to 2.23

* Fri May 17 2013 Tom Callaway <spot@fedoraproject.org> - 2.22-1
- update to 2.22

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.21-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Thu Jan 31 2013 Tom Callaway <spot@fedoraproject.org> - 2.21-4
- use pillow compatible import (from PIL import foo)

* Tue Oct 23 2012 Tom Callaway <spot@fedoraproject.org> - 2.21-3
- more missing BR, conditionalize texlive hacks

* Sat Oct 20 2012 Jindrich Novy <jnovy@redhat.com> - 2.21-2
- fix (Build)Requires

* Wed Oct 10 2012 Tom Callaway <spot@fedoraproject.org> - 2.21-1
- update to 2.21

* Thu Sep 20 2012 Tom Callaway <spot@fedoraproject.org> - 2.18-1
- update to 2.18

* Thu Sep 20 2012 Tom Callaway <spot@fedoraproject.org> - 2.17-1
- update to 2.17

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Tom Callaway <spot@fedoraproject.org> - 2.16-1
- update to 2.16

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Tom Callaway <spot@fedoraproject.org> - 2.13-1
- update to 2.13

* Fri May 27 2011 Tom Callaway <spot@fedoraproject.org> - 2.10-1
- update to 2.10

* Thu Mar  3 2011 Tom Callaway <spot@fedoraproject.org> - 2.08-4
- no, really, fix info parsing
- breakout emacs subpackages

* Fri Feb 18 2011 Tom Callaway <spot@fedoraproject.org> - 2.08-3
- fix info parsing

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.08-1
- update to 2.08

* Mon Nov  1 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.07-1
- update to 2.07

* Mon Oct 25 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.06-1
- update to 2.06

* Wed Oct 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.05-1
- update to 2.05

* Mon Aug 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.04-1
- update to 2.04

* Thu Aug  5 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.03-1
- update to 2.03

* Thu Jul 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.02-2
- fix man page generation (bz 582010)

* Tue Jul 13 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.02-1
- update to 2.02

* Mon Jul  5 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.01-1
- update to 2.01

* Mon Jun 28 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.00-1
- update to 2.00

* Fri Feb 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.91-1
- update to 1.91

* Thu Nov 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.90-1
- update to 1.90

* Mon Oct  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.88-1
- update to 1.88

* Mon Sep 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.87-2
- fix gcc44 patch

* Mon Sep 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.87-1
- update to 1.87

* Sun Sep  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.86-1
- update to 1.86

* Mon Aug 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.85-1
- update to 1.85

* Thu Aug 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.84-1
- update to 1.84

* Mon Aug 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.83-1
- update to 1.83

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.82-1
- update to 1.82

* Fri Jul 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.80-1
- update to 1.80

* Wed Jul  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.78-2
- disable pdf generation in rawhide

* Wed Jul  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.78-1
- update to 1.78

* Mon May 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.73-1
- update to 1.73
- change license from GPLv3+ to LGPLv3+

* Mon Apr 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.70-1
- update to 1.70

* Tue Apr  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.69-1
- update to 1.69

* Wed Mar 25 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.68-1
- update to 1.68

* Thu Mar 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.67-1
- update to 1.67

* Fri Feb 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.66-1
- update to 1.66

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.63-4
- more gcc44 fixes with BIG_ENDIAN platforms

* Wed Feb 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.63-3
- fix gcc44 issue with BIG_ENDIAN platforms

* Wed Feb 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.63-2
- forgot to put in new source

* Wed Feb 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.63-1
- 1.63

* Fri Jan 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.60-1
- 1.60

* Mon Jan 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.59-1
- 1.59

* Mon Jan 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.58-1
- 1.58

* Mon Dec 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.57-1
- 1.57

* Tue Dec  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.56-1
- 1.56

* Tue Dec  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.54-1
- 1.54

* Tue Nov 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.52-1
- 1.52

* Tue Nov 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.51-1
- update to 1.51

* Mon Nov  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.49-1
- update to 1.49

* Sun Oct 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.47-1
- update to 1.47

* Mon Oct 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.46-1
- update to 1.46

* Mon Oct  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.44-2
- add missing BuildRequires

* Mon Oct  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.44-1
- update to 1.44

* Fri Jun 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.43-1
- update to 1.43

* Fri Apr 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.42-3
- explicitly call "make asymptote.pdf" in doc/

* Fri Apr  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.42-2
- fix build failure (use _POSIX_ARG_MAX) resolves bz 440799

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.42-1
- update to 1.42

* Wed Feb  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.41-1
- update to 1.41
- enable desktop file for xasy

* Thu Jan  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.37-1
- bump to 1.37
- fix gcc43 failures
- drop triggers

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - sh: kpsewhich: command not found
- Rebuild for selinux ppc32 issue.

* Sun Jul 29 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.33-1
- Update 1.33.

* Sat Jun 30 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.32-1
- Update to 1.32.
- vim-common triggers: correction and improvements (#246131).

* Wed Jun 27 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.31-1
- Update to 1.31.

* Sat Jun 16 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.30-1
- Update to 1.30.

* Sat Jun 16 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.29-3
- Using "evince" as the default PS and PDF viewers (#244151).
  (patch file: asymptote-1.29-settings.patch)
- Use relative symbolic links in the {emacs,xemacs}-common triggers (#155750).
- Use relative symbolic links in the vim-common triggers.

* Sat Jun  2 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.29-2
- Add asy-faq to install-info (#155750).
- Add support for vim 7.1.

* Mon May 21 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.29-1
- Update to 1.29.

* Tue May  8 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.28-1
- Update to 1.28.

* Sat May  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.27-1
- Update to 1.27.

* Wed Apr 25 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.26-1
- Update to 1.26.

* Tue Apr 10 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.25-1
- Update to 1.25.

* Sun Apr  1 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.24-1
- Update to 1.24.

* Sun Mar 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.23-1
- Update to 1.23.

* Tue Mar  6 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.22-1
- Update to 1.22.

* Sat Mar  3 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.21-1
- Update to 1.21.

* Fri Dec 29 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.20-1
- Update to 1.20.

* Sat Dec 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.19-1
- Update to 1.19.

* Sun Nov  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.18-1
- Update to 1.18.

* Wed Nov  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.17-1
- Update to 1.17.

* Wed Oct 25 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.16-1
- Update to 1.16.

* Sun Oct 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.15-1
- Update to 1.15.

* Wed Sep  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.13-1
- Update to 1.13.

* Thu Aug  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-1
- Update to 1.12.

* Thu Jul  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.11-1
- Update to 1.11.

* Wed Jun 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.10-1
- Update to 1.10.

* Fri Jun 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.09-1
- Update to 1.09.

* Thu Jun 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-1
- Update to 1.08.
- Also installs the info file.

* Mon May 29 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-5
- Fedora Core 6: the texinfo package has been splitted (texinfo + texinfo-tex).

* Sat May 27 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-4
- Group: Development/Tools -> Applications/Publishing (#193154).

* Sat May 27 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-3
- Emacs/Xemacs init file (#193154 comment 6).

* Fri May 26 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-2
- Directories ownership (#193154).

* Wed May 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-1
- Update to 1.06.
- Using triggers to install the Vim syntax file and the Emacs/Xemacs mode file.

* Mon May 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-1
- Update to 1.05.

* Sun May  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-1
- Update to 1.04.

* Fri Mar 31 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-1
- Update to 1.03.

* Thu Mar 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.02-1
- First build.

# vim:set ai ts=4 sw=4 sts=4 et:
