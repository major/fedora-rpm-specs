# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    k3b
Summary: CD/DVD/Blu-ray burning application
Epoch:   1
Version: 25.07.90
Release: 1%{?dist}

License: GPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/k3b

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=2212471
Patch10: prefer-wodim.patch

## downstream patches

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Core5Compat)

%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KCddb6)

BuildRequires: ffmpeg-free-devel
BuildRequires: lame-devel
BuildRequires: libmpcdec-devel
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(flac++)

BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(vorbisenc) pkgconfig(vorbisfile)
BuildRequires: pkgconfig(taglib)

Conflicts: k3b-extras-freeworld < 1:17.03

Obsoletes: k3b-common < 1:17.03
Provides:  k3b-common = %{epoch}:%{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

Requires: cdrdao
# cdrecord compatibility layer from libburn, I know it's newer, but k3b
# hangs when trying to use it, and installs as same priority as wodim (50)
# do definitely confusing in the least, dropping for now -- rex
#Requires: cdrskin
Requires: dvd+rw-tools
## BR these runtime dependencies for sanitiy (for now) -- rex
## use real packages, not virtual provides since they have
## been recently removed, https://bugzilla.redhat.com/1599009
# mkisofs
BuildRequires: genisoimage
Requires: genisoimage
# cdrecord
BuildRequires: wodim
Requires: wodim

%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Files for the development of applications which will use %{name} 
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  -DK3B_BUILD_FFMPEG_DECODER_PLUGIN:BOOL=ON \
  -DK3B_BUILD_LAME_ENCODER_PLUGIN:BOOL=ON \
  -DK3B_BUILD_MAD_DECODER_PLUGIN:BOOL=ON

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.k3b.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.k3b.desktop


%files -f %{name}.lang
%doc README*
%license LICENSES/*
%{_kf6_bindir}/k3b
%{_kf6_metainfodir}/org.kde.k3b.appdata.xml
%{_kf6_datadir}/applications/org.kde.k3b.desktop
%{_kf6_datadir}/knotifications6/k3b.*
%{_datadir}/knsrcfiles/k3btheme.knsrc
%{_kf6_datadir}/konqsidebartng/virtual_folders/services/*.desktop
%{_kf6_datadir}/solid/actions/k3b*.desktop
%{_kf6_datadir}/mime/packages/x-k3b.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/k3b/
%{_kf6_datadir}/kio/servicemenus/*
%{_kf6_datadir}/qlogging-categories6/k3b.categories
%{_libexecdir}/kf6/kauth/k3bhelper
%{_datadir}/dbus-1/system-services/org.kde.k3b.service
%{_datadir}/dbus-1/system.d/org.kde.k3b.conf
%{_datadir}/polkit-1/actions/org.kde.k3b.policy

%files libs
%{_kf6_libdir}/libk3bdevice.so.*
%{_kf6_libdir}/libk3blib.so.*
%{_kf6_qtplugindir}/k3b_plugins
%{_kf6_plugindir}/kio/videodvd.so

%files devel
%{_includedir}/k3b*.h
%{_kf6_libdir}/libk3bdevice.so
%{_kf6_libdir}/libk3blib.so


%changelog
* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 1:25.07.90-1
- 25.07.90

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Steve Cossette <farchord@gmail.com> - 1:25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 1:25.04.3-1
- 25.04.3

* Wed Jun 04 2025 Steve Cossette <farchord@gmail.com> - 1:25.04.2-1
- 25.04.2

* Tue May 27 2025 Jitka Plesnikova <jplesnik@redhat.com> - 1:25.04.1-2
- Rebuilt for flac 1.5.0

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 1:25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 1:25.04.0-1
- 25.04.0

* Thu Mar 20 2025 Steve Cossette <farchord@gmail.com> - 1:25.03.80-1
- 25.03.80 (Beta)

* Tue Mar 04 2025 Steve Cossette <farchord@gmail.com> - 1:24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 1:24.12.2-2
- Rebuild for ppc64le enablement

* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 1:24.12.2-1
- 24.12.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 1:24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 1:24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 1:24.08.2-1
- 24.08.2

* Fri Oct 04 2024 Than Ngo <than@redhat.com> - 1:24.08.1-2
- fixed rhbz#2316261, rebuild against new ffmpeg7

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 1:24.08.1-1
- 24.08.1

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 1:24.08.0-2
- Rebuild for ffmpeg 7

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 1:24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.01.90-1
- 24.01.90

* Fri Jan 05 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-1
- 24.01.85 using Qt6/KF6

* Tue Jan 02 2024 Alessandro Astone <ales.astone@gmail.com> - 1:23.08.2-2
- Prefer wodim to cdrecord

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.03.80-1
- 23.03.80

* Fri Mar 17 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1:22.12.3-3
- Rebuilt for libmpcdec 1.3.0

* Sun Mar 12 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1:22.12.3-2
- Enable ffmpeg decoder support

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:22.12.3-1
- 22.12.3

* Sat Feb 18 2023 Than Ngo <than@redhat.com> - 22.12.2-2
- migrated to SPDX license

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:22.12.1-1
- 22.12.1

* Fri Dec 09 2022 Than Ngo <than@redhat.com> - 22.12.0-1
- 22.12.0

* Fri Nov 25 2022 Marc Deop marcdeop@fedoraproject.org - 22.08.3-2
- Rebuild

* Thu Nov 03 2022 Than Ngo <than@redhat.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.2-1
- 22.08.2

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 1:22.08.1-2
- Rebuilt for flac 1.4.0

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu Jun 23 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Thu May 12 2022 Than Ngo <than@redhat.com> - 22.04.1-1
- 22.04.1

* Tue Apr 26 2022 Than Ngo <than@redhat.com> - 22.04.0-1
- 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:21.12.1-1
- 21.12.1

* Mon Dec 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.1-1
- 21.04.1

* Mon May 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.0-2
- drop cdrskin dep
- .spec cleanup

* Mon Apr 19 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:20.12.3-1
- 20.12.3

* Wed Feb 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 14:59:31 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.3-1
- 20.08.3

* Sat Oct 17 2020 Dominik Mierzejewski <rpm@greysector.net> - 1:20.08.1-2
- rebuild for libdvdread-6.1 ABI bump

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.1-1
- 20.04.1

* Mon May 04 2020 Troy Dawson <tdawson@redhat.com> - 1:20.04.0-2
- List k3btheme.knsrc in correct directory in %files

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.2-1
- 19.12.2

* Fri Jan 31 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.1-1
- 19.12.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:19.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1:19.08.3-2
- rebuild for libdvdread ABI bump

* Tue Nov 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.2-1
- 19.08.2

* Fri Oct 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.1-1
- 19.08.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.04.3-1
- 19.04.3

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.1-1
- 18.12.1

* Sun Dec 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.2-1
- 18.08.2

* Sun Sep 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.3-1
- 18.04.3

* Sun Jul 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.2-4
- Requires: wodim  (#1599009)
- drop ExcludeArch: s390 s390x (wodim is available now)

* Sat Jul 07 2018 Kevin Fenzi <kevin@scrye.com> - 1:18.04.2-3
- Require genisoimage (real subpackage) instead of mkisofs (dropped provides from genisoimage)

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.2-2
- use %%make_build %%ldconfig_scriptlets
- fix use of %%webkit conditional

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.1-1
- 18.04.1

* Thu Apr 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.3-1
- 17.12.3

* Thu Feb 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.2-1
- 17.12.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.1-1
- 17.12.1

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:17.12.0-3
- Remove obsolete scriptlets

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.0-2
- k3b (still) uses /tmp (#1530047,kde#385367))
- %%check: appdata validation

* Thu Dec 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.0-1
- 17.12.0

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.2-1
- 17.08.2

* Thu Sep 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.1-1
- 17.08.1

* Fri Aug 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.3-2
- Requires: cdrskin

* Thu Aug 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.3-1
- 17.04.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.2-1
- 17.04.2

* Sun May 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.1-1
- 17.04.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.3-10
- backport no_fake_mimetypes fix from master/ branch
- workaround FTBFS with -std=gnu++98 (#1307677)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.3-8
- kf5 solid/actions,ServiceMenus
- use %%license
- drop hard/versioned qt4/kdelibs/kde-runtime deps

* Wed Oct 21 2015 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.3-7
- rebuild (kdelibs/taglib)

* Wed Oct 21 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.3-6
- respin tarball
- pull in latest 2.0 branch fixes
- hack around cmake FTBFS
- drop deprecated libmusicbrainz dep

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:2.0.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Feb 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.0.3-3
- don't own %%_datadir/appdata (#1188048)

* Tue Nov 04 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.3-2
- upstream patch to fix version

* Mon Nov 03 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.3-1
- k3b-2.0.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.2-23.20130927git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-22.20130927git
- optimize mimeinfo scriptlet, fix icon scriptlet

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.2-21.20130927git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.2-20.20130927git
- trim changelog
- include appdata (kde review #113531)

* Tue Oct 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.2-19.20130927git
- use libkcddb dep where possible

* Fri Sep 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.2-18.20130927git
- 20130927git snapshot
- .spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-15
- use /var/tmp instead of /tmp

* Thu Nov 29 2012 Radek Novacek <rnovacek@redhat.com> 1:2.0.2-14
- Use -fno-strict-aliasing (k3b does some nasty stuff with pointers in iso9660 support)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Radek Novacek <rnovacek@redhat.com> 1:2.0.2-12
- Disable HAL support at all, it's not even in Fedora anymore

* Tue Jun 12 2012 Radek Novacek <rnovacek@redhat.com> 1:2.0.2-11
- Don't show suggestion to start HAL daemon when no CD/DVD device is found

* Fri May 04 2012 Radek Novacek <rnovacek@redhat.com> 1:2.0.2-10
- Fix conditional for RHEL

* Fri May 04 2012 Radek Novacek <rnovacek@redhat.com> 1:2.0.2-9
- Remove QtWebKit BR on RHEL

* Fri May 04 2012 Radek Novacek <rnovacek@redhat.com> 1:2.0.2-8
- Don't use webkit on RHEL

* Tue Feb 28 2012 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-7
- pkgconfig-style deps
- +BR: pkgconfig(QtWebKit)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 17 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:2.0.2-5
- increase overburning tolerance from 1/10 to 1/4 for CD-R90/99 (kde#276002)
- fix overburning check to not count the used capacity twice

* Sat Apr 23 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:2.0.2-4
- prefer growisofs to wodim for DVD/BluRay also for DVD copying and data
  projects, the previous patch only worked for ISO burning (#610976)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.2-2
- use growisofs for blueray too (#610976)

* Wed Jan 19 2011 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.2-1
- k3b-2.0.2 (#670325)
- use growisofs for dvd's (#610976)

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.1-5
- turns out existing hal support is mostly harmless (not required, but will
  use if present), so back out those changes.

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.1-4
- build without ENABLE_HAL_SUPPORT (f15+)
- spec cleanup

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.1-3
- Requires: hal-storage-addon

* Tue Oct 05 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.1-2
- drop workaround patch if building on/for kde-4.5.2+ (#582764)

* Tue Aug 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.1-1
- k3b-2.0.1

* Mon Aug 30 2010 Radek Novacek <rnovacek@redhat.com> - 1:2.0.0-3
- Added temporary workaround for #582764

* Tue Jul 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.0-2
- Missing Icon of k3b (#611272)

* Mon Jun 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.0-1
- k3b-2.0.0

* Thu Jun 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.93.0-1
- k3b-1.93.0 (rc3)

* Sat May 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.92.0-1
- k3b-1.92.0 (rc3)
- enable -common noarch content

* Sat Mar 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.91.0-2
- Requires: kdebase-runtime

* Sat Mar 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.91.0-1
- k3b-1.91.0 (rc2)

* Fri Mar 05 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.90.0-1
- k3b-1.90.0 (rc1)

* Mon Feb 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.70.0-1
- k3b-1.70.0 (beta1)

* Thu Jan 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.69.0-3
- use %%{_kde4_version}

* Thu Dec 10 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.69.0-2
- fix %%post scriptlet

* Thu Dec 10 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.69.0-1
- k3b-1.69.0 (alpha4)

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.68.0-3 
- rebuild (for qt-4.6.0-rc1, f13+)

* Thu Oct 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.68.0-2
- -common (noarch) subpkg handling
- -libs: add min runtime deps for qt4/kdelibs4

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.68.0-1
- k3b-1.68.0 (alpha3)

* Sat Sep 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.66.0-5
- Epoch: 1 (increment Release too, to minimize confusion)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.66.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0:1.66.0-3
- -extras-freeworld avail now, drop Obsoletes

* Wed Jun 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 0:1.66.0-2
- Obsoletes: k3b-extras-freeworld (at least until it's ready)

* Wed May 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 0:1.66.0-1
- k3b-1.66.0 (alpha2)

* Wed Apr 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 0:1.65.0-1
- k3b-1.65.0 (alpha1)
- optimize scriptlets

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.5-7
- Summary: omit "for KDE"
- add rhel portability to .spec

* Wed Oct 01 2008 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.5-6
- revert libdvdread header changes, fix build (#465115)
- (re)enable -devel on f9

* Wed Aug 27 2008 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.5-5
- resurrect -devel (!=f9), grow -libs (f10+, #341651)
- avoid auto*foo
- fix build on rawhide (libdvdread header changes)
- conditionalize i18n bits

* Thu Jul 31 2008 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.5-4
- try alternative fix for tray eject/reload (kde#156684)

* Mon Jun 30 2008 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.5-3
- No association k3b with .iso files in gnome (#419681)
- scriptlet deps
- cleanup doc/HTML

* Sat May 31 2008 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.5-2
- (re)enable reload patch

* Tue May 27 2008 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.5-1
- k3b-1.0.5
- k3brc: set manual buffer size here
- omit reload patch (for now), to verify if still needed.

* Wed May  7 2008 Roman Rakus <rrakus@redhat.cz> - 0:1.0.4-9
- Fix doc dir (#238070), patch by Alain PORTAL (aportal@univ-montp2.fr)

* Tue Apr 22 2008 Roman Rakus <rrakus@redhat.cz> - 0:1.0.4-8
- Use manual buffer size by default (#220481)

* Tue Feb 19 2008 Rex Dieter <rdieter@fedoraproject.org> - 0:1.0.4-7
- f9+: Obsoletes: k3b-devel (#429613)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0.4-6
- Autorebuild for GCC 4.3

* Sat Dec 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 0:1.0.4-5
- patch for "k3b can't reload media for verification" (kde#151816)
- BR: kdelibs3-devel

* Wed Nov 21 2007 Adam Tkac <atkac redhat com> - 0:1.0.4-3
- rebuild against new libdvdread

* Mon Nov 05 2007 Rex Dieter <rdieter[AT]fedorproject.org> - 0:1.0.4-2
- k3b-1.0.4
- omit -devel subpkg (f9+), fixes multiarch conflicts (#341651)

* Fri Aug 17 2007 Harald Hoyer <harald@redhat.com> - 0:1.0.3-3
- changed license tag to GPLv2+

* Fri Aug  3 2007 Harald Hoyer <harald@redhat.com> - 0:1.0.3-2
- added gnome-umount options

* Fri Jul 27 2007 Harald Hoyer <harald@redhat.com> - 0:1.0.3-1
- version 1.0.3
- added gnome-umount patch

* Sat Jun 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 0:1.0.2-1
- k3b-1.0.2

* Sat Jun 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 0:1.0.1-4
- k3b-iso.desktop,k3b-cue.desktop: +NoDisplay=True (#244513)

* Wed Jun 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 0:1.0.1-3
- --without-cdrecord-suid-root

* Wed Jun 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 0:1.0.1-2
- respin (for libmpcdec)

* Wed May 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 0:1.0.1-1
- k3b-1.0.1
- include icon/mime scriptlets
- cleanup/simplify BR's
- optimize %%configure
- restore applnk/.hidden bits

* Wed Apr 11 2007 Harald Hoyer <harald@redhat.com> - 0:1.0-1
- version k3b-1.0
- provide/obsolete k3b-extras

* Thu Feb 15 2007 Harald Hoyer <harald@redhat.com> - 0:1.0.0-0.rc6.1
- version k3b-1.0rc6

* Wed Feb  7 2007 Harald Hoyer <harald@redhat.com> - 0:1.0.0-0.rc5.1
- version k3b-1.0rc5

* Wed Jan 17 2007 Harald Hoyer <harald@redhat.com> - 0:1.0.0-0.rc4.1
- version k3b-1.0rc4

* Thu Oct 26 2006 Harald Hoyer <harald@backslash.home> - 0:1.0.0-0.pre2.1
- version 1.0pre2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:0.12.15-3.1.1
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:0.12.15-3.1
- rebuild

* Mon Jun 12 2006 Harald Hoyer <harald@redhat.com> - 0:0.12.15-3
- fixed symlinks

* Tue May 02 2006 Harald Hoyer <harald@redhat.com> 0:0.12.15-1
- version 0.12.15

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0:0.12.10-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0:0.12.10-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 24 2006 Harald Hoyer <harald@redhat.com> 0:0.12.10-2
- removed .la files (#172638)

* Tue Dec 20 2005 Harald Hoyer <harald@redhat.com> 0:0.12.10-1
- version 0.12.10

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Dec 06 2005 Harald Hoyer <harald@redhat.com> 0:0.12.8-1
- version 0.12.8

* Wed Sep 21 2005 Harald Hoyer <harald@redhat.com> 0:0.12.4-0.a.1
- version 0.12.4a

* Thu Jul 14 2005 Harald Hoyer <harald@redhat.com> 0:0.12.2-1
- version 0.12.2
- ported some patches

* Wed Jul 11 2005 Harald Hoyer <harald@redhat.com> 0:0.11.23-2
- added "dvd+rw-tools cdrdao" to Requires

* Thu Apr  7 2005 Petr Rockai <prockai@redhat.com> - 0:0.11.23-3
- fix statfs usage (as per issue 65935 from IT)

* Wed Mar 30 2005 Harald Hoyer <harald@redhat.com> 0:0.11.23-1
- update to 0.11.23

* Fri Mar 25 2005 David Hill <djh[at]ii.net> 0:0.11.22-1
- update to 0.11.22

* Tue Mar 08 2005 Than Ngo <than@redhat.com> 0:0.11.17-2
- rebuilt against gcc-4

* Tue Oct 05 2004 Harald Hoyer <harald@redhat.com> 0:0.11.17-1
- version 0.11.17
- revert the dao -> tao change
- add the suid feature to every app automatically

* Tue Oct 05 2004 Harald Hoyer <harald@redhat.com> 0:0.11.14-2
- fixed version string parsing, which fixes bug 134642

* Wed Sep 01 2004 Harald Hoyer <harald@redhat.com> 0:0.11.14-1
- added k3b-0.11.14-rdrw.patch for kernel >= 2.6.8
- update to 0.11.14

* Fri Jun 25 2004 Bill Nottingham <notting@redhat.com> 0:0.11.12-2
- update to 0.11.12

* Mon Jun 21 2004 Than Ngo <than@redhat.com> 0:0.11.11-1
- update to 0.11.11
- add prereq:/sbin/ldconfig

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 31 2004 Justin M. Forbes <64bit_fedora@comcast.net> - 0.11.10-1
- remove unnecesary [ -z "$QTDIR" ] check
- Update to 0.11.10 upstream 
- remove qt-devel BuildRequires, implied with kde-devel
- remove ldconfig Requires, implied
- remove i18n docbook patch, fixed upstream.

* Fri May 28 2004 Bill Nottingham <notting@redhat.com> - 0.11.9-5
- fix burning on SCSI CD-ROMS (#122096)

* Thu May 13 2004 Than Ngo <than@redhat.com> 0.11.9-4
- get rid of rpath

* Fri Apr 16 2004 Bill Nottingham <notting@redhat.com> - 0.11.9-3
- nuke k3bsetup
- use %%find_lang

* Thu Apr 15 2004 Justin M. Forbes <64bit_fedora@comcast.net> - 0.11.9-2
- Clean up i18n build to make improve maintainability

* Wed Apr 7 2004 Justin M. Forbes <64bit_fedora@comcast.net> - 0.11.9-1
- Update to 0.11.9 upstream
- Spec Cleanup for Fedora Core 2

* Wed Mar 18 2004 Justin M. Forbes <64bit_fedora@comcast.net> - 0.11.6-1
- Initial packaging of 0.11.6 for Fedora Core 2
- remove mp3 plugin build options
- add i18n package
- clean up for kde 3.2/FC2 target


