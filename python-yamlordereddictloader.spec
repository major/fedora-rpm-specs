%global srcname yamlordereddictloader
%global sum YAML loader for PyYAML that maintains key order

Name:		python-%{srcname}
Version:	0.4.0
Release:	17%{?dist}
Summary:	%{sum}

License:	MIT
URL:		https://github.com/fmenabe/python-yamlordereddictloader
Source0:	https://files.pythonhosted.org/packages/source/y/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-PyYAML

BuildArch: noarch

%description
This is a loader for PyYAML that maintains the order of the keys
and values in a dictionary as they appear in the input file. This
can be useful for certain applications where named values should
also be maintained in a particular order

%package -n python%{python3_pkgversion}-%{srcname}
Summary:	%{sum}
Requires:	python3-PyYAML
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This is a loader for PyYAML that maintains the order of the keys
and values in a dictionary as they appear in the input file. This
can be useful for certain applications where named values should
also be maintained in a particular order

%prep
%setup -q -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}.py*
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/%{srcname}.cpython*py*


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Greg Hellings <greg.hellings@gmail.com> - 0.4.0-1
- Upstream version 0.4.4
- Switched hard-coded python3 to use %%{python3_pkgversion}
- Addresses BZ#1647597

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.0-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Greg Hellings <greg.hellings@gmail.com> - 0.3.0-1
- New upstream version 0.3.0

* Thu Apr 20 2017 Greg Hellings <greg.hellings@gmail.com> - 0.2.2-2
- Removed outdated comments in spec file

* Thu Apr 20 2017 Greg Hellings <greg.hellings@gmail.com> - 0.2.2-1
- Upstream version 0.2.2
- Added new LICENSE from upstream to files

* Wed Apr 19 2017 Greg Hellings <greg.hellings@gmail.com> - 0.2.0-1
- Upstream version 0.2.0
- Added README.rst
- Added PyYAML/python3-PyYAML as requires

* Mon Apr 03 2017 Greg Hellings <greg.hellings@gmail.com> - 0.1.1-1
- Upstream version 0.1.1
