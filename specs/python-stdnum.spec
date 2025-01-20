%global srcname stdnum

Name:           python-%{srcname}
Version:        1.20
Release:        4%{?dist}
Summary:        Python module to handle standardized numbers and codes

License:        LGPL-2.0-or-later
URL:            http://arthurdejong.org/python-stdnum/
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

#BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# needed for tests
#BuildRequires:  python3-nose

%global _description %{expand:
Parse, validate and reformat standard numbers and codes. This library offers
functions for parsing, validating and reformatting standard numbers and codes
in various formats like personal IDs, VAT numbers, IBAN and more.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1

# Patch out coverage options
sed -r -i 's/--cov[^[:blank:]]*//g' setup.cfg

# Patch out unnecessary coverage dependencies:
sed -r -i '/pytest-cov/d' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{srcname}

%check
export LANG=C.utf-8
%tox


%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc NEWS README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.20-2
- Rebuilt for Python 3.13

* Mon Mar 18 2024 Dan Horák <dan[at]danny.cz> - 1.20-1
- updated to 1.20 (rhbz#2269981)

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 22 2023 Dan Horák <dan[at]danny.cz> - 1.19-1
- updated to 1.19 (#2232942)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.18-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Dan Horák <dan[at]danny.cz> - 1.18-1
- updated to 1.18 (#2142430)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.17-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Dan Horák <dan[at]danny.cz> - 1.17-1
- updated to 1.17 (#2010089)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.16-2
- Rebuilt for Python 3.10

* Wed Feb 17 2021 Dan Horák <dan[at]danny.cz> - 1.16-1
- updated to 1.16 (#1925795)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Dan Horák <dan[at]danny.cz> - 1.15-1
- updated to 1.15 (#1915087)

* Mon Aug 10 2020 Dan Horák <dan[at]danny.cz> - 1.14-1
- updated to 1.14 (#1867401)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13-2
- Rebuilt for Python 3.9

* Fri Feb 21 2020 Dan Horák <dan[at]danny.cz> - 1.13-1
- updated to 1.13 (#1792735)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Dan Horák <dan[at]danny.cz> - 1.12-1
- updated to 1.12 (#1765966)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Dan Horák <dan[at]danny.cz> - 1.11-1
- updated to 1.11 (#1697435)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Dan Horák <dan[at]danny.cz> - 1.3-10
- drop Python2 subpackage (#1627313)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Dan Horák <dan@danny.cz> - 1.3-2
- address comments from package review (#1357566)

* Mon Jul 18 2016 Dan Horák <dan@danny.cz> - 1.3-1
- Initial package.
