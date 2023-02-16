%bcond_without check

Name:           cargo2rpm
Version:        0.1.1
Release:        %autorelease
Summary:        Translation layer between cargo and RPM
License:        MIT

URL:            https://pagure.io/fedora-rust/cargo2rpm
Source:         %{url}/archive/%{version}/cargo2rpm-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       cargo

%description
cargo2rpm implements a translation layer between cargo and RPM. It
provides a CLI interface (for implementing RPM macros and generators)
and a Python API (which rust2rpm is built upon).

%prep
%autosetup -n cargo2rpm-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%if %{with check}
%tox
%endif

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_bindir}/cargo2rpm
%{python3_sitelib}/cargo2rpm-*.dist-info/
%{python3_sitelib}/cargo2rpm/

%changelog
%autochangelog
