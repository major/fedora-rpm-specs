%global pypi_name Pint
%bcond_with docs

Name:           python-pint
Version:        0.16.1
Release:        8%{?dist}
Summary:        Physical quantities module

License:        BSD
URL:            https://github.com/hgrecco/pint
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros

%description
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.

%package -n python3-pint
Summary:        Physical quantities module
%{?python_provide:%python_provide python3-pint}

BuildRequires:  python3-numpy
BuildRequires:  python3-pytest

%description -n python3-pint
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.

%if %{with docs}
%package -n python3-pint-doc
Summary:        Documentation for the pint module
%{?python_provide:%python_provide python3-pint-doc}

BuildRequires:  pandoc
BuildRequires:  python3-graphviz
BuildRequires:  python3-ipykernel
BuildRequires:  python3-jupyter-client
BuildRequires:  python3-matplotlib
BuildRequires:  python3-nbsphinx
BuildRequires:  python3-pandas
BuildRequires:  python3-dask
BuildRequires:  python3-pygments
BuildRequires:  python3-sphinx
BuildRequires:  python3-xarray

%description -n python3-pint-doc
Documentation for the pint module
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

# drop numpy version requirement
sed -i '/@helpers.requires_numpy_at_least("1.16")/d' pint/testsuite/test_quantity.py

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%if %{with docs}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 docs html
# remove the sphinx-build leftovers

rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
%pytest

%files -n python3-pint
%license LICENSE
%{_bindir}/pint-convert
%{python3_sitelib}/pint
%{python3_sitelib}/Pint-%{version}.*

%if %{with docs}
%files -n python3-pint-doc
%doc html
%license docs/_themes/LICENSE
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.16.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.16.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Matthias Runge <mrunge@redhat.com> - 0.16.1-2
- rebuild without bootstrap
- fix FTBFS (rhbz#1914333)

* Mon Sep 21 2020 Lumír Balhar <lbalhar@redhat.com> - 0.13-3
- Fix test dependencies and execution

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13-1
- Update to 0.13

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Matthias Runge <mrunge@redhat.com> - 0.10.1-1
- update to 0.10.1 (rhbz#1789066)
- modernize specfile

* Thu Sep 05 2019 Matthias Runge <mrunge@redhat.com> - 0.9-5
- skip test_quantity for now (rhbz#1706212)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Matthias Runge <mrunge@redhat.com> - 0.9-3
- Use context manager for assertWarns and fix DeprecationWarning
  resolves: rhbz#1706212

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-2
- Subpackages python2-pint, python2-pint-doc have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Feb 25 2019 Yatin Karel <ykarel@redhat.com> - 0.9-1
- Update to 0.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 06 2015 Matthias Runge <mrunge@redhat.com> - 0.6-5
- fix uppercase/lowercase naming, fix obsoletes

* Fri Sep 04 2015 Chandan Kumar <chkumar246@gmail.com> - 0.6-4
- Add python2 and python3 subpackages

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Matthias Runge <mrunge@redhat.com> - 0.6-2
- change BR python-devel to python2-devel (rhbz#1173109)

* Thu Dec 11 2014 Matthias Runge <mrunge@redhat.com> - 0.6-1
- Initial package.
