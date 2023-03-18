%global ename  dash-to-panel
%global extdir %{_datadir}/gnome-shell/extensions/dash-to-panel@jderose9.github.com

Name:           gnome-shell-extension-%{ename}
Version:        55
Release:        2%{?dist}
Summary:        Integrated icon taskbar and status panel for Gnome Shell
License:        GPL-2.0-or-later
URL:            https://github.com/home-sweet-gnome/dash-to-panel
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# correct install paths
Patch0:         %{name}-system-install-paths.patch
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       clutter
Requires:       gnome-shell >= 42

%description
Dash to Panel is an icon taskbar for Gnome Shell. This extension moves the dash
into the gnome main panel so that the application launchers and system tray are
combined into a single panel, similar to that found in KDE Plasma and Windows
7+. A separate dock is no longer needed for easy access to running and favorited
applications.

%prep
%autosetup -n %{ename}-%{version} -p1

%build
%make_build VERSION=%{version}

%install
%make_install VERSION=%{version}
rm -v %{buildroot}%{extdir}/{COPYING,README.md}

%find_lang %{ename}

%files -f %{ename}.lang
%license COPYING
%doc README.md
%{extdir}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{ename}.gschema.xml

%changelog
* Wed Mar 15 2023 Dominik Mierzejewski <dominik@greysector.net> - 55-2
- correct run-time dependencies
- add explicit slash to extdir
- add missing comment

* Wed Mar 15 2023 Dominik Mierzejewski <dominik@greysector.net> - 55-1
- intial package
