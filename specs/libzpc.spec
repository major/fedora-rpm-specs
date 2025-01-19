Name:		libzpc
Version:	1.2.0
Release:	6%{?dist}
Summary:	Open Source library for the IBM Z Protected-key crypto feature

License:	MIT
Url:		https://github.com/opencryptoki/libzpc
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:	s390x
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	g++
BuildRequires:	make
BuildRequires:	json-c-devel

#Additional prerequisites for building the test program: libjson-c devel 
#Additional prereqs for building the html and latex doc: doxygen >= 1.8.17, latex, bibtex

# Be explicit about the soversion in order to avoid unintentional changes.
%global soversion 1

%description
The IBM Z Protected-key Crypto library libzpc is an open-source library
targeting the 64-bit Linux on IBM Z (s390x) platform. It provides interfaces
for cryptographic primitives. The underlying implementations make use of
z/Architecture's extensive performance-boosting hardware support and its
protected-key feature which ensures that key material is never present in
main memory at any time.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup %{name}-%{version}

# The following options can be passed to cmake:
#   -DCMAKE_INSTALL_PREFIX=<path> : 
#        Change the install prefix from `/usr/local/` to `<path>`.
#   -DCMAKE_BUILD_TYPE=<type> : Choose predefined build options. 
#        The choices for `<type>` are `Debug`, `Release`, `RelWithDebInfo`, 
#        and `MinSizeRel`.
#   -DBUILD_SHARED_LIBS=ON : Build a shared object (instead of an archive).
#   -DBUILD_TEST=ON : Build the test program.
#   -DBUILD_DOC=ON : Build the html and latex doc.
%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%doc README.md CHANGES.md
%license LICENSE
%{_libdir}/%{name}.so.%{soversion}*


%files devel
%{_includedir}/zpc/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Joerg Schmidbauer <jschmidb@de.ibm.com> - 1.2.0
- Support for get/set intermediate iv for CBC and XTS
- Support for internal iv for GCM
- Exploit KBLOB2PROTK3 ioctl for clear AES and EC keys
- Fix AES EP11 version 6 key support for generate and import_clear

* Wed Sep 20 2023 Joerg Schmidbauer <jschmidb@de.ibm.com> - 1.1.1
- Exploit PKEY_KBLOB2PROTK2 for AES EP11 version 6 keys
  
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 02 2023 Joerg Schmidbauer <jschmidb@de.ibm.com> - 1.1.0
- Support for ECC keys and ECDSA signatures.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jun 22 2022 Joerg Schmidbauer <jschmidb@de.ibm.com> - 1.0.1
- Updated spec file for rpm build and changed location
  of pkgconfig file to libdir.

* Mon Feb 21 2022 Joerg Schmidbauer <jschmidb@de.ibm.com> - 1.0.0
- Initial version based on libzpc provided by Patrick Steuer,
  <steuer@linux.vnet.ibm.com>

