%global srcname bitstring

Name:           python-%{srcname}
Version:        4.1.4
Release:        6%{?dist}
Summary:        Simple construction, analysis and modification of binary data

License:        MIT
URL:            https://github.com/scott-griffiths/bitstring
Source0:        https://github.com/scott-griffiths/bitstring/archive/%{srcname}-%{version}/%{srcname}-%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{srcname}-%{version}

sed -i '1{s|^#!\(/usr\)\?/bin/\(env \)\?python\d\?$||}' %{srcname}/__init__.py


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files bitstring


%check
%{__python3} -m unittest


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md release_notes.txt


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.1.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Scott K Logan <logans@cottsay.net> - 4.1.4-1
- Update to 4.1.4 (rhbz#2143436)
- Define _description variable to reduce duplication
- Drop macro from URL to improve ergonomics
- Use modern Python packaging macros

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1.9-7
- Rebuilt for Python 3.12

* Thu Jan 26 2023 Scott K Logan <logans@cottsay.net> - 3.1.9-6
- Add missing dependency on setuptools (rhbz#2142041)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.9-3
- Rebuilt for Python 3.11

* Fri May 06 2022 Scott K Logan <logans@cottsay.net> - 3.1.9-2
- Switch from nose to pytest

* Fri May 06 2022 Scott K Logan <logans@cottsay.net> - 3.1.9-1
- Update to 3.1.9 (rhbz#1983354)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.7-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Scott K Logan <logans@cottsay.net> - 3.1.7-1
- Update to 3.1.7 (rhbz#1831898)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Scott K Logan <logans@cottsay.net> - 3.1.6-1
- Update to 3.1.6
- Introduce Python 3 subpackage in EPEL

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.5-7
- Subpackage python2-bitstring has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.5-5
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.5-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Scott K Logan <logans@cottsay.net> - 3.1.5-1
- Update to 3.1.5
- Include LICENSE file

* Tue Apr 26 2016 Scott K Logan <logans@cottsay.net> - 3.1.4-1
- Initial package
