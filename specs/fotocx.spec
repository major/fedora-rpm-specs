Name:    fotocx
Version: 25.0
Release: 1%{?dist}
Summary: Photo editor

License: GPL-3.0-or-later
URL:     https://kornelix.net/fotocx/fotocx.html
Source0: https://kornelix.net/downloads/downloads/fotocx-%{version}-source.tar.gz
Source1: %{name}.desktop
Patch0:  metainfo.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

BuildRequires: gcc-c++
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libjpeg-turbo-devel
BuildRequires: libtiff-devel
BuildRequires: lcms2-devel
BuildRequires: libchamplain-devel
BuildRequires: clutter-gtk-devel
BuildRequires: make

# Presence checked at build time
Requires: perl-Image-ExifTool
Requires: xdg-utils
Requires: dcraw
Requires: xmessage
Requires: hicolor-icon-theme

Recommends: binutils
Recommends: ffmpeg-free
Recommends: ImageMagick
Recommends: libheif-tools
Recommends: libwebp-tools
Recommends: openjpeg2-tools
Recommends: rawtherapee
Recommends: vlc-cli vlc-plugins-video-out

# Drop after Fedora 43
Provides: fotoxx = %{version}-%{release}
Obsoletes: fotoxx < 23.82-5

%description
Fotocx is a free open source Linux program for editing image files
from a digital camera. The goal of fotocx is to meet most image editing
needs while remaining easy to use.

%prep
%autosetup -p0 -n %{name}
# make binutils optional
sed -i -e '/addr2line/s/"yes"/"no"/' fotocx.cc

