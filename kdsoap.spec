Name:           kdsoap
Version:        2.0.0
Release:        3%{?dist}
Summary:        A Qt-based client-side and server-side SOAP component

# The entire source code is the GPLv3 expect libkdsoap-server which is AGPLv3
License:        GPLv3 and AGPLv3
URL:            https://github.com/KDAB/KDSoap
Source0:        https://github.com/KDAB/KDSoap/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  dos2unix
BuildRequires:  qt5-qhelpgenerator
BuildRequires:  doxygen

%description
KD Soap is a Qt-based client-side and server-side SOAP component.

It can be used to create client applications for web services and also provides
the means to create web services without the need for any further component
such as a dedicated web server.

KD Soap targets C++ programmers who use Qt in their applications.

For more information, see http://www.kdab.com/kdab-products/kd-soap

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}

%prep
%autosetup


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DKDSoap_EXAMPLES=false -DCMAKE_SKIP_RPATH=true -DKDSoap_DOCS=True
%cmake_build


%install
%cmake_install
rm -rf $RPM_BUILD_ROOT/%{_datarootdir}/doc/KDSoap
find $RPM_BUILD_ROOT -name '*.la' -print -delete


%check
%ctest


%files
%{_libdir}/libkdsoap-server.so.2*
%{_libdir}/libkdsoap.so.2*
%doc README.txt
%license LICENSES/GPL-3.0-only.txt LICENSES/LicenseRef-KDAB-KDSoap-AGPL3-Modified.txt

%files devel
%doc kdsoap.pri kdwsdl2cpp.pri
%dir %{_datadir}/mkspecs
%dir %{_datadir}/mkspecs/features
%{_datadir}/mkspecs/features/kdsoap.prf
%{_includedir}/KDSoapClient/
%{_includedir}/KDSoapServer/
%{_libdir}/libkdsoap-server.so
%{_libdir}/libkdsoap.so
%{_bindir}/kdwsdl2cpp
%{_libdir}/cmake/KDSoap/
%{_libdir}/qt5/mkspecs/modules/

%files doc
%doc docs


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Casper Meijn <casper@meijn.net> - 2.0.0-1
- Update to KDSoap 2.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Casper Meijn <casper@meijn.net> - 1.10.0-1
- Update to KDSoap 1.10.0

* Sat Nov 14 2020 Marie Loise Nolden <loise@kde.org> - 1.9.1-1
- Update to 1.9.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Casper Meijn <casper@meijn.net> - 1.9.0-6
- Update to KDSoap 1.9.0
- Disable building examples
- Remove RPath patch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Casper Meijn <casper@meijn.net> - 1.8.0-3
- Update to KDSoap 1.8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Casper Meijn <casper@meijn.net> - 1.7.0-1
- First kdsoap package
