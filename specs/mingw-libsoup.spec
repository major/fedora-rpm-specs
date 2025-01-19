%{?mingw_package_header}

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:		mingw-libsoup
Version:	2.74.3
Release:	9%{?dist}
Summary:	MinGW library for HTTP and XML-RPC functionality

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
URL:		https://wiki.gnome.org/Projects/libsoup
Source0:	https://download.gnome.org/sources/libsoup/%{release_version}/libsoup-%{version}.tar.xz
# Fix initialization from incompatible pointer type
Patch0:         libsoup-incompat-pointer-type.patch
# Backport fix for CVE-2024-52532
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/6adc0e3eb74c257ed4e2a23eb4b2774fdb0d67be
Patch1:         CVE-2024-52532.patch
# Backport fix for CVE-2024-52530
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/04df03bc092ac20607f3e150936624d4f536e68b
Patch2:         CVE-2024-52530.patch

BuildArch:	noarch

BuildRequires: gcc
BuildRequires: meson

BuildRequires: mingw32-filesystem >= 107
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gcc
BuildRequires: mingw32-glib2
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-brotli
BuildRequires: mingw32-libpsl
BuildRequires: mingw32-sqlite

BuildRequires: mingw64-filesystem >= 107
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gcc
BuildRequires: mingw64-glib2
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-brotli
BuildRequires: mingw64-libpsl
BuildRequires: mingw64-sqlite

# For glib-genmarshal
BuildRequires:	glib2-devel
BuildRequires:	intltool

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of Libsoup


# Win32
%package -n mingw32-libsoup
Summary:	MinGW library for HTTP and XML-RPC functionality
Requires:       pkgconfig
Requires:       mingw32-glib-networking
# Dropped in F25
Obsoletes:      mingw32-libsoup-static < 2.54.1

%description -n mingw32-libsoup
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of Libsoup

# Win64
%package -n mingw64-libsoup
Summary:        MinGW library for HTTP and XML-RPC functionality
Requires:       pkgconfig
Requires:       mingw64-glib-networking
# Dropped in F25
Obsoletes:      mingw64-libsoup-static < 2.54.1

%description -n mingw64-libsoup
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of Libsoup


%{?mingw_debug_package}


%prep
%autosetup -p1 -n libsoup-%{version}

%build
%mingw_meson \
    -Dgtk_doc=false \
    -Dgssapi=disabled \
    -Dintrospection=disabled \
    -Dtests=false \
    -Dtls_check=false \
    -Dvapi=disabled

%install
%mingw_ninja_install

# Remove the .la files
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la

%mingw_find_lang libsoup

# Win32
%files -n mingw32-libsoup -f mingw32-libsoup.lang
%license COPYING
%{mingw32_bindir}/libsoup-2.4-1.dll
%{mingw32_bindir}/libsoup-gnome-2.4-1.dll
%{mingw32_includedir}/libsoup-2.4
%{mingw32_includedir}/libsoup-gnome-2.4
%{mingw32_libdir}/libsoup-2.4.dll.a
%{mingw32_libdir}/libsoup-gnome-2.4.dll.a
%{mingw32_libdir}/pkgconfig/libsoup-2.4.pc
%{mingw32_libdir}/pkgconfig/libsoup-gnome-2.4.pc

# Win64
%files -n mingw64-libsoup -f mingw64-libsoup.lang
%license COPYING
%{mingw64_bindir}/libsoup-2.4-1.dll
%{mingw64_bindir}/libsoup-gnome-2.4-1.dll
%{mingw64_includedir}/libsoup-2.4
%{mingw64_includedir}/libsoup-gnome-2.4
%{mingw64_libdir}/libsoup-2.4.dll.a
%{mingw64_libdir}/libsoup-gnome-2.4.dll.a
%{mingw64_libdir}/pkgconfig/libsoup-2.4.pc
%{mingw64_libdir}/pkgconfig/libsoup-gnome-2.4.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Sandro Mani <manisandro@gmail.com> - 2.74.3-8
- Backport fix for CVE-2024-52530 and CVE-2024-52532

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.74.3-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 30 2022 Sandro Mani <manisandro@gmail.com> - 2.74.3-1
- Update to 2.74.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.74.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Sandro Mani <manisandro@gmail.com> - 2.74.2-1
- Update to 2.74.2

* Thu Oct 28 2021 Sandro Mani <manisandro@gmail.com> - 2.74.1-1
- Update to 2.74.1

* Fri Sep 10 2021 Sandro Mani <manisandro@gmail.com> - 2.74.0-1
- Update to 2.74.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.72.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Sandro Mani <manisandro@gmail.com> - 2.72.0-1
- Update to 2.72.0

* Tue Sep 08 2020 Sandro Mani <manisandro@gmail.com> - 2.71.1-1
- Update to 2.71.1

* Wed Aug 12 13:43:26 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.71.0-2
- Rebuild (mingw-gettext)

* Fri Jul 31 2020 Sandro Mani <manisandro@gmail.com> - 2.71.0-1
- Update to 2.71.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.70.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 2.70.0-2
- Rebuild (gettext)

