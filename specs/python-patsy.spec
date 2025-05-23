%bcond_without check

%global srcname patsy

%global _description %{expand:
A Python package for describing statistical models and for building 
design matrices. It is closely inspired by and compatible with 
the 'formula' mini-language used in R and S.}

Name: python-%{srcname}
Version: 1.0.1
Release: %autorelease
Summary: Describing statistical models in Python using symbolic formulas
# All code is under BSD except patsy.compat that is under Python
# See LICENSE.txt for details
License: BSD-2-Clause AND PSF-2.0

URL: https://github.com/pydata/patsy
Source0:  %{pypi_source %srcname} 

BuildArch: noarch
BuildRequires: python3-devel

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%if %{with check}
BuildRequires: %{py3_dist pytest}
%endif

# For splines
BuildRequires: python3-scipy  
# For splines
Recommends: %{py3_dist scipy}


%description -n python3-%{srcname} %_description

%package -n python3-%{srcname}-doc
Summary: Documentation for python3-%{srcname}, includes full API docs
BuildArch: noarch

%description -n python3-%{srcname}-doc
This package contains the full API documentation for python3-%{srcname}.


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files patsy

%check
%pyproject_check_import
%if %{with check}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md TODO
%license LICENSE.txt

%files -n python3-%{srcname}-doc
%doc README.md 
%license LICENSE.txt

%changelog
%autochangelog
