%bcond_without check

Name:           rust2rpm
Version:        27.1.0
Release:        %autorelease
Summary:        Generate RPM spec files for Rust crates
License:        MIT

URL:            https://pagure.io/fedora-rust/rust2rpm
Source:         %{url}/archive/v%{version}/rust2rpm-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  /usr/bin/asciidoctor

%if %{with check}
BuildRequires:  cargo
BuildRequires:  rust2rpm-helper >= 0.1.2
%endif

Requires:       cargo
Requires:       cargo-rpm-macros
Recommends:     rust2rpm-helper >= 0.1.2

# obsolete old provides (removed in Fedora 38)
Obsoletes:      cargo-inspector < 24

# obsolete and / or provide removed Python subpackages (removed in Fedora 38)
%py_provides    python3-rust2rpm
Obsoletes:      python3-rust2rpm < 24
Obsoletes:      python3-rust2rpm-core < 24

%description
rust2rpm is a tool that automates the generation of RPM spec files for
Rust crates.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-t}

%build
%pyproject_wheel
# build man pages
pushd docs
asciidoctor -b manpage rust2rpm.1.asciidoc
asciidoctor -b manpage rust2rpm.conf.5.asciidoc
asciidoctor -b manpage rust2rpm.toml.5.asciidoc
popd

%install
%pyproject_install
%pyproject_save_files rust2rpm
# install man pages
install -Dpm 644 docs/rust2rpm.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 644 docs/rust2rpm.conf.5 -t %{buildroot}/%{_mandir}/man5/
install -Dpm 644 docs/rust2rpm.toml.5 -t %{buildroot}/%{_mandir}/man5/

%check
%pyproject_check_import
%if %{with check}
%tox
%endif

%files -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%{_bindir}/rust2rpm
%{_mandir}/man1/rust2rpm.1*
%{_mandir}/man5/rust2rpm.{conf,toml}.5*

%changelog
%autochangelog
