Name:           cppcheck
Version:        2.18.0
Release:        1%{?dist}
Summary:        Tool for static C/C++ code analysis
License:        GPL-3.0-or-later
URL:            http://cppcheck.sourceforge.io/
Source0:        https://github.com/danmar/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Fix location of translations
Patch0:         cppcheck-2.11-translations.patch

BuildRequires:  gcc-c++
BuildRequires:  pcre-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  pandoc
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  tinyxml2-devel >= 2.1.0
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-linguist
BuildRequires:  make
BuildRequires:  boost-devel

%description
Cppcheck is a static analysis tool for C/C++ code. Unlike C/C++
compilers and many other analysis tools it does not detect syntax
errors in the code. Cppcheck primarily detects the types of bugs that
the compilers normally do not detect. The goal is to detect only real
errors in the code (i.e. have zero false positives).

%package gui
Summary:        Graphical user interface for cppcheck
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gui
This package contains the graphical user interface for cppcheck.

%package htmlreport
Summary:        HTML reporting for cppcheck
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-pygments

%description htmlreport
This package contains the Python utility for generating html reports
from xml files first generated using cppcheck.

%prep
%setup -q
%patch -P 0 -p1 -b .translations
# Make sure bundled tinyxml2 is not used
rm -r externals/tinyxml2
# Generate the Qt online-help file
cd gui/help
%{_qt6_libexecdir}/qhelpgenerator online-help.qhcp -o online-help.qhc

%build
# Manuals
make DB2MAN=/usr/share/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl man
pandoc man/manual.md -o man/manual.html -s --number-sections --toc
pandoc man/reference-cfg-format.md -o man/reference-cfg-format.html -s --number-sections --toc

# Binaries
# Upstream doesn't support shared libraries (unversioned solib)
%cmake -DCMAKE_BUILD_TYPE=Release -DUSE_MATCHCOMPILER=ON -DHAVE_RULES=yes -DBUILD_GUI=1 -DUSE_QT6=1 -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_TESTS=yes -DFILESDIR=%{_datadir}/Cppcheck -DUSE_BUNDLED_TINYXML2=OFF -DENABLE_OSS_FUZZ=OFF -DUSE_BOOST=1
%ifarch i686
export RPM_BUILD_NCPUS=1
%endif
%cmake_build

