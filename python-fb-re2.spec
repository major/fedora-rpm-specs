%global srcname fb-re2
%global _description %{expand:
python-fb-re2 is a Python extension that wraps Google's RE2 regular expression
library.

This is Facebook's pyre2 Python extension that wraps Google's RE2 regular
expression library. It implements many of the features of Python's built-in re
module with compatible interfaces.}

Name:               python-%{srcname}
Version:            1.0.7
Release:            15%{?dist}
Summary:            Python wrapper for Google's RE2 library

License:            BSD
URL:                https://github.com/facebook/pyre2
Source0:            %pypi_source

%description %_description

%package -n python3-%{srcname}
Summary:            %{summary}
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      re2-devel
BuildRequires:      gcc-c++
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README
%pycached %{python3_sitearch}/re2.py
%{python3_sitearch}/*re2*.so
%{python3_sitearch}/fb_re2-*.egg-info/

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.7-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.7-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-7
- Rebuilt for libre2.so.9

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-2
- Rebuilt for Python 3.9

* Tue Mar 10 2020 Fabien Boucher <fboucher@redhat.com> - 1.0.7-1
- Bump to 1.0.7

* Sat Apr 14 2018 Tristan Cacqueray <tdecacqu@redhat.com> - 1.0.6-1
- Bump to 1.0.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Mads Kiilerich <mads@kiilerich.com> - 1.0.5-1
- python3-re2 1.0.5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mads Kiilerich <mads@kiilerich.com> - 1.0.4-1
- change from the axiak/pyre2 fork back to the upstream facebook/pyre2
- enable tests

* Thu Feb 12 2015 Ralph Bean <rbean@redhat.com> - 0.2.20-2.20150211git382bb74
- Move to a post-release git checkout to include various bugfixes.
- Remove rpath settings.
- Use Cython for the build.

* Wed Feb 11 2015 Ralph Bean <rbean@redhat.com> - 0.2.20-1
- initial package for Fedora
