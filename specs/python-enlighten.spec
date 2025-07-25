%global pypi_name enlighten
%global sum  Enlighten Progress Bar
%global desc Enlighten Progress Bar is console progress bar module for Python.\
The main advantage of Enlighten is it allows writing to stdout and stderr\
without any redirection.

Name:           python-%{pypi_name}
Version:        1.13.0
Release:        4%{?dist}
Summary:        %{sum}

License:        MPL-2.0
URL:            https://github.com/Rockhopper-Technologies/enlighten
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-blessed
BuildRequires:  python%{python3_pkgversion}-prefixed

%description
%{desc}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-blessed
Requires:       python%{python3_pkgversion}-prefixed

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove benchmark scripts
rm -rf benchmarks

# Remove Python byte cache from previous Python versions shipped in upstream tarball
find -name '*.pyc' -delete

%build
%py3_build

%install
%py3_install

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README*
%doc examples
%license LICENSE
%{python3_sitelib}/enlighten*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1.13.0-3
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Avram Lubkin <aviso@rockhopper.net> - 1.13.0-1
- Update to 1.13.0 (#2329787)
- Remove old logic from kickstart

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.12.4-2
- Rebuilt for Python 3.13

* Sun Apr 21 2024 Avram Lubkin <aviso@rockhopper.net> - 1.12.4-1
- Update to 1.12.4 (#2240497)

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 1.11.2-6
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.11.2-2
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Avram Lubkin <aviso@rockhopper.net> - 1.11.2-1
- Update to 1.11.2 (#2130958)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.10.2-2
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Avram Lubkin <aviso@rockhopper.net> - 1.10.2-1
- Update to 1.10.2 (#2031522)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Miro Hrončok <mhroncok@redhat.com> - 1.10.1-4
- Remove unused Python 2.7, 3.9, 3.8 and 3.7 byte cache from examples

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.1-2
- Rebuilt for Python 3.10

* Tue May 25 2021 Avram Lubkin <aviso@rockhopper.net> - 1.10.1-1
- Update to 1.10.1
- Drop EL6
- Fix dependencies

* Fri Apr 02 2021 Avram Lubkin <aviso@rockhopper.net> - 1.9.0-2
- Update EL7 patch

* Mon Mar 29 2021 Avram Lubkin <aviso@rockhopper.net> - 1.9.0-1
- Update to 1.9.0

* Wed Feb 24 2021 Avram Lubkin <aviso@rockhopper.net> - 1.8.0-1
- Update to 1.8.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Avram Lubkin <aviso@rockhopper.net> - 1.7.2-1
- Update to 1.7.2

* Tue Sep 15 2020 Avram Lubkin <aviso@rockhopper.net> - 1.6.2-1
- Update to 1.6.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Avram Lubkin <aviso@rockhopper.net> - 1.6.0-2
- Update EL7 patch

* Fri Jun 19 2020 Avram Lubkin <aviso@rockhopper.net> - 1.6.0-1
- Update to 1.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Avram Lubkin <aviso@rockhopper.net> - 1.5.1-1
- Update to 1.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Avram Lubkin <aviso@rockhopper.net> - 1.4.0-1
- Update to 1.4.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Avram Lubkin <aviso@rockhopper.net> - 1.3.0-1
- Update to 1.3.0

* Sat Mar 30 2019 Avram Lubkin <aviso@rockhopper.net> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Avram Lubkin <aviso@rockhopper.net> - 1.1.0-1
- Update to 1.1.0

* Sun Nov 04 2018 Avram Lubkin <aviso@rockhopper.net> - 1.0.7-6
- Remove Python 2 packages in Fedora 30+ (bz#1641299)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Avram Lubkin <aviso@rockhopper.net> - 1.0.7-1
- Update to 1.0.7

* Fri Oct 13 2017 Avram Lubkin <aviso@rockhopper.net> - 1.0.6-1
- Initial package.
