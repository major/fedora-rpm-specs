# this is BRed by pytest, so we need to run without tests when bootstrapping
# also pygments-ansi-color is not available in Fedora yet
%bcond_with tests

Name:           python-pygments-pytest
Version:        2.5.0
Release:        %autorelease
Summary:        A pygments lexer for pytest output
License:        MIT
URL:            https://github.com/asottile/pygments-pytest
Source:         %{url}/archive/v%{version}/pygments-pytest-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.

%package -n     python3-pygments-pytest
Summary:        %{summary}

%description -n python3-pygments-pytest
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.


%prep
%autosetup -n pygments-pytest-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygments_pytest

%if %{with tests}
%check
%pytest -v
%endif

%files -n python3-pygments-pytest -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
