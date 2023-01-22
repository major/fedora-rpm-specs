%global	module	tkrzw

Name:		python-%{module}
Version:	0.1.28
Release:	9%{?dist}
License:	ASL 2.0
Summary:	TKRZW Python bindings
URL:		https://dbmx.net/tkrzw/
Source0:	https://dbmx.net/tkrzw/pkg-python/%{module}-python-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	python3-setuptools
# python3-devel
BuildRequires:	pkgconfig(python3)
# zlib-devel
#BuildRequires:	pkgconfig(zlib)
# tkrzw_build_util
BuildRequires:	tkrzw >= 1.0.21
# tkrzw-devel
BuildRequires:	pkgconfig(tkrzw) >= 1.0.21
# python3-sphinx
BuildRequires:	python3dist(sphinx)
%if 0%{?fedora} > 35
# Temporary disabled: https://github.com/estraier/tkrzw-python/issues/4
ExcludeArch:	i686
%endif

%description
TKRZW is a library of routines for managing a key-value database.

%package -n	python3-%{module}
Summary:	%{summary}
%if 0%{?epel} && 0%{?epel} < 9
%{?python_provide:%python_provide python3-%{module}}
%endif

%description -n	python3-%{module}
TKRZW is a library of routines for managing a key-value database.

%package	doc
Summary:	%{summary} - API documentation
BuildArch:	noarch

%description	doc
TKRZW is a library of routines for managing a key-value database.
This package contains API documentation of it.


%prep
%autosetup -n %{module}-python-%{version}


%build
%py3_build
%make_build apidoc


%install
%py3_install


%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%make_build check


%files -n python3-%{module}
%license COPYING
%{python3_sitearch}/tkrzw-0.1-py%{python3_version}.egg-info
%if 0%{?epel} && 0%{?epel} < 9
%{python3_sitearch}/tkrzw.cpython-%{python3_version_nodots}m-*-linux-gnu*.so
%else
%{python3_sitearch}/tkrzw.cpython-%{python3_version_nodots}-*-linux-gnu*.so
%endif

%files doc
%license COPYING
%doc README CONTRIBUTING.md example?.py api-doc/


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.28-7
- Rebuilt for Python 3.11

* Fri Apr 08 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-6
- Temporary excluded i686 for F36+

* Fri Apr 08 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-5
- Rebuild against tkrzw-1.0.24

* Wed Mar 09 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-4
- Rebuild against tkrzw-1.0.23

* Sun Jan 23 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-3
- Rebuild against tkrzw-1.0.22

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 27 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-1
- Version bump

* Thu Nov 18 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.27-1
- Version bump

* Sat Oct 09 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.23-1
- Version bump
- Build against tkrzw-1.0.17
- ppc64le enabled back

* Sat Sep 25 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.22-1
- Version bump
- Build against tkrzw-1.0.13
- ppc64le temporary excluded

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.7-2
- Rebuilt for Python 3.10

* Fri May 14 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.7-1
- Version bump
- Build against tkrzw-0.9.16

* Tue May 04 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.6-1
- Version bump

* Sun Feb 14 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.4-2
- python_provide fix
- -doc subpackage added
- check introduced
- epel8 compatible

* Sat Feb 06 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.4-1
- Initial build
