%global pypi_name importmagic

Name:           python-%{pypi_name}
Version:        0.1.7
Release:        23%{?dist}
Summary:        Python library to auto-magically add, remove and manage imports

License:        BSD
URL:            http://github.com/alecthomas/importmagic
Source0:        https://pypi.python.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{fedora} >= 24
%else
BuildRequires:  pytest
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytest

%description
The goal of this package is to be able to automatically manage imports
in Python. To that end it can:

o Build an index of all known symbols in all packages.

o Find unresolved references in source, and resolve them against the
  index, effectively automating imports.

o Automatically arrange imports according to PEP8.

It was originally written for the Sublime Text 2 Python Import Magic
plugin.


%package -n python3-%{pypi_name}
Summary:     Python library to auto-magically add, remove and manage imports
Requires:    python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The goal of this package is to be able to automatically manage imports
in Python. To that end it can:

o Build an index of all known symbols in all packages.

o Find unresolved references in source, and resolve them against the
  index, effectively automating imports.

o Automatically arrange imports according to PEP8.

It was originally written for the Sublime Text 2 Python Import Magic
plugin.


%prep
%setup -q -n %{pypi_name}-%{version}

rm -rf %{pypi_name}.egg-info

# Unbundle six.py
# https://github.com/alecthomas/importmagic/issues/23
pushd %{pypi_name}
rm -f six.py
for i in *.py ; do
    sed -i -e 's/importmagic.six/six/g' ${i}
done
popd

# We're going to use py.test as packaged for Fedora rather than the
# bundled binary blob
rm -f runtests.py

# Move test files out of the importmagic directory so they don't get
# installed. Removing them after install would also require removing
# the __pycache__ files, so let's just avoid the faff.
mkdir test
mv %{pypi_name}/*test* test

%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitelib} py.test-3 test

%files -n python3-%{pypi_name}
%doc README.md CHANGES
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.7-22
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.7-19
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.7-10
- Subpackage python2-importmagic has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 24 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.7-1
- Update to 0.1.7

* Tue Mar  8 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.5-4
- Simplify testing logic to test files in buildroot

* Mon Mar  7 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.5-3
- Remove all files from the importmagic directory before linking
  installed files

* Mon Mar  7 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.5-2
- Don't leave __pycache__ entries installed for the test files

* Mon Mar  7 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.5-1
- Update to 0.1.5
- Remove Python 3 conditional building - always build
- Use new standard Python build and install macros
- No longer build in separate directories
- Run tests against installed modules rather than sources

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6.033e3efgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.3-5.033e3efgit
- Update to current git snapshot to fix Python 3.5 build and test issues

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Jul 12 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.3-3
- Fix typo in %%check
- Remove macro from URL
- Unbundle python-six files
- Require and BuildRequire (for %%check) python[3]-six
- Remove tabs from spec file

* Sat Jul 11 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.3-2
- Add BuildRequires for python-setuptools and python3-setuptools

* Fri Jul 10 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.1.3-1
- Initial package
