Name:           gnome-sharp
Version:        2.24.2
Release:        38%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            ftp://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.24/
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.24/gnome-sharp-%{version}.tar.bz2

Patch0: %{name}-2241-getopts.patch
# init gtype before using gconf
Patch2: gnome-sharp-gconf-init.patch
# https://github.com/meebey/gnome-sharp/commit/e9d06b56a54dcd399d1d3eaaf62bdacb7e07084d
Patch3: gnome-sharp-2.24.2-dbus-thread-fix.patch
# https://github.com/mono/gnome-sharp/commit/d797ce61a18f8238acd2f9a7bf97b157ae70b443
Patch4: gnome-sharp-2.24.2-canvaspathdef.patch
# https://github.com/mono/gnome-sharp/commit/cfabe1b0a581f8cd10ec75d347a93ebc1c365ac7
Patch5: gnome-sharp-2.24.2-gconf-path.patch

BuildRequires:  mono-devel gtk2-devel libart_lgpl-devel gnome-vfs2-devel libgnomecanvas-devel libgnomeui-devel
BuildRequires:  gtk-sharp2-devel >= 2.12.7
BuildRequires:  gtk-sharp2-gapi >= 2.12.7
BuildRequires:  librsvg2-devel vte291-devel
BuildRequires:  automake, libtool
BuildRequires: make

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. gnome-sharp
extends gtk-sharp2 and adds bindings for gconf, libgnome, gnome-vfs,
libart, librsvg, and vte291.

%package devel
Summary: Files needed for developing with gnome-sharp
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package provides the necessary development libraries and headers
for writing gnome-sharp2 applications.

%prep
%setup -q
%patch -P0 -p1 -b .getopts
%patch -P2 -p1 -b .gconf-init
%patch -P3 -p1 -b .threadfix
%patch -P4 -p1 -b .canvaspathdef
%patch -P5 -p1 -b .gconfpath

%build
autoreconf --force --install
aclocal
#sed -i -e 's!-r:Mono.GetOptions.dll! !' sample/gnomevfs/Makefile.in
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
%configure
make

%install
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.*a

%ldconfig_scriptlets

%files
%doc COPYING ChangeLog README
%{_bindir}/gconfsharp2-schemagen
%{_prefix}/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%{_libdir}/*.so
%{_prefix}/lib/mono/gac
%{_prefix}/lib/mono/gtk-sharp-2.0/*.dll
%{_datadir}/gapi-2.0/*

%files devel
%{_libdir}/pkgconfig/*-sharp-2.0.pc
%{_libdir}/pkgconfig/gconf-sharp-peditors-2.0.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.24.2-37
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-27
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.24.2-24
- switch from vte to vte291

* Wed Jul 31 2019 Tom Callaway <spot@fedoraproject.org> - 2.24.2-23
- rebuild for auto-provides/requires

* Mon Jul 29 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.24.2-22
- fix to build with Mono 5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Timotheus Pokorra <tp@tbits.net> - 2.24.2-18
- fix FTBFS related to CanvasPathDef

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-13
- mono rebuild for aarch64 support

* Tue Feb 16 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.24.2-12
- Remove libgnomeprint deps (#1307549)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.24.2-9
- Rebuild (mono4)

* Tue Mar 24 2015 Than Ngo <than@redhat.com> - 2.24.2-8
- use %%mono_arches

* Mon Sep 15 2014 Karsten Hopp <karsten@redhat.com> 2.24.2-7
- drop ppc64le

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 2.24.2-4
- Changing ppc64 to power64 macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.24.2-2
- Drop dead gnome-panel dependency

* Wed Mar 27 2013 Tom Callaway <spot@fedoraproject.org> - 2.24.2-1
- update to 2.24.2
- explicitly initialize dbus glib threading

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.24.1-8
- Rebuild for new libpng

* Sun Oct 23 2011 Christian Krause <chkr@fedoraproject.org> - 2.24.1-7
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Mon Mar 28 2011 Christian Krause <chkr@fedoraproject.org> - 2.24.1-6
- Rebuilt against mono-2.10
- Remove gtkhtml binding
- Minor spec file cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Dan Horák <dan[at]danny.cz> - 2.24.1-4
- updated the supported arch list

* Fri Oct 29 2010 Christian Krause <chkr@fedoraproject.org> - 2.24.1-3
- Rebuild again to create correct requires/provides capabilities

* Sat Oct 09 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.24.1-2
- Rebuild
- Alter mono-cairo export position
- Add Mono.GetOptions patch (gone in Mono 2.8)

* Wed Jun 23 2010 Christian Krause <chkr@fedoraproject.org> - 2.24.1-1
- Update to most recent upstream version 2.24.1
- Cleanup spec file

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 2.24.0-7
- build sparcv9

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Karsten Hopp <karsten@redhat.com> 2.24.0-5
- mono is available on s390x

* Mon May 25 2009 Xavier lamien <laxathom@fedoraproject.org> - 2.24.0-4
- build ppc64.

* Sat Apr  4 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.0-3
- Make tomboy work before gconfd is started (#494065)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 16 2008 Dan Winship <dwinship@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Thu Jul 03 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.20.0-2
- Fix gnome-sharp-2.0 pkconfig.

* Thu Jul 03 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.20.0-1
- Update release.

* Wed Jun 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.16.1-3
- fix license, fix libdir patch (gconf-sharp-peditors-2.0.pc)

* Tue Jun 03 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.16.1-2
- Rebuild against new gtk-sharp2.

* Fri Apr 11 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.16.1-1
- Updated Release.

* Wed Mar 05 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.16.0-7
- Fixed Assembly_dir on Rawhide (bug #434280).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.16.0-6
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.16.0-5
- Rebuild for selinux ppc32 issue.

* Thu Jul 26 2007 Matthias Clasen <mclasen@redhat.com> - 2.16.0-4
- Add alpha to ExclusiveArch (#246205)

* Tue Jul 17 2007 Xavier Lamien < lxtnow[at]gmail.com > - 2.16.0-3
- Fixed gtkhtml dependency version [bug #247831]

* Tue Jul 10 2007 Xavier Lamien < lxtnow[at]gmail.com > - 2.16.0-2
- Fixed build with automake-1.10 [bug #247592].

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Fri Aug 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.0-2.fc6
- Require pkgconfig, not pkg-config

* Mon Aug 14 2006 Alexander Larsson <alexl@redhat.com> - 2.15.0-1
- Initial version split out from gtk-sharp2
