%{?mingw_package_header}

Name:           mingw-libmicrohttpd
Version:        0.9.73
Release:        11%{?dist}
Summary:        MinGW package for libmicrohttpd

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnu.org/software/libmicrohttpd/
Source0:        https://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-gnutls

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-gnutls


%description
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.


# Mingw32
%package -n mingw32-libmicrohttpd
Summary:        MinGW package for libmicrohttpd

%description -n mingw32-libmicrohttpd
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.


%package -n mingw32-libmicrohttpd-static
Summary:        Static version of the libmicrohttpd library
Requires:       mingw32-libmicrohttpd = %{version}-%{release}


%description -n mingw32-libmicrohttpd-static
Static version of the libmicrohttpd library.


# Mingw64
%package -n mingw64-libmicrohttpd
Summary:        MinGW package for libmicrohttpd


%description -n mingw64-libmicrohttpd
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.


%package -n mingw64-libmicrohttpd-static
Summary:        Static version of the libmicrohttpd library
Requires:       mingw64-libmicrohttpd = %{version}-%{release}


%description -n mingw64-libmicrohttpd-static
Static version of the libmicrohttpd library.


%?mingw_debug_package


%prep
%setup -q -n libmicrohttpd-%{version}


%build
# microspdy is not MinGW-compatible at this time
%mingw_configure --with-gnutls --enable-spdy=no --enable-https=yes
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# remove documentation provided by native package
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/info
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/info
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

# remove libtool files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# remove libmicrospdy autotool files as we do not provide a dll
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig/libmicrospdy.pc
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig/libmicrospdy.pc


# Win32
%files -n mingw32-libmicrohttpd
%license COPYING
%{mingw32_bindir}/libmicrohttpd-12.dll
%{mingw32_includedir}/microhttpd.h
%{mingw32_libdir}/libmicrohttpd.dll.a
%{mingw32_libdir}/pkgconfig/libmicrohttpd.pc

%files -n mingw32-libmicrohttpd-static
%{mingw32_libdir}/libmicrohttpd.a


# Win64
%files -n mingw64-libmicrohttpd
%license COPYING
%{mingw64_bindir}/libmicrohttpd-12.dll
%{mingw64_includedir}/microhttpd.h
%{mingw64_libdir}/libmicrohttpd.dll.a
%{mingw64_libdir}/pkgconfig/libmicrohttpd.pc

%files -n mingw64-libmicrohttpd-static
%{mingw64_libdir}/libmicrohttpd.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.73-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.9.73-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Michael Cronenworth <mike@cchtml.com> - 0.9.73-1
- New upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Michael Cronenworth <mike@cchtml.com> - 0.9.55-1
- New upstream release

* Sat Apr 01 2017 Michael Cronenworth <mike@cchtml.com> - 0.9.52-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Michael Cronenworth <mike@cchtml.com> - 0.9.46-1
- New upstream release

* Fri Oct 09 2015 Michael Cronenworth <mike@cchtml.com> - 0.9.44-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Michael Cronenworth <mike@cchtml.com> - 0.9.39-2
- Rebuild against mingw-gnutls 3.4

* Wed Mar 25 2015 Michael Cronenworth <mike@cchtml.com> - 0.9.39-1
- New upstream release

* Sat Jan 03 2015 Michael Cronenworth <mike@cchtml.com> - 0.9.34-4
- Drop plibc

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.34-2
- Rebuild against mingw-libgcrypt 1.6

* Tue Mar 25 2014 Michael Cronenworth <mike@cchtml.com> - 0.9.34-1
- Update to 0.9.34

* Tue Jan 07 2014 Michael Cronenworth <mike@cchtml.com> - 0.9.33-1
- Update to latest upstream.
- Package review fixes.

* Fri Aug 30 2013 Michael Cronenworth <mike@cchtml.com> - 0.9.27-4
- Link against PlibC now that bad code has been removed.

* Wed Aug 07 2013 Michael Cronenworth <mike@cchtml.com> - 0.9.27-3
- Patches to remove more PlibC dependencies, fix pipe usage.

* Tue Aug 06 2013 Michael Cronenworth <mike@cchtml.com> - 0.9.27-2
- Patches to remove PlibC dependency.

* Thu Jul 25 2013 Michael Cronenworth <mike@cchtml.com> - 0.9.27-1
- Initial RPM release.

