%bcond_without check

%global srcname emcee

Name: python-%{srcname}
Version: 3.1.4
Release: 2%{?dist}
Summary: The Python ensemble sampling toolkit for affine-invariant MCMC
License: MIT

URL: https://emcee.readthedocs.io/en/stable/
Source0: %{pypi_source}
BuildRequires: python3-devel 
BuildArch: noarch

%global _description %{expand: 
emcee is a stable, well tested Python implementation of the affine-invariant ensemble sampler for Markov chain Monte Carlo (MCMC) proposed by Goodman & Weare (2010). The code is open source and has already been used in several published projects in the Astrophysics literature.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist setuptools_scm}
%if %{with check}
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist scipy}
BuildRequires: %{py3_dist h5py}
%endif

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files emcee

%if %{with check}
%check
# Some tests are failling in ppc64le with longdouble
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}/%{python3_sitelib}
   pytest-%{python3_version} \
%ifarch ppc64le
   --deselect "emcee/tests/integration/test_longdouble.py::test_longdouble_actually_needed[TempHDFBackend]" \
   --deselect "emcee/tests/unit/test_backends.py::test_longdouble_preserved[TempHDFBackend]" \
   --deselect "emcee/tests/unit/test_backends.py::test_hdf5_dtypes" \
%endif
   emcee
popd
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS.rst HISTORY.rst README.rst 

%changelog
* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 3.1.4-2
- Rebuilt for Python 3.12

* Tue May 02 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.4-1
- New upstream source 3.1.4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.3-1
- New upstream source 3.1.3

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.1.2-2
- Rebuilt for Python 3.11

* Sun Jun 12 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.2-1
- New upstream source 3.1.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.1-1
- New upstream source 

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.2-4
- Rebuilt for Python 3.10

* Mon Feb 15 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 3.0.2-3
- Deselect some tests in ppc64le

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 3.0.2-1
- New upstream source (3.0.2)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.0.0-2
- New upstream source (3.0.0)
- Enable tests in python 3.8
- Updated sources

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild


* Thu Jul 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-15
- Do not run the tests on python 3.8 (bz #1705929)

* Thu Jul 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-13
- Add patch to fix the faulty test "test_nan_lnprob"

* Wed Feb 13 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-12
- Allow faillures in test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-10
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-5
- Python 2 binary package renamed to python2-emcee
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuild for Python 3.6

* Wed Jul 27 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.1-1
- New upstream source (2.2.1)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 14 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.0-2
- Remove reference to patch in specfile

* Wed Jul 13 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.2.0-1
- New upstream source (2.2.0)
- Update pypi url
- Remove numpy 1.11 patch (upstream fixed it)

* Tue Mar 29 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.0-5
- Provide python2 package
- Fix problem with numpy 1.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 15 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.0-1
- Initial spec
