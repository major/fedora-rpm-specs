%bcond system_qtsingleapplication %{undefined flatpak}

%global smplayer_themes_ver 20.11.0
%global smplayer_skins_ver 20.11.0

Name:           smplayer
Version:        24.5.0
Release:        4%{?dist}
Summary:        A graphical frontend for mplayer and mpv

License:        GPL-2.0-or-later
URL:            https://www.smplayer.info/
Source0:        https://github.com/smplayer-dev/smplayer/releases/download/v%{version}/smplayer-%{version}.tar.bz2
Source3:        https://downloads.sourceforge.net/smplayer/smplayer-themes-%{smplayer_themes_ver}.tar.bz2
Source4:        https://downloads.sourceforge.net/smplayer/smplayer-skins-%{smplayer_skins_ver}.tar.bz2
# Fix regression in Thunar (TODO: re-check in upcoming versions!)
# https://bugzilla.rpmfusion.org/show_bug.cgi?id=1217
Patch0:         smplayer-21.08.0-desktop-files.patch
Patch1:         smplayer-14.9.0.6966-system-qtsingleapplication.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
#BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(xext)
# for unbundle sources
%if %{with system_qtsingleapplication}
BuildRequires:  qtsingleapplication-qt5-devel
%endif
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Requires:       mpv
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp

Provides:       bundled(mongoose) = 6.11
Provides:       bundled(libmaia) = 0.9.0

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
SMPlayer is a graphical user interface (GUI) for the award-winning mplayer
and also for mpv. But apart from providing access for the most common
and useful options of mplayer and mpv, SMPlayer adds other interesting features
like the possibility to play Youtube videos or search and download subtitles.
One of the main features is the ability to remember the state of a
played file, so when you play it later it will be resumed at the same point
and with the same settings.
SMPlayer is developed with the Qt toolkit, so it's multi-platform.

%package themes
Summary:  Themes and Skins for SMPlayer
Requires: %{name} = %{version}-%{release}
BuildArch:  noarch

%description themes
A set of themes for SMPlayer and a set of skins for SMPlayer.

%prep
%setup -q -a3 -a4
#remove some bundle sources
rm -rf zlib
%if %{with system_qtsingleapplication}
rm -rf src/qtsingleapplication/
%endif
#TODO unbundle libmaia
#rm -rf src/findsubtitles/libmaia

%patch -P0 -p1 -b .desktop-files
%if %{with system_qtsingleapplication}
%patch -P1 -p1 -b .qtsingleapplication
%endif

# correction for wrong-file-end-of-line-encoding
%{__sed} -i 's/\r//' *.txt

# change rcc binary
%{__sed} -e 's/rcc -binary/rcc-qt5 -binary/' -i smplayer-themes-%{smplayer_themes_ver}/themes/Makefile
%{__sed} -e 's/rcc -binary/rcc-qt5 -binary/' -i smplayer-skins-%{smplayer_skins_ver}/themes/Makefile

%build
pushd src
    sed -i 's/DEFINES += YT_CODEDOWNLOADER/DEFINES -= YT_CODEDOWNLOADER/' smplayer.pro
    %{qmake_qt5}
    %make_build DATA_PATH="\\\"%{_datadir}/%{name}\\\"" \
        TRANSLATION_PATH="\\\"%{_datadir}/%{name}/translations\\\"" \
        DOC_PATH="\\\"%{_docdir}/%{name}\\\"" \
        THEMES_PATH="\\\"%{_datadir}/%{name}/themes\\\"" \
        SHORTCUTS_PATH="\\\"%{_datadir}/%{name}/shortcuts\\\""
    lrelease-qt5 %{name}.pro
popd

pushd smplayer-themes-%{smplayer_themes_ver}
    %make_build
popd

pushd smplayer-skins-%{smplayer_skins_ver}
    %make_build
popd
pushd webserver
export CFLAGS_EXTRA="%{optflags}"
%make_build
popd

%install
%make_install PREFIX=%{_prefix} DOC_PATH=%{_docdir}/%{name}

# License docs go to another place
rm -r %{buildroot}%{_docdir}/%{name}/Copying*

