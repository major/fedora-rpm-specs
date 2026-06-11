%global sname pyghmi

%global _description %{expand:
This is a pure Python implementation of IPMI protocol.

The included pyghmicons and pyghmiutil scripts demonstrate how one may
incorporate the pyghmi library into a Python application.}


Summary: Python General Hardware Management Initiative (IPMI and others)
Name: python-%{sname}
Version: 1.6.16
Release: 4%{?dist}
Source0: https://tarballs.opendev.org/x/%{sname}/%{sname}-%{version}.tar.gz
License: Apache-2.0
BuildArch: noarch
Url: https://opendev.org/x/pyghmi

BuildRequires: python3-devel


%description %{_description}


%package -n python3-%{sname}
Summary: %{summary}


%description -n python3-%{sname} %{_description}


%package -n python3-%{sname}-tests
Summary: %{summary}
Requires: python3-%{sname} = %{version}-%{release}


%description -n python3-%{sname}-tests
%_description

Tests for the pyghmi library


%package -n python-%{sname}-doc
Summary: The pyghmi library documentation


%description -n python-%{sname}-doc
Documentation for the pyghmi library


%prep
%autosetup -n %{sname}-%{version}

sed -i '/^coverage[^a-zA-Z]/d' test-requirements.txt

# Drop global openstack constraints
sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

%generate_buildrequires
%pyproject_buildrequires -t -e docs,%{default_toxenv}


%build
%pyproject_wheel

%tox -e docs

# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


%install
%pyproject_install

%pyproject_save_files -l pyghmi


%check
%tox -e %{default_toxenv}


%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%{_bindir}/pyghmicons
%{_bindir}/pyghmiutil
%{_bindir}/virshbmc
%{_bindir}/fakebmc
%exclude %{python3_sitelib}/%{sname}/tests


%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests


%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.md


%changelog
* Tue Jun 09 2026 Steve Traylen <steve.traylen@cern.ch> - 1.6.16-4
- Run tests in spec file under tox

* Thu Jun 04 2026 Python Maint <python-maint@redhat.com> - 1.6.16-3
- Rebuilt for Python 3.15

* Thu May 21 2026 Steve Traylen <steve.traylen@cern.ch> - 1.6.16-2
- Modernise spec file

* Thu May 21 2026 Steve Traylen <steve.traylen@cern.ch> - 1.6.16-1
- Update to v1.6.16

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.6.2-4
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.6.2-3
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 08 2025 Dmitry Tantsur <dtantsur@proton.me> - 1.6.2-1
- Update to 1.6.2
- Stop using deprecated macros (#2378038)

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.5.69-7
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.69-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Pavel Cahyna <pcahyna@redhat.com> - 1.5.69-5
- migrated to SPDX license

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.5.69-3
- Rebuilt for Python 3.13

* Thu May 02 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5.69-2
- Limit dependencies in RHEL builds

* Sun Apr 21 2024 Dmitry Tantsur <dtantsur@proton.me> - 1.5.69-1
- Update to 1.5.69

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Dmitry Tantsur <dtantsur@protonmail.com> - 1.5.29-7
- Avoid setup.py build_sphinx (#2221967)

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.5.29-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.5.29-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Joel Capitao <jcapitao@redhat.com> - 1.5.29-1
- Update to 1.5.29.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.19-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Joel Capitao <jcapitao@redhat.com> - 1.5.19-1
- Updated to 1.5.19.

* Sun Aug 30 2020 Dmitry Tantsur <divius.inside@gmail.com> - 1.5.16-1
- Updated to 1.5.16.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Dmitry Tantsur <divius.inside@gmail.com> - 1.5.14-4
- Relax dateutil requirement in requirement.txt as well (#1835084)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.14-3
- Rebuilt for Python 3.9

* Wed May 13 2020 Yatin Karel <ykarel@redhat.com> - 1.5.14-2
- Fix typo in requirements

* Mon May 11 2020 Yatin Karel <ykarel@redhat.com> - 1.5.14-1
- Updated to 1.5.14.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.16-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.16-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.2.16-1
- Updated to 1.2.16.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Aug 14 2018 Ilya Etingof <etingof@gmail.com> - 1.2.4-3
- Added Python 3 build

* Mon Aug 13 2018 Ilya Etingof <etingof@gmail.com> - 1.2.4-1
- Upstream 1.2.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.22-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.22-1
- Upstream 1.0.22

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.12-4
- Python 2 binary package renamed to python2-pyghmi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Lucas Alvares Gomes <lucasagomes@gmail.com> - 1.0.12-1
- Rebased to 1.0.12

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Lucas Alvares Gomes <lucasagomes@gmail.com> - 0.8.0-1
- Rebased to 0.8.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Lucas Alvares Gomes <lucasagomes@gmail.com> - 0.5.9-1
- Initial package.
