Name:           gmime
Version:        2.6.23
Release:        23%{?dist}
Summary:        Library for creating and parsing MIME messages

# Files in examples/, src/ and tests/ are GPLv2+
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://spruce.sourceforge.net/gmime/
Source0:        http://download.gnome.org/sources/gmime/2.6/gmime-%{version}.tar.xz

BuildRequires:  glib2-devel >= 2.18.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpgme-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  vala-devel
BuildRequires:  vala
BuildRequires:  zlib-devel >= 1.2.1.1
BuildRequires:  gettext-devel, gtk-doc
BuildRequires:  automake autoconf

Patch3: gmime-2.5.8-gpg-error.patch

# mono available only on selected architectures
%ifarch  %mono_arches
%define buildmono 1
%else
%define buildmono 0
%endif

%if 0%{?rhel} >= 6
%define buildmono 0
%endif

%if 0%buildmono
BuildRequires:  mono-devel gtk-sharp2-gapi
BuildRequires:  gtk-sharp2-devel >= 2.4.0
%endif
BuildRequires: make

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).


%package        devel
Summary:        Header files to develop libgmime applications
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       glib2-devel

%description    devel
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME). The devel-package contains header files
to develop applications that use libgmime.

%if 0%buildmono
%package        sharp
Summary:        Mono bindings for gmime
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       gtk-sharp2

%description    sharp
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME). The devel-package contains support 
for developing mono applications that use libgmime.
%endif

%prep
%setup -q
%patch -P3 -p1 -b .gpg-error

%build
autoreconf -vif
MONO_ARGS="--enable-mono=no"
%if 0%buildmono
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
MONO_ARGS="--enable-mono"
%endif
# Don't conflict with sharutils.
%configure $MONO_ARGS --program-prefix=%{name} --disable-static

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1

%install
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS README TODO
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/GMime-2.6.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/gmime-2.6.pc
%{_includedir}/gmime-2.6
%{_datadir}/gir-1.0/GMime-2.6.gir
%{_datadir}/gtk-doc/html/gmime-2.6
%{_datadir}/vala/

%if 0%buildmono
%files sharp
%{_libdir}/pkgconfig/gmime-sharp-2.6.pc
%{_monogacdir}/gmime-sharp
%{_monodir}/gmime-sharp-2.6
%{_datadir}/gapi-2.0/gmime-api.xml
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.23-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Harry Míchal <harrymichal@seznam.cz> - 2.6.23-9
- Fix hardcoded paths

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Kalev Lember <klember@redhat.com> - 2.6.23-1
- Update to 2.6.23

* Sat Dec 17 2016 Kalev Lember <klember@redhat.com> - 2.6.22-1
- Update to 2.6.22
- Use license macro for COPYING
- Tighten subpackage dependencies

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 2.6.20-7
- BR vala instead of obsolete vala-tools subpackage

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.6.20-5
- Rebuild (mono4)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.6.20-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 2.6.20-1
- Update to 2.6.20

* Sat Jan 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.6.19-2
- Fix FTBFS
- cleanup spec
- fix ARM conditionals

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 2.6.19-1
- Update to 2.6.19

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 2.6.18-1
- Update to 2.6.18
- Enable introspection and vala support

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 2.6.17-1
- Update to 2.6.17

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 2.6.16-1
- Update to 2.6.16

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 2.6.15-1
- Update to 2.6.15

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 2.6.13-1
- Update to 2.6.13

* Mon Nov 12 2012 Kalev Lember <kalevlember@gmail.com> - 2.6.12-1
- Update to 2.6.12

* Sat Oct 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.6.11-1
- Update to 2.6.11

* Tue Jul 31 2012 Richard Hughes <hughsient@gmail.com> - 2.6.10-1
- Update to 2.6.10

* Tue Jul 24 2012 Kalev Lember <kalevlember@gmail.com> - 2.6.9-1
- Update to 2.6.9, sync with the f17 branch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Tomas Bzatek <tbzatek@redhat.com> - 2.6.4-1
- Update to 2.6.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 02 2011 Christian Krause <chkr@fedoraproject.org> - 2.6.1-2
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Tue Nov 22 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.6.1-1
- Update to 2.6.1

* Tue Jun 14 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.5.8-1
- Update to 2.5.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Dan Horák <dan[at]danny.cz> - 2.5.1-3
- sync the architecture list with the mono package

* Thu Oct 28 2010 Christian Krause <chkr@fedoraproject.org> - 2.5.1-2
- Rebuilt against Mono 2.8

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.5.1-1
- Update to 2.5.1

* Wed Nov 18 2009 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.11-2
- Enabled rpath removal, got confirmation that it should be safe now

