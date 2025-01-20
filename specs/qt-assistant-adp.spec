Summary: Compatibility version of Qt Assistant
Name:    qt-assistant-adp
Version: 4.6.3
Release: 34%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
# Automatically converted from old format: LGPLv2 with exceptions or GPLv3 with exceptions - review is highly recommended.
License: LGPL-2.0-or-later WITH FLTK-exception OR LicenseRef-Callaway-GPLv3-with-exceptions
Url: https://download.qt.io/archive/qt/4.6/
Source0: https://download.qt.io/archive/qt/4.6/qt-assistant-qassistantclient-library-compat-src-%{version}.tar.gz
# missing header files from Debian (Fathi Boudra)
Source1: QAssistantClient
Source2: QtAssistant
# build fixes from Debian (Fathi Boudra)
Patch1: 01_build_system.diff

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt4-devel >= 4.7.0
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
The old version of Qt Assistant, based on Assistant Document Profile (.adp)
files, and the associated QtAssistantClient library, for compatibility with
applications providing help in that format.

New applications should use the new version of Qt Assistant introduced in Qt
4.4, based on the Qt Help Framework also introduced in Qt 4.4, instead.


%package devel
Summary: Development files for the compatibility QAssistantClient
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt4-devel
%description devel
This package contains the files necessary to build applications using the
deprecated QAssistantClient class (in the deprecated QtAssistantClient library),
which is used together with the legacy Assistant Document Profile (.adp) version
of Qt Assistant.

This class is obsolete. It is provided to keep old source code working. We
strongly advise against using it in new code. New code should use the Qt Help
Framework introduced in Qt 4.4 and/or the version of Qt Assistant based on it
(also introduced in Qt 4.4) instead.


%prep
%setup -q -n qt-assistant-qassistantclient-library-compat-version-%{version}
%patch -P1 -p1 -b .build_system
mkdir include
cp -p %{SOURCE1} %{SOURCE2} include/


%build
# build assistant_adp
%{qmake_qt4} QT_PRODUCT=OpenSource
%make_build

# build libQtAssistantClient
pushd lib
%{qmake_qt4} CONFIG=create_prl
%make_build
popd

# build assistant_adp translations
pushd translations
lrelease-qt4 assistant_adp_*.ts
popd


%install
# install assistant_adp
make install INSTALL_ROOT=%{buildroot}

# install libQtAssistantClient
make install INSTALL_ROOT=%{buildroot} -C lib

# install assistant_adp translations
mkdir -p %{buildroot}%{_qt4_translationdir}
install -p -m644 translations/assistant_adp_*.qm \
                 %{buildroot}%{_qt4_translationdir}/

# install assistant.prf mkspec
install -D -p -m644 features/assistant.prf \
                    %{buildroot}%{_qt4_datadir}/mkspecs/features/assistant.prf

# install missing headers (thanks to Fathi Boudra from Debian)
install -p -m644 include/Q* %{buildroot}%{_qt4_headerdir}/QtAssistant/

# nuke dangling reference(s) to the buildroot
sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" %{buildroot}%{_qt4_libdir}/*.prl

# let rpm handle binaries conflicts
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt4_bindir}
mv assistant_adp ../../../bin/
ln -s ../../../bin/assistant_adp .
popd

# _debug target (see bug #196513)
pushd %{buildroot}%{_qt4_libdir}
echo "INPUT(-lQtAssistantClient)" >libQtAssistantClient_debug.so
popd

# Note that we intentionally DO NOT install a .desktop file for assistant_adp
# because it makes no sense to invoke it without a specific .adp file to open.
# By default, it views the Qt documentation, for which we already have a menu
# entry using the current version of the Qt Assistant, and there is no UI for
# viewing anything different. The .adp file needs to be passed on the command
# line, which is usually done by the application.

%find_lang assistant_adp --with-qt --without-mo


%ldconfig_scriptlets

%files -f assistant_adp.lang
%license LGPL_EXCEPTION.txt LICENSE.LGPL LICENSE.GPL3
%{_bindir}/assistant_adp
%{_qt4_bindir}/assistant_adp
%{_qt4_libdir}/libQtAssistantClient.so.4*

%files devel
%{_qt4_headerdir}/QtAssistant/
%{_qt4_libdir}/libQtAssistantClient.so
%{_qt4_libdir}/libQtAssistantClient_debug.so
%{_qt4_libdir}/libQtAssistantClient.prl
%{_libdir}/pkgconfig/QtAssistantClient.pc
%{_qt4_datadir}/mkspecs/features/assistant.prf


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.6.3-33
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Than Ngo <than@redhat.com> - 4.6.3-18
- fixed source url

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.6.3-17
- BR: gcc-c++, use %%ldconfig_scriptlets %%make_build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-11
- .spec cosmetics, use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.6.3-9
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 05 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.6.3-1
- new upstream tarball with only the compat assistant_adp and QAssistantClient
- build fixes from Debian (Fathi Boudra)
- use find_lang to package the qm files (#609749)

* Tue Mar 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-2
- use versioned BR/Requires to avoid Conflicts

* Sat Mar 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.6.2-1
- first Fedora package
