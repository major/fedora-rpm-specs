%global forgeurl https://github.com/luebking/phototonic
Version:        3.1.0
%forgemeta

Name:           phototonic
Release:        %autorelease
Summary:        Image viewer and organizer

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Phototonic is a fast and functional image viewer and organizer, inspired by the
traditional image viewer design (i.e. thumbnails and viewer layouts).

%prep
%forgeautosetup -p1

%build
%qmake_qt6
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"
%find_lang phototonic --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f phototonic.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
