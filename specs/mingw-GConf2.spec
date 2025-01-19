%?mingw_package_header

Summary:        MinGW Windows port of the GNOME 2.x Desktop Configuration Database System
Name:           mingw-GConf2
Version:        3.2.6
Release:        29%{?dist}
# Automatically converted from old format: LGPLv2 or MPLv1.1 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 OR LicenseRef-Callaway-MPLv1.1
URL:            http://www.gnome.org/
Source:         http://ftp.gnome.org/pub/GNOME/sources/GConf/3.2/GConf-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-dbus
BuildRequires:  mingw32-dbus-glib
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-dbus
BuildRequires:  mingw64-dbus-glib
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

BuildRequires:  intltool
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel

%description
MinGW Windows port of GConf, the GNOME configuration database. It
is used by the GNOME 2.x Desktop platform.


# Win32
%package -n mingw32-GConf2
Summary:        MinGW Windows port of the GNOME 2.x Desktop Configuration Database System

%description -n mingw32-GConf2
MinGW Windows port of GConf, the GNOME configuration database. It
is used by the GNOME 2.x Desktop platform.

%package -n mingw32-GConf2-static
Summary:        MinGW Windows port of the GNOME 2.x Desktop Configuration Database System
Requires:       mingw32-GConf2 = %{version}-%{release}

%description -n mingw32-GConf2-static
Static version of the MinGW Windows GConf2 library.

# Win64
%package -n mingw64-GConf2
Summary:        MinGW Windows port of the GNOME 2.x Desktop Configuration Database System

%description -n mingw64-GConf2
MinGW Windows port of GConf, the GNOME configuration database. It
is used by the GNOME 2.x Desktop platform.

%package -n mingw64-GConf2-static
Summary:        MinGW Windows port of the GNOME 2.x Desktop Configuration Database System
Requires:       mingw64-GConf2 = %{version}-%{release}

%description -n mingw64-GConf2-static
Static version of the MinGW Windows GConf2 library.


%?mingw_debug_package


%prep
%setup -q -n GConf-%{version}
autoreconf --install --force

%build
%mingw_configure --enable-shared --disable-static \
	--without-openldap --disable-defaults-service \
	--with-gtk=3.0 --disable-orbit
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

mv $(find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.dll') $RPM_BUILD_ROOT%{mingw32_bindir}
mv $(find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.dll') $RPM_BUILD_ROOT%{mingw64_bindir}

find $RPM_BUILD_ROOT -name '*.la' -delete

rm -f $RPM_BUILD_ROOT%{mingw32_sysconfdir}/xdg/autostart/gsettings-data-convert.desktop
rm -f $RPM_BUILD_ROOT%{mingw64_sysconfdir}/xdg/autostart/gsettings-data-convert.desktop
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}/man1
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}/man1

%mingw_find_lang GConf2

for f in $(find %{buildroot} -type f); do
	sed -i -e 's,#!/usr/bin/env python,#!/usr/bin/python3,' "${f}"
done

# Win32
%files -n mingw32-GConf2 -f mingw32-GConf2.lang
%doc COPYING README
%{mingw32_sysconfdir}/gconf/2/path
%{mingw32_sysconfdir}/gconf/gconf.xml.*
%{mingw32_bindir}/gconf-merge-tree.exe
%{mingw32_bindir}/gconftool-2.exe
%{mingw32_bindir}/gsettings-data-convert.exe
%{mingw32_bindir}/gsettings-schema-convert
%{mingw32_bindir}/libgconf-2-4.dll
%{mingw32_bindir}/libgconfbackend-oldxml.dll
%{mingw32_bindir}/libgconfbackend-xml.dll
%{mingw32_bindir}/libgsettingsgconfbackend.dll
%{mingw32_libexecdir}/gconfd-2.exe
%dir %{mingw32_includedir}/gconf/
%dir %{mingw32_includedir}/gconf/2/
%{mingw32_includedir}/gconf/2/gconf
%{mingw32_libdir}/libgconf-2.dll.a
%{mingw32_libdir}/gio/modules/libgsettingsgconfbackend.dll.a
%dir %{mingw32_libdir}/GConf/
%dir %{mingw32_libdir}/GConf/2/
%{mingw32_libdir}/GConf/2/libgconfbackend-oldxml.dll.a
%{mingw32_libdir}/GConf/2/libgconfbackend-xml.dll.a
%{mingw32_libdir}/pkgconfig/gconf-2.0.pc
%{mingw32_datadir}/aclocal/gconf-2.m4
%{mingw32_datadir}/dbus-1/services/org.gnome.GConf.service
%dir %{mingw64_datadir}/sgml/gconf/
%{mingw32_datadir}/sgml/gconf/gconf-1.0.dtd

# Win64
%files -n mingw64-GConf2 -f mingw64-GConf2.lang
%doc COPYING README
%dir %{mingw64_sysconfdir}/gconf/
%dir %{mingw64_sysconfdir}/gconf/2/
%{mingw64_sysconfdir}/gconf/2/path
%{mingw64_sysconfdir}/gconf/gconf.xml.*
%{mingw64_bindir}/gconf-merge-tree.exe
%{mingw64_bindir}/gconftool-2.exe
%{mingw64_bindir}/gsettings-data-convert.exe
%{mingw64_bindir}/gsettings-schema-convert
%{mingw64_bindir}/libgconf-2-4.dll
%{mingw64_bindir}/libgconfbackend-oldxml.dll
%{mingw64_bindir}/libgconfbackend-xml.dll
%{mingw64_bindir}/libgsettingsgconfbackend.dll
%{mingw64_libexecdir}/gconfd-2.exe
%dir %{mingw64_includedir}/gconf/
%dir %{mingw64_includedir}/gconf/2/
%{mingw64_includedir}/gconf/2/gconf
%{mingw64_libdir}/libgconf-2.dll.a
%{mingw64_libdir}/gio/modules/libgsettingsgconfbackend.dll.a
%dir %{mingw64_libdir}/GConf/
%dir %{mingw64_libdir}/GConf/2/
%{mingw64_libdir}/GConf/2/libgconfbackend-oldxml.dll.a
%{mingw64_libdir}/GConf/2/libgconfbackend-xml.dll.a
%{mingw64_libdir}/pkgconfig/gconf-2.0.pc
%{mingw64_datadir}/aclocal/gconf-2.m4
%{mingw64_datadir}/dbus-1/services/org.gnome.GConf.service
%dir %{mingw64_datadir}/sgml/gconf/
%{mingw64_datadir}/sgml/gconf/gconf-1.0.dtd



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.6-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.2.6-21
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:36:17 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.2.6-17
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 3.2.6-15
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Greg Hellings <greg.hellings@gmail.com> - 3.2.6-12
- Fix python shebang line

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Greg Hellings <greg.hellings@gmail.com> - 3.2.6-2
- Fixed spaces/tab rpmlint warning
- Removed ChangeLog file from distribution for encoding infractions
- Changed name to mingw-GConf2 in line with upstream

* Sun Jan 27 2013 Greg Hellings <greg.hellings@gmail.com> - 3.2.6-1
- Updated to new upstream release.
- Removed config*.cache files & replaced with autoreconf
- Removed older mingw RPM macros
- Removed reference to orbit dependency
- Corrected BuildRequires lines
- Removed redundant manpages
- Removed desktop autostart files
- Adjusted to using find_lang macro

* Wed Aug 22 2012 Greg Hellings <greg.hellings@gmail.com> - 3.2.5-1
- Initial build
