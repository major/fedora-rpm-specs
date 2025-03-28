# When bootstrapping Python, we cannot test this yet
# RHEL does not include the test dependencies
%bcond tests    %{undefined rhel}
# The extras are disabled on RHEL to avoid pysocks and deprecated requests[security]
%bcond extras    %[%{undefined rhel} || %{defined eln}]
%bcond extradeps %{undefined rhel}

Name:           python-requests
Version:        2.32.3
Release:        4%{?dist}
Summary:        HTTP library, written in Python, for human beings

License:        Apache-2.0
URL:            https://pypi.io/project/requests
Source:         https://github.com/requests/requests/archive/v%{version}/requests-v%{version}.tar.gz

# Explicitly use the system certificates in ca-certificates.
# https://bugzilla.redhat.com/show_bug.cgi?id=904614
Patch:          system-certs.patch

# Add support for IPv6 CIDR in no_proxy setting
# This functionality is needed in Openshift and it has been
# proposed for upstream in 2021 but the PR unfortunately stalled.
# Upstream PR: https://github.com/psf/requests/pull/5953
# This change is backported also into RHEL 9.4 (via CS)
Patch:          support_IPv6_CIDR_in_no_proxy.patch

# Fix crash on import if /etc/pki/tls/certs/ca-bundle.crt is missing
# https://bugzilla.redhat.com/show_bug.cgi?id=2297632
# https://github.com/psf/requests/pull/6781
# Note: this can be replaced by https://github.com/psf/requests/pull/6767
# when it is ready, or dropped in a release where that is merged
Patch:          0001-Don-t-create-default-SSLContext-if-CA-bundle-isn-t-p.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-httpbin)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(trustme)
%endif

%description
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.


%package -n python%{python3_pkgversion}-requests
Summary:        %{summary}

%description -n python%{python3_pkgversion}-requests
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.


%if %{with extras}
%pyproject_extras_subpkg -n python%{python3_pkgversion}-requests security socks
%endif


%generate_buildrequires
%pyproject_buildrequires %{?with_extradeps:-x security,socks}


%prep
%autosetup -p1 -n requests-%{version}

# env shebang in nonexecutable file
sed -i '/#!\/usr\/.*python/d' src/requests/certs.py

# Some doctests use the internet and fail to pass in Koji. Since doctests don't have names, I don't
# know a way to skip them. We also don't want to patch them out, because patching them out will
# change the docs. Thus, we set pytest not to run doctests at all.
sed -i 's/ --doctest-modules//' pyproject.toml


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files requests


%check
%pyproject_check_import
%if %{with tests}
# test_unicode_header_name - reported: https://github.com/psf/requests/issues/6734
# test_use_proxy_from_environment needs pysocks
%pytest -v tests -k "not test_unicode_header_name %{!?with_extradeps:and not test_use_proxy_from_environment}"
%endif


