%global rdnsname io.gitlab.LibreGames.jumpnbump

Name:           jumpnbump
Version:        1.70
Release:        1%{?dist}
Summary:        Cute multiplayer platform game with bunnies
License:        GPL-2.0-or-later
URL:            https://gitlab.com/LibreGames/jumpnbump
Source0:        https://gitlab.com/LibreGames/jumpnbump/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(zlib)

# For desktop and AppStream files validation
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# For icon theme directories
Requires:       hicolor-icon-theme

# For music support, dlopen()'ed by SDL2_mixer
Requires:       libmodplug
Requires:       libxmp

%if 0%{?fedora}
Recommends:     %{name}-menu
%endif

%description
Jump 'n Bump is a cute multiplayer platform game in which you, as a bunny,
have to jump on your opponents to make them explode. It is a true multiplayer
game with network support and shouldn't be played alone, although computer
bunnies with limited AI are available. The game is a UNIX port of the old DOS
game by Brainchild Design.

%package menu
Summary:        Level selection and config menu for the Jump 'n Bump game
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  make

Requires:       %{name} = %{version}-%{release}
Requires:       python3-pillow
Requires:       python3-gobject

%description menu
Python 3/GTK+3 based level selection and configuration interface for the Jump 'n
Bump game.

%prep
%autosetup -p1

%build
export CFLAGS="%{?build_cflags}"
export LDFLAGS="%{?build_ldflags}"

%make_build PREFIX=%{_prefix} SYSINSTALL=1
%make_build PREFIX=%{_prefix} -C menu

%install
%make_install PREFIX=%{_prefix} SYSINSTALL=1
%make_install PREFIX=%{_prefix} -C menu

%find_lang %{name}-menu

%check
# Validate desktop and AppStream files
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}{,-menu}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.metainfo.xml

%files
%doc AUTHORS ChangeLog docs/* README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/gobpack
%{_bindir}/jnb*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/jumpbump.dat
%{_datadir}/applications/%{rdnsname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{rdnsname}.png
%{_datadir}/metainfo/%{rdnsname}.metainfo.xml
%{_mandir}/man6/%{name}.6*

%files menu -f %{name}-menu.lang
%doc menu/README.md
%license COPYING
%{_bindir}/%{name}-menu
%{_datadir}/%{name}/%{name}_menu.glade
%{_datadir}/applications/%{rdnsname}-menu.desktop

%changelog
* Mon Mar 09 2026 Rémi Verschelde <rverschelde@gmail.com> - 1.70-1
- Version 1.70

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.61-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 06 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.61-13
- Fix icon installation

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Rémi Verschelde <rverschelde@gmail.com> - 1.61-3
- Workaround FTBFS with GCC 10 defaulting to -fno-common (rhbz#1799558)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Rémi Verschelde <rverschelde@gmail.com> - 1.61-1
- Version 1.61
- jumpnbump-menu now uses Python 3/GTK+3 (rhbz#1738040)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.60-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 02 2017 Rémi Verschelde <rverschelde@gmail.com> 1.60-2
- Add missing dependency: libmodplug for music support
- Add missing dependency: pygtk2-libglade

* Mon May 29 2017 Rémi Verschelde <rverschelde@gmail.com> 1.60-1
- Import in Fedora (#1456203)
- Adapt to Fedora with help from Neal Gompa
- Backport upstream patches for appdata file and python shebang
- Add scriptlets to update the icon cache in the absence of filetriggers
  https://fedoraproject.org/wiki/Packaging:Scriptlets#Icon_Cache

* Sat May 27 2017 Rémi Verschelde <akien@mageia.org> 1.60-2.mga6
+ Revision: 1105173
- Package more docs and license terms

* Wed May 24 2017 Rémi Verschelde <akien@mageia.org> 1.60-1.mga6
+ Revision: 1104457
- Version 1.60

* Fri May 19 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170519.3.mga6
+ Revision: 1103391
- Fix bogus requires in jumpnbump-menu, and make it noarch

* Fri May 19 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170519.2.mga6
+ Revision: 1103253
- Disable parallel build completely
- Sync with upstream 20170519, adds jumpnbump-menu subpackage

* Wed May 17 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170516.1.mga6
+ Revision: 1102304
- Snapshot 20170516

* Wed Apr 19 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170411.4.mga6
+ Revision: 1096845
- Limit number of jobs for parallel build
- Another attempt to fix parallel building
- Attempt at fixing dependency ordering
- imported package jumpnbump
