%global pypi_name pytzdata

%global _description %{expand:
The Olson timezone database for Python.

This package contains the python bindings to the database provided by
the tzdata package as installed (version %{version} or later).}

Name: python-%{pypi_name}
Version: 2020.1
Release: %autorelease

License: MIT
Summary: Timezone database for Python
URL: https://github.com/sdispater/%{pypi_name}
Source0: %{pypi_source}
BuildArch: noarch

# Cleo was updated to 1.0.0a5 because the latest version of poetry needed it.
# It changed the way how some modules are imported and this patch should fix it.
Patch1: %{pypi_name}-cleo-imports-fix.patch

# Set mandatory name attribute in Command class to make pytzdata
# compatible with cleo 2.0.0+.
Patch2: %{pypi_name}-cleo-2.0.0-compatibility.patch

BuildRequires: python3-devel
BuildRequires: tzdata >= %{version}

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}
Requires: tzdata >= %{version}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -r pytzdata/zoneinfo
sed -i "s|os.path.dirname(__file__)|'%{_datadir}'|" pytzdata/__init__.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
