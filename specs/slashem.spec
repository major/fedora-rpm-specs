Name:           slashem
Version:        0.0.8
Release:        0.40.E0F1%{?dist}
Summary:        Super Lotsa Added Stuff Hack - Extended Magic

License:        NGPL
URL:            https://slashem.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/se008e0f1.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         slashem-config.patch
# fix building with libpng 1.5
Patch1:         slashem-libpng-1.5.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1037330
Patch2:         slashem-format-security.patch
# https://sourceforge.net/p/slashem/bugs/963/
Patch3:         slashem-add-FDECLs-c99.patch
Patch4:         slashem-configure-c99.patch
Patch5:         slashem-c99.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/convert
BuildRequires:  ncurses-devel
BuildRequires:  bison, flex, desktop-file-utils
BuildRequires:  bdftopcf, libX11-devel, libXext-devel
BuildRequires:  libXmu-devel, libXpm-devel, libXt-devel
BuildRequires:  SDL-devel  libGL-devel libpng-devel zlib-devel
BuildRequires:  pkgconfig(xaw7)
# to compress save files
Requires:       bzip2
# For icon theme directories.
Requires:       hicolor-icon-theme
# for X11 core fonts
Requires:       nethack-bitmap-fonts-core

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global fa_var      /var/games/%{name}
%global fa_save     /var/games/%{name}/save
%global fa_share    %{_datadir}/games/%{name}
%global fa_unshare  %{_libdir}/games/%{name}
%global fa_doc      %{_pkgdocdir}

%description
From the land before 3DFX, before VGA graphics and DOOM, before the IBM PC, way
back in the dark ages of Unixland, there was a game. They called it Rogue.
People played it, and found it good. From this basis, Hack was born. Soon Hack
became Nethack, because it was developed by many people (and has nothing to do
with hacking the internet). And people played this on many machines, from
Unices to Macs to PCs, due to the amazing power of Open Source Code.

But the DevTeam, the reclusive masterminds of Nethack, are a rather quiet
bunch, gracing the world with new versions as they see fit, and when they see
fit. Which is usually a new version every good number of years.

And there was much gnashing of teeth.

But because of the Freely Available Source Code Phenomenon, people began making
their own versions of Nethack to tide themselves between magical releases.

SLASH'EM is the (continuing) saga of one such variant...


%prep
%autosetup -p1 -n %{name}-%{version}E0F1

sed -i \
    -e 's:^\(#define FILE_AREA_VAR\).*:\1 "%{fa_var}/":' \
    -e 's:^\(#define FILE_AREA_SAVE\).*:\1 "%{fa_save}/":'  \
    -e 's:^\(#define FILE_AREA_SHARE\).*:\1 "%{fa_share}/":' \
    -e 's:^\(#define FILE_AREA_UNSHARE\).*:\1 "%{fa_unshare}/":' \
    -e 's:^\(#define FILE_AREA_DOC\).*:\1 "%{fa_doc}/":' \
    include/unixconf.h

for f in *.txt ; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done


%build
export LIBXAW_CFLAGS="-I/usr/include"
export LIBXAW_LIBS="$(pkg-config --libs xaw7)"
%configure \
    --enable-tty-graphics   \
    --enable-x11-graphics   \
    --enable-sdl-graphics   \
    --enable-gl-graphics    \
    --enable-data-librarian \
    --enable-sinks          \
    --enable-reincarnation  \
    --enable-zouthern       \
    --enable-score-on-botl  \
    --enable-wizmode=games
# smp_mflags fails
make \
    FILE_AREA_VAR=%{fa_var} \
    FILE_AREA_SAVE=%{fa_save} \
    FILE_AREA_SHARE=%{fa_share} \
    FILE_AREA_UNSHARE=%{fa_unshare} \
    FILE_AREA_DOC=%{fa_doc} \
    SHELLDIR=%{_bindir}


