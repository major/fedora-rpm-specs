%global srcname     quantities

Name:       python-%{srcname}
Version:    0.13.0
Release:    4%{?dist}
Summary:    Support for physical quantities with units, based on numpy

License:    BSD
URL:        http://python-quantities.readthedocs.io/
Source0:    %{pypi_source}

BuildRequires:  git-core

# From
# https://raw.githubusercontent.com/python-quantities/python-quantities/master/doc/user/license.rst
Source1:    license.rst

BuildArch:      noarch


%global _description\
Quantities is designed to handle arithmetic and conversions of physical\
quantities, which have a magnitude, dimensionality specified by various units,\
and possibly an uncertainty. See the tutorial for examples. Quantities builds\
on the popular numpy library and is designed to work with numpy ufuncs, many of\
which are already supported. Quantities is actively developed, and while the\
current features and API are stable, test coverage is incomplete so the package\
is not suggested for mission-critical applications.

%description %_description

%package -n python3-%{srcname}
Summary:    Support for physical quantities with units, based on numpy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
Requires:       python3-numpy

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -S git
cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc CHANGES.txt license.rst
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.13.0-1
- Update to 0.13.0

* Tue Aug 17 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.5-1
- Update to latest release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.3-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.3-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.3-2
- Move BR outside conditional since new autosetup command wants git even without patches

* Thu Oct 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.3-1
- Update to 0.12.3
- Include patch to fix test on F31+

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-3
- Subpackage python2-quantities has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.2-1
- Rebuilt for new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Jan 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.1-1
- Update to latest release
- Update source url
- Update spec per new python guidelines

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.1-9
- Python 2 binary package renamed to python2-quantities
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 07 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.10.1-1
- Include license file

* Tue Oct 07 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.10.1-1
- Initial rpm build
