%global usesnapshot 0
%global commit0 5f80bc4c5d0cb532f1a5ad9679d56bd16db89414
%if 0%{?usesnapshot}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20241205
%endif
%global metadata_name org.guayadeque.guayadeque

Name:           guayadeque
%if 0%{?usesnapshot}
Version:        0.6.2
Release:        0.2.beta6.git%{shortcommit0}%{dist}
%else
Version:        0.6.2
Release:        2%{?dist}
%endif
Summary:        Music player
# The entire source code is GPL-3.0-or-later except hmac/ which is BSD-3-Clause
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/thothix/guayadeque
%if 0%{?usesnapshot}
Source0:        %url/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
# For a breakdown of the licensing, see PACKAGE-LICENSING
Source1:        PACKAGE-LICENSING

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  taglib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgpod-devel
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sqlite-devel
BuildRequires:  wxGTK-devel
BuildRequires:  wxsqlite3-devel
BuildRequires:  dbus-devel
BuildRequires:  gettext-devel
Suggests:       gstreamer1-libav

Provides:       bundled(md5-polstra)

%description
Guayadeque is a lightweight and easy-to-use music player and music collection
organizer that can easily manage large music collections and supports smart
playlists.
In the technical side, it's written in C++, uses the wxWidget toolkit and the
Gstreamer media framework.

Main features include:

  - Play mp3, ogg, flac, wav, wma, mpc, mp4, ape, ...
  - Read and write tags in all supported formats.
  - Smart play mode that add tracks that fit your music taste using the tracks
    in the playlist.
  - Allow to catalogue your music using labels. Any track, artist or album can
    have as many labels you want.
  - Allow fast access to any music file by genre, artist, album
  - Audio equalizer
  - Configurable cross fader engine
  - Configurable Silence detector to avoid listening to silence between tracks
  - Dynamic and static playlists management.
  - Tracks tag editor with automatically fetching of tags information for easily
    completion.
  - Ability to download covers manually or automatically
  - Lyrics downloads from different lyrics providers.
  - You can rate the tracks from 0 to 5 stars.
  - Desktop notifications.
  - MPRIS D-Bus interface support so it can easily controlled from music applets
    for example.
  - Allow to resume play status and position when closed and reopened.
  - Allow to subscribe to podcasts and download all new episodes automatically
    or manually.
  - Play and Record shoutcast radios
  - Suggest music using last.fm service.
  - Last.fm audioscrobbling support.
  - Easily expandable contextual links support. With it you can find information
    about a track, an artist or an album on your favourite site.
  - Easily expandable contextual commands support. For example you can right
    click on any album and click in option to record the album in a burning
     application.
  - Option to copy the selection you want to a directory or device like USB
    players and IPod using a configurable pattern.
  - Partial GNOME session support to detect when GNOME session is about to
    close and save the play list so it can continue next time with the same
    tracks.
  - and many more.

