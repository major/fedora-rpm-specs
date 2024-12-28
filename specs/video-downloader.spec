%global uuid    com.github.unrud.VideoDownloader

Name:           video-downloader
Version:        0.12.21
Release:        %autorelease
Summary:        Download videos from websites like YouTube and many others

License:        GPL-3.0-or-later
URL:            https://github.com/Unrud/video-downloader
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gtk-update-icon-cache
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  meson >= 0.59
BuildRequires:  python3-devel

BuildRequires:  pkgconfig(glib-2.0)

Requires:       gtk4
Requires:       hicolor-icon-theme
Requires:       libadwaita >= 1.2.0
Requires:       python3-xlib
Requires:       yt-dlp

%description
Download videos from websites with an easy-to-use interface. Provides the
following features:

  * Convert videos to MP3
  * Supports password-protected and private videos
  * Download single videos or whole playlists
  * Automatically selects a video format based on your preferred resolution

Based on yt-dlp.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.{png,svg}
%{_metainfodir}/*.xml


%changelog
%autochangelog
