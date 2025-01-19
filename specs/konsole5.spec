# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

%global  base_name konsole

Name:    konsole5
Summary: KDE Terminal emulator
Version: 23.08.5
Release: 4%{?dist}

# sources: MIT and LGPLv2 and LGPLv2+ and GPLv2+
License: GPL-2.0-only AND GFDL-1.1-or-later
URL:     http://www.kde.org/applications/system/konsole/
#URL:    http://konsole.kde.org/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

## upstreamable patches

## upstream patches
# 21.08 branch fixes

## downstream patches
Patch200: konsole-history_location_default.patch
# custom konsolerc that sets default to cache as well
Source10: konsolerc

Obsoletes: konsole < 14.12
Provides:  konsole = %{version}-%{release}

%global maj_ver %(echo %{version} | cut -d. -f1)

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Bookmarks)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5NewStuffCore)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Pty)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: libappstream-glib
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: libicu-devel

%if 0%{?tests}
BuildRequires: appstream
BuildRequires: xorg-x11-server-Xvfb dbus-x11
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: keditbookmarks

%description
%{summary}.

%package part
Summary: Konsole5 kpart plugin
%description part
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf5 \
  %{?flatpak:-DINSTALL_ICONS:BOOL=ON} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build


%install
%cmake_install

install -m644 -p -D %{SOURCE10} %{buildroot}%{_kf5_sysconfdir}/xdg/konsolerc

%find_lang konsole --with-html

# add startupWMClass=konsole if not already present
grep 'StartupWMClass=' %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop >& /dev/null || \
desktop-file-edit --set-key=StartupWMClass --set-value=konsole %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.konsole.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop
%if 0%{?tests}
test "$(xvfb-run -a %{_target_platform}/src/konsole --version)" = "konsole %{version}" ||:
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 30" ||:
%endif


