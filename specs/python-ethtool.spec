# The tests fail in mock
%bcond_with tests

# Created by pyp2rpm-3.2.2
%global pypi_name ethtool

Name:           python-%{pypi_name}
Version:        0.15
Release:        15%{?dist}
Summary:        Python module to interface with %{pypi_name}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/fedora-python/%{name}
Source0:        %{pypi_source}

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  libnl3-devel
BuildRequires:  asciidoc

%description
Python bindings for the ethtool kernel interface, that allows querying and
changing of Ethernet card settings, such as speed, port, auto-negotiation, and
PCI locations.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python 3 bindings for the ethtool kernel interface, that allows querying and
changing of Ethernet card settings, such as speed, port, auto-negotiation, and
PCI locations.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

a2x -d manpage -f manpage man/pethtool.8.asciidoc
a2x -d manpage -f manpage man/pifconfig.8.asciidoc

%install
%py3_install
%if "%{_sbindir}" != "%{_bindir}"
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}{%{_bindir},%{_sbindir}}/pifconfig
mv %{buildroot}{%{_bindir},%{_sbindir}}/pethtool
%endif

mkdir -p %{buildroot}%{_mandir}/man8/
cp -p man/*.8 %{buildroot}%{_mandir}/man8/


%if %{with tests}
%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{__python3} tests/parse_ifconfig.py -v
%{__python3}  -m unittest discover -v
%endif


%files -n python3-%{pypi_name}
%doc README.rst CHANGES.rst
%license COPYING
%{_sbindir}/pifconfig
%{_sbindir}/pethtool
%doc %{_mandir}/man8/*
%{python3_sitearch}/%{pypi_name}.cpython-%{python3_version_nodots}*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.15-14
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.15-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.15-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.15-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.15-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Lumír Balhar <lbalhar@redhat.com> - 0.15-1
- Update to 0.15
Resolves: rhbz#1976135

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.14-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14-5
- Drop python2-ethtool

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14-1
- Update to 0.14

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Miro Hrončok <mhroncok@redhat.com> - 0.13-1
- Updated to 0.13
- Added python3 and python2 subpackages
- Add --with tests
- Modernize spec
- Remove merged patch
- Update upstream URL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 0.11-5
- Fix compile on F23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 8 2014 David Sommerseth <davids@redhat.com> - 0.11-1
- Updated to the lastest python-ethtool-0.11 release, which
  incorporates all these additional patches and improves
  libnl3 connection error checking.

* Mon Apr 7 2014 David Sommerseth <davids@redhat.com> - 0.10-6
- Removed the never close netlink patch
- Added a patch which will ensure it will open a valid socket in open_netlink()

* Wed Apr 2 2014 David Sommerseth <davids@redhat.com> - 0.10-5
- Update patch 8 - to also never close the netlink socket

* Wed Apr 2 2014 David Sommerseth <davids@redhat.com> - 0.10-4
- Added patch 8 - to see of FD_CLOEXEC impacts vdsm

* Tue Apr 1 2014 David Sommerseth <davids@redhat.com> - 0.10-3
- Added patch 6 and 7, to improve error handling.  Will be removed when released upstream

* Thu Mar 20 2014 David Sommerseth <davids@redhat.com> - 0.10-2
- Added patch 1, 2, 4 and 5; they have not appeared in an upstream release yet

* Thu Jan 09 2014 David Sommerseth <davids@redhat.com> - 0.10-1
- Updated to v0.10

* Wed Dec 11 2013 David Sommerseth <davids@redhat.com> - 0.9-2
- Forced rebuild with new tarball. Had pushed up old version.

* Tue Dec 10 2013 David Sommerseth <davids@redhat.com> - 0.9-1
- Rebased against upstream 0.9

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 David Malcolm <dmalcolm@redhat.com> - 0.8-1
- 0.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 13 2011 David Sommerseth <davids@redhat.com> - 0.7-2
- Fixed missing man page packaging

* Mon Apr 11 2011 David Sommerseth <davids@redhat.com> - 0.7-1
- Fixed several memory leaks (commit aa2c20e697af, abc7f912f66d)
- Improved error checking towards NULL values(commit 4e928d62a8e3)
- Fixed typo in pethtool --help (commit 710766dc722)
- Only open a NETLINK connection when needed (commit 508ffffbb3c)
- Added man page for pifconfig and pethtool (commit 9f0d17aa532, rhbz#638475)
- Force NETLINK socket to close on fork() using FD_CLOEXEC (commit 1680cbeb40e)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 David Sommerseth <dazo@users.sourceforge.net> - 0.6-1
- Don't segfault if we don't receive any address from rtnl_link_get_addr()
- Remove errornous file from MANIFEST
- Added ethtool.version string constant
- Avoid duplicating IPv6 address information
- import sys module in setup.py (Miroslav Suchy)

* Mon Aug  9 2010 David Sommerseth <davids@redhat.com> - 0.5-1
- Fixed double free issue (commit c52ed2cbdc5b851ebc7b)

* Wed Apr 28 2010 David Sommerseth <davids@redhat.com> - 0.4-1
- David Sommerseth is now taking over the maintenance of python-ethtool
- New URLs for upstream source code
- Added new API: ethtool.get_interfaces_info() - returns list of etherinfo objects
- Added support retrieving for IPv6 address, using etherinfo::get_ipv6_addresses()

* Fri Sep  5 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.3-2
- Rewrote build and install sections as part of the fedora review process
  BZ #459549

* Tue Aug 26 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.3-1
- Add get_flags method from the first python-ethtool contributor, yay
- Add pifconfig command, that mimics the ifconfig tool using the
  bindings available

* Wed Aug 20 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.2-1
- Expand description and summary fields, as part of the fedora
  review process.

* Tue Jun 10 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-3
- add dist to the release tag

* Tue Dec 18 2007 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-2
- First build into MRG repo

* Tue Dec 18 2007 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-1
- Get ethtool code from rhpl 0.212
