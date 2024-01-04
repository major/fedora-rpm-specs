%global forgeurl https://github.com/bottlesdevs/Bottles

Name:       bottles
Epoch:      1
Version:    51.10
Release:    %autorelease
Summary:    Run Windows in a Bottle

%global tag %{version}
%forgemeta

# The following two files are licensed as MIT:
# bottles/backend/models/vdict.py
# bottles/backend/utils/vdf.py
License:    GPL-3.0-or-later AND MIT
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildArch:  noarch
# blueprint-compiler does not work on s390x:
# https://gitlab.gnome.org/jwestman/blueprint-compiler/-/issues/96
ExcludeArch:    s390x

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: python3

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1) >= 1.1.99

BuildRequires: blueprint-compiler

Requires:   cabextract
Requires:   glibc(x86-32)           %dnl # https://github.com/bottlesdevs/Bottles/issues/601#issuecomment-936772762
Requires:   gtk4
Requires:   gtksourceview5
Requires:   hicolor-icon-theme
Requires:   libadwaita >= 1.1.99
Requires:   p7zip p7zip-plugins     %dnl # needed by the dependencies manager
Requires:   patool
Requires:   python3-gobject
Requires:   python3-icoextract      %dnl # icons support
Requires:   python3-markdown
Requires:   python3-patool
Requires:   python3-pefile          %dnl # icons support
Requires:   python3-pyyaml
Requires:   python3-requests        %dnl # needed by the download manager
Requires:   python3-urllib3         %dnl # needed by the download manager
Requires:   xdpyinfo                %dnl # needed by the display util
Requires:   python3-pathvalidate
Requires:   python3-fvs
Requires:   python3-vkbasalt-cli
Requires:   ImageMagick             %dnl # https://bugzilla.redhat.com/show_bug.cgi?id=2227538
Requires:   python3-chardet         %dnl # https://bugzilla.redhat.com/show_bug.cgi?id=2240292

%description
Bottles lets you run Windows software on Linux, such as applications
and games. It introduces a workflow that helps you organize by
categorizing each software to your liking. Bottles provides several
tools and integrations to help you manage and optimize your
applications.

Features:

- Use pre-configured environments as a base
- Change runners for any bottle
- Various optimizations and options for gaming
- Repair in case software or bottle is broken
- Install various known dependencies
- Integrated task manager to manage and monitor processes
- Backup and restore

%prep
%forgeautosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING.md
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml


%changelog
%autochangelog
