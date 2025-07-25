%global pypi_name apypie

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        4%{?dist}
Summary:        Apipie bindings for Python

License:        MIT
URL:            https://github.com/Apipie/apypie
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description
Python bindings for the Apipie - Ruby on Rails API documentation tool.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Apipie bindings for Python

%description -n python%{python3_pkgversion}-%{pypi_name}
Apipie bindings for Python3

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 10 2025 Ondřej Gajdušek <ogajduse@redhat.com> - 0.7.1-3
- pyprojectize RPM spec - rhbz#2377456

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.7.1-2
- Rebuilt for Python 3.14

* Fri Apr 04 2025 Packit <hello@packit.dev> - 0.7.1-1
- New release 0.7.1

* Thu Mar 13 2025 Packit <hello@packit.dev> - 0.7.0-1
- New release 0.7.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 13 2025 Packit <hello@packit.dev> - 0.6.2-1
- New release 0.6.2

* Tue Nov 19 2024 Packit <hello@packit.dev> - 0.5.0-1
- New release 0.5.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.12

* Thu Jun 15 2023 Ondřej Gajdušek <ogajduse@redhat.com> - 0.4.0-1
- Update to apypie 0.4.0

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.2-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.3.2-1
- Update to apypie 0.3.2

* Wed Oct 21 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.3.1-1
- Update to apypie 0.3.1

* Mon Oct 19 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.3.0-1
- Update to apypie 0.3.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.9

* Thu Apr 09 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.2.2-1
- Release python-apypie 0.2.2

* Tue Apr 07 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.2.1-2
- Build customization for Fedora

* Mon Nov 25 2019 Evgeni Golov - 0.2.1-1
- Release python-apypie 0.2.1

* Mon Nov 04 2019 Evgeni Golov - 0.2.0-1
- Release python-apypie 0.2.0

* Tue Sep 10 2019 Evgeni Golov - 0.1.0-1
- Update to apypie 0.1.0

* Thu Aug 15 2019 Evgeni Golov - 0.0.5-1
- Update to apypie 0.0.5

* Fri Aug 09 2019 Evgeni Golov - 0.0.4-1
- Update to apypie 0.0.4

* Wed Jul 17 2019 Evgeni Golov - 0.0.3-1
- Initial package.

