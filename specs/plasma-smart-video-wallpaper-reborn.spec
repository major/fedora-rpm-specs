Name:           plasma-smart-video-wallpaper-reborn
Version:        2.3.2
Release:        1%{?dist}
Summary:        Play videos on your Plasma 6 Desktop/Lock Screen
License:        GPL-2.0-only
URL:            https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Plasma)

Requires:       plasma-desktop
Requires:       qt6-qtmultimedia
# Only a recommendation, unless they want to use "the other one"...
Recommends:     ffmpeg-free

%description
Plasma 6 wallpaper plugin to play videos on your Desktop/Lock Screen.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
chmod 755 %{buildroot}%{_datadir}/plasma/wallpapers/luisbocanegra.smart.video.wallpaper.reborn/contents/ui/tools/gdbus_get_signal.sh
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/luisbocanegra.smart.video.wallpaper.reborn.appdata.xml

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/plasma/wallpapers/luisbocanegra.smart.video.wallpaper.reborn/
%{_metainfodir}/luisbocanegra.smart.video.wallpaper.reborn.appdata.xml


%changelog
* Thu Aug 7 2025 Steve Cossette <farchord@gmail.com> - 2.3.2-1
- Initial Import
