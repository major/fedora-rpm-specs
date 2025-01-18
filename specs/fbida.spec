Summary:        FrameBuffer Imageviewer
Name:           fbida
Version:        2.14
Release:        21%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.kraxel.org/blog/linux/fbida/
Source:         https://www.kraxel.org/releases/fbida/fbida-%{version}.tar.gz
BuildRequires:  libexif-devel fontconfig-devel libjpeg-devel
BuildRequires:  libpng-devel libtiff-devel pkgconfig
BuildRequires:  giflib-devel curl-devel
BuildRequires:  libXpm-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  motif-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  libepoxy-devel
BuildRequires:  pixman-devel
BuildRequires:  freetype-devel
BuildRequires:  libdrm-devel
BuildRequires:  lirc-devel
BuildRequires:  libwebp-devel
BuildRequires:  perl-generators
BuildRequires:  gcc
BuildRequires: make
Requires:       ImageMagick dejavu-sans-mono-fonts
Patch0:         fbida.gcc10.patch

%description
fbi displays the specified file(s) on the linux console using the
framebuffer device. PhotoCD, jpeg, ppm, gif, tiff, xwd, bmp and png
are supported directly. For other formats fbi tries to use
ImageMagick's convert.

%package fbgs
Summary: Framebuffer Postscript Viewer
Requires: ghostscript fbida

%description fbgs
A wrapper script for viewing ps/pdf files on the framebuffer console using fbi

%package fbpdf
Summary: Framebuffer PDF Viewer

%description fbpdf
fbpdf displays PDF files on the framebuffer device.

%package ida
Summary: Motif based Imageviewer

%description ida
This is a X11 application (Motif based) for viewing images. Some basic
editing functions are available too.

%prep
%setup -q
%patch -P0 -p1

%build
LIB=%{_lib} prefix=%{_prefix} CFLAGS=$RPM_OPT_FLAGS %{__make} %{?_smp_mflags} all verbose=1

%install
cd man
for man in fbi exiftran fbgs ida; do
    iconv -t UTF-8 -f ISO-8859-1 $man.1 > $man.new
    %{__mv} $man.new fbi.1
done
cd ..
lib=%{_lib} prefix=%{_prefix} %{__make} DESTDIR=%{buildroot} STRIP= install

%files
%license COPYING
%doc Changes COPYING README TODO
%doc %{_mandir}/man1/fbi*
%doc %{_mandir}/man1/exiftran*
%{_bindir}/fbi
%{_bindir}/exiftran

%files fbgs
%license COPYING
%doc %{_mandir}/man1/fbgs*
%{_bindir}/fbgs

%files fbpdf
%license COPYING
%{_bindir}/fbpdf

%files ida
%license COPYING
%doc %{_mandir}/man1/ida*
%{_bindir}/ida
%{_datadir}/X11/app-defaults/Ida

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.14-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 2.14-8
- Rebuild for poppler-0.84.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Adrian Reber <adrian@lisas.de> - 2.14-5
- Added BR: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 2.14-3
- Rebuild (giflib)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Adrian Reber <adrian@lisas.de> - 2.14-1
- updated to 2.14

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.09-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.09-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Adrian Reber <adrian@lisas.de> - 2.09-1
- updated to 2.09

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.07-9
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Matěj Cepl <mcepl@redhat.com> - 2.07-6
- actually ida* stuff doesn't get build without Motif

* Thu Feb 26 2009 Matěj Cepl <mcepl@redhat.com> - 2.07-5
- Fix dependencies on fonts (bug# 480450) -- I made a typo in
  BuildRequires.
- Fix %%files (missing *ida* stuff).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Adrian Reber <adrian@lisas.de> - 2.07-3
- removed bitstream-vera dependency to fix (#473559)
  "Replace bitstream-vera dependencies with dejavu dependencies"
- changed BR libungif-devel to giflib-devel

* Fri Jul 04 2008 Adrian Reber <adrian@lisas.de> - 2.07-2
- applied patch from Ville Skyttä to fix
  "fbida: empty debuginfo package" (#453998)

* Mon Jun 09 2008 Adrian Reber <adrian@lisas.de> - 2.07-1
- updated to 2.07
- fixes "The fbi command aborts with a stack trace" (#448126)

* Fri Feb 15 2008 Adrian Reber <adrian@lisas.de> - 2.06-5
- rebuilt
- added patch to fix build failure on ppc/ppc64

* Sat Aug 25 2007 Adrian Reber <adrian@lisas.de> - 2.06-4
- rebuilt

* Tue Oct 31 2006 Adrian Reber <adrian@lisas.de> - 2.06-3
- rebuilt for new curl

* Fri Sep 29 2006 Adrian Reber <adrian@lisas.de> - 2.06-2
- obsoleted fbida-ida subpackage (#208457)

* Wed Aug 30 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 2.06-1
- get rid of ida, we can't build a working version without openmotif

* Fri Jul 28 2006 Adrian Reber <adrian@lisas.de> - 2.05-1
- updated to 2.05
- dropped fbida.CVE-2006-1695.patch (now included)
- dropped fix for #200321 (included in new release)
- added two patches from debian to fix typos in manpages

* Thu Jul 27 2006 Adrian Reber <adrian@lisas.de> - 2.03-12
- security fix for #200321

* Mon Apr 24 2006 Adrian Reber <adrian@lisas.de> - 2.03-11
- security fix for #189721

* Mon Feb 13 2006 Adrian Reber <adrian@lisas.de> - 2.03-10
- rebuilt

* Wed Jan 18 2006 Adrian Reber <adrian@lisas.de> - 2.03-9
- this should finally work; also on x86_64

* Wed Jan 18 2006 Adrian Reber <adrian@lisas.de> - 2.03-8
- rebuilt

* Wed Jan 18 2006 Adrian Reber <adrian@lisas.de> - 2.03-7
- moved file Ida to %%{_datadir}/X11/app-defaults

* Thu Nov 24 2005 Adrian Reber <adrian@lisas.de> - 2.03-6
- updated for modular xorg-x11

* Tue May 10 2005 Adrian Reber <adrian@lisas.de> - 2.03-5
- fix debuginfo subpackage creation

* Mon Apr 04 2005 Adrian Reber <adrian@lisas.de> - 2.03-4
- rebuild for new libexif

* Mon Feb 21 2005 Thorsten Leemhuis <fedora at leemhuis dot info> - 2.03-3
- Fix typo; must be LIB=%%{_lib}; really fixes x86_64

* Sat Feb 12 2005 Thorsten Leemhuis <fedora at leemhuis dot info> - 2.03-2
- lib=%%{_lib} in make call; fixes x86_64

* Fri Feb 11 2005 Adrian Reber <adrian@lisas.de> - 2.03-1
- updated to 2.03
- created subpackages for ida and fbgs

* Sun Nov 28 2004 Adrian Reber <adrian@lisas.de> - 2.02-1
- updated to 2.02
- converted manpages to UTF-8

* Sun Nov 28 2004 Adrian Reber <adrian@lisas.de> - 2.01-1
- initial package
