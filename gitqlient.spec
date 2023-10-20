%global forgeurl https://github.com/francescmm/%{upstream_package_name}
%global tag v%{version}
%global upstream_package_name GitQlient

Name:       gitqlient
Version:    1.6.2
%forgemeta
Release:    %autorelease
Summary:    Multi-platform Git client written with Qt

# Required 'qt5-qtwebengine' which is not available on some arches.
# https://src.fedoraproject.org/rpms/qt5-qtwebengine/blob/rawhide/f/qt5-qtwebengine.spec#_113
ExclusiveArch: %{qt5_qtwebengine_arches}

License:    LGPL-2.1-or-later
URL:        %{forgeurl}
Source0:    %{url}/releases/download/v%{version}/%{name}_%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: git-core

BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)

Requires:   git-core
Requires:   hicolor-icon-theme
Requires:   qt5-qtsvg

%description
GitQlient, pronounced as git+client (/gɪtˈklaɪənt/) is a multi-platform Git
client originally forked from QGit. Nowadays it goes beyond of just a fork and
adds a lot of new functionality.

Some of the major feature you can find are:

  * Easy access to remote actions like: push, pull, submodules management and
    branches
  * Branches management
  * Tags and stashes management
  * Submodules handling
  * Allow to open several repositories in the same window
  * Better visualization of the commits and the work in progress
  * Better visualization of the repository view
  * GitHub/GitLab integration
  * Embedded text editor with syntax highlight for C++


%prep
%autosetup -n %{name}_%{version}


%build
%qmake_qt5 \
    PREFIX=%{_prefix} \
    %{upstream_package_name}.pro \
    %{nil}
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.{png,svg}


%changelog
%autochangelog
