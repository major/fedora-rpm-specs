# mailman3's TestableMaster can't be used outside of a
# source checkout?
%bcond_with tests

%global srcname postorius

Name:           python-%{srcname}
Version:        1.3.8
Release:        %autorelease
Summary:        Web UI for GNU Mailman
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/postorius
Source:         %{pypi_source %{srcname}}
# use PEP503 normalized dependencies
Patch:          %{srcname}-pep503.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
The Postorius Django app provides a web user interface to access GNU Mailman.}

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}

%description -n %{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
PYTHONPATH=$(pwd)/src:${PYTHONPATH} \
%tox
%endif


%files -n %{srcname} -f %{pyproject_files}
%license COPYING
%doc README.rst


%changelog
%autochangelog
