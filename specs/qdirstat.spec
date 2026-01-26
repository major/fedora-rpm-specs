Name:           qdirstat
Version:        2.0
Release:        %autorelease
Summary:        Qt-based directory statistics

License:        GPL-2.0-only
URL:            https://github.com/shundhammer/qdirstat
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
QDirStat is a graphical application to show where your disk space has gone and
to help you to clean it up.

It shows the total size of directories and of their files both in a traditional
tree view and in a colored treemap graphics where a large file is shown as a
large rectangle, and small files are shown as small rectangles. Click on it, and
you will see where in the tree the file is, and you can instantly move it to the
trash if you like. The color corresponds to the file type: Images, videos or
whatever.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
latest Qt6. It does not need any KDE libs or infrastructure. It runs on every
X11-based desktop on Linux, BSD and other Unix-like systems, and in a Docker
container.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%qmake_qt6
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dp -m 644 metainfo/io.github.shundhammer.qdirstat.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/io.github.shundhammer.qdirstat.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%license LICENSE
%{_docdir}/%{name}/
%{_bindir}/qdirstat
%{_bindir}/qdirstat-cache-writer
%{_mandir}/man1/qdirstat-cache-writer.1.*
%{_mandir}/man1/qdirstat.1.*
%{_datadir}/metainfo/io.github.shundhammer.qdirstat.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
%autochangelog
