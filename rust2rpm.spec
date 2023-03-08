%bcond_without check

Name:           rust2rpm
Version:        24.1.0
Release:        %autorelease
Summary:        Generate RPM spec files for Rust crates
License:        MIT

URL:            https://pagure.io/fedora-rust/rust2rpm
Source:         %{url}/archive/v%{version}/rust2rpm-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with check}
BuildRequires:  cargo
%endif

Requires:       cargo
Requires:       cargo-rpm-macros

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

%install
%pyproject_install
%pyproject_save_files rust2rpm

%check
%pyproject_check_import
%if %{with check}
%tox
%endif

%files -f %{pyproject_files}
%doc README.md
%doc NEWS
%{_bindir}/rust2rpm

%changelog
%autochangelog
