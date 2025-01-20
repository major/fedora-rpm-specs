%global pretty_name FireflyAlgorithm
%global new_name fireflyalgorithm

%global _description %{expand:
Implementation of Firefly Algorithm (FA) for optimization.}

Name:           python-%{new_name}
Version:        0.4.5
Release:        2%{?dist}
Summary:        Implementation of Firefly Algorithm in Python

# SPDX
License:        MIT
URL:            https://github.com/firefly-cpp/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

Provides: python-FireflyAlgorithm = %{version}-%{release}
Obsoletes: python-FireflyAlgorithm < 0.0.4-2

%description %_description

%package -n python3-%{new_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-toml-adapt
BuildRequires:  python3-pytest

Provides: python3-FireflyAlgorithm = %{version}-%{release}
Obsoletes: python3-FireflyAlgorithm < 0.0.4-2

%description -n python3-%{new_name} %_description

%prep
%autosetup -n %{pretty_name}-%{version}
rm -rf %{pretty_name}.egg-info
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{new_name}

%check
%pytest

%files -n python3-%{new_name} -f %{pyproject_files}
%{_bindir}/firefly-algorithm
%license LICENSE
%doc README.md examples/ Problems.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%doc CHANGELOG.md CITATION.cff

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 9 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.5-1
- Update to the latest upstream's release

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.4.4-2
- Rebuilt for Python 3.13

* Tue Feb 6 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.4-1
- Update to the latest upstream's release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 4 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-1
- Update to the latest upstream's release
- Install additional doc files

* Thu Nov 23 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.1-2
- Install additional doc file

* Thu Nov 23 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.1-1
- Update to the latest upstream's release

* Mon Nov 6 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.0-1
- Update to the latest upstream's release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.3.4-4
- Rebuilt for Python 3.12

* Tue Jun 6 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-3
- Use standard format for dependencies

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-1
- Update to the latest upstream's release

* Wed Nov 2 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.3-1
- Update to the latest upstream's release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Update to the latest upstream's release

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.11

* Sun Jun 5 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Update to the latest upstream's release

* Sat Mar 12 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3-1
- Update to the latest upstream's release
- Enable tests
- Install examples

* Thu Jan 20 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2-4
- Remove unneeded dependency

* Thu Jan 6 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2-3
- Support Python 3.11+ versions

* Wed Dec 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2-2
- Support Python 3.11

* Fri Sep 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2-1
- Update to the latest upstream's release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.4-3
- Rebuilt for Python 3.10

* Mon Apr 19 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.4-2
- Initial package
- Previous package python-FireflyAlgorithm will be retired
