%global short_version 1.0
Name:           freedroidrpg
Version:        %{short_version}
Release:        7%{?dist}
Summary:        Role playing game with Freedroid theme and Tux as the hero

License:        GPL-2.0-or-later
URL:            http://freedroid.sourceforge.net/
Source0:        http://ftp.osuosl.org/pub/freedroid/freedroidRPG-%{version}/freedroidRPG-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  ImageMagick
BuildRequires:  libvorbis-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libGLU-devel
BuildRequires:  gettext-devel
BuildRequires:  lua-devel
BuildRequires:  glew-devel
BuildRequires:  make
BuildRequires:  autoconf automake

Requires:       freedroidrpg-data = %{version}-%{release}


%description
The Freedroid RPG is an extension/modification of the classical
freedroid engine into a role playing game.

%package data
Summary:        Data files for the freedroidrpg game
BuildArch:      noarch
Requires:       freedroidrpg = %{version}-%{release}
%description data
Data files for the freedroidrpg game.

%prep
%setup -q
rm -f lua/*.a
rm -f lua/*.o

# Update the timestamp to avoid unnecessarily running configure
touch -r configure.ac aclocal.m4


%build
autoreconf -fi
export CPPFLAGS="$CPPFLAGS -fcommon -fPIE"
%configure --disable-dependency-tracking
%make_build


%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -m 644 data/graphics/FreedroidRPG.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/freedroidrpg.png
# Fix permissions, remove extra junk.
find $RPM_BUILD_ROOT%{_datadir}/%{name} -type f -exec chmod -x "{}" \;


%find_lang freedroidrpg
%find_lang freedroidrpg-data
%find_lang freedroidrpg-dialogs
cat freedroidrpg-data.lang >> freedroidrpg.lang
cat freedroidrpg-dialogs.lang >> freedroidrpg.lang
rm -f freedroidrpg-data.lang
rm -f freedroidrpg-dialogs.lang




%files -f freedroidrpg.lang
%license COPYING
%doc AUTHORS README* NEWS CONTRIBUTING.md
%{_bindir}/*
%{_datadir}/applications/org.freedroid.freedroidRPG.desktop
%{_metainfodir}/org.freedroid.freedroidRPG.appdata.xml
%{_datadir}/icons/*
%{_mandir}/man6/freedroidRPG.6.*

%files data
%{_datadir}/%{name}


%changelog
* Wed Jan 08 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.0-7
- Fix FTBFS

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0-2
- migrated to SPDX license

* Fri Feb 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0-1
- 1.0 final, move to Codeberg

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0rc2-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0rc2-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 09 2022 Leigh Scott <leigh123linux@gmail.com> - 1.0rc2-0.1
- Remove unused gtk+-devel
- Spec file clean up

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 1.0-0.rc2.8
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.rc2.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.rc2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.rc2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.rc2.4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.rc2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.0-0.rc2.2
- Fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.0-0.rc2
- 1.0 rc2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.16.1-9
- Remove obsolete requirements for %%post/%%postun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.1-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 06 2016 Jon Ciesla <limburgher@gmail.com> - 0.16.1-1
- Update to 0.16.1.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Jon Ciesla <limburgher@gmail.com> - 0.16-1
- Update to 0.16 final.

* Mon Sep 07 2015 Jon Ciesla <limburgher@gmail.com> - 0.16-0.rc2
- Update to latest.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0.15.1-9
- Rebuild for new SDL_gfx

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.15.1-7
- Build with system lua instead of bundled one

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.15.1-5
- Drop desktop vendor tag.

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.15.1-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.15.1-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.15.1-1
- New upstream.

* Mon Jan 09 2012 Jon Ciesla <limburgher@gmail.com> - 0.15-1
- New upstream.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.13-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.13-2
- recompiling .py files against Python 2.7 (rhbz#623297)

* Mon Apr 19 2010 Wart <wart@kobold.org> - 0.13-1
- Update to 0.13

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 4 2009 Wart <wart@kobold.org> - 0.12.1-1
- Update to 0.12.1
- Move data files to a noarch -data subpackage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Wart <wart at kobold.org> - 0.11.1-2
- Add coreutils requirement for rpm post scripts (BZ #476162)

* Tue Dec 16 2008 Wart <wart at kobold.org> - 0.11.1-1
- Update to 0.11.1

* Sun Feb 10 2008 Wart <wart at kobold.org> - 0.10.3-2
- Rebuild for gcc 4.3

* Sun Sep 16 2007 Wart <wart at kobold.org> - 0.10.3-1
- Update to 0.10.3

* Tue Aug 28 2007 Wart <wart at kobold.org> - 0.10.2-2
- License tag clarification
- Use correct .desktop file version
- Update to 0.10.2

* Sun Feb 25 2007 Wart <wart at kobold.org> - 0.10.1-1
- Update to 0.10.1
- Remove X-Fedora category from desktop file
- Remove patch that was incorporated upstream

* Wed Jan 10 2007 Wart <wart at kobold.org> - 0.10.0-1
- Update to 0.10.0
- Update the icon cache scriptlet to the Fedora recommendation
- Move game data out of /usr/share/games and into /usr/share/<name>,
  per the Games SIG recommendation.

* Fri Sep 1 2006 Wart <wart at kobold.org> - 0.9.13-3
- Rebuild for Fedora Extras
- Change BR: for opengl

* Thu Mar 9 2006 Wart <wart at kobold.org> - 0.9.13-2
- Add BR: for modular xorg.

* Sat Sep 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1
- 0.9.13.
- Drop some outdated docs.

* Thu Aug  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-0.2.rc3
- 0.9.13rc3, build with gcc4, lvalue cast fix applied upstream.
- Move icon to %%{datadir}/icons/hicolor.

* Sun Jul 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-0.2.rc2
- 0.9.13rc2.
- Apply upstream lvalue cast fix.
- Update desktop entry categories.

* Thu Jun  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.12-5
- Rebuild for FC4+ with compat-gcc-32 due to crashy gcc4 experience (#152498).
- Build with dependency tracking disabled.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.9.12-3
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.12-2
- rebuilt

* Mon Apr  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.12-0.fdr.1
- Update to 0.9.12 (bz2 tarball available upstream, yay!).

* Tue Feb 17 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.11-0.fdr.1
- Update to 0.9.11.
- Re-bzip2 tarball to save 15MB.
- Improve summary and description.

* Fri Jan 16 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.10-0.fdr.1
- Update to 0.9.10.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.9-0.fdr.1
- Update to 0.9.9-1.

* Tue Sep 16 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.8-0.fdr.2
- Use upstream "0.9.8-1" tarball.  Sigh.

* Mon Aug 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.8-0.fdr.1
- Update to 0.9.8.

* Fri Jul 18 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.6-0.fdr.1
- Update to 0.9.6.

* Tue May 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.5-0.fdr.1.patchlv1
- First build.
