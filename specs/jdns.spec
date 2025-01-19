%global use_qt4 1
%global use_qt5 1

%global wrpname q%{name}
%global qt4_build_dir release-qt4
%global qt5_build_dir release-qt5

Name: jdns
Version: 2.0.6
Release: 15%{?dist}

License: MIT
Summary: A simple DNS queries library
URL: https://github.com/psi-im/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: ninja-build

%if 0%{?use_qt4}
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtNetwork)
%endif

%if 0%{?use_qt5}
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)
%endif

%description
JDNS is a simple DNS implementation that can perform normal DNS
queries of any record type (notably SRV), as well as Multicast DNS
queries and advertising. Multicast support is based on Jeremie
Miller's "mdnsd" implementation.

For maximum flexibility, JDNS is written in C with no direct
dependencies, and is licensed under the MIT license. Your application
must supply functionality to JDNS, such as UDP sending/receiving, via
callbacks.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: %{name} API documentation
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description doc
This package includes %{name} API documentation in HTML format.

%if 0%{?use_qt4}
%package -n %{wrpname}-qt4
Summary: Qt4-wrapper for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{wrpname} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{wrpname} < %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt4
For Qt4 users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

%package -n %{wrpname}-qt4-devel
Summary: Development files for %{wrpname}-qt4
Requires: %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{wrpname}-qt4%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{wrpname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{wrpname}-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt4-devel
This package contains libraries and header files for developing applications
that use %{wrpname}-qt4.
%endif

%if 0%{?use_qt5}
%package -n %{wrpname}-qt5
Summary: Qt5-wrapper for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt5
For Qt5 users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

%package -n %{wrpname}-qt5-devel
Summary: Development files for %{wrpname}-qt5
Requires: %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{wrpname}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt5-devel
This package contains libraries and header files for developing applications
that use %{wrpname}-qt5.

%package -n %{wrpname}-qt5-tools
Summary: Qt-based command-line tool %{name}

%description -n %{wrpname}-qt5-tools
This package contains Qt-based command-line tool called %{name} that can
be used to test functionality.
%endif

%prep
%autosetup -p1

%build
%if 0%{?use_qt4}
mkdir %{qt4_build_dir} && pushd %{qt4_build_dir}
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_JDNS_TOOL:BOOL=OFF \
    -DQT4_BUILD:BOOL=ON
%cmake_build
popd
%endif

%if 0%{?use_qt5}
mkdir %{qt5_build_dir} && pushd %{qt5_build_dir}
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_JDNS_TOOL:BOOL=ON \
    -DQT4_BUILD:BOOL=OFF
%cmake_build
popd
%endif

%install
%if 0%{?use_qt4}
pushd %{qt4_build_dir}
%cmake_install
popd
%endif

%if 0%{?use_qt5}
pushd %{qt5_build_dir}
%cmake_install
popd
%endif

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.2*

%files devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/%{name}.h
%{_includedir}/%{name}/%{name}_export.h
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%{_docdir}/%{name}/html/

%files -n %{wrpname}-qt4
%{_libdir}/lib%{wrpname}-qt4.so.2*

%files -n %{wrpname}-qt4-devel
%{_includedir}/%{name}/%{wrpname}.h
%{_includedir}/%{name}/%{wrpname}shared.h
%{_libdir}/lib%{wrpname}-qt4.so
%{_libdir}/cmake/%{wrpname}/
%{_libdir}/cmake/%{wrpname}-qt4/
%{_libdir}/pkgconfig/%{wrpname}-qt4.pc

%files -n %{wrpname}-qt5
%{_libdir}/lib%{wrpname}-qt5.so.2*

%files -n %{wrpname}-qt5-devel
%{_includedir}/%{name}/%{wrpname}.h
%{_includedir}/%{name}/%{wrpname}shared.h
%{_libdir}/lib%{wrpname}-qt5.so
%{_libdir}/cmake/%{wrpname}/
%{_libdir}/cmake/%{wrpname}-qt5/
%{_libdir}/pkgconfig/%{wrpname}-qt5.pc

%files -n %{wrpname}-qt5-tools
%{_bindir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.6-9
- Fixed FTBFS on Fedora 37+.
- Performed major SPEC cleanup.
- Switched jdns tool to Qt 5.

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
