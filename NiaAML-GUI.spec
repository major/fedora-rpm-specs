%global commit fff3dd3e5ae1ec26df77d952970d90e1b26a0cf3
%global snapdate 20211203

Name:           NiaAML-GUI
Version:        0.1.11^%{snapdate}git%(echo '%{commit}' | cut -b -7)
Release:        %autorelease
Summary:        GUI for NiaAML Python package

# SPDX
License:        MIT
URL:            https://github.com/lukapecnik/NiaAML-GUI
# Also distributed via PyPI (https://pypi.org/project/niaaml-gui/) but without
# tests and other auxiliary files.
%global tag %{?commit:%{commit}}%{?!commit:%{version}}
%global srcversion %{?commit:%{commit}}%{?!commit:%{version}}
Source0:        %{url}/archive/%{tag}/NiaAML-GUI-%{srcversion}.tar.gz

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
%autosetup -n %{name}-%{srcversion}


%generate_buildrequires
%pyproject_buildrequires


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
%doc CITATION.cff
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
