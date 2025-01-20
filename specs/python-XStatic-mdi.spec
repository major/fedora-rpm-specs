%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name XStatic-mdi

Name:           python-%{pypi_name}
Version:        1.6.50.2
Release:        18%{?dist}
Summary:        mdi (XStatic packaging standard)

# mdi is licensed under SIL 1.1.
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses_4
# short name: OFL

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://materialdesignicons.com
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/openstack/xstatic-mdi/master/LICENSE
BuildArch:      noarch
 
%description
mdi javascript library packaged for setuptools
(easy_install) / pip.

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        mdi (XStatic packaging standard)
%{?python_provide:%python_provide python2-%{pypi_name}}
# python_provide does not exist in CentOS7 buildroot
Provides:       python-%{pypi_name} = %{version}-%{release}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires: python2-XStatic  
Requires: mdi-common = %{version}-%{release}
Requires: mdi-fonts  = %{version}-%{release}

%description -n python2-%{pypi_name}
mdi javascript library packaged for setuptools
(easy_install) / pip.
%endif

%package -n mdi-common
Summary:        mdi (XStatic packaging standard) common files
BuildRequires:  web-assets-devel

Requires: web-assets-filesystem

%description -n mdi-common
Common mdi static content (CSS and SCSS)

%package -n mdi-fonts
Summary:        mdi (XStatic packaging standard) fonts
BuildRequires:  fontpackages-filesystem

Requires: fontpackages-filesystem

%description -n mdi-fonts
mdi fonts

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        mdi (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires: python3-XStatic
Requires: mdi-common = %{version}-%{release}
Requires: mdi-fonts  = %{version}-%{release}

%description -n python3-%{pypi_name}
mdi javascript library packaged for setuptools
(easy_install) / pip.

%endif

%prep
%setup -q -n %{pypi_name}-%{version}

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/mdi'|" xstatic/pkg/mdi/__init__.py
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
mkdir -p %{buildroot}/%{_datadir}/fonts/mdi
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/mdi/data/fonts/* %{buildroot}/%{_datadir}/fonts/mdi
rmdir %{buildroot}/%{python2_sitelib}/xstatic/pkg/mdi/data/fonts
# Move static files
mkdir -p %{buildroot}/%{_jsdir}/mdi
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/mdi/data/css %{buildroot}/%{_jsdir}/mdi
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/mdi/data/scss %{buildroot}/%{_jsdir}/mdi
# link fonts
mkdir %{buildroot}/%{_jsdir}/mdi/fonts
pushd %{buildroot}/%{_jsdir}/mdi/fonts
ln -s ../../../fonts/mdi/materialdesignicons-* .
popd
%endif

%if %{with python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Move fonts to the right directory
mkdir -p %{buildroot}/%{_datadir}/fonts/mdi
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/mdi/data/fonts/* %{buildroot}/%{_datadir}/fonts/mdi
rmdir %{buildroot}/%{python3_sitelib}/xstatic/pkg/mdi/data/fonts
# Move static files
mkdir -p %{buildroot}/%{_jsdir}/mdi
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/mdi/data/css %{buildroot}/%{_jsdir}/mdi
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/mdi/data/scss %{buildroot}/%{_jsdir}/mdi
# link fonts
mkdir %{buildroot}/%{_jsdir}/mdi/fonts
pushd %{buildroot}/%{_jsdir}/mdi/fonts
ln -s ../../../fonts/mdi/materialdesignicons-* .
popd

%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.txt 
%license LICENSE
%{python2_sitelib}/xstatic/pkg/mdi
%{python2_sitelib}/XStatic_mdi-%{version}-py?.?.egg-info
%{python2_sitelib}/XStatic_mdi-%{version}-py?.?-nspkg.pth
%endif

%files -n mdi-common
%license LICENSE
%{_jsdir}/mdi

%files -n mdi-fonts
%license LICENSE
%{_datadir}/fonts/mdi

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.txt 
%license LICENSE
%{python3_sitelib}/xstatic/pkg/mdi
%{python3_sitelib}/XStatic_mdi-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_mdi-%{version}-py%{python3_version}-nspkg.pth
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.50.2-17
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.50.2-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.50.2-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.50.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.50.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.50.2-2
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Radomir Dopieralski <rdopiera@redhat.com> - 1.6.50.2-1
- Update to 1.6.50.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.57.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.57.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.57.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.57.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.57.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Javier Peña <jpena@redhat.com> - 1.4.57.0-9
- Removed Python 2 package from Fedora 30+ (bz#1627370)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.57.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.57.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.57.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.57.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.57.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.57.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.57.0-2
- Rebuild for Python 3.6

* Fri Aug 19 2016 Javier Peña <jpena@redhat.com> - 1.4.57.0-1
- Updated to upstream version 1.4.57.0
- Updated source URL
- License file is no longer included in source

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.70.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 12 2016 Matthias Runge <mrunge@redhat.com> - 1.1.70.1-5
- also link fonts (rhbz#1333600)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.70.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.70.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 04 2015 jpena <jpena@redhat.com> - 1.1.70.1-2
- Created fonts subpackage.
* Fri Sep 04 2015 jpena <jpena@redhat.com> - 1.1.70.1-1
- Initial package.
