%bcond system_qtsingleapplication %{undefined flatpak}

%global smplayer_themes_ver 20.11.0
%global smplayer_skins_ver 20.11.0

Name:           smplayer
Version:        25.6.0
Release:        %autorelease
Summary:        Graphical frontend for mplayer and mpv

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
%autochangelog
