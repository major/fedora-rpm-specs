Name:           asylum
Version:        0.3.2
Release:        33%{?dist}
Summary:        Game involving shooting anything that moves & collecting others
# For detailed licensing, see the README
License:        GPL-3.0-only and LicenseRef-Fedora-Public-Domain
URL:            http://sdl-asylum.sourceforge.net
Source0:        http://downloads.sourceforge.net/sdl-%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Patch0:         asylum-0.3.2-paths.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  SDL_mixer-devel
BuildRequires: make
Requires:       hicolor-icon-theme

%description
SDL Asylum is a C port of the computer game Asylum, which was written by Andy
Southgate in 1994 for the Acorn Archimedes and is now public domain. The object
is to find things that look like brain cells and shut them down! The game
revolves around shooting anything which moves, collecting anything which
doesn't move and most importantly, finding your way to each of the eight
pulsating neurons scattered through the immense map.

%prep
%setup -q

%patch -P0 -p0

# Character encoding fixes
iconv -f iso8859-1 README -t utf8 > README.conv \
    && /bin/mv -f README.conv README

# Delete bundled binary to make absolutely sure we get a new one.
rm -f %{name}

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=Asylum
GenericName=Platform Game
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ActionGame;
EOF

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_var}/games/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
touch %{buildroot}%{_var}/games/%{name}/{EgoHighScores,PsycheHighScores,IdHighScores,ExtendedHighScores}

install -m0755 %{name} %{buildroot}%{_bindir}
cp -a data/* %{buildroot}%{_datadir}/%{name}

install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop

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
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: https://sourceforge.net/u/blotwell/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">asylum.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A retro platform style game where you enter the surreal world of a brain</summary>
  <description>
    <p>
      Asylum is a Linux port of the game "Asylum" written originally for the
      Acorn Archimedes.
    </p>
    <p>
      Enter the surreal world inside a young boy's brain and help destroy
      malfunctioning brain cells.
    </p>
  </description>
  <url type="homepage">http://sdl-asylum.sourceforge.net</url>
  <screenshots>
    <screenshot type="default">http://sourceforge.net/p/sdl-asylum/screenshot/134775.jpg</screenshot>
    <screenshot>http://sourceforge.net/p/sdl-asylum/screenshot/136451.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
# Note the game is SETGID games for the hi-scores.
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%attr(0775,root,games) %dir %{_var}/games/%{name}
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc Instruct README COPYING
%ghost %{_var}/games/%{name}/EgoHighScores
%ghost %{_var}/games/%{name}/PsycheHighScores
%ghost %{_var}/games/%{name}/IdHighScores
%ghost %{_var}/games/%{name}/ExtendedHighScores


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-28
- Convert top SPDX license.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-16
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.2-10
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.3.2-9
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.3.2-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Thu Jul 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.3.2-4
- Fixed data path.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May  4 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.3.2-2
- Build with RPM_OPT_FLAGS and RPM_LD_FLAGS.
- Fix desktop entry warnings.

* Fri Apr 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.2-1
- Update 0.3.2 - Fix FTBFS, drop not needed patch

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Michael Fleming <mfleming+rpm@thatfleminggent.com> - 0.3.0-1
- Update to 0.3.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.4-3
- fix makefile patch to apply properly

* Fri Aug 29 2008 Michael Fleming <mfleming+rpm@enlartenment.com> - 0.2.4-2
- New builders don't like Patch0 declaration, adjust make it happy

* Fri Aug 29 2008 Michael Fleming <mfleming+rpm@enlartenment.com> - 0.2.4-1
- Upgrade to 0.2.4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.3-3
- Autorebuild for GCC 4.3

* Tue Nov 27 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.2.3-2
- Enable ppc/ppc64 build. Endian issues seem resolved (BZ 319541)

* Sun Nov 25 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.2.3-1
- Upgrade to 0.2.3
- Removed asylum-0.2.2-fixsound.patch - fixed upstream

* Fri Oct 05 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.2.2-2
- Release bump

* Sun Sep 09 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.2.2-1
- Initial release