%files -n python%{python3_pkgversion}-requests -f %{pyproject_files}
%license LICENSE
%doc README.md HISTORY.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 01 2024 Adam Williamson <awilliam@redhat.com> - 2.32.3-3
- Backport PR #6781 to fix crash on import if CA cert bundle is missing (#2297632)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Lumír Balhar <lbalhar@redhat.com> - 2.32.3-1
- Update to 2.32.3 (rhbz#2281881)
- Fix for CVE-2024-35195 (rhbz#2282205)

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.31.0-7
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.31.0-6
- Bootstrap for Python 3.13

* Tue May 14 2024 Lumír Balhar <lbalhar@redhat.com> - 2.31.0-5
- Add support for IPv6 CIDR in no_proxy setting
- Fix FTBFS

* Thu Apr 11 2024 Lumír Balhar <lbalhar@redhat.com> - 2.31.0-4
- Fix compatibility with pytest 8

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 16 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 2.31.0-1
- Update to 2.31.0
- Fixes: rhbz#2189970

* Tue Oct 10 2023 Miro Hrončok <mhroncok@redhat.com> - 2.28.2-7
- Do not package requests[security] and requests[socks] on RHEL
- Make the package build even when urllib3 won't pull in pysocks

* Tue Aug 08 2023 Karolina Surma <ksurma@redhat.com> - 2.28.2-6
- Declare the license as an SPDX expression

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 2.28.2-4
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.28.2-3
- Bootstrap for Python 3.12

* Tue May 23 2023 Miro Hrončok <mhroncok@redhat.com> - 2.28.2-2
- Security fix for CVE-2023-32681
- https://github.com/psf/requests/security/advisories/GHSA-j8r2-6x86-q33q

* Wed Feb 01 2023 Lumír Balhar <lbalhar@redhat.com> - 2.28.2-1
- Update to 2.28.2 (rhbz#2160527)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Kevin Fenzi <kevin@scrye.com> - 2.28.1-3
- Enable all tests and drop no longer needed test patch.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Adam Williamson <awilliam@redhat.com> - 2.28.1-1
- Update to 2.28.1, rediff patches

* Mon Jun 20 2022 Lumír Balhar <lbalhar@redhat.com> - 2.27.1-5
- Allow charset_normalizer 2.1.0 and newer up to 3.0.0

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.27.1-4
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.27.1-3
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Kevin Fenzi <kevin@scrye.com> - 2.27.1-1
- Update to 2.27.1. Fixes rhbz#2037431

* Tue Jan 04 2022 Adam Williamson <awilliam@redhat.com> - 2.27.0-1
- Update to 2.27.0
- Re-enable test_https_warnings as it works with pytest-httpbin 1.0.0 now
- Re-enable test_pyopenssl_redirect, it seems to work too

* Sun Jul 25 2021 Lumír Balhar <lbalhar@redhat.com> - 2.26.0-1
- Update to 2.26.0
Resolves: rhbz#1981856

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.25.1-3
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 2.25.1-2
- Bootstrap for Python 3.10

* Tue Feb 02 2021 Kevin Fenzi <kevin@scrye.com> - 2.25.1-1
- Update 2.25.1. Fix is rhbz#1908487

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Petr Viktorin <pviktori@redhat.com> - 2.25.0-1
- Update to 2.25.0

* Fri Nov 13 2020 Miro Hrončok <mhroncok@redhat.com> - 2.24.0-5
- Don't BR pytest-cov

* Fri Sep 18 2020 Petr Viktorin <pviktori@redhat.com> - 2.24.0-4
- Port to pyproject macros

* Fri Sep 18 2020 Miro Hrončok <mhroncok@redhat.com> - 2.24.0-3
- Build with pytest 6, older version is no longer required

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 2.24.0-1
- Update to 2.24.0
- Resolves rhbz#1848104

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 2.23.0-5
- Add requests[security] and requests[socks] subpackages

* Sat May 30 2020 Miro Hrončok <mhroncok@redhat.com> - 2.23.0-4
- Test with pytest 4, drop manual requires

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 2.23.0-3
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 2.23.0-2
- Bootstrap for Python 3.9

* Fri Feb 21 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.23.0-1
- Update to 2.23.0 (#1804863).
- https://requests.readthedocs.io/en/latest/community/updates/

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Charalampos Stratakis <cstratak@redhat.com> - 2.22.0-7
- Remove the python2 subpackage (rhbz#1761787)

* Wed Sep 18 2019 Petr Viktorin <pviktori@redhat.com> - 2.22.0-6
- Python 2: Remove tests and test dependencies

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.22.0-5
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.22.0-4
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Yatin Karel <ykarel@redhat.com> - 2.22.0-2
- Add minimum requirement for chardet and urllib3

* Thu May 23 2019 Jeremy Cline <jcline@redhat.com> - 2.22.0-1
- Update to v2.22.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Jeremy Cline <jeremy@jcline.org> - 2.21.0-1
- Update to v2.21.0
- Don't rely on certifi being patched properly to use the system CA bundle

* Mon Nov 26 2018 Miro Hrončok <mhroncok@redhat.com> - 2.20.0-2
- No pytest-httpbin for Python 2

* Mon Oct 29 2018 Jeremy Cline <jeremy@jcline.org> - 2.20.0-1
- Update to v2.20.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.19.1-2
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Jeremy Cline <jeremy@jcline.org> - 2.19.1-1
- Update to v2.19.1 (rhbz 1591531)

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 2.19.0-2
- Bootstrap for Python 3.7

* Tue Jun 12 2018 Jeremy Cline <jeremy@jcline.org> - 2.19.0-1
- Update to v2.19.0 (rhbz 1590508)

* Fri Jun 08 2018 Jeremy Cline <jeremy@jcline.org> - 2.18.4-6
- Don't print runtime warning about urllib3 v1.23 (rhbz 1589306)

* Tue Jun 05 2018 Jeremy Cline <jeremy@jcline.org> - 2.18.4-5
- Allow urllib3 v1.23 (rhbz 1586311)

* Mon Apr 16 2018 Jeremy Cline <jeremy@jcline.org> - 2.18.4-4
- Stop injecting PyOpenSSL (rhbz 1567862)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.18.4-2
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Aug 18 2017 Jeremy Cline <jeremy@jcline.org> - 2.18.4-1
- Update to 2.18.4

* Wed Jul 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.18.2-1
- Update to 2.18.2

* Tue Jun 20 2017 Jeremy Cline <jeremy@jcline.org> - 2.18.1-2
- Drop the dependency on certifi in setup.py

* Mon Jun 19 2017 Jeremy Cline <jeremy@jcline.org> - 2.18.1-1
- Update to 2.18.1 (#1449432)
- Remove tests that require non-local network (#1450608)

* Wed May 17 2017 Jeremy Cline <jeremy@jcline.org> - 2.14.2-1
- Update to 2.14.2 (#1449432)
- Switch to autosetup to apply patches

* Sun May 14 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.13.0-2
- Don't run tests when building as a module

* Thu Feb 09 2017 Jeremy Cline <jeremy@jcline.org> - 2.13.0-1
- Update to 2.13.0 (#1418138)

* Fri Dec 30 2016 Adam Williamson <awilliam@redhat.com> - 2.12.4-3
- Include and enable tests (now python-pytest-httpbin is packaged)

* Wed Dec 21 2016 Kevin Fenzi <kevin@scrye.com> - 2.12.4-2
- Rebuild for Python 3.6 again.

* Tue Dec 20 2016 Jeremy Cline <jeremy@jcline.org> - 2.12.4-1
- Update to 2.12.4. Fixes #1404680

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 2.12.3-2
- Rebuild for Python 3.6

* Thu Dec 01 2016 Jeremy Cline <jeremy@jcline.org> - 2.12.3-1
- Update to 2.12.3. Fixes #1400601

* Wed Nov 30 2016 Jeremy Cline <jeremy@jcline.org> - 2.12.2-1
- Update to 2.12.2

* Wed Nov 23 2016 Jeremy Cline <jeremy@jcline.org> - 2.12.1-2
- Backport #3713. Fixes #1397149

* Thu Nov 17 2016 Jeremy Cline <jeremy@jcline.org> - 2.12.1-1
- Update to 2.12.1. Fixes #1395469
- Unbundle idna, a new upstream dependency

* Sat Aug 27 2016 Kevin Fenzi <kevin@scrye.com> - 2.11.1-1
- Update to 2.11.1. Fixes #1370814

* Wed Aug 10 2016 Kevin Fenzi <kevin@scrye.com> - 2.11.0-1
- Update to 2.11.0. Fixes #1365332

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Ralph Bean <rbean@redhat.com> - 2.10.0-3
- Update python2 packaging.

* Thu Jun 02 2016 Ralph Bean <rbean@redhat.com> - 2.10.0-2
- Fix python2 subpackage to comply with guidelines.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Ralph Bean <rbean@redhat.com> - 2.9.1-1
- new version

* Fri Dec 18 2015 Ralph Bean <rbean@redhat.com> - 2.9.0-1
- new version

* Mon Dec 14 2015 Ralph Bean <rbean@redhat.com> - 2.8.1-1
- Latest upstream.
- Bump hard dep on urllib3 to 1.12.

* Mon Nov 02 2015 Robert Kuska <rkuska@redhat.com> - 2.7.0-8
- Rebuilt for Python3.5 rebuild

* Sat Oct 10 2015 Ralph Bean <rbean@redhat.com> - 2.7.0-7
- Tell setuptools about what version of urllib3 we're unbundling
  for https://github.com/kennethreitz/requests/issues/2816

* Thu Sep 17 2015 Ralph Bean <rbean@redhat.com> - 2.7.0-6
- Replace the provides macro with a plain provides field for now until we can
  re-organize this package into two different subpackages.

* Thu Sep 17 2015 Ralph Bean <rbean@redhat.com> - 2.7.0-5
- Remove 'provides: python2-requests' from the python3 subpackage, obviously.

* Tue Sep 15 2015 Ralph Bean <rbean@redhat.com> - 2.7.0-4
- Employ %%python_provides macro to provide python2-requests.

* Fri Sep 04 2015 Ralph Bean <rbean@redhat.com> - 2.7.0-3
- Lock down the python-urllib3 version to the specific version we unbundled.
  https://bugzilla.redhat.com/show_bug.cgi?id=1253823

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Ralph Bean <rbean@redhat.com> - 2.7.0-1
- new version

* Wed Apr 29 2015 Ralph Bean <rbean@redhat.com> - 2.6.2-1
- new version

* Thu Apr 23 2015 Ralph Bean <rbean@redhat.com> - 2.6.1-1
- new version

* Wed Apr 22 2015 Ralph Bean <rbean@redhat.com> - 2.6.0-1
- new version
- Remove patch for CVE-2015-2296, now included in the upstream release.

* Mon Mar 16 2015 Ralph Bean <rbean@redhat.com> - 2.5.3-2
- Backport fix for CVE-2015-2296.

* Thu Feb 26 2015 Ralph Bean <rbean@redhat.com> - 2.5.3-1
- new version

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 2.5.1-1
- new version

* Tue Dec 16 2014 Ralph Bean <rbean@redhat.com> - 2.5.0-3
- Pin python-urllib3 requirement at 1.10.
- Fix requirement pinning syntax.

* Thu Dec 11 2014 Ralph Bean <rbean@redhat.com> - 2.5.0-2
- Do the most basic of tests in the check section.

* Thu Dec 11 2014 Ralph Bean <rbean@redhat.com> - 2.5.0-1
- Latest upstream, 2.5.0 for #1171068

* Wed Nov 05 2014 Ralph Bean <rbean@redhat.com> - 2.4.3-1
- Latest upstream, 2.4.3 for #1136283

* Wed Nov 05 2014 Ralph Bean <rbean@redhat.com> - 2.3.0-4
- Re-do unbundling by symlinking system libs into the requests/packages/ dir.

* Sun Aug  3 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.0-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Arun S A G <sagarun@gmail.com> - 2.3.0-1
- Latest upstream

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Sep 25 2013 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Latest upstream.
- Add doc macro to the python3 files section.
- Require python-urllib3 greater than or at 1.7.1.

* Mon Aug 26 2013 Rex Dieter <rdieter@fedoraproject.org> 1.2.3-5
- fix versioned dep on python-urllib3

* Mon Aug 26 2013 Ralph Bean <rbean@redhat.com> - 1.2.3-4
- Explicitly versioned the requirements on python-urllib3.

* Thu Aug 22 2013 Ralph Bean <rbean@redhat.com> - 1.2.3-3
- Release bump for a coupled update with python-urllib3.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 01 2013 Ralph Bean <rbean@redhat.com> - 1.2.3-1
- Latest upstream.
- Fixed bogus date in changelog.

* Tue Jun 11 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-4
- Correct a rhel conditional on python-ordereddict

* Thu Feb 28 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-3
- Unbundled python-urllib3.  Using system python-urllib3 now.
- Conditionally include python-ordereddict for el6.

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Unbundled python-charade/chardet.  Using system python-chardet now.
- Removed deprecated comments and actions against oauthlib unbundling.
  Those are no longer necessary in 1.1.0.
- Added links to bz tickets over Patch declarations.

* Tue Feb 26 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- Latest upstream.
- Relicense to ASL 2.0 with upstream.
- Removed cookie handling patch (fixed in upstream tarball).
- Updated cert unbundling patch to match upstream.
- Added check section, but left it commented out for koji.

* Fri Feb  8 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.14.1-4
- Let brp_python_bytecompile run again, take care of the non-python{2,3} modules
  by removing them from the python{,3}-requests package that they did not belong
  in.
- Use the certificates in the ca-certificates package instead of the bundled one
  + https://bugzilla.redhat.com/show_bug.cgi?id=904614
- Fix a problem with cookie handling
  + https://bugzilla.redhat.com/show_bug.cgi?id=906924

* Mon Oct 22 2012 Arun S A G <sagarun@gmail.com>  0.14.1-1
- Updated to latest upstream release

* Sun Jun 10 2012 Arun S A G <sagarun@gmail.com> 0.13.1-1
- Updated to latest upstream release 0.13.1
- Use system provided ca-certificates
- No more async requests use grrequests https://github.com/kennethreitz/grequests
- Remove gevent as it is no longer required by requests

* Sun Apr 01 2012 Arun S A G <sagarun@gmail.com> 0.11.1-1
- Updated to upstream release 0.11.1

* Thu Mar 29 2012 Arun S A G <sagarun@gmail.com> 0.10.6-3
- Support building package for EL6

* Tue Mar 27 2012 Rex Dieter <rdieter@fedoraproject.org> 0.10.6-2
- +python3-requests pkg

* Sat Mar 3 2012 Arun SAG <sagarun@gmail.com> - 0.10.6-1
- Updated to new upstream version

* Sat Jan 21 2012 Arun SAG <sagarun@gmail.com> - 0.9.3-1
- Updated to new upstream version 0.9.3
- Include python-gevent as a dependency for requests.async
- Clean up shebangs in requests/setup.py,test_requests.py and test_requests_ext.py

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Arun SAG <sagarun@gmail.com> - 0.8.2-1
- New upstream version
- keep alive support
- complete removal of cookiejar and urllib2

* Thu Nov 10 2011 Arun SAG <sagarun@gmail.com> - 0.7.6-1
- Updated to new upstream release 0.7.6

* Thu Oct 20 2011 Arun SAG <sagarun@gmail.com> - 0.6.6-1
- Updated to version 0.6.6

* Fri Aug 26 2011 Arun SAG <sagarun@gmail.com> - 0.6.1-1
- Updated to version 0.6.1

* Sat Aug 20 2011 Arun SAG <sagarun@gmail.com> - 0.6.0-1
- Updated to latest version 0.6.0

* Mon Aug 15 2011 Arun SAG <sagarun@gmail.com> - 0.5.1-2
- Remove OPT_FLAGS from build section since it is a noarch package
- Fix use of mixed tabs and space
- Remove extra space around the word cumbersome in description

* Sun Aug 14 2011 Arun SAG <sagarun@gmail.com> - 0.5.1-1
- Initial package
