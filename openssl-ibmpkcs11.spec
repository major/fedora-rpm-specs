%global enginesdir %(pkg-config --variable=enginesdir libcrypto)

Name:           openssl-ibmpkcs11
Version:        1.0.2
Release:        13%{?dist}
Summary:        IBM OpenSSL PKCS#11 engine

License:        OpenSSL
URL:            https://github.com/opencryptoki/openssl-ibmpkcs11
Source0:        https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  automake autoconf libtool
BuildRequires:  openssl-devel
Requires:       opencryptoki-libs%{?_isa}


%description
This package contains a shared object OpenSSL dynamic engine for the use
with a PKCS#11 implementation such as openCryptoki.

%prep
%autosetup -p1

./bootstrap.sh


%build
%configure --libdir=%{enginesdir}
%make_build


%install
%make_install
mv openssl.cnf.sample openssl.cnf.sample.%{_arch}
rm -f $RPM_BUILD_ROOT%{enginesdir}/*.la


%files
%license LICENSE
%doc README openssl.cnf.sample.%{_arch}
%{enginesdir}/ibmpkcs11.so


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.2-9
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Dan Horák <dan@danny.cz> - 1.0.2-1
- updated to 1.0.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Dan Horák <dan@danny.cz> - 1.0.1-2
- apply fix for autotools
- don't hard-code %%enginesdir

* Fri Jan 19 2018 Dan Horák <dan@danny.cz> - 1.0.1-1
- initial Fedora version
