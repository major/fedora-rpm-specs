%global pypi_name pygments-lexer-solidity

Name:          python-%{pypi_name}
Version:       0.7.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Solidity lexer for Pygments
License:       BSD-2-Clause
URL:           https://gitlab.com/veox/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name}}
BuildSystem:   pyproject
BuildOption(install): -l pygments_lexer_solidity

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
