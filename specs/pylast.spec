%global pypi_name pylast

Name:		%{pypi_name}
Version:	5.5.0
Release:	%autorelease
Summary:	Python interface to Last.fm API compatible social networks
License:	Apache-2.0
URL:		https://github.com/pylast/pylast
VCS:		git:%{url}.git
Source0:	%{pypi_source %{pypi_name}}
BuildArch:	noarch
BuildRequires:	python3-devel

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:	%{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# FIXME - no tests
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
