%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           python-setuptools-rust
Version:        1.6.0
Release:        %autorelease
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        %{pypi_source setuptools-rust}
BuildArch:      noarch
ExclusiveArch:  %{rust_arches}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) > 46.1
BuildRequires:  python3dist(semantic-version) >= 2.8.2
BuildRequires:  python3dist(typing-extensions) >= 3.7.4.4
%if 0%{?fedora}
BuildRequires:  python3dist(wheel)
BuildRequires:  rust-packaging
%else
# RHEL has rust-toolset and neither setuptools-scm nor wheel
BuildRequires:  rust-toolset >= 1.45
%endif
%if %{with tests}
BuildRequires:  rust-pyo3+default-devel
%endif

%description
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%package -n     python3-setuptools-rust
Summary:        %{summary}
%if 0%{?fedora}
Requires:       rust-packaging
%else
Requires:       rust-toolset >= 1.45
%endif

%description -n python3-setuptools-rust
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%prep
%autosetup -n setuptools-rust-%{version}
# Remove bundled egg-info
rm -rf setuptools-rust.egg-info

%if ! 0%{?fedora}
# RHEL doesn't have setuptools-scm
# remove setuptools-scm
rm pyproject.toml
sed -i 's/setup_requires.*//' setup.cfg

# create version.py without setuptools-scm
cat > setuptools_rust/version.py << EOF
version = '%{VERSION}'
version_tuple = ($(echo %{VERSION} | sed 's/\./, /g'))
EOF
%endif


%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{__python3} -c "from setuptools_rust import RustExtension, version"

%if %{with tests}
cd examples/hello-world
%cargo_prep
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py build
cd ../..
%endif


%files -n python3-setuptools-rust
%doc README.md CHANGELOG.md
%license LICENSE
%{python3_sitelib}/setuptools_rust/
%{python3_sitelib}/setuptools_rust-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