pushd smplayer-themes-%{smplayer_themes_ver}
    %make_install PREFIX=%{_prefix}
popd

pushd smplayer-skins-%{smplayer_skins_ver}
    %make_install PREFIX=%{_prefix}
    mv README.txt README-skins.txt
    mv Changelog Changelog-skins.txt
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license Copying*
%{_bindir}/smplayer
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/smplayer/
%exclude %{_datadir}/smplayer/themes/
%{_mandir}/man1/%{name}.1.*
%{_docdir}/%{name}/
%{_bindir}/simple_web_server
%{_metainfodir}/%{name}.appdata.xml

%files themes
%doc smplayer-themes-%{smplayer_themes_ver}/README.txt
%doc smplayer-themes-%{smplayer_themes_ver}/Changelog
%doc smplayer-skins-%{smplayer_skins_ver}/README-skins.txt
%doc smplayer-skins-%{smplayer_skins_ver}/Changelog-skins.txt
%license smplayer-themes-%{smplayer_themes_ver}/COPYING*
%{_datadir}/smplayer/themes/

%changelog
* Wed Feb 19 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 24.5.0-4
- Update yt-dlp dependency

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Packit <hello@packit.dev> - 24.5.0-1
- Update to version 24.5.0

* Mon Apr 29 2024 Sérgio Basto <sergio@serjux.com> - 23.12.0-4
- Remove support to epel-7 and epel-8

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 23.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Sérgio Basto <sergio@serjux.com> - 23.12.0-2
- Migrate to SPDX license
- Change the themes subpackage to noarch
- Fixes for EPEL 9

* Thu Jan 04 2024 Sérgio Basto <sergio@serjux.com> - 23.12.0-1
- Update smplayer to 23.12.0

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 23.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Leigh Scott <leigh123linux@gmail.com> - 23.6.0-1
- Update smplayer to 23.6.0

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 22.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Jul 14 2022 Sérgio Basto <sergio@serjux.com> - 22.7.0-1
- Update smplayer to 22.7.0

* Tue Mar 01 2022 Sérgio Basto <sergio@serjux.com> - 22.2.0-1
- Update smplayer to 22.2.0

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Sérgio Basto <sergio@serjux.com> - 21.10.0-2
- After require yt-dlp, we disable "donwload and install yt-dl" feature

* Mon Nov 01 2021 Sérgio Basto <sergio@serjux.com> - 21.10.0-1
- Update smplayer to 21.10.0

* Tue Aug 17 2021 Sérgio Basto <sergio@serjux.com> - 21.8.0-2
- smplayer.appdata.xml also upstreamed, but not validate well on epel 7 and 8

* Mon Aug 16 2021 Sérgio Basto <sergio@serjux.com> - 21.8.0-1
- Update smplayer to 21.8.0
- Patch3 was upstremed

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 21.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 21.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Sérgio Basto <sergio@serjux.com> - 21.1.0-2
- Update appdata.xml and relax the validation

* Thu Jan 07 2021 Sérgio Basto <sergio@serjux.com> - 21.1.0-1
- Update smplayer to 21.1.0

* Sat Dec 05 2020 Sérgio Basto <sergio@serjux.com> - 20.6.0-4
- Update skins and themes

* Thu Sep 10 2020 Leigh Scott <leigh123linux@gmail.com> - 20.6.0-3
- Fix and vailidate appdata

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Sérgio Basto <sergio@serjux.com> - 20.6.0-1
- Update smplayer to 20.6.0
- Add BR qt5-qtbase-private-devel

* Thu Apr 16 2020 Leigh Scott <leigh123linux@gmail.com> - 20.4.2-1
- Update smplayer to 20.4.2

* Thu Apr 09 2020 Sérgio Basto <sergio@serjux.com> - 20.4.0-1
- Update smplayer to 20.4.0

* Sun Mar 01 2020 Sérgio Basto <sergio@serjux.com> - 19.10.2-3
- Add appdata file, copied from
  https://github.com/sanjayankur31/rpmfusion-appdata

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 19.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sérgio Basto <sergio@serjux.com> - 19.10.2-1
- Update to 19.10.2
- Drop patch4, upstream did a similar fix.

