%bcond_without tests
# /etc/xdg is recommended since v1.7
%global   dunst_confdir %{_sysconfdir}/xdg

Name:     dunst
Version:  1.12.1
Release:  %autorelease
Summary:  Lightweight and customizable notification-daemon
License:  BSD-3-Clause
URL:      https://dunst-project.org
Source:   https://github.com/dunst-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:    https://github.com/dunst-project/dunst/pull/1422.patch#./0001-Change-type-of-bool-to-gboolean.patch

Requires: dbus
# Required for dunstctl
Requires: /usr/bin/dbus-send
# xdg-open is the default 'browser' for opening URLs
Recommends: /usr/bin/xdg-open
# jq is used in completion definitions
Recommends: jq

# keep this sorted please
BuildRequires: /usr/bin/pod2man
BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.44
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr) >= 1.5
BuildRequires: pkgconfig(xscrnsaver)
%if %{with tests}
# tests require DBus
BuildRequires: dbus-daemon
# SVG pixbuf loader
BuildRequires: librsvg2
%endif

Provides: desktop-notification-daemon


%description
Dunst is a lightweight replacement for the notification daemons provided by
most desktop environments. It’s very customizable, isn’t dependent on any
toolkits, and therefore fits into those window manager centric setups we all
love to customize to perfection.

%prep
%autosetup -p1


%build
%global make_options %{shrink:
    PREFIX=%{_prefix}
    SYSCONFDIR=%{dunst_confdir}
    SYSTEMD=1
    VERSION=%{version}
}
%set_build_flags
%make_build %{make_options} wayland-protocols
%make_build %{make_options}


%install
%make_install %{make_options}
# create directory for config drop-in files
install -d -m 0755 -pv %{buildroot}%{dunst_confdir}/%{name}/dunstrc.d


%if %{with tests}
%check
%make_build test %{make_options}
%endif


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%doc AUTHORS CHANGELOG.md README.md RELEASE_NOTES
%license LICENSE
%dir %{dunst_confdir}/%{name}
%dir %{dunst_confdir}/%{name}/dunstrc.d
%config(noreplace) %{dunst_confdir}/%{name}/dunstrc
%{_bindir}/%{name}
%{_bindir}/dunstctl
%{_bindir}/dunstify
%{_datadir}/dbus-1/services/org.knopwob.%{name}.service
%{_userunitdir}/%{name}.service
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man5/%{name}.5*
%{bash_completions_dir}/dunst*
%{fish_completions_dir}/dunst*
%{zsh_completions_dir}/_dunst*

%changelog
%autochangelog
