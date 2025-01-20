Name: qtile
Version: 0.29.0
Release: 4%{?dist}
Summary: A pure-Python tiling window manager
Source: https://github.com/qtile/qtile/archive/v%{version}/qtile-%{version}.tar.gz

# Everything licensed under MIT except for the following files.
# GPL-3.0-or-later:
#   libqtile/widget/cmus.py
#   libqtile/widget/moc.py
License: MIT AND GPL-3.0-or-later
Url: http://qtile.org

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

# Test dependencies
BuildRequires:  gcc
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  rsvg-pixbuf-loader
BuildRequires: (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)
# https://github.com/qtile/qtile/issues/4830
BuildRequires: python3-isort

# Some dependencies are loaded with ffi.dlopen, and to declare them properly
# we'll need this suffix.
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

BuildRequires: libgobject-2.0.so.0%{libsymbolsuffix}
BuildRequires: libpango-1.0.so.0%{libsymbolsuffix}
BuildRequires: libpangocairo-1.0.so.0%{libsymbolsuffix}
Requires: libgobject-2.0.so.0%{libsymbolsuffix}
Requires: libpango-1.0.so.0%{libsymbolsuffix}
Requires: libpangocairo-1.0.so.0%{libsymbolsuffix}

# Recommended packages for widgets
Recommends: python3-psutil
Recommends: python3-pyxdg
Recommends: python3-dbus-next
Recommends: python3-xmltodict
Recommends: python3-dateutil
Recommends: python3-mpd2
Recommends: python3-pulsectl
Recommends: python3-pulsectl-asyncio

Requires: python3-libqtile = %{version}-%{release}


%description
A pure-Python tiling window manager.

Features
========

    * Simple, small and extensible. It's easy to write your own layouts,
      widgets and commands.
    * Configured in Python.
    * Command shell that allows all aspects of
      Qtile to be managed and inspected.
    * Complete remote scriptability - write scripts to set up workspaces,
      manipulate windows, update status bar widgets and more.
    * Qtile's remote scriptability makes it one of the most thoroughly
      unit-tested window mangers around.


%package -n python3-libqtile
Summary: Qtile's python library


%description -n python3-libqtile
%{summary}.


%package wayland
Summary: Qtile wayland session
BuildRequires: xorg-x11-server-Xwayland
Requires: qtile = %{version}-%{release}
Requires: python3-libqtile+wayland = %{version}-%{release}


%description wayland
%{summary}.


%pyproject_extras_subpkg -n python3-libqtile wayland


%prep
%autosetup -p 1


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x test,wayland


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
PYTHONPATH=${PWD} ./scripts/ffibuild


%install
%pyproject_install
%pyproject_save_files libqtile

mkdir -p %{buildroot}%{_datadir}/xsessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/xsessions/ \
    resources/qtile.desktop

mkdir -p %{buildroot}%{_datadir}/wayland-sessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/wayland-sessions/ \
    resources/qtile-wayland.desktop


%check
# The tests can sometimes randomly fail. Rebuilding the package again usually
# solves the issue. Please see the upstream issue:
# https://github.com/qtile/qtile/issues/4573
%ifnarch s390x ppc64le
# The test_chord_widget is broken on Rawhide (F41)
# https://github.com/qtile/qtile/issues/4930
%pytest -vv --backend x11 --backend wayland -k "not test_chord_widget"
%endif


%files
%doc README.rst
%{_bindir}/qtile
%{_datadir}/xsessions/qtile.desktop


%files -n python3-libqtile -f %{pyproject_files}


%files wayland
%{_datadir}/wayland-sessions/qtile-wayland.desktop


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 19 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-3
- Recommend python3-pulsectl-asyncio for the PulseVolume widget

* Mon Dec 02 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-2
- Recommend python3-pulsectl for the PulseVolume widget

* Wed Oct 30 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-1
- New upstream version

* Wed Aug 21 2024 Jakub Kadlcik <frostyx@email.cz> - 0.28.1-1
- New upstream version

* Sat Jul 20 2024 Jakub Kadlcik <frostyx@email.cz> - 0.27.0-2
- Skip a broken test (test_chord_widget)

* Sat Jul 13 2024 Jakub Kadlcik <frostyx@email.cz> - 0.27.0-1
- New upstream version
- Use pkgconfig for wlroots dependency

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.26.0-2
- Rebuilt for Python 3.13

* Thu May 23 2024 Jakub Kadlcik <frostyx@email.cz> - 0.26.0-1
- Upgrade to the new upstream version

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 Jakub Kadlcik <frostyx@email.cz> - 0.23.0-6
- Exclude ix86
- Specify required wlroots version
- Skip tests on s390x and ppc64le

