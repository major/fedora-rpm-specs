%global srcname eventlet
%global _description %{expand:
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using co-routines to make the non-blocking
io operations appear blocking at the source code level.}

%bcond_without tests

Name:           python-%{srcname}
Version:        0.40.0
Release:        2%{?dist}
Summary:        Highly concurrent networking library
License:        MIT

URL:            https://eventlet.net
Source:         %pypi_source %{srcname}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

%package -n python3-%{srcname}-doc
Summary:        Documentation for python3-%{srcname}

%description -n python3-%{srcname}-doc
%{summary}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

sed -i '/ *pip install -e.*/d' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv},docs

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%tox -e docs

%check
%if %{with tests}
# Disable setting up dns (we have no /etc/resolv.conf in mock)
export EVENTLET_NO_GREENDNS=yes
%tox -e %{default_toxenv} -- -- -k 'not test_clear and not test_noraise_dns_tcp and not test_raise_dns_tcp and not test_dns_methods_are_green and not test_fork_after_monkey_patch and not test_send_timeout'
%else
%pyproject_check_import -e eventlet.green.* -e eventlet.hubs.pyevent -e eventlet.support.* -e eventlet.zipkin.*
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS NEWS

%files -n python3-%{srcname}-doc
%license LICENSE
%doc doc/build/html

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 16 2025 Peter Stensmyr <peter.stensmyr@aiven.io> - 0.40.0-1
- Update to 0.40.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.36.1-2
- Rebuilt for Python 3.13

* Thu Apr 11 2024 Alfredo Moralejo <amoralej@redhat.com > - 0.36.1-1
- Update to 0.36.1

* Fri Apr 5 2024 Alfredo Moralejo <amoralej@redhat.com > - 0.35.1-1
- Update to 0.35.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.33.3-2
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Sandro Mani <manisandro@gmail.com> - 0.33.3-1
- Update to 0.33.3

* Sun Sep 25 2022 Kevin Fenzi <kevin@scrye.com> - 0.33.1-5
- Disable failing test to fix FTBFS

* Tue Jul 26 2022 Carl George <carl@george.computer> - 0.33.1-4
- Convert to pyproject macros
- Build docs with make
- Disable tests on EPEL9

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.33.1-2
- Rebuilt for Python 3.11

* Sun May 29 2022 Kevin Fenzi <kevin@scrye.com> - 0.33.1-1
- Update to 0.33.1. Fixes rhbz#2085297

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Kevin Fenzi <kevin@scrye.com> - 0.33.0-1
- Update to 0.33.0. Fixes rhbz#2023953

* Tue Oct 05 2021 Lumír Balhar <lbalhar@redhat.com> - 0.32.0-2
- Unbundle dnspython

* Sat Sep 25 2021 Kevin Fenzi <kevin@scrye.com> - 0.32.0-1
- Update to 0.32.0. Fixes rhbz#2000093

* Fri Jul 30 2021 Kevin Fenzi <kevin@scrye.com> - 0.31.1-1
- Update to 0.31.1. Fixes rhbz#1981430
- Fix FTBFS rhbz#1981320

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.31.0-3
- Backport upstream patch to add compatibility of Eventlet with Python 3.10
- Fixes: rhbz#1913291

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.31.0-2
- Rebuilt for Python 3.10

* Sun May 16 2021 Kevin Fenzi <kevin@scrye.com> - 0.31.0-1
- Update to 0.31.0. Fixes rhbz#1957249
- Mitigates CVE-2021-21419

* Sun Mar 07 2021 Kevin Fenzi <kevin@scrye.com> - 0.30.2-1
- Update to 0.30.2. Fixes rhbz#1934511

