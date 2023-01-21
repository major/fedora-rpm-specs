%global glib2_version 2.45.8
%global json_glib_version 1.1.1

Summary:   Library for reading Jcat files
Name:      libjcat
Version:   0.1.12
Release:   2%{?dist}
License:   LGPLv2+
URL:       https://github.com/hughsie/libjcat
Source0:   https://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: json-glib-devel >= %{json_glib_version}
BuildRequires: gnutls-devel
BuildRequires: gnutls-utils
BuildRequires: gpgme-devel
BuildRequires: vala

Requires: glib2%{?_isa} >= %{glib2_version}

%description
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package tests
Summary: Files for installed tests

%description tests
Executable and data files for installed tests.

%prep
%autosetup -p0

%build

%meson \
    -Dgtkdoc=true \
    -Dtests=true

%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%license LICENSE
%{_bindir}/jcat-tool
%{_datadir}/man/man1/*.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libjcat.so.1*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libjcat
%{_includedir}/libjcat-1
%{_libdir}/libjcat.so
%{_libdir}/pkgconfig/jcat.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/jcat.deps
%{_datadir}/vala/vapi/jcat.vapi

%files tests
%doc README.md
%{_libexecdir}/installed-tests/libjcat/*
%{_datadir}/installed-tests/libjcat/*
%dir %{_datadir}/installed-tests/libjcat

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 11 2022 Richard Hughes <richard@hughsie.com> 0.1.12-1
- New upstream release
- Correctly export the AliasIds in all cases
- Install all files to fix the installed-tests

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 16 2022 Richard Hughes <richard@hughsie.com> 0.1.10-1
- New upstream release
- Add ED25519 support
- Define three more types used for the firmware transparency log

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Richard Hughes <richard@hughsie.com> 0.1.9-1
- New upstream release
- Return an error if we try to self-sign no bytes of data
- Set which backends are supported in the pkgconfig file

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Richard Hughes <richard@hughsie.com> 0.1.8-1
- New upstream release
- Fix a warning when used in a subproject

* Thu May 06 2021 Richard Hughes <richard@hughsie.com> 0.1.7-1
- New upstream release
- Do not use help2man to build manual pages

* Mon Feb 08 2021 Richard Hughes <richard@hughsie.com> 0.1.6-1
- New upstream release
- Fall back to the AliasId for validation
- Fix jcat_context_verify_blob() to use self verify for checksums

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Richard Hughes <richard@hughsie.com> 0.1.5-1
- New upstream release
- Allow verifying expired certificates with an additional argument

* Fri Oct 23 2020 Richard Hughes <richard@hughsie.com> 0.1.4-1
- New upstream release
- Export the old JCatEngine property to preserve internal ABI

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream release
- Export the JcatBlobKind and JcatBlobMethod on the result

* Fri Jun 05 2020 Richard Hughes <richard@hughsie.com> 0.1.2-2
- Fix for CVE-2020-10759

* Mon Apr 27 2020 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream release
- Build fixes mostly for RHEL

* Tue Apr 14 2020 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream release
- Allow adding an item ID 'alias'
- Make the installed tests actually work

* Mon Mar 23 2020 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial release for Fedora package review