%files -f konsole.lang
%dir %{_kf5_datadir}/knsrcfiles/
%doc README*
%config(noreplace) %{_kf5_sysconfdir}/xdg/konsolerc
%{_kf5_datadir}/konsole/
%{_kf5_bindir}/konsole
%{_kf5_bindir}/konsoleprofile
%{_kf5_datadir}/applications/org.kde.konsole.desktop
%{_kf5_datadir}/kglobalaccel/org.kde.konsole.desktop
%{_kf5_datadir}/kconf_update/konsole.upd
%{_kf5_datadir}/kconf_update/konsole_add_hamburgermenu_to_toolbar.sh
%{_kf5_datadir}/kio/servicemenus/konsolerun.desktop
%{_kf5_datadir}/knotifications5/konsole.notifyrc
%{_kf5_datadir}/knsrcfiles/konsole.knsrc
%{_kf5_datadir}/kservicetypes5/terminalemulator.desktop
%{_kf5_datadir}/qlogging-categories5/konsole.*
%{_kf5_datadir}/zsh/site-functions/_konsole
%{_kf5_libdir}/kconf_update_bin/konsole_globalaccel
%{_kf5_libdir}/kconf_update_bin/konsole_show_menubar
%{_kf5_metainfodir}/org.kde.konsole.appdata.xml
%if 0%{?flatpak}
%{_kf5_datadir}/icons/hicolor/*/apps/utilities-terminal.*
%endif

%ldconfig_scriptlets part

%files part
%{_kf5_libdir}/libkonsoleapp.so.*
%{_kf5_libdir}/libkonsoleprivate.so.*
%{_kf5_qtplugindir}/konsolepart.so
%{_kf5_qtplugindir}/konsoleplugins/
%{_kf5_datadir}/kservices5/konsolepart.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 23.08.5-3
- Rebuild for ICU 76

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 24 2024 Alessandro Astone <ales.astone@gmail.com> - 23.08.5-1
- 23.08.5

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 23.08.4-5
- Rebuild for ICU 74

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 Marie Loise Nolden <loise@kde.org> - 23.08.4-2
- Update to 23.08.4-2 to be on par with f39 and co-installability

* Sun Dec 03 2023 Alessandro Astone <ales.astone@gmail.com> - 23.08.3-1
- Update to 23.08.3
- Restore upstream config that defaults to hiding the menu bar
- Make konsole5-part co-installable with konsole-part from Plasma 6

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 23.04.3-2
- Rebuilt for ICU 73.2

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Mon Feb 20 2023 Than Ngo <than@redhat.com> - 22.12.2-2
- migrated to SPDX license

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 22.12.0-2
- Rebuild for ICU 72

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- Update to 22.04.3

* Thu Jun 23 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- Update to 22.04.2

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Wed Feb 02 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Thu Dec 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Fri Oct 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Thu Aug 19 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.0-2
- 21.08 branch fixes

* Fri Aug 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.0-1
- 21.08.0

* Mon Aug 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.07.90-1
- 21.07.90
- backport https://invent.kde.org/utilities/konsole/-/merge_requests/447

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Mon Jul 26 2021 Rex Dieter <rdieter@fedoraproject.org> 21.04.2-3
- backport fix for initial konsole size
- fix changelog to be rhel-friendly

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2
- revert revert, causes other side-effects

* Wed Jun 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-3
- revert upstream commit causing sizing regresssion (kde#437791)

* Tue May 25 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-2
- pull in upstream crashfix

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Sat Apr 17 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Tue Mar 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Tue Feb 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.1-1
- 20.12.1

* Wed Nov  4 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Mon Aug 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Tue May 26 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Thu Apr 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Thu Mar 05 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Sat Sep 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.1-1
- 19.08.1

* Tue Aug 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.0-1
- 19.08.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.1-1
- 19.04.1

* Thu Apr 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-2
- Crashes When Logging Out All Tabs in a Window Using "Copy Input To" Feature (#1657013,kde#405158)

* Thu Mar 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Sat Dec 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Tue Oct 30 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-2
- add StartupWMClass=konsole (kde#372441)

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Fri Sep 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Wed Aug 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.0-1
- 18.08.0

* Thu Jul 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Tue Jun 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Tue May 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Sat Apr 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0
- Requires: keditbookmarks (#1565758)

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Wed Feb 28 2018 Sandro Mani <manisandro@gmail.com> - 17.12.2-2
- Add konsole_REP.patch (fixes drawing issues with ncurses applications)

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.2-1
- 17.08.2

* Sat Sep 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Sat Aug 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.0-1
- 17.08.0

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Wed May 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Sat Apr 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.0-2
- use %%find_lang for html handbooks too

* Tue Apr 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.0-1
- 17.04.0

* Wed Mar 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Wed Feb 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Tue Jan 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Thu Dec 22 2016 Rex Dieter <rdieter@math.unl.edu> - 16.12.0-1
- 16.12.0

* Wed Nov 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Tue Sep 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-2
- Konsole title does not update to current program or host run (#1379753)

* Tue Sep 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-1
- 16.07.90

* Fri Jul 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-2
- %%check: drop use of 'time', not needed

* Fri Jul 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Thu Jul 07 2016 Rex Dieter <rdieter@fedoraproject.org> 16.04.3-1
- 16.04.3

* Thu Jun 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-2
- update URL (use www.kde.org/applications/...)

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Tue May 31 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-2
- backport upstream fixes

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Thu Apr 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-2
- enable tests, support %%base_name, %%bootstrap

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-2
- TERM=xterm-256color default (#1172329)

* Sun Mar 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.1-2
- "Terminal Size" setting in profile ignored (#345403)
- cleanup, validate appdata

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.1-1
- 15.12.1

* Mon Dec 14 2015 Rex Dieter <rdieter@fedoraproject.org> 15.12.0-1
- 15.12.0

* Thu Nov 12 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.3-1
- 15.08.3
- use %%license
- backport support for FileLocation UI (default: cache)

* Wed Sep 16 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.1-1
- 15.08.1

* Wed Aug 26 2015 Daniel Vrátil <dvratil@redhat.com> - 15.08.0-1
- 15.08.0

* Sat Aug 15 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.3-2
- fix 'konsole --version' to match reality
- backport copy-n-paste fixes (#1235024)

* Tue Jun 30 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.3-1
- 15.04.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.2-1
- 15.04.2

* Mon Jun 01 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.1-2
- +%%{?kf5_kinit_requires}

* Fri May 15 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.1-1
- 15.04.1

* Fri May 15 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-2
- store history in cachedir instead of tmp (#1222061,kde#173283)

* Tue Apr 14 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.0-1
- 15.04.0

* Sat Jan 31 2015 Rex Dieter <rdieter@fedoraproject.org>  14.12.1-1
- kf5-based konsole-14.12.x

