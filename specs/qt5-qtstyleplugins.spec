Name:	 qt5-qtstyleplugins
Summary: Classic Qt widget styles
Version: 5.0.0
Release: 57%{?dist}
# Automatically converted from old format: LGPLv2 or GPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 OR GPL-2.0-only
URL:	 https://github.com/qtproject/qtstyleplugins
Source0: http://download.qt.io/community_releases/additional_qt_src_pkgs/qtstyleplugins-src-%{version}.tar.gz

## upstream (in lookaside cache)
BuildRequires: make
BuildRequires: git-core
Patch1: 0001-Cleanlooks-style-Fix-floating-point-exception.patch
Patch2: 0002-Sync-QStyleHelper-code-with-the-latest-code-in-qtbas.patch
Patch3: 0003-Import-gtk2-style-from-qtbase.patch
Patch4: 0004-QGtkStyle-fix-spinbox-arrows.patch
Patch5: 0005-Ensure-the-right-color-is-used-for-drawing-the-label.patch
Patch6: 0006-GTK-style-Disable-Ubuntu-scrollbars.patch
Patch7: 0007-Relocate-bb10style-from-qtbase.patch
Patch8: 0008-gtk2-style-get-rid-of-GConf-usage.patch
Patch9: 0009-Import-gtk2-platform-theme-from-qtbase-5.6.patch
Patch10: 0010-Allow-building-of-gtk2-style-when-GConf-is-missing.patch
Patch11: 0011-skip-building-gtk2-platform-theme-if-gtk-2.0-is-miss.patch
Patch12: 0012-Remove-use-of-deprecated-QStyleOption-V-N.patch
Patch13: 0013-Add-Q_DECL_OVERRIDE.patch
Patch14: 0014-Build-the-BB10-style-with-Qt-5.7-or-later-only.patch
Patch15: 0015-Add-missing-PLUGIN_CLASS_NAMEs.patch
Patch16: 0016-Remove-obsolete-and-unused-QBB10StylePlugin-keys.patch
Patch17: 0017-Remove-unused-sync.profile.patch
Patch18: 0018-Fix-build-with-Qt-5.8.0.patch
Patch19: 0019-QCleanlooksStyle-Use-QCommonStyle-instead-of-QProxyS.patch
Patch20: 0020-QPlastiqueStyle-Use-QCommonStyle-instead-of-QProxySt.patch
Patch21: 0021-Plastique-Fix-QSpinBox-height-in-layout.patch
Patch22: 0022-Motif-CDE-Fix-QSpinBox-height-in-layout.patch
Patch23: 0023-Fix-plastique-cleanlooks-and-motif-animation-timer.patch
Patch24: 0024-Fix-build-qt-5.15.patch

## upstreamable patches

BuildRequires: gtk2-devel
BuildRequires: qt5-qtbase-devel >= 5.7
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtbase-private-devel


# Do not check gtk2-related files for for requires.
# If the required libraries are not there, the platform/style to integrate
# with isn't either. Then Qt will just silently ignore the plugin.
%global __requires_exclude_from ^(%{_qt5_plugindir}/platformthemes/libqgtk2.so|%{_qt5_plugindir}/styles/libqgtk2style.so)$

%description
%{summary}, including cleanlooks, motif, plastique, qgtk.


%prep
%autosetup -n qtstyleplugins-src-%{version} -Sgit


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} ..
%make_build
popd


%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}


%files
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QCleanlooksStylePlugin.cmake
%{_qt5_plugindir}/styles/libqcleanlooksstyle.so
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QMotifStylePlugin.cmake
%{_qt5_plugindir}/styles/libqmotifstyle.so
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QPlastiqueStylePlugin.cmake
%{_qt5_plugindir}/styles/libqplastiquestyle.so
# qgtk2 platform/style
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QGtk2StylePlugin.cmake
%{_qt5_plugindir}/styles/libqgtk2style.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QGtk2ThemePlugin.cmake
%{_qt5_plugindir}/platformthemes/libqgtk2.so
# bb10
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QBB10StylePlugin.cmake
%{_qt5_plugindir}/styles/libbb10styleplugin.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.0-56
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.0-49
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.0-48
- Rebuild (qt5)

* Fri Mar 11 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.0-47
- Rebuild (qt5)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:56:00 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.0.0-43
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.0.0-42
- rebuild (qt5)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-41
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-39
- rebuild (qt5)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.0-37
- rebuild (qt5)

* Sat Sep 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-36
- rebuild (qt5)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.0-34
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-33
- rebuild (qt5)

* Mon Feb 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-32
- rebuild (qt5)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-30
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.0.0-29
- rebuild (qt5)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-27
- use %%make_build %%make_install

* Sun May 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-26
- drop qgtk2/bb10 conditionals

* Sun Feb 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-25
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 5.0.0-23
- rebuild (qt5)

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-22
- rebuild (qt5)

* Mon Oct 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-21
- rebuild (qt5)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 5.0.0-19
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-17
- rebuild (qt5)

* Mon May 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-16
- rebuild (qt5)

* Thu Mar 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-15
- rebuild (qt5)
- pull in upstream fixes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-13
- rebuild (qt5)

* Thu Dec 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-12
- make qgtk2 style qt57+ only too

* Wed Dec 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-11
- more upstream fixes, include qgtk2 platform plugin on f25+ only

* Sat Dec 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-10
- rebuild (qt5)

* Wed Oct 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-9
- pull in upstream fixes, added qgtk2 (#1386404), bb10 support

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-8
- rebuild (qt5)

* Sun Jul 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-7
- rebuild (qt5-qtbase)

* Thu Jun 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-6
- rebuild (qtbase)

* Sun Apr 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-5
- BR: qt5-qtbase-private-devel

* Sat Apr 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-4
- rebuild (qt 5.6)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-2
- pull in some post v5.0.0 fixes (one crashfix)

* Mon Dec 14 2015 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-1
- first try


