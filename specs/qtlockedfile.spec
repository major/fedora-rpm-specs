%if (0%{?fedora} || 0%{?rhel} < 8) && ! 0%{?flatpak}
%global _with_qt4      1
%endif

%global commit0	   5a07df503a6f01280f493cbcc2aace462b9dee57
%global commitdate 20150629

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:	QFile extension with advisory locking functions
Name:		qtlockedfile
Version:	2.4
Release:	44.%{commitdate}git%{shortcommit0}%{?dist}

License:	GPLv3 or LGPLv2 with exceptions
URL:		http://doc.qt.digia.com/solutions/4/qtlockedfile/qtlockedfile.html
Source0:	https://github.com/qtproject/qt-solutions/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Source1:	qtlockedfile.prf.in
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source2:	LICENSE.LGPL
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source3:	LGPL_EXCEPTION
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source4:	LICENSE.GPL3
%{?_with_qt4:BuildRequires:	qt4-devel}
BuildRequires: make
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt6-qtbase-devel

%description
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.

%if 0%{?_with_qt4}
%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt4-devel

%description devel
This package contains libraries and header files for developing applications
that use QtLockedFile.
%endif

%package qt5
Summary:	QFile extension with advisory locking functions (Qt5)
Requires:	qt5-qtbase

%description qt5
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.
This is a special build against Qt5.

%package qt5-devel
Summary:	Development files for %{name}-qt5
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	qt5-qtbase-devel

%description qt5-devel
This package contains libraries and header files for developing applications
that use QtLockedFile with Qt5.

%package qt6
Summary:	QFile extension with advisory locking functions (Qt6)
Requires:	qt6-qtbase

%description qt6
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.
This is a special build against Qt6.

%package qt6-devel
Summary:	Development files for %{name}-qt6
Requires:	%{name}-qt6 = %{version}-%{release}
Requires:	qt6-qtbase-devel

%description qt6-devel
This package contains libraries and header files for developing applications
that use QtLockedFile with Qt6.

%prep
%setup -qn qt-solutions-%{commit0}/%{name}
# use versioned soname
sed -i s,head,%{version}, common.pri
# do not build example source
sed -i /example/d %{name}.pro
mkdir licenses
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} licenses


%build
# Does not use GNU configure
./configure -library
%if 0%{?_with_qt4}
%{qmake_qt4}
%make_build
sed -e 's|@QT_INCLUDEDIR@|%{_qt4_headerdir}|' %{SOURCE1} > qtlockedfile.prf
%endif
mkdir qt5
pushd qt5
%{qmake_qt5} ..
%make_build
sed -e 's|@QT_INCLUDEDIR@|%{_qt5_headerdir}|' %{SOURCE1} > qtlockedfile.prf
popd
mkdir qt6
pushd qt6
%{qmake_qt6} ..
%make_build
sed -e 's|@QT_INCLUDEDIR@|%{_qt6_headerdir}|' %{SOURCE1} > qtlockedfile.prf
popd

%install
# libraries
mkdir -p %{buildroot}%{_libdir}
cp -ap lib/* %{buildroot}%{_libdir}

# headers
%if 0%{?_with_qt4}
mkdir -p %{buildroot}%{_qt4_headerdir}/QtSolutions
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt4_headerdir}/QtSolutions
install -p -D -m644 qtlockedfile.prf %{buildroot}%{_qt4_datadir}/mkspecs/features/qtlockedfile.prf
%endif
mkdir -p %{buildroot}%{_qt5_headerdir}/QtSolutions
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt5_headerdir}/QtSolutions
install -p -D -m644 qt5/qtlockedfile.prf %{buildroot}%{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf
mkdir -p %{buildroot}%{_qt6_headerdir}/QtSolutions
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt6_headerdir}/QtSolutions
install -p -D -m644 qt6/qtlockedfile.prf %{buildroot}%{_qt6_archdatadir}/mkspecs/features/qtlockedfile.prf

%if 0%{?_with_qt4}
%files
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt4_libdir}/libQtSolutions_LockedFile*.so.*

%files devel
%doc doc/html/ example/
%{_qt4_headerdir}/QtSolutions/
%{_qt4_libdir}/libQtSolutions_LockedFile*.so
%{_qt4_datadir}/mkspecs/features/qtlockedfile.prf
%endif

%files qt5
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt5_libdir}/libQt5Solutions_LockedFile*.so.*

%files qt5-devel
%doc doc/html/ example/
%{_qt5_headerdir}/QtSolutions/
%{_qt5_libdir}/libQt5Solutions_LockedFile*.so
%{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf

%files qt6
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt6_libdir}/libQt6Solutions_LockedFile*.so.*

%files qt6-devel
%doc doc/html/ example/
%{_qt6_headerdir}/QtSolutions/
%{_qt6_libdir}/libQt6Solutions_LockedFile*.so
%{_qt6_archdatadir}/mkspecs/features/qtlockedfile.prf

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-44.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-43.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-42.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-41.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

	
* Sat Jan 06 2024 Marie Loise Nolden <loise@kde.org> - 2.4-40.20150629git5a07df5
- add qt6 build	

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-39.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-38.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-37.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-36.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-35.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-34.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-33.20150629git5a07df5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-32.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-31.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Leigh Scott <leigh123linux@gmail.com> - 2.4-30.20150629git5a07df5
- Add option to disable qt4 build which is needed for epel8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-29.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-28.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.4-27.20150629git5a07df5
- use %%make_build %%ldconfig_scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-26.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-25.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-24.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-23.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-22.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-21.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.4-20.20160120git5a07df5
- Rebuild

* Sun Oct 11 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-19.20150629git5a07df5
- rebuilt

* Mon Jul 27 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-18.20150629git5a07df5
- apply Qt5 fixes of upstream (rhbz#1239869)
- use sources from github instead of gitlab
- remove obsoleted patches
- simplify installation of header files

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Rex Dieter <rdieter@fedoraproject.org> 2.4-16
- qtlockedfile.prf: use versioned lib for linking

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.4-15
- qtlockedfile.prf: use QT_INSTALL_HEADERS instead, drop DEPENDPATH

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.4-14
- fix/simplify qt5 mkspecs/features install path

* Sun Apr 26 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-13
- readd lost patch

*  Sat Apr 25 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-12
- add Qt5 build
- use latest commit of dedicated source folder
- remove upstreamed patch
- replace buildroot macro
- remove deprecated spec entries

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.4-10
- Fix conflicting license files
 
* Thu Aug 14 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.4-9
- Update to Digia's repository

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.4-2
- Remove unnecessary linkage to libQtGui

* Thu Apr 15 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.4-1
- Initial Fedora package.
