%bcond_without check

Name:           rust-packaging
Version:        26.4
Release:        %autorelease
Summary:        RPM macros and generators for building Rust packages
License:        MIT

URL:            https://pagure.io/fedora-rust/rust-packaging
Source:         %{url}/archive/%{version}/rust-packaging-%{version}.tar.gz

# temporary patch for compatibility with RHEL / ELN:
# The %%cargo_prep macro in RHEL / ELN accepts a -V flag. Using the same spec
# file for both Fedora and ELN would cause spec file parsing errors because
# the -V flag is not known in Fedora.
Patch:          0001-Temporarily-accept-cargo_prep-V-flag-for-spec-compat.patch

BuildArch:      noarch

%if %{with check}
BuildRequires:  python3-pytest
%endif

%description
%{summary}.

%if ! 0%{?rhel}
%package -n rust-srpm-macros
Summary:        RPM macros for building Rust projects

%description -n rust-srpm-macros
RPM macros for building source packages for Rust projects.
%endif

%package -n cargo-rpm-macros
Summary:        RPM macros for building projects with cargo

# obsolete + provide rust-packaging (removed in Fedora 38)
Obsoletes:      rust-packaging < 24
Provides:       rust-packaging = %{version}-%{release}

Requires:       cargo2rpm >= 0.1.8

Requires:       cargo
Requires:       gawk
Requires:       grep

%if ! 0%{?rhel}
Requires:       rust-srpm-macros = %{version}-%{release}
%else
# The "rust-srpm-macros" package is built from the "rust" source package in
# RHEL, so the package follows a different versioning scheme.
Requires:       rust-srpm-macros
%endif

%description -n cargo-rpm-macros
RPM macros for building projects with cargo.

%prep
%autosetup -p1

%build
# nothing to do

%install
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.cargo
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust
%if ! 0%{?rhel}
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust-srpm
%endif
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo.attr
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo_vendor.attr

%if %{with check}
%check
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
pytest -vv
%endif

%if ! 0%{?rhel}
%files -n rust-srpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.rust
%{_rpmmacrodir}/macros.rust-srpm
%endif

%files -n cargo-rpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.cargo
%if 0%{?rhel}
%{_rpmmacrodir}/macros.rust
%endif
%{_fileattrsdir}/cargo.attr
%{_fileattrsdir}/cargo_vendor.attr

%changelog
%autochangelog
