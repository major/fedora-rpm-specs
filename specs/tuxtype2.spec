Name:           tuxtype2
Version:        1.8.1
Release:        35%{?dist}

Summary:        Tux Typing, an educational typing tutor for children
License:        GPL-2.0-or-later
URL:            https://github.com/tux4kids/tuxtype/
Source0:        https://github.com/tux4kids/tuxtype/archive/1.8.1-7/tuxtype_w_fonts-%{version}.tar.gz
Patch0:         tuxtype2-1.8.1-chown.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel >= 1.2.5 SDL_image-devel SDL_mixer-devel SDL_Pango-devel
BuildRequires:  SDL_ttf-devel ImageMagick desktop-file-utils t4k_common-devel
BuildRequires:  automake autoconf
BuildRequires:  librsvg2-devel


%description
Tux Typing is an educational typing tutor for children. It features several
different types of game-play, at a variety of difficulty levels.


%prep
%setup -q -n tuxtype_w_fonts-1.8.1
%patch -P0 -p1
rm -rf data/fonts/*.ttf
# fix wrong end of line encoding
sed -i -e 's|\r||g' doc/en/TuxType_port_Mac.txt
#unknow lang
pushd po
mv zh_N.gmo zh_CN.gmo
mv zh_N.po zh_CN.po
popd


%build
%configure --localstatedir=%{_localstatedir}/games --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT/%{_usr}/doc
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/games/tuxtype

cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Tux Typing
Comment=An educational typing tutor for children.
Exec=tuxtype
Icon=tuxtype
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Game;Application;
EOF

convert -size 48x48 tuxtype.ico $RPM_BUILD_ROOT/%{_datadir}/pixmaps/tuxtype.png
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ \
                     --add-category X-Fedora \
                     %{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<application>
  <id type="desktop">tuxtype2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      TuxTyping is an educational typing tutor for kids starring Tux, the Linux
      penguin.
    </p>
    <p>
      This educational game comes with two different games for practicing your
      typing, and having a great time doing it.
    </p>
  </description>
  <url type="homepage">http://tux4kids.alioth.debian.org/tuxtype/index.php</url>
  <screenshots>
    <screenshot type="default">http://tux4kids.alioth.debian.org/tuxtype/screenshots/tux_eat_fish.jpg</screenshot>
    <screenshot>http://tux4kids.alioth.debian.org/tuxtype/screenshots/tux_waiting.jpg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%find_lang tuxtype


%files -f tuxtype.lang
%doc AUTHORS COPYING ChangeLog README TODO doc/en/howtotheme.html doc/en/TuxType_port_Mac.txt
%attr(-,root,games) %{_bindir}/tuxtype
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/tuxtype
%config(noreplace) %{_sysconfdir}/tuxtype
%attr(0755,root,games) %config(noreplace) %{_localstatedir}/games/tuxtype


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.8.1-31
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.8.1-23
- New upstream location.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.8.1-13
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.8.1-8
- Remove vendor tag from desktop file
- Cleanup spec as per recently changed packaging guidelines

* Thu Aug 16 2012 Tom Callaway <spot@fedoraproject.org> - 1.8.1-7
- fix chown patch

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.8.1-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 31 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.8.1-2
- missing sysconfidir ; fixes bug #598112
- unknown zh_N language, renamed to zh_CN

* Sat May 01 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.8.1-1
- 1.8.1
- remove DSO link fix applied upstream

* Sat Feb 13 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.8.0-3
- Fix DSO link bug (bz #564706)

* Sat Jan 09 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.8.0-2
- Fix for wordlist path

* Tue Nov 10 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.8.0-1
- 1.8.0

* Mon Sep 14 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.7.5-1
- 1.7.5
- removed shipped fonts

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.17-1
- update to 1.5.17 (incorporate Jonathan Dieter's changes)

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.3-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.3-3
- Autorebuild for GCC 4.3

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 1.5.3-2
- Rebuild.
- Use "make install DESTDIR=..." instead of the macro.

* Fri Feb 17 2006 Steven Pritchard <steve@kspei.com> 1.5.3-1
- Update to 1.5.3

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.5.2-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Mar 30 2004 Panu Matilainen <pmatilai@welho.com> 0:1.5.2-0.fdr.1
- update to 1.5.2
- remove the silly separator lines from spec
- add encoding to desktop file

* Fri Nov 28 2003 Panu Matilainen <pmatilai@welho.com> 0:1.5.1-0.fdr.2
- run aclocal + autoconf before configure
- add build dependencies for automake and autoconf

* Sat Aug 23 2003 Panu Matilainen <pmatilai@welho.com> 0:1.5.1-0.fdr.1
- Initial Fedora packaging.
