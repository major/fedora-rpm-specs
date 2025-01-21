#
# Relax build_type_safety_c for gcc14 pointer type validation
#
%global         build_type_safety_c 2

Name:           tpm2-tss-engine
Version:        1.2.0
Release:        7%{?dist}
Summary:        OpenSSL Engine for TPM2 devices using the tpm2-tss software stack

License:        BSD-3-Clause
URL:            https://github.com/tpm2-software/tpm2-tss-engine
Source0:        https://github.com/tpm2-software/tpm2-tss-engine/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gcc-c++ 
BuildRequires:  pkgconfig
BuildRequires:  pandoc
BuildRequires:  tpm2-tss-devel 
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine

Requires:       openssl 
Requires:       tpm2-tss

%description
tpm2-tss-engine is an engine implementation for OpenSSL that uses tpm2-tss 
software stack. It uses the Enhanced System API (ESAPI) interface of the
TSS 2.0 for downwards communication. It supports RSA decryption and signatures
as well as ECDSA signatures.

%prep
%autosetup -n %{name}-%{version}


%build
%configure --disable-static
%make_build


%install
%make_install



%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/engines-3/libtpm2tss.so
%{_libdir}/engines-3/tpm2tss.so



%package devel
Summary:  Headers and libraries for building applications against tpm2-tss-engine
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
This package contains headers and libraries for building apps applications
against tpm2-tss-engine

%files devel
%{_includedir}/tpm2-tss-engine.h
%{_mandir}/man3/tpm2tss_*.3{,.*}



%package utilities
Summary:  Utility binary for openssl using tpm2-tss software stack
Requires: %{name}%{_isa} = %{version}-%{release}

%description utilities
This package contains the binary of the engine implementation for openssl that
uses the tpm2-tss software stack

%files utilities
%{_bindir}/tpm2tss-genkey
%{_datadir}/bash-completion/completions/tpm2tss-genkey
%{_mandir}/man1/tpm2tss-genkey.1{,.*}




%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 1.2.0-5
- Adjust BR for openssl engine deprecation

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 1.2.0-3
- Relax build_type_safety_c for gcc14 pointer type validation

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 1.2.0-1
- Update to 1.2.0
- Don't build static libraries
- Minor glob changes to follow the spirit of recent packaging guidelines
- SPDX License

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.1.0-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 3 2020 Mathias Zavala <zvl.mathias@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 1 2020 Mathias Zavala <zvl.mathias@gmail.com> - 1.0.1-2
- Move tpm2tss.so from -devel to main package to fix missing engine error

* Mon Nov 18 2019 Mathias Zavala <zvl.mathias@gmail.com> - 1.0.1-1
- initial version of the package