%define         lang_subpkg() \
%package        langpack-%{1}\
Summary:        %{2} language data for %{name}\
BuildArch:      noarch \
Requires:       %{name} = %{version}-%{release}\
Supplements:    (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description    langpack-%{1}\
%{2} language data for %{name}.\
\
%files          langpack-%{1}\
%{_datadir}/locale/%{1}*/LC_MESSAGES/%{name}.mo

%lang_subpkg bg Bulgarian
%lang_subpkg ca_ES Catalan
%lang_subpkg cs Czech
%lang_subpkg da Danish
%lang_subpkg de German
%lang_subpkg el Greek
%lang_subpkg es Spanish
%lang_subpkg fr French
%lang_subpkg hr Croatian
%lang_subpkg hu Hungarian
%lang_subpkg is Icelandic
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg lt Lithuanian
%lang_subpkg ms "Malay (Malaysia)"
%lang_subpkg nb Norwegian
%lang_subpkg nl Dutch
%lang_subpkg pl Polish
%lang_subpkg pt Portuguese
%lang_subpkg pt_BR Brazil
%lang_subpkg ru Russian
%lang_subpkg sk Slovakian
%lang_subpkg sr "Serbian (Cyrillic and Latin)"
%lang_subpkg sv Swedish
%lang_subpkg th Thai
%lang_subpkg tr Turkish
%lang_subpkg uk Ukrainian

%prep
%if 0%{?usesnapshot}
%autosetup -p1 -n %{name}-%{commit0}
%else
%autosetup -p1 -n %{name}-%{version}
%endif
cp -p %{SOURCE1} PACKAGE-LICENSING

%build
%cmake .                                                       \
 -DCMAKE_BUILD_TYPE='Release'                                  \
 -DCMAKE_CXX_FLAGS="%{optflags}"                               \
 -D_GUREVISION_:STRING="%{release}"
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/{applications,appdata}
desktop-file-install --delete-original  \
        --dir %{buildroot}%{_datadir}/applications   \
        --remove-category Application \
        %{buildroot}%{_datadir}/applications/%{metadata_name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%doc README
%license INSTALL.md LICENSE PACKAGE-LICENSING
%{_bindir}/%{name}
%{_datadir}/%{name}/*.conf
%{_datadir}/%{name}/*.xml
%dir %{_datadir}/%{name}
%exclude %{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/applications/%{metadata_name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/metainfo/%{metadata_name}.metainfo.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 0.6.1-2
- Rebuild for ICU 76

* Wed Nov 13 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-1
- Correct license type
- Update to 0.6.1

* Sat Nov 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-1
- Add new github url
- Update to 0.6.0
- Convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-0.6.20230928gitd524675
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.4.8-0.5.20230928gitd524675
- Update to 0.4.8-0.5.20230928gitd524675
- Rebuilt for new wxsqlite3 version

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-0.4.20230319git1ae725a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-0.3.20230319git1ae725a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-0.2.20230319git1ae725a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.4.8-0.1.20230319git1ae725a
- Update to 0.4.8-0.1.20230319git1ae725a

* Fri Feb 24 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-1
- Update to 0.4.7
- Add guayadeque-ambiguous-overload.patch

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.41.20220801gita8b47a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.49.20220801gita8b47a6
- Rebuild without debug flag as long as https://github.com/anonbeat/guayadeque/issues/151 is not fixed

* Sun Aug 07 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.39.20220801gita8b47a6
- Rebuilt for wxversion 3.2
- Add guayadeque-wxwidgets-3.2.patch

* Thu Aug 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.38.20220801gita8b47a6
- Update to 0.4.7-0.38.20220801gita8b47a6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.37.20220618gitd947179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.36.20220618gitd947179
- Update to 0.4.7-0.36.20220618gitd947179

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.35.20211201git2aa235b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.34.20211201git2aa235b
- Update to 0.4.7-0.34.20211201git2aa235b

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 0.4.7-0.33.20210917git5eed2ee
- Rebuild (jsoncpp)

* Mon Sep 20 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.32.20210917git5eed2ee
- Update to 0.4.7-0.32.20210917git5eed2ee

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.31.20210415git79ec09d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.30.20210415git79ec09d
- Update to 0.4.7-0.30.20210415git79ec09d

* Mon Apr 12 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.29.20210412gitfb61dee
- Update to 0.4.7-0.29.20210412gitfb61dee

* Sat Apr 10 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.28.20210409gitdfc6b42
- Update to 0.4.7-0.28.20210409gitdfc6b42

* Fri Mar 19 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.27.20210319git37840c1
- Update to 0.4.7-0.27.20210319git37840c1
- Replace RR of gstreamer1-libav by Suggests

* Tue Mar 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.26.20210309git46cd022
- Update to 0.4.7-0.26.20210309git46cd022

* Tue Mar 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.25.20210308git592022f
- Update to 0.4.7-0.25.20210308git592022f
- Add BR pkgconfig(gstreamer-pbutils-1.0)
- Add RR gstreamer1-libav

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.24.20201230git3632ef8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.23.20201230git3632ef8
- Update to 0.4.7-0.23.20201230git3632ef8

* Tue Dec 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.22.20201222git407b183
- Update to 0.4.7-0.22.20201222git407b183

* Mon Dec 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.21.20201221git24353c0
- Update to 0.4.7-0.21.20201221git24353c0

* Sat Oct 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.20.20201013giteaa8597
- Update to 0.4.7-0.20.20201013giteaa8597

* Thu Oct 01 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.19.20200931git5bd2778
- Update to 0.4.7-0.19.20200931git5bd2778

* Tue Sep 01 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.18.20200831git5d2432e
- Update to 0.4.7-0.18.20200831git5d2432e

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.17.20200717git3c54f64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.16.20200716git3c54f64
- Update to 0.4.7-0.16.20200716git3c54f64
- Use %%cmake_build and %%cmake_install macros instead of %%make_build and %%make_install

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.4.7-0.15.20200528gited0b3ca
- Rebuild (jsoncpp)

* Thu May 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.14.20200528gited0b3ca
- Update to 0.4.7-0.14.20200528gited0b3ca

* Sun May 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.13.20200524gita066689
- Update to 0.4.7-0.13.20200524gita066689

* Sat May 23 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.12.20200522git41564bd
- Update to 0.4.7-0.12.20200522git41564bd

* Wed May 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.11.20200520git6be35ba
- Update to 0.4.7-0.11.20200520git6be35ba

* Fri May 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.10.20200507gitb08bddd
- Update to 0.4.7-0.10.20200507gitb08bddd
- Add BR pkgconfig(jsoncpp)

* Thu May 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.9.20200507git3d4ee2b
- Update to 0.4.7-0.9.20200507git3d4ee2b

* Mon Apr 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.8.20200427git42f77b6
- Update to 0.4.7-0.8.20200427git42f77b6

* Fri Apr 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.7.20200417git7de91e5
- Update to 0.4.7-0.7.20200417git7de91e5

* Thu Apr 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.6.20200415git08fe80e
- Update to 0.4.7-0.6.20200415git08fe80e

* Tue Feb 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.5.20200123git3ef808d
- Rebuilt

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.4.20200122git3ef808d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.3.20200123git3ef808d
- Update to 0.4.7-0.3.20200123git3ef808d

* Sun Dec 08 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.2.20191208git71b5e35
- Update to 0.4.7-0.2.20191208git71b5e35

* Fri Nov 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.1.20191117git89c6ab2
- Update to 0.4.7-0.1.20191117git89c6ab2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.6-1
- Update to stable 0.4.6

* Thu May 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.22.beta1gitddb8cbe
- Update to 0.4.5-0.22.beta1gitddb8cbe

* Tue Apr 16 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.21.beta1git093f588
- Update to 0.4.5-0.21.beta1git093f588

* Fri Apr 12 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.20.beta1gitdfc4acb
- Update to 0.4.5-0.20.beta1gitdfc4acb
- Add -DCMAKE_EXE_LINKER_FLAGS:STRING=-lwx_gtk3u_aui-3.0 due missing aui library

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.19.beta1git3b64a58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.18.beta13b64a58
- Update to 0.4.5-0.18.beta13b64a58

* Thu Sep 20 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.17.beta19688c4d
- Update to 0.4.5-0.17.beta19688c4d

* Thu Sep 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.16.beta1fa7ab20
- Update to 0.4.5-0.16.beta1gitfa7ab20

* Fri Aug 24 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.15.beta1gite7257da
- Update to 0.4.5-0.15.beta1gite7257da

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.14.beta1gitb3a7ec3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.13.beta1gitb3a7ec3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.12.beta1gitb3a7ec3
- Update to 0.4.5-0.12.beta1gitb3a7ec3

* Thu Oct 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.11.beta1git55efd99
- Update to 0.4.5-0.11.beta1git55efd99

* Sat Oct 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.10.beta1gitf4cd389
- Update to 0.4.5-0.10.beta1gitf4cd389

* Thu Aug 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.9.beta1git8137051
- Update to 0.4.5-0.9.beta1git8137051

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.8.beta1git35eaa95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.7.beta1git35eaa95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.6.beta1git35eaa95
- Update to 0.4.5-0.6.beta1git35eaa95

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.5.beta1gitc2d3854
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.4.beta1gitc2d3854
- Update to 0.4.5-0.4.beta1gitc2d3854

* Tue Jan 31 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.3.beta1gitfcf165e
- Update to 0.4.5-0.3.beta1gitfcf165e
- first version with proxy support

* Sun Jan 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.2.beta1git9fec4f7
- Update to 0.4.5-0.2.beta1git9fec4f7

* Sat Nov 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.1.beta1git5def972
- Update to 0.4.5-0.1.beta1git5def972

* Fri Nov 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.3-0.2.beta1git1943e6e
- Update to 0.4.3-0.2.beta1git1943e6e

* Fri Nov 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.3-0.1.beta1gitaf526c9
- Update to 0.4.3-0.1.beta1gitaf526c9

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.17.beta1git8706c86
- Update to 0.4.1-0.17.beta1git8706c86

* Sat Oct 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.16.beta1git45a439f
- Update to 0.4.1-0.16.beta1git45a439f

* Mon Oct 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.15.beta1gitf3a156b
- Update to 0.4.1-0.15.beta1gitf3a156b

* Thu Aug 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.14.beta1git6a66f9b
- Update to 0.4.1-0.14.beta1git6a66f9b

* Fri Jul 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.13.beta1gita2ae83e
- Update to 0.4.1-0.13.beta1gita2ae83e

* Mon Jul 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.12.beta1git2dbffbc
- Update to 0.4.1-0.12.beta1git2dbffbc
- First version with audio cd support
- Changed BR from gstreamer1-devel to gstreamer1-plugins-base-devel

* Wed Jun 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.11.beta1git1bc65f9
- Update to 0.4.1-0.11.beta1git1bc65f9
- Added BR libappstream-glib
- Added appdata.xml file
- Spec file cleanup

* Sat Jun 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.10.beta1git2420c01
- Update to 0.4.1-0.10.beta1git2420c01

* Mon Jun 13 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.9.beta1gitf6b11ba
- Dropped Provides: bundled(wxcurl) = wxcurl_version
  wxcurl was replaced by libcurl library directly
- Update to 0.4.1-0.9.beta1gitf6b11ba

* Wed Jun 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.8.beta1gitce1ab15
- Update to 0.4.1-0.8.beta1gitce1ab15

* Sun Jun 05 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.7.beta1git79b6383
- Documented licensing breakdown
- Added Provides: bundled(wxcurl) = wxcurl_version

* Sat Jun 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.6.beta1git79b6383
- Update to 0.4.1-0.6.beta1git79b6383
- Added wxWidgets to License tag
- Added %%dir %%{_datadir}/%%{name} because it's owned by the package
- modified macro for l10n subpackage

* Mon May 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.5.beta1git26eaf8d
- Update to 0.4.1-0.5.beta1git26eaf8d

* Wed May 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.4.beta1git13013ff
- Update to 0.4.1-0.4.beta1git13013ff
- Split locales into a l10n subpackage

* Sun May 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.3.beta1git35561f6
- Update to 0.4.1-0.3.beta1git35561f6
- Dropped BR subversion-devel
- Removed Group tag, it's obsolete
- Addes %%{name}-desktop.patch
- Dropped -DCMAKE_INSTALL_PREFIX='%%{_prefix}' because it's already in %%cmake macro 
- Changed -DCMAKE_BUILD_TYPE='Release' to -DCMAKE_BUILD_TYPE='Debug'

* Sun May 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.2.beta1gitd2c0281
- Update to 0.4.1-0.2.beta1gitd2c0281
- Mark license files as %%license where available
- Cleanup spec file

* Sat May 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.1.beta1git65f759c
- Update to 0.4.1-0.1.beta1git65f759c

* Sat Jul 04 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-10.svn1894
- rebuild for new svn release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-9.svn1893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.7-8.svn1893
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 05 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-7.svn1893
- dropped CMAKE_INSTALL_PREFIX because already sets by %%cmake macro
- rebuild for new wxsqlite3 version

* Fri Jan 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-6.svn1893
- added timeline patch to avoid crash on pause or stop

* Mon Jan 05 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-5.svn1893
- rebuild for new wxsqlite3 version

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-4.svn1893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-3.svn1893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-2.svn1893
- rebuild for new svn release

* Tue Apr 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-1.svn1891
- removed flac dependencies
- rebuild for new release

* Sat Jan 18 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-19.svn1890
- rebuild for new svn release

* Fri Jan 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-18.svn1889
- rebuild for new svn release

* Tue Dec 3 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-17.svn1887
- rebuild for new svn release
- added compiler flag to suppress "-Wno-unused-local-typedefs" warnings

* Tue Oct 22 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-16.svn1885
- added correct license type
- removed tabs in the spec file
- added %%desktop-database because desktop entry has a 'MimeType key.
- removing .svn directory will now used before building the tarball

* Mon Oct 21 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-15.svn1885
- added command to remove .svn dirs
- added %%cmake option for svn revision

* Mon Oct 14 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-14.svn1885
- rebuild
- corrected url address

* Wed Feb 13 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-13.svn1872
- rebuild

* Wed Dec 26 2012 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-12.svn1858
- removed %%cmake flags for wxsqlite3
- rebuild
- spec file cleanup

* Sun Dec 23 2012 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-11.svn1858
- rebuild for new svn release

* Sat Dec 1 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-10.svn1848
- changed %%cmake flag for new wxsqlite3 version 
- rebuild for new release 

* Sat Nov 24 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-9.svn1845
- update CMakeLists.patch and unbundle-wxsqlite3.patch for fedora 17 / 18

* Sat Nov 24 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-8.svn1845
- added wxsqlite3 build requirenment
- added CMakeLists.patch
- changed cmake flags
- spec file cleanup
- rebuild for new svn release

* Sun Oct 21 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-7.svn1830
- added unbundle-wxsqlite3.patch
- added command to remove src/wx/wxsql* src/wxsqlite3 from source

* Sat Sep 15 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-6.svn1830
- used %%{name} in file section
- removed unnecessary Requirements

* Sun Sep 9 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-5.svn1830
- added BSD license for HMAC-SHA implementation

* Sat Sep 8 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-4.svn1830
- removed  gcc-c++ build requirement
- removed %%defattr from file section

* Fri Sep 7 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-3.svn1830
- added patch for DSO linker problem on fedora 19
- added missing build requirements

* Tue Sep 4 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-2.svn1830
- changed release tag
- changed to buildroot variante
- removed uneeded macro _pkgbuilddir
- added Provides: bundled(md5-polstra)

* Thu Aug 30 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-2.svn1830
-  initial release for Fedora17 

