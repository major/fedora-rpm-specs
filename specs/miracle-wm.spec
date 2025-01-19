%global miral_ver 5.1
%global miroil_ver 5.0
%global mirversion 2.19

Name:           miracle-wm
Version:        0.4.0
Release:        2%{?dist}
Summary:        A tiling Wayland compositor based on Mir

License:        GPL-3.0-or-later and MIT
URL:            https://github.com/miracle-window-manager/miracle-wm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig(miral) >= %{miral_ver}
BuildRequires:  pkgconfig(miroil) >= %{miroil_ver}
BuildRequires:  pkgconfig(mirrenderer) >= %{mirversion}
BuildRequires:  pkgconfig(mirplatform) >= %{mirversion}
BuildRequires:  pkgconfig(mircommon) >= %{mirversion}
BuildRequires:  pkgconfig(mirwayland) >= %{mirversion}
BuildRequires:  pkgconfig(mircommon-internal) >= %{mirversion}
BuildRequires:  pkgconfig(mirserver-internal) >= %{mirversion}
BuildRequires:  pkgconfig(mirserver-internal) >= %{mirversion}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  cmake(nlohmann_json) >= 3.2.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  cmake(gtest)
BuildRequires:  libxkbcommon-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pcre2
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  glm-devel
BuildRequires:  boost-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  systemd-rpm-macros

%description
miracle-wm is a Wayland compositor based on Mir. It features a tiling window
manager at its core, very much in the style of i3 and sway. The intention is
to build a compositor that is flashier and more feature-rich than either of
those compositors, like swayfx.

%prep
%autosetup -S git_am


%build
%cmake -DSYSTEMD_INTEGRATION=ON
%cmake_build


%install
%cmake_install


%check
%{_vpath_builddir}/bin/miracle-wm-tests


%files
%{_bindir}/miracle-wm
%{_bindir}/miracle-wm-sensible-terminal
%{_bindir}/miracle-wm-session
%{_bindir}/miraclemsg
%{_libexecdir}/miracle-wm-session-setup
%{_datarootdir}/wayland-sessions/miracle-wm.desktop
%{_userunitdir}/miracle-wm*
%license LICENSE
%license miraclemsg/LICENSE.sway session/LICENSE.sway-systemd


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Matthew Kosarek <matthew@matthewkosarek.xyz> - 0.4.0-1
- Update to 0.4.0

* Mon Dec 02 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.3.7-3
- Rebuild for Mir 2.19

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 0.3.7-2
- Rebuild for yaml-cpp 0.8

* Tue Oct 22 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7

* Tue Oct 01 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.3.6-2
- Fix miral and miroil versioned BRs

* Wed Sep 25 2024 Matthew Kosarek <matthew@matthewkosarek.xyz> - 0.3.6-1
- Update to 0.3.6

* Mon Sep 09 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5
- Enable systemd session
- Drop upstreamed patches

* Tue Sep 03 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.3.4-3
- Backport miraclemsg

* Wed Aug 28 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.3.4-2
- Backport fix for initializing default config

* Tue Aug 27 2024 Matthew Kosarek <matthew@matthewkosarek.xyz> - 0.3.4-1
- Update to 0.3.4

* Tue Aug 13 2024 Matthew Kosarek <matthew@matthewkosarek.xyz> - 0.3.2-1
- Adjustment so that we're no longer building against the dev release of Mir

