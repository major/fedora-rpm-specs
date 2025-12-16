%global forgeurl https://github.com/bk138/gromit-mpx
Version:        1.8.0
%global tag %{version}
%forgemeta

Name:           gromit-mpx
Release:        %autorelease
Summary:        An on-screen annotation tool
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(liblz4)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Gromit-MPX is an on-screen annotation tool that works with any Unix desktop
environment under X11 as well as Wayland.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \

%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml

%files -f %{name}.lang
%license COPYING
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/net.christianbeier.Gromit-MPX.desktop
%{_metainfodir}/net.christianbeier.Gromit-MPX.appdata.xml
%{_mandir}/man1/gromit-mpx.1*
%{_datadir}/doc/%{name}/

%changelog
%autochangelog
