%global qtinc   %(qmake -query QT_INSTALL_PREFIX)/include
%global qtlib   %(qmake -query QT_INSTALL_PREFIX)/lib

Name:           qwtplot3d
Version:        0.2.7
Release:        38%{?dist}
Summary:        Qt/OpenGL-based C++ library providing a bunch of 3D-widgets

# zlib/libpng License
License:        zlib
URL:            http://qwtplot3d.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tgz

## upstreamable patches
Patch50:  qwtplot3d-glu.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1077865
Patch51:  qwtplot3d-%{version}-syslibs.patch

BuildRequires: make
BuildRequires:  qt3-devel
BuildRequires:  qt-devel
BuildRequires:  libXmu-devel
BuildRequires:  gl2ps-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++

%description
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt3-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        qt4
Summary:        Qt4/OpenGL-based C++ library providing a bunch of 3D-widgets
BuildRequires:  qt4-devel

%description    qt4
QwtPlot3D is not a program, but a feature-rich Qt4/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

%package        qt4-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt4%{?_isa} = %{version}-%{release}
Requires:       qt4-devel

%description    qt4-devel
The %{name}-devel package contains qt4 libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}

#fix line endings
sed -i 's/\r//' COPYING
find examples -type f | xargs %{__sed} -i 's/\r//'

sed  -i "s|0.2.6|%{version}|" qwtplot3d.pro

# treating soname
sed -i "s|TARGET *= qwtplot3d|TARGET = qwtplot3d-qt4|" qwtplot3d.pro

# fixing gcc4.4 build
sed  -i "4i\#include <cstdio>" src/qwt3d_function.cpp

%patch50 -p1 -b .glu

dos2unix qwtplot3d.pro src/qwt3d_io_gl2ps.cpp
%patch51 -p1 -b .syslibs
rm -r 3rdparty

%build
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-fexceptions/-fno-exceptions/g')

############### QT4 ######################
mkdir -p qt4 && pushd qt4
%{qmake_qt4} ../qwtplot3d.pro QMAKE_CXXFLAGS+="$SETOPT_FLAGS" QMAKE_LFLAGS+="%{__global_ldflags} -Wl,--as-needed"
make %{?_smp_mflags}

make clean
popd
# treating soname
sed -i "s|TARGET *= qwtplot3d-qt4|TARGET = qwtplot3d|" qwtplot3d.pro

############### QT3 ######################
%{_libdir}/qt-3.3/bin/qmake qwtplot3d.pro QMAKE_CXXFLAGS+="$SETOPT_FLAGS" QMAKE_LFLAGS+="%{__global_ldflags} -Wl,--as-needed"
make %{?_smp_mflags}

%install
############### QT3 ######################
mkdir -p %{buildroot}%{qtlib}
install -p -m 0755 lib/libqwtplot3d.so.%{version} %{buildroot}%{qtlib}
ln -sf libqwtplot3d.so.%{version} %{buildroot}%{qtlib}/libqwtplot3d.so
ln -sf libqwtplot3d.so.%{version} %{buildroot}%{qtlib}/libqwtplot3d.so.0

mkdir -p %{buildroot}%{qtinc}/qwtplot3d
install -p -m 0644 include/* %{buildroot}%{qtinc}/qwtplot3d

############### QT4 ######################
mkdir -p %{buildroot}%{_qt4_headerdir}/qwtplot3d
install -p -m 0644 include/* %{buildroot}%{_qt4_headerdir}/qwtplot3d

cd qt4
mkdir -p %{buildroot}%{_qt4_libdir}
install -p -m 0755 lib/libqwtplot3d-qt4.so.%{version} %{buildroot}%{_qt4_libdir}
ln -sf libqwtplot3d-qt4.so.%{version} %{buildroot}%{_qt4_libdir}/libqwtplot3d-qt4.so
ln -sf libqwtplot3d-qt4.so.%{version} %{buildroot}%{_qt4_libdir}/libqwtplot3d-qt4.so.0

%ldconfig_scriptlets
%ldconfig_scriptlets qt4

%files
%license COPYING
%{qtlib}/libqwtplot3d.so.*

%files devel
%doc examples
%{qtinc}/%{name}/
%{qtlib}/libqwtplot3d.so

%files qt4
%license COPYING
%{_qt4_libdir}/libqwtplot3d-qt4.so.*

%files qt4-devel
%doc examples
%{_qt4_headerdir}/%{name}/
%{_qt4_libdir}/libqwtplot3d-qt4.so

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.7-28
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 20 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.2.7-22
- Unbundle gl2ps (bz#1077865)
- Fix compiler/linker flags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.2.7-20
- Spec adjustments (use license tag, global instead of define)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.7-18
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> 
- 0.2.7-12
- Building against qwtplot3d-qt4 fails (#805684)
- tighten subpkg deps

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-8
- fixed failed build on gcc 4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.2.7-6
- s/qt-devel/qt3-devel/

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.7-5
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-4
- fixed -qt4 symbolic links
- update license to zlib

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-3
- queued for mass rebuild for Fedora 8 - BuildID

* Wed Aug 08 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-2
- built and shipped qwtplot3d-qt4 and devel

* Mon Jul 30 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-1
- New upstream release
- Added optflags to the make process
- fix ownership

* Tue Jan 02 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.6-2
- Added qt-devel to -devel subpackage requires

* Sun Dec 31 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.6-1
- Initial RPM release
