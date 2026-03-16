%global alt_pkg_name swaync

Name:       SwayNotificationCenter
Version:    0.12.5
Release:    %autorelease
Summary:    Simple notification daemon with GTK GUI for SwayWM
License:    GPL-3.0-only
URL:        https://github.com/ErikReider/SwayNotificationCenter
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fish)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  scdoc
BuildRequires:  sassc
BuildRequires:  blueprint-compiler

Requires:       gvfs
Requires:       libnotify
Requires:       dbus
Requires:       dbus-common

Provides:   desktop-notification-daemon
Provides:   sway-notification-center = %{version}-%{release}
Provides:   %{alt_pkg_name} = %{version}-%{release}

%description
%{summary}.

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{alt_pkg_name}-bash-completion = %{version}-%{release}
Supplements:    (%{name} and bash-completion)

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}
Provides:       %{alt_pkg_name}-zsh-completion = %{version}-%{release}
Supplements:    (%{name} and zsh)

Requires:       zsh
Requires:       %{name} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}
Provides:       %{alt_pkg_name}-fish-completion = %{version}-%{release}
Supplements:    (%{name} and fish)

Requires:       fish
Requires:       %{name} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{name}

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post swaync.service

%preun
%systemd_user_preun swaync.service


%files
%doc README.md
%{_bindir}/swaync-client
%{_bindir}/swaync
%license COPYING
%dir %{_sysconfdir}/xdg/swaync
%config(noreplace) %{_sysconfdir}/xdg/swaync/configSchema.json
%config(noreplace) %{_sysconfdir}/xdg/swaync/config.json
%config(noreplace) %{_sysconfdir}/xdg/swaync/style.css
%{_userunitdir}/swaync.service
%{_datadir}/dbus-1/services/org.erikreider.swaync.service
%{_datadir}/dbus-1/services/org.erikreider.swaync.cc.service
%{_datadir}/glib-2.0/schemas/org.erikreider.swaync.gschema.xml
%{_mandir}/man1/swaync-client.1*
%{_mandir}/man1/swaync.1*
%{_mandir}/man5/swaync.5*

%files bash-completion
%{_datadir}/bash-completion/completions/swaync
%{_datadir}/bash-completion/completions/swaync-client

%files zsh-completion
%{_datadir}/zsh/site-functions/_swaync
%{_datadir}/zsh/site-functions/_swaync-client

%files fish-completion
%{_datadir}/fish/vendor_completions.d/swaync-client.fish
%{_datadir}/fish/vendor_completions.d/swaync.fish

%changelog
%autochangelog
