Name:		nip2
Version:	8.7.1
Release:	16%{?dist}
Summary:	Interactive tool for working with large images

License:	GPLv2+
URL:		https://libvips.github.io/libvips/
Source0:	https://github.com/libvips/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# avoid using bool keyword
Patch0:	nip2-8.7.1-keyword-bool.patch

BuildRequires: make
BuildRequires:	pkgconfig(vips)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(libgvc)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	gcc
BuildRequires:	shared-mime-info gnome-icon-theme-devel
BuildRequires:	flex bison intltool gettext
BuildRequires:	desktop-file-utils xdg-utils
BuildRequires:	libappstream-glib


# description taken from Debian package
%description
nip2 is a graphical front end to the VIPS package.
With nip2, rather than directly editing images, you build
relationships between objects in a spreadsheet-like fashion. When you
make a change somewhere, nip2 recalculates the objects affected by
that change. Since it is demand-driven this update is very fast, even
for very, very large images. nip2 is very good at creating pipelines
of image manipulation operations. It is not very good for image
editing tasks like touching up photographs. For that, a tool like the
GIMP should be used instead.


%prep
%setup -q
%patch0 -p1 -b .bool


%build
%configure --disable-update-desktop
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# AppStream spec changed its install directory
mv $RPM_BUILD_ROOT%{_datadir}/appdata $RPM_BUILD_ROOT%{_datadir}/metainfo

# delete doc (we will get it later)
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/nip2

# locale stuff
%find_lang nip2

# icon
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
cp -a share/nip2/data/vips-128.png	\
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/nip2.png


%check
# metainfo
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/nip2.appdata.xml

# desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/nip2.desktop

%files -f nip2.lang
%doc doc/html doc/pdf AUTHORS ChangeLog NEWS THANKS TODO
%license COPYING
%{_bindir}/nip2
%{_datadir}/nip2
%{_mandir}/man1/nip2.1.gz
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/nip2.appdata.xml
%{_datadir}/applications/nip2.desktop
%{_datadir}/mime/packages/nip2.xml


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.7.1-13
- Avoid using bool keyword

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.7.1-12
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr  8 2020 Adam Goode <adam@spicenitz.org> - 8.7.1-6
- Remove goffice requirement, the package was retired

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 8.7.1-4
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.1-1
- New release

* Fri Jan 11 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.0-2
- Fix segfault at startup

* Thu Oct 04 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.0-1
- New release
- Update package URLs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.6.0-2
- Remove obsolete scriptlets

* Sun Dec 17 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.0-1
- New release

* Thu Nov 23 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.1-4
- Move appdata to %%{_datadir}/metainfo per policy

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.1-2
- Rebuild for gsl 2.4

* Sat Jun 17 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.1-1
- New release
- Update project URLs
- Drop Group tag

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.4.0-1
- New release
- Drop mimeinfo and desktop-database scriptlets per policy change
- Redirect icon post scriptlet to /dev/null per policy

* Sat May 21 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.3.0-1
- New release

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 8.2-4
- Rebuild for gsl 2.1

* Sun Feb 21 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.2-3
- BuildRequire gcc per new policy

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.2-1
- New release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Benjamin Gilbert <bgilbert@backtick.net> - 8.0-1
- New release
- Move license file to %%license

* Tue Dec 30 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.42.1-1
- New release

* Sun Dec 28 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.42.0-1
- New release
- Re-enable graphviz
- Minor specfile cleanups

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> - 7.40.4-2
- rebuild (vips)
- fix icon/mime scriptlets
- validate appdata

* Thu Sep 25 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.4-1
- New release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.40.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Richard Hughes <richard@hughsie.com> - 7.40.3-1
- New release

* Tue Jul 08 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.2-1
- New release

* Sun Jun 29 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.1-1
- New release
- Add libgsf dependency
- Use macros for package version

* Sun Jun 22 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.38.3-1
- New release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.38.1-2
- Rebuild for ImageMagick

* Tue Jan 21 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.38.1-1
- New release

* Thu Jan 09 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.5-3
- Rebuild for cfitsio

* Thu Jan 02 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.5-2
- Rebuild for libwebp

* Mon Dec 23 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.5-1
- New release

* Thu Nov 28 2013 Rex Dieter <rdieter@fedoraproject.org> 7.36.4-2
- rebuild (openexr)

* Wed Nov 13 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.4-1
- New release

* Sat Oct 05 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.0-1
- New release

* Tue Sep 10 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.34.1-4
- Rebuild for ilmbase 2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.34.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.34.1-2
- Update for UnversionedDocdirs

* Tue Jul 16 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.34.1-1
- New release

* Sat Jun 29 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.34.0-1
- New release

* Fri Jun 28 2013 Kalev Lember <kalevlember@gmail.com> - 7.32.1-3
- Adapt for gnome-icon-theme packaging changes

* Fri May 17 2013 Orion Poplawski <orion@cora.nwra.com> - 7.32.1-2
- Rebuild for hdf5 1.8.11

* Thu Mar 21 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.1-1
- New release

* Thu Mar 21 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.0-4
- Rebuild for cfitsio

* Sun Mar 17 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.0-3
- Rebuild for ImageMagick

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> - 7.32.0-2
- rebuild (OpenEXR)

