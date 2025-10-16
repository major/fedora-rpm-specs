# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (C) Fedora Project Authors
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond tests 1
# Optional integration tests (no effect if tests are disabled)
%bcond numpy_tests 1
%bcond pandas_tests 1
%bcond inline_snapshot_tests 1

Name:           python-pydantic-core
Version:        2.41.4
Release:        %autorelease
Summary:        Core validation logic for pydantic written in rust

License:        MIT
URL:            https://github.com/pydantic/pydantic-core
Source:         %{url}/archive/v%{version}/pydantic-core-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
The pydantic-core project provides the core validation logic for pydantic
written in Rust.}

%description %_description


%package -n python3-pydantic-core
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        %{shrink:
                (MIT OR Apache-2.0)
                AND MIT
                AND Unicode-3.0
                AND Unicode-DFS-2016
                AND (Apache-2.0 OR BSL-1.0)
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND (Unlicense OR MIT)
                }

%description -n python3-pydantic-core %_description


%prep
%autosetup -p1 -n pydantic-core-%{version}

# Remove unused Cargo config that contains buildflags for Darwin
rm -v .cargo/config.toml

# Upstream tests with certain dependencies on x86_64 only (and only on certain
# Python interpreter versions) due to the limited availability of precompiled
# wheels on PyPI. We have no such limitations, except that python-pandas is not
# available on i686.
tomcli-set pyproject.toml lists replace 'dependency-groups.testing' \
    'pandas; *' 'pandas; platform_machine != "i686"'
tomcli-set pyproject.toml lists replace 'dependency-groups.testing' \
    'pytest-examples; *' 'pytest-examples'
tomcli-set pyproject.toml lists replace 'dependency-groups.testing' \
    'numpy; *' 'numpy'

# Use a regex to remove entries from the testing dependency group.
remove_from_testing() {
  tomcli-set pyproject.toml lists delitem --type regex \
      'dependency-groups.testing' "${1}"
}
# Remove coverage analysis, etc. from testing dependency group.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
remove_from_testing 'coverage\b.*'
# The pytest-examples plugin is possibly useful, but not packaged.
# The pytest-pretty plugin is purely cosmetic.
# The pytest-run-parallel plugin is possibly useful, but not packaged.
# The pytest-speed plugin is for benchmarking, which we do not need.
# The pytest-timeout plugin is not needed for downstream tests.
remove_from_testing 'pytest-(examples|pretty|run-parallel|speed|timeout)\b.*'
# We rely on the system timezone database, not on PyPI tzdata.
remove_from_testing 'tzdata\b.*'
# Handle conditional test dependencies.
%if %{without numpy_tests}
remove_from_testing 'numpy\b.*'
%endif
%if %{without pandas_tests}
remove_from_testing 'pandas\b.*'
%endif
%if %{without inline_snapshot_tests}
remove_from_testing 'inline-snapshot\b.*'
%endif

# Delete pytest addopts. We don't care about benchmarking.
tomcli-set pyproject.toml del 'tool.pytest.ini_options.addopts'
# Remove pytest timeout config. pytest-timeout is not needed for downstream tests.
tomcli-set pyproject.toml del 'tool.pytest.ini_options.timeout'
# Work around patched-out pytest-run-parallel plugin dependency (avoid
# "pytest.PytestUnknownMarkWarning: Unknown pytest.mark.thread_unsafe" error)
tomcli-set pyproject.toml list 'tool.pytest.ini_options.markers' \
    'thread_unsafe: mark as incompatible with patched-out pytest-run-parallel'

%cargo_prep

# Remove Windows-only dependencies
tomcli-set Cargo.toml lists delitem 'dependencies.pyo3.features' 'generate-import-lib'


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g testing}
%cargo_generate_buildrequires


%build
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pydantic_core


%check
%pyproject_check_import
%if %{with tests}
ignore="${ignore-} --ignore=tests/benchmarks"
%if %{without inline_snapshot_tests}
ignore="${ignore-} --ignore=tests/validators/test_allow_partial.py"
%endif

# Due to patching out the pytest-timeout dependency:
warningsfilter="${warningsfilter-} -W ignore::pytest.PytestUnknownMarkWarning"

%pytest ${warningsfilter-} ${ignore-} -k "${k-}" -rs
%endif


%files -n python3-pydantic-core -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
