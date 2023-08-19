Name:           rust-packaging
Version:        24
Release:        %autorelease
Summary:        RPM macros and generators for building Rust packages
License:        MIT

URL:            https://pagure.io/fedora-rust/rust-packaging
Source:         %{url}/archive/%{version}/rust-packaging-%{version}.tar.gz

# backported upstream patches for minor fixes
Patch:          https://pagure.io/fedora-rust/rust-packaging/c/3df6ad1.patch
Patch:          https://pagure.io/fedora-rust/rust-packaging/c/b9d6410.patch
Patch:          https://pagure.io/fedora-rust/rust-packaging/c/8690145.patch
Patch:          https://pagure.io/fedora-rust/rust-packaging/c/0ff9bb8.patch
Patch:          https://pagure.io/fedora-rust/rust-packaging/c/801dd51.patch

BuildArch:      noarch

%description
%{summary}.

%package -n rust-srpm-macros
Summary:        RPM macros for building Rust projects

%description -n rust-srpm-macros
RPM macros for building source packages for Rust projects.

%package -n cargo-rpm-macros
Summary:        RPM macros for building projects with cargo

# obsolete + provide rust-packaging (removed in Fedora 38)
Obsoletes:      rust-packaging < 24
Provides:       rust-packaging = %{version}-%{release}

Requires:       cargo
Requires:       cargo2rpm >= 0.1.0
Requires:       gawk

Requires:       rust-srpm-macros = %{version}-%{release}

%description -n cargo-rpm-macros
RPM macros for building projects with cargo.

%prep
%autosetup -p1

%build
# nothing to do

%install
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.cargo
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust-srpm
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo.attr

%files -n rust-srpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.rust
%{_rpmmacrodir}/macros.rust-srpm

%files -n cargo-rpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.cargo
%{_fileattrsdir}/cargo.attr

%changelog
%autochangelog
