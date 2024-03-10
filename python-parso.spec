%global srcname parso
%global common_description %{expand:
Parso is a Python parser that supports error recovery and round-trip parsing
for different Python versions (in multiple Python versions). Parso is also able
to list multiple syntax errors in your python file.  Parso has been
battle-tested by jedi. It was pulled out of jedi to be useful for other
projects as well.  Parso consists of a small API to parse Python and analyse
the syntax tree.}

Name:           python-%{srcname}
Version:        0.8.3
Release:        10%{?dist}
Summary:        Parser that supports error recovery and round-trip parsing
License:        MIT and Python
BuildArch:      noarch
URL:            https://github.com/davidhalter/parso
Source:         %pypi_source

# https://github.com/davidhalter/parso/pull/220
Patch:          0001-ENH-add-grammar-file-from-py313.patch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}

sed -e 's/pytest<6.0.0/pytest/' -i setup.py
sed -e '/^addopts/d' -i pytest.ini


%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# https://github.com/davidhalter/parso/issues/123
# https://bugzilla.redhat.com/show_bug.cgi?id=1830965
%pytest --verbose -k "not test_python_exception_matches"


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Thu Mar 07 2024 Carl George <carlwgeorge@fedoraproject.org> - 0.8.3-10
- Add patch for Python 3.13 compatibility rhbz#2246284

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.3-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.3-3
- Rebuilt for Python 3.11

* Mon Apr 25 2022 Carl George <carl@george.computer> - 0.8.3-2
- Remove upstream pytest addopts
- Resolves: rhbz#2078414

* Fri Apr 08 2022 Carl George <carl@george.computer> - 0.8.3-1
- Latest upstream
- Resolves: rhbz#2027862

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2^1.da3a748-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Carl George <carl@george.computer> - 0.8.2^1.da3a748-1
- Latest upstream snapshot
- Resolves: rhbz#1906491
- Resolves: rhbz#1987878

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Carl George <carl@george.computer> - 0.8.0-2
- Rebuild

* Wed Sep 09 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.8.0-1
- Update to 0.8.0 (rhbz#1860194)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Carl George <carl@george.computer> - 0.6.2-1
- Latest upstream
- Add patch0 to fix test suite on Python 3.8.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Carl George <carl@george.computer> - 0.5.2-1
- Latest upstream

* Thu Oct 17 2019 Carl George <carl@george.computer> - 0.5.1-4
- Run tests on el8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Carl George <carl@george.computer> - 0.5.1-1
- Latest upstream
- Drop EPEL python34 subpackage
- Disable python2 package on F31+ and EL8+ rhbz#1733248

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Carl George <carl@george.computer> - 0.5.0-1
- Latest upstream

* Mon Apr 08 2019 Carl George <carl@george.computer> - 0.4.0-1
- Latest upstream rhbz#1668959
- Don't use common documentation directory between subpackages

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 08 2018 Carl George <carl@george.computer> - 0.3.1-1
- Latest upstream
- Use common documentation directory
- Enable python36 subpackage for EPEL

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Carl George <carl@george.computer> - 0.2.1-1
- Latest upstream

* Mon Apr 16 2018 Carl George <carl@george.computer> - 0.2.0-1
- Latest upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Carl George <carl@george.computer> - 0.1.1-2
- Be more explicit with the files in site-packages

* Tue Dec 26 2017 Carl George <carl@george.computer> - 0.1.1-1
- Initial package
