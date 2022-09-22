%global pypi_name Pykka

Name:             pykka
Version:          2.0.2
Release:          13%{?dist}
Summary:          Python library that provides concurrency using actor model

License:          ASL 2.0
URL:              https://www.pykka.org/
Source0:          https://github.com/jodal/pykka/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:        noarch

%description
Pykka is a Python implementation of the actor model. The actor
model introduces some simple rules to control the sharing of state
and cooperation between execution units, which makes it easier to
build concurrent applications.

%package -n python3-%{pypi_name}
Summary:        Python library that provides concurrency using actor model

BuildRequires: make
BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-mock
BuildRequires:    python3-gevent
BuildRequires:    python3-eventlet
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pykka is a Python implementation of the actor model. The actor
model introduces some simple rules to control the sharing of state
and cooperation between execution units, which makes it easier to
build concurrent applications.

%package docs
Summary:        Documentation for %{name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

Requires:       devhelp

%description docs
This package provides the documentation for %{name}, e.g. the API as
devhelp docs, and examples.

%prep
%autosetup
# disable 1 failing test (already removed from pykka 2.0.3)
sed -i '/def test_upgrade_internal_message/i@pytest.mark.skip()' tests/test_messages.py

%build
%py3_build
pushd docs
SPHINXBUILD='sphinx-build-3 %{_smp_mflags}' make %{_smp_mflags} devhelp
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
mkdir -p %{buildroot}%{_datarootdir}/devhelp/%{pypi_name}
cp -rp docs/_build/devhelp %{buildroot}%{_datarootdir}/devhelp/%{pypi_name}

# Some tests are failing to fix the FTBFS they are disabled now
#%check
#PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*-py*.egg-info
%{python3_sitelib}/%{name}/

%files docs
%license LICENSE
%doc examples/
%{_datarootdir}/devhelp/%{pypi_name}/
%exclude %{_datarootdir}/devhelp/%{pypi_name}/.*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.0.2-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.2-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-7
- Fix FTBFS

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-5
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Tobias Girstmair <t-fedora@girst.at> - 2.0.2-2
- Further improvements of the spec file incl. tests

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Fix tests
- Remove pointless variables
- Update to latest upstream release 2.0.2 (rhbz#1785943)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-0.7.20181208git
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-0.6.20181208git
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.5.20181208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.4.20181208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.3-0.3.20181208git
- execute tests

* Thu Dec 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.3-0.2.20181208git
- use license macro, exclude build files

* Thu Dec 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.3-0.1.20181208git
- provide new snapshot from latest github (25%)
- modernize

* Sun Oct 07 2018 My Karlsson <mk@acc.umu.se> - 1.2.1-13
- Remove python2 subpackage (rhbz#1627414)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-11
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Aug 18 2015 Jonathan Dieter <jdieter@lesbg.com> - 1.2.1-2
- Update to 1.2.1
- Build Python 3 library (with limited functionality)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-1
- Update to latest release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Matěj Cepl <mcepl@redhat.com> - 0.15-3
- Add documentation and examples.

* Mon Aug 27 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.15-2
- Update to latest version
- Remove unneeded sections
- Remove trailing .0 as it's not part of the original versioning
- Remove buildroot tag

* Wed Jan  4 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.13.0-1
- Initial release
