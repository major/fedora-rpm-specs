%global srcname astropy-healpix
%global modname astropy_healpix
%global sum HEALPix for Astropy

Name:           python-%{srcname}
Version:        0.7
Release:        3%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source astropy_healpix}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  %{py3_dist astropy}
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist extension-helpers}
# BuildRequires for tests, healpy only available on 64 bit architectures,
# thus these tests are skipped on 32 bit
%ifnarch %{ix86} %{arm}
BuildRequires:  %{py3_dist healpy}
%endif
BuildRequires:  %{py3_dist hypothesis}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist pytest-astropy}

%description
This is a BSD-licensed Python package for HEALPix, which is based on the C
HEALPix code written by Dustin Lang originally in astrometry.net, and was
added here with a Cython wrapper and expanded with a Python interface.


%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
%{description}


%prep
%autosetup -n %{modname}-%{version} -p1

# Remove egg files from source
rm -r %{modname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%ifnarch s390x
pushd %{buildroot}/%{python3_sitearch}
%pytest %{modname}
popd
# Hypothesis tests creates some files in sitearch... we remove them now
rm -rf %{buildroot}%{python3_sitearch}/.hypothesis
rm -rf %{buildroot}%{python3_sitearch}/.pytest_cache
%endif

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{srcname}
%license LICENSE.md
%doc README.rst
%{python3_sitearch}/%{modname}
%{python3_sitearch}/%{modname}*egg-info

%changelog
* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 0.7-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Christian Dersch <lupinix@mailbox.org> - 0.7-1
- Update to 0.7

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.6-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-2
- Rebuilt for Python 3.10

* Sat May 01 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.6-1
- Upgrade to 0.6
- Fixes rhbz#1937438

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Christian Dersch <lupinix@fedoraproject.org> - 0.5-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.4-5
- Disable tests on s90x until numpy is fixed

* Fri Sep 13 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4-4
- Patch for astropy.tests.pytest_plugins error (bug 1743897)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.4-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.3.1-1
- new version

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.2.1-1
- new version

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.2-6
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Christian Dersch <lupinix@mailbox.org> - 0.2-4
- Use PyPI tar and delete the Cythonized code

* Sat Jun 30 2018 Christian Dersch <lupinix@mailbox.org> - 0.2-3
- Use GitHub tar instead of PyPI one (as GitHub one is not Cythonized)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2-2
- Rebuilt for Python 3.7

* Sat Mar 17 2018 Christian Dersch <lupinix@mailbox.org> - 0.2-1
- initial package

