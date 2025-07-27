%global tag     1.11

Name:           sway
Version:        1.11
Release:        2%{?dist}
Summary:        i3-compatible window manager for Wayland
License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        %{url}/releases/download/%{tag}/%{name}-%{tag}.tar.gz
Source1:        %{url}/releases/download/%{tag}/%{name}-%{tag}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

# Minimal configuration file for headless or buildroot use
Source100:      config.minimal
Source101:      sway-portals.conf
Source102:      README.md

# Upstream patches

# Fedora patches

# Conditional patches

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson >= 1.3
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 1.26.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd) >= 239
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server) >= 1.21.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon) >= 1.5.0

# Require any of the available configuration packages;
# Prefer the -upstream one if none are directly specified in the package manager transaction
Requires:       %{name}-config
Suggests:       %{name}-config-upstream

%description
Sway is a tiling window manager supporting Wayland compositor protocol and
i3-compatible configuration.


# Configuration presets:
#
%package        config-upstream
Summary:        Upstream configuration for Sway
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-config = %{version}-%{release}
Conflicts:      %{name}-config

# Require the wallpaper referenced in the config.
# Weak dependency here causes a swaynag warning during the configuration load
Requires:       sway-wallpapers
# Lack of graphical drivers may hurt the common use case
Requires:       mesa-dri-drivers
# Logind needs polkit to create a graphical session
Requires:       polkit
# swaybg is used in the default config
Requires:       swaybg
# dmenu (as well as rxvt any many others) requires XWayland on Sway
Requires:       xorg-x11-server-Xwayland

# Sway binds the terminal shortcut to one specific terminal. In our case foot
Recommends:     foot
# grim is the recommended way to take screenshots on sway 1.0+
Recommends:     grim
# wmenu is the default launcher in sway
Recommends:     wmenu
# Install configs and scripts for better integration with systemd user session
Recommends:     sway-systemd
# Both utilities are suggested in the default configuration
Recommends:     swayidle
Recommends:     swaylock

# Minimal installation doesn't include Qt Wayland backend
Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

%description    config-upstream
Upstream configuration for Sway.
Includes all important dependencies for a typical desktop system
with minimal or no divergence from the upstream.


%package        config-minimal
RemovePathPostfixes:  .minimal
Summary:        Minimal configuration for Sway
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-config = %{version}-%{release}
Conflicts:      %{name}-config
# List of dependencies for headless or buildroot use

%description    config-minimal
Minimal configuration for Sway without any extra dependencies.
Suitable for headless or buildroot use.


# The artwork is heavy and we don't use it with our default config
%package        wallpapers
Summary:        Wallpapers for Sway
BuildArch:      noarch
License:        CC0-1.0

%description    wallpapers
Wallpaper collection provided with Sway


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -n %{name}-%{tag}
# apply unconditional patches
#autopatch -p1 -M99
# apply conditional patches

%build
%meson \
    -Dsd-bus-provider=libsystemd \
    -Dwerror=false
%meson_build

%install
%meson_install
# Install minimal configuration file
install -D -m644 -pv %{SOURCE100} %{buildroot}%{_sysconfdir}/sway/config.minimal
# Install portals.conf for xdg-desktop-portal
install -D -m644 -pv %{SOURCE101} %{buildroot}%{_datadir}/xdg-desktop-portal/sway-portals.conf
# install the documentation
install -D -m644 -pv README.md    %{buildroot}%{_pkgdocdir}/README.md
install -D -m644 -pv %{SOURCE102} %{buildroot}%{_pkgdocdir}/README.Fedora
# Create directory for extra config snippets
install -d -m755 -pv %{buildroot}%{_sysconfdir}/sway/config.d

