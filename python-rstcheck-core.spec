%global _description %{expand:
Library for checking syntax of reStructuredText and code blocks nested within
it.}

Name:           python-rstcheck-core
Version:        1.0.3
Release:        %{autorelease}
Summary:        Checks syntax of reStructuredText and code blocks nested within it

License:        MIT
URL:            https://pypi.org/pypi/rstcheck-core
Source0:        %{pypi_source rstcheck_core}

BuildArch:      noarch

%description %_description

%package -n python3-rstcheck-core
Summary:        %{summary}
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-sphinx
BuildRequires:  python3-tomli
BuildRequires:  python3-toml
BuildRequires:  gcc gcc-c++

%description -n python3-rstcheck-core %_description

%prep
%autosetup -n rstcheck_core-%{version}

# loosen dep versions
sed -i 's/docutils.*/docutils = ">=0.7"/' pyproject.toml
sed -i 's/types-docutils.*/types-docutils = ">=0.18"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rstcheck_core

%check
# https://github.com/rstcheck/rstcheck-core/issues/57
%{pytest} -k "not test_check_python_returns_error_on_syntax_warning"

%files -n python3-rstcheck-core -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
