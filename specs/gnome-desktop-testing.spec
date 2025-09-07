%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)

Name:           gnome-desktop-testing
Version:        2021.1
Release:        %autorelease
Summary:        GNOME test runner for installed tests

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/gnome-desktop-testing
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  git automake autoconf libtool
BuildRequires:  make

%description
gnome-desktop-testing-runner is a basic runner for tests that are
installed in /usr/share/installed-tests.  For more information, see
"https://wiki.gnome.org/Initiatives/GnomeGoals/InstalledTests"

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/gnome-desktop-testing-runner
%{_bindir}/ginsttest-runner
%{_mandir}/man1/ginsttest-runner.1.gz
%{_mandir}/man1/gnome-desktop-testing-runner.1.gz

%changelog
%autochangelog
