Name:           qdirstat
Version:        1.9
Release:        %autorelease
Summary:        Qt-based directory statistics

License:        GPL-2.0-only
URL:            https://github.com/shundhammer/qdirstat
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       qt5-qtbase
Requires:       hicolor-icon-theme

%description
QDirStat is a graphical application to show where your disk space has gone
and to help you to clean it up.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
 latest Qt 5. It does not need any KDE libs or infrastructure. It runs on
 every X11-based desktop on Linux, BSD and other Unix-like systems.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{qmake_qt5}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/qdirstat.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license LICENSE
%{_docdir}/%{name}/
%{_bindir}/qdirstat
%{_bindir}/qdirstat-cache-writer
%{_mandir}/man1/qdirstat-cache-writer.1.*
%{_mandir}/man1/qdirstat.1.*
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
%autochangelog
