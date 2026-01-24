%bcond_without tests

%global forgeurl https://github.com/sharkwouter/minigalaxy
%global tag %{version}
%global uuid io.github.sharkwouter.Minigalaxy

Name:           minigalaxy
Version:        1.4.1
%forgemeta
Release:        %autorelease
Summary:        Simple GOG client for Linux
BuildArch:      noarch

# CC-BY-3.0:    Logo image (data/minigalaxy.png)
License:        GPL-3.0-or-later and CC-BY-3.0
URL:            https://sharkwouter.github.io/minigalaxy
Source0:        %{forgesource}

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  gdk-pixbuf2-xlib
BuildRequires:  gobject-introspection
BuildRequires:  gtk3
BuildRequires:  libnotify
BuildRequires:  libX11
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(simplejson)
%endif

Requires:       hicolor-icon-theme
Requires:       unzip
Requires:       webkit2gtk4.1

Recommends:     dosbox
Recommends:     gamemode
Recommends:     innoextract
Recommends:     libvkd3d
Recommends:     mangohud
Recommends:     wine
Recommends:     wine-dxvk

Suggests:       scummvm

%description
%{summary}.


%prep
%forgeautosetup
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop
%if %{with tests}
# Tests requires to run in X11 environment
%pyproject_check_import -e '*.ui.*' -e '*.ui' -e '*.css'
%pytest \
    --ignore=tests/test_ui_library.py \
    --ignore=tests/test_ui_window.py \
    %{nil}
%endif


%files -f %{pyproject_files}
%license LICENSE THIRD-PARTY-LICENSES.md
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/%{uuid}.metainfo.xml


%changelog
%autochangelog