%install
%cmake_install
install -D -p -m 644 cppcheck.1 %{buildroot}%{_mandir}/man1/cppcheck.1
# Install desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/cppcheck-gui.desktop
# Install logo
install -D -p -m 644 gui/cppcheck-gui.png %{buildroot}%{_datadir}/pixmaps/cppcheck-gui.png
# Install the Qt online-help file
install -D -p -m 644 gui/help/online-help.qhc %{buildroot}%{_datadir}/Cppcheck/help/online-help.qhc
install -D -p -m 644 gui/help/online-help.qch %{buildroot}%{_datadir}/Cppcheck/help/online-help.qch
# Install htmlreport
install -D -p -m 755 htmlreport/cppcheck-htmlreport %{buildroot}%{_bindir}/cppcheck-htmlreport
# Restore execute permission of python files
grep -l "#\!/usr/bin/env python3" %{buildroot}%{_datadir}/Cppcheck/addons/*.py | xargs chmod +x

%check
%ifarch i686
%ctest -E "TestCppcheck|TestCondition|TestCmdlineParser|TestFileLister"
%else
%ctest -E "TestCppcheck|TestCondition"
%endif

%files
%doc AUTHORS man/manual.html man/reference-cfg-format.html
%license COPYING
%{_datadir}/Cppcheck/
%{_bindir}/cppcheck
%{_mandir}/man1/cppcheck.1*

%files gui
%{_bindir}/cppcheck-gui
%{_datadir}/applications/cppcheck-gui.desktop
%{_datadir}/pixmaps/cppcheck-gui.png
%{_datadir}/icons/hicolor/64x64/apps/cppcheck-gui.png
%{_datadir}/icons/hicolor/scalable/apps/cppcheck-gui.svg

%files htmlreport
%{_bindir}/cppcheck-htmlreport

%changelog
* Mon Jul 21 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.18.0-1
- 2.18.0

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu May 15 2025 Troy Dawson <tdawson@redhat.com> - 2.17.1-2
- Change from qt5 to qt6

* Sat Mar 22 2025 Wolfgang Stöggl <c72578@yahoo.de> - 2.17.1-1
- 2.17.1

* Sun Feb 23 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.17.0-1
- 2.17.0

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 28 2024 Wolfgang Stöggl <c72578@yahoo.de> - 2.16.2-1
- 2.16.2

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 2.16.0-2
- rebuild for tinyxml2

* Mon Oct 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.16.0-1
- 2.16.0

* Sat Aug 31 2024 Wolfgang Stöggl <c72578@yahoo.de> - 2.15.0-1
- Update to 2.15.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 22 2024 Wolfgang Stöggl <c72578@yahoo.de> - 2.14.2-1
- Update to 2.14.2

* Sun May 26 2024 Wolfgang Stöggl <c72578@yahoo.de> - 2.14.1-1
- Update to 2.14.1

* Thu Apr 25 2024 Wolfgang Stöggl <c72578@yahoo.de> - 2.14.0-1
- Update to 2.14.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 23 2023 Wolfgang Stöggl <c72578@yahoo.de> - 2.13.0-1
- Update to 2.13.0

* Wed Sep 20 2023 Wolfgang Stöggl <c72578@yahoo.de> - 2.12.1-1
- Update to 2.12.1

* Tue Sep 12 2023 Wolfgang Stöggl <c72578@yahoo.de> - 2.12.0-2
- Add "-fsigned-char" to CXXFLAGS, to make tests pass

* Sun Sep 10 2023 Wolfgang Stöggl <c72578@yahoo.de> - 2.12.0-1
- Update to 2.12.0 (#2165211)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Steve Grubb <sgrubb@redhat.com> - 2.11-1
- Update to 2.11
- Disable tests (2 style tests failing)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Steve Grubb <sgrubb@redhat.com> - 2.9-3
- SPDX Migration

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 2.9-2
- Rebuild for tinyxml2-9.0.0

* Sun Aug 28 2022 Wolfgang Stöggl <c72578@yahoo.de> - 2.9-1
- Update to 2.9

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Wolfgang Stöggl <c72578@yahoo.de> - 2.8.2-1
- Update to 2.8.2

* Wed May 25 2022 Wolfgang Stöggl <c72578@yahoo.de> - 2.8-1
- Update to 2.8

* Thu May 19 2022 Jerry James <loganjerry@gmail.com> - 2.7.4-2
- Rebuild for z3 4.8.17

* Fri Mar 25 2022 Wolfgang Stöggl <c72578@yahoo.de> - 2.7.4-1
- Update to 2.7.4

* Wed Mar 23 2022 Wolfgang Stöggl <c72578@yahoo.de> - 2.7.3-2
- Update tinyxml2 patch, add upstream link and rebuild

* Sat Mar 19 2022 Wolfgang Stöggl <c72578@yahoo.de> - 2.7.3-1
- Update to 2.7.3.

* Tue Feb 08 2022 Wolfgang Stöggl <c72578@yahoo.de> - 2.7-1
- Update to 2.7.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 02 2021 Wolfgang Stöggl <c72578@yahoo.de> - 2.6-1
- Update to 2.6.

* Fri Jul 23 2021 Wolfgang Stöggl <c72578@yahoo.de> - 2.5-3
- Fix Failed to load translation for English (#1983599)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Wolfgang Stöggl <c72578@yahoo.de> - 2.5-1
- Update to 2.5.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Timm Bäder <tbaeder@redhat.com> - 2.3-2
- Explicitly disable oss-fuzz

* Sat Dec 05 2020 Wolfgang Stöggl <c72578@yahoo.de> - 2.3-1
- Update to 2.3.

* Sun Nov 08 2020 Wolfgang Stöggl <c72578@yahoo.de> - 2.2-5
- Add cppcheck-2.2-online-help_q_readonly.patch

* Thu Oct 22 2020 Wolfgang Stöggl <c72578@yahoo.de> - 2.2-4
- Fix missing Contents and Index in Qt online-help file

* Tue Oct 13 2020 Jeff Law <law@redhat.com> - 2.2-3
- Fix missing #include for gcc-11

* Sun Oct 11 2020 Wolfgang Stöggl <c72578@yahoo.de> - 2.2-2
- Fix Helpfile 'online-help.qhc' was not found

* Sun Oct 04 2020 Wolfgang Stöggl <c72578@yahoo.de> - 2.2-1
- Update to 2.2.

* Tue Aug 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1-7
- Gui package is always built.

* Tue Aug 04 2020 Wolfgang Stöggl <c72578@yahoo.de> - 2.1-6
- Fix FTBFS #1863368

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1-3
- Drop EPEL specifics since cppcheck is included in RHEL8.

* Tue Jun 16 2020 Wolfgang Stöggl <c72578@yahoo.de> - 2.1-2
- Enable Z3 on Fedora builds.

* Mon Jun 15 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1-1
- Update to 2.1.

* Mon May 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0-1
- Update to 2.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Wolfgang Stöggl <c72578@yahoo.de> - 1.90-4
- Use python3 on EPEL7

* Mon Dec 23 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.90-3
- Fix typo in CMake flag (Stöggl's pull request #3).

* Sat Dec 21 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.90-2
- Adaptations to build also on EPEL 7.

* Sat Dec 21 2019 Wolfgang Stöggl <c72578@yahoo.de> - 1.90-1
- New upstream version 1.90

* Thu Dec 12 2019 Steve Grubb <sgrubb@redhat.com> - 1.89-2
- Add "-fsigned-char" to CXXFLAGS, to make tests pass
- https://trac.cppcheck.net/ticket/9359

* Sat Dec 07 2019 Steve Grubb <sgrubb@redhat.com> - 1.89-1
- New upstream release 1.89

* Fri Aug 16 2019 Susi Lehtola <susi.lehtola@iki.fi> - 1.88-5
- rebuilt

* Wed Aug 14 2019 Susi Lehtola <jussilehtola@redhat.com> - 1.88-5
- Switch to python3 in htmlreport (BZ #1737972).

* Mon Jul 29 2019 Susi Lehtola <jussilehtola@redhat.com> - 1.88-4
- Second patch for another issue in BZ #1733663.

* Sat Jul 27 2019 Susi Lehtola <jussilehtola@redhat.com> - 1.88-3
- Fix BZ #1733663.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Steve Grubb <sgrubb@redhat.com> - 1.88-1
- Update to 1.88

* Sat Feb 09 2019 Steve Grubb <sgrubb@redhat.com> - 1.87-1
- Update to 1.87.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Steve Grubb <sgrubb@redhat.com> - 1.86-1
- Update to 1.86.

* Tue Nov 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.85-2
- Rebuild for tinyxml2 7.x

* Thu Nov 08 2018 Steve Grubb <sgrubb@redhat.com> - 1.85-1
- Update to 1.85.

* Tue Sep 11 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.84-1
- Update to 1.84.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.83-3
- Add htmlreport tool.

* Thu May 17 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.83-2
- Qt5 is available on RHEL 7 after all, re-enable gui in EPEL 7.

* Sat Apr 14 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.83-1
- GUI no longer available on RHEL 7 due to Qt5 dependency.
- Update to 1.83.

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.81-5
- Added gcc-c++ buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Björn Esser <besser82@fedoraproject.org> - 1.81-3
- Rebuilt for tinyxml2 soname/ABI change again

* Tue Jan 23 2018 François Cami <fcami@fedoraproject.org> - 1.81-2
- Rebuilt for tinyxml2 soname/ABI change

* Wed Oct 18 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.81-1
- Update to 1.81.

* Tue Aug 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.80-1
- 1.80

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.79-1
- Update to 1.79.

* Sun Apr 09 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.78-1
- Make cppcheck able to find its configs once again (bug 1427788).
- Update to 1.78.

* Mon Feb 27 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.77-4
- Remove Patch2: fixed in gcc side (gcc-7.0.1-10.fc26)
  (ref: bug 1423312)

* Fri Feb 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.77-3
- Fix FTBFS with gcc7 (bug 1423312, upstream ticket 7910)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jon Ciesla <limburgher@gmail.com> - 1.77-1
- 1.77.

* Mon Aug 08 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.75-1
- Update to 1.75.

* Tue Aug 02 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.74-2
- Re-enable tests on x86.

* Mon Aug 01 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.74-1
- Update to 1.74.

* Sun May 22 2016 Rich Mattes <richmattes@gmail.com> - 1.73-2
- Rebuild for tinyxml2-3.0.0

* Sat Apr 09 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.73-1
- Update to 1.73.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.71-1
- Update to 1.71.

* Fri Nov 13 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.70-4
- Link whole archive (BZ #1280242), patch by Mamoru Tasaka.
- Compile and run tests using CMake.

* Wed Nov 11 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.70-3
- Enable HAVE_RULES.

* Thu Nov 5 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.70-2
- Include GUI (BZ #1278318).

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.70-1
- Update to 1.70.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.68-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 03 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.68-1
- Update to 1.68.

* Mon Dec 01 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.67-1
- Update to 1.67.

* Sat Aug 23 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.66-1
- Update to 1.66.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.65-1
- Update to 1.65.

* Wed Jan 22 2014 François Cami <fcami@fedoraproject.org> - 1.63-3
- Add HAVE_RULES=yes (#1056733).

* Tue Jan 07 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.63-2
- Include cfg files as well.

* Tue Jan 07 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.63-1
- Update to 1.63.

* Sun Oct 13 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.62-1
- Update to 1.62.

* Sat Aug 10 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.61-1
- Update to 1.61.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 François Cami <fcami@fedoraproject.org> - 1.60.1-1
- Update to 1.60.1.

* Mon Apr 01 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.59-1
- Update to 1.59.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 François Cami <fcami@fedoraproject.org> - 1.58-1
- Update to 1.58.

* Tue Sep 18 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.57-1
- Update to 1.57.

* Tue Sep 18 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.56-1
- Update to 1.56.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.55-1
- Update to 1.55.

* Sun Apr 15 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.54-1
- Update to 1.54.

* Sat Feb 11 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.53-1
- Update to 1.53.

* Thu Jan 05 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.52-2
- Add missing includes (fix FTBFS in rawhide).

* Sun Dec 11 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.52-1
- Update to 1.52.

* Wed Oct 26 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.51-2
- Include man page and more other docs.
- Build with $RPM_LD_FLAGS.
- Improve summary and description.

* Sun Oct 09 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.51-1
- Update to 1.51.

* Fri Aug 19 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.50-2
- Fix build on EPEL-4.

* Sun Aug 14 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.50-1
- Update to 1.50.

* Mon Jun 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.49-1
- Update to 1.49.

* Sat Apr 30 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.48-2
- Build with system tinyxml and support for rules.
- Run test suite during build, don't include its sources in docs.
- Drop readme.txt from docs, it doesn't contain useful info after installed.

* Fri Apr 15 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.48-1
- Update to 1.48.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.47-1
- Update to 1.47.

* Thu Dec 30 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.46.1-1
- Update to 1.46.1.

* Wed Dec 15 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.46-1
- Update to 1.46.

* Mon Oct 4 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.45-1
- Update to 1.45.

* Sat Jul 24 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.44-1
- Update to 1.44.

* Sun May 9 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.43-1
- Update to 1.43.

* Wed Mar 10 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.42-1
- Update to 1.42.

* Mon Jan 18 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.40-1
- Update to 1.40.

* Sun Dec 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.39-1
- Update to 1.39.

* Sat Nov 07 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.38-1
- Update to 1.38.

* Tue Sep 22 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.36-1
- Update to 1.36.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.34-1
- Update to 1.34.

* Mon Apr 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.31-1
- First release.
