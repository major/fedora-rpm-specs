%global pypi_name  localzone
%global forgeurl   https://github.com/ags-slc/localzone
Version:           0.9.8
%forgemeta

Name:           python-%{pypi_name}
Release:        9%{?dist}
Summary:        A simple library for managing DNS zones

License:        BSD
URL:            %{forgeurl}
# pypi releases don't contain necessary data to run the tests
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Comprehensive, low-level DNS toolkits can be cumbersome for the more common
zone management tasks–especially those related to making simple changes to
zone records. They can also come with a steep learning curve.
Enter localzone: a simple library for managing DNS zones. While localzone may
be a low-calorie library, it’s stuffed full of everything that a hungry
hostmaster needs.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.8-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.9.8-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Apr 27 2022 Christian Schuermann <spike@fedoraproject.org> 0.9.8-1
- Initial package.