%build
# This package's Makefile is bizarre
# Misc. environment tweaks to let Makefile honor %%{optflags}
make %{?_smp_mflags} PREFIX=%{_prefix} \
    CXXFLAGS="%{optflags}" \
    LDFLAGS="%{build_ldflags}"

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} DOCDIR=%{_pkgdocdir}
install -Dm 644 -p %{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

desktop-file-install --vendor="" \
    --mode 644 \
    --remove-category="Application" \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{SOURCE1}

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*%{name}.metainfo.xml

#symlink identical binaries
rm -f %{buildroot}%{_bindir}/fotocx-snap
ln -s %{_bindir}/fotocx %{buildroot}%{_bindir}/fotocx-snap

# Drop unused
rm -f %{buildroot}%{_prefix}/applications/fotocx.desktop
rm -f %{buildroot}%{_datadir}/icons/fotocx.png


%files
%license doc/copyright
%doc doc/*
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_metainfodir}/*%{name}.metainfo.xml

%changelog
* Thu Jan 02 2025 Gwyn Ciesla <gwync@protonmail.com> - 25.0-1
- 25.0

* Tue Nov 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.70-1
- 24.70

* Tue Oct 01 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.60-1
- 24.60

* Tue Oct 01 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.50-3
- Update and soften optional dependencies

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.50-1
- 24.50

* Wed Jun 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.40-1
- 24.40

* Mon May 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.30-1
- 24.30

* Thu Apr 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.21-1
- 24.21

* Wed Apr 03 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.20-1
- 24.20

* Wed Feb 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.11-2
- Review fixes.

* Tue Feb 27 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.11-1
- 24.11, rename Fotoxx->Fotocx

* Tue Feb 13 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 23.82-4
- Drop i686 support (leaf package)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.82-1
- 23.82

* Mon Dec 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.81-1
- 23.81

* Mon Dec 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.80-1
- 23.80

* Wed Nov 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.74-1
- 23.74

* Fri Oct 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.72-1
- 23.72

* Mon Oct 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.70-1
- 23.70

* Tue Aug 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.60-1
- 23.60

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.50-1
- 23.50

* Wed Apr 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.32-1
- 23.32

* Mon Apr 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.31-1
- 23.31

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.2-2
- migrated to SPDX license

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.2-1
- 23.2

* Tue Jan 31 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.1-1
- 23.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.0-1
- 23.0

* Thu Nov 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.41-1
- 22.41

* Tue Nov 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.40-1
- 22.40

* Mon Oct 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.35-1
- 22.35

* Thu Sep 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.31-1
- 22.31

* Mon Aug 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.30-1
- 22.30

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.20-1
- 22.20

* Wed Jun 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.18-1
- 22.18

* Mon May 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.16-1
- 22.16

* Sun Apr 03 2022 Sérgio Basto <sergio@serjux.com> - 22.15-1
- Update fotocx to 22.15

* Thu Mar 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.14-1
- 22.14

* Fri Feb 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.12-1
- 22.12

* Thu Jan 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.11-1
- 22.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.1-1
- 22.1

* Mon Oct 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.60-1
- 21.60

* Fri Oct 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.55-1
- 21.55

* Tue Sep 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.52-1
- 21.52

* Thu Sep 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.51-1
- 21.51

* Mon Aug 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.50-1
- 21.50

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Sérgio Basto <sergio@serjux.com> - 21.44-2
- Adjustment of build requires and requires based on doc/README and fotocx.cc
  line 402
- Patch to use opj2_decompress provided by openjpeg2 package

* Wed Jun 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.44-1
- 21.44

* Tue Jun 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.42-1
- 21.42

* Tue Jun 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.41-1
- 21.41

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.40-1
- 21.40

* Mon Mar 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.34-1
- 21.34

* Mon Feb 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.33-1
- 21.33

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.32-1
- 21.32

* Wed Oct 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.19-1
- 20.19

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.18-1
- 20.18

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.17-1
- 20.17

* Mon Jul 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.16-1
- 20.16

* Fri Jul 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.15-1
- 20.15

* Tue Jun 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.14-1
- 20.14

* Tue May 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.13-1
- 20.13

* Sun May 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.12-1
- 20.12

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.11-1
- 20.11

* Wed Mar 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.10-1
- 20.10

* Tue Feb 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.09-1
- 20.09

* Wed Feb 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.08-1
- 20.08

* Mon Feb 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.07-1
- 20.07

* Mon Feb 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.06-1
- 20.06

* Wed Jan 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.05-1
- 20.05

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04-1
- 20.04

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.03-1
- 20.03

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.02-1
- 20.02

* Mon Nov 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.20-1
- 19.20

* Mon Nov 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.19-1
- 19.19

* Wed Oct 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.18-1
- 19.18

* Wed Sep 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.17-1
- 19.17

* Tue Aug 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.16-1
- 19.16

* Sat Aug 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.15-1
- 19.15

* Mon Aug 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.14-1
- 19.14

* Mon Aug 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.13-1
- 19.13

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.12-1
- 19.12

* Thu May 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.11-1
- 19.11

* Thu Apr 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.10-1
- 19.10

* Tue Apr 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.9-1
- 19.9

* Fri Apr 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.8-1
- 19.8

* Mon Apr 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.7-1
- 19.7

* Wed Mar 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.6-1
- 19.6

* Mon Feb 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.5-1
- 19.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Gwyn Ciesla <limburgher@gmail.com> - 19.4-1
- 19.4

* Tue Jan 29 2019 Gwyn Ciesla <limburgher@gmail.com> - 19.2-1
- 19.2

* Mon Jan 07 2019 Gwyn Ciesla <limburgher@gmail.com> - 19.0-1
- 19.0

* Fri Jul 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.07.1-1
- 18.07.1

* Thu Jul 19 2018 Adam Williamson <awilliam@redhat.com> - 18.07-3
- Rebuild for new libraw
- Disable -Wall so it builds despite format-truncation mistakes

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.07-1
- 18.07

* Wed May 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.01.4-1
- 18.01.4

* Fri Feb 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.01.3-1
- 18.01.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.01.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.01.2-1
- 18.01.2

* Thu Jan 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.01.1-1
- 18.01.1

* Tue Jan 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.01-1
- 18.01

* Fri Sep 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 17.08.3-1
- 17.08.3

* Fri Aug 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 17.08.2-1
- 17.08.2, BZ 1354187.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 16.08.1-2
- Rebuild for new LibRaw.

* Tue Sep 13 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 16.08.1-1
- Update to 16.08.1 version by mail request of Eduardo.
- Add BR LibRaw-devel, libchamplain-devel

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 16.01-1
- Update to 16.01 upstream version (bz#1249298).

* Wed Jul 08 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 15.07-1
- New version 15.07 - bz#1217732 (also request by mail from Eduardo Jorde).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 15.04.1-1
- Update to 15.04.1 - bz#1197327.

* Wed Feb 25 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 15.02.1-1
- Update to 15.02.1 - bz#1157447.

* Fri Oct 24 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.10.1-1
- Update to 14.10.2 - bz#1150466.

* Sun Sep 7 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.09-1
- Update to 14.09 - bz#1135811
- Drop appdata file/directory hack.

* Mon Aug 18 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.08-1
- Update to 14.08 - bz#1103438
- Install appdata dir.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.05.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.05.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.05.1-1
- Update to 14.05.1 - bz#1096062

* Tue Apr 29 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.05-1
- Update to 14.05 - bz#1092427

* Tue Apr 22 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.04.2-1
- Update to 14.04.2 version - bz#1084959.

* Thu Apr 3 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.04-1
- Update to 14.04 version - bz#1080804.

* Fri Mar 7 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.03.1-1
- Update to 14.03.1 version - bz#1070119.

* Sat Feb 8 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.02.2-1
- Update to 14.02.2 - bz#1062186

* Tue Jan 7 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 14.02.1-1
- Update to 14.02.1 (#977116)

* Mon Aug 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 13.04-4
- Reflect docdir changes (Fix FTBFS, RHBZ#992281).
- Drop fotocx-13.01-pthread-dep.patch (not required, anymore).
- Add tweaks to let package honour %%optflags.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 13.04-2
- Add dcraw dependency (bz#947087).

* Sat Mar 30 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 13.04-1
- Update to 13.04.
- Fix URL (bz#910155)
- Add BR lcms2-devel

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 2 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 13.01-1
- Updated to new version by mail request from Eduardo Jorge.
- Bump gtk dep to 3 version.
- Remade patch to link with pthread for new version.

* Thu Aug 23 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 12.01.2-5
- Remove require printoxx as it dead - bz#843258. Author said it replaced by mashup.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.01.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 12.01.2-3
- Rebuild due libtiff update http://www.mail-archive.com/devel@lists.fedoraproject.org/msg42846.html

* Fri Jan 6 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 12.01.2-2
- Update to 12.01.2 for fix bz#755715

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 10.11.1-9
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 4 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 10.11.1-7
- Major update (BZ#644023)
- Remove outdated patch - fotocx-8.0-mandir.patch.
- Add BR libtiff-devel
- Adjust some pathes for new version.
- Remove %%doc mark from man.

* Sun Aug 9 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 8.0-6
- Add R and BR: xdg-utils

* Sun Aug 9 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 8.0-5
- Update to version 8.0
- Delete old patches.
- Remove rm libfreeimage.a, name of dir in %%setup.
- Replace all $RPM_BUILD_ROOT by %%{buildroot}
- Add Patch0: fotocx-8.0-mandir.patch
- Add new file %%doc %%{_mandir}/man1/%%{name}.1*

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Dennis Gilmore <dennis@ausil.us> - 6.0-3
- add patch to dynamically link to libfreeimage

* Wed Feb 25 2009 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] spb [ dOt.] su> - 6.0-2
- Forgot patch

* Wed Feb 25 2009 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] spb [ dOt.] su> - 6.0-1
- New version 6.0
- Adjust Source0 url (inspired by Kevin Fenzi in fedora-devel-list: https://www.redhat.com/archives/fedora-devel-list/2009-February/msg01622.html ).

* Wed Feb 25 2009 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] spb [ dOt.] su> - 5.8-2
- Add patch0 fotocx-5.8.constchar.patch
- Reformat spec with tabs, remove trailing spaces.

* Sun Jan  4 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.8-1
- Rebuild for 5.8
* Mon Dec  1 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.7-1
- Rebuild for 5.7
* Sun Nov 16 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.6-1
- Rebuild for 5.6
* Tue Nov  4 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.5-1
- Rebuild for 5.5
* Thu Oct  9 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.4-1
- Rebuild for 5.4
* Thu Sep 18 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.3-1
- Rebuild for 5.3
* Sun Aug 31 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.2-1
- Rebuild for 5.2
* Sun Aug 24 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.1-1
- Rebuild for 5.1
* Fri Aug  8 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.0.1-1
- Rebuild for 5.0.1
* Sat Aug  2 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 5.0-1
- Rebuild for 5.0
* Tue Jul 22 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.9-1
- Initial build
