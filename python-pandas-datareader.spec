%bcond_without check

%global srcname pandas-datareader
%global summary Data readers from the pandas codebase

%global common_description                                                   \
Data readers extracted from the pandas codebase, should be compatible with   \
recent pandas versions.

Name: python-%{srcname}
Version: 0.10.0
Release: %autorelease
Summary: %{summary}
License: BSD-3-Clause

URL: https://github.com/pydata/pandas-datareader
Source0: %{pypi_source}
# Old version of versioner still uses deprecated SafeConfigParser
# https://github.com/pydata/pandas-datareader/issues/969
Patch: pandas-datareader-python312.patch

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
%{common_description}

%package -n python3-%{srcname}
Summary: %{summary}

%if %{with check}
BuildRequires: python3-pytest
BuildRequires: python3-numpy
BuildRequires: python3-pandas
BuildRequires: python3-requests
BuildRequires: python3-wrapt
%endif

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pandas_datareader

%check
# Most tests require network
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