* Sat Mar 07 2020 Sandro Mani <manisandro@gmail.com> - 2.70.0-1
- Update to 2.70.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.68.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Sandro Mani <manisandro@gmail.com> - 2.68.3-1
- Update to 2.68.3

* Thu Nov 14 2019 Sandro Mani <manisandro@gmail.com> - 2.68.2-1
- Update to 2.68.2

* Thu Nov 07 2019 Fabiano Fidêncio <fidencio@redhat.com> - 2.68.0-3
- Enable GNOME support

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.68.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Aug 15 2019 Fabiano Fidêncio <fidencio@redhat.com> - 2.68.0-1
- Update to its native counter-part version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59.90.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59.90.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.59.90.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.59.90.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.59.90.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Kalev Lember <klember@redhat.com> - 2.59.90.1-2
- Bump and rebuild for an rpm signing issue

* Thu Aug 10 2017 Kalev Lember <klember@redhat.com> - 2.59.90.1-1
- Update to 2.59.90.1 (CVE-2017-2885)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.58.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 2.58.1-1
- Update to 2.58.1

* Sat Feb 11 2017 Richard W.M. Jones <rjones@redhat.com> - 2.56.0-3
- Add BR python.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 2.56.0-1
- Update to 2.56.0

* Wed Sep 07 2016 Kalev Lember <klember@redhat.com> - 2.54.1-1
- Update to 2.54.1
- Drop static subpackage as the static libs don't build any more
- Don't set group tags
- Update project URLs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 2.52.2-2
- Use global instead of define.

* Wed Nov 18 2015 Kalev Lember <klember@redhat.com> - 2.52.2-1
- Update to 2.52.2

* Fri Oct 16 2015 Kalev Lember <klember@redhat.com> - 2.52.1-1
- Update to 2.52.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 2.50.0-1
- Update to 2.50.0
- Use license macro for the COPYING file

* Mon Dec 01 2014 Fabiano Fidêncio <fidencio@redhat.com> - 2.48.0-2
- Add mingw-glib-networking as dep (#1169185)

* Tue Oct 14 2014 Kalev Lember <kalevlember@gmail.com> - 2.48.0-1
- Update to 2.48.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.46.0-1
- Update to 2.46.0

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.44.2-1
- Update to 2.44.2

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.43.90-1
- Update to 2.43.90

* Sat Aug  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.43.5-1
- Update to 2.43.5
- Make sure translations get installed to the correct folder (intltool bug #398571)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.43.4-1
- Update to 2.43.4

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.43.1-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Thu May  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.43.1-1
- Update to 2.43.1

* Fri Mar 29 2013 Kalev Lember <kalevlember@gmail.com> - 2.42.0-1
- Update to 2.42.0

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.41.92-1
- Update to 2.41.92

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Kalev Lember <kalevlember@gmail.com> - 2.40.2-1
- Update to 2.40.2

* Sat Oct 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.40.1-1
- Update to 2.40.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 2.38.1-1
- Update to 2.38.1

* Mon Mar 26 2012 Kalev Lember <kalevlember@gmail.com> - 2.38.0-1
- Update to 2.38.0

* Sun Mar 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.37.90-3
- Added win64 support

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 2.37.90-2
- Renamed the source package to mingw-libsoup (#800433)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.37.90-1
- Update to 2.37.90
- Remove the .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.37.5-2
- Rebuild against the mingw-w64 toolchain

* Tue Feb 07 2012 Kalev Lember <kalevlember@gmail.com> - 2.37.5-1
- Update to 2.37.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Kalev Lember <kalevlember@gmail.com> - 2.36.1-1
- Update to 2.36.1

* Sun Oct 02 2011 Kalev Lember <kalevlember@gmail.com> - 2.36.0-1
- Update to 2.36.0
- Spec cleanup for recent rpmbuild

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 2.34.1-2
- Rebuilt against win-iconv

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.34.1-1
- Update to 2.34.1
- Build with --with-gnome
- Dropped the BR: mingw32-gnutls as support for TLS connections has
  moved to glib-networking

* Sun Apr 24 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.34.0-1
- Update to 2.34.0

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 2.32.0-3
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.32.0-1
- Update to 2.32.0

* Fri Nov 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.1-1
- Update to 2.28.1

* Sat Sep 19 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.92-2
- Rebuild because of broken mingw32-gcc/mingw32-binutils
- Added a patch to workaround GNOME BZ #595176

* Thu Sep 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.92-1
- Update to 2.27.92
- Dropped the workaround for GNOME BZ #593845

* Tue Sep  1 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.91-1
- Update to 2.27.91

* Thu Aug 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.90-1
- Update to 2.27.90
- Automatically generate debuginfo subpackage
- Added BR: mingw32-gnutls for SSL support

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.1-1
- Update to 2.27.1

* Fri May 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.1-2
- Fixed license typo
- Use %%global instead of %%define
- Fixed mixed-use-of-spaces-and-tabs rpmlint warning

* Sat May  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.1-1
- Update to 2.26.1

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-2
- Added -static subpackage

* Fri Mar 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0

* Sat Feb 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.25.5-1
- Initial release