* Tue Oct 29 2019 Sérgio Basto <sergio@serjux.com> - 19.10.0-1
- Update smplayer to 19.10.0 (with fix for new mpv)

* Sun Oct 27 2019 Sérgio Basto <sergio@serjux.com> - 19.5.0-5
- Remove smtube sub-package it is available in separated package
- Announce bundle of libmaia
- Suggests mpv instead mplayer

* Sat Oct 26 2019 Leigh Scott <leigh123linux@gmail.com> - 19.5.0-4
- Fix controls with mpv-0.30.0

* Fri Sep 13 2019 Sérgio Basto <sergio@serjux.com> - 19.5.0-3
- Update smtube to 19.6.0

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 19.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Sérgio Basto <sergio@serjux.com> - 19.5.0-1
- Update smplayer to 19.5.0

* Sun Apr 21 2019 Leigh Scott <leigh123linux@googlemail.com> - 19.1.0-3
- Remove Group tag
- Remove obsolete scriptlets for Fedora

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 19.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Sérgio Basto <sergio@serjux.com> - 19.1.0-1
- Update smplayer to 19.1.0

* Fri Jan 04 2019 Sérgio Basto <sergio@serjux.com> - 18.10.0-2
- Update smtube to 18.11.0

* Sun Oct 21 2018 Sérgio Basto <sergio@serjux.com> - 18.10.0-1
- Update smplayer to 18.10.0

* Tue Sep 18 2018 Sérgio Basto <sergio@serjux.com> - 18.9.0-1
- Update smplayer and smtube to 18.9.0

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 18.6.0-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Sérgio Basto <sergio@serjux.com> - 18.6.0-1
- Update smplayer to 18.6.0

* Thu May 31 2018 Sérgio Basto <sergio@serjux.com> - 18.5.0-1
- Update smplayer to 18.5.0

* Tue Apr 24 2018 Sérgio Basto <sergio@serjux.com> - 18.4.0-1
- Update smplayer to 18.4.0

* Mon Mar 26 2018 Sérgio Basto <sergio@serjux.com> - 18.3.0-2
- Fix for epel-7 and announce bundle of mongoose

* Sun Mar 25 2018 Sérgio Basto <sergio@serjux.com> - 18.3.0-1
- Update smplayer to 18.3.0

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 18.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 20 2018 Sérgio Basto <sergio@serjux.com> - 18.2.2-3
- Fix one GCC 8 warning
- Build simple_web_server with rpm CFLAGS
- Better ifdefs scriptlets

* Mon Feb 19 2018 Sérgio Basto <sergio@serjux.com> - 18.2.2-2
- Mute GCC 8 warnings

* Sun Feb 18 2018 Sérgio Basto <sergio@serjux.com> - 18.2.2-1
- Update smplayer to 18.2.2

* Mon Jan 29 2018 Sérgio Basto <sergio@serjux.com> - 18.2.0-1
- Update smplayer to 18.2.0 and smtube to 18.1.0

* Wed Jan 10 2018 Sérgio Basto <sergio@serjux.com> - 18.1.0-1
- Update smplayer to 18.1.0

* Tue Dec 26 2017 Sérgio Basto <sergio@serjux.com> - 17.12.0-1
- Update smplayer to 17.12.0

* Thu Nov 16 2017 Sérgio Basto <sergio@serjux.com> - 17.11.2-1
- Update smplayer to 17.11.2

* Sun Nov 05 2017 Sérgio Basto <sergio@serjux.com> - 17.11.0-1
- Update smplayer to 17.11.0

* Wed Oct 18 2017 Sérgio Basto <sergio@serjux.com> - 17.10.2-1
- Update smplayer to 17.10.2

* Sat Sep 30 2017 Sérgio Basto <sergio@serjux.com> - 17.10.0-1
- Update smplayer to 17.10.0

* Tue Sep 12 2017 Sérgio Basto <sergio@serjux.com> - 17.9.0-1
- Update smplayer to 17.9.0

* Wed Aug 23 2017 Sérgio Basto <sergio@serjux.com> - 17.8.0-1
- Update smplayer to 17.8.0

* Wed Jul 05 2017 Sérgio Basto <sergio@serjux.com> - 17.7.0-1
- Update smplayer to 17.7.0

