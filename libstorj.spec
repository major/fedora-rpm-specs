Name: libstorj
Version: 1.0.3
Release: 12%{?dist}
Summary: Client library and CLI for encrypted file transfer on the Storj network
License: LGPLv2+
URL:     https://github.com/Storj/libstorj/
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?rhel} == 8
# libuv-devel not present on s390x on EL-8
ExcludeArch: s390x
%endif

Patch0: pbkdf2.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libmicrohttpd)
BuildRequires: pkgconfig(libuv)
BuildRequires: make

%package devel
Summary: Development files for libstorj
Requires: %{name}%{?_isa} = %{version}-%{release}

%description
Asynchronous multi-platform C client library and CLI for encrypted file
transfer on the Storj network.

%description devel
Asynchronous multi-platform C client library and CLI for encrypted file
transfer on the Storj network.

This package contains files needed to compile code using libstorj.

%prep
%autosetup -p0

%build
autoreconf -vif
%configure
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_bindir}/storj
%{_libdir}/libstorj.so.0
%{_libdir}/libstorj.so.0.0.0

%files devel
# Exclude static library files from package.
%exclude %{_libdir}/libstorj.a
%exclude %{_libdir}/libstorj.la
%doc README.md
%{_includedir}/storj.h
%{_libdir}/libstorj.so
%{_libdir}/pkgconfig/libstorj.pc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.0.3-9
- Rebuild for versioned symbols in json-c

* Thu Mar 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.0.3-8
- Fix FTBFS.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.0.3-6
- Exclude s390x on EL-8 due to missing libuv-devel

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.0.3-4
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Phil Wyett <philwyett@kathenas.org> - 1.0.3-1
- Use %%autosetup.
- Use %%exclude rather than rm for static lib files.
- Clean-ups and small lib need not wildcard for one file in a folder etc.
- Update to 1.0.3.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.2-5
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-3
- Rebuilt for libjson-c.so.3

* Wed Oct 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.2-2
- Review fixes.

* Wed Oct 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.2-1
- Initial package creation.
