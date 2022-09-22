%global AName GitQlient

Name:       gitqlient
Version:    1.4.3
Release:    3%{?dist}
Summary:    Multi-platform Git client

# Required 'qt5-qtwebengine' which is not available on some arches.
# https://src.fedoraproject.org/rpms/qt5-qtwebengine/blob/rawhide/f/qt5-qtwebengine.spec#_113
ExclusiveArch: %{qt5_qtwebengine_arches}

License:    LGPLv2+
URL:        https://github.com/francescmm/GitQlient
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5WebChannel)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)
BuildRequires: pkgconfig(Qt5Widgets)

Requires:   git-core
Requires:   hicolor-icon-theme

Provides:   bundled(marked)

%description
GitQlient, pronounced as git+client (/gɪtˈklaɪənt/) is a multi-platform Git
client originally forked from QGit. Nowadays it goes beyond of just a fork and
adds a lot of new functionality.

Some of the major feature you can find are:

  1. New features:

    * Easy access to remote actions like: push, pull, submodules management
      and branches
    * Branches management
    * Tags and stashes management
    * Submodules handling
    * Allow to open several repositories in the same window
    * Better visualization of the commits and the work in progress
    * Better visualization of the repository view
    * GitHub/GitLab integration
    * Embedded text editor with syntax highlight for C++

  2. Improved UI experience

    * Easy access to the main Git actions
    * Better code separation between Views and Models
    * Simplification of the different options one can do, keeping it to what a
      Git client is


%prep
%autosetup -n %{AName}-%{version} -p1


%build
%qmake_qt5 \
    PREFIX=%{_prefix} \
    %{AName}.pro \
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 30 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.3-1
- build(update): 1.4.3

* Sat Aug 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.1-1
- build(update): 1.4.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.0-1
- build(update): 1.4.0

* Tue Apr 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.2-1
- Initial package
