%global srcname atpublic
%global pkgname atpublic
%global summary Decorator for populating a Python module's __all__
%global _description \
This is a very simple decorator and function which populates a  \
module's __all__ and optionally the module globals.  \
This provides both a pure-Python implementation and a C implementation.  \
It is proposed that the C implementation be added to built-ins for  \
Python 3.6.


Name:           python-%{pkgname}
Version:        1.0
Release:        11%{?dist}
Summary:        %{summary}

License:        ASL 2.0
URL:            http://public.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python-srpm-macros
BuildRequires:  python%{python3_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-nose2
BuildRequires:  python%{python3_pkgversion}-flufl-testing
%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-nose2
BuildRequires:  python%{python3_other_pkgversion}-flufl-testing
%endif

%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pkgname}}
Requires:       python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version}


%build
export ATPUBLIC_BUILD_EXTENSION=1
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
export ATPUBLIC_BUILD_EXTENSION=1
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif


%check
%{__python3} -m nose2 -v
%if 0%{?with_python3_other}
%{__python3_other} -m nose2 -v
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc README.rst NEWS.rst
%{python3_sitearch}/public/
%{python3_sitearch}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitearch}/_public.*.so

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc README.rst NEWS.rst
%{python3_other_sitearch}/public/
%{python3_other_sitearch}/%{srcname}-%{version}*-py%{python3_other_version}.egg-info/
%{python3_other_sitearch}/_public.*.so
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0-10
- Rebuilt for Python 3.11

* Wed Mar 30 2022 Aurélien Bompard <abompard@fedoraproject.org> - 1.0-9
- rebuilt

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1.0-1
- Version 1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Dec 05 2016 Aurelien Bompard <abompard@fedoraproject.org> - 0.4-1
- Initial package.
