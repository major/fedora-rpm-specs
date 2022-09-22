%bcond_without check

%global srcname pandas-datareader
%global summary Data readers from the pandas codebase

%global common_description                                                   \
Data readers extracted from the pandas codebase, should be compatible with   \
recent pandas versions.

Name: python-%{srcname}
Version: 0.10.0
Release: 4%{?dist}
Summary: %{summary}
License: BSD

URL: https://github.com/pydata/pandas-datareader
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
%{common_description}

%package -n python3-%{srcname}
Summary: %{summary}

%if %{with check}
BuildRequires: python3-pytest
BuildRequires: python3-numpy
BuildRequires: python3-pandas
BuildRequires: python3-requests
BuildRequires: python3-wrapt
%endif

#Requires: python3-requests-file
#Requires: python3-requests-ftp

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
# Most tests require network
%py3_check_import pandas_datareader pandas_datareader.av pandas_datareader.iex pandas_datareader.io
%py3_check_import pandas_datareader.yahoo
%endif

%files -n python3-%{srcname}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/pandas_datareader/ 
%{python3_sitelib}/pandas_datareader-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.10.0-1
- New upstream source (0.10.0)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.0-1
- New upstream source (0.9.0)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.0-1
- New upstream source (0.8.0)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-2
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.7.4-1
- New upstream source (0.7.4)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.0-4
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.0-1
- New upstream version (0.6.0)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-1
- New upstream version (0.5.0)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2.post0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-1.post0
- New upstream release (0.3.0.post0)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuild for Python 3.6

* Tue Oct 18 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.1-3
- Disable tests for the moment

* Mon Oct 17 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.1-2
- Improve spec for review

* Sun Oct 02 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.1-1
- Initial spec
