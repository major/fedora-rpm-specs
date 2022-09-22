Name:           NiaAML-GUI
Version:        0.1.11
Release:        %autorelease
Summary:        GUI for NiaAML Python package

License:        MIT
URL:            https://github.com/lukapecnik/NiaAML-GUI
# Also distributed via PyPI (https://pypi.org/project/niaaml-gui/) but without
# tests and other auxiliary files.
Source0:        %{url}/archive/%{version}/NiaAML-GUI-%{version}.tar.gz
# Add an icon file to AppData
# https://github.com/lukapecnik/NiaAML-GUI/pull/14
Source1:        %{url}/raw/c0d10e18af0334896a40ff0675a9b3135ea96fab/AppData/niaaml-gui.png

# Create initial .desktop and .metadata files
# https://github.com/lukapecnik/NiaAML-GUI/pull/9
Patch0:         %{url}/pull/9.patch
# Fix LICENSE file installed directly in site-packages
# https://github.com/lukapecnik/NiaAML-GUI/pull/11
Patch1:         %{url}/pull/11.patch
# Add a GUI script entry point
# https://github.com/lukapecnik/NiaAML-GUI/pull/13
Patch2:         %{url}/pull/13.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# pyproject.toml: [tool.poetry.dev-dependencies]
# pytest = "^5.2"
# Version specification loosened to allow newer versions
BuildRequires:  python3dist(pytest) >= 5.2

Requires:       hicolor-icon-theme

%global app_id io.github.lukapecnik.niaaml_gui

%global common_description %{expand:
This is a basic graphical user interface intended for users of the NiaAML
Python package.}

%description %{common_description}


%prep
%autosetup -p1
cp -p '%{SOURCE1}' AppData/


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files niaaml_gui

desktop-file-install --dir='%{buildroot}%{_datadir}/applications' \
    AppData/%{app_id}.desktop
install -t '%{buildroot}%{_metainfodir}' -p -m 0644 -D \
    AppData/%{app_id}.metainfo.xml
install -t '%{buildroot}%{_datadir}/icons/hicolor/256x256/apps' -p -m 0644 -D \
    AppData/niaaml-gui.png


%check
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'

# https://github.com/lukapecnik/NiaAML-GUI/issues/10
k="${k-}${k+ and }not test_version"
# Since we have deselected the only test, we do not run pytest at all for now.
# (It fails, i.e. exits with a non-zero code, if there are no tests.)
# %%pytest -k "${k-}"

# The upstream tests are extremely minimal, so we also perform an import “smoke
# test.”
%pyproject_check_import


%files -f %{pyproject_files}
%license LICENSE
%doc CODE_OF_CONDUCT.md
%doc README.md
# README.rst is present but empty.

%{_bindir}/NiaAML-GUI
# There is no need for a man page, since this is a pure GUI application with no
# useful command-line options.

%{_datadir}/applications/%{app_id}.desktop
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/icons/hicolor/256x256/apps/niaaml-gui.png


%changelog
%autochangelog
