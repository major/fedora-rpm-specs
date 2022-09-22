Name:           python-pytest-click
Version:        1.1.0
Release:        1%{?dist}
Summary:        Pytest plugin for Click

License:        MIT
URL:            https://github.com/Stranger6667/pytest-click
Source:         %{pypi_source pytest_click}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click) >= 6
BuildRequires:  python3dist(pytest) >= 5
BuildRequires:  python3dist(setuptools)

%description
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%package -n     python3-pytest-click
Summary:        %{summary}

%description -n python3-pytest-click
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%prep
%autosetup -n pytest_click-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-pytest-click
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_click/
%{python3_sitelib}/pytest_click-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Aug 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.1.0-1
- Initial package.