* Mon Aug 12 2024 Matthew Kosarek <matthew@matthewkosarek.xyz> - 0.3.1-1
- snap: update to v0.3.0 by @mattkae in https://github.com/mattkae/miracle-wm/pull/187
- test + refactor: renames to more closely match i3, refactor to accomodate testing of the TilingWindowTree, initial tests for the tiling window tree by @mattkae in https://github.com/mattkae/miracle-wm/pull/189
- minor: rename master to develop because master is not the mastered version in this context by @mattkae in https://github.com/mattkae/miracle-wm/pull/190
- refactor: establish a single source of truth for the selected window by @mattkae in https://github.com/mattkae/miracle-wm/pull/192
- refactor: giving Window modification control over to the Workspace instead of the Output by @mattkae in https://github.com/mattkae/miracle-wm/pull/193
- refactor: make it so that the tiling window tree relies on the active window much less by @mattkae in https://github.com/mattkae/miracle-wm/pull/194
- refactor: remove `WindowMetadata` and make everything a container + refactor `Output` and `Workspace` big time such that they do way less work by @mattkae in https://github.com/mattkae/miracle-wm/pull/195
- bugfix: fixing how modes are reported and multi-subscriptions are created by @mattkae in https://github.com/mattkae/miracle-wm/pull/199
- bugfix: no longer relying on the Output to get the compositor state by @mattkae in https://github.com/mattkae/miracle-wm/pull/200
- refactor: a Container is used as the active element instead of a miral::Window by @mattkae in https://github.com/mattkae/miracle-wm/pull/201
- Allow using custom mir libraries directory by @TibboddiT in https://github.com/mattkae/miracle-wm/pull/198
- feature: swaymsg exit works now by @mattkae in https://github.com/mattkae/miracle-wm/pull/203
- feature: no longer restarting commands that exit with 127 by @mattkae in https://github.com/mattkae/miracle-wm/pull/204
- feature: if the configuration doesn't exist, we try to copy it from /usr/share/miracle-wm/config/default.yaml or we write it blank by @mattkae in https://github.com/mattkae/miracle-wm/pull/205

