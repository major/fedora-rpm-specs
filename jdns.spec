# override default value to allow build both qt4 and qt5 versions
%define _vpath_srcdir ..

Name:           jdns
Version:        2.0.6
Release:        8%{?dist}
Summary:        A simple DNS queries library

License:        MIT
URL:            https://github.com/psi-im/jdns
Source0:        https://github.com/psi-im/jdns/archive/v%{version}/%{name}-%{version}.tar.gz

## upstream patches

## upstreamable patches

BuildRequires:  cmake
BuildRequires:  pkgconfig(QtCore) pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(Qt5Core) pkgconfig(Qt5Network)
BuildRequires:  doxygen

%description
JDNS is a simple DNS implementation that can perform normal DNS
queries of any record type (notably SRV), as well as Multicast DNS
queries and advertising. Multicast support is based on Jeremie
Miller's "mdnsd" implementation.

For maximum flexibility, JDNS is written in C with no direct
dependencies, and is licensed under the MIT license. Your application
must supply functionality to JDNS, such as UDP sending/receiving, via
callbacks.

Qt-based command-line tool called ‘jdns’ that can be used to test
functionality.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        %{name} API documentation
BuildArch:      noarch
%description    doc
This package includes %{name} API documentation in HTML.

%package -n     qjdns-qt4
Summary:        Qt4-wrapper for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      qjdns < %{version}-%{release}
Provides:       qjdns = %{version}-%{release}

# avoid abi breaking
%if 0%{?__isa_bits} == 64
Provides:       libqjdns.so.2()(64bit)
%else
Provides:       libqjdns.so.2
%endif

%description -n qjdns-qt4
For Qt4 users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

Qt-based command-line tool called ‘jdns’ that can be used to test
functionality.

%package -n     qjdns-qt4-devel
Summary:        Development files for qjdns-qt4
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      qjdns-devel < %{version}-%{release}
Provides:       qjdns-devel = %{version}-%{release}
Requires:       qjdns-qt4%{?_isa} = %{version}-%{release}
%description -n qjdns-qt4-devel
The qjdns-qt4-devel package contains libraries and header files for
developing applications that use qjdns-qt4.

%package -n     qjdns-qt5
Summary:        Qt5-wrapper for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n qjdns-qt5
For Qt5 users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

%package -n     qjdns-qt5-devel
Summary:        Development files for qjdns-qt5
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       qjdns-qt5%{?_isa} = %{version}-%{release}
%description -n qjdns-qt5-devel
The qjdns-qt5-devel package contains libraries and header files for
developing applications that use qjdns-qt5.


%prep
%setup -q


%build
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
# FIXME: JDNS_TOOL FTBFS due to -fPIC/-fPIE wierdness, omit for now -- rex
%{cmake} %_vpath_srcdir \
  -DBUILD_JDNS_TOOL:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING="Release"

%cmake_build
popd

mkdir %{_target_platform}-qt4
pushd %{_target_platform}-qt4
%{cmake} %_vpath_srcdir \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DQT4_BUILD:BOOL=ON

%cmake_build
popd


%install
pushd %{_target_platform}-qt5
%cmake_install
popd

pushd %{_target_platform}-qt4
%cmake_install
popd

# Avoid api/abi breaking wich introduced with jdns-2.0.3
ln -s libqjdns-qt4.so.2 %{buildroot}%{_libdir}/libqjdns.so.2
ln -s qjdns-qt4.pc %{buildroot}%{_libdir}/pkgconfig/qjdns.pc

%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
# The pkg-config versions should match the tarball version
test "$(pkg-config --modversion jdns)" = "%{version}"
test "$(pkg-config --modversion qjdns)" = "%{version}"
test "$(pkg-config --modversion qjdns-qt4)" = "%{version}"
test "$(pkg-config --modversion qjdns-qt5)" = "%{version}"


%ldconfig_scriptlets

%files
%doc COPYING README.md
%{_libdir}/libjdns.so.2*
## HACK alert, quirk of recycling default %%_docdir below in -doc subpkg -- rex
%exclude %{_docdir}/jdns/html/

