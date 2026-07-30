%global srcname memray
%global forgeurl https://github.com/bloomberg/%{srcname}

# The tests attempt to perform tracing and are generally flaky in mock/koji
%bcond_with tests

Name:           python-%{srcname}
Version:        1.13.4
Release:        %autorelease
Summary:        Memory profiler for Python applications

# memray is Apache-2.0, the vendored libbacktrace is BSD-3-Clause
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://bloomberg.github.io/memray/
# PyPI tarball doesn't include tests
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python3-docs
BuildRequires:  sed

BuildRequires:  elfutils-debuginfod-client-devel
BuildRequires:  libunwind-devel
BuildRequires:  lz4-devel
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

# Vendored and patched copy in src/vendor/libbacktrace
# License: BSD-3-Clause
Provides:       bundled(libbacktrace) = 1.0

%global _description %{expand:
Memray is a memory profiler for Python. It can track memory allocations in
Python code, in native extension modules, and in the Python interpreter itself.
It can generate several different types of reports to help you analyze the
captured memory usage data. While commonly used as a CLI tool, it can also be
used as a library to perform more fine-grained profiling tasks.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%package -n     %{srcname}
Summary:        %{summary}
Requires:       python3-%{srcname} = %{version}-%{release}
Suggests:       %{name}-doc = %{version}-%{release}

%description -n %{srcname} %_description

%package        doc
Summary:        Documentation for %{name}
# The actual docs are Apache-2.0, the vendored copy of js-furo is MIT
License:        Apache-2.0 AND MIT
Requires:       python3-docs
# This is arched because the docs are generated from the modules, and the
# native ones are arch specific.

# This is vendored by the sphinx theme that the docs use under
# html/_static/scripts/
Provides:       bundled(js-furo)

%description    doc
This package contains additional documentation for %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py

%generate_buildrequires
%pyproject_buildrequires -x docs %{?with_tests:-x test}

%build
%pyproject_wheel

# Build the docs
PYTHONPATH="build/lib.%{python3_platform}-cpython-%{python3_version_nodots}" \
  sphinx-build-3 docs html
rm -r html/{.buildinfo,.doctrees,.nojekyll}

%install
%pyproject_install
%pyproject_save_files %{srcname}

# Remove duplicate binary
rm %{buildroot}%{_bindir}/%{srcname}%{python3_version}

%check
%if %{with tests}
%pytest tests
%else
%pyproject_check_import
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%exclude %{python3_sitearch}/%{srcname}/_%{srcname}/

%files -n %{srcname}
%doc README.md NEWS.rst
%{_bindir}/%{srcname}

%files doc
%license LICENSE html/_static/scripts/furo.js.LICENSE.txt
%doc html

%changelog
%autochangelog
