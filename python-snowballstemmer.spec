%global pypi_name snowballstemmer

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        2%{?dist}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/44/7b/af302bebf22c749c56c9c3e8ae13190b5b5db37a33d9068652e8f73b7089/snowballstemmer-2.2.0.tar.gz
Source1:        https://raw.githubusercontent.com/snowballstem/snowball/master/COPYING

BuildArch:      noarch

%description
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.


%if 0%{?python3_other_pkgversion}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildArch:      noarch
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}

%description -n python%{python3_other_pkgversion}-%{pypi_name}
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.
%endif # python3_other_pkgversion


%prep
%setup -qn %{pypi_name}-%{version}
# Remove upstream's egg-info
rm -rf %{pypi_name}.egg-info
cp %{SOURCE1} .


%build
%py3_build
%{?python3_other_pkgversion: %py3_other_build}


%install
%py3_install
%{?python3_other_pkgversion: %py3_other_install}


%check
# No tests


%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license COPYING
%doc README.rst
%{python3_other_sitelib}/%{pypi_name}-%{version}-py%{python3_other_version}.egg-info
%{python3_other_sitelib}/%{pypi_name}/
%endif # python3_other_pkgversion


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Julien Enselme <jujens@jujens.eu> - 2.2.0-1
- Update to 2.2.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.9.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 1.9.0-1
- Update to 1.9.0

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-10
- Subpackage python2-snowballstemmer has been removed
  See https://fedoraproject.org/wiki/Changes/Sphinx2

* Sun Feb 24 2019 Julien Enselme <jujens@jujens.eu> - 1.2.1-9
- Can build on EPEL7 (#1622605). Thanks to Scott K Logan for the patch.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.2.1-2
- Rebuild for Python 3.6

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 1.2.1-1
- Update to 1.2.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 1.2.0-2
- Rebuilt for python 3.5

* Mon Aug 24 2015 Julien Enselme <jujens@jujens.eu> - 1.2.0-1
- Initial package
