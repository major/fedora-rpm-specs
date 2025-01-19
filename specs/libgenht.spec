%global srcname genht

Name:           lib%{srcname}
Version:        1.1.3
Release:        7%{?dist}
Summary:        Simple generic hash table implementation in C

License:        LicenseRef-Fedora-Public-Domain
URL:            http://repo.hu/projects/genht
Source0:        http://repo.hu/projects/genht/releases/%{srcname}-%{version}.tar.gz

# patch Makefile to accept CFLAGS and LDFLAGS from environment, set SONAME and create an .so file
Patch0:         00-fix-makefile.patch

BuildRequires:  gcc
BuildRequires:  make

%description
genht is a simple generic hash table implementation in C.
Uses open addressing scheme with space doubling.
Type generics is achieved by ugly name prefixing macros.

%package devel
Summary:        Libraries, includes, etc. to develop applications using genht
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries, includes, etc. to develop applications using genht.

%package static
Summary:        static library for genht
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description static
Static library to develop applications using genht. Please, prefer the shared libraries.


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%set_build_flags
%make_build

%install
# Depending on arch, install in /usr/lib or /usr/lib64.
%make_install LIBDIR=%{buildroot}/%{_libdir}


%files
%license src/LICENSE
%doc src/AUTHORS
%{_libdir}/libgenht.so.1
%{_libdir}/libgenht.so.%{version}

%files devel
%{_includedir}/%{srcname}/
%{_libdir}/libgenht.so

%files static
%{_libdir}/libgenht.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Alain Vigne <avigne@fedoraproject.org> - 1.1.3-1
- Upstream release 1.1.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 29 2021 Alain <alain DOT vigne DOT 14 AT gmail DOT com> 1.1.2-1
- New upstream release
- Install the .a lib in -static subpackage

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 01 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> 1.0.1-3
- Remove static subpackage
- Patch the Makefile to install the .so file link.

* Sat Nov 24 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> 1.0.1-2
- Implement suggestions from review

* Sat Nov 17 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> 1.0.1-1
- Initial proposal
