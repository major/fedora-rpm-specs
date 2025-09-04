%global _description %{expand:
Library for checking syntax of reStructuredText and code blocks nested within
it.}

%global forgeurl https://github.com/rstcheck/rstcheck-core

Name:           python-rstcheck-core
Version:        1.2.2
Release:        %{autorelease}
Summary:        Checks syntax of reStructuredText and code blocks nested within it

%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-rstcheck-core
Summary:        %{summary}
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  gcc gcc-c++

%description -n python3-rstcheck-core %_description

%prep
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%forgeautosetup


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
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
