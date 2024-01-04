%global srcname astropy-healpix
%global modname astropy_healpix
%global sum HEALPix for Astropy

Name:           python-%{srcname}
Version:        1.0.2
Release:        1%{?dist}
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source astropy_healpix}
# https://github.com/astropy/astropy-healpix/issues/183
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1026012
# https://salsa.debian.org/debian-astro-team/astropy-healpix/-/blob/master/debian/patches/Temporarily-disable-tests-that-fail-due-to-limited-FP-pre.patch
Patch0:         astropy_healpix-0.7-disable-FP-limited-test.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
#
BuildRequires:  %{py3_dist pytest-astropy}
# BuildRequires for tests, healpy only available on 64 bit architectures,
# thus these tests are skipped on 32 bit
%ifnarch %{ix86} %{arm}
BuildRequires:  %{py3_dist healpy}
%endif

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

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
pushd %{buildroot}/%{python3_sitearch}
  %pytest %{modname}
  # Hypothesis tests creates some files in sitearch... we remove them now
  rm -rf .hypothesis
  rm -rf .pytest_cache
popd

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.md
%doc README.rst

%changelog
* Tue Jan 02 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sun Sep 17 2023 Mattia Verga <mattia.verga@proton.me> - 1.0.0-1
- Update to 1.0.0 (fedora#2233129)
- Migrate license to SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7-4
- Disable tests related to FP limitation (upstream github bug 183)

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