* Wed May 31 2017 Sérgio Basto <sergio@serjux.com> - 17.6.0-1
- Update smplayer to 17.6.0

* Mon May 08 2017 Sérgio Basto <sergio@serjux.com> - 17.5.0-1
- Update smplayer and smtube to 17.5.0

* Sat Apr 22 2017 Sérgio Basto <sergio@serjux.com> - 17.4.2-1
- Update smplayer to 17.4.2

* Thu Apr 06 2017 Sérgio Basto <sergio@serjux.com> - 17.4.0-1
- Update smplayer to 17.4.0

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 17.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 11 2017 Sérgio Basto <sergio@serjux.com> - 17.3.0-1
- Update smplayer to 17.3.0 and smplayer-themes to 17.2.0

* Fri Feb 03 2017 Sérgio Basto <sergio@serjux.com> - 17.2.0-2
- Better read %setup options and better rhel requires

* Fri Feb 03 2017 Sérgio Basto <sergio@serjux.com> - 17.2.0-1
- Update smplayer to 17.2.0 and smtube to 17.1.0

* Thu Jan 26 2017 Sérgio Basto <sergio@serjux.com> - 17.1.0-2
- el7 support
- Some syncs with upstream spec, quazip-qt5-devel is not
  needed anymore.

* Tue Jan 24 2017 Sérgio Basto <sergio@serjux.com> - 17.1.0-1
- Update smplayer to 17.1.0

* Wed Nov 16 2016 Sérgio Basto <sergio@serjux.com> - 16.11.0-2
- Test weak_deps on RPM Fusion

* Sun Nov 06 2016 Sérgio Basto <sergio@serjux.com> - 16.11.0-1
- Update smplayer to 16.11.0 and themes to 16.8.0
- Weak deps is not working in RPMFusion packages