%files
%license LICENSE
%doc %{_pkgdocdir}
%dir %{_sysconfdir}/sway
%dir %{_sysconfdir}/sway/config.d
%{_mandir}/man1/sway*
%{_mandir}/man5/*
%{_mandir}/man7/*
%caps(cap_sys_nice=ep) %{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/sway-portals.conf
%{bash_completions_dir}/sway*
%{fish_completions_dir}/sway*.fish
%{zsh_completions_dir}/_sway*

%files config-upstream
%config(noreplace) %{_sysconfdir}/sway/config
%{_datadir}/wayland-sessions/sway.desktop

%files config-minimal
%config(noreplace) %{_sysconfdir}/sway/config.minimal

%files wallpapers
%license assets/LICENSE
%{_datadir}/backgrounds/sway

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 08 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.11-1
- Update to 1.11 (#2361231)

* Sun Jan 26 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#2342139)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10-1
- Update to 1.10 (#2319183)

* Sun Oct 06 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10~rc2-1
- Update to 1.10-rc2

* Sun Sep 29 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10~rc1-1
- Update to 1.10-rc1

* Sun Sep 29 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.9-3
- Set Inhibit portal backend to 'none'

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 24 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.9-1
- Update to 1.9

* Sun Feb 04 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.9~rc2-1
- Update to 1.9-rc2 (rhbz#2260566)

* Sun Jan 14 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.1-4
- Use gnome-keyring for Secret portal implementation

* Thu Sep 14 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.1-3
- Add sway-portals.conf for xdg-desktop-portal >= 1.17

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 12 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1
- Set CAP_SYS_NICE on f38+

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 25 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8-1
- Update to 1.8

* Fri Dec 02 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8~rc1-1
- Update to 1.8-rc1
- Create two sway-config- packages with different sets of dependencies.
- Move sway.desktop to sway-config-upstream

* Mon Nov 14 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7-4
- Add upstream patch to fix crash in xdg-activation
- Convert license to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7-2
- Drop patches for wayland 1.19/meson 0.59 compatibility
- Split package with the default wallpapers
- Add upstream patch to fix crash in layer-shell code

* Sat Jan 22 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7-1
- Update to 1.7
- Add scripts from contrib to the package

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7~rc3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7~rc3-1
- Update to 1.7-rc3
- Change default terminal dependency to foot
- Disable `werror` to work around a couple of new warnings in GCC 12

* Mon Jan 10 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.6.1-4
- Add upstream patch to increase RLIMIT_NOFILE

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.6.1-2
- Rebuild for versioned symbols in json-c

* Thu Jun 24 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1
- Add Recommends: swayidle, swaylock
- Add upstream patch to fix pixman renderer init.

* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.6-1
- Update to 1.6 (#1939820)

* Sat Feb 20 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.1-3
- Recommend wayland backend for Qt
- Add subpackage for contrib/grimshot screenshot tool
- Add 'Recommend: sway-systemd'

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Thu Oct 22 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5-3
- Remove default terminal patching; alacritty is avaliable in Fedora (#1830595)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Aleksei Bavshin <alebastr89@gmail.com> - 1.5-1
- Update to 1.5
- Fix urxvt256c-ml dependency for f32+
- Add source verification
- Cleanup build dependencies

* Sat May 30 2020 Jan Pokorný <jpokorny@fedoraproject.org> 1.4-7
- Enhance greenfield readiness with optional pull of default driver set & xargs

* Thu Apr 30 2020 Aleksei Bavshin <alebastr89@gmail.com> - 1.4-6
- Add patch for layer-shell popups layer (#1829130)

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.4-5
- Rebuild (json-c)

* Wed Feb 26 2020 Aleksei Bavshin <alebastr89@gmail.com> - 1.4-4
- Fix default terminal and background

* Sun Feb 09 2020 Till Hofmann <thofmann@fedoraproject.org> - 1.4-3
- Add patch to fix strcmp on nullptr (upstream PR #4991)

* Fri Feb 07 2020 Jan Staněk <jstanek@redhat.com> - 1.4-2
- Apply upstream patch to allow compiling with -fno-common flag

* Thu Feb 06 2020 Joe Walker <grumpey0@gmail.com> 1.4-1
- Update to 1.4
- Added Build requires to pull in mesa-libEGL-devel manually

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Benjamin Lowry <ben@ben.gmbh> 1.2-3
- Uncomment 'Recommends: grim'

* Wed Sep 11 2019 Ivan Mironov <mironov.ivan@gmail.com> - 1.2-2
- Add patch to fix easily reproducible crash

* Thu Aug 29 2019 Jeff Peeler <jpeeler@redhat.com> - 1.2-1
- Update to 1.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1
- Add 'Requires: swaybg' (swaybg has been split from sway)
- Remove upstreamed patch

* Sun Mar 24 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.0-3
- Replace 'Requires: dmenu' by 'Recommends: dmenu'
- Re-enable manpages
- Remove cap_sys_ptrace, cap_sys_tty_config from sway binary
- Replace 'Requires: libinput' by 'BuildRequires: pkgconfig(libinput)'
- Replace 'BuildRequires: wlroots-devel' by 'BuildRequires: pkgconfig(wlroots)'

* Thu Mar 21 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.0-2
- Remove obsolete (and failing) call to %%make_install
- Fix directories without owner

* Mon Mar 18 2019 Jeff Peeler <jpeeler@redhat.com> - 1.0-1
- Update to 1.0 (without man pages)

* Thu Feb 07 2019 Björn Esser <besser82@fedoraproject.org> - 0.15.2-3
- Add patch to disable -Werror, fixes FTBFS

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.15.2-1
- Update to stable release 0.15.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.15.1-3
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Till Hofmann <thofmann@fedoraproject.org> - 0.15.1-1
- Update to 0.15.1
- Remove upstreamed patch (upstream PR #1517)

* Thu Dec 14 2017 Björn Esser <besser82@fedoraproject.org> - 0.15.0-4
- Add upstream patch fixing issues with json-c

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.15.0-3
- Rebuilt for libjson-c.so.3

* Sat Nov 11 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.0-2
- Bump for wlc rebuild

* Fri Nov 10 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.0-1
- update to stable 0.15.0

* Tue Oct 10 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.0-0.3.rc1
- Rebuild for fix for #1388
- fix versioning according to guidelines

* Mon Oct 09 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.rc1-1
- Update to 0.15.0-rc1
- remove patch
- fix sources link

* Thu Oct 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.14.0-3
- Fix freezing

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Aug 02 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.14.0-1
- Update to 0.14.0
- add libinput as dependency
- add dbus as build dependency for tray icon support
- remove -Wno-error flag

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Mon Apr 03 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Wed Mar 15 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Wed Mar 08 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12-1
- Update to 0.12

* Tue Feb 28 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12-0.rc2
- Update to 0.12-rc2

* Sat Feb 25 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12-0.rc1
- Update to 0.12-rc1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7.gitb3c0aa3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-6.gitb3c0aa3
- Update to HEAD

* Thu Jan 12 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-5
- Fix bug #1008 with backported patch

* Thu Dec 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-4
- Set ptrace capability for sway

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-3
- Fix LD_LIBRARY_PATH

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-2
- Fix bug #971 with backported patch

* Tue Dec 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-1
- Update to 0.11

* Sun Dec 18 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-0.rc3
- Update to 0.11-rc3

* Sat Dec 17 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-0.rc2
- Update to 0.11-rc2

* Sat Nov 26 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-2
- Require Xwayland instead of just suggesting it, since at the moment is needed by dmenu (and other)

* Wed Oct 26 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-1
- Update to 0.10

* Thu Oct 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-0.1.rc3
- Update to 0.10-rc3

* Tue Oct 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-0.1.rc2
- Update to 0.10-rc2

* Wed Sep 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-0.1.rc1
- Update to 0.10-rc1

* Tue Sep 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-4
- Do not Require the urxvt shell
- Rebuild due to a wlc rebuild
- Add Recommends ImageMagick

* Wed Aug 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-3
- Remove some compilation flags that were not needed

* Sun Aug 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-2
- Add dmenu dependency
- Add rxvt-unicode-256color-ml dependency
- Use urxvt256c-ml instead of urxvt by default
- Improve default wallpaper
- Add suggests xorg-x11-server-Xwayland

* Wed Aug 03 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-1
- Upgrade to 0.9

* Thu Jul 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.8-2
- Move ffmpeg and ImageMagick from Required to Suggested

* Thu Jul 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.8-1
- Update to version 0.8
- Re-enable ZSH bindings
- Remove sway wallpapers

* Sun May 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.7-1
- Update to version 0.7
- Drop ZSH bindings that are no longer shipped with Sway

* Thu May 05 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.6-1
- Update to current upstream version

* Wed Apr 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3-1
- Update to current upstream version

* Sun Feb 14 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0-1.20160214git016a774
- Initial packaging
