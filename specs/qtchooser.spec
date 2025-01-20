
%define git g4717841

Name:	 qtchooser
Summary: Wrapper to select between Qt development binary versions
Version: 39
Release: 33%{?dist}

# Automatically converted from old format: LGPLv2 or GPLv3 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 OR GPL-3.0-only
URL:	 http://macieira.org/qtchooser
Source0: http://macieira.org/qtchooser/qtchooser-%{version}-%{git}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
## Qt5
BuildRequires: pkgconfig(Qt5Core) pkgconfig(Qt5Test)
## default runtime expected
Recommends: qt5-assistant
Recommends: qt5-designer
Recommends: qt5-linguist
Recommends: qt5-qdbusviewer
Recommends: qt5-qtbase-devel
Recommends: qt5-qtdeclarative-devel
Recommends: qt5-qtquick1-devel
Recommends: qt5-qttools
Recommends: qt5-qtxmlpatterns-devel

## Qt4
#BuildRequires: pkgconfig(QtCore) pkgconfig(QtTest)
## default runtime expected
#Recommends: %{_qt4}-config
#Recommends: %{_qt4}-devel
#Recommends: %{_qt4}-qdbusviewer

# profile.d snippets to add /usr/lib/qthcooser to $PATH
SOURCE10: qtchooser.sh
SOURCE11: qtchooser.csh

%description
Qt Chooser provides a wrapper to switch between versions of Qt development
binaries when multiple versions like 4 and 5 are installed or local Qt builds
are to be used.


%prep
%setup -q -n qtchooser-%{version}-%{git}


%build
#PATH="%{_qt5_bindir}:$PATH" ; export PATH
%make_build \
  %{?optflags:CXXFLAGS="%{optflags}"} \
  %{?__global_ldflags:LFLAGS="%{__global_ldflags}"}


%install
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}/etc/xdg/qtchooser

# Install man page not installed by Makefile
install -D -p -m 0644 doc/qtchooser.1 %{buildroot}%{_mandir}/man1/qtchooser.1

## env vars
#QT_SELECT
#QTCHOOSER_RUNTOOL

## HACK ALERT
# so, kde-sig decided putting this into %_bindir and using unconditionally is...
# problematic and unacceptable, so a compromise is to stuff this away so users
# can opt-in to use it
mkdir -p %{buildroot}%{_prefix}/lib/qtchooser
mv %{buildroot}%{_bindir}/* %{buildroot}%{_prefix}/lib/qtchooser/

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m644 -p %{SOURCE10} %{SOURCE11} \
  %{buildroot}%{_sysconfdir}/profile.d/


%check
PATH="%{_qt5_bindir}:$PATH" ; export PATH
make check


%files
%license LGPL_EXCEPTION.txt LICENSE.GPL LICENSE.LGPL
%dir %{_sysconfdir}/xdg/qtchooser
%{_sysconfdir}/profile.d/qtchooser.*
%{_mandir}/man1/qtchooser.1*
%dir %{_prefix}/lib/qtchooser/
%{_prefix}/lib/qtchooser/qtchooser
%{_prefix}/lib/qtchooser/assistant
%{_prefix}/lib/qtchooser/designer
%{_prefix}/lib/qtchooser/lconvert
%{_prefix}/lib/qtchooser/linguist
%{_prefix}/lib/qtchooser/lrelease
%{_prefix}/lib/qtchooser/lupdate
%{_prefix}/lib/qtchooser/moc
%{_prefix}/lib/qtchooser/pixeltool
%{_prefix}/lib/qtchooser/qcollectiongenerator
%{_prefix}/lib/qtchooser/qdbus
%{_prefix}/lib/qtchooser/qdbuscpp2xml
%{_prefix}/lib/qtchooser/qdbusviewer
%{_prefix}/lib/qtchooser/qdbusxml2cpp
%{_prefix}/lib/qtchooser/qdoc
%{_prefix}/lib/qtchooser/qdoc3
%{_prefix}/lib/qtchooser/qglinfo
%{_prefix}/lib/qtchooser/qhelpconverter
%{_prefix}/lib/qtchooser/qhelpgenerator
%{_prefix}/lib/qtchooser/qmake
%{_prefix}/lib/qtchooser/qml
%{_prefix}/lib/qtchooser/qml1plugindump
%{_prefix}/lib/qtchooser/qmlbundle
%{_prefix}/lib/qtchooser/qmlmin
%{_prefix}/lib/qtchooser/qmlplugindump
%{_prefix}/lib/qtchooser/qmlprofiler
%{_prefix}/lib/qtchooser/qmlscene
%{_prefix}/lib/qtchooser/qmltestrunner
%{_prefix}/lib/qtchooser/qmlviewer
%{_prefix}/lib/qtchooser/qtconfig
%{_prefix}/lib/qtchooser/rcc
%{_prefix}/lib/qtchooser/uic
%{_prefix}/lib/qtchooser/uic3
%{_prefix}/lib/qtchooser/xmlpatterns
%{_prefix}/lib/qtchooser/xmlpatternsvalidator


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 39-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 39-32
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 39-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 39-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 39-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 39-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 39-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 39-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 39-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 39-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 39-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 39-22
- Install man page

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 39-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 39-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 39-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 39-15
- BR: gcc-c++, use %%license %%make_build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 39-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 39-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 39-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 39-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 39-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Rex Dieter <rdieter@fedoraproject.org> 39-9
- changed my mind, add Recommends for Qt5-based tools instead

* Mon Oct 19 2015 Rex Dieter <rdieter@fedoraproject.org> 39-8
- Recommends: qt-config qt-qdbusviewer qt-devel

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 39-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Oct 19 2014 Rex Dieter <rdieter@fedoraproject.org> 39-5
- own /usr/lib/qtchooser (#1154372)

* Thu Oct 16 2014 Rex Dieter <rdieter@fedoraproject.org> 39-4
- improve description/summary (#1153827)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Rex Dieter <rdieter@fedoraproject.org> 39-1
- qtchooser-39

* Sat May 18 2013 Rex Dieter <rdieter@fedoraproject.org> 31-1
- qtchooser-31

* Wed Mar 06 2013 Rex Dieter <rdieter@fedoraproject.org> 26-1
- qtchooser-26

* Thu Jan 24 2013 Rex Dieter <rdieter@fedoraproject.org> 9-2
- move binaries to /usr/lib/qtchooser, keeps this optional, allows
  users to install/opt-in instead

* Mon Dec 31 2012 Rex Dieter <rdieter@fedoraproject.org> 9-1
- first try
