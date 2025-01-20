%global modname piexif

Name:           python-%{modname}
Version:        1.1.3
Release:        23%{?dist}
Summary:        Pure Python library to simplify exif manipulations with python

License:        MIT
URL:            https://github.com/hMatoba/Piexif
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# Taken from https://github.com/hMatoba/Piexif/issues/108
Patch0:         python-piexif-fix-tests-pillow.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Very simple Python library to simplify exif manipulations that does
not depend on other libraries.

There are only just five functions:
    load(filename)                 - Get exif data as dict.
    dump(exif_dict)                - Get exif as bytes to save with JPEG.
    insert(exif_bytes, filename)   - Insert exif into JPEG.
    remove(filename)               - Remove exif from JPEG.
    transplant(filename, filename) - Transplant exif from JPEG to JPEG.}

%description %{_description}

%package -n     python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
Suggests:       python%{python3_version}dist(pillow)

%description -n python3-%{modname} %{_description}

%prep
%autosetup -p1 -n Piexif-%{version}

sed -i 's|==.*$||' requirements.txt
sed -i 's|unittest.makeSuite|unittest.defaultTestLoader.loadTestsFromTestCase|' tests/s_test.py

%generate_buildrequires
%pyproject_buildrequires requirements.txt -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.1.3-21
- Rebuilt for Python 3.13

* Sat Feb  3 2024 José Matos <jamatos@fedoraproject.org> - 1.1.3-20
- Replace deprecated functions in tests.
- Update the spec file to more modern Python guidelines

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.1.3-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.3-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.3-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 José Matos <jamatos@fedoraproject.org> - 1.1.3-8
- Add patch to run tests with Pillow >= 7.2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 José Matos <jamatos@fedoraproject.org> - 1.1.3-1
- update to 1.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.13-5
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.13-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.13-1
- Update to 1.0.13

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.10-1
- Update to 1.0.10

* Thu Jan 19 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.8-1
- Update to 1.0.8

* Tue Sep  6 2016 José Matos <jamatos@fedoraproject.org> - 1.0.7-1
- update to 1.0.7
- remove files need for tests since they have been included upstream

* Thu Sep  1 2016 José Matos <jamatos@fedoraproject.org> - 1.0.5-1
- Initial package.