* Sun Feb 07 2021 Kevin Fenzi <kevin@scrye.com> - 0.30.1-1
- Update to 0.30.1. Fixes rhbz#1923933

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Kevin Fenzi <kevin@scrye.com> - 0.30.0-1
- Update to 0.30.0. (rhbz#1907221)

* Mon Nov 30 2020 Joel Capitao <jcapitao@redhat.com> - 0.29.1-2.20201102git087ba743
- Bundle dns1 (rhbz#1896191)

* Fri Nov 06 2020 Joel Capitao <jcapitao@redhat.com> - 0.29.1-1.20201102git087ba743
- Update to 0.29.1.20201102git087ba743. (rhbz#1862178)

* Sat Oct 10 2020 Kevin Fenzi <kevin@scrye.com> - 0.26.0-1
- Update to 0.26.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.25.2-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Kevin Fenzi <kevin@scrye.com> - 0.25.2-1
- Update to 0.25.2. Fixes bug #1822602

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Subpackage python2-eventlet has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 0.25.1-1
- Update to 0.25.1. Fixes bug #1744357

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Kevin Fenzi <kevin@scrye.com> - 0.25.0-1
- Update to 0.25.0. Fixes bug #1713639

* Sat Mar 09 2019 Kevin Fenzi <kevin@scrye.com> - 0.24.1-4
- Drop python2-eventlet-doc subpackage as python2-sphinx is going away.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.24.1-2
- use python dependency generator

* Sun Oct 14 2018 Kevin Fenzi <kevin@scrye.com> - 0.24.1-1
- Update to 0.24.1. Fixes bug #1611023

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-1
- Update to 0.23.0 (#1575434)
- Add patch for Python 3.7 (#1594248)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.22.1-2
- Rebuilt for Python 3.7

* Sun Feb 18 2018 Kevin Fenzi <kevin@scrye.com> - 0.22.1-1
- Update to 0.22.1. Fixes bug #1546471

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Update to 0.22.0

* Tue Oct  3 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.21.0-3
- Fix upstream #401
- Fix compat with PyOpenSSL 17.3.0
- Cleanup BR

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Lumír Balhar <lbalhar@redhat.com> - 0.21.0-1
- Upstream 0.21.0
- Fix issue with enum-compat dependency for dependent packages
- Enable tests
- Fix tracebacks during docs generating by install python[23]-zmq

* Tue Apr 25 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.20.1-1
- Upstream 0.20.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.18.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 25 2016 Kevin Fenzi <kevin@scrye.com> - 0.18.4-1
- Update to 0.18.4. Fixes bug #1329993

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Jon Schlueter <jschluet@redhat.com> 0.17.4-4
- greenio: send() was running empty loop on ENOTCONN rhbz#1268351

* Thu Sep 03 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.4-3
- Tighten up Provides: and Obsoletes: for previous change

* Tue Sep 01 2015 Chandan Kumar <chkumar246@gmail.com> - 0.17.4-2
- Added python3 support

* Wed Jul 22 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.4-1
- Latest upstream

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.3-1
- Latest upstream

* Tue Mar 31 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.1-1
- Latest upstream

* Tue Sep 02 2014 Pádraig Brady <pbrady@redhat.com> - 0.15.2-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Alan Pevec <apevec@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Pádraig Brady <P@draigBrady.com - 0.12.0-1
- Update to 0.12.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Pádraig Brady <P@draigBrady.com - 0.9.17-2
- fix waitpid() override to not return immediately

* Fri Aug 03 2012 Pádraig Brady <P@draigBrady.com - 0.9.17-1
- Update to 0.9.17

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-6
- Update patch to avoid leak of _DummyThread objects

* Mon Mar  5 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-5
- Fix patch to avoid leak of _DummyThread objects

* Wed Feb 29 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-4
- Apply a patch to avoid leak of _DummyThread objects

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Pádraig Brady <P@draigBrady.com - 0.9.16-2
- Apply a patch to support subprocess.Popen implementations
  that accept the timeout parameter, which is the case on RHEL >= 6.1

* Sat Aug 27 2011 Kevin Fenzi <kevin@scrye.com> - 0.9.16-1
- Update to 0.9.16

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.12-1
- Updated to version 0.9.12.

* Wed Jul 28 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.9-1
- Updated to version 0.9.9.

* Wed Apr 14 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.7-1
- Initial package version.
