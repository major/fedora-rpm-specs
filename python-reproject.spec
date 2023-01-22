%global srcname reproject
%global sum Reproject astronomical images

Name:           python-%{srcname}
Version:        0.8
Release:        5%{?dist}
Summary:        %{sum}

License:        BSD and ASL 2.0 and Python
# Licensing breakdown
# In general: BSD, see licenses/LICENSE.rst
#
# Exceptions:
# Apache (2.0):
#    astropy_helpers/astropy_helpers/sphinx/themes/bootstrap-astropy/static/bootstrap-astropy.css
#
# PSF:
#    astropy_helpers/licenses/LICENSE_COPYBUTTON.rst
#    astropy_helpers/astropy_helpers/sphinx/themes/bootstrap-astropy/static/copybutton.js
#
URL:            https://reproject.readthedocs.io/
Source0:        %{pypi_source}

BuildRequires:  gcc

BuildRequires:  python3-astropy
BuildRequires:  python3-astropy-healpix
BuildRequires:  python3-astropy-helpers
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-extension-helpers
BuildRequires:  python3-pytest-astropy
BuildRequires:  python3-scipy
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%description
%{sum}.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-astropy
Requires:       python3-astropy-healpix

%description -n python3-%{srcname}
%{sum}.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%ifnarch s390x
pushd %{buildroot}/%{python3_sitearch}
py.test-%{python3_version} reproject
rm -rf .pytest_cache
popd
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGES.md README.rst
%{python3_sitearch}/*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 0.8-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Christian Dersch <lupinix@fedoraproject.org> - 0.8-1
- new version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul  4 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-5
- BR: python3-scipy for %%check

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Christian Dersch <lupinix@fedoraproject.org> - 0.7.1-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.5.1-2
- use un-cythonized sources

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.5.1-1
- new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.4-5
- drop python2 subpackage

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.4-4
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-2
- Rebuilt for Python 3.7

* Fri Mar 23 2018 Christian Dersch <lupinix@mailbox.org> - 0.4-1
- new version

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.3.2-3
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.2-1
- new version

* Thu Oct 12 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.1-7
- Recommend python-healpy

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuild for Python 3.6

* Fri Oct 07 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.1-2
- Added license breakdown

* Tue Oct 04 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.1-1
- Initial packaging

