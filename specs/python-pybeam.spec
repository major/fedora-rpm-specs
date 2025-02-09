%global pypi_name pybeam

Name:		python-%{pypi_name}
Version:	0.8
Release:	%autorelease
Summary:	Python module to parse Erlang BEAM files
License:	MIT
URL:		https://github.com/matwey/%{pypi_name}
VCS:		git:%{url}.git
#Source0:	%{pypi_source %{pypi_name}}
Source0:	%{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
