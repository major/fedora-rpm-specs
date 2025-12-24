%bcond_without check

%global srcname joblib

Name:  python-%{srcname}
Version: 1.5.3
Release: %autorelease
Summary: Lightweight pipelining: using Python functions as pipeline jobs

License: BSD-3-Clause
URL: https://joblib.readthedocs.io
Source0: %{pypi_source}

Patch: joblib-unbundle-cloudpickle.patch

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
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist lz4}
BuildRequires:  %{py3_dist psutil} 
BuildRequires:  %{py3_dist threadpoolctl}
%endif

Recommends: %{py3_dist numpy}
Recommends: %{py3_dist lz4}
Recommends: %{py3_dist psutil} 
Provides: bundled(python3dist(loky)) = 3.5.6

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
 --deselect "joblib/test/test_numpy_pickle.py::test_joblib_pickle_across_python_versions" \
 --deselect "joblib/test/test_numpy_pickle.py::test_joblib_pickle_across_python_versions_with_mmap" \
  joblib
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
