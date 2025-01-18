Name:           foobillard
Version:        3.0a
Release:        51%{?dist}

Summary:        OpenGL billard game

License:        GPL-2.0-only
URL:            http://foobillard.sunsite.dk/
# Based on http://foobillard.sunsite.dk/dnl/foobillard-3.0a.tar.gz
Source0:        foobillard-3.0a-hobbled.tar.bz2
Source1:        foobillard.desktop
Source2:        hobble-foobillard.sh
Patch0:         foobillard-3.0a-nonv.patch
Patch1:         foobillard-3.0a-no-fonts.patch
Patch2:		foobillard-3.0a-clothtex.patch
Patch3:         foobillard-configure-c99.patch
Patch4:         foobillard-c99.patch
Patch5:         pointer-types.patch
Requires:       dejavu-sans-fonts
BuildRequires:  gcc
BuildRequires:  SDL-devel ImageMagick alsa-lib-devel
BuildRequires:  freetype-devel libpng-devel perl-interpreter zlib-devel freeglut-devel
BuildRequires:  libGL-devel libGLU-devel libX11-devel libXaw-devel libXi-devel
BuildRequires:  make

%description
FooBillard is an attempt to create a free OpenGL-billard for Linux.
FooBillard is still under development but the main physics is implemented.


%prep
%setup -q -n foobillard-3.0a
%patch -P 0 -p1
%patch -P 1 -p1 -b .no-fonts
%patch -P 2 -p0 -b .clothtex
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p0

%build
iconv -f iso-8859-1 -t utf-8 < ChangeLog > _
mv _ ChangeLog
./configure --prefix=%{_prefix} --disable-nvidia --enable-SDL CFLAGS="${RPM_OPT_FLAGS} -DUSE_SOUND" LDFLAGS="${RPM_LD_FLAGS}"
make %{?_smp_mflags}
convert -resize 48x48 -background transparent -gravity center -extent 48x48 data/foobillard.png foobillard.png
convert -resize 256x256 -background transparent -gravity center -extent 256x256 data/foobillard.png foobillard-256x256.png


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -pm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/applications/foobillard.desktop
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -pm 644 foobillard.6 $RPM_BUILD_ROOT%{_mandir}/man6
install -D -p -m 644 foobillard.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/foobillard.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 foobillard.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 foobillard-256x256.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps



%files
%doc AUTHORS COPYING ChangeLog README TODO
%doc foobillardrc.example
%{_bindir}/foobillard
%{_datadir}/applications/foobillard.desktop
%{_datadir}/foobillard
%{_datadir}/pixmaps/foobillard.png
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_mandir}/man6/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.0a-49
- Patch for stricter flags

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0a-45
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Florian Weimer <fweimer@redhat.com> - 3.0a-43
- Port to C99 (#2155183)

* Fri Dec 09 2022 Kalev Lember <klember@redhat.com> - 3.0a-42
- Make sure the installed icon is square
- Install an additional 256x256 px sized icon

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Kalev Lember <klember@redhat.com> - 3.0a-38
- Honor LDFLAGS from the build system

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0a-35
- Update dejavu font paths.

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0a-34
- Configure macro results in freeze in f32+

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0a-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 3.0a-20
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Jon Ciesla <limburgher@gmail.com> - 3.0a-18
- Build with SDL to fix sound, BZ 801588.

* Wed Mar 07 2012 Jon Ciesla <limburgher@gmail.com> - 3.0a-17
- Patch to fix cloth texture, BZ 709202.
- Build with glut.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Miloslav Trmač <mitr@redhat.com> - 3.0a-15
- Add dist tag
- Rebuild with newer libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 06 2009 Jesse Keating <jkeating@redhat.com> - 3.0a-12
- Correct the fonts requires due to package name change

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec  6 2008 Miloslav Trmač <mitr@volny.cz> - 3.0a-10
- Add SportsGame category to foobillard.spec
  Resolves: #465700

* Thu Dec  4 2008 Miloslav Trmač <mitr@volny.cz> - 3.0a-9
- Use a more specific dejavu-fonts requirement
  Resolves: #473554

* Mon Sep 15 2008 Miloslav Trmač <mitr@volny.cz> - 3.0a-8
- Add missing Requires: dejavu-fonts
  Resolves: #462168

* Sat Jul 19 2008 Miloslav Trmač <mitr@volny.cz> - 3.0a-7
- Don't ship the non-free fonts
- Update License:
- Fix foobillard.desktop
- Convert ChangeLog to UTF-8
- Don't ship empty NEWS

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0a-6
- Autorebuild for GCC 4.3

* Wed Sep 13 2006 Miloslav Trmac <mitr@redhat.com> - 3.0a-5
- Rebuild for Fedora Extras 6

* Mon Feb 20 2006 Miloslav Trmac <mitr@volny.cz> - 3.0a-4
- Rebuild for Fedora Extras 5

* Tue Jan 31 2006 Miloslav Trmac <mitr@volny.cz> - 3.0a-3
- Update BuildRequires for modular X

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:3.0-a.1
- Added BuildRequires: xorg-x11-devel libGL.so.1 libGLU.so.1

* Mon Jul  5 2004 Miloslav Trmac <mitr@volny.cz> - 0:3.0-0.fdr.2.a
- Add missing BuildRequires: alsa-lib-devel libGLU

* Thu Apr 29 2004 Miloslav Trmac <mitr@volny.cz> 0:3.0-0.fdr.1.a
- Update to foobillard-3.0a

* Tue Jan  6 2004 Miloslav Trmac <mitr@volny.cz> 0:2.9-0.fdr.1
- Update to foobillard-2.9

* Mon Oct  6 2003 Warren Togami <warren@togami.com> 0:2.8-0.fdr.3
- Ville's spec patch #713

* Sat Oct  4 2003 Miloslav Trmac <mitr@volny.cz> 0:2.8-0.fdr.2
- Use $RPM_OPT_FLAGS
- Use 'fedora' as desktop file vendor
- Preserve timestamps of the desktop file and the man page

* Sat Sep 13 2003 Miloslav Trmac <mitr@volny.cz> 0:2.8-0.fdr.1
- Initial Fedora package
