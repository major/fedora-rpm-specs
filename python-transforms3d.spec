%global modname transforms3d

Name:           python-%{modname}
Version:        0.3.1
Release:        18%{?dist}
Summary:        3 dimensional spatial transformations

License:        BSD
URL:            http://matthew-brett.github.io/transforms3d/
Source0:        https://github.com/matthew-brett/transforms3d/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

%description
Code to convert between various geometric transformations.

* Composing rotations / zooms / shears / translations into affine matrix;
* Decomposing affine matrix into rotations / zooms / shears / translations;
* Conversions between different representations of rotations, including:
** 3x3 Rotation matrices;
** Euler angles;
** quaternions.


%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-numpy
Requires:       python3-numpy
Recommends:     python3-sympy

%description -n python3-%{modname}
Code to convert between various geometric transformations.

* Composing rotations / zooms / shears / translations into affine matrix;
* Decomposing affine matrix into rotations / zooms / shears / translations;
* Conversions between different representations of rotations, including:
** 3x3 Rotation matrices;
** Euler angles;
** quaternions.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
nosetests-%{python3_version} -v

%files -n python3-%{modname}
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitelib}/%{modname}*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.1-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-5
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.3-1
- Update to 0.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.1-3
- Backport another upstream patch

* Sun Nov 01 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.1-2
- Backport patch from upstream (nipy/nipy)

* Sun Nov 01 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.1-1
- Initital package
