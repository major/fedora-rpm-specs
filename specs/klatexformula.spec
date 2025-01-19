# The soversion for the included libraries
%define libver    4

Name:             klatexformula
Version:          4.1.0
Release:          11%{?dist}
Summary:          Application for easy image creating from a LaTeX equation
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              http://klatexformula.sourceforge.net/
Source0:          http://downloads.sourceforge.net/klatexformula/%{name}-%{version}.tar.gz

# Backported from upstream commit 513ce8f47293d3acaaaf5ee3efe2aabedbca8d1b
# (https://github.com/klatexformula/klatexformula/commit/513ce8f47293d3acaaaf5ee3efe2aabedbca8d1b)
Patch0:           painter_path.patch

BuildRequires:    qt5-qtbase-devel
BuildRequires:    kf5-plasma-devel
BuildRequires:    qt5-qttools-static
BuildRequires:    qt5-qtsvg-devel
BuildRequires:    qt5-qtx11extras-devel
BuildRequires:    desktop-file-utils
BuildRequires:    doxygen
BuildRequires:    help2man
BuildRequires:    graphviz
BuildRequires:    python3-devel
BuildRequires:    make
Requires:         texlive-latex
Requires:         hicolor-icon-theme

# Recommend the dvisvgm program as a way of creating SVG files from the latex input
Recommends:       texlive-dvisvgm

%description
This application provides a GUI for writing and generating an image
(e.g. PNG, JPG, BMP, etc.) from a LaTeX equation. The images can be dragged
and dropped or copied and pasted into other applications, or can be saved
to disk.

A command-line mode is available (e.g. for scripts) using the klatexformula_cmdl
executable.


%package -n libklatexformula
Summary:          Backend and tools libraries provided by KLatexFormula
Obsoletes:        libklfbackend < 4.0.0
Provides:         libklfbackend = %{version}

%description -n libklatexformula
C++/QT libraries containing functionality from klatexformula, including the klfbackend
library for integrating klatexformula functionality into other programs, and general
purpose tools that were written for klatexformula but have now been made into a library
for use in any application.


%package -n libklatexformula-devel
Summary:          Development files for libklatexformula
Requires:         qt5-qtbase-devel
Requires:         libklatexformula%{?_isa} = %{version}-%{release}
Obsoletes:        %{name}-devel < 4.0.0
Provides:         %{name}-devel = %{version}
Obsoletes:        libklfbackend-devel < 4.0.0
Provides:         libklfbackend-devel = %{version}

%description -n libklatexformula-devel
Development files for libklatexformula.


%package -n libklatexformula-static
Summary:          Static library for libklatexformula
Requires:         qt5-qtbase-devel
Requires:         libklatexformula-devel%{?_isa} = %{version}-%{release}

%description -n libklatexformula-static
Static library for the klfbackend library provided by libklatexformula.


%prep
%autosetup -p1

%build
%{cmake_kf5} \
        -DCMAKE_SKIP_RPATH=ON \
        -DKLF_LIBKLFAPP_STATIC=OFF \
        -DKLF_LIBKLFBACKEND_STATIC=OFF \
        -DKLF_LIBKLFTOOLS_STATIC=OFF \
        -DKLF_INSTALL_POST_UPDATEMIMEDATABASE=OFF \
        -DKLF_INSTALL_SHARE_PIXMAPS_DIR="" \
        -DKLF_NO_CMU_FONT=ON \
        -DKLF_INSTALL_LIB_DIR=%{_libdir} \
        -DKLF_INSTALL_KLFTOOLSDESPLUGIN=YES \
        -DKLF_INSTALL_ICON_THEME=%{_datadir}/icons/hicolor/ \
        -DKLF_INSTALL_DESKTOP_CATEGORIES="Qt;Office;" \
        -DKLF_INSTALL_DESKTOP_ICON="%{name}" \
        -DKLF_INSTALL_DESPLUGIN_DIR=%{_qt5_plugindir}/designer/ \
        %{nil}
%cmake_build

%install
%cmake_install

# Byte compile the user script interface
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/userscripts/pyklfuserscript


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS README
%license COPYING.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/mime/packages/klatexformula-mime.xml
%{_mandir}/man1/klatexformula*

%files -n libklatexformula
%doc AUTHORS README
%license COPYING.txt
%{_libdir}/libklftools.so.%{libver}
%{_libdir}/libklfbackend.so.%{libver}

%files -n libklatexformula-devel
%doc AUTHORS README
%license COPYING.txt
%{_libdir}/libklftools.so
%{_libdir}/libklfbackend.so
%{_qt5_plugindir}/designer/libklftoolsdesplugin.so
%{_includedir}/klftools
%{_includedir}/klfbackend
%{_docdir}/%{name}/apidoc/*

%files -n libklatexformula-static
%doc AUTHORS README
%license COPYING.txt
%{_libdir}/libklfbackend*.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.0-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Ian McInerney <ian.s.mcinerney@ieee.org> - 4.1.0-1
- Add a Recommends on texlive-dvisvgm to allow SVG output
- Update to version 4.1.0 (BZ#1837014)
- Fix FTBFS on QT 5.15 (BZ#1863946)
- Move all libraries into new libklatexformula package
- Split klfbackend static library into new libklatexformula-static package to follow packaging guidelines
- Move the API docs into libklatexformula-devel subpackage
- Readd debuginfo package generation
- Spec file cleanup (remove outdated macro definitions)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.0.0-8
- cleanup qt5 deps (mostly replacing qt5-devel with qt5-qtbase-devel)
- tighten subpkg dep with %%{?_isa}

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-4
- added graphviz as BR

* Thu Sep 20 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-3
- Fix FTBFS rhbz #1604508 (thanks to Juhani Numminen)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-1
- New upstream release 4.0.0
- Build with qt5
- Spec cleanup / modernization
- Fixes rhbz #1136243 and rhbz #1423816

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.10-10
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.2.10-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 3.2.10-3
- minor .spec cleanup, update scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.10-1
- klatexformula 3.2.10

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun  4 2014 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.9-2
- rebuild

* Thu May 15 2014 Filipe Rosset <rosset.filipe@gmail.com> - 3.2.9-1
- New upstream version 3.2.9 + spec cleanup
- Removed patches (already included in upstream)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.3-4
- fix build with gcc-4.7.0

* Tue Apr 26 2011 Dan Horák <dan[at]danny.cz> - 3.2.3-3
- the buildsystem sets the proper 64/32-bit compile flags (fixes build on s390)

* Wed Apr 13 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.3-2
- require qt4 version used at build time

* Wed Apr 13 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.3-1
- update to 3.2.3

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec  4 2010 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.2-1
- update to 3.2.2
- set KLF_NO_CMU_FONT for using system fonts by default
- BR: help2man

* Sun Oct 10 2010 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Wed Sep 29 2010 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- added devel and ktexteditor-plugin subpackages

* Sun Nov 22 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.1.2-1
- update to 3.1.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.1-3
- build with shared libraries
- fixed license tag
- libklfbackend subpackage
- fix build with GCC 4.4

* Mon May  4 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.1-2
- changed Requires to texlive-latex
- added Requires hicolor-icon-theme
- removed license tag in devel subpackage
- added Provides -static in devel subpackage

* Mon May  4 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.1-1
- Initial RPM release
