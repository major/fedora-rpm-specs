# Filter the _speedups.so provides that otherwise comes into the provides
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

%global pypi_name pyScss
%global sname pyscss
# the package name is still python-scss
%global pname scss


Name:           python-scss
Version:        1.3.7
Release:        9%{?dist}
Summary:        A Scss compiler for Python

License:        MIT
URL:            https://github.com/Kronuz/pyScss
#Source0:        https://github.com/Kronuz/pyScss/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# get source file with spectool -g python-scss.spec
Source0:        https://github.com/Kronuz/pyScss/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  pcre-devel
BuildRequires:  gcc

%description
A Scss compiler for Python

%package -n python3-%{pname}
Summary:        A Scss compiler for Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
Requires:       python3-six
Requires:       python3-setuptools

%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
A Scss compiler for Python

%prep
%autosetup -n %{pypi_name}-%{version}
# Change shebang according to Python version

# Fix shebangs
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build
# build documentationx
cd docs
make SPHINXBUILD=sphinx-build-3 man

%install
%py3_install
chmod +x %{buildroot}%{python3_sitearch}/scss/tool.py

# install man page
mkdir -p %{buildroot}%{_mandir}/man1/
cp -ar docs/_build/man/pyscss.1 %{buildroot}%{_mandir}/man1/pyscss.1


%files -n python3-%{pname}
%doc DESCRIPTION README.rst
%license LICENSE
%{python3_sitearch}/*
%{_bindir}/pyscss
%{_bindir}/less2scss
%{_mandir}/man1/pyscss.1.gz


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.7-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-2
- Rebuilt for Python 3.9

* Mon Apr 20 2020 Matthias Runge <mrunge@redhat.com> - 1.3.7-1
- rebase to 1.3.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-5
- Subpackage python2-scss has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-3
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Jan Beran <jberan@redhat.com - 1.3.5-2
- Fix of python3-scss requires both Python 2 and Python 3 (rhbz #1546811)

* Wed Feb 21 2018 Matthias Runge <mrunge@redhat.com> - 1.3.5-1
- update to 1.3.5
- add gcc to buildrequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.4-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-7
- Rebuild for Python 3.6

* Fri Nov 25 2016 Matthias Runge <mrunge@redhat.com> - 1.3.4-6
- add requires: python-pathlib (rhbz#1299228)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul  1 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.4-4
- Drop incorrect provides

* Fri Jul 01 2016 Matthias Runge <mrunge@redhat.com> - 1.3.4-3
- fix provides/package names

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Matthias Runge <mrunge@redhat.com> - 1.3.4-1
- update to 1.3.4, requirement for fix FTBFS for python-django-pyscss
  (rhbz#1239832)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 07 2014 Matthias Runge <mrunge@redhat.com> - 1.2.1-1
- update to 1.2.1 (rhbz#1148966)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-3
- Require python-setuptools as thats needed for the binary to work

* Wed Nov 06 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.2.0-2
- Buildrequire set to python2-devel
- Added buildrequire pcre-devel
- Changed URL to Source
- Added -a to cp to retain timestamp

* Thu Oct 17 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.2.0-1
- Initial packaging