* Mon Jul 29 2024 Matthew Kosarek <matt.kosarek@canonical.com> - 0.3.0-1
- bugfix: temporary fix for #24 while we consider it in the Mir project by @mattkae in https://github.com/mattkae/miracle-wm/pull/112
- (#113) bugfix: fullscreen windows no longer get their rectangle set if one is pending by @mattkae in https://github.com/mattkae/miracle-wm/pull/114
- feature: supporting the i3 focus command by @mattkae in https://github.com/mattkae/miracle-wm/pull/116
- feature: displaying a border around windows by @mattkae in https://github.com/mattkae/miracle-wm/pull/103
- feature: animation groundwork + window movement animation by @mattkae in https://github.com/mattkae/miracle-wm/pull/121
- feature: configurable animations + animation for window opening + multiple ease functions by @mattkae in https://github.com/mattkae/miracle-wm/pull/125
- feature: workspace switching animations by @mattkae in https://github.com/mattkae/miracle-wm/pull/128
- epic: animations, animations, and animations! by @mattkae in https://github.com/mattkae/miracle-wm/pull/127
- feature + testing: animation testing refactor + slide animation now includes a scale + improving workspace transforms + constraining less often by @mattkae in https://github.com/mattkae/miracle-wm/pull/130
- snap: upgrade to core24 by @mattkae in https://github.com/mattkae/miracle-wm/pull/129
- (#131 #132 #133) bugfix: clipped windows now behave properly when being animated by @mattkae in https://github.com/mattkae/miracle-wm/pull/135
- refactor: move ProgramFactory to its own file + clang-tidy issues around the renderer by @mattkae in https://github.com/mattkae/miracle-wm/pull/139
- bugfix: unset CMAKE_CXX_COMPILER by @pastalian in https://github.com/mattkae/miracle-wm/pull/138
- feature: support for i3 'exec' command by @mattkae in https://github.com/mattkae/miracle-wm/pull/140
- feature: implementation if the i3 'split' command by @mattkae in https://github.com/mattkae/miracle-wm/pull/142
- feature: support for the i3 'move' command by @mattkae in https://github.com/mattkae/miracle-wm/pull/143
- feature: support for i3 'sticky' command by @mattkae in https://github.com/mattkae/miracle-wm/pull/145
- (#136) bugfix: interpolating first slide animation from the current position by @mattkae in https://github.com/mattkae/miracle-wm/pull/146
- (#147) bugfix: workspace animations are now interpolated + border respecting workspace transforms + massive simplification of workspace transformation code by @mattkae in https://github.com/mattkae/miracle-wm/pull/148
- refactor: resizing is now global instead of local to a particular output by @mattkae in https://github.com/mattkae/miracle-wm/pull/150
- frankenstein: borders disappearing bug for floating windows + percentage not being clamped on animations + IPC_GET_VERSION + IPC_GET_BINDING_MODES + IPC_GET_BINDING_STATE + IPC_GET_OUTPUTS by @mattkae in https://github.com/mattkae/miracle-wm/pull/153
- (#122) bugfix: border rendering no longer throws GL error 1281 by @mattkae in https://github.com/mattkae/miracle-wm/pull/155
- (#156) bugfix: place fullscreen windows properly by @mattkae in https://github.com/mattkae/miracle-wm/pull/159
- bugfix: XWayland windows some times become unclickable by @mattkae in https://github.com/mattkae/miracle-wm/pull/167
- (#166) XWayland windows now have a proper Z-order so that they don't step on each other's toes by @mattkae in https://github.com/mattkae/miracle-wm/pull/170
- bugfix: handling initially fullscreen windows + allowing workspaces to be floating by default + allowing windows to be floating initially + fixes for #168 by @mattkae in https://github.com/mattkae/miracle-wm/pull/171
- bugfixes: select on hover always + release builds for debian & snap + fix for for #174 when we have zero monitors by @mattkae in https://github.com/mattkae/miracle-wm/pull/176
- (#4) bugfix: gedit save dialog no longer appears as a tile + removing some dead code + mild refactor and debugging by @mattkae in https://github.com/mattkae/miracle-wm/pull/177
- (#178) bugfix: fix for menus no longer being selectable + being able to allocate a floating window as the initial window by @mattkae in https://github.com/mattkae/miracle-wm/pull/179
- bugfix: need libnotify4 in stage packages by @mattkae in https://github.com/mattkae/miracle-wm/pull/182
- (#97) bugfix: preventing some windows (e.g. emacs) from deciding on too small of size for their tile by @mattkae in https://github.com/mattkae/miracle-wm/pull/184
- Fix compile with glm 1.0.0+ and musl libc by @JamiKettunen in https://github.com/mattkae/miracle-wm/pull/185

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 15 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.2.1-2
- Rebuild for Mir 2.17

* Tue Apr 23 2024 Matthew Kosarek <matt.kosarek@canonical.com> - 0.2.1-1
- Release for the deb and Fedora packages

* Mon Apr 22 2024 Matthew Kosarek <matt.kosarek@canonical.com> - 0.2.0-1
- (#35) sway/i3 IPC support has been implemented to minimally support waybar
- (#45) Added "floating window manager" support whereby individual windows can be made to float above the tiling grid and behave just as they would in a "traditional" floating window manager
- (#38) The user configuration now automatically reloads when a change is made to it
- (#37) A terminal option can now be specified in the configuration to decide which terminal is opened up by the keybind. We also do a much better job of deciding on a sane default terminal
- Environment variables can now be specified in the configuration (e.g. I needed to set mesa_glthread=false to prevent a bunch of screen tearing on my new AMD card)
- Upgrade to Mir v2.16.4 which brought in a few important bugfixes for miracle-wm
- (#48) Fullscreened windows are now guaranteed to be on top
- (#34) Fixed a bug where panels could not be interacted with
- (#50) Keyboard events are now properly consumed when a workspace switch happens
- (#61) Outer gaps no longer include inner gaps
- (#66) Disabled moving fullscreen windows between workspaces
- (#67) Fixed a bug where resizing a window over and over again would make it progressively tinier due to rounding errors
- Refactored the tiling window system in a big way for readability. This solved a number of tricky bugs in the process so I am very happy about it
- (#81) Gaps algorithm no longer leaves some nodes smaller than others
- The project finally has meaningful tests with many more to come 🧪

* Mon Apr 01 2024 Matthew Kosarek <matt.kosarek@canonical.com> - 0.1.0-1
- Initial version
