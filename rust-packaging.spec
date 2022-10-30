%bcond_without check
# https://pagure.io/koji/issue/659
%global debug_package %{nil}

Name:           rust-packaging
Version:        23
Release:        %autorelease
Summary:        RPM macros for building Rust packages
License:        MIT

URL:            https://pagure.io/fedora-rust/rust2rpm
Source:         %{url}/archive/v%{version}/rust2rpm-v%{version}.tar.gz

# https://pagure.io/fedora-rust/rust2rpm/pull-request/221
Patch:          0001-Adjust-build-flags-to-allow-the-new-implementation-u.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  python3-devel

%if %{with check}
BuildRequires:  cargo
%endif

Requires:       python3-rust2rpm-core = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       rust-srpm-macros = %{version}

Requires:       rust
Requires:       cargo >= 1.41

# gawk is needed for stripping dev-deps in macro
Requires:       gawk

%description
The package provides RPM macros for building Rust projects.

Note that rust-srpm-macros is a seperate arch-independent package that
is also required to build Rust packages.

%package     -n python3-rust2rpm
Summary:        Generate RPM spec files for Rust packages
Requires:       cargo
Requires:       python3-rust2rpm-core = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       rust2rpm = %{version}-%{release}

%description -n python3-rust2rpm
rust2rpm is a tool that automates the generation of RPM spec files for
Rust crates.

%package     -n python3-rust2rpm-core
Summary:        Generate RPM spec files for Rust packages (core functionality)
Requires:       cargo
Provides:       cargo-inspector = %{version}-%{release}

%description -n python3-rust2rpm-core
rust2rpm is a tool that automates the generation of RPM spec files for
Rust crates.

This package contains the core functionality which doesn't depend on
any third-party python packages.

%prep
%autosetup -n rust2rpm-v%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} data/macros.rust data/macros.cargo
install -D -p -m 0644 -t %{buildroot}%{_fileattrsdir} data/cargo.attr

%if %{with check}
%check
%tox
%endif

%files
%{_rpmmacrodir}/macros.rust
%{_rpmmacrodir}/macros.cargo
%{_fileattrsdir}/cargo.attr

%files -n python3-rust2rpm
%{_bindir}/rust2rpm
%{python3_sitelib}/rust2rpm-*.dist-info/
%{python3_sitelib}/rust2rpm/
%exclude %{python3_sitelib}/rust2rpm/core/

%files -n python3-rust2rpm-core
%license LICENSE
%doc README.md NEWS
%{_bindir}/cargo-inspector
%{python3_sitelib}/rust2rpm/core/

%changelog
%autochangelog
