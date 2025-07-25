%define glib2_version 2.26.0
%define pango_version 1.22.0
%define gtk2_version 2.20.0

Name: vte
Version: 0.28.2
Release: 45%{?dist}
Summary: A terminal emulator
License: LGPL-2.0-or-later
#VCS: git:git://git.gnome.org/vte
URL: http://developer.gnome.org/vte/
Source: http://download.gnome.org/sources/vte/0.28/%{name}-%{version}.tar.xz
# https://bugzilla.gnome.org/show_bug.cgi?id=663779
Patch0: vte-alt-meta-confusion.patch
# Python bindings bugfix
# https://bugzilla.redhat.com/show_bug.cgi?id=556200
Patch1: vte-python-bugfixes.patch
# limit arguments to avoid DOS
# http://git.gnome.org/browse/vte/patch/?id=feeee4b5832b17641e505b7083e0d299fdae318e
Patch2: vte-0.28.2-limit-arguments.patch
#
# aarch64 support
Patch3: http://ausil.fedorapeople.org/aarch64/vte/vte-aarch64.patch
# Fix control home/control end codes
# https://bugzilla.redhat.com/show_bug.cgi?id=1114074
Patch4: vte-0.28.2-control.patch
# Fix mc paste
# https://bugzilla.redhat.com/show_bug.cgi?id=1114301
Patch5: vte-0.28.2-paste-fix.diff
# Backport introspection fixes
# https://bugzilla.redhat.com/show_bug.cgi?id=1256535
Patch6: vte-0.28.2-introspection-fixes.patch
# Backport "cat bigfile" speedup
# https://bugzilla.gnome.org/show_bug.cgi?id=721944
Patch7: vte-0.28.2-performance.patch
# Backport shift-mouse grab "hang" fix
# https://bugzilla.gnome.org/show_bug.cgi?id=683730
Patch8: vte-0.28.2-683730.patch
# Backport extended xterm/urxvt mouse tracking support
# https://bugzilla.gnome.org/show_bug.cgi?id=681329
Patch9: vte-0.28.2-mouse-tracking.patch
Patch10: pointer-types.patch

