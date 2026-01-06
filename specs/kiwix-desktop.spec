Name: kiwix-desktop
Version: 2.5.1
Release: %autorelease

License: GPL-3.0-or-later
Summary: Kiwix desktop application

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: libkiwix-devel
BuildRequires: libzim-devel
BuildRequires: mustache-devel
BuildRequires: pugixml-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtwebengine-devel
BuildRequires: qtsingleapplication-qt6-devel

BuildRequires: aria2
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make

Requires: aria2%{?_isa}
Requires: hicolor-icon-theme
Requires: qt6-qtsvg%{?_isa}
Requires: shared-mime-info

# Required qt6-qtwebengine is not available on some arches.
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
The Kiwix-desktop is a view/manager of zim files for GNU/Linux
and Windows. You can download and view your zim files as you
which.

%prep
%autosetup -p1
mkdir %{_vpath_builddir}
sed -e "/static {/,+2d" -i %{name}.pro
rm -rf subprojects

%build
pushd %{_vpath_builddir}
    %qmake_qt6 PREFIX=%{_prefix} CONFIG+=qtsingleapplication ..
popd

%make_build -C %{_vpath_builddir}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_vpath_builddir}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.appdata.xml

%changelog
%autochangelog
