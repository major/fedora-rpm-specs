%global uuid pm.mirko.%{name}
%global suf brescia-3

Name:       bottles
Version:    2022.7.14
Release:    %autorelease
BuildArch:  noarch

License:    GPLv3+
Summary:    Easily manage Wine prefix in a new way
URL:        https://github.com/bottlesdevs/Bottles
Source0:    %{url}/archive/%{version}-%{suf}/%{name}-%{version}-%{suf}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: python3
BuildRequires: python3-gobject

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1) >= 1.1.99

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

%description
Easily manage Wine prefix in a new way! (Run Windows software and games on
Linux).

Features:

  * Create bottles based on environments (a set of rule and dependencies for
    better software compatibility)
  * Access to a customizable environment for all your experiments
  * Run every executable (.exe/.msi) in your bottles, using the context menu
    in your file manager
  * Integrated management and storage for executable file arguments
  * Support for custom environment variables
  * Simplified DLL overrides
  * On-the-fly runner change for any Bottle
  * Various optimizations for better gaming performance (esync, fsync, dxvk,
    cache, shader compiler, offload .. and much more.)
  * Tweak different wine prefix settings, without leaving Bottles
  * Automated dxvk installation
  * Automatic installation and management of Wine and Proton runners
  * System for checking runner updates for the bottle and automatic repair in
    case of breakage
  * Integrated Dependencies installer with compatibility check based on a
    community-driver repository
  * Detection of installed programs
  * Integrated Task manager for wine processes
  * Easy access to ProtonDB and WineHQ for support
  * Configurations update system across Bottles versions
  * Backup bottles as configuration file or full archive
  * Import backup archive
  * Importer from Bottles v1 (and other wineprefix manager)
  * Bottles versioning (experimental)
  * .. and much more that you can find by installing Bottles!


%prep
%autosetup -n Bottles-%{version}-%{suf}


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
%license LICENSE
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
