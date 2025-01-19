Name:           monsterz
Version:        0.7.1
Release:        38%{?dist}
Summary:        Puzzle game, similar to Bejeweled or Zookeeper
License:        WTFPL
URL:            http://sam.zoy.org/monsterz/
Source0:        http://sam.zoy.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.score
Patch0:         %{name}-0.7.1-userpmopts.patch
Patch1:         %{name}-0.7.1-64bitfix.patch
Patch2:         %{name}-0.7.1-blit-crash.patch
Patch3:         %{name}-0.7.1-py3.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
Requires:       python3-pygame
Requires:       hicolor-icon-theme
Provides:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-data < 0.7.1

%description
Monsterz is a little arcade puzzle game, similar to the famous Bejeweled or
Zookeeper. The goal of the game is to create rows of similar monsters, either
horizontally or vertically. The only allowed move is the swap of two adjacent
monsters, on the condition that it creates a row of three or more. When
alignments are cleared, pieces fall from the top of the screen to fill the
board again. Chain reactions earn you even more points.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p1
%py3_shebang_fix .

%build
make %{?_smp_mflags} prefix=%{_usr} datadir=%{_datadir} pkgdatadir=%{_datadir}/%{name} CFLAGS="%{optflags}"

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Monsterz
GenericName=Monsterz Puzzle Game
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF


%install
# Bypass make install as it requires root priviledges and the SRPM
# may not necessarily be built as root
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/{applications,icons/hicolor/64x64/apps}
mkdir -p %{buildroot}%{_datadir}/%{name}/{graphics,sound}
mkdir -p %{buildroot}%{_var}/games
install -pm0755 %{name} %{buildroot}%{_bindir}
install -pm0755 %{name}.py %{buildroot}%{_datadir}/%{name}
cp -a graphics/* %{buildroot}%{_datadir}/%{name}/graphics
cp -a sound/* %{buildroot}%{_datadir}/%{name}/sound

install -pm0664 %{SOURCE1} %{buildroot}%{_var}/games/%{name}

desktop-file-install \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop

install -pm0644 graphics/icon.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}
%attr(2755,root,games) %{_bindir}/%{name}
%attr(-,root,games) %config(noreplace) %{_var}/games/%{name}
%license COPYING
%doc AUTHORS README TODO


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.1-33
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.1-26
- Bump EVR.

* Fri Jun 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.1-25
- Fix 64 bit patch.

* Mon May 25 2020 scott snyder <sss@li-snyder.org> - 0.7.1-24
- Python 3 compatibility.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.1-22
- Fix shebang handling.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-19
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.1-10
- Drop desktop vendor tag.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Rafał Psota <rafalzaq@gmail.com> - 0.7.1-4
- fixed #473763

* Tue Feb 26 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.1-3
- Fix for BZ 434688

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.1-2
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.1-1
- Upgrade to 0.7.1
- Drop separate data package as it's unnecessary
- Merge .desktop back into SPEC
- Various spec cleanups
- Updated the "use rpm opts" patch
- Use the icon now supplied

* Wed Aug 22 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-8
- Release bump for F8 mass rebuild

* Mon Aug 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-7
- Release bump for FC6 mass rebuild

* Tue Jul 25 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-6
- Split data into a separate package.

* Sun Jul 23 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-5
- Moved .desktop external to spec
- Moved score file external to spec
- License changed to WTFPL
- Use %%{_datadir}/%%{name} not %%{_datadir}/games/%%{name}

* Sun Jul 09 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-4
- Moved icon installation to make it freedesktop compliant
- Added %%post and %%postun sections to update icon cache at installation
- Move hiscore table and .desktop generation to %%build

* Sat Jun 24 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-3
- Cosmetic fixes for the Dribble repository

* Mon May 29 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-2
- Replace %%{__rm} in clean section with rm
- Added patch to compile using rpmoptflags

* Mon May 22 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.0-1.iss
- Initial Release
