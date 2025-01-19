Name:		libu2f-server
Version:	1.0.1
Release:	32%{?dist}
Summary:	Yubico Universal 2nd Factor (U2F) Server C Library

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://developers.yubico.com/%{name}
Source0:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.xz
Source1:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.xz.sig
Source2:	gpgkey-01F3D14D.gpg

# Picked from upstream
# https://github.com/Yubico/libu2f-server/commit/5d74f88b278ca1df6c69d7328be2a8035ca7976c
Patch0:		%{name}-1.0.1_fix_memory_errors.patch
# https://github.com/Yubico/libu2f-server/commit/72997944d5ee7f165fe04f1ac451d115e97d75e9
Patch1:		%{name}-1.0.1_check_result_json_object.patch
# https://github.com/Yubico/libu2f-server/pull/31
Patch2:		%{name}-1.0.1_fix_refcount_json_object.patch
# https://github.com/Yubico/libu2f-server/pull/42
Patch3:		%{name}-1.0.1_add_support_for_upcoming_json_c_0_14_0.patch

#BuildRequires:	json-c-devel openssl-devel check-devel gnupg2 systemd
BuildRequires:  gcc
BuildRequires:	json-c-devel openssl-devel check-devel systemd
BuildRequires: make

# Bundled gnulib https://fedorahosted.org/fpc/ticket/174
Provides:	bundled(gnulib)

%description
This is a C library that implements the server-side of the U2F protocol. More
precisely, it provides an API for generating the JSON blobs required by U2F
devices to perform the U2F Registration and U2F Authentication operations, and
functionality for verifying the cryptographic operations.

%package -n u2f-server
Summary:	Server-side command-line tool for U2F devices
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n u2f-server
u2f-server provides a command line tool that implements the server-side of the
U2F protocol.


%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed to develop applications that
use libu2f-server.

%global _hardened_build 1

%prep
# disable signature verficiation due to gpgv2 bug
# https://bugzilla.redhat.com/show_bug.cgi?id=1292687
#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p 1

%build
%configure --disable-rpath --disable-static

# --disable-rpath doesn't work.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
LD_LIBRARY_PATH="$(pwd)/u2f-server/.libs" make check

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc README AUTHORS NEWS THANKS
%{_libdir}/*.so.*

%files -n u2f-server
%{_bindir}/u2f-server
%{_mandir}/man1/u2f-server.1*

%files devel
%doc %{_datadir}/gtk-doc/html/u2f-server
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.1-23
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.0.1-21
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.0.1-18
- Rebuild (json-c)

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 1.0.1-17
- Add support for upcoming json-c 0.14.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.1-12
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-10
- Add upstreamed patch for proper refcount on json_objects

* Wed Dec 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-9
- Add two cherry-picked patches from upstream

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-8
- Rebuilt for libjson-c.so.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 4 2016 Seth Jennings <spartacus06@gmail.com> - 1.0.1-4
- disable signature verficiation due to gpgv2 bug

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.1-2
- Enable _hardened_build
- Remove redundant license from u2f-server package
- More specific path for gtk-doc files

* Sat Aug 1 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.1-1
- Initial package release.
