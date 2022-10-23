%global pypi_name numpy-stl

Name:           python-%{pypi_name}
Version:        2.17.1
Release:        1%{?dist}
Summary:        Library for reading, writing and modifying STL files

License:        BSD
URL:            https://github.com/WoLpH/numpy-stl/
Source:         %{pypi_source}

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

%ifnarch armv7hl
# the test is optional based on the presence of PyQt5
# xvfb somehow fails on this arch
BuildRequires:  python3-PyQt5
BuildRequires:  /usr/bin/xvfb-run
%endif

%description
Simple library to make working with STL files (and 3D objects in general) fast
and easy. Due to all operations heavily relying on numpy this is one of the
fastest STL editing libraries for Python available.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Simple library to make working with STL files (and 3D objects in general) fast
and easy. Due to all operations heavily relying on NumPy this is one of the
fastest STL editing libraries for Python available.

%package        doc
Summary:        %{name} documentation
Suggests:       python3-%{pypi_name}
BuildArch:      noarch
%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files stl

%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/stl
%{_bindir}/stl2bin
%{_bindir}/stl2ascii

%files doc
%doc html

%changelog
* Tue Oct 18 2022 Karolina Surma <ksurma@redhat.com> - 2.17.1-1
- Update to 2.17.1
Resolves: rhbz#2086213

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.16.3-2
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Karolina SUrma <ksurma@redhat.com> - 2.16.3-1
- Update to 2.16.3
Resolves: rhbz#2000197

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.16.0-2
- Rebuilt for Python 3.10

* Thu Apr 01 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.16.0-1
- Update to 2.16.0

* Wed Feb 17 2021 Lumír Balhar <lbalhar@redhat.com> - 2.15.1-1
- Update to 2.15.1
Resolves: rhbz#1889048

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.11.1-1
- Update to 2.11.1 (#1816884)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.10.1-2
- Rebuilt for Python 3.9

* Thu Mar 12 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.10.1-1
- Update to 2.10.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.10.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.10.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Lumír Balhar <lbalhar@redhat.com> - 2.10.0-1
- Update to 2.10.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 2.8.0-1
- Update to 2.8.0, fixes a long-standing bug with ASCII STL files (#1589520)

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-1
- Update to 2.7.0 (#1595001)
- Make doc subpackage noarch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-1
- Update to 2.6.0 (#1577429)
- Add a patch to support Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-2
- Rebuilt for Python 3.7

* Fri May 11 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-1
- Updated to 2.4.1 (#1475307)
- Enable automatic dependency generator, drop nine from BRs
- Enable tests on armv7hl once again (it works now)
- Add tolerance to tests that check float equality, fixes test failure on ppc64le

* Wed Feb 14 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-1
- Updated to 2.3.2 to fix FTBFS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-1
- Updated to 2.2.3

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-1
- Updated to 2.2.2

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-1
- Updated to 2.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-1
- New version with LICENSE
- Add patch for Big Endian
- Disable tests on armv7hl for now

* Sun Dec 04 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-1
- Initial package
