%global         srcname  acme

%global         SPHINXBUILD sphinx-build-3
%bcond_without  docs


Name:           python-acme
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python library for the ACME protocol
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/acme
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
Source2:        https://dl.eff.org/certbot.pub
# EPEL 9 does not have some of the test-only requirements right now (2022-04).
# pytest-xdist and typing-extensions are also not that useful for distro-level
# testing anyway so removing these is probably the easiest way forward.
Patch1:         python-acme-test-buildrequires.patch

%if %{with docs}
BuildRequires: make
%endif

BuildRequires:  python3-devel

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

BuildArch:      noarch

%description
Python libraries implementing the Automatic Certificate Management Environment
(ACME) protocol. It is used by the Let's Encrypt project.

%package -n python3-acme
#Recommends: python-acme-doc
Summary:        %{summary}
%{?python_provide:%python_provide python3-acme}

%description -n python3-acme
Python 3 library for use of the Automatic Certificate Management Environment
protocol as defined by the IETF. It's used by the Let's Encrypt project.

%if %{with docs}
%package doc
# CSS uses @font-face … src:local("fontawesome/FontAwesome") format("truetype")
Requires: fontawesome-fonts
Summary:  Documentation for python-acme libraries

%description doc
Documentation for the ACME python libraries
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x docs,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with docs}
# man page is pretty useless but api pages are decent
# Issue opened upstream for improving man page
# Need to cd as parent makefile tries to build libraries
(  cd docs && make html SPHINXBUILD=%{SPHINXBUILD} )
# Clean up stuff we don't need for docs
rm -rf docs/_build/html/{.buildinfo,man,_sources}
%endif
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest -v

%files -n python3-acme -f %{pyproject_files}
# LICENSE.txt already declared via %%{pyproject_files}
%doc README.rst

%if 0%{?with_docs}
%files doc
%license LICENSE.txt
%doc README.rst
%doc docs/_build/html
%endif

%changelog
* Wed Dec 07 2022 Nick Bebout <nb@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Nov 09 2022 Nick Bebout <nb@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.30.0-1
- Update to 1.30.0 rhbz#2125043

* Tue Aug 09 2022 Jonathan Wright <jonathan@almalinux.org> - 1.29.0-2
- Increment version for new side tag build

* Tue Aug 09 2022 Jonathan Wright <jonathan@almalinux.org> - 1.29.0-1
- Update to 1.29.0 (#2094618)
- Update license to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.27.0-2
- Rebuilt for Python 3.11

* Wed May 04 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.27.0-1
- Update to 1.27.0 (#2081542)

* Thu Apr 07 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0 (#2064937)

* Mon Mar 14 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0 (#2052121)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.22.0-1
- Update to 1.22.0 (#2020089)

* Tue Oct 05 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0 (#2010929)

* Fri Sep 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0 (#2002035)

* Wed Aug 04 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0 (#1957419)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14.0-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0 (#1946825)

* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0 (#1934816)

* Tue Feb 2 2021 Nick Bebout <nb@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.11.0-1
- update to 1.11.0 (#1913050)

* Fri Dec 25 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.1-2
- "docs" subpackage only requires fontawesome-fonts now

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1

* Wed Dec 02 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#1903306)

* Wed Oct 07 2020 Nick Bebout <nb@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Tue Oct 06 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Aug 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#1866070)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1854594)

* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843199)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9
- EPEL 8: disable failing test case (rhbz #1834530)

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831912)

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809794)

* Fri Feb 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (#1791073)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.1.0-1
- Update to 1.1.0

* Thu Dec 05 2019 Felix Schwarz <fschwarz@fedoraproject.org> 1.0.0-2
- adapt conditions for EPEL8
- remove runtime dependency on mock

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769084)

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757606)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748611)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742576)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Sun Jun 30 2019 Miro Hrončok <mhroncok@redhat.com> - 0.35.1-2
- Rebuilt to update automatic Python dependencies

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717675)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686201)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673768)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669312)

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1625793)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600290)

* Thu Jul 12 2018 Eli Young <elyscape@gmail.com> - 0.26.0-1
- Update to 0.26.0 (#1600290)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591030)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588214)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574138)
- Remove unnecessary build dependencies and patches

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563878)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2 (#1558275)

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0 (#1552951)

* Thu Mar 08 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.21.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.1-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Update to 0.21.1 (#1535990)

* Wed Dec 20 2017 Eli Young <elyscape@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Fri Oct 06 2017 Eli Young <elyscape@gmail.com> - 0.19.0-1
- Update to 0.19.0 (bz#1499366)

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2

* Mon Sep 18 2017 Eli Young <elyscape@gmail.com> - 0.18.1-2
- Disable doc package entirely for EPEL7

* Mon Sep 18 2017 Eli Young <elyscape@gmail.com> - 0.18.1-1
- Disable doc generation for EPEL7

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Fri May 12 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.0-1
- Update to 0.14.0

* Wed Apr 19 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-1
- Update to 0.13.0

* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-3
- upstream request not to use py3 yet so switch jws to py2
- include a py3 option for testing

* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-2
- Build for python rpm macro change

* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-1
- Update to 0.12.0
- Change %%{_bindir}/jws to be python3 on Fedora

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-1
- Upgrade to 0.11.1

* Thu Jan 05 2017 Adam Williamson <awilliam@redhat.com> - 0.9.3-2
- Backport upstream fix for tests with OpenSSL 1.1
- Backport upstream removal of sphinxcontrib-programoutput usage
- Re-enable doc generation

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6
- Removing the docs subpackage for now until the dependency works in rawhide

* Fri Oct 14 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.3-1
- Upgrade to 0.9.3
* Thu Oct 13 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.2-1
- Upgrade to 0.9.2
* Fri Oct 07 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.1-1
- Upgrade to 0.9.1
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Wed Jun 15 2016 Nick Bebout <nb@fedoraproject.org> - 0.8.1-1
- Upgrade to 0.8.1
* Fri Jun 03 2016 James Hogarth <james.hogarth@gmail.com> - 0.8.0-1
- update to 0.8.0 release
* Mon May 30 2016 Nick Bebout <nb@fedoraproject.org> - 0.7.0-1
- Upgrade to 0.7.0
* Thu May 12 2016 Nick Bebout <nb@fedoraproject.org> - 0.6.0-1
- Upgrade to 0.6.0
* Wed Apr 06 2016 Nick Bebout <nb@fedoraproject.org> - 0.5.0-1
- Upgrade to 0.5.0
* Sat Mar 05 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-3
- Package does not require python-werkzeug anymore, upstream #2453
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-2
- Fix build on EL7 where no newer setuptools is available
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-1
- Upgrade to 0.4.2
* Tue Mar 1 2016 Nick Le Mouton <nick@noodles.net.nz> - 0.4.1-1
- Upgrade to 0.4.1
* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Upgrade to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Upgrade to 0.3.0
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Upgrade to 0.2.0
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- Upgrade to 0.1.1
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-3
- Restore missing dependencies causing a FTBFS with py3 tests
- Add the man pages
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-4
- Specify more of the EPEL dependencies
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-3
- epel7: Only build python2 package
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Fix up the removal of the dev release snapshot
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Mon Nov 30 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3-dev20151123
- Update spec with comments from review
* Sat Nov 28 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec with comments from review
- Add python3 library
* Fri Nov 27 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-1.dev20151123
- initial packaging
