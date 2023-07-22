%global oqs_version 0.5.0
Name:       oqsprovider
Version:    %{oqs_version}
Release:    2%{?dist}
Summary:    oqsprovider is an OpenSSL provider for quantum-safe algorithms based on liboqs

License:    Apache-2.0 AND MIT
URL:        https://github.com/open-quantum-safe/oqs-provider.git
Source:     https://github.com/open-quantum-safe/oqs-provider/archive/refs/tags/0.5.0.tar.gz

Requires: liboqs
Requires: openssl
BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: liboqs-devel
BuildRequires: openssl-devel

%description
oqs-provider fully enables quantum-safe cryptography for KEM key
establishment in TLS1.3 including management of such keys via the OpenSSL (3.0)
provider interface and hybrid KEM schemes. Also, QSC signatures including CMS
functionality are available via the OpenSSL EVP interface. Key persistence is
provided via the encode/decode mechanism and X.509 data structures.

%prep
%setup -T -b 0 -q -n oqs-provider-%{oqs_version}

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Debug -LAH ..
%cmake_build

%check
cd "%{_vpath_builddir}"
ctest -V

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ossl-modules
install %{_vpath_builddir}/lib/oqsprovider.so.%{oqs_version} $RPM_BUILD_ROOT/%{_libdir}/ossl-modules
(cd $RPM_BUILD_ROOT/%{_libdir}/ossl-modules/ && ln -s oqsprovider.so.%{oqs_version} oqsprovider.so)

%files
%license LICENSE.txt
%{_libdir}/ossl-modules/oqsprovider.so.%{oqs_version}
%{_libdir}/ossl-modules/oqsprovider.so

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Dmitry Belyavskiy - 0.5.0-1
- Initial build of oqsprovider for Fedora

