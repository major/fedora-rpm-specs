%global upstream_name pytest-randomly

Name:           python-%{upstream_name}
Version:        3.15.0
Release:        %autorelease
Summary:        Pytest plugin to randomly order tests and control random.seed
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source0:        %{url}/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Required for tests
BuildRequires:  python3dist(factory-boy)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(pytest-xdist)

%description
%{summary}.

%package -n     python3-%{upstream_name}
Summary:        %{summary}

%description -n python3-%{upstream_name}
%{summary}.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_randomly

%check
# Skip test_model_bakery to avoid new dependency on model_bakery
%pytest -p no:randomly -k 'not test_it_runs_before_stepwise and not test_model_bakery'

%files -n python3-%{upstream_name} -f %{pyproject_files}
%doc README.rst HISTORY.rst
%license LICENSE

%changelog
%autochangelog
