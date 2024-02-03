%global oqs_version 0.5.3
Name:       oqsprovider
Version:    %{oqs_version}
Release:    1%{?dist}
Summary:    oqsprovider is an OpenSSL provider for quantum-safe algorithms based on liboqs

License:    Apache-2.0 AND MIT
URL:        https://github.com/open-quantum-safe/oqs-provider.git
Source:     https://github.com/open-quantum-safe/oqs-provider/archive/refs/tags/0.5.3.tar.gz

#TODO increase version - 0.5.2 is in sync with liboqs 0.9.0 but doesn't require it
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
%cmake -GNinja -DCMAKE_BUILD_TYPE=Debug -DOQS_KEM_ENCODERS=ON -LAH ..
%cmake_build

%check
cd "%{_vpath_builddir}"
ctest -V

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ossl-modules
install %{_vpath_builddir}/lib/oqsprovider.so $RPM_BUILD_ROOT/%{_libdir}/ossl-modules
(cd $RPM_BUILD_ROOT/%{_libdir}/ossl-modules/ && ln -s oqsprovider.so oqsprovider.so.%{oqs_version})

%files
%license LICENSE.txt
%{_libdir}/ossl-modules/oqsprovider.so.%{oqs_version}
%{_libdir}/ossl-modules/oqsprovider.so

%changelog
* Thu Feb 01 2024 Dmitry Belyavskiy <dbelyavs@redhat.com> - 0.5.3-1
- Update to 0.5.3 version
  Enable KEM encoders

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 27 2023 Dmitry Belyavskiy <dbelyavs@redhat.com> - 0.5.2-1
- Switch to 0.5.2 version
  Resolves: rhbz#2224598

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Dmitry Belyavskiy - 0.5.0-1
- Initial build of oqsprovider for Fedora

