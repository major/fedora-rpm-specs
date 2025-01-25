# Build with Compiz session
# * Disable due minimum 'libcompizconfig' >= 0.9.14.0 version
%bcond_with compiz_session

Name:           gnome-flashback
Version:        3.54.0
Release:        %autorelease
Summary:        GNOME Flashback session

License:        GPL-3.0-or-later
URL:            https://wiki.gnome.org/Projects/GnomeFlashback
Source0:        https://download.gnome.org/sources/%{name}/3.54/%{name}-%{version}.tar.xz
Source1:        %{name}.pamd

# input-sources: use correct function to get attribute type (rhbz#2340243)
Patch0:         https://gitlab.gnome.org/GNOME/gnome-flashback/-/commit/1bb758374500e247ffab150205d05b72bf21b561.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32.2
BuildRequires:  pkgconfig(gdm)
BuildRequires:  pkgconfig(glib-2.0) >= 2.67.3
%ifnarch s390x
BuildRequires:  pkgconfig(gnome-bluetooth-3.0)
%endif
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 43
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 42.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.2
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.13
BuildRequires:  pkgconfig(libgnome-panel) >= 3.49
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.97
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi) >= 1.6.0
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr) >= 1.5.0
BuildRequires:  pkgconfig(xxf86vm) >= 1.1.4
%if %{with compiz_session}
BuildRequires:  pkgconfig(compiz)
BuildRequires:  pkgconfig(libcompizconfig) >= 0.9.14.0
%endif

Requires:       gnome-applets%{?_isa}
Requires:       gnome-keyring%{?_isa}
Requires:       gnome-panel%{?_isa}
Requires:       gnome-session%{?_isa}
Requires:       gnome-settings-daemon%{?_isa}
Requires:       metacity%{?_isa}

Recommends:     alacarte
Recommends:     geoclue2%{?_isa}
Recommends:     nautilus%{?_isa}
Recommends:     network-manager-applet%{?_isa}
Recommends:     gnome-power-manager

%if %{with compiz_session}
Suggests:       compiz%{?_isa}
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
GNOME Flashback is a session for GNOME 3 which was initially called "GNOME
Fallback", and shipped as a stand-alone session in Debian and Ubuntu. It
provides a similar user experience to the GNOME 2.x series sessions. The
differences to the MATE project is that GNOME Flashback uses GTK+ 3 and tries to
follow the current GNOME development by integrating recent changes of the GNOME
libraries. The development currently lags behind a little but a lot of progress
has been made and most importantly many open bugs have been fixed.


%prep
%autosetup -p1
NOCONFIGURE=1 gnome-autogen.sh


%build
%if %{with compiz_session}
%configure --with-compiz-session
%else
%configure
%endif
%make_build


%install
%make_install
%find_lang %{name}

install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%config %{_sysconfdir}/pam.d/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/glib-2.0/schemas/*.gschema.override
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.desktop.enums.xml
%{_datadir}/gnome-control-center/keybindings/50-%{name}-screenshots.xml
%{_datadir}/gnome-panel/layouts/%{name}.layout
%{_datadir}/gnome-session/sessions/%{name}-metacity.session
%{_datadir}/xsessions/%{name}-metacity.desktop
%{_libdir}/gnome-panel/modules/system_indicators.so
%{_libexecdir}/%{name}-clipboard
%{_libexecdir}/%{name}-idle-monitor
%{_libexecdir}/%{name}-media-keys
%{_libexecdir}/%{name}-metacity
%{_libexecdir}/%{name}-polkit
%{_sysconfdir}/xdg/autostart/%{name}-clipboard.desktop
%{_sysconfdir}/xdg/autostart/%{name}-geoclue-demo-agent.desktop
%{_sysconfdir}/xdg/autostart/%{name}-idle-monitor.desktop
%{_sysconfdir}/xdg/autostart/%{name}-media-keys.desktop
%{_sysconfdir}/xdg/autostart/%{name}-nm-applet.desktop
%{_sysconfdir}/xdg/autostart/%{name}-polkit.desktop
%{_sysconfdir}/xdg/menus/%{name}-applications.menu
%{_userunitdir}/*%{name}*

%if %{with compiz_session}
%{_datadir}/gnome-session/sessions/%{name}-compiz.session
%{_datadir}/xsessions/%{name}-compiz.desktop
%{_libexecdir}/%{name}-compiz
%endif


%changelog
%autochangelog
