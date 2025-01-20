%global pkg_name httpagentparser

Name:           python-%{pkg_name}
Version:        1.9.5
Release:        9%{?dist}
Summary:        Extracts OS Browser etc information from http user agent string

License:        MIT
URL:            https://github.com/shon/httpagentparser
Source0:        %{pypi_source httpagentparser}
BuildArch:      noarch

BuildRequires:  python3-devel


%description
Extracts OS Browser etc information from http user agent string.


%package -n python3-%{pkg_name}
Summary:        Extracts OS Browser etc information from http user agent string


%description -n python3-%{pkg_name}
Extracts OS Browser etc information from http user agent string.


%prep
%autosetup -p1 -n %{pkg_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files httpagentparser


%check
%py3_check_import httpagentparser


%files -n python3-%{pkg_name}  -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.9.5-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.9.5-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Sandro Mani <manisandro@gmail.com> - 1.9.5-1
- Update to 1.9.5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Python Maint <python-maint@redhat.com> - 1.9.3-2
- Rebuilt for Python 3.11

* Sun Jun 19 2022 Sandro Mani <manisandro@gmail.com> - 1.9.3-1
- Update to 1.9.3

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.2-2
- Rebuilt for Python 3.11

* Sun Jan 30 2022 Sandro Mani <manisandro@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Sandro Mani <manisandro@gmail.com> - 1.9.1-1
- Initial package
