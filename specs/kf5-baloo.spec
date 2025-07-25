%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%global framework baloo

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Summary: A Tier 3 KDE Frameworks 5 module that provides indexing and search functionality
Version: 5.116.0
Release: 4%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-or-later
URL:     https://community.kde.org/Baloo
#URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

Source1:        97-kde-baloo-filewatch-inotify.conf
# shutdown script to explictly stop baloo_file on logout
# Now that baloo supports systemd user unit, this can probably be dropped -- rex
Source2:        baloo_file_shutdown.sh

## upstreamable patches
# http://bugzilla.redhat.com/1235026
Patch100: baloo-5.67.0-baloofile_config.patch

## upstream patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kcrash-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kfilemetadata-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kidletime-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  kf5-solid-devel >= %{majmin}

BuildRequires:  lmdb-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

# for systemd-related macros
BuildRequires:  systemd

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Obsoletes:      kf5-baloo-tools < 5.5.95-1
Provides:       kf5-baloo-tools = %{version}-%{release}

%if 0%{?fedora}
Obsoletes:      baloo < 5
Provides:       baloo = %{version}-%{release}
%else
Conflicts:      baloo < 5
%endif

# main pkg accidentally multilib'd prior to 5.21.0-4
Obsoletes:      kf5-baloo < 5.21.0-4

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
# KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel >= %{majmin}
Requires:       kf5-kfilemetadata-devel >= %{majmin}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{without kf6_compat}
%package        file
Summary:        File indexing and search for Baloo
# KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
%if 0%{?fedora}
Obsoletes:      baloo-file < 5.0.1-2
Provides:       baloo-file = %{version}-%{release}
%else
Conflicts:      baloo-file < 5
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    file
%{summary}.
%endif

%package        libs
Summary:        Runtime libraries for %{name}
# KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
%description    libs
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  %{?with_kf6_compat:-DBUILD_INDEXER_SERVICE=OFF}
%cmake_build


%install
%cmake_install

%if 0%{?flatpak:1}
find %{buildroot} -name kde-baloo.service -delete
%endif

# baloodb not installed unless BUILD_EXPERIMENTAL is enabled, so omit translations
rm -fv %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/baloodb5.*

%if %{without kf6_compat}
install -p -m644 -D %{SOURCE1} %{buildroot}%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf
install -p -m755 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/shutdown/baloo_file.sh
%endif

%find_lang kio5_baloosearch
%find_lang kio5_tags
%find_lang kio5_timeline
%find_lang balooctl5
%find_lang balooengine5
%find_lang baloosearch5
%find_lang balooshow5
%find_lang baloo_file5
%find_lang baloo_file_extractor5
#find_lang baloomonitorplugin

cat kio5_tags.lang kio5_baloosearch.lang kio5_timeline.lang \
    balooctl5.lang balooengine5.lang baloosearch5.lang \
    balooshow5.lang \
    > %{name}.lang

cat baloo_file5.lang baloo_file_extractor5.lang \
    > %{name}-file.lang

%if %{with kf6_compat}
cat %{name}-file.lang | xargs printf "%{buildroot}%.0s%s\n" | xargs rm
%endif


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif


