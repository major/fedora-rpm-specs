%global srcname pytest-filter-subpackage
%global modname pytest_filter_subpackage
%global sum Pytest plugin for filtering based on sub-packages


Name:           python-%{srcname}
Version:        0.2.0
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package contains a simple plugin for the pytest framework that provides
a shortcut to testing all code and documentation for a given sub-package.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -rf %{pythonicname}.egg-info

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst CHANGES.rst


%changelog
%autochangelog
