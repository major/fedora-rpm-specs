# Minimum GNOME Shell version supported
%global min_gs_version %%(cut -d "." -f 1 <<<%{version})

%global pkg_prefix gnome-shell-extension
%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(cut -d "." -f 1 <<<%{tarball_version})

%if 0%{?rhel}
%global xsession 0
%else
%global xsession 1
%endif

Name:           gnome-shell-extensions
Version:        48~alpha
Release:        %autorelease
Summary:        Modify and extend GNOME Shell functionality and behavior

License:        GPL-2.0-or-later
URL:            http://wiki.gnome.org/Projects/GnomeShell/Extensions
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  meson
BuildRequires:  git
BuildRequires:  gettext >= 0.19.6
BuildRequires:  glib2%{?_isa}
Requires:       gnome-shell >= %{min_gs_version}
BuildArch:      noarch

%description
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.

Enabled extensions:
  * apps-menu
  * auto-move-windows
  * drive-menu
  * launch-new-instance
  * light-style
  * native-window-placement
  * places-menu
  * screenshot-window-sizer
  * status-icons
  * system-monitor
  * user-theme
  * window-list
  * windowsNavigator
  * workspace-indicator


%package -n %{pkg_prefix}-common
Summary:        Files common to GNOME Shell Extensions
License:        GPL-2.0-or-later
Requires:       gnome-shell >= %{min_gs_version}
Obsoletes:      %{pkg_prefix}-horizontal-workspaces < 40.0~alpha.1-3

%description -n %{pkg_prefix}-common
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.

This package provides common data files shared by various extensions.


%package -n gnome-classic-session
Summary:        GNOME "classic" mode session
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-apps-menu = %{version}-%{release}
Requires:       %{pkg_prefix}-launch-new-instance = %{version}-%{release}
Requires:       %{pkg_prefix}-places-menu = %{version}-%{release}
Requires:       %{pkg_prefix}-window-list = %{version}-%{release}
Requires:       nautilus

%description -n gnome-classic-session
This package contains the required components for the GNOME Shell "classic"
mode, which aims to provide a GNOME 2-like user interface.


%if %{xsession}
%package -n gnome-classic-session-xsession
Summary:        GNOME "classic" mode session on X11
License:        GPL-2.0-or-later
Requires:       gnome-classic-session = %{version}-%{release}
# The X11 session is deprecated and eventually will be removed
Provides:       deprecated()

%description -n gnome-classic-session-xsession
This package contains the required components for the GNOME Shell "classic"
mode on X11, which aims to provide a GNOME 2-like user interface.
%endif


%package -n %{pkg_prefix}-apps-menu
Summary:        Application menu for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}
Requires:       gnome-menus

%description  -n %{pkg_prefix}-apps-menu
This GNOME Shell extension adds a GNOME 2.x style menu for applications.


%package -n %{pkg_prefix}-auto-move-windows
Summary:        Assign specific workspaces to applications in GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-auto-move-windows
This GNOME Shell extension enables easy workspace management. A specific
workspace can be assigned to each application as soon as it creates a window, in
a manner configurable with a GSettings key.


%package -n %{pkg_prefix}-drive-menu
Summary:        Drive status menu for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-drive-menu
This GNOME Shell extension provides a panel status menu for accessing and
unmounting removable devices.


%package -n %{pkg_prefix}-launch-new-instance
Summary:        Always launch a new application instance for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description  -n %{pkg_prefix}-launch-new-instance
This GNOME Shell extension modifies the behavior of clicking in the dash and app
launcher to always launch a new application instance.


%package -n %{pkg_prefix}-light-style
Summary:        Use light style in GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description  -n %{pkg_prefix}-light-style
This GNOME Shell extension changes the default style to light.


%package -n %{pkg_prefix}-native-window-placement
Summary:        Native window placement for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description  -n %{pkg_prefix}-native-window-placement
This GNOME Shell extension provides additional configurability for the window
layout in the overview, including a mechanism similar to KDE4.


%package -n %{pkg_prefix}-places-menu
Summary:        Places status menu for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-places-menu
This GNOME Shell extension add a system status menu for quickly navigating
places in the system.