* Wed Nov 18 2009 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.11-1
- Updated to 2.4.11
- Adjusted the license tag (fixes RH bug #522630)
- Got rid of rpath issue properly (but left disabled, need to confirm why chrpath was dropped in the first place)

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 2.4.7-3
- build mono support on s390 and s390x
- exclude mono support on sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.4.7-1
- Update to 2.4.7

* Mon May 25 2009 Xavier Lamien <laxaathom@fedoraprojet.org> - 2.4.3-5
- Build arch ppc64.
- Fix uu??code binaries.

* Tue Mar 31 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.4.3-4
- Merge review feedback (#225808)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.4.3-2
- Update to 2.4.3

* Fri Oct 24 2008 Xavier Lamien <lxtnow@gmail.com> - 2.2.23-2
- Fix Strong name check.

* Mon Sep 15 2008 Matthias Clasen <mclasen@redhat.com> - 2.2.23-1
- Update to 2.2.23
- Drop static libraries from -devel

* Tue May 27 2008 Matthias Clasen <mclasen@redhat.com> - 2.2.21-1
- Update to 2.2.21

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.2.19-1
- Update to 2.2.19
- Fix source url

* Thu Mar 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.2.18-1
- Update to 2.2.18

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.2.17-1
- Update to 2.2.17

* Wed Feb  6 2008 Matthias Clasen <mclasen@redhat.com> - 2.2.16-1
- Update to 2.2.16

* Tue Jan 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.2.15-1
- Update to 2.2.15

* Sun Dec 16 2007 Matthias Clasen  <mclasen@redhat.com> 2.2.12-1
- Update to 2.2.12

* Tue Nov 13 2007 Matthias Clasen  <mclasen@redhat.com> 2.2.11-1
- Update to 2.2.11

* Fri Oct 12 2007 Matthias Clasen  <mclasen@redhat.com> 2.2.10-5
- Don't export unnamespaced internal symbols (#216434)

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.2.10-4
- Rebuild for selinux ppc32 issue.

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 2.2.10-2
- Rebuild for RH #249435

* Mon Jul 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.2.10-1
- Update to 2.2.10

* Sun Jul 08 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.2.9-3
- there is no mono for ppc64 as well

* Fri Jul 06 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.2.9-2
- build stuff depending on mono on all archs except those where
  we know there is no mono (fixes alpha, #246437)

* Tue May 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.2.9-1
- Update to 2.2.9

* Mon May 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.2.8-1
- Update to 2.2.8

* Tue Feb  6 2007 Alexander Larsson <alexl@redhat.com> - 2.2.3-5
- Fix build with new automake (#224157)

* Thu Oct 12 2006 Alexander Larsson <alexl@redhat.com> - 2.2.3-4
- Bump glib requirement to 2.6 (#209565)

* Tue Sep  5 2006 Alexander Larsson <alexl@redhat.com> - 2.2.3-3
- fix gmime-config multilib conflict (#205208)

* Sat Aug 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.3-2
- Rebuild

* Fri Aug 18 2006 Alexander Larsson <alexl@redhat.com> - 2.2.3-1
- Upgrade to 2.2.3
- Use the new mono libdir

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri Jun  9 2006 Alexander Larsson <alexl@redhat.com> - 2.2.1-2
- Disable mono parts on s390* as mono doesn't build on s390 atm

* Tue May 23 2006 Alexander Larsson <alexl@redhat.com> - 2.2.1-1
- Update to 2.2.1
- Fix multilib -devel conflict by using pkg-config in gmime-config (#192675)

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 2.1.19-4
- BuildRequires: gtk-sharp2 on mono archs only

* Sun Feb 12 2006 Christopher Aillon <caillon@redhat.com> - 2.1.19-3
- Rebuild

* Tue Feb  7 2006 Jesse Keating <jkeating@redhat.com> - 2.1.19-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> - 2.1.19-2
- Rebuild

* Sun Jan 22 2006 Alexander Larsson <alexl@redhat.com> - 2.1.19-1
- Update to 2.1.19 (needed by beagle 0.2.0)

* Thu Jan 19 2006 Alexander Larsson <alexl@redhat.com> 2.1.17-3
- Build on s390x

* Mon Jan  9 2006 Alexander Larsson <alexl@redhat.com> 2.1.17-2
- build gmime-sharp conditionally on mono arches

* Mon Jan  9 2006 Alexander Larsson <alexl@redhat.com> - 2.1.17-1
- Move from Extras to Core, Update to 2.1.17, add gmime-sharp subpackage

* Wed Aug 10 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.1.15-1
- Update to 2.1.15
- Use dist

* Wed May 18 2005 Colin Charles <colin@fedoraproject.org> - 2.1.9-5
- bump release, request build on ppc

* Thu Mar 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.1.9-4
- add dep glib2-devel for pkgconfig in -devel package

* Mon Oct 18 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:2.1.9-0.fdr.3
- Remove ldconfig from Requires pre and post

* Mon Oct 18 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:2.1.9-0.fdr.2
- BR zlib-devel
- Don't ship empty news file
- Fixes to the files section
- Change ldconfig in post* calls to -p /sbin/ldconfig


* Sun Oct 17 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:2.1.9-0.fdr.1
- Initial RPM release.
