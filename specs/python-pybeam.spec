%global pypi_name pybeam

Name:		python-%{pypi_name}
Version:	0.8.1
Release:	%autorelease
Summary:	Python module to parse Erlang BEAM files
License:	MIT
URL:		https://github.com/matwey/%{pypi_name}
VCS:		git:%{url}.git
Source0:	%{pypi_source %{pypi_name}}
BuildArch:	noarch
BuildRequires:	python3-pytest
BuildSystem:	pyproject
BuildOption(install):	-l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
