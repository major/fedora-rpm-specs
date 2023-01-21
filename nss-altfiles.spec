%global commit 89f3f0b390f3bbc58d8964b11a517173ed4eed78
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: NSS module to look up users in /usr/lib/passwd too
Name: nss-altfiles
Version: 2.18.1
Release: 22%{?dist}
#VCS: https://github.com/aperezdc/nss-altfiles
Source0: https://github.com/aperezdc/nss-altfiles/archive/v%{version}.tar.gz
# From pull request: https://github.com/marineam/nss-altfiles/commit/dda5073238b88b4537f2d2707b0ef67bdd11fe06
# FIXME: Change nss-altfiles to not use glibc internal symbols
#Patch0: 0001-Explicitly-link-to-libc.patch
Patch1: 0001-build-sys-Inherit-LDFLAGS.patch
License: LGPLv2+
URL: https://github.com/aperezdc/nss-altfiles

BuildRequires: make
BuildRequires: glibc-devel
BuildRequires: gcc
BuildRequires: git

%description
When installed, this package allows looking up users
in %{prefix}/lib/passwd, similarly, groups in %{prefix}/lib/group.

%prep
%autosetup -Sgit

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README.md
%{_libdir}/*.so.*

%ldconfig_scriptlets

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Colin Walters <walters@verbum.org> - 2.18.1-13
- BR gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.18.1-3
- Build with $RPM_OPT_FLAGS

* Tue Apr 08 2014 Colin Walters <walters@verbum.org>
- Revert patch to link to libc, causes a dep on GLIBC_PRIVATE

* Sat Mar 22 2014 Colin Walters <walters@verbum.org>
- Initial packaging
