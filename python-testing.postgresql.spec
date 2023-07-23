Name:           python-testing.postgresql
Version:        1.3.0
Release:        9%{?dist}
Summary:        Automatically sets up a PostgreSQL testing instance

License:        Apache-2.0
URL:            https://github.com/tk0miya/testing.postgresql
Source0:        %{pypi_source testing.postgresql}
BuildArch:      noarch

# Backport unreleased commit 738c8eb19a4b064dd74ff851c379dd1cbf11bc65
# “Use utility methods of testing.common.database >= 1.1.0”, required
# for compatibility with testing.common.database >= 2.0.0.
Patch0:         %{url}/commit/738c8eb19a4b064dd74ff851c379dd1cbf11bc65.patch

# Backport unreleased commit 577445d8ff5e0ea89ccaf09fd5b82165a0875afe
# “Add CentOS/RHEL postgesql home directory blob to search patterns.”
Patch1:         %{url}/commit/577445d8ff5e0ea89ccaf09fd5b82165a0875afe.patch

BuildRequires:  python3-devel

BuildRequires:  postgresql-server
Requires:       postgresql-server

%global common_description %{expand: \
Automatically sets up a PostgreSQL instance in a temporary directory, and
destroys it after testing.}

%description
%{common_description}


%package -n     python3-testing.postgresql
Summary:        %{summary}

%description -n python3-testing.postgresql
%{common_description}


%prep
%autosetup -n testing.postgresql-%{version} -p1
# Do not generate a BR on deprecated python3dist(nose); use pytest instead
sed -r -i "s/'nose'/'pytest'/" setup.py


%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files testing


%check
%pytest


%files -n python3-testing.postgresql -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE; verify with “rpm -qL -p …”
%doc README.rst

# %%{python3_sitelib}/testing is a namespace package directory, but we do not
# need to (co-)own it because is owned by dependency
# python3dist(testing.common.database)
%exclude %dir %{python3_sitelib}/testing

%{python3_sitelib}/testing.postgresql-%{version}-py%{python3_version}-nspkg.pth


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.3.0-8
- Rebuilt for Python 3.12

* Sat Feb 11 2023 msuchy <msuchy@redhat.com> - 1.3.0-7
- migrate license to SPDX

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.0-2
- Port to pyproject-rpm-macros (“new Python guidelines”)

* Thu Jan 06 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.0-1
- Update to 1.3.0 (close RHBZ#1639492)
- Remove BR on deprecated python3dist(nose)
- Correctly mark LICENSE file

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-24
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 - Ernestas Kulik <ekulik@redhat.com> - 1.1.0-21
- Explicitly depend on python3-setuptools for building

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-14
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-12
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Martin Kutlak <mkutlak@redhat.com> - 1.1.0-11
- Add a missing dependency on which (BZ#1455202)

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Richard Marko <rmarko@fedoraproject.org> - 1.1.0-1
- Initial package
