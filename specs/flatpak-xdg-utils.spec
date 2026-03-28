Name:     flatpak-xdg-utils
Summary:  Command-line tools for use inside Flatpak sandboxes
Version:  1.0.6
Release:  %autorelease
License:  LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:      https://github.com/flatpak/flatpak-xdg-utils
Source:   https://github.com/flatpak/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)

Requires: flatpak-spawn%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This package contains a number of command-line utilities for use inside
Flatpak sandboxes. They work by talking to portals.

%package -n     flatpak-spawn
Summary:        Command-line frontend for the org.freedesktop.Flatpak service
License:        LGPL-2.1-or-later

%description -n flatpak-spawn
This package contains the flatpak-spawn command-line utility. It can be
used to talk to the org.freedesktop.Flatpak service to spawn new sandboxes,
run commands on the host, or use one of the session or system helpers.

%package tests
Summary:   Tests for %{name}
License:   LGPL-2.1-or-later AND MIT
Requires:  %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:  flatpak-spawn%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description tests
This package contains installed tests for %{name}.

%prep
%autosetup

%build
%meson -Dinstalled_tests=true
%meson_build

%install
%meson_install

mv $RPM_BUILD_ROOT%{_bindir}/xdg-email $RPM_BUILD_ROOT%{_bindir}/flatpak-xdg-email
mv $RPM_BUILD_ROOT%{_bindir}/xdg-open $RPM_BUILD_ROOT%{_bindir}/flatpak-xdg-open

%files
%doc README.md
%license COPYING
%{_bindir}/flatpak-xdg-email
%{_bindir}/flatpak-xdg-open

%files -n flatpak-spawn
%license COPYING
%{_bindir}/flatpak-spawn

%files tests
%{_datadir}/installed-tests
%{_libexecdir}/installed-tests

%changelog
%autochangelog
