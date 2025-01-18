
# uncomment to enable bootstrap mode
%global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    blogilo
Summary: Blogging Client
Version: 17.08.3
Release: 33%{?dist}

# code (generally) GPLv2, docs GFDL
# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://www.kde.org/applications/internet/blogilo

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

Patch0:  blogilo-17.08.3-fix-dependencies.patch
Patch1:  blogilo-17.08.3-no-disable-deprecated.patch
Patch2:  blogilo-17.08.3-kdepim-23.04.patch
Patch3:  blogilo-17.08.3-kdepim-23.08.patch

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: boost-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineWidgets)

# kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5TextEditTextToSpeech)
BuildRequires: cmake(KF5TextEmoticonsWidgets)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5XmlGui)

# kde-apps
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: kf5-kblog-devel >= %{majmin_ver}
BuildRequires: kf5-kpimtextedit-devel >= %{majmin_ver}
BuildRequires: kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires: kf5-messagelib-devel >= %{majmin_ver}
BuildRequires: kf5-pimcommon-devel >= %{majmin_ver}
BuildRequires: libkgapi-devel >= %{majmin_ver}

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: hicolor-icon-theme

%description
Blogilo is a blogging client which supports various blogging APIs.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .fix-dependencies
%patch -P1 -p1 -b .no-disable-deprecated
%patch -P2 -p1 -b .kdepim-23.04
if [ ! -f %{_kf5_libdir}/cmake/KF5PimCommon/KF5PimCommonConfig.cmake ] ; then
%patch -P3 -p1 -b .kdepim-23.08
fi


%build
%cmake_kf5 -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%files -f %{name}.lang
%license COPYING*
%{_kf5_sysconfdir}/xdg/blogilo.*
%{_kf5_bindir}/blogilo
%{_kf5_metainfodir}/org.kde.blogilo.appdata.xml
%{_kf5_datadir}/applications/org.kde.blogilo.desktop
%{_kf5_datadir}/config.kcfg/blogilo.kcfg
%{_kf5_datadir}/kconf_update/blogilo-15.08-kickoff.sh
%{_kf5_datadir}/kconf_update/blogilo.upd
%{_kf5_datadir}/icons/hicolor/*/apps/blogilo.png
%{_kf5_datadir}/icons/hicolor/*/actions/upload-media.png
%{_kf5_datadir}/icons/hicolor/*/actions/format-text-blockquote.png
%{_kf5_datadir}/icons/hicolor/*/actions/format-text-code.png
%{_kf5_datadir}/icons/hicolor/*/actions/insert-more-mark.png
%{_kf5_datadir}/icons/hicolor/*/actions/remove-link.png
%{_kf5_datadir}/composereditorwebengine/
%if 0%{?tests}
# is this supposed to be conditional?  --rex
%{_kf5_bindir}/composerhtmleditor
%{_kf5_datadir}/kxmlgui5/composerhtmleditor/
%endif

%files libs
%{_kf5_libdir}/libcomposereditorwebengineprivate.so.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 17.08.3-32
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-28
- Patch and rebuild for new kdepim libraries, again! (#2239665)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 07 2023 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-26
- Patch and rebuild for new kdepim libraries (#2182704)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-24
- use new CMake macros (the transitional -B. hack no longer works) (#2113123)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-19
- Don't use -DQT_DISABLE_DEPRECATED_BEFORE=0x060000 moving target (#1799192)
- Pass -B. to cmake to work around incompatible RPM macro change (#1863271)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-14
- Rebuild for pimcommon 19.04 (#1729068)

* Thu Mar 14 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-13
- Add missing (optional) BuildRequires: libkgapi-devel

* Thu Mar 14 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-12
- Bump Release for upgrade path from the Kannolo Copr

* Tue Mar 12 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-11
- Remove obsolete ldconfig scriptlets
- Add missing Requires: hicolor-icon-theme
- Add missing BuildRequires: gcc-c++ and (explicit) BuildRequires: cmake
- Remove duplicate mention of the HTML documentation from the file list

* Thu Jan 03 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-10
- Bump Release to evade bogus Obsoletes in kf5-kblog
- Add upstream patch by dvratil to fix dependencies, from Debian package
- Use the _kf5_metainfodir macro instead of hardcoding appdata

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.08.3-2
- Remove obsolete scriptlets

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- blogilo-16.12.1

