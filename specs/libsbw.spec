%global __cmake_in_source_build 1

Name:           libsbw
Summary:        C++ Broker library 
Version:        2.12.2
Release:        18%{?dist}
URL:            http://sourceforge.net/projects/sbw/
Source0:        https://sourceforge.net/projects/sbw/files/sbw/%{version}/sbw-core-%{version}.tar.bz2
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

BuildRequires: cmake
BuildRequires: gcc-c++, gcc
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: dos2unix
BuildRequires: help2man
BuildRequires: make

%description
The Systems Biology Workbench (SBW) is a framework for application
intercommunications. It uses a broker-based, distributed,
message-passing architecture, supports many languages
including Java, C++, Perl & Python, and runs under Linux,OSX & Win32.
By default, the Broker opens a port for inter-Broker communications
by searching for the first free port in the range 10102 through 10202,
inclusive.
By default, in Fedora this port range is not opened.
See man-page for further informations.

libSBW is the C++ Broker port from the original SBW Broker (written in Java)
to C++. The current version implements all the functionality for the local side.
Meaning if you will just use the Broker on a single machine you should be fine
using the C++ Broker.

%package devel
Summary: Development files of libSBW
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides header files, shared and static library files of libSBW.

##Static library may be useful for COPASI build
%package static
Summary: Static library of libSBW
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides static library file of libSBW.

%prep
%autosetup -n sbw-core-%{version}
dos2unix ReadMe.txt
rm -rf VisualStudio

##Remove bundled/pre-compiled files
rm -rf bin/*
rm -rf include/libxml include/iconv.h include/libcharset.h include/localcharset.h

##Fix installation paths of CMake config files
sed -e 's|lib/cmake|%{_lib}/cmake|g' -i CMakeLists.txt

##Fix permissions of header and cpp files
sed -e 's|DESTINATION include/SBW|PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ DESTINATION include/SBW|g' -i CMakeLists.txt
find ./SBWBroker \( -name \*.cpp -o -name \*.h \) -print0 | xargs -0 chmod -x
find ./SBWCore \( -name \*.cpp -o -name \*.h \) -print0 | xargs -0 chmod -x
find ./include/SBW \( -name \*.h \) -print0 | xargs -0 chmod -x

%build
mkdir -p build && cd build
export CXXFLAGS="-std=c++14 %{optflags} -Wl,-z,now -Wno-deprecated"
export LDFLAGS="%{__global_ldflags} -Wl,-z,now -Wl,--as-needed"
%cmake -Wno-cpp \
 -DLIBXML_INCLUDE_DIR:PATH=%{_includedir}/libxml2 -DLIBXML_LIBRARY:FILEPATH=%{_libdir}/libxml2.so \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} -DWITH_STRICT_INCLUDES:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DWITH_BUILD_BROKER:BOOL=ON  -DWITH_BUILD_SHARED:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON -DWITH_BUILD_STATIC:BOOL=ON \
 -DCPACK_BINARY_TZ:BOOL=OFF -DCPACK_BINARY_TGZ:BOOL=OFF -DCPACK_SOURCE_TBZ2:BOOL=OFF \
 -DCPACK_SOURCE_TGZ:BOOL=OFF -DCPACK_SOURCE_TZ:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES ..

%make_build

%install
export LIBDIR=%{_libdir}
%make_install -C build

## Make Broker man page
cd build/SBWBroker
help2man ./Broker -o Broker.1 --version-string=%{version}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 Broker.1 $RPM_BUILD_ROOT%{_mandir}/man1

%ldconfig_scriptlets

%files
%doc ReadMe.txt VERSION
%license LICENSE
%{_bindir}/Broker
%{_libdir}/libSBW.so.*
%{_mandir}/man1/Broker.1*

%files devel
%{_libdir}/libSBW.so
%{_includedir}/SBW/
%{_libdir}/cmake/SBW-config-*.cmake
%{_libdir}/cmake/SBW-config.cmake

%files static
%{_libdir}/libSBW-static.a
%{_libdir}/cmake/SBW-static-config-*.cmake
%{_libdir}/cmake/SBW-static-config.cmake

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12.2-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 2.12.2-7
- Force C++14 as this code is not C++17 ready

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.12.2-1
- Update to 2.12.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-20.20160916svn589
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.11.1-19.20160916svn589
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-18.20160916svn589
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-17.20160916svn589
- Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-16.20160916svn589
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-15.20160916svn589
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-14.20160916svn589
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-13.20160916svn589
- Update to latest commit (#589)

* Sun Apr 10 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-12.20160105svn582
- Update to latest commit (#582)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-11.20150414svn579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 01 2015 Antonio Trande <sagitterATfedoraproject.org> 2.11.1-10.20150414svn579
- Hardened builds on <F23

* Thu Oct 22 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-9.20150414svn579
- Rebuild for cmake 3.4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-8.20150414svn579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-7.20150414svn579
- 'static' sub-package requires the 'devel' one

* Tue Jun 09 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-6.20150414svn579
- Make a standalone package for static library

* Tue Jun 09 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-5.20150414svn579
- Removed iconv.h bundled file
- Description improved

* Sun May 31 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-4.20150414svn579
- Update to svn post-release #579
- Packaged Broker manpage

* Fri Jan 09 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-3
- Added SKIP_INSTALL_RPATH/CMAKE_SKIP_RPATH options
- Static file packaged again; seems necessary at building time

* Thu Jan 01 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-2
- Excluded static library packaging 

* Wed Dec 31 2014 Antonio Trande <sagitterATfedoraproject.org> - 2.11.1-1
- Update to 2.11.1

* Sun Dec 28 2014 Antonio Trande <sagitterATfedoraproject.org> - 2.10.0-1
- First package
