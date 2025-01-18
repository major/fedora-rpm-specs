%global patched_tarball 1

%if %patched_tarball
%global patch_ext .p
%else
%global patch_ext %{nil}
%endif

Summary: High speed arctic racing game
Name: extremetuxracer
Version: 0.8.2
Release: 10%{?dist}
License: GPL-2.0-or-later
URL: http://extremetuxracer.sourceforge.net
# This is really
# http://downloads.sourceforge.net/extremetuxracer/etr-%%{version}.tar.xz, but
# with a badly licensed font file removed. Use etr-clean-tarball.sh to
# regenerate from the upstream tarball.
Source0: etr-%{version}%{patch_ext}.tar.xz
Source1: etr-clean-tarball.sh
Source2: etr.appdata.xml
Source3: %{name}.metainfo.xml
Source4: %{name}-papercuts.metainfo.xml
#Source5: %%{name}-papercuts-outline.metainfo.xml
# manpages courtesy of Debian
Source6: etr.6
Source7: etr.de.6

# Don't reference removed files
#Patch0: etr-0.6.0-clean-tarball.patch

BuildRequires:  gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: SFML-devel
BuildRequires: freetype-devel
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: fontpackages-devel
BuildRequires: symlinks
BuildRequires: make

Requires: opengl-games-utils
Requires: extremetuxracer-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: extremetuxracer-papercuts-fonts = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires: extremetuxracer-papercuts-outline-fonts = %%{?epoch:%%{epoch}:}%%{version}-%%{release}
Requires: gnu-free-sans-fonts
Requires: hicolor-icon-theme

Provides:  %{name}-papercuts-outline-fonts = %{version}-%{release}
Obsoletes: %{name}-papercuts-outline-fonts < %{version}-%{release}

%description
Extreme Tux Racer is an open-source downhill racing game starring Tux, the
Linux mascot.


%package common
Summary: Common files for Extreme Tux Racer and its fonts
BuildArch: noarch

%description common
This package consists of files used by other %{name} packages.


%package papercuts-fonts
Summary: PaperCuts 2.0 font
BuildArch: noarch
Requires: extremetuxracer-common = %{?epoch:%{epoch}:}%{version}-%{release}

%description papercuts-fonts
This package contains the PaperCuts 2.0 font which is used by Extreme Tux
Racer.

%_font_pkg -n papercuts pc_20.ttf
%{_datadir}/appdata/%{name}-papercuts.metainfo.xml


#%%package papercuts-outline-fonts
#Summary: PaperCuts Outline 2.0 font
#BuildArch: noarch
#Requires: extremetuxracer-common = %%{?epoch:%%{epoch}:}%%{version}-%%{release}

#%%description papercuts-outline-fonts
#This package contains the PaperCuts Outline 2.0 font which is used by Extreme
#Tux Racer.

#%%_font_pkg -n papercuts-outline pc_outline.ttf
#%%{_datadir}/appdata/%%{name}-papercuts-outline.metainfo.xml


%prep
%setup -q -n etr-%{version}%{?patch_ext}
#%patch0 -p1 -b .clean-tarball
autoreconf -ivf


%build
%configure
make %{?_smp_mflags}


%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/etr.desktop
ln -snf opengl-game-wrapper.sh %{buildroot}%{_bindir}/etr-wrapper
desktop-file-edit --set-key=Exec --set-value=etr-wrapper \
    %{buildroot}%{_datadir}/applications/etr.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/pixmaps/etr.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{buildroot}%{_datadir}/pixmaps/etr.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

mkdir -p %{buildroot}%{_fontdir}
pushd %{buildroot}%{_datadir}/etr/fonts
rm -f stdbold.ttf stditalic.ttf std.ttf
for i in *.ttf; do
    mv "$i" %{buildroot}%{_fontdir}/
    ln -s "%{buildroot}%{_fontdir}/$i" "$i"
done
# Trick symlinks into making symlinks relative which are dangling in the
# buildroot
mkdir -p "%{buildroot}%{_fontbasedir}/gnu-free"
for i in FreeSansBold.ttf FreeSansOblique.ttf FreeSans.ttf; do
    touch "%{buildroot}%{_fontbasedir}/gnu-free/$i"
