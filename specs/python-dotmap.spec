%bcond_without tests

%global pypi_name dotmap

%global _description %{expand:
DotMap is a dot-access dict subclass that has dynamic hierarchy
creation (autovivification), can be initialized with keys, easily
initializes from dict, easily converts to dict, is ordered by insertion.
The key feature is exactly what you want: dot-access.}


Name:           python-%{pypi_name}
Version:        1.3.30
Release:        11%{?dist}
Summary:        Dot access dictionary with dynamic hierarchy creation and ordered iteration

License:        MIT
URL:            https://github.com/drgrib/%{pypi_name}
Source0:        %{pypi_source dotmap}

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dotmap

%check
%if %{with tests}
python3 -m unittest
%endif

%files -n python3-dotmap -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.30-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.30-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.30-2
- Rebuilt for Python 3.11

* Thu Apr 7 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.30-1
- Update to the latest upstream's release

* Thu Apr 7 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.29-2
- Source corrected

* Tue Apr 5 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.29-1
- Update to the latest upstream's release

* Fri Apr 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.27-1
- Update to the latest upstream's release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.26-1
- Initial package
