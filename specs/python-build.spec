# uv has many build dependencies, and will take some time to be available for
# new EPEL major versions.
%bcond uv %{undefined rhel}

%global pypi_name build

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        %autorelease
Summary:        A simple, correct PEP517 package builder

License:        MIT
URL:            https://github.com/pypa/build
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# downstream-only
Patch:          0001-fedora-disable-some-build-requirements.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41

%description
A simple, correct PEP517 package builder.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A simple, correct PEP517 package builder.


%pyproject_extras_subpkg -n python3-%{pypi_name} virtualenv %{?with_uv:uv}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test,virtualenv%{?with_uv:,uv}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Upstream has integration tests that can be run with the --run-integration
# flag, but currently that only includes one network test and one test that is
# xfail when flit-core is installed (which it will be during our package
# build), so including that flag doesn't run any additional tests.
%pytest -v -m "not network"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pyproject-build

%changelog
%autochangelog
