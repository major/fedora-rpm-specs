%global pypi_name pylast

Name:		%{pypi_name}
Version:	7.0.1
Release:	%autorelease
Summary:	Python interface to Last.fm API compatible social networks
License:	Apache-2.0
URL:		https://github.com/pylast/pylast
VCS:		git:%{url}.git
Source0:	%{pypi_source %{pypi_name}}
BuildArch:	noarch
BuildSystem:	pyproject
BuildOption(install):	-l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
