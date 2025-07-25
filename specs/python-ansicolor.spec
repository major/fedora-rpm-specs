%global srcname ansicolor
%global desc %{srcname} is a library to produce ANSI color output, colored highlighting\
and diffing.


%if 0%{?fedora}
  %bcond_without python3
  %if 0%{?fedora} > 29
    %bcond_with python2
  %else
    %bcond_without python2
  %endif
%else
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif


Name:           python-%{srcname}
Version:        0.2.4
Release:        34%{?dist}
Summary:        A library to produce ANSI color output

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/numerodix/%{srcname}
Source0:        https://github.com/numerodix/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
%endif
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
%endif

%description
%{desc}


%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%endif


%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}
%endif


%package doc
Summary:        Documentation for %{name}

%description doc
This package contains the documentation for %{name}.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}

PYTHONPATH=$(pwd) ./build_docs.sh
rm -f docs/_build/html/.buildinfo


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%check
%{?with_python2:py.test-%{python2_version} -v}
%{?with_python3:py.test-%{python3_version} -v}


%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif

%files doc
%license LICENSE
%doc docs/_build/html/*


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.2.4-33
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.4-31
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.4-29
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.2.4-25
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.4-22
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.4-19
- Rebuilt for Python 3.10

* Tue Feb 16 2021 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-18
- BuildRequire make for https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Pavel Raiskup <praiskup@redhat.com> - 0.2.4-9
- python3/python2 ifdefs so we can build for both Fedora/EPEL
- disable python2 package on f30+ (rhbz#1630071)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 0.2.4-3
- Fix spelling errors

* Thu Jan 05 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 0.2.4-2
- Use %%{summary} macro
- Add license file to -doc subpackage

* Tue Dec 20 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 0.2.4-1
- Initial release
