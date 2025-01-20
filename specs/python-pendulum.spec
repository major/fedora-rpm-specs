%bcond tests 1
%global pypi_name pendulum

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        4%{?dist}
Summary:        Python datetimes made easy

License:        MIT
URL:            https://pendulum.eustace.io
Source0:        https://github.com/sdispater/pendulum/archive/%{version}/pendulum-%{version}.tar.gz
Patch0:         0001-Use-zoneinfo-instead-of-tzdata-package-to-retrieve-t.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  tomcli
BuildRequires:  tzdata
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist time-machine}
%endif

%description
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
# Primary: MIT
# Apache-2.0
# MIT
# MIT OR Apache-2.0
License:        MIT AND Apache-2.0 AND (MIT OR Apache-2.0)

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       tzdata

%description -n python3-%{pypi_name}
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove tzdata dependency. We use the system one.
tomcli-set pyproject.toml lists delitem project.dependencies 'tzdata.*'
# Remove pytest-benchmark dependency. We don't care about it in RPM builds.
sed -i '/@pytest.mark.benchmark/d' $(find tests -type f -name '*.py')
%cargo_prep
cd rust
rm -rf Cargo.lock
# Remove unpackaged feature. This is only needed for Windows.
tomcli-set Cargo.toml lists delitem dependencies.pyo3.features 'generate-import-lib'

%generate_buildrequires
%pyproject_buildrequires -r
cd rust
%cargo_generate_buildrequires -t

%build
export RUSTFLAGS=%{shescape:%build_rustflags}
%pyproject_wheel

cd rust
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%install
%pyproject_install
%pyproject_save_files pendulum

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE rust/LICENSES.dependencies
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.13

* Mon Feb 05 2024 Maxwell G <maxwell@gtmx.me> - 3.0.0-1
- Update to 3.0.0. Fixes rhbz#2147455.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.2-12
- Add setuptools BR for distutils in Python 3.12

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 2.1.2-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.1.2-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.2-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-2
- Update build workflow

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Update to new upstream release 2.1.2 (#1876673)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-2
- Fix description (rhbz#1790074)

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-1
- Initial package for Fedora
