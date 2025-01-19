%global libmediainfo_version    23.10
%global libzen_version          0.4.41

Name:           mediaconch
Version:        23.10
Release:        6%{?dist}
Summary:        Most relevant technical and tag data for video and audio files (CLI)

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://mediaarea.net/MediaConch/
Source0:        https://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libmediainfo) >= %{libmediainfo_version}
BuildRequires:  pkgconfig(libzen) >= %{libzen_version}
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebengine-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(jansson)
BuildRequires:  systemd
BuildRequires:  libappstream-glib

ExclusiveArch:  %{qt5_qtwebengine_arches}


%description
MediaConch is an implementation checker, policy checker, reporter,
and fixer that targets preservation-level audiovisual files
(specifically Matroska, Linear Pulse Code Modulation (LPCM)
and FF Video Codec 1 (FFV1)).

This project is maintained by MediaArea and funded by PREFORMA.

This package includes the command line interface.

%package gui
Summary:    Supplies technical and tag information about a video or audio file (GUI)
Requires:   hicolor-icon-theme

%description gui
MediaConch is an implementation checker, policy checker, reporter,
and fixer that targets preservation-level audiovisual files
(specifically Matroska, Linear Pulse Code Modulation (LPCM)
and FF Video Codec 1 (FFV1)).

This project is maintained by MediaArea and funded by PREFORMA.

This package includes the graphical user interface.

%package server
Summary:    Supplies technical and tag information about a video or audio file (Server)
%{?systemd_requires}

%description server
MediaConch is an implementation checker, policy checker, reporter,
and fixer that targets preservation-level audiovisual files
(specifically Matroska, Linear Pulse Code Modulation (LPCM)
and FF Video Codec 1 (FFV1)).

This project is maintained by MediaArea and funded by PREFORMA.

This package includes the server.

%prep
%autosetup -n MediaConch
rm -rf Source/ThirdParty/sqlite
sed -i 's/.$//' *.txt *.html Release/*.txt

sed -i 's/AC_PROG_LIBTOOL/LT_INIT([disable-static])/' Project/GNU/CLI/configure.ac
sed -i 's/AC_PROG_LIBTOOL/LT_INIT([disable-static])/' Project/GNU/Server/configure.ac

pushd Project/GNU/CLI
    autoreconf -fiv
popd

pushd Project/GNU/Server
    autoreconf -fiv
popd


%build
# build CLI
pushd Project/GNU/CLI
    %configure --enable-static=no
    %make_build
popd

# build server
pushd Project/GNU/Server
    %configure --enable-static=no
    %make_build
popd

# now build GUI
pushd Project/Qt
    %{qmake_qt5}
    %make_build
popd


%install
pushd Project/GNU/CLI
    %make_install
popd

pushd Project/GNU/Server
    %make_install
popd

pushd Project/Qt
    install -dm 755 %{buildroot}%{_bindir}
    install -m 755 -p mediaconch-gui %{buildroot}%{_bindir}
popd

# icon
install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 -p Source/Resource/Image/MediaConch.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 -p Source/Resource/Image/MediaConch.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu-entry
install -dm 755 %{buildroot}%{_datadir}/applications
install -m 644 -p Project/GNU/GUI/mediaconch-gui.desktop %{buildroot}%{_datadir}/applications

desktop-file-install --dir="%{buildroot}%{_datadir}/applications" -m 644 Project/GNU/GUI/mediaconch-gui.desktop

install -dm 755 %{buildroot}%{_datadir}/appdata/
install -m 644 -p Project/GNU/GUI/mediaconch-gui.metainfo.xml %{buildroot}%{_datadir}/appdata/mediaconch-gui.appdata.xml

install -dm 755 %{buildroot}%{_unitdir}
install -m 644 -p Project/GNU/Server/mediaconchd.service  %{buildroot}%{_unitdir}/mediaconchd.service

install -dm 755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -p Project/GNU/Server/MediaConch.rc  %{buildroot}%{_sysconfdir}/%{name}/MediaConch.rc

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%post server
%systemd_post mediaconchd.service

%preun server
%systemd_preun mediaconchd.service

%postun server
%systemd_postun_with_restart mediaconchd.service

%files
%doc Release/ReadMe_CLI_Linux.txt History_CLI.txt
%license LICENSE License.html
%{_bindir}/mediaconch

%files server
%doc Documentation/Daemon.md Documentation/Config.md
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/mediaconchd
%{_unitdir}/mediaconchd.service


%files gui
%doc Release/ReadMe_GUI_Linux.txt History_GUI.txt
%license LICENSE License.html
%{_bindir}/mediaconch-gui
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/appdata/mediaconch-gui.appdata.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 23.10-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 23.10-1
- Update to 23.10

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 23.07-1
- Update to 23.07

* Sat Apr 01 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 23.03-1
- Update to 23.03

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 29 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.09-1
- Update to 22.09

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 02 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.03-1
- Update to 22.03

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 28 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-17
- Rebuild with new mediainfo 21.03

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 18.03.2-16
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-14
- Rebuild for libevent soname change

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-12
- Rebuild with new mediainfo 20.03

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-10
- Rebuild with new mediainfo 19.09

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-8
- Rebuild with new mediainfo 19.07

* Wed Apr 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-7
- Rebuild with new mediainfo 19.04

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-5
- Rebuild with new mediainfo 18.12

* Tue Sep 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-4
- Rebuild with new mediainfo 18.08.1

* Mon Sep 03 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-3
- Rebuild with new mediainfo

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03.2-1
- Update to 18.03.2

* Tue Mar 20 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03-1
- Update to 18.03

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.12-1
- Update to 17.12

* Tue Dec 12 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.11-1
- Update to 17.11

* Fri Dec 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.08-3
- Rebuild due to libmediainfo .so version change

* Fri Nov 10 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.08-2
- Rebuild for new libmediainfo

* Wed Sep 13 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.08-1
- Update to 17.08

* Mon Aug 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.07-1
- Update to 17.07

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.06-3
- AC_PROG_LIBTOOL -> LT_INIT

* Wed Jul 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.06-2
- Clean spec

* Fri Jul 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.06-1
- Update to 17.06

* Thu Jun 29 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.05-1
- Update to 17.05

* Thu Apr 13 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.03-1
- Update to 17.03

* Thu Apr 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.02-1
- Update to 17.02

* Thu Feb 09 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.01-1
- Update to 17.01

* Mon Jan 09 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 16.12-1
- Update to 16.12

* Fri Dec 09 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.11-1
- Update to 16.11

* Thu Nov 24 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.10-1
- Update to 16.10

* Fri Oct 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.09-1
- Update to 16.09

* Wed Sep 21 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.08-1
- Update to 16.08

* Mon Aug 01 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.07-1
- Update to 16.07

* Wed Jul 06 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.06-1
- Update to 16.06

* Wed Jun 01 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.05-1
- Update to 16.05

* Thu May 05 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.04-1
- Update to 16.04

* Tue Apr 26 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.03-3
- Add validate appdata XML

* Tue Apr 26 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.03-2
- Add appdata XML
- Switch BRs to use pkgconfig
- Add systemd unit for mediaconchd

* Tue Apr 12 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.03-1
- Update to 16.03

* Wed Mar 02 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 16.02-1
- Update to 16.02
- add %%license macro

* Wed Feb 10 2016 Vasiliy N. Glazov <vascom2@gmail.com> 16.01-1
- Initial release
