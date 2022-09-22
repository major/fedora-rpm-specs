%global module cornice_sphinx
%global desc Automatically generates Sphinx documentation for Cornice web services.

Name:             python-cornice-sphinx
Epoch:            1
Version:          0.3
Release:          20%{?dist}
BuildArch:        noarch

License:          ASL 2.0 and MPLv2.0
Summary:          Cornice extension to generate Sphinx docs
URL:              https://github.com/Cornices/cornice.ext.sphinx
Source0:          %{url}/archive/%{version}/%{module}-%{version}.tar.gz
# https://github.com/Cornices/cornice.ext.sphinx/pull/14
Patch0:           0000-Don-t-install-the-tests.patch
# Workaound https://github.com/sphinx-doc/sphinx/issues/6474
Patch1:           0001-Fix-compatibility-with-Sphinx-2.1.patch


BuildRequires: %{py3_dist cornice} >= 3
BuildRequires: %{py3_dist docutils nose setuptools sphinx mock}
BuildRequires: python3-devel


%description
%{desc}


%package -n python3-cornice-sphinx
Summary:          %{summary}

Requires: %{py3_dist cornice} >= 3
Requires: %{py3_dist docutils sphinx}

%{?python_provide:%python_provide python3-cornice-sphinx}


%description -n python3-cornice-sphinx
%{desc}


%prep
%autosetup -p1 -n cornice.ext.sphinx-%{version}


%build
%py3_build


%install
%py3_install


%check
# https://github.com/Cornices/cornice.ext.sphinx/issues/19
PYTHONPATH="." nosetests-3 --exclude test_string_validator_resolved


%files -n python3-cornice-sphinx
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1:0.3-19
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:0.3-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.3-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.3-10
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1:0.3-9
- Add patch to work around https://github.com/sphinx-doc/sphinx/issues/6474

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.3-7
- Subpackage python2-cornice-sphinx has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.3-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3-3
- Raise the epoch to 1.

* Thu Dec 21 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3-2
- Use fancy new py2_dist and py3_dist macros.

* Wed Dec 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3-1
- Initial release (#1528008).
