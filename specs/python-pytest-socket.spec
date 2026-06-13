Name:           python-pytest-socket
Version:        0.8.0
Release:        %autorelease
Summary:        Pytest Plugin to disable socket calls during tests

License:        MIT
URL:            https://pypi.org/project/pytest-socket/
Source:         %{pypi_source pytest_socket}

BuildArch:      noarch
# Test dependencies added manually since pyproject.toml doesn't specify them
# separately from dev dependencies.
BuildRequires:  python3dist(httpx) >= 0.28.1
BuildRequires:  python3dist(starlette) >= 0.47.1


%global _description %{expand:
A plugin to use with Pytest to disable or restrict socket calls during tests to
ensure network calls are prevented.}

%description %_description

%package -n     python3-pytest-socket
Summary:        %{summary}

%description -n python3-pytest-socket %_description


%prep
%autosetup -p1 -n pytest_socket-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files --assert-license pytest_socket


%check
# Deselect tests that fail due to trying to reach external hosts and can't pass in Mock/Koji.
%pytest \
    --deselect tests/test_combinations.py::test_parametrize_with_socket_enabled_and_allow_hosts \
    --deselect tests/test_precedence.py::test_global_disable_and_allow_host \
    --deselect tests/test_socket.py::test_urllib_succeeds_by_default \
    --deselect tests/test_socket.py::test_enabled_urllib_succeeds


%files -n python3-pytest-socket -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
