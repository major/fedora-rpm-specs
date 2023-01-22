%bcond_without check
# https://bitbucket.org/glotzer/gsd/issues/11/
%bcond_with docs

%global pname gsd

%global desc \
GSD (General Simulation Data) is a file format specification and a library\
to read and write it. The package also contains a python module that reads\
and writes hoomd schema gsd files with an easy to use syntax.\
\
* Efficiently store many frames of data from simulation runs.\
* High performance file read and write.\
* Support arbitrary chunks of data in each frame (position, orientation,\
  type, etc...).\
* Append frames to an existing file with a monotonically increasing frame\
  number.\
* Resilient to job kills.\
* Variable number of named chunks in each frame.\
* Variable size of chunks in each frame.\
* Each chunk identifies data type.\
* Common use cases: NxM arrays in double, float, int, char types.\
* Generic use case: binary blob of N bytes.\
* Easy to integrate into other tools with python, or a C API (< 1k lines).\
* Fast random access to frames.

Name: python-gsd
Version: 2.5.2
Release: 4%{?dist}
Summary: Read and write hoomd schema gsd files with an easy to use syntax 
License: BSD
URL: https://gsd.readthedocs.io/
Source0: https://github.com/glotzerlab/%{pname}/archive/v%{version}/%{pname}-%{version}.tar.gz
Source1: https://readthedocs.org/projects/%{pname}/downloads/htmlzip/v%{version}/#/%{pname}-v%{version}-html.zip
BuildRequires: make
BuildRequires: gcc
%if %{with docs}
BuildRequires: python3-ipython-sphinx
%endif

%description
%{desc}

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
%{desc}

This package contains the documentation.

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-Cython
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-setuptools
%if %{with check}
BuildRequires: python3-pytest
%endif
%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
%{desc}

%prep
%setup -q -n %{pname}-%{version}

%build
%py3_build
%if %{with docs}
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$PWD \
  %{__python3} setup.py develop -d $PWD
make -C doc html
%else
unzip -qq %{S:1}
mv %{pname}-v%{version}/index.html doc/
rm doc/_static/css/gsd-theme.css
mv %{pname}-v%{version}/_static/*  doc/_static/
%endif

%install
%py3_install

%if %{with check}
%check
ln -s %{buildroot}/%{python3_sitearch}/%{pname}/fl.cpython-%{python3_version_nodots}-%{python3_platform_triplet}.so gsd/
%pytest -v gsd \
--basetemp=$(mktemp -d -p %{_tmppath}) \
%ifarch armv7hl i686
-k 'not test_large_n'
# array size too large for 32-bit arches
# https://github.com/glotzerlab/gsd/issues/58
%endif
%ifarch ppc64 s390x
-k "not test_gsd_v1_read \
and not test_gsd_v1_upgrade_read \
and not test_gsd_v1_write \
and not test_gsd_v1_upgrade_write"
# reading little-endian files on big-endian is unsupported
# https://github.com/glotzerlab/gsd/issues/12
%endif

rm -v gsd/fl.cpython-%{python3_version_nodots}-%{python3_platform_triplet}.so
%endif

%files doc
%license LICENSE
%doc doc/index.html doc/_static

%files -n python3-%{pname}
%license LICENSE
%doc CHANGELOG.rst README.md
%{_bindir}/%{pname}
%{python3_sitearch}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pname}

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.2-2
- Rebuilt for Python 3.11

* Tue May 31 2022 Dominik Mierzejewski <dominik@greysector.net> - 2.5.2-1
- update to 2.5.2 (fixes rhbz#2075808)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.5.1-1
- update to 2.5.1 (#2024221)

* Fri Oct 15 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.5.0-1
- update to 2.5.0 (#2013823)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.2-2
- Rebuilt for Python 3.10

* Fri May 21 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.4.2-1
- update to 2.4.2 (#1937729)
- work around testsuite looking for build module in source dir
- use pytest macro

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.4.0-1
- update to 2.4.0 (#1896835)

* Wed Nov 04 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.3.0-1
- update to 2.3.0 (#1893273)
- require setuptools explicitly

* Fri Aug 07 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.2.0-1
- update to 2.2.0 (#1866366)

* Thu Jul 23 2020 Dominik Mierzejewski <dominik@greysector.net> 2.1.2-1
- update to 2.1.2 (#1851376)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.9

* Thu Apr 23 2020 Dominik Mierzejewski <dominik@greysector.net> 2.1.1-1
- update to 2.1.1 (#1797605)
- update largefile test name to skip on 32-bit
- skip little-endian GSD file access tests on big-endian

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Dominik Mierzejewski <dominik@greysector.net> 1.10.0-1
- update to 1.10.0 (#1754636)
- skip largefile tests on 32-bit arches
- use /var/tmp instead of /tmp for test files to avoid filling up builder memory

* Sun Sep 22 2019 Dominik Mierzejewski <dominik@greysector.net> 1.9.0-1
- update to 1.9.0
- point to new upstream URLs
- switch test framework to pytest

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.1-4
- Subpackage python2-gsd has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Dominik Mierzejewski <dominik@greysector.net> 1.5.1-1
- update to 1.5.1
- include HTML documentation

* Fri Feb 23 2018 Dominik Mierzejewski <dominik@greysector.net> 1.5.0-1
- initial build