%files -f %{name}.lang
%license LICENSES/*.txt
#{_kf5_bindir}/baloodb
%{_kf5_bindir}/baloosearch
%{_kf5_bindir}/balooshow
%if %{without kf6_compat}
%{_kf5_bindir}/balooctl
%endif
%{_kf5_datadir}/qlogging-categories5/%{framework}*

%if %{without kf6_compat}
%files file -f %{name}-file.lang
%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/shutdown/baloo_file.sh
%{_kf5_bindir}/baloo_file
%{_kf5_bindir}/baloo_file_extractor
%config(noreplace) %{_kf5_sysconfdir}/xdg/autostart/baloo_file.desktop
%if ! 0%{?flatpak:1}
%{_userunitdir}/kde-baloo.service
%endif
%{_libexecdir}/baloo_file
%{_libexecdir}/baloo_file_extractor
%endif

%ldconfig_scriptlets libs

%files libs
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Baloo.so.*
%{_kf5_libdir}/libKF5BalooEngine.so.*
# multilib'd plugins and friends
%{_kf5_plugindir}/kio/baloosearch.so
%{_kf5_plugindir}/kio/tags.so
%{_kf5_plugindir}/kio/timeline.so
%{_kf5_plugindir}/kded/baloosearchmodule.so
%{_kf5_qmldir}/org/kde/baloo

%files devel
%{_kf5_libdir}/libKF5Baloo.so
%{_kf5_libdir}/cmake/KF5Baloo/
%{_kf5_libdir}/pkgconfig/Baloo.pc
%{_kf5_includedir}/Baloo/

%{_kf5_archdatadir}/mkspecs/modules/qt_Baloo.pri
%if %{without kf6_compat}
%{_kf5_datadir}/dbus-1/interfaces/org.kde.baloo.*.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.Baloo*.xml
%endif


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.116.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.116.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.116.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 19 2024 Alessandro Astone <ales.astone@gmail.com> - 5.116.0-1
- 5.116.0

* Thu Feb 22 2024 Alessandro Astone <ales.astone@gmail.com> - 5.115.0-2
- Drop kf5-baloo-file subpackage, obsoleted by kf6-baloo-file

* Sat Feb 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.115.0-1
- 5.115.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.113.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.113.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.113.0-1
- 5.113.0

* Mon Oct 16 2023 Alessandro Astone <ales.astone@gmail.com> - 5.111.0-3
- Require kf6-baloo if compat build

* Thu Oct 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.111.0-2
- Add KF6 compatibility flag

* Tue Oct 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.111.0-1
- 5.111.0

* Tue Sep 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.110.0-1
- 5.110.0

* Sat Aug 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.109.0-1
- 5.109.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.108.0-1
- 5.108.0

* Wed Jun 07 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.107.0-2
- Backport patch from upstream

* Sat Jun 03 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.107.0-1
- 5.107.0

* Mon May 15 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.106.0-1
- 5.106.0

* Sun Apr 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.105.0-1
- 5.105.0

* Sat Mar 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.104.0-1
- 5.104.0

* Sun Feb 05 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.103.0-1
- 5.103.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.102.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.102.0-1
- 5.102.0

* Mon Dec 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.101.0-1
- 5.101.0
- use new macros to simplify code

* Sun Nov 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.100.0-1
- 5.100.0

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.99.0-1
- 5.99.0

* Thu Sep 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.98.0-1
- 5.98.0

* Sat Aug 13 2022 Justin Zobel <justin@1707.io> - 5.97.0-1
- Update to 5.97.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.96.0-1
- 5.96.0

* Fri May 13 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.94.0-1
- 5.94.0

* Sun Apr 10 2022 Justin Zobel <justin@1707.io> - 5.93-1
- Update to 5.93

* Thu Mar 10 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.92.0-1
- 5.92.0

* Fri Feb 11 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.90.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 5.90.0-1
- 5.90.0

* Wed Dec 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.89.0-1
- 5.89.0

* Mon Nov 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.88.0-1
- 5.88.0

* Tue Oct 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.87.0-1
- 5.87.0

* Tue Sep 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.86.0-1
- 5.86.0

* Thu Aug 12 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.85.0-1
- 5.85.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.83.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.83.0-1
- 5.83.0

* Mon May 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.82.0-1
- 5.82.0
- new systemd user kde-baloo.service

* Tue Apr 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.81.0-1
- 5.81.0

* Tue Mar 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.80.0-1
- 5.80.0

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.79.0-2
- respin

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.79.0-1
- 5.79.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.78.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 08:37:51 CST 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.78.0-1
- 5.78.0

* Sun Dec 13 14:06:56 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.77.0-1
- 5.77.0

* Thu Nov 19 08:53:35 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.76.0-1
- 5.76.0

* Wed Oct 14 09:44:03 CDT 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.75.0-1
- 5.75.0

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.74.0-1
- 5.74.0

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.73.0-3
- shutdown scripts must be executable+valid shell (apparently)

* Mon Sep 14 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.73.0-2
- add explicit shutdown script for baloo_file (parent bug #1861700)

* Mon Aug 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.73.0-1
- 5.73.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.72.0-1
- 5.72.0

* Tue Jun 16 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.71.0-1
- 5.71.0

* Mon May 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.70.0-1
- 5.70.0

* Tue Apr 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.69.0-1
- 5.69.0

* Fri Mar 20 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.68.0-1
- 5.68.0

* Sun Feb 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.67.0-1
- 5.67.0
- Port baloofile_config patch to kcfg (Kevin Kofler)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.66.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.66.0-1
- 5.66.0

* Tue Dec 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.65.0-1
- 5.65.0

* Fri Nov 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.64.0-1
- 5.64.0

* Tue Oct 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.63.0-1
- 5.63.0

* Mon Sep 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.62.0-1
- 5.62.0

* Wed Aug 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.61.0-1
- 5.61.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.60.0-1
- 5.60.0

* Thu Jun 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.59.0-1
- 5.59.0

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.58.0-1
- 5.58.0

* Tue Apr 09 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.57.0-1
- 5.57.0

* Tue Mar 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.56.0-1
- 5.56.0

* Mon Feb 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.55.0-1
- 5.55.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.54.0-1
- 5.54.0

* Sun Dec 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.53.0-1
- 5.53.0

* Mon Nov 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.52.0-2
- rebuild

* Sun Nov 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.52.0-1
- 5.52.0

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.51.0-1
- 5.51.0

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.50.0-1
- 5.50.0

* Tue Aug 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.49.0-1
- 5.49.0

* Mon Jul 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.48.0-1
- 5.48.0

* Sat Jun 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.47.0-1
- 5.47.0

* Sat May 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.46.0-1
- 5.46.0

* Sun Apr 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.45.0-1
- 5.45.0

* Sat Mar 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.44.0-1
- 5.44.0

* Wed Feb 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.43.0-1
- 5.43.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.0-2
- .spec cleanup

* Mon Jan 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.0-1
- 5.42.0

* Mon Dec 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-2
- rebuild

* Mon Dec 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-1
- 5.41.0

* Fri Nov 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-1
- 5.40.0

* Sun Oct 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-1
- 5.39.0

* Mon Sep 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-1
- 5.38.0

* Fri Aug 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.37.0-1
- 5.37.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.36.0-1
- 5.36.0

* Sun Jun 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.35.0-1
- 5.35.0

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.34.0-1
- 5.34.0

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.33.0-1
- 5.33.0

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.32.0-2
- .spec cosmetics, update URL

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.32.0-1
- 5.32.0

* Mon Feb 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.31.0-1
- 5.31.0

* Fri Dec 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.29.0-1
- 5.29.0

* Tue Oct 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Thu Sep 08 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.26.0-1
- KDE Frameworks 5.26.0

* Thu Aug 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.25.0-2
- validate baloo.file.desktop (#1367207)

* Mon Aug 08 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.25.0-1
- KDE Frameworks 5.25.0

* Wed Jul 06 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.24.0-1
- KDE Frameworks 5.24.0

* Tue Jun 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.23.0-1
- KDE Frameworks 5.23.0

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.22.0-1
- KDE Frameworks 5.22.0

* Sat Apr 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-6
- %%check: use standardized BRs, 'make test'

* Fri Apr 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-5
- -file: Requires: %%name-libs

* Fri Apr 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-4
- fix URL
- -devel: depend (only) on -libs
- -libs: move plugins here
- Provides: kf5-baloo-tools

* Wed Apr 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-3
- support bootstrap, %%check: enable tests (advisory)

* Wed Apr 27 2016 Orion Poplawski <orion@cora.nwra.com> - 5.21.0-2
- Do not obsolete/provide baloo{-file} in EPEL, use Conflicts (#1329899)
- update URL

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-1
- KDE Frameworks 5.21.0

* Mon Mar 14 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.20.0-1
- KDE Frameworks 5.20.0

* Thu Feb 18 2016 Rex Dieter <rdieter@fedoraproject.org> 5.19.0-2
- cleanup

* Thu Feb 11 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.19.0-1
- KDE Frameworks 5.19.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.18.0-1
- KDE Frameworks 5.18.0

* Tue Dec 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.17.0-1
- KDE Frameworks 5.17.0

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.16.0-1
- KDE Frameworks 5.16.0

* Thu Oct 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.15.0-1
- KDE Frameworks 5.15.0

* Sat Oct 03 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.14.0-2
- index only well-known document-centric dirs by default (#1235026)
- .spec cosmetics
- polish licensing
- -devel: drop xapian dep

* Wed Sep 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.14.0-1
- KDE Frameworks 5.14.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Tue Aug 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-0.1
- KDE Frameworks 5.13 (Baloo moved from Plasma 5 to KF5)

* Wed Apr 22 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.95-1
- Plasma 5.2.95

* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.2-1
- Plasma 5.2.2

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.1-2
- Rebuild (GCC 5)

* Tue Feb 24 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.1-1
- Plasma 5.2.1

* Sun Feb 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-3
- kf5-baloo-file provides baloo-file

* Sat Feb 07 2015 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-2
- port 97-kde-baloo-filewatch-inotify.conf from Obsoletes'd baloo pkg

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- Plasma 5.2.0

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> - 5.5.95-1
- Plasma 5.1.95 (Plasma 5.2 beta) (baloo 5.5.95 to follow KF5)
- create -libs subpkg

* Wed Jan 07 2015 Jan Grulich <jgrulich@redhat.com> - 5.1.2-3
- Drop -tools subpkg
-  Add icon cache scriptlets
-  Remove deprecated Group: tag
-  Move org.kde.baloo.file.indexer.xml to -file subpkg

* Wed Dec 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2
- Plasma 5.1.2

* Fri Nov 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1
- Plasma 5.1.1

* Tue Oct 14 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0.1-1
- Plasma 5.1.0.1

* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- Plasma 5.1.0

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.2-1
- Plasma 5.0.2

* Mon Aug 18 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-2
- Fix coinstallability with updated baloo package

* Sun Aug 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-1
- Plasma 5.0.1

* Tue Jul 22 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-4
- -devel Requires xapian-core-devel

* Tue Jul 22 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-3
- split bin tools to -tools subpackage

* Tue Jul 22 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-2
- -devel Requires kf5-kfilemetadata-devel
- does not obsolete baloo < 5.0.0 (coinstallability)

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Wed Jun 11 2014 Daniel Vrátil <dvratil@redhat.com> - 4.98.0-3.20140611git84bc23c
- Update to latest git snapshot

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> - 4.90.0-2.20140611git46e3ea7
- KF5 Baloo 4.90.0 (git snapshot built from common kdepimlibs/frameworks repo)