BuildRequires: make
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: pango-devel >= %{pango_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: ncurses-devel
BuildRequires: gettext
BuildRequires: libXt-devel
BuildRequires: intltool
# Work around broken perl / perl-Carp
BuildRequires: perl-Carp
BuildRequires: gobject-introspection-devel

# systemd creates the utmp group
Requires: systemd

%description
VTE is a terminal emulator widget for use with GTK+ 2.0.

%package devel
Summary: Files needed for developing applications which use vte
Requires: %{name} = %{version}-%{release}
Requires: gtk2-devel
Requires: ncurses-devel
Requires: pkgconfig

%description devel
The vte-devel package includes the header files and developer docs
for the vte package.

Install vte-devel if you want to develop programs which will use
vte.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p2
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p0

%build
%configure \
        --enable-shared \
        --enable-static \
        --enable-introspection \
        --with-gtk=2.0 \
        --libexecdir=%{_libdir}/%{name} \
        --without-glX \
        --disable-gtk-doc \
        --disable-python
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove the .a and .la file.
rm $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.a
rm $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.la

# Remove static python modules and la files, which are probably useless to Python anyway.
rm -f $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/*.a

%find_lang vte-0.0

%files -f vte-0.0.lang
%doc COPYING HACKING NEWS README
%doc src/iso2022.txt
%doc doc/utmpwtmp.txt doc/boxes.txt doc/openi18n/UTF-8.txt doc/openi18n/wrap.txt
%{_libdir}/*.so.*
%dir %{_libdir}/vte
%attr(2711,root,utmp) %{_libdir}/vte/gnome-pty-helper
%{_datadir}/%{name}
%{_libdir}/girepository-1.0

#rpmlint gives:
#vte.x86_64: W: private-shared-object-provides /usr/lib64/python2.7/site-packages/gtk-2.0/vtemodule.so vtemodule.so()(64bit)
# This is not used by anything except possibly third party scripts, so we're leaving it in place.

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_bindir}/%{name}
%{_datadir}/gir-1.0
%doc %{_datadir}/gtk-doc/html/vte-0.0

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.28.2-42
- PAtch for modern C.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.28.2-39
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Petr Viktorin <pviktori@redhat.com> - 0.28.2-34
- Remove Requires on pygtk2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 2019 Lumír Balhar <lbalhar@redhat.com> - 0.28.2-30
- Disable Python 2 bindings

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Kevin Fenzi <kevin@scrye.com> - 0.28.2-28
- Fix last python unversioned deps.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Kevin Fenzi <kevin@scrye.com> - 0.28.2-25
- Depend on systemd for utmp group, not initscripts anymore. Fixes bug #1592402

* Sun May 06 2018 Kevin Fenzi <kevin@scrye.com> - 0.28.2-24
- Add backported patches for various issues. Fixes bug #1574683

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.28.2-22
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-18
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 0.28.2-16
- Enable GObject Introspection (#1256535)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Kevin Fenzi <kevin@scrye.com> 0.28.2-13
- Add patch to fix bracketed paste. Fixes bug #1114301
- Thanks to nerijus for the patch

* Sat Jun 28 2014 Kevin Fenzi <kevin@scrye.com> 0.28.2-12
- Add patch to fix control+home/control+end. Fixes bug #1114074
- Thanks to jskarvad for the patch

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Kevin Fenzi <kevin@scrye.com> 0.28.2-9
- Add patch to support aarch64. Fixes bug #926706

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.28.2-6
- Add patch for DOS. Fixes bug #832356
- fixes CVE-2012-2738

* Tue Apr 03 2012 Jon Ciesla <limburgher@gmail.com> - 0.28.2-5
- Added URL, fixed whitespace for Merge Review BZ 226534.
- Commented on odd provides for rpmlint warning.

* Sat Mar 10 2012 Kevin Fenzi <kevin@scrye.com> - 0.28.2-4
- Add patch for python bindings. Fixes bug #556200

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Matthias Clasen <mclasen@redhat.com> - 0.28.2-2
- Fix problems with Alt<>Meta with recent gtk

* Fri Nov 25 2011 Tomas Bzatek <tbzatek@redhat.com> - 0.28.2-1
- Update to 0.28.2

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 0.28.1-1
- Update to 0.28.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.co> - 0.28.0-1
- Update to 0.28.0

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.co> - 0.27.90-1
- Update to 0.27.90

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> 0.27.4-1
- Update to 0.27.4

* Thu Dec  2 2010 Matthias Clasen <mclasen@redhat.com> 0.27.2-1
- Update to 0.27.2

* Fri Oct 29 2010 Bill Nottingham <notting@redhat.com> 0.27.1-1
- Update to 0.27.1

* Mon Oct  4 2010 Matthias Clasen <mclasen@redhat.com> 0.27.0-1
- Update to 0.27.0

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> 0.26.0-1
- Update to 0.26

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> 0.25.91-1
- Update to 0.25.91

* Wed Aug 18 2010 Matthias Clasen <mclasen@redhat.com> 0.25.90-1
- Update to 0.25.90

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue May  4 2010 Matthias Clasen <mclasen@redhat.com> 0.25.1-1
- Update to 0.25.1

* Mon Apr 26 2010 Matthias Clasen <mclasen@redhat.com> 0.24.1-1
- Update to 0.24.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> 0.24.0-1
- Update to 0.24.0

* Fri Jan 29 2010 Behdad Esfahbod <behdad@redhat.com> 0.23.5-2
- Remove stale spec code

* Thu Jan 14 2010 Behdad Esfahbod <behdad@redhat.com> 0.23.5-1
- Update to 0.23.5

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.23.2-1
- Update to 0.23.2

* Wed Dec  3 2009 Behdad Esfahbod <behdad@redhat.com> 0.23.1-1
- Update to 0.23.1

* Mon Sep 28 2009 Behdad Esfahbod <behdad@redhat.com> 0.22.2-1
- Update to 0.22.2

* Fri Sep 25 2009 Behdad Esfahbod <behdad@redhat.com> 0.22.1-2
- Second try

* Fri Sep 25 2009 Behdad Esfahbod <behdad@redhat.com> 0.22.1-1
- Update to 0.22.1

* Mon Sep 21 2009 Behdad Esfahbod <behdad@redhat.com> 0.22.0-1
- Update to 0.22.0

* Fri Sep 18 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.7-2
- Update to 0.21.7, second try

* Fri Sep 18 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.7-1
- Update to 0.21.7

* Thu Sep 17 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.6-1
- Update to 0.21.6

* Tue Sep  8 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.5-1
- Update to 0.21.5

* Mon Aug 25 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.4-1
- Update to 0.21.4

* Mon Aug 25 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.3-1
- Update to 0.21.3

* Mon Aug 25 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.2-1
- Update to 0.21.2

* Mon Aug 24 2009 Behdad Esfahbod <behdad@redhat.com> 0.21.1-1
- Update to 0.21.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Matthias Clasen <mclasen@redhat.com> 0.20.5-2
- Rebuild against new gcc to get rid of crashes

* Wed Jun 10 2009 Matthias Clasen <mclasen@redhat.com> 0.20.5-1
- Update to 0.20.5

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> 0.20.3-1
- Update to 0.20.3

* Fri May 15 2009 Matthias Clasen <mclasen@redhat.com> 0.20.2-1
- Update to 0.20.2
- See http://download.gnome.org/sources/vte/0.20/vte-0.20.2.news

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> 0.20.1-1
- Update to 0.20.1
- See http://download.gnome.org/sources/vte/0.20/vte-0.20.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> 0.20.0-1
- Update to 0.20.0

* Wed Mar  4 2009 Warren Togami  <wtogami@redhat.com> 0.19.4-6
- remove workaround after gcc-4.4.0-0.22

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> 0.19.4-5
- Work around gcc 4.4 miscompilation

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Behdad Esfahbod <besfahbo@redhat.com> 0.19.4-3
- Add gtk2/pango/glib2 required versions
- Resolves #477213

* Tue Dec 16 2008 Matthias Clasen <mclasen@redhat.com> 0.19.4-2
- Update to 0.19.4

* Fri Dec  5 2008 Behdad Esfahbod <besfahbo@redhat.com> 0.19.3-1
- Update to 0.19.3

* Fri Dec  5 2008 Behdad Esfahbod <besfahbo@redhat.com> 0.19.2-1
- Update to 0.19.2

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.19.1-2
- Rebuild for Python 2.6

* Mon Dec  1 2008 Behdad Esfahbod <besfahbo@redhat.com> 0.19.1-1
- Update to 0.19.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.17.4-2
- Rebuild for Python 2.6

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 0.17.4-1
- Update to 0.17.4

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 0.17.3-1
- Update to 0.17.3

* Thu Aug 14 2008 Behdad Esfahbod <besfahbo@redhat.com> 0.17.2-1
- Update to 0.17.2

* Tue Aug  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.17.1-1
- Update to 0.17.1

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.16.14-1
- Update to 0.16.14

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 0.16.13-1
- Update to 0.16.13

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.16.12-2
- Autorebuild for GCC 4.3

* Tue Jan  8 2008 Matthias Clasen <mclasen@redhat.com> - 0.16.12-1
- Update to 0.16.12

* Fri Dec 21 2007 Matthias Clasen <mclasen@redhat.com> - 0.16.11-1
- Update to 0.16.11

* Thu Dec  6 2007 Matthias Clasen <mclasen@redhat.com> - 0.16.10-1
- Update to 0.16.10

* Tue Nov 06 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.16.9-2
- Package /usr/bin/vte in devel package
- Add docs to devel package

* Tue Sep 18 2007 Matthias Clasen <mclasen@redhat.com> - 0.16.9-1
- Update to 0.16.9

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 0.16.8-3
- Rebuild for PPC toolchain bug
- Fix %%doc listing

* Thu Aug  2 2007 Matthias Clasen <mclasen@redhat.com> 0.16.8-2
- Update the License field

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> 0.16.8-1
- Update to 0.16.8

* Sat Jul 28 2007 Matthias Clasen <mclasen@redhat.com> 0.16.7-1
- Update to 0.16.7

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> 0.16.6-1
- Update to 0.16.6

* Mon Jun 04 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.16.5-1
- Update to 0.16.5

* Fri May  4 2007 Matthias Clasen <mclasen@redhat.com> 0.16.3-2
- Fix a gnome-terminal crash with input methods

* Tue Apr 27 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.16.3-1
- Update to 0.16.3

* Tue Apr 10 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.16.1-1
- Update to 0.16.1
- Drop all patches.  All upstreamed.

* Wed Apr  4 2007 Ray Strode <rstrode@redhat.com> 0.16.0-4
- Add upstream patch from ickle to fix unicode input crash 
  (#235160)

* Mon Mar 26 2007 Matthias Clasen <mclasen@redhat.com> 0.16.0-3
- Add a patch to fix transparency (#232781)

* Sat Mar 24 2007 Matthias Clasen <mclasen@redhat.com> 0.16.0-2
- Add a patch to fix redraw problems

* Mon Mar 12 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.16.0-1
- Update to 0.16.0

* Thu Mar 01 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.15.6-1
- Update to 0.15.6

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> 0.15.5-1
- Update to 0.15.5

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> 0.15.3-1
- Update to 0.15.3

* Tue Jan 22 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.15.2-1
- Update to 0.15.2
- Drop upstreamed vte-0.15.1-segfault.patch

* Tue Jan 10 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.15.1-2
- Add vte-0.15.1-segfault.patch
- Fixes crasher on x86_64 (GNOME#394890)

* Tue Jan 09 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.15.1-1
- Update to 0.15.1

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.15.0-2
- rebuild for python 2.5

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> 0.15.0-1
- Update to 2.15.0

* Sat Oct 22 2006 Matthias Clasen <mclasen@redhat.com> 0.14.1-1
- Update to 2.14.1

* Tue Oct 17 2006 Behdad Esfahbod <besfahbo@redhat.com> 0.14.0-2
- Do not require bitmap-fonts

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> 0.14.0-1
- Update to 0.14.0

* Thu Aug 24 2006 Behdad Esfahbod <besfahbo@redhat.com> 0.13.4-1
- Update to 0.13.7

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.13.6-1.fc6
- Update to 0.13.6

* Wed Aug  2 2006 Matthias Clasen <mclasen@redhat.com> - 0.13.5-1.fc6
- Update to 0.13.5

* Tue Jul 25 2006 Behdad Esfahbod <besfahbo@redhat.com> 0.13.4-1
- Update to 0.13.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.13.3-1.1
- rebuild

* Mon Jul 10 2006 Behdad Esfahbod <besfahbo@redhat.com> 0.13.3-1
- Update to 0.13.3

* Thu Jun 15 2006 Behdad Esfahbod <besfahbo@redhat.com> 0.13.2-1
- Update to 0.13.2

* Sun May 28 2006 Stepan Kasal <skasal@redhat.com>    - 0.13.1-3
- Fix the URL of Source:.

* Tue May 23 2006 Matthias Clasen <mclasen@redhat.com> 0.13.1-2
- Make it build in mock

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> 0.13.1-1
- Update to 0.13.1

* Tue May  9 2006 Matthias Clasen <mclasen@redhat.com> 0.13.0-1
- Update to 0.13.0
- Remove "experimental" from descriptions

* Mon May  8 2006 Kristian Høgsberg <krh@redhat.com> 0.12.1-3
- Bump and rebuild in rawhide.

* Mon May  8 2006 Kristian Høgsberg <krh@redhat.com> 0.12.1-2.fc5aiglx
- Build with fc5aiglx sub-release for FC5 AIGLX repository.

* Fri Apr 28 2006 Matthias Clasen <mclasen@redhat.com> 0.12.1-2
- Update to 0.12.1

* Thu Apr 13 2006 Kristian Høgsberg <krh@redhat.com> 0.12.0-3
- Bump for rawhide build.

* Thu Apr 13 2006 Kristian Høgsberg <krh@redhat.com> 0.12.0-2
- Add vte-0.12.0-real-transparency.patch for extra bling points.

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> 0.12.0-1
- Update to 0.12.0-1

* Fri Mar 10 2006 Matthias Clasen <mclasen@redhat.com> 0.11.21-1
- Update to 0.11.21

* Sun Feb 26 2006 Matthias Clasen <mclasen@redhat.com> 0.11.20-1
- Update to 0.11.20

* Sat Feb 25 2006 Matthias Clasen <mclasen@redhat.com> 0.11.19-1
- Update to 0.11.19
- Drop upstreamed patch

* Fri Feb 17 2006 Matthias Clasen <mclasen@redhat.com> 0.11.18-2
- Change Shift-Insert back to insert PRIMARY 

* Sat Feb 11 2006 Matthias Clasen <mclasen@redhat.com> 0.11.18-1
- Update to 0.11.18

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.11.17-1.fc5.1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.11.17-1.fc5.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> 0.11.17-1
- Update to 0.11.17

* Tue Jan 10 2006 Bill Nottingham <notting@redhat.com> 0.11.16-2
- prereq initscripts as it creates the utmp group

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 0.11.16-1
- Update to 0.11.16

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Sep  8 2005 Matthias Clasen <mclasen@redhat.com> 0.11.15-1
- update to 0.11.15

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> 0.11.14-3
- make python version automatic

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> 0.11.14-2
- remove huge and rarely needed devel docs
- remove .a because nobody should be using this

* Thu Aug  4 2005 Matthias Clasen <mclasen@redhat.com> 0.11.14-1
- New upstream version

* Mon May 23 2005 Bill Nottingham <notting@redhat.com> 0.11.13-2.fc4
- fix removal of static libs from python bindings

* Thu Apr 28 2005 Warren Togami <wtogami@redhat.com> 0.11.13-1
- 0.11.13, all patches are now upstream

* Fri Apr 22 2005 Warren Togami <wtogami@redhat.com> 0.11.12-2
- fix vte python module import (#151348)

* Mon Mar 07 2005 Warren Togami <wtogami@redhat.com> 0.11.12-1
- upgrade to 0.11.12
- remove upstreamed patches (0-2, 5-9)
- remove patch3, clashes and probably not needed anymore
- reverse patch4, because upstream merged this broken patch
- test Novell's excessive malloc for new terminals patch v3 
  (GNOME #160993)

* Wed Nov 17 2004 Ray Strode <rstrode@redhat.com> 0.11.11-15
- Remove workaround for bug 134300 and add 
  better patch from Nalin.

* Tue Nov 11 2004 Ray Strode <rstrode@redhat.com> 0.11.11-14
- Workaround bug 134300 by removing 
  the initiate-hilite-mouse-tracking capability from 
  vte.

* Tue Nov  9 2004 Ray Strode <rstrode@redhat.com> 0.11.11-13
- Don't copy blocks; use pointers to block array directly.
  (based on the debugging efforts of 
  Egmont Koblinger <egmong@uhulinux.hu>, bug 135537).

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 0.11.11-12
- rebuild against python 2.4

* Mon Nov  8 2004 Ray Strode <rstrode@redhat.com> 0.11.11-11
- Fix keypad keys when numlock is on in application mode
- (Patch from <jylefort@brutele.be>, bug 126110).

* Sun Oct 31 2004 Dan Williams <dcbw@redhat.com> 0.11.11-10
- Redraw background when unobscured visiblity event is received
- (workaround, patch from Jon Nettleton) #rh100420#
- Mad speed zoom zoom (patch from Soren Sandmann) #rh132770#

* Sun Oct 31 2004 Ray Strode <rstrode@redhat.com> 0.11.11-9
- Stop using patch previous patch for now until certain 
  unaddressed issues with it are resolved.

* Fri Oct 29 2004 Ray Strode <rstrode@redhat.com> 0.11.11-8
- Commit patch from Owen to avoid scrolling invalid regions.

* Thu Oct 28 2004 Ray Strode <rstrode@redhat.com> 0.11.11-7
- Add support for "scroll-up" and "scroll-down" control 
  sequences to make vte more xterm compatible (Patch
  from Nalin, #128375)

* Fri Oct 15 2004 Matthias Clasen <mclasen@redhat.com> 0.11.11-6
- Fix a crash with input methods.  (#131226)

* Thu Sep 16 2004 Ray Strode <rstrode@redhat.com> 0.11.11-5 
- Do bottom row snapping yet another way to fix scrolling
  artifacts (bug 131798)
- Add new debugging patch for keeping track of row numbers

* Thu Sep 09 2004 Ray Strode <rstrode@redhat.com> 0.11.11-4 
- Fix "scroll on output" option (bug 131755)

* Wed Sep 01 2004 Ray Strode <rstrode@redhat.com> 0.11.11-3 
- A more robust bottom row snapping fix.

* Tue Aug 31 2004 Warren Togami <wtogami@redhat.com> 0.11.11-2
- #111012 BuildReq gettext, ncurses-devel
- remove large and not useful doc

* Tue Aug 24 2004 Ray Strode <rstrode@redhat.com> 0.11.11-1 
- update to 0.11.11

* Tue Aug 24 2004 Ray Strode <rstrode@redhat.com> 0.11.10-8 
- Stick bottom row to bottom of terminal when resizing.
  (fixes #130204)

* Thu Jul 22 2004 Ray Strode <rstrode@redhat.com> 0.11.10-7 
- add ncurses-devel to devel package reqs

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Sep 16 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.10-4
- rebuild

* Mon Sep 15 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.10-3
- don't reset conversion states at end-of-line (GNOME #122156)

* Fri Sep 12 2003 Nalin Dahyabhai <nalin@redhat.com>
- draw the preedit string the way GTK+ wants us to draw it (#104039)

* Mon Jun 16 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.10-2
- rebuild

* Mon Jun 16 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.10-1
- fix vte_terminal_set_encoding() so that the Terminal/Character Coding
  menu works in gnome-terminal again
- fix display of the character under the cursor in cases where it's too wide

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun  2 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.9-2
- rebuild

* Mon Jun  2 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.9-1
- fix saving/restoring the cursor with DECSET/DECRST
- revert behavior wrt ambiguously-wide characters to be more like 0.10.x

* Thu May 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.8-1
- close some memory leaks
- fix conversions of NUL bytes (Ctrl-Space)

* Tue May 20 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.7-1
- make handling of 8-bit SS2 and SS3 coexist properly with UTF-8 and other
  encodings where valid text can't be mistaken for the control codes
- fix keypad page down in application keypad mode
- fix reference loop which prevented proper finalizing of the widget

* Tue May  6 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.6-1
- handle 8-bit SS2 and SS3
- share backgrounds between terminal instances

* Wed Apr 30 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.5-1
- pick up font settings from xrdb if GTK+ doesn't know anything
- support CP437 as a national replacement charset

* Thu Apr 24 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.4-1
- update transparent background faster when moving windows
- fix bold
- add an AtkComponent interface for accessibility

* Thu Apr 17 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.3-1
- rework support for national replacement charsets and iso2022

* Thu Apr 17 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.2-1
- selection tweaks and an openi18n fix

* Mon Apr 14 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.1-1
- drawing cleanups

* Wed Apr  9 2003 Nalin Dahyabhai <nalin@redhat.com>
- rework drawing with Xft2 to use font sets
- implement drawing with freetype using font sets

* Mon Feb 24 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.25-1
- incorporate fix for issues noted by H D Moore (CAN-2003-0070)

* Mon Feb 24 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.24-3
- home the cursor when we switch to the alternate screen
 
* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com> 0.10.24-2
- rebuilt
  
* Fri Feb 21 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.24-1
- be consistently wrong about the width of ACS characters (#84783)

* Fri Feb 21 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.23-1
- update to 0.10.23
- don't always perform character centering

* Thu Feb 20 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.22-3
- refix ctrl-[2-8] (#83563) to not break meta variants

* Thu Feb 20 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.22-2
- stop gratuitously resetting the IM (#81542)
- be more careful about assuming the IM exists when it might not

* Thu Feb 20 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.22-1
- be more careful about when we reset the IM (#81542)
- always perform character centering
- fix drawing of rows where the first exposed cell is the second half of a
  full-width character

* Wed Feb 19 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.21-1
- report accessible focus-changed events properly
- fix window_scroll optimization check (#83679)
- fix ctrl-[2-8] (#83563)
- grab focus on button 1 click (#84384)

* Fri Feb 14 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.20-1
- don't mix up maintainer mode with debugging mode
- coalesce data reads to spare the X server from too many small updates (#83472)
- fix backtab

* Thu Feb 13 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.19-1
- close descriptor leak
- skip over fragments correctly when retrieving text and drawing rows

* Tue Feb 11 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.18-1
- fix for uncertain finalize order between the terminal and its accessible peer
- always update the cursor position on accessibe-changed events so that the
  accessibility layer doesn't ask for text past the end of the buffer

* Tue Feb 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add symlink to shared lib

* Mon Feb  3 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.17-1
- draw 0x2592 natively

* Fri Jan 31 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.16-1
- fix "selection always extends by default" bug

* Thu Jan 30 2003 Nalin Dahyabhai <nalin@redhat.com> 0.11.0-1
- fork stable branch

* Wed Jan 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.15-1
- make mouse modes mutually-exclusive
- update background immediately on realize
- fix compile error on older versions of gcc
- fix cursor hiding

* Wed Jan 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.14-1
- fix assorted mouse event bugs

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.10.12-2
- rebuilt
 
* Tue Jan 21 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.13-1
- use less memory when setting up pseudo-transparent backgrounds

* Mon Jan 20 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.12-1
- fix a few accessibility bugs
- fix colors 90-97,100-107 not bright (GNOME #103713)

* Fri Jan 17 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.11-1
- fix overzealous clearing when drawing the cursor

* Tue Jan 14 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.10-1
- add text that scrolls off of a restricted scrolling area which goes to the
  top of the visible screen to the scrollback buffer (#75900)

* Mon Jan 13 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.9-1
- fix scrolling through the accessibility layer
- stop heeding NumLock when mapping cursor keys
- steal keypress events from the input method if Meta modifier is in effect

* Mon Jan  6 2003 Nalin Dahyabhai <nalin@redhat.com> 0.10.8-1
- report changes to the accessibility layer when text is removed or moved
  around, still needs work
- don't use XftNameUnparse, it might not always be there

* Fri Dec 13 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.7-2
- rebuild

* Wed Dec 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.7-1
- distinguish line-drawing character set code points from the same code points
  received from the local encoding

* Tue Dec 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.6-1
- handle ambiguous-width line-drawing characters

* Tue Dec 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.5-3
- rebuild

* Mon Dec  9 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.5-2
- work around AM_PATH_PYTHON not being multilib-aware

* Tue Dec  3 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.5-1
- cleaned up the keyboard

* Mon Nov 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.4-1
- make selection wrap like XTerm

* Thu Nov  7 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.3-1
- get selection sorted out, really this time

* Tue Nov  5 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.2-1
- get selection sorted out

* Tue Oct 29 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10.1-1
- add the ability to remove matching patterns

* Thu Oct 24 2002 Nalin Dahyabhai <nalin@redhat.com> 0.10-1
- allow setting the working directory (#76529)

* Thu Oct 17 2002 Nalin Dahyabhai <nalin@redhat.com> 0.9.2-1
- fix the crash-on-resize bug (#75871)
- add bold
- implement sun/hp/legacy function key modes
- recognize cs with no parameters
- fix ring buffer manipulation bugs
- cut down on overly-frequent invalidates

* Wed Sep 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.9.1-1
- refresh gnome-pty-helper from libzvt

* Wed Sep 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.9.0-1
- build fixes from Jacob Berkman
- warning fixes from Brian Cameron
- gnome-pty-helper integration

* Fri Sep  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.20-1
- build fixups from Jacob Berkman
- move the python module into the gtk-2.0 subdirectory, from James Henstridge

* Thu Sep  5 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.19-1
- possible fix for focusing bugs

* Thu Sep  5 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.18-1
- fix for worst-case when stripping termcap entries from Brian Cameron
- add docs

* Tue Sep  3 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.17-1
- track Xft color deallocation to prevent freeing of colors we don't own

* Tue Sep  3 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.16-1
- handle color allocation failures better

* Mon Sep  2 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.15-1
- cleanups

* Fri Aug 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.14-1
- get smarter about adjusting our adjustments (#73091)

* Fri Aug 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.13-1
- restore the IM status window by restoring our own focus-in/focus-out
  handlers (#72946)

* Fri Aug 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.12-1
- cleanups

* Thu Aug 29 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.11-1
- clean up autoscroll (#70481)
- add Korean text examples to docs

* Tue Aug 27 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.10-1
- autoscroll (#70481)
- only perform cr-lf substitutions when pasting (#72639)
- bind GDK_ISO_Left_Tab to "kB" (part of #70340)

* Tue Aug 27 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.9-1
- handle forward scrolling again (#73409)

* Tue Aug 27 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.8-1
- fix crashes on resize

* Mon Aug 26 2002 Nalin Dahyabhai <nalin@redhat.com>
- fix missing spaces on full lines

* Mon Aug 26 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.7-1
- fix deadlock when substitutions fail

* Mon Aug 26 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.6-1
- one-liner segfault bug fix

* Sun Aug 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.5-1
- fix reverse video mode, which broke during the rendering rewrite

* Fri Aug 23 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.4-1
- prevent up/UP/DO from scrolling
- bind shift+insert to "paste PRIMARY", per xterm/kterm/hanterm

* Thu Aug 22 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.3-1
- track changes to the style's font
- always open fonts right away so that the metric information is correct
- make audible and visual bell independent options

* Wed Aug 21 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.2-1
- don't perform text substitution on text that is part of a control sequence

* Tue Aug 20 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.1-1
- dispose of the updated iso2022 context properly when processing incoming text

* Tue Aug 20 2002 Nalin Dahyabhai <nalin@redhat.com> 0.8.0-1
- rework font handling to use just-in-time loading
- handle iso-2022 escape sequences, perhaps as much as they might make sense
  in a Unicode environment

* Wed Aug 14 2002 Nalin Dahyabhai <nalin@redhat.com> 0.7.4-1
- handle massive amounts of invalid data better (the /dev/urandom case)
- munged up patch from Owen to fix language matching
- fix initialization of new rows when deleting lines

* Mon Aug 12 2002 Nalin Dahyabhai <nalin@redhat.com> 0.7.3-1
- more fixes for behavior when not realized
- require bitmap-fonts
- escape a control sequence properly

* Thu Aug  8 2002 Nalin Dahyabhai <nalin@redhat.com> 0.7.2-1
- fix cursor over reversed text
- fix character positioning in Xft1
- add border padding
- fix lack of shift-in when resetting

* Tue Aug  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.7.1-1
- rework rendering with Pango
- special-case monospaced Xft1 rendering, hopefully making it faster
- modify pasting to use carriage returns instead of linefeeds

* Thu Aug  1 2002 Nalin Dahyabhai <nalin@redhat.com> 0.7.0-1
- rework drawing to minimize round trips to the server

* Tue Jul 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.6.0-1
- rework parsing to use tables instead of tries
- implement more xterm-specific behaviors

* Thu Jul 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.5.4-1
- fix default PTY size bug

* Wed Jul 24 2002 Nalin Dahyabhai <nalin@redhat.com> 0.5.3-1
- open PTYs with the proper size (#69606)

* Tue Jul 23 2002 Nalin Dahyabhai <nalin@redhat.com> 0.5.2-1
- fix imbalanced realize/unrealize routines causing crashes (#69605)

* Thu Jul 18 2002 Nalin Dahyabhai <nalin@redhat.com> 0.5.1-1
- fix a couple of scrolling artifacts

* Thu Jul 18 2002 Nalin Dahyabhai <nalin@redhat.com> 0.5.0-1
- use gunichars internally
- scroll regions more effectively
- implement part of set-mode/reset-mode (maybe fixes #69143)
- fix corner case in dingus hiliting (#67930, really this time)

* Thu Jul 18 2002 Jeremy Katz <katzj@redhat.com> 0.4.9-3
- free trip through the build system

* Tue Jul 16 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.9-2
- build in different environment

* Tue Jul 16 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.9-1
- check for iconv failures properly and report them more aggressively
- guess at a proper default bold color (#68965)

* Mon Jul 15 2002 Nalin Dahyabhai <nalin@redhat.com>
- cosmetic fixes

* Sat Jul 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- fix segfaulting during dingus highlighting when the buffer contains non-ASCII
  characters (#67930)

* Fri Jul 12 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.8-1
- implement BCE (#68414)
- bind F13-F35 per termcap

* Thu Jul 11 2002 Nalin Dahyabhai <nalin@redhat.com>
- rework default color selection
- provide a means for apps to just set the foreground/background text colors
- don't scroll-on-keystroke when it's just alt, hyper, meta, or super (#68986)

* Tue Jul  2 2002 Nalin Dahyabhai <nalin@redhat.com>
- allow shift+click to extend the selection (re: gnome 86246)

* Mon Jul  1 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.7-1
- recover from encoding errors more gracefully

* Mon Jul  1 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.6-1
- draw unicode line-drawing characters natively

* Tue Jun 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.5-1
- don't append spaces to multicolumn characters when reading the screen's
  contents (part of #67379)
- fix overexpose of neighboring cells (part of #67379)
- prevent backscroll on the alternate screen for consistency with xterm
- bind F10 to "k;", not "k0" (#67133)

* Tue Jun 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.4-1
- clear alternate buffer when switching screens (#67094)
- fix setting of titles, but crept in when cleaning up GIConv usage (#67236)

* Tue Jun 18 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.3-1
- correct referencing/dereferencing of I/O channels (#66248)
- correct package description to not mention the sample app which is no longer
  included

* Tue Jun 18 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.2-1
- fix "cursor mistakenly hidden when app exits" by making cursor visibility
  a widget-wide (as opposed to per-screen) setting

* Tue Jun 18 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.1-1
- fix use of alternate buffer in xterm emulation mode

* Fri Jun 14 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.0-1
- add a means for apps to add environment variables

* Fri Jun 14 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.30-1
- package up the python module

* Mon Jun 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.29-1
- compute padding correctly

* Mon Jun 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.28-1
- finish merging otaylor's Xft2 patch

* Mon Jun 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.27-1
- rework accessibility

* Thu Jun  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.26-1
- don't package up the test program
- emit "child-exited" signals properly
- try to allow building with either pangoxft-with-Xft1 or pangoxft-with-Xft2

* Wed Jun  5 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.25-1
- compute font widths better

* Mon Jun  3 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.24-1
- tweak handling of invalid sequences again

* Fri May 31 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.23-1
- switch to g_convert (again?)
- fix use of core fonts

* Tue May 28 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.22-1
- plug some memory leaks

* Tue May 28 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.21-1
- fix matching, fix async background updates

* Fri May 24 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.20-1
- fixes from notting and otaylor

* Tue May 21 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.19-1
- fixes from andersca and Hidetoshi Tajima

* Thu May 16 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.18-1
- finish implementing matching

* Thu May 16 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.17-1
- tweak finding of selected text

* Wed May 15 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.16-1
- hook up Insert->kI
- convert scroll events to button 4/5 if an app wants mouse events
- don't send drag events when apps only want click events
- fix selection crashbug

* Tue May 14 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.15-1
- fix ce, implement save/restore mode

* Tue May 14 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.14-1
- don't draw nul chars

* Mon May 13 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.13-1
- fix insert mode, implement visual bells

* Thu May  9 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.12-1
- iconv and remapping from otaylor
- implement custom tabstopping

* Wed May  8 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.11-1
- add mouse drag event handling

* Mon May  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.10-1
- do mouse autohide and cursor switching

* Mon May  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.9-1
- start handling mouse events

* Mon May  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.8-1
- handle window manipulation sequences

* Fri May  3 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.7-1
- discard invalid control sequences
- recognize designate-??-character-set correctly

* Thu May  2 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.6-1
- add a couple of sequence handlers, fix a couple of accessibility crashbugs

* Thu May  2 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.5-1
- fix cap parsing error and "handle" long invalid multibyte sequences better

* Thu May  2 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.4-1
- try to speed up sequence recognition a bit
- disable some window_scroll speedups that appear to cause flickering

* Wed May  1 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.2-1
- include a small default termcap for systems without termcap files

* Tue Apr 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.1-1
- disconnect from the configure_toplevel signal at finalize-time

* Tue Apr 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3-1
- add an accessiblity object

* Mon Apr 29 2002 Nalin Dahyabhai <nalin@redhat.com> 0.2.3-1
- fix color resetting
- fix idle handlers not being disconnected

* Mon Apr 29 2002 Nalin Dahyabhai <nalin@redhat.com> 0.2.2-1
- bug fixes

* Thu Apr 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.1-1
- finish initial packaging, start the changelog
