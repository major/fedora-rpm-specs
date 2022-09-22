%global srcname pecan-notario

Name:           python-%{srcname}
Version:        0.0.3
Release:        26%{?dist}
Summary:        JSON validation for Pecan with Notario
License:        BSD
URL:            https://github.com/alfredodeza/pecan-notario
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

Patch0001: 0001-exceptions-webob-1.7-compat.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-notario
BuildRequires:  python3-pecan

%description
Notario is flexible and succinct Python dictionary validator with the ability
to validate against both keys and values. Schemas are smaller and readable
representations of data being validated.

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3
Requires:       python3-notario
Requires:       python3-pecan

%description -n python3-%{srcname}
Notario is flexible and succinct Python dictionary validator with the ability
to validate against both keys and values. Schemas are smaller and readable
representations of data being validated.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{py3_build}

%install
%py3_install

%check
export PYTHONPATH=$(pwd)
py.test-%{python3_version} -v pecan_notario/tests

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 0.0.3-25
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.3-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-13
- Subpackage python2-pecan-notario has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 26 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 0.0.3-12
- exceptions: webob 1.7 compat

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-7
- Update Source0 URL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 15 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-3
- correct license tag (rhbz#1315816)

* Tue Mar 15 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-2
- use %%global instead of %%define (rhbz#1315816)

* Mon Mar 07 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-1
- Initial package
