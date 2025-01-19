Name:			libsafec
Version:		3.7.1
Release:		6%{?dist}
Summary:		Safec fork with all C11 Annex K functions

License:		MIT
URL:			https://github.com/rurban/safeclib
Source0:		%url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	libtool

%description
This library implements the secure C11 Annex K1 functions on top of most
libc implementations, which are missing from them.

%package -n libsafec-devel
Summary: Development packages for libsafec
Requires:		libsafec%{?_isa} = %{version}-%{release}

%description -n libsafec-devel
Development files for libsafec

%package -n libsafec-check
Summary: Finds unsafe APIs
Requires:		perl-DirHandle

%description -n libsafec-check
Traverses specified directory trees and/or files (cwd by default)
searching for C source files (*.c), rooting out unsafe API calls.

%prep
%autosetup -n safeclib-%{version}

%build
autoreconf -Wall --install
%configure --disable-static --disable-doc --enable-strmax=0x8000
%make_build

%install
%make_install

%files -n libsafec
%license COPYING
%{_libdir}/libsafec.so.*

%files -n libsafec-devel
%{_includedir}/safeclib
%{_libdir}/libsafec.so
%{_libdir}/pkgconfig/*.pc

%files -n libsafec-check
%license COPYING
%{_bindir}/check_for_unsafe_apis

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1 (RHBZ #2045831)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Juston Li <juston.li@intel.com> - 3.3-3
- Fix versioning, just use simple 3.3 version
- Add comments for packages
- Capitalize summary/description
- use make_build macro
- remove ldconfig for f28
- remote defattr
- remove redundent include header files
- remote .la file

* Mon Jul 02 2018 Juston Li <juston.li@intel.com> - 03032018-2
- Add pkgconfig_include.patch to fix pkgconfig include path

* Mon Jun 25 2018 Juston Li <juston.li@intel.com> - 03032018-1
- Initial spec
