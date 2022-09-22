%global     srcname  rstcheck

Name:       python-%{srcname}
Version:    3.3.1
Release:    13%{?dist}
Summary:    Checks syntax of reStructuredText and code blocks nested within it

License:    MIT
URL:        https://github.com/myint/rstcheck
Source0:    https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz


BuildArch:  noarch
%description
Checks syntax of reStructuredText and code blocks nested within it.

%package -n python3-%{srcname}
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
Requires:   python3-docutils
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Checks syntax of reStructuredText and code blocks nested within it.


%prep
%autosetup -n %{srcname}-%{version}
rm -frv %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS.rst
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*
%{_bindir}/%{srcname}

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.1-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.1-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.3.1-1
- Update to 3.3.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1-4
- Updated as per final comments
- add missing BR
- make URL complete without macro
- correct file lists

* Thu Oct 26 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1-3
- Update based on review comments
- Make BRs and Rs specific to sub packages
- Make file lists more specific
- Use summary macro

* Thu Oct 26 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1-2
- No need to provide different binaries - they provide same functionality
- https://fedoraproject.org/wiki/Packaging:Python#Executables_in_.2Fusr.2Fbin

* Wed Oct 25 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1-1
- Initial rpmbuild
