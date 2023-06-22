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
BuildRequires:  gcc gcc-c++

%description -n python3-rstcheck-core %_description

%prep
%autosetup -n rstcheck_core-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rstcheck_core

%check
%{pytest}

%files -n python3-rstcheck-core -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