* Mon Nov 13 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.23.0-5
- Fix ffibuild to enable wayland subpackages

* Fri Nov 10 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.23.0-4
- Add python3-libqtile, qtile-wayland, and python3-libqtile+wayland subpackages

* Fri Nov 10 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.23.0-3
- Remove manual dependencies that duplicate generated ones
- Remove temporary python3-cairocffi dependencies
- Remove duplicate %%pyproject_buildrequires
- Buildrequire rsvg-pixbuf-loader for SVG image loading during the test suite
- Remove unnecessary buildrequires
- Correct wayland recommends

* Sat Nov 04 2023 Jakub Kadlcik <frostyx@email.cz> - 0.23.0-2
- Remove noarch
- Only optional dependency on xorg-x11-server-Xwayland

* Tue Oct 10 2023 Jakub Kadlcik <frostyx@email.cz> - 0.23.0-1
- Upgrade to the new upstream version

* Sun Jan 01 2023 Jakub Kadlcik <frostyx@email.cz> - 0.22.1-4
- Use Source0 from GitHub instead of PyPI
- Remove Source1
- Don't use _description macro
- Use desktop-file-install instead of desktop-file-validate
- Run tests with --backend wayland
- Specify some dependencies missing from python3-cairocffi
- Automatically generate wayland dependencies
- Remove explicit license file

* Wed Dec 21 2022 Jakub Kadlcik <frostyx@email.cz> - 0.22.1-3
- Run desktop-file-validate in the check section

* Tue Dec 20 2022 Jakub Kadlcik <frostyx@email.cz> - 0.22.1-2
- Use autosetup macro
- SPDX license expression and changed license docstring
- Add check section and run tests
- Use 2021+ python package format
- Add bcond for wayland, not all dependencies are in Fedora yet

* Thu Sep 22 2022 Jakub Kadlcik <frostyx@email.cz> - 0.22.1-1
- Upgrade to the new upstream version

* Tue Jun 14 2022 Jakub Kadlcik <frostyx@email.cz> - 0.21.0-2
- Install Qtile session file from upstream
- Install Qtile Wayland session file
- Recommend Wayland-specific dependencies on Fedora 36

* Wed Mar 23 2022 Jakub Kadlcik <frostyx@email.cz> - 0.21.0-1
- Upgrade to the new upstream version

* Sat Feb 26 2022 Jakub Kadlcik <jkadlcik@redhat.com> - 0.20.0-2
- Recommend packages needed by widgets

* Mon Jan 24 2022 Jakub Kadlcik <jkadlcik@redhat.com> - 0.20.0-1
- Upgrade to the new upstream version

* Wed Jan 05 2022 Jakub Kadlcik <jkadlcik@redhat.com> - 0.19.0-1
- Upgrade to the new upstream version

* Thu Nov 18 2021 Jakub Kadlčík <jkadlcik@redhat.com> - 0.18.1-2
- Add missing runtime dependency to python3-dbus-next

* Wed Nov 17 2021 Jakub Kadlčík <jkadlcik@redhat.com> - 0.18.1-1
- Update to the new upstream version
- Use source from PyPI
- Temporarily drop manpage because I don't know where to get it

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-2
- Rebuilt for Python 3.9

* Mon Feb 03 2020 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.14.2-1
- Update to latest release
- Remove buildrequires python-nose-cov

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.13.0-1
- !!! deprecation warning !!!
-   wmii layout is deprecated in terms of columns layout, which has the
-   same behavior with different defaults, see the wmii definition for
-   more details
- * features
-   add svg handling for images
-   allow addgroup command to set the layout
-   add command to get current log level
-   allow groupbox to hide unused groups
-   add caps lock indicator widget
-   add custom_command to check_update widget
- * bugfixes
-   better shutdown handling
-   fix clientlist current client tracking
-   fix typo in up command on ratiotile layout
-   various fixes to check_update widget
-   fix 0 case for resize screen