* Sat Nov 05 2016 Leigh Scott <leigh123linux@googlemail.com> - 16.9.0-2
- Add requires mplayer-backend (rfbz#4284)

* Sat Sep 10 2016 Sérgio Basto <sergio@serjux.com> - 16.9.0-1
- Update smplayer tp 16.9.0

* Tue Aug 16 2016 Sérgio Basto <sergio@serjux.com> - 16.8.0-4
- Fix translation.

* Tue Aug 16 2016 Sérgio Basto <sergio@serjux.com> - 16.8.0-3
- More reviews, with Vascom, rfbz #4187, fix cflags in builds

* Tue Aug 09 2016 Sérgio Basto <sergio@serjux.com> - 16.8.0-2
- Recommends mplayer instead Requires, rfbz #4068

* Mon Aug 08 2016 Sérgio Basto <sergio@serjux.com> - 16.8.0-1
- Update smplayer tp 16.8.0
- Separate smtube package rfbz #4171

* Sat Jul 23 2016 Sérgio Basto <sergio@serjux.com> - 16.7.0-3
- Package scriplets review, based on RussianFedora work
  https://github.com/RussianFedora/smplayer

* Tue Jul 19 2016 Sérgio Basto <sergio@serjux.com> - 16.7.0-2
- Add patch to fix build in rawhide

* Sun Jul 17 2016 Sérgio Basto <sergio@serjux.com> - 16.7.0-1
- Update smplayer to 16.7.0 and smtube to 16.7.2
- Install smplayer-themes and smplayer-skins
- Few more cleanup, especially in docs and licenses.

* Sun Jul 17 2016 Sérgio Basto <sergio@serjux.com> - 16.6.0-2
- Switch builds to Qt5
- Do not apply a vendor tag to .desktop files (using --vendor).
- Drop old smplayer_enqueue.desktop

* Wed Jun 22 2016 Sérgio Basto <sergio@serjux.com> - 16.6.0-1
- Update to 16.6.0

* Fri Apr 01 2016 Sérgio Basto <sergio@serjux.com> - 16.4.0-1
- Update to 16.4.0

* Sun Jan 17 2016 Sérgio Basto <sergio@serjux.com> - 16.1.0-1
- Update 16.1.0

* Sun Dec 06 2015 Sérgio Basto <sergio@serjux.com> - 15.11.0-1
- Update smplayer and smtube 15.11.0

* Fri Oct 02 2015 Sérgio Basto <sergio@serjux.com> - 15.9.0-1
- Update smplayer to 15.9.0 and smtube to 15.9.0 .

* Thu Aug 20 2015 Sérgio Basto <sergio@serjux.com> - 14.9.0.6994-2
- Update smtube to 15.8.0 .
- Removed version of package from _docdir directory (following the guidelines).

* Wed Jun 17 2015 Sérgio Basto <sergio@serjux.com> - 14.9.0.6994-1
- Update to 4.9.0.6994 .
- Drop smplayer-14.9.0-get_svn_revision.patch .

* Mon Jun 08 2015 Sérgio Basto <sergio@serjux.com> - 14.9.0.6966-3
- Added smplayer-14.9.0-get_svn_revision.patch, I think is better have a
  hardcore version than (svn r0UNKNOWN)

* Sun Jun 07 2015 Sérgio Basto <sergio@serjux.com> - 14.9.0.6966-2
- Update to smtube-15.5.17

* Sat Jun 06 2015 Sérgio Basto <sergio@serjux.com> - 14.9.0.6966-1
- Update to smplayer-14.9.0.6966 and smtube-15.5.10
- Fix warning "The desktop entry file "ServiceMenus/smplayer_enqueue.desktop
  has an empty mimetype! " .
- Rebase patches 2 and 3 .

* Wed Mar 25 2015 Sérgio Basto <sergio@serjux.com> - 14.9.0.6690-1
- Update smplayer to smplayer-14.9.0.6690 and smtube to smtube-15.1.26

* Mon Sep 15 2014 Sérgio Basto <sergio@serjux.com> - 14.9.0-1
- New upstream releases smplayer 14.9.0 and smtube 14.8.0
- Rebase patches 1 and 3 .

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 14.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Apr 04 2014 Sérgio Basto <sergio@serjux.com> - 14.3.0-1
- New upstream release, Previous version was 0.8.6, this new release is 14.3...
  What happened? Now the version is just the year and month of the release.
- Patches refactor.

* Tue Oct 01 2013 Sérgio Basto <sergio@serjux.com> - 0.8.6-1
- Update smplayer to 0.8.6 and smtube to 1.8

* Mon May 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.5-2
- Rebuilt for x264/FFmpeg

* Sat May 11 2013 Sérgio Basto <sergio@serjux.com> - 0.8.5-1
- Update smplayer to 0.8.5 and smtube to 1.7
- Fix patches smplayer-0.8.3-smtube-system-qtsingleapplication and
  smplayer-0.8.1-system-qtsingleapplication.patch for 0.8.5 and smtube 1.7

* Mon Mar 25 2013 Sérgio Basto <sergio@serjux.com> - 0.8.4-2
- New tag 

* Mon Mar 25 2013 Sérgio Basto <sergio@serjux.com> - 0.8.4-1
- New upsteam release.
- Drop "updates *.desktop with video/webm;" on patch smplayer-0.8.3-desktop-files.patch.
- Fix patch smplayer-0.8.3-smtube-system-qtsingleapplication.patch 
- Fix dates on changelog specs.

* Thu Jan 10 2013 Sérgio Basto <sergio@serjux.com> - 0.8.3-2
- bug #2635, Update *.desktop with video/webm; mimetype support, as upstream do in svn r5005.

* Mon Dec 24 2012 Sérgio Basto <sergio@serjux.com> - 0.8.3-1
- New updates to smplayer-0.8.3 and smtube-1.5 . Fix for Youtube playback.

* Mon Dec 17 2012 Sérgio Basto <sergio@serjux.com> - 0.8.2.1-1
- New updates to smplayer-0.8.2.1 and smtube-1.4 .

* Sun Nov 25 2012 Sérgio Basto <sergio@serjux.com> - 0.8.2-3
- now smtube new source b372bd396c068aa28798bf2b5385bf59  smtube-1.3.tar.bz2 .

* Sun Nov 25 2012 Sérgio Basto <sergio@serjux.com> - 0.8.2-2
- 0.8.2 new source 0dee3f9a4f0d87d37455efc800f9bba7 smplayer-0.8.2.tar.bz2 this one has some minor
  fixes ... , smplayer-0.8.2.tar.bz2 was announced at 2012-11-24. 

* Thu Nov 22 2012 Sérgio Basto <sergio@serjux.com> - 0.8.2-1
- New upsteam release.

* Thu Sep 27 2012 Sérgio Basto <sergio@serjux.com> - 0.8.1-2
- fix rfbz #2488

* Thu Sep 20 2012 Sérgio Basto <sergio@serjux.com> - 0.8.1-1
- New upsteam release.
- rfbz #2113, all done by Nucleo.

* Sat Apr 28 2012 Sérgio Basto <sergio@serjux.com> - 0.8.0-2
- fix smtube translations.
- drop support for Fedora < 9 and EPEL 5, since we need kde4.

* Sat Apr 28 2012 Sérgio Basto <sergio@serjux.com> - 0.8.0-1 
- New release
- add smtube support
- use system qtsingleapplication
- a little review with: fedora-review -n smplayer --mock-config fedora-16-i386

* Sat Mar 24 2012 Sérgio Basto <sergio@serjux.com> - 0.7.1-1
- New upstream version: 0.7.1, changelog says "This version includes some bug fixes, 
  some of them important. It's highly recommended to update." 
- Remove some bundle sources.
- Small fixes in patches to fit on 0.7.1.

* Sat Mar 24 2012 Sérgio Basto <sergio@serjux.com> - 0.7.0-3
- Add a patch to remove bundled quazip shlibs and Requires kde-filesystem, bug rfbz #1164
- Removed tag BuildRoot.

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.0-2
- Rebuilt for c++ ABI breakage

* Tue Feb 7 2012 Sérgio Basto <sergio@serjux.com> - 0.7.0-1
- new upstream version: 0.7.0

* Mon May 24 2010 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.9-2
- #1217: fix regression in Thunar

* Sat Apr 24 2010 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.9-1
- new upstream version: 0.6.9

* Sun Jun 28 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.8-1
- new upstream version: 0.6.8

* Sun Mar 29 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.7-1
- new upstream version: 0.6.7

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.6.6-2
- rebuild for new F11 features

* Sat Jan 10 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.6-1
- new upstream version: 0.6.6

* Thu Nov 13 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.5.1-1
- new upstream version: 0.6.5.1

* Wed Oct 29 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.4-1
- new upstream version: 0.6.4

* Mon Sep 29 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.3-1
- new upstream version: 0.6.3

* Fri Aug 15 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.2-1
- new upstream version: 0.6.2
- add servicemenus depending on the KDE version

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.6.1-4
- rebuild for buildsys cflags issue

* Tue Jul 22 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.1-3
- import into rpmfusion

* Tue Jul 08 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.1-2
- fix packaging of FAQs

* Tue Jun 17 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.1-1
- update to latest upstream version

* Sun Feb 24 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.0-0.3.rc2
- add %%{?_smp_mflags} in Makefile to really use it
- finally fix usage of macros
- mode 0644 for desktop-file isn't needed anymore

* Sat Feb 23 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.0-0.2.rc2
- Update %%post and %%postun scriplets
- use %%{?_smp_mflags} in make
- change vendor to rpmfusion in desktop-file-install
- some minor spec cleanups

* Thu Feb 14 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.0-0.1.rc2
- new upstream version: 0.6.0rc2

* Tue Feb 12 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.0-0.1.rc1
- new upstream version: 0.6.0rc1
- added docs: Changelog Copying.txt Readme.txt Release_notes.txt
- fix path of %%docdir in Makefile

* Tue Dec 18 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.62-1
- new version: 0.5.62
- specify license as GPLv2+

* Thu Sep 20 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.60-1
- Update to development version of qt4

* Thu Sep 20 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.21-1
- new upstream version: 0.5.21
- don't add category "Multimedia" to desktop-file
- correct url of Source0

* Sun Jul 29 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.20-1
- new upstream version: 0.5.20

* Mon Jun 18 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.14-1
- new upstream version: 0.5.14

* Thu Jun 14 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.7-1
- Initial Release
