%global pypi_name textfsm

%global _description %{expand:
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.}


Name:           python-%{pypi_name}
Version:        2.1.0
Release:        %autorelease
Summary:        Python module for parsing semi-structured text into python tables

License:        Apache-2.0
URL:            https://github.com/google/textfsm
Source0:        https://github.com/google/textfsm/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l textfsm


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING
%{_bindir}/textfsm
%exclude %{python3_sitelib}/testdata


%changelog
%autochangelog
