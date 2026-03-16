# RHEL does not have packaged rust libraries
%bcond packaged_rust_libraries %[ %{undefined rhel} || %{defined epel} ]
# The integration tests depend on the presence of these libraries
%bcond integration_tests %{with packaged_rust_libraries}
# Regex of integration tests to skip.
#  * html-py-ever requires unpackaged rust crates
%global integration_tests_exc '^(html-py-ever)'

Name:           python-setuptools-rust
Version:        1.12.0
Release:        %autorelease
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        %{pypi_source setuptools_rust}

# Allow building examples with PyO3 0.26, 0.27, and 0.28:
# https://github.com/PyO3/setuptools-rust/commit/6868a518681cfd99544c45c33ccd8d752d386c1c
# https://github.com/PyO3/setuptools-rust/commit/7b4279c196117c59c80d98e1d7d3cad70f6ed6c3
# https://github.com/PyO3/setuptools-rust/commit/112be5ce8a82d955fb0b8bea9653f24173d1e475
# https://github.com/PyO3/setuptools-rust/commit/608006f30addc03341daca6ee0d4d4a6439b1302
# https://github.com/PyO3/setuptools-rust/commit/8a76c7dd45af4cdaced3da756b4f898a34035bf5
# https://github.com/PyO3/setuptools-rust/pull/576
Patch:          setuptools_rust-1.12.0-pyo3-0.28.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
%if %{undefined rhel} || %{defined epel}
BuildRequires:  cargo-rpm-macros >= 24
%else
# RHEL has rust-toolset instead of cargo-rpm-macros
BuildRequires:  rust-toolset >= 1.45
%endif
%if %{with integration_tests}
BuildRequires:  %{py3_dist cffi}
%endif


%global _description %{expand:
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.}

%description %{_description}


%package -n     python3-setuptools-rust
Summary:        %{summary}
Requires:       cargo

%description -n python3-setuptools-rust %{_description}


%prep
%autosetup -p1 -n setuptools_rust-%{version}

%cargo_prep

%if %{with integration_tests}
for example in $(ls examples/ | grep -vE %{integration_tests_exc}); do
    cd "examples/${example}"
    %cargo_prep
    cd -
done
%endif


%generate_buildrequires
%pyproject_buildrequires
%if %{with integration_tests}
for example in $(ls examples/ | grep -vE %{integration_tests_exc}); do
    cd "examples/${example}"
    %cargo_generate_buildrequires
    cd - >&2
done
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l setuptools_rust


%check
%pyproject_check_import
# Disable tests that require internet access and/or test Windows functionality
%global test_ignores %{shrink:
        not test_adjusted_local_rust_target_windows_msvc
    and not test_get_lib_name_namespace_package
}

%if %{without packaged_rust_libraries}
%global test_ignores %{shrink:%{test_ignores}
    and not test_metadata_contents
    and not test_metadata_cargo_log
}
%endif

%pytest tests/ setuptools_rust/ --import-mode importlib -k '%{test_ignores}'

%if %{with integration_tests}
export %{py3_test_envvars}
%global _pyproject_wheeldir dist
for example in $(ls examples/ | grep -vE %{integration_tests_exc}); do
    cd "examples/${example}"
    %pyproject_wheel
    if [ -d "tests/" ]; then
        %{python3} -m venv venv --system-site-packages
        ./venv/bin/pip install dist/*.whl
        ./venv/bin/python -Pm pytest tests/
    fi
    cd -
done
%endif


%files -n python3-setuptools-rust -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