%install
make install DESTDIR=%{buildroot} \
    FILE_AREA_VAR=%{buildroot}%{fa_var} \
    FILE_AREA_SAVE=%{buildroot}%{fa_save} \
    FILE_AREA_SHARE=%{buildroot}%{fa_share} \
    FILE_AREA_UNSHARE=%{buildroot}%{fa_unshare} \
    FILE_AREA_DOC=%{buildroot}%{fa_doc} \
    INSTALL="install -p" \
    SHELLDIR=%{buildroot}%{_bindir} \
    CHOWN=/bin/true \
    CHGRP=/bin/true

install -d -m 0755 %{buildroot}%{_mandir}/man6
make -C doc MANDIR=%{buildroot}%{_mandir}/man6 manpages

sed -i \
    -e 's!%{buildroot}!!g' \
    -e '/XUSERFILE/s!\$HACKDIR!%{fa_share}!' \
    %{buildroot}%{_bindir}/slashem

mv %{buildroot}%{fa_unshare}/recover %{buildroot}%{_bindir}/slashem-recover
mv %{buildroot}%{_mandir}/man6/recover.6 %{buildroot}%{_mandir}/man6/slashem-recover.6
rm %{buildroot}%{_mandir}/man6/[^s]*
rm %{buildroot}%{_pkgdocdir}/license

sed -i -e 's:^!\(SlashEM.tile_file.*\):\1:' %{buildroot}%{fa_share}/SlashEM.ad

install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
convert win/X11/nh_icon.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc history.txt doc/*.txt README.34 readme.* slamfaq.txt dat/history
%license dat/license
%{_bindir}/slashem
%{_bindir}/slashem-recover
%{fa_share}
%dir %{fa_unshare}
%{fa_unshare}/nhushare
%{_mandir}/man6/*.6*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/slashem.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%defattr(0664,root,games)
%config(noreplace) %{fa_var}/logfile
%config(noreplace) %{fa_var}/perm
%config(noreplace) %{fa_var}/record
%attr(0775,root,games) %dir %{fa_var}
%attr(0775,root,games) %dir %{fa_var}/save
%attr(2755,root,games) %{fa_unshare}/slashem


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.40.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.39.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.38.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.37.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Florian Weimer <fweimer@redhat.com> - 0.0.8-0.36.E0F1
- Further C99 compatibility fixes

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.35.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Peter Fordham <peter.fordham@gmail.com> - 0.0.8-0.34.E0F1
- Add missing Forward declarations for rename_area and remove_area and fix a call-site.
- Port configure script to C99.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.33.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.32.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.31.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.30.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.29.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.28.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.27.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.26.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.25.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.24.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.23.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.22.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.21.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-0.20.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 David King <amigadave@amigadave.com> - 0.0.8-0.19.E0F1
- Convert XPM icon the PNG

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.18.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 20 2014 David King <amigadave@amigadave.com> - 0.0.8-0.17.E0F1
- Update desktop file and validate it during check
- Add AppData description and validate it during check
- Preserve timestamps during install
- Tidy spec file

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.16.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.15.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Iain Arnell <iarnell@gmail.com> 0.0.8-0.14.E0F1
- apply patch to avoid format-security errors (RHBZ#1037330)

* Sat Aug 10 2013 Iain Arnell <iarnell@gmail.com> 0.0.8-0.13.E0F1
- use _pkgdocdir macro

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.12.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Iain Arnell <iarnell@gmail.com> 0.0.8-0.11.E0F1
- patch to support aarch64 (thanks, ausil)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.10.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.9.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 15 2012 Iain Arnell <iarnell@gmail.com> 0.0.8-0.8.E0F1
- fix build against libpng 1.5

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.7.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.6.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-0.5.E0F1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 19 2009 Iain Arnell <iarnell@gmail.com> 0.0.8-0.4.E0F1
- require nethack-bitmap-fonts-core, not nethack anymore

* Mon Jul 06 2009 Iain Arnell <iarnell@gmail.com> 0.0.8-0.3.E0F1
- don't install fonts - require nethack instead

* Wed Jun 10 2009 Iain Arnell <iarnell@gmail.com> 0.0.8-0.2.E0F1
- additional requires for scriptlets
- only run preun for final uninstall

* Thu May 21 2009 Iain Arnell <iarnell@gmail.com> 0.0.8-0.1.E0F1
- initial packaging

