%global pypi_name XStatic-Font-Awesome

Name:           python-%{pypi_name}
Version:        4.7.0.0
Release:        20%{?dist}
Summary:        Font-Awesome (XStatic packaging standard)

# font awesome is licensed under SIL 1.1.
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses_4
# short name: OFL
# Code is distributed under MIT
License:        OFL and MIT
URL:            https://fortawesome.github.io/Font-Awesome/
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  web-assets-devel
BuildRequires:  fontawesome-fonts-web >= 4.1.0
BuildRequires:  fontawesome-fonts

%description
Font Awesome icons packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.


%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       web-assets-filesystem
Requires:       fontawesome-fonts-web >= 4.1.0
Requires:       fontawesome-fonts

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Font Awesome icons packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install

# use fontawesome-fonts directly
rm -f %{buildroot}/%{python3_sitelib}/xstatic/pkg/font_awesome/data/fonts/*
ln -s %{_datadir}/fonts/fontawesome/*  %{buildroot}/%{python3_sitelib}/xstatic/pkg/font_awesome/data/fonts/

# use fontawesome-fonts-web for css, scss,
for dir in css less scss ; do
rm -rf %{buildroot}/%{python3_sitelib}/xstatic/pkg/font_awesome/data/$dir
ln -s %{_datadir}/font-awesome-web/$dir %{buildroot}/%{python3_sitelib}/xstatic/pkg/font_awesome/data/$dir
done


%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/font_awesome
%{python3_sitelib}/XStatic_Font_Awesome-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_Font_Awesome-%{version}-py%{python3_version}-nspkg.pth


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.7.0.0-18
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.7.0.0-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.0.0-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.7.0.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.7.0.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 4.7.0.0-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Sep 28 2018 Alfredo Moralejo <amoralej@redhat.com> - 4.7.0.0-6
- Requirements moved to python2 and python3 subpackages instead of empty python- one.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.7.0.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb  6 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 4.7.0.0-1
- Upstream 4.7.0.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.3.0.0-5
- Rebuild for Python 3.6

* Thu Oct 13 2016 Jan Beran <jberan@redhat.com> - 4.3.0.0-4
- Provides a Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Matthias Runge <mrunge@redhat.com> - 4.3.0-1
- update to 4.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Matthias Runge <mrunge@redhat.com> - 4.1.0.0-4
- add br fontawesome-fonts-web to catch .woff (rhbz#1218627)

* Fri Dec 05 2014 Matthias Runge <mrunge@redhat.com> - 4.1.0.0-3
- version bumped due to adding .woff and .svg to fontawesome-fonts

* Wed Oct 01 2014 Matthias Runge <mrunge@redhat.com> - 4.1.0.0-2
- require at least version 4.1.0 of fontawesome-fonts-web

* Wed Sep 10 2014 Matthias Runge <mrunge@redhat.com> - 4.1.0.0-1
- Initial package. (rhbz#1140377)

