%?mingw_package_header

Name:           mingw-libglade2
Version:        2.6.4
Release:        41%{?dist}
Summary:        MinGW Windows Libglade2 library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/libglade/2.6/libglade-%{version}.tar.bz2
# http://bugzilla.gnome.org/show_bug.cgi?id=121025
Patch1:         libglade-2.0.1-nowarning.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=510736
Patch2:         libglade-secondary.patch
# As of pango 1.29.5 the gmodule library isn't pulled in automatically anymore
Patch3:         libglade-link-against-gmodule.patch

BuildArch:      noarch

BuildRequires:  gtk-doc
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-libxml2

BuildRequires:  mingw64-filesystem >= 68
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-libxml2

# Native one for msgfmt
BuildRequires:  gettext

# Needed for patch3
BuildRequires:  gtk2-devel
BuildRequires:  autoconf automake libtool

%description
MinGW Windows Libglade2 library.


# Win32
%package -n mingw32-libglade2
Summary:        MinGW Windows Libglade2 library
Requires:       pkgconfig

%description -n mingw32-libglade2
MinGW Windows Libglade2 library.

%package -n mingw32-libglade2-static
Summary:        Static MinGW Windows Libglade2 library
Requires:       mingw32-libglade2 = %{version}-%{release}

%description -n mingw32-libglade2-static
Static MinGW Windows Libglade2 library.

# Win64
%package -n mingw64-libglade2
Summary:        MinGW Windows Libglade2 library
Requires:       pkgconfig

%description -n mingw64-libglade2
MinGW Windows Libglade2 library.

%package -n mingw64-libglade2-static
Summary:        Static MinGW Windows Libglade2 library
Requires:       mingw64-libglade2 = %{version}-%{release}

%description -n mingw64-libglade2-static
Static MinGW Windows Libglade2 library.


%?mingw_debug_package


%prep
%setup -q -n libglade-%{version}
%patch -P1 -p1 -b .nowarning
%patch -P2 -p1 -b .secondary
%patch -P3 -p0 -b .gmodule

autoreconf --install --force


%build
%mingw_configure --disable-gtk-doc

cp glade/glade.def build_win32/glade
cp glade/glade.def build_win64/glade

%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/gtk-doc/html/libglade
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/gtk-doc/html/libglade

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-libglade2
%doc COPYING
%{mingw32_bindir}/libglade-2.0-0.dll
%{mingw32_bindir}/libglade-convert
%{mingw32_includedir}/libglade-2.0
%{mingw32_libdir}/libglade-2.0.dll.a
%{mingw32_libdir}/pkgconfig/libglade-2.0.pc

%dir %{mingw32_datadir}/xml/libglade
%{mingw32_datadir}/xml/libglade/glade-2.0.dtd

%files -n mingw32-libglade2-static
%{mingw32_libdir}/libglade-2.0.a

# Win64
%files -n mingw64-libglade2
%doc COPYING
%{mingw64_bindir}/libglade-2.0-0.dll
%{mingw64_bindir}/libglade-convert
%{mingw64_includedir}/libglade-2.0
%{mingw64_libdir}/libglade-2.0.dll.a
%{mingw64_libdir}/pkgconfig/libglade-2.0.pc

%dir %{mingw64_datadir}/xml/libglade
%{mingw64_datadir}/xml/libglade/glade-2.0.dtd

%files -n mingw64-libglade2-static
%{mingw64_libdir}/libglade-2.0.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.4-40
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.6.4-33
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:42:01 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.6.4-29
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 2.6.4-27
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-13
- Added win64 support (contributed by Mikkel Kruse Johnsen)

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-12
- Renamed the source package to mingw-libglade2 (RHBZ #800908)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-11
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-10
- Rebuild against libpng 1.5
- Fix compilation against pango 1.29.5
- Dropped unneeded RPM tags
- Dropped the dependency extraction overrides as that's done automatically as of RPM 4.9
- Dropped .la files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul  7 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-8
- Rebuild against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.6.4-7
- Dropped the gettext soft dependency patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-5
- Rebuild in order to have a soft dependency on mingw32-gettext
- Fixed FTBFS
- Use correct %%defattr tag
- Fixed a small rpmlint warning

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.4-3
- add debuginfo packages

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.4-2
- fix static Requires

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.4-1
- replace %%define with %%global
- update to 2.6.4
- move static library to its own subpackage
- add secondary patch from native libglade2 package

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-5
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-4
- Include license file.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-3
- Use _smp_mflags.
- +BR mingw32-libxml2.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-2
- Requires pkgconfig.

* Fri Nov 28 2008 Daniel P. Berrange <berrange@redhat.com> - 2.6.3-1
- Initial build
