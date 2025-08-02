%global pypi_name py-solc-ast

Name:          python-solc-ast
Version:       1.2.10
Release:       %autorelease
BuildArch:     noarch
Summary:       A tool for exploring the solc abstract syntax tree
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name}}
Patch1:        python-solc-ast-0001-Remove-all-shebangs.patch
BuildSystem:   pyproject
BuildOption(install): -l solcast

%description
%{summary}.

%package -n python3-solc-ast
Summary: %{summary}

%description -n python3-solc-ast
%{summary}.

%check -a
# FIXME Unfortunately tests requires 30+ mbytes data file
#%%pytest

%files -n python3-solc-ast -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
