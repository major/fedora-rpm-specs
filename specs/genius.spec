Name:           genius
Version:        1.0.25
Release:        13%{?dist}
Summary:        An arbitrary precision integer and multiple precision floatingpoint calculator

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.jirka.org/genius.html
Source0:        https://download.gnome.org/sources/genius/1.0/genius-%{version}.tar.xz

BuildRequires:  amtk-devel
BuildRequires:  gcc
BuildRequires:  vte291-devel
BuildRequires:  readline-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  popt
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires: make

%description
Genius is a calculator program similar in some aspects to BC, Matlab
or Maple. GEL is the name of its extension language, in fact, a large
part of the standard genius functions are written in GEL itself.

%package devel
Summary:        Development files for Genius
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for Genius.

%package -n gnome-genius
Summary:        GNOME frontend for Genius
Requires:       %{name} = %{version}-%{release}

%description -n gnome-genius
GNOME frontend for Genius.

%prep
%setup -q
#sed -i "s|Mime-Type|MimeType|" src/gnome-genius.desktop*
find -name \*.c | xargs chmod 0644

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/genius/plugins/test.plugin
rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime/{subclasses,text,XMLnamespaces,aliases,globs,magic,mime.cache,icons,generic-icons,treemagic,types,globs2,version}
rm -rf $RPM_BUILD_ROOT/var
desktop-file-install \
    --add-category Utility \
    --remove-category Office \
    --remove-category Scientific \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --delete-original \
    $RPM_BUILD_ROOT%{_datadir}/applications/gnome-genius.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%exclude %{_datadir}/genius/gtksourceview
%{_bindir}/genius
%{_datadir}/genius

%files devel
%{_includedir}/genius

%files -n gnome-genius
%{_bindir}/gnome-genius
%{_libexecdir}/*
%{_datadir}/genius/gtksourceview
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/gnome-genius.svg
%{_datadir}/mime/packages/*
%{_datadir}/applications/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.25-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Kalev Lember <klember@redhat.com> - 1.0.25-1
- Update to 1.0.25

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <Loganjerry@gmail.com> - 1.0.24-6
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.24-4
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Tom Callaway <spot@fedoraproject.org> - 1.0.24-1
- update to 1.0.24

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.23-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.23-1
- update to 1.0.23

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.22-3
- Rebuild for readline 7.x

* Wed Jan 04 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.22-2
- move gtksourceview files to gnome-genius (bz1401890)

* Tue Jan 03 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.22-1
- update to 1.0.22

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 30 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.20-3
- Switch to gtksourceview2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Tom Callaway <spot@fedoraproject.org> - 1.0.20-1
- update to 1.0.20

* Wed Sep 24 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.19-1
- update to 1.0.19

* Tue Aug 26 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.18-1
- update to 1.0.18

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.17-1
- update to 1.0.17

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.16-3
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan  3 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.16-1
- update to 1.0.16

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.14-1
- update to 1.0.14

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.12-3.2
- Rebuild for new libpng

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.0.12-2.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 1.0.12-2.1
- rebuild with new gmp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb  5 2011 Gérard Milmeister <gemi@bluewin.ch> - 1.0.12-1
- new release 1.0.12

* Sat Aug  8 2009 Gerard Milmeister <gemi@bluewin.ch> - 1.0.7-1
- new release 1.0.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6-1
- new release 1.0.6

* Sat Sep  6 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.3-1
- new release 1.0.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-3
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.2-2
- remove _smp_mflags

* Sun Jan 27 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.2-1
- new release 1.0.2

* Wed Nov  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.0-2
- added buildreq mpfr-devel

* Wed Oct 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.0-1
- new release 1.0.0

* Sun Feb 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.7.7-2
- rebuild to use ncurses

* Fri Feb  2 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.7.7-1
- new version 0.7.7

* Wed Oct 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.7.6.1-3
- Fixed Req and permissions

* Mon Oct 16 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.7.6.1-2
- Fixed BR

* Sun Oct 15 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.7.6.1-1
- first Fedora release

