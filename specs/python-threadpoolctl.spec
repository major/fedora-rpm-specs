%bcond_without check

%global srcname threadpoolctl

Name: python-%{srcname}
Version: 3.5.0
Release: %autorelease
Summary: Thread-pool Controls
License: BSD-3-Clause

URL: https://github.com/joblib/threadpoolctl
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python helpers to limit the number of threads used in the 
threadpool-backed of common native libraries used for scientific computing 
and data science (e.g. BLAS and OpenMP).
Fine control of the underlying thread-pool size can be useful in 
workloads that involve nested parallelism so as to mitigate 
oversubscription issues.}     

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
# Testing
%if %{with check}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(scipy)
BuildRequires: python3dist(cython)
%endif

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files threadpoolctl

%check
%if %{with check}
# test_architecture has a hardcoded list of architectures,
# instead of playing Whac-A-Mole by adding new and new, we skip it
%pytest -v -k 'not test_architecture and not test_command_line' \
 --deselect "tests/test_threadpoolctl.py::test_controller_info_actualized" 

%else
%pyproject_check_import -t
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md multiple_openmp.md

%changelog
%autochangelog
