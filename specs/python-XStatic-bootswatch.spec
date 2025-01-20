%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name XStatic-bootswatch

Name:           python-%{pypi_name}
Version:        3.3.7.0
Release:        28%{?dist}
Summary:        bootswatch (XStatic packaging standard)

License:        MIT
URL:            http://bootswatch.com
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/openstack/xstatic-bootswatch/master/LICENSE
BuildArch:      noarch

%description
Bootswatch javascript library packaged
for setuptools (easy_install) / pip.

Free themes for Bootstrap

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        bootswatch (XStatic packaging standard)
%{?python_provide:%python_provide python2-%{pypi_name}}
# python_provide does not exist in CentOS7 buildroot
Provides:       python-%{pypi_name} = %{version}-%{release}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python2-XStatic
Requires:       bootswatch-common = %{version}-%{release}
Requires:       bootswatch-fonts  = %{version}-%{release}

%description -n python2-%{pypi_name}
bootswatch javascript library packaged
for setuptools (easy_install) / pip.

Free themes for Bootstrap
%endif

%package -n bootswatch-common
Summary:    bootswatch (XStatic packaging standard) common files
BuildRequires:  web-assets-devel

Requires:       web-assets-filesystem

%description -n bootswatch-common
Common bootswatch static content (CSS and SCSS)

%package -n bootswatch-fonts
Summary:    bootswatch (XStatic packaging standard) fonts
BuildRequires:  fontpackages-filesystem

Requires:       fontpackages-filesystem

%description -n bootswatch-fonts
Bootswatch fonts

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        bootswatch (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       bootswatch-common = %{version}-%{release}
Requires:       bootswatch-fonts  = %{version}-%{release}

%description -n python3-%{pypi_name}
bootswatch javascript library packaged
for setuptools (easy_install) / pip.

Free themes for Bootstrap
%endif


%prep
%setup -q -n %{pypi_name}-%{version}

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/bootswatch'|" xstatic/pkg/bootswatch/__init__.py
# License file is present in GitHub repo, but not in PyPi file
cp %{SOURCE1} .


%build
%if %{with python2}
%{__python2} setup.py build
%endif

%if %{with python3}
%{__python3} setup.py build
%endif

%install
%if %{with python2}
%{__python2} setup.py install --skip-build --root %{buildroot}
# Move fonts to the right directory
mkdir -p %{buildroot}/%{_datadir}/fonts/bootswatch
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/bootswatch/data/fonts/* %{buildroot}/%{_datadir}/fonts/bootswatch
rmdir %{buildroot}/%{python2_sitelib}/xstatic/pkg/bootswatch/data/fonts

# Move static files
mkdir -p %{buildroot}/%{_jsdir}/bootswatch
for theme in cerulean cosmo cyborg darkly flatly journal lumen paper readable sandstone simplex slate spacelab superhero united yeti
do
 mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/bootswatch/data/${theme} %{buildroot}/%{_jsdir}/bootswatch
done
%endif


%if %{with python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Move fonts to the right directory
mkdir -p %{buildroot}/%{_datadir}/fonts/bootswatch
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/bootswatch/data/fonts/* %{buildroot}/%{_datadir}/fonts/bootswatch
rmdir %{buildroot}/%{python3_sitelib}/xstatic/pkg/bootswatch/data/fonts

# Move static files
mkdir -p %{buildroot}/%{_jsdir}/bootswatch
for theme in cerulean cosmo cyborg darkly flatly journal lumen paper readable sandstone simplex slate spacelab superhero united yeti
do
 mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/bootswatch/data/${theme} %{buildroot}/%{_jsdir}/bootswatch
done
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.txt
%license LICENSE
%{python2_sitelib}/xstatic/pkg/bootswatch
%{python2_sitelib}/XStatic_bootswatch-%{version}-py?.?.egg-info
%{python2_sitelib}/XStatic_bootswatch-%{version}-py?.?-nspkg.pth
%endif

%files -n bootswatch-common
%doc README.txt
%license LICENSE
%{_jsdir}/bootswatch

%files -n bootswatch-fonts
%doc README.txt
%license LICENSE
%{_datadir}/fonts/bootswatch

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.txt
%license LICENSE
%{python3_sitelib}/xstatic/pkg/bootswatch
%{python3_sitelib}/XStatic_bootswatch-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_bootswatch-%{version}-py%{python3_version}-nspkg.pth
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.7.0-26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.3.7.0-22
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.7.0-19
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.7.0-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.0-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Javier Peña <jpena@redhat.com> - 3.3.7.0-7
- Removed Python 2 package from Fedora 30+ (bz#1629755)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.3.7.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb  6 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 3.3.7.0-1
- Upstream 3.3.7.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.3.6.0-2
- Rebuild for Python 3.6

* Fri Aug 19 2016 jpena <jpena@redhat.com> - 3.3.6.0-1
- Updated to upstream version 3.3.6.0
- Added external license file, it is no longer bundled in source
- Fixed source URL

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 07 2015 jpena <jpena@redhat.com> - 3.3.5.3-2
- Added bootswatch-fonts subpackage.
- Shortened description.
* Fri Sep 04 2015 jpena <jpena@redhat.com> - 3.3.5.3-1
- Initial package.
