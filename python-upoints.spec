%global srcname upoints
%global sum Python modules for working with points on Earth

Name:           python-upoints
Version:        0.12.2
Release:        22%{?dist}
Summary:        %{sum}

License:        GPLv3+
URL:            https://pypi.python.org/pypi/upoints/
Source0:        https://pypi.python.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.bz2

# Patch needed for setup.py to read the README file (UTF-8) correctly,
# since Koji defaults to an ASCII locale.
# Fixed upstream: https://github.com/JNRowe/upoints/pull/2

Patch0:         upoints-utf8.patch

# Workaround for the edist binary to work correctly
# under Python 3.5+
# Reported upstream: https://github.com/JNRowe/upoints/issues/4
Patch1:			fix-edist-binary-under-python3.patch
BuildArch:      noarch

%description
upoints, previously called earth_distance, is a collection of modules for
working with points on a spherical object. It allows you to calculate the
distance and bearings between points, mangle xearth/xplanet data files, work
with online UK trigpoint databases and various other databases.

%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-lxml
Requires:       python3-aaargh
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
upoints, previously called earth_distance, is a collection of modules for
working with points on a spherical object. It allows you to calculate the
distance and bearings between points, mangle xearth/xplanet data files, work
with online UK trigpoint databases and various other databases.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CONTRIBUTING.rst NEWS.rst README.rst doc/
%license COPYING
%{_bindir}/edist
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.12.2-21
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.2-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12.2-9
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017  Petr Viktorin <pviktori@redhat.com> - 0.12.2-4
- Fix Python3 patch to use UTF-8 for README
- Fix the edist binary under Python 3.5+

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 02 2016  Fabian Affolter <mail@fabian-affolter.ch> - 0.12.2-1
- Support for py3 (rhbz#1309265)
- Update to latest upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to new upstream release 0.12.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-8
- Minor changes 

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-3
- Changed define to global 

* Sat Apr 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-2
- Removed ./

* Sat Apr 11 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-1
- Initial spec for Fedora