* Wed Jul 18 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.12.0-1
- !!! Config breakage !!!
-   Tile layout commands up/down/shuffle_up/shuffle_down changed to be
-   more consistent with other layouts
-   move qcmd to qtile-cmd because of conflict with renameutils, move
-   dqcmd to dqtile-cmd for symmetry
- add `add_after_last` option to Tile layout to add windows to the end of the list
- add new formatting options to TaskList
- allow Volume to open app on right click
- fix floating of file transfer windows and java drop-downs
- fix exception when calling `cmd_next` and `cmd_previous` on layout without windows
- fix caps lock affected behaviour of key bindings
- re-create cache dir if it is deleted while qtile is running
- fix CheckUpdates widget color when no updates
- handle cases where BAT_DIR does not exist
- fix the wallpaper widget when using `wallpaper_command`
- fix Tile layout order to not reverse on reset
- fix calling `focus_previous/next` with no windows* Wed Jul 18 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.12.0-1
- !!! Config breakage !!!
-   Tile layout commands up/down/shuffle_up/shuffle_down changed to be
-   more consistent with other layouts
-   move qcmd to qtile-cmd because of conflict with renameutils, move
-   dqcmd to dqtile-cmd for symmetry
- add `add_after_last` option to Tile layout to add windows to the end of the list
- add new formatting options to TaskList
- allow Volume to open app on right click
- fix floating of file transfer windows and java drop-downs
- fix exception when calling `cmd_next` and `cmd_previous` on layout without windows
- fix caps lock affected behaviour of key bindings
- re-create cache dir if it is deleted while qtile is running
- fix CheckUpdates widget color when no updates
- handle cases where BAT_DIR does not exist
- fix the wallpaper widget when using `wallpaper_command`
- fix Tile layout order to not reverse on reset
- fix calling `focus_previous/next` with no windows

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-3
- Rebuilt for Python 3.7
- Don't require trollius (only needed on Python < 3.4)

* Wed Mar 28 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.11.1-2
- Add unpackaged files %#{_bindir}/dqcmd %#{_bindir}/qcmd

* Wed Feb 28 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.11.1-1
- !!! Completely changed extension configuration, see the documentation !!!
- !!! `extention` subpackage renamed to `extension` !!!
- !!! `extentions` configuration variable changed to `extension_defaults` !!!
- qshell improvements
- new MonadWide layout
- new Bsp layout
- new pomodoro widget
- new stock ticker widget
- new `client_name_updated` hook
- new RunCommand and J4DmenuDesktop extension
- task list expands to fill space, configurable via `spacing` parameter
- add group.focus_by_name() and group.info_by_name()
- add disk usage ratio to df widget
- allow displayed group name to differ from group name
- enable custom TaskList icon size
- add qcmd and dqcmd to extend functionality around qtile.command functionality
- add ScratchPad group that has configurable drop downs
- fix race condition in Window.fullscreen
- fix for string formatting in qtile_top
- fix unicode literal in tasklist
- move mpris2 initialization out of constructor
- fix wlan widget variable naming and division
- normalize behavior of layouts on various commands
- add better fallback to default config
- update btc widget to use coinbase
- fix cursor warp when using default layout implementation
- don't crash when using widget with unmet dependencies
- fix floating window default location

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.10.7-1
- new MPD widget, widget.MPD2, based on `mpd2` library
- add option to ignore duplicates in prompt widget
- add additional margin options to GroupBox widget
- add option to ignore mouse wheel to GroupBox widget
- add `watts` formatting string option to Battery widgets
- add volume commands to Volume widget
- add Window.focus command


* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.6-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 25 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.6-1
- Add `startup_complete` hook
- Restore dynamic groups on restart
- Major bug fixes with floating window handling

* Fri Mar 04 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.5-1
- Python 3.2 support dropped !!!
- GoogleCalendar widget dropped for KhalCalendar widget !!!
- qtile-session script removed in favor of qtile script !!!
- new Columns layout, composed of dynamic and configurable columns of windows
- new iPython kernel for qsh, called iqsh, see docs for installing
- new qsh command `display_kb` to show current key binding
- add json interface to IPC server
- add commands for resizing MonadTall main panel
- wlan widget shows when you are disconnected and uses a configurable format
- fix path handling in PromptWidget
- fix KeyboardLayout widget cycling keyboard
- properly guard against setting screen to too large screen index

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.4-2
- Fix rpmlint issues

* Tue Jan 19 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.4-1
- New release

* Fri Dec 25 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.3-1
- New upstream release

* Fri Nov 20 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-5
- Build against new python-xcffib

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 21 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-3
- Fix minor issue with spec file.

* Tue Oct 20 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-2
- /usr/bin/qtile-top to files list

* Tue Oct 20 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-1
- Update to latest upstream

* Mon Oct 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.1-1
- Fix soname issue

* Mon Aug 03 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.1-0
- Update to latest upstream

* Mon Aug 03 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-4
- Use Python3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 22 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-2
- Final update to licensing

* Sat Feb 14 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-1
- Update for new upstream release
- Fix license headers.

* Sun Feb 01 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.0-2
- Update spec for qtile-0.9.0
- Include in Fedora.

* Wed Oct 08 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.8.0-1
- Initial packaging
- Spec based on python-nose
