%global icon_dest_dir %{_datadir}/icons/hicolor/32x32/apps
Name:     7kaa
Version:  2.15.4p1
Release:  7%{?dist}
Summary:  Seven Kingdoms: Ancient Adversaries

# Main program: GPLv2+
# misc_uuid: BSD
License:  GPLv2+ and BSD
URL:      http://7kfans.com/
Source0:  https://github.com/the3dfxdude/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libenet)
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_net)
BuildRequires: make

Requires: %{name}-data = %{version}-%{release}
Requires: hicolor-icon-theme

%description
Seven Kingdoms is a real-time strategy (RTS) computer game developed
by Trevor Chan of Enlight Software. The game enables players to
compete against up to six other kingdoms allowing players to conquer
opponents by defeating them in war (with troops or machines),
capturing their buildings with spies, or offering opponents money
for their kingdom.

Seven Kingdoms: Ancient Adversaries is a free patch provided by
Interactive Magic and added three new cultures, the Egyptians, the
Mughals and the Zulus, and a new war machine, Unicorn.

Due to licensing, in-game music needs to be downloaded separately.
Place the music files in /usr/share/7kaa/music.

%package data
BuildArch: noarch
Summary: In-Game data Seven Kingdoms: Ancient Adversaries

Requires: %{name} = %{version}-%{release}
Requires: hicolor-icon-theme

%description data
In-Game data Seven Kingdoms: Ancient Adversaries.

%prep
%setup -q

%build
# https://bugzilla.redhat.com/show_bug.cgi?id=1306226
export CXXFLAGS="%{optflags} -fsigned-char"
./autogen.sh
%configure
%make_build

%install
%make_install -p
%find_lang %{name}

### == icon files
mkdir -p %{buildroot}%{icon_dest_dir}
install -m 644 doc/7kicon.png %{buildroot}%{icon_dest_dir}

### == desktop file
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
GenericName=Seven Kingdoms: Ancient Adversaries
Comment=A real-time strategy (RTS) computer game
Exec=%{_bindir}/%{name}
Icon=%{name}_icon
Terminal=false
Type=Application
Categories=Game;StrategyGame
EOF

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

### == remove misplaced license file
rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%files -f %{name}.lang
%doc README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{icon_dest_dir}/7kicon.png

%files data
%{_datadir}/%{name}/

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4p1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4p1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4p1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4p1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.4p1-3
- Use pkgconfig for libcurl, enet, SDL2, SDL2_net, openal-soft

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.4p1-1
- Bump version and add note about music files to description

* Sun Jul 05 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.4-1
- Bump version and improve spec file

* Wed Jun 17 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.3-5
- Use the make_build macro instead of legacy _smp_mflags

* Wed May 27 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.3-4
- Fix files section, correct description

* Tue May 26 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.3-3
- Split off music installation from main 7kaa package

* Sat May 23 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.3-2
- Clean up and improve spec file

* Sun May 17 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.15.3-1
- Try to unorphan and update the package

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.14.7-2
- Remove obsolete scriptlets

* Thu Dec 07 2017 Ding-Yi Chen <dchen@redhat.com> - 2.14.7-1
- Upstream update to 2.14.7
  Fixes Bug 1458610 - 7kaa-2.14.7 is available
- Add Requires and BuildRequires libcurl

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Raphael Groner <projects.rg@smart.ms> - 2.14.6-2
- rebuilt due to branching

* Wed Mar 01 2017 Ding-Yi Chen <dchen@redhat.com> 2.14.6-1
- Upstream update to 2.14.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 07 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.14.5-12
- Build with -fsigned-char to fix FTBFS with GCC 6 (#1306226)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-10
- music won't get uninstall when upgrading.
- Remove /usr/share/doc/COPYING as it is already installed.

* Fri Jun 26 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-8
- Use name macro whenever possible.

* Wed Jun 24 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-7
- Fix the .desktop file.

* Tue Jun 23 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-6
- Requires: hicolor-icon-theme
- License become GPLv3+ and GPLv2+ as "gettext.h" is GPLv3

* Wed Jun 17 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-5
- Fix for Review Request Comment #11

* Tue Jun 16 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-4
- Fix for Review Request Comment #10

* Tue Jun 02 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-3
- Fix for Review Request Comment #8

* Mon Jun 01 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-2
- Fix for Review Request Comment #6

* Sun May 31 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.5-1
- Upstream update to 2.14.5
- BuildRequires: add enet-devel
- Use autodownloader to download music.

* Wed May 27 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.4-2
- Remove music.

* Tue May 05 2015 Ding-Yi Chen <dchen@redhat.com> 2.14.4-1
- Initial packaging.