* Thu Mar 07 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.0-1
- New release
- Remove stray empty file in examples directory

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.30.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 7.30.1-3
- rebuild due to "jpeg8-ABI" feature drop

* Thu Jan 17 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.30.1-2
- Disable workspace dependency graphs pending graphviz 2.30 support

* Sun Oct 21 2012 Benjamin Gilbert <bgilbert@backtick.net> - 7.30.1-1
- New release
- Switch back to goffice 0.8 for gtk2
- Fix build with flex 2.5.36
- Disable bundled GtkSheet
- Minor specfile cleanups

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.28.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Adam Jackson <ajax@redhat.com> 7.28.1-2
- Rebuild for new libmatio

* Fri Apr 13 2012 Tom Callaway <spot@fedoraproject.org> - 7.28.1-1
- update to 7.28.1

* Mon Jan 16 2012 Adam Goode <adam@spicenitz.org> - 7.26.4-1
- New upstream release (better error messages for print-main)
- Fix goffice requirement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.26.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 7.26.3-2
- Rebuild for new libpng

* Sat Sep  3 2011 Adam Goode <adam@spicenitz.org> - 7.26.3-1
- New upstream release
    + New operations
    + Faster!

* Fri Aug 12 2011 Adam Goode <adam@spicenitz.org> - 7.24.2-1
- New upstream release
    + Workspace as Graph mode
    + Better nibs in paintbox

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 7.22.2-3
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.22.2-2
- rebuild for new ImageMagick

* Fri Aug  6 2010 Adam Goode <adam@spicenitz.org> - 7.22.2-1
- New upstream release
    + New image repaint system
    + Many improvements from new VIPS
- Use upstream desktop file

* Mon Mar  8 2010 Adam Goode <adam@spicenitz.org> - 7.20.7-4
- Rebuild for imagemagick soname change
- Remove some old RPM stuff

* Sat Feb 27 2010 Adam Goode <adam@spicenitz.org> - 7.20.7-3
- Rebuild for goffice soname change

* Thu Jan  7 2010 Adam Goode <adam@spicenitz.org> - 7.20.7-2
- Enable goffice for charts
- Update desktop file

* Wed Jan  6 2010 Adam Goode <adam@spicenitz.org> - 7.20.7-1
- New upstream release
    + Faster image painting
    + Better progress feedback
    + GOffice now used to draw charts
    + Support for newer GTK+ features

* Fri Sep  4 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 7.18.2-1
- Fix FTBFS: update to 7.18.2, added nip2-7.18.2-gtk.patch to build with gtk >= 2.17

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.16.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Adam Goode <adam@spicenitz.org> - 7.16.4-3
- Rebuild for ImageMagick soname change

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Adam Goode <adam@spicenitz.org> - 7.16.4-1
- New release
- Drop upstreamed flex patch

* Sat Dec 27 2008 Adam Goode <adam@spicenitz.org> - 7.16.3-3
- Fix build problem related to flex

* Mon Dec 22 2008 Adam Goode <adam@spicenitz.org> - 7.16.3-2
- Add gsl-devel and xdg-utils to build requires

* Sun Dec 21 2008 Adam Goode <adam@spicenitz.org> - 7.16.3-1
- New release
- Update description

* Sat Aug 30 2008 Adam Goode <adam@spicenitz.org> - 7.14.5-1
- New release
- RPM 4.6 fix for patch tag

* Sat Jun 21 2008 Adam Goode <adam@spicenitz.org> - 7.14.4-1
- New release

* Sat Mar 15 2008 Adam Goode <adam@spicenitz.org> - 7.14.1-1
- New release

* Mon Mar 10 2008 Adam Goode <adam@spicenitz.org> - 7.14.0-1
- New release

* Sat Feb  9 2008 Adam Goode <adam@spicenitz.org> - 7.12.5-4
- GCC 4.3 mass rebuild

* Wed Dec  5 2007 Adam Goode <adam@spicenitz.org> - 7.12.5-3
- Fix desktop file validation

* Tue Oct 16 2007 Adam Goode <adam@spicenitz.org> - 7.12.5-2
- Rebuild for OpenEXR soname change

* Fri Sep 21 2007 Adam Goode <adam@spicenitz.org> - 7.12.5-1
- New upstream release

* Thu Aug 16 2007 Adam Goode <adam@spicenitz.org> - 7.12.4-1
- New upstream release
- Update License tag

* Wed Jul 25 2007 Adam Goode <adam@spicenitz.org> - 7.12.2-1
- New stable release 7.12

* Sat May  5 2007 Adam Goode <adam@spicenitz.org> - 7.12.0-1
- New upstream release
- Update desktop file
- Remove X-Fedora category

* Thu Aug 31 2006 Adam Goode <adam@spicenitz.org> - 7.10.21-1
- New upstream release

* Sun Aug 13 2006 Adam Goode <adam@spicenitz.org> - 7.10.20-2
- Fix location of documentation in program so help works
- Semicolon-terminate Category entry in desktop file

* Sat Jul 22 2006 Adam Goode <adam@spicenitz.org> - 7.10.20-1
- New upstream release
- Updated for FC5

* Thu Jan 30 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.6-1
- first stab at an rpm package for nip
