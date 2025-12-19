# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Git submodules
%global singleapplication_commit f1e15081dc57a9c03f7f4f165677f18802e1437a
%global singleapplication_shortcommit %(c=%{singleapplication_commit}; echo ${c:0:7})

Name: kdiskmark
Version: 3.2.0
Release: %autorelease
Summary: Simple open-source disk benchmark tool for Linux distros

License: GPL-3.0-or-later
URL: https://github.com/JonMagon/KDiskMark
Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source: https://github.com/itay-grudev/SingleApplication/archive/%{singleapplication_commit}/singleapplication-%{singleapplication_shortcommit}.tar.gz

### For next releases
# BuildRequires: libappstream-glib

BuildRequires: cmake >= 3.12
BuildRequires: cmake(PolkitQt5-1)
BuildRequires: cmake(Qt5Core) >= 5.9
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++

Requires: fio%{?_isa} >= 3.1
Requires: fio-engine-libaio%{?_isa}
Requires: hicolor-icon-theme

Provides: bundled(singleapplication) = 3.3.4

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user
interface. KDiskMark with its presets and powerful GUI calls Flexible I/O Tester
and handles the output to provide an easy to view and interpret comprehensive
benchmark result. The application is written in C++ with Qt and doesn't have any
KDE dependencies.


%prep
%autosetup -n KDiskMark-%{version}
%autosetup -n KDiskMark-%{version} -DT -a1

mv SingleApplication-%{singleapplication_commit}/* src/singleapplication/


%build
# TODO: Switch to Qt 6 on next build
%cmake -D USE_QT5=ON
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/polkit-1/actions/*.policy
%{_libexecdir}/kdiskmark_helper


%changelog
%autochangelog