%package -n %{pkg_prefix}-screenshot-window-sizer
Summary:        Screenshot window sizer for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-screenshot-window-sizer
This GNOME Shell extension allows to easily resize windows for GNOME Software
screenshots.


%package -n %{pkg_prefix}-status-icons
Summary:        Status icons support for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-status-icons
This GNOME Shell extension displays status icons in the top bar.


%package -n %{pkg_prefix}-system-monitor
Summary:        System monitor for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-system-monitor
This GNOME Shell extension displays system usage information in the top bar.


%package -n %{pkg_prefix}-user-theme
Summary:        Support for custom themes in GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-user-theme
This GNOME Shell extension enables loading a GNOME Shell theme from
~/.themes/<name>/gnome-shell/.


%package -n %{pkg_prefix}-window-list
Summary:        Display a window list at the bottom of the screen in GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-window-list
This GNOME Shell extension displays a window list at the bottom of the screen.


%package -n %{pkg_prefix}-windowsNavigator
Summary:        Support for keyboard selection of windows and workspaces in GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-windowsNavigator
This GNOME Shell extension enables keyboard selection of windows and workspaces
in overlay mode, by pressing the Alt and Ctrl key respectively.


%package -n %{pkg_prefix}-workspace-indicator
Summary:        Workspace indicator for GNOME Shell
License:        GPL-2.0-or-later
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-workspace-indicator
This GNOME Shell extension add a system status menu for quickly changing
workspaces.


%prep
%autosetup -S git -n %{name}-%{tarball_version}


%build
%meson -Dextension_set="all" -Dclassic_mode=true
%meson_build


%install
%meson_install

%find_lang %{name}

%if !%{xsession}
rm -rf %{buildroot}/%{_datadir}/xsessions
%endif


%files -n %{pkg_prefix}-common -f %{name}.lang
%doc NEWS README.md
%license COPYING


%files -n gnome-classic-session
%{_datadir}/gnome-shell/modes/classic.json
%{_datadir}/wayland-sessions/gnome-classic.desktop
%{_datadir}/wayland-sessions/gnome-classic-wayland.desktop
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.classic.gschema.override


%if %{xsession}
%files -n gnome-classic-session-xsession
%{_datadir}/xsessions/gnome-classic.desktop
%{_datadir}/xsessions/gnome-classic-xorg.desktop
%endif


%files -n %{pkg_prefix}-apps-menu
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.apps-menu.gschema.xml
%{_datadir}/gnome-shell/extensions/apps-menu*/


%files -n %{pkg_prefix}-auto-move-windows
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/gnome-shell/extensions/auto-move-windows*/

%files -n %{pkg_prefix}-drive-menu
%{_datadir}/gnome-shell/extensions/drive-menu*/


%files -n %{pkg_prefix}-launch-new-instance
%{_datadir}/gnome-shell/extensions/launch-new-instance*/


%files -n %{pkg_prefix}-light-style
%{_datadir}/gnome-shell/extensions/light-style*/


%files -n %{pkg_prefix}-native-window-placement
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement*/


%files -n %{pkg_prefix}-places-menu
%{_datadir}/gnome-shell/extensions/places-menu*/


%files -n %{pkg_prefix}-screenshot-window-sizer
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%{_datadir}/gnome-shell/extensions/screenshot-window-sizer*/


%files -n %{pkg_prefix}-status-icons
%{_datadir}/gnome-shell/extensions/status-icons*/


%files -n %{pkg_prefix}-system-monitor
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.system-monitor.gschema.xml
%{_datadir}/gnome-shell/extensions/system-monitor*/


%files -n %{pkg_prefix}-user-theme
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/gnome-shell/extensions/user-theme*/


%files -n %{pkg_prefix}-window-list
%{_datadir}/gnome-shell/extensions/window-list*/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml


%files -n %{pkg_prefix}-windowsNavigator
%{_datadir}/gnome-shell/extensions/windowsNavigator*/


%files -n %{pkg_prefix}-workspace-indicator
%{_datadir}/gnome-shell/extensions/workspace-indicator*/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.workspace-indicator.gschema.xml


%changelog
%autochangelog
