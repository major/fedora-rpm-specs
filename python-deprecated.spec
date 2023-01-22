%global srcname Deprecated
%global pkgname deprecated

Name:           python-%{pkgname}
Version:        1.2.13
Release:        4%{?dist}
Summary:        Python decorator to deprecate old python classes, functions or methods
License:        MIT
URL:            https://github.com/tantale/%{pkgname}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Python @deprecated decorator to deprecate old python classes, functions or
methods.}

%description %{_description}

%package -n python3-%{pkgname}
Summary:        %{summary}
%description -n python3-%{pkgname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pkgname}

%check
%pyproject_check_import

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE.rst
%doc README.md


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.13-2
- Rebuilt for Python 3.11

* Fri Apr 29 2022 Hunor Csomortáni <csomh@redhat.com> - 1.2.13-1
- Update to version 1.2.13

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.12-2
- Rebuilt for Python 3.10

* Sat Mar 13 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 1.2.12-1
- new upstream release: 1.2.12

* Sat Feb 06 2021 Hunor Csomortáni <csomh@redhat.com> - 1.2.11-1
- new upstream release: 1.2.11

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Hunor Csomortáni <csomh@redhat.com> - 1.2.10-1
- new upstream release: 1.2.10

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-4
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Petr Hracek <phracek@redhat.com> - 1.2.6-3
- Enable python dependency generator

* Fri Jul 26 2019 Petr Hracek <phracek@redhat.com> - 1.2.6-2
- Fix python3_sitelib issue

* Fri Jul 26 2019 Petr Hracek <phracek@redhat.com> - 1.2.6-1
- Initial package