%files devel
%dir %{_includedir}/jdns/
%{_includedir}/jdns/jdns.h
%{_includedir}/jdns/jdns_export.h
%{_libdir}/libjdns.so
%{_libdir}/cmake/jdns/
%{_libdir}/pkgconfig/jdns.pc

%ldconfig_scriptlets -n qjdns-qt4

%files doc
%{_docdir}/jdns/html/

%files -n qjdns-qt4
%{_bindir}/jdns
%{_libdir}/libqjdns.so.2
%{_libdir}/libqjdns-qt4.so.2*

%files -n qjdns-qt4-devel
%{_includedir}/jdns/qjdns.h
%{_includedir}/jdns/qjdnsshared.h
%{_libdir}/libqjdns-qt4.so
%{_libdir}/cmake/qjdns/
%{_libdir}/cmake/qjdns-qt4/
%{_libdir}/pkgconfig/qjdns.pc
%{_libdir}/pkgconfig/qjdns-qt4.pc

%ldconfig_scriptlets -n qjdns-qt5

%files -n qjdns-qt5
%{_libdir}/libqjdns-qt5.so.2*

%files -n qjdns-qt5-devel
%{_includedir}/jdns/qjdns.h
%{_includedir}/jdns/qjdnsshared.h
%{_libdir}/libqjdns-qt5.so
%{_libdir}/cmake/qjdns/
%{_libdir}/cmake/qjdns-qt5/
%{_libdir}/pkgconfig/qjdns-qt5.pc


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug  3 2020 Ivan Romanov <drizt72@zoho.eu> - 2.0.6-4
- Use new cmake macroses
- Fix #1863901

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Ivan Romanov <drizt72@zoho.eu> - 2.0.6-1
- Bump to 2.0.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 2.0.5-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Ivan Romanov <drizt@land.ru> - 2.0.5-1
- Bump to 2.0.5
- Add Doxygen documentation

* Tue Mar  7 2017 Ivan Romanov <drizt@land.ru> - 2.0.4-3
- delta.affinix.com not used anymore

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 27 2016 Ivan Romanov <drizt@land.ru> - 2.0.4-1
- Update to 2.0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul  9 2015 Ivan Romanov <drizt@land.ru> - 2.0.3-1
- updated to 2.0.3
- 2.0.3 introduces some api/abi breaking. They fixed/workarounded.
- corrected description
- parallel-installable -qt5 support. some redesign. (#1234209)

* Mon Jun 22 2015 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-4
- parallel-installable -qt5 support (#1234209)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 Ivan Romanov <drizt@land.ru> - 2.0.2-2
- fixed el6 building (el6 doesn't know %%autosetup)

* Sun May 10 2015 Ivan Romanov <drizt@land.ru> - 2.0.2-1
- updated to 2.0.2
- dropped patches. went to upstream.

* Sat May 09 2015 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-4
- pull in upstream fixes (including one for pkgconfig issue 6)

* Fri May 08 2015 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-3
- USE_RELATIVE_PATHS=OFF (ON produces broken .pc files), .spec cosmetics

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 15 2015 Ivan Romanov <drizt@land.ru> - 2.0.1-1
- new upstream version

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-7
- use pkgconfig-style build dependencies
- %%check: make dir used in %%files, ensure string compare
- %%install: make install/fast ...
- %%files: track library sonames

* Mon Apr 14 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-6
- Removed duplicated description for each package

* Fri Apr 11 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-5
- separated qjdns-devel subpackage
- dropped any Confilcts/Obsoletes/Provides tags

* Wed Apr  9 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-4
- obsoletes/conflicts/provides fixes

* Wed Apr  9 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-3
- removed jdns binary from jdns package
- dropped reduntant dependencies
- use only %%{buildroot}
- merged jdns-bin with qjdns subpackage

* Fri Apr  4 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-2
- dropped __requires_exclude_from hach
- dropped removing buildroot before installing

* Thu Apr  3 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-1
- Initial version of package
