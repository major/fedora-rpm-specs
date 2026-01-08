Name:           python-desktop-entry-lib
Version:        5.0
Release:        %autorelease
Summary:        Library for working with .desktop files
License:        BSD-2-Clause
URL:            https://codeberg.org/JakobDev/desktop-entry-lib
# PyPI tarball is missing test data
Source:         %{url}/archive/%{version}.tar.gz#/desktop-entry-lib-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-subtests
BuildRequires:  python3-pyfakefs
BuildRequires:  tomcli

%global _description %{expand:
desktop-entry-lib allows reading and writing .desktop files according to the
Desktop Entry Specification.}


%description %_description


%package -n python3-desktop-entry-lib
Summary:        %{summary}


%description -n python3-desktop-entry-lib %_description


%pyproject_extras_subpkg -n python3-desktop-entry-lib xdg-desktop-portal


%prep
%autosetup -C
# remove coverage options
tomcli set pyproject.toml del tool.pytest.ini_options.addopts


%generate_buildrequires
%pyproject_buildrequires -x xdg-desktop-portal


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l desktop_entry_lib


%check
%pytest


%files -n python3-desktop-entry-lib -f %{pyproject_files}


%changelog
%autochangelog
