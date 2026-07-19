%global app_id  io.github.mpc_qt.mpc-qt

Name:           mpc-qt
Version:        26.07
Release:        %autorelease
Summary:        A clone of Media Player Classic reimplemented in Qt
# MainWindow::on_actionHelpAbout_triggered states "or later"
# qthelper.hpp is ISC
License:        GPL-2.0-or-later AND ISC
URL:            https://mpc-qt.github.io/
Source0:        https://github.com/mpc-qt/mpc-qt/archive/v%{version}/%{name}-%{version}.tar.gz
# data: Fix syntax in metainfo
Patch0:         https://github.com/mpc-qt/mpc-qt/commit/c8c491c8486d6f1638f245a76c1883673572076c.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

BuildRequires:  boost-devel
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(mpv)

BuildRequires:  xwayland-run

Requires:       hicolor-icon-theme

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Media Player Classic Home Cinema (mpc-hc) is considered by many to be the
quintessential media player for the Windows desktop.
Media Player Classic Qute Theater (mpc-qt) aims to reproduce most of the
interface and functionality of mpc-hc.

%prep
%autosetup -p1
rm -rf mpv-dev


%build
%cmake -DMPCQT_VERSION=%{version}
%cmake_build


%install
%cmake_install
rm -f %{buildroot}%{_datadir}/doc/mpc-qt/ipc.md


%check
xwfb-run -- %{buildroot}%{_bindir}/mpc-qt -v
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml


%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/mpc-qt
%{_datadir}/applications/%{app_id}*.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{app_id}.metainfo.xml


%changelog
%autochangelog
