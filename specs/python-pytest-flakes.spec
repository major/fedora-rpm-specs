%global srcname pytest-flakes

Name:           python-%{srcname}
Version:        4.0.5
Release:        %autorelease
Summary:        Pytest plugin to check source code with pyflakes

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-flakes
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Py.test plugin for efficiently checking python source with pyflakes.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest) >= 2.8
BuildRequires:  python3dist(pyflakes)

%description -n python3-%{srcname}
Py.test plugin for efficiently checking python source with pyflakes.

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_flakes

%check
%pytest -k "not test_pep263"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
