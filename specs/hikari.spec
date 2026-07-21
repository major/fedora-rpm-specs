Name:           hikari
Version:        3.0.0
Release:        %autorelease
Summary:        Stacking Wayland compositor with tiling capabilities
License:        BSD-2-Clause
URL:            https://codeberg.org/thomasadam/hikari
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildRequires:  bmake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  mk-files
BuildRequires:  pam-devel
BuildRequires:  pandoc-cli
BuildRequires:  pixman-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libucl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
Recommends:     xorg-x11-server-Xwayland

%description
Hikari is a stacking Wayland compositor with additional tiling capabilities, it
is heavily inspired by the Calm Window manager (cwm(1)). Its core concepts are
views, groups, sheets and the workspace.

%prep
%autosetup -n %{name}

%build
%set_build_flags
export CFLAGS_EXTRA="$CFLAGS"
export LDFLAGS_EXTRA="$LDFLAGS"
bmake WITH_POSIX_C_SOURCE=YES \
      WITH_XWAYLAND=YES \
      WITH_SCREENCOPY=YES \
      WITH_GAMMACONTROL=YES \
      WITH_LAYERSHELL=YES \
      WITH_VIRTUAL_INPUT=YES

%install
bmake DESTDIR=%{buildroot} \
      PREFIX=%{_prefix} \
      ETC_PREFIX="" \
      WITHOUT_SUID=YES \
      install

# FIXME: fix this in install/bmake process.
for binary in %{buildroot}/usr/bin/hikari %{buildroot}/usr/bin/hikari-unlocker; do
      chmod 0755 "${binary:?}"
done

%check
# No upstream tests are available

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/pam.d/%{name}-unlocker
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0755, root, root) %{_bindir}/%{name}
%attr(0755, root, root) %{_bindir}/%{name}-unlocker
%{_mandir}/man1/hikari.1*
%{_datadir}/backgrounds/%{name}/hikari_wallpaper.png
%{_datadir}/wayland-sessions/%{name}.desktop

%changelog
%autochangelog
