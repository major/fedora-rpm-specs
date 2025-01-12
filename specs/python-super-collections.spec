Name:           python-super-collections
Version:        0.5.3
Release:        %autorelease
Summary:        Python SuperDictionaries (with attributes) and SuperLists

License:        MIT
URL:            https://github.com/fralau/super-collections
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/super-collections-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a Python library to instantly convert JSON and YAML files
into objects with attributes.}

%description %_description

%package -n     python3-super-collections
Summary:        %{summary}

%description -n python3-super-collections %_description

%prep
%autosetup -p1 -n super-collections-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l super_collections

%check
%pytest -v

%files -n python3-super-collections -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
