%bcond_without check

%global srcname joblib

Name:  python-%{srcname}
Version: 1.4.2
Release: %autorelease
Summary: Lightweight pipelining: using Python functions as pipeline jobs

License: BSD-3-Clause
URL: https://joblib.readthedocs.io
Source0: %{pypi_source}

Patch: joblib-unbundle-cloudpickle.patch

# Downstream only: Don't count DeprecationWarnings in test_main_thread_renamed_no_warning
# Upstream issue: https://github.com/joblib/joblib/issues/1478
Patch: joblib-dont-count-DeprecationWarnings.patch

# Numpy 2.x patch fixing failing doctest.
# https://github.com/joblib/joblib/pull/1632
Patch: https://github.com/joblib/joblib/pull/1632.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Joblib is a set of tools to provide lightweight pipelining in Python.
In particular, joblib offers:
 * transparent disk-caching of the output values and lazy
   re-evaluation (memorize pattern)
 * easy simple parallel computing
 * logging and tracing of the execution}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

# Testing
%if %{with check}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist lz4}
BuildRequires:  %{py3_dist psutil} 
BuildRequires:  %{py3_dist threadpoolctl}
%endif

Recommends: %{py3_dist numpy}
Recommends: %{py3_dist lz4}
Recommends: %{py3_dist psutil} 
Provides: bundled(python3dist(loky)) = 3.4.1

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf joblib/externals/cloudpickle/ 

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files joblib

%if %{with check}
%check
%pytest \
 --deselect "joblib/test/test_memory.py::test_parallel_call_cached_function_defined_in_jupyter" \
  joblib
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
