%global pypi_name pylast

Name:		%{pypi_name}
Version:	7.3.0
Release:	%autorelease
Summary:	Python interface to Last.fm API compatible social networks
License:	Apache-2.0
URL:		https://github.com/pylast/pylast
VCS:		git:%{url}.git
Source:		%{pypi_source %{pypi_name}}
# Drop the Python 3.16 trove classifier unknown to f44's trove-classifiers (FTBFS).
Patch0:		pylast-drop-py316-classifier.patch
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
