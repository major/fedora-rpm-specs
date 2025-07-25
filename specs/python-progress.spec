%global pypi_name progress

Name:           python-%{pypi_name}
Version:        1.6
Release:        17%{?dist}
Summary:        Easy to use progress bars

License:        ISC
URL:            http://github.com/verigak/progress/
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{defined el8}
BuildRequires:  python3-setuptools
%endif

Patch1:         0001-fixup-moving-average-window.patch

%global _description %{expand:
Collection of easy to use progress bars and spinners.}


%description %_description


%package -n     python3-%{pypi_name}
Summary:        Easy to use progress bars

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%if %{undefined el8}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
%if %{defined el8}
%py3_build
%else
%pyproject_wheel
%endif


%install
%if %{defined el8}
%py3_install
%else
%pyproject_install
%pyproject_save_files -l %{pypi_name}
%endif


%check
%if %{defined el8}
%py3_check_import %{pypi_name}
%else
%pyproject_check_import
%endif


%files -n python3-%{pypi_name} %{!?el8:-f %{pyproject_files}}
%doc README.rst
%if %{defined el8}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1.6-16
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 24 2024 Carl George <carlwgeorge@fedoraproject.org> - 1.6-14
- Convert to pyproject macros

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Pavel Raiskup <praiskup@redhat.com> - 1.6-6
- use time.monotonic(), bar.avg is infinity for zero speed

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Pavel Raiskup <praiskup@redhat.com> - 1.6-4
- fix for very frequent next() call, rhbz#2103093

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Pavel Raiskup <praiskup@redhat.com> - 1.5-1
- the latest upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Pavel Raiskup <praiskup@redhat.com> - 1.4-2
- followup for previous commit, PR#3

* Wed Dec 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.4-1
- 1.4

* Wed Oct 03 2018 Pavel Raiskup <praiskup@redhat.com> - 1.2-19
- no python2 in f30+ (rhbz#1634951)
- fix el6 build (rhbz#1310704)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-17
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2-14
- Python 2 binary package renamed to python2-progress
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-11
- Rebuild for Python 3.6

* Thu Dec 08 2016 Pavel Raiskup <praiskup@redhat.com> - 1.2-10
- keep enabled python3 subpackage only in fedora, and merge into epel7

* Tue Nov 01 2016 Pavel Raiskup <praiskup@redhat.com> - 1.2-9
- fix avg counter for copr-cli (rhbz#1299634)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Feb 18 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-2
- Add missing BR: python{,3}-setuptools

* Tue Feb 18 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-1
- Initial package.
