Name:           python-pdir2
Version:        1.1.0
Release:        3%{?dist}
Summary:        Pretty dir() printing with joy

License:        MIT
URL:            https://github.com/laike9m/pdir2
Source0:        %{pypi_source pdir2}

# https://github.com/laike9m/pdir2/issues/78
Patch0:         python313.patch

BuildArch:      noarch

BuildRequires:  python3-devel python3-pip python3-pdm-pep517
BuildRequires:  python3-typing-extensions
BuildRequires:  pytest

%global _description %{expand:
An improved version of dir() with better output.  Attributes are grouped by
types/functionalities, with beautiful colors.  Supports ipython, ptpython,
bpython, and Jupyter Notebook.}

%description %_description

%package -n python3-pdir2
Summary: %{summary}

%description -n python3-pdir2 %_description

%prep
%autosetup -n pdir2-%{version} -p 1
# We can’t respect preemptive upper bounds on dependency versions. At least
# convert them into lower bounds. Also turn invalid version specifiers (.*)
# into valid ones, see: https://fedoraproject.org/wiki/Changes/Update_python-packaging_to_version_22_plus
sed -r -i 's/=(=[[:digit:]\.]+)\.\*/>\1/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pdir

%check
%pytest

%files -n python3-pdir2 -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 06 2024 Simon de Vlieger <cmdr@supakeen.com> - 1.1.0-2
- Patch for Python 3.13

* Tue Aug 06 2024 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.6-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Simon de Vlieger <cmdr@supakeen.com> - 0.3.6-6
- Patched for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.6-5
- Rebuilt for Python 3.12

* Mon Jan 30 2023 Simon de Vlieger <cmdr@supakeen.com> - 0.3.6-4
- Update dependency version specifiers to be valid.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.3.6-2
- Fix a stray comment
- Remove version upper-bounds; in particular, allow typing-extensions ≥4.3
  (fix RHBZ#2148950)

* Fri Nov 11 2022 Simon de Vlieger <cmdr@supakeen.com> - 0.3.6-1
- New upstream version

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Simon de Vlieger <cmdr@supakeen.com> - 0.3.1.post2-15
- Add patch for Python 3.11 __getstate__

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.3.1.post2-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1.post2-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.post2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Carl George <carl@george.computer> - 0.3.1.post2-6
- Add patch2 for Python 3.9 compatiblity rhbz#1794276

* Thu Jan 02 2020 Carl George <carl@george.computer> - 0.3.1.post2-5
- Update patch1 to add support for pytest 5

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.post2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.post2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Carl George <carl@george.computer> - 0.3.1.post2-1
- Latest upstream
- Drop python3_other subpackage
- Disable python2 subpackage on EL8
- Run python2 tests on EL7
- Add patch for pytest 4 compatibility rhbz#1706163

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 0.3.0-6
- Rebuilt to change main python from 3.4 to 3.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Carl George <carl@george.computer> - 0.3.0-5
- Disable python2 subpackage on F30+
- Enable python36 subpackage on EPEL7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Carl George <carl@george.computer> - 0.3.0-3
- Add patch1 to mark test_pdir_class as an expected fail
- Share doc and license dir between subpackages
- Update URL

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Carl George <carl@george.computer> - 0.3.0-1
- Latest upstream

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Carl George <carl@george.computer> - 0.2.2-1
- Latest upstream
- Remove environment markers from setup.py to allow using older setuptools
- EPEL compatibility

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Carl George <carl@george.computer> - 0.2.1-1
- Latest upstream
- Remove patch100 and patch101

* Thu Jun 29 2017 Carl George <carl@george.computer> - 0.2.0-1
- Initial package
