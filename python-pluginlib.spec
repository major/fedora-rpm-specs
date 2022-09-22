%global pypi_name pluginlib
%global sum  A framework for creating and importing plugins in Python
%global desc Pluginlib is a Python framework for creating and importing plugins.\
Pluginlib makes creating plugins for your project simple.

%bcond_without python3

# Drop Python 2 with Fedora 30 and EL8
%if (0%{?fedora} && 0%{?fedora} < 30) || (0%{?rhel} && 0%{?rhel} < 8)
  %bcond_without python2
%else
  %bcond_with python2
%endif


Name:           python-%{pypi_name}
Version:        0.9.0
Release:        3%{?dist}
Summary:        %{sum}

License:        MPLv2.0
URL:            https://github.com/Rockhopper-Technologies/pluginlib
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-mock

# Additional build requirements for Python 2.6
%if 0%{?el6}
BuildRequires:  python-unittest2
BuildRequires:  python-importlib
%endif
%endif

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%endif

%description
%{desc}


# Python 2 package
%if %{with python2}
%package -n     python2-%{pypi_name}

Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:       python2-setuptools

%if 0%{?el6}
Requires:  python-importlib
%endif

%description -n python2-%{pypi_name}
%{desc}
%endif

# Python 3 package
%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}
%endif

# Python 3 other package
%if 0%{?with_python3_other}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}
Requires:       python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-%{pypi_name}
%{desc}
%endif


%prep
%autosetup -p0 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py2_install
%endif


%check
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python3}
%{__python3} setup.py test
%endif

%if 0%{?with_python3_other}
%{__python3_other} setup.py test
%endif


%if %{with python2}
%files -n python2-%{pypi_name}
%doc README*
%license LICENSE
%{python2_sitelib}/pluginlib*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README*
%license LICENSE
%{python3_sitelib}/pluginlib*
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%doc README*
%license LICENSE
%{python3_other_sitelib}/pluginlib*
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.11

* Wed Mar 30 2022 Avram Lubkin <aviso@rockhopper.net> - 0.9.0-1
- Update to 0.9.0 (#2054005)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.10

* Sat Feb 20 2021 Avram Lubkin <aviso@rockhopper.net> - 0.8.2-1
- 0.8.2 Release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Avram Lubkin <aviso@rockhopper.net> - 0.8.1-1
- 0.8.1 Release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Avram Lubkin <aviso@rockhopper.net> - 0.8.0-1
- 0.8.0 Release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Avram Lubkin <aviso@rockhopper.net> - 0.7.0-1
- 0.7.0 Release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Avram Lubkin <aviso@rockhopper.net> - 0.6.2-1
- 0.6.2 Release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Avram Lubkin <aviso@rockhopper.net> - 0.6.1-1
- 0.6.1 Release

* Sat Aug 04 2018 Avram Lubkin <aviso@rockhopper.net> - 0.6.0-2
- EL6 build requirements should only apply to Python 2

* Mon Jul 23 2018 Avram Lubkin <aviso@rockhopper.net> - 0.6.0-1
- 0.6.0 Release

* Mon Jul 23 2018 Avram Lubkin <aviso@rockhopper.net> - 0.5.1-2
- Change with_pythonX to use bcond_with(out)
- Make files sections more specific

* Mon Jul 23 2018 Avram Lubkin <aviso@rockhopper.net> - 0.5.1-1
- Initial package.