done
ln -s "%{buildroot}%{_fontbasedir}/gnu-free/FreeSansBold.ttf" stdbold.ttf
ln -s "%{buildroot}%{_fontbasedir}/gnu-free/FreeSansOblique.ttf" stditalic.ttf
ln -s "%{buildroot}%{_fontbasedir}/gnu-free/FreeSans.ttf" std.ttf
symlinks -c -s .
rm -rf "%{buildroot}%{_fontbasedir}/gnu-free"
popd
# move docs in correct location
mv -f %{buildroot}%{_docdir}/etr %{buildroot}%{_pkgdocdir}

# install appdata file
install -DT -m0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/etr.appdata.xml

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{name}-papercuts.metainfo.xml
#install -Dm 0644 -p %{SOURCE5} \
#        %{buildroot}%{_datadir}/appdata/%{name}-papercuts-outline.metainfo.xml

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml

install -Dm 0644 -p %{SOURCE6} %{buildroot}%{_mandir}/man6/etr.6
install -Dm 0644 -p %{SOURCE7} %{buildroot}%{_mandir}/de/man6/etr.6


%files
%doc %{_pkgdocdir}/*
%{_bindir}/etr
%{_bindir}/etr-wrapper
%{_datadir}/etr
%{_datadir}/appdata/etr.appdata.xml
%{_datadir}/metainfo/etr.appdata.xml
%{_datadir}/applications/etr.desktop
%{_datadir}/icons/hicolor/*/apps/etr.*
%{_mandir}/man6/etr.6*
%lang(de) %{_mandir}/de/man6/etr.6*

%files common
%doc AUTHORS ChangeLog
%license COPYING
%{_datadir}/appdata/%{name}.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Sérgio Basto <sergio@serjux.com> - 0.8.2-6
- Rebuild for SFML-2.6.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-1
- 0.8.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.8.1-1
- 0.8.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.0-1
- 0.8.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.5-1
- 0.7.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.4-6
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.4-1
- 0.7.4

* Fri Aug 19 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.3-1
- 0.7.3
- outline.ttf dropped upstream.

* Sat Feb 27 2016 Hans de Goede <hdegoede@redhat.com> - 0.7.1-1
- Update to new 0.7.1 release
- Switch to using SFML as game-lib (upstream change)
- Properly install new scalable icon
- Add manpage (courtesy of Debian)
- Cleanup spec file a bit

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Nils Philippsen <nils@redhat.com> - 0.6.0-7
- don't crash in treeless levels (#1183260, thanks to Jakub Vaněk for the
  original patch)

* Tue Nov 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.6.0-6
- Add metainfo file to show this font in gnome-software

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Nils Philippsen <nils@redhat.com> - 0.6.0-3
- phase out font compat symlinks from Fedora 21 on

* Wed Dec 11 2013 Nils Philippsen <nils@redhat.com> - 0.6.0-2
- install appdata file (#1036330)

* Wed Dec 11 2013 Nils Philippsen <nils@redhat.com> - 0.6.0-1
- version 0.6.0
- use patched tarball cleaned from dubiously licensed font
- drop obsolete patches, build requirements and age-old compat cruft
- use %%global instead of %%define

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.4-12
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 0.4-8
- rebuild for gcc 4.7

* Wed Nov 09 2011 Nils Philippsen <nils@redhat.com> - 0.4-7
- comment patches
- patch and rebuild for libpng-1.5
- fix use of memset()

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Nils Philippsen <nils@redhat.com> 0.4-5
- don't call null members (#652913)

* Mon Nov 15 2010 Nils Philippsen <nils@redhat.com> 0.4-4
- rebuild against new toolchain

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Nils Philippsen <nils@redhat.com> 0.4-2
- package fonts separately to comply with font packaging guidelines (#477383)

* Wed Mar 05 2008 Nils Philippsen <nphilipp@redhat.com> 0.4-1
- Package Review (#436126):
  - remove BR: sed, zlib-devel
  - add BR: pkgconfig
  - use icon name without extension in desktop file

* Wed Mar 05 2008 manuel wolfshant <wolfy@fedoraproject.org>
- add --with-tcl=... to %%configure line

* Wed Mar 05 2008 Nils Philippsen <nphilipp@redhat.com> 0.4-0
- version 0.4
- initial packaging based on ppracer
