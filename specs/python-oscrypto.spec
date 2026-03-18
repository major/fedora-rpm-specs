# main package is archful to run tests everywhere but produces noarch packages
%global debug_package %{nil}
%bcond_without check
%global pname oscrypto
%global forgeurl https://github.com/wbond/oscrypto
%global commit 1547f535001ba568b239b8797465536759c742a3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230823
%global version0 1.3.0

%global desc %{expand:
Currently the following features are implemented. Many of these should only be
used for integration with existing/legacy systems.

* TLSv1.x socket wrappers
* Exporting OS trust roots
* Encryption/decryption
* Generating public/private key pairs
* Generating DH parameters
* Signing and verification
* Loading and normalizing DER and PEM formatted keys
* Key derivation
* Random byte generation
}

Name: python-%{pname}
Version: %{version0}^%{commitdate}git%{shortcommit}
Release: 1%{?dist}
Summary: Compiler-free Python crypto library backed by the OS
License: MIT
URL: %{forgeurl}
Source0: %{url}/archive/%{commit}/oscrypto-%{shortcommit}.tar.gz

%description %{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: ca-certificates
BuildRequires: python3-asn1crypto
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: openssl-libs
%endif
BuildArch: noarch
Requires: ca-certificates
Requires: openssl-libs

%description -n python3-%{pname} %{desc}

%prep
%autosetup -n oscrypto-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pname}

%if %{with check}
%check
export SSL_CERT_FILE=/etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt
export OPENSSL_ENABLE_SHA1_SIGNATURES=1 
# run only non-network tests
%pytest -k 'not TLSTests'
%endif

%files -n python3-%{pname} -f %{pyproject_files}
%license LICENSE
%doc readme.md

%changelog
* Thu Mar 05 2026 Benson Muite <fed500@fedoraproject.org> - 1.3.0^20230823git1547f53-1
- Update to latest commit and enable tests to run

* Sat Apr 12 2025 Benson Muite <fed500@fedoraproject.org> - 1.3.0-10
- Spec file cleanup

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Dominik Mierzejewski <dominik@greysector.net> 1.3.0-3
- fix build with python-3.12

* Thu Jun 29 2023 Dominik Mierzejewski <dominik@greysector.net> 1.3.0-2
- use pyproject macros and drop explicit BR: on setuptools
- improve description
- run only non-network tests

* Fri May 06 2022 Dominik Mierzejewski <dominik@greysector.net> 1.3.0-1
- initial build
