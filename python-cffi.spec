Name:           python-cffi
%global general_version 1.15.1
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        6%{?dist}
Summary:        Foreign Function Interface for Python to call C code
# Patch 482f0af has bits copied from CPython (PSF-2.0)
License:        MIT AND PSF-2.0
URL:            https://cffi.readthedocs.org/
Source:         https://foss.heptapod.net/pypy/cffi/-/archive/v%{version}/cffi-v%{version}.tar.bz2

# Adjust tests for a last minute Python 3.11 change in the traceback format 
Patch:          https://foss.heptapod.net/pypy/cffi/-/merge_requests/113.patch

# Drop usage of the deprecated py.test package
Patch:          https://foss.heptapod.net/pypy/cffi/-/merge_requests/115.patch
# Drop usage of the deprecated py.code package
Patch:          https://foss.heptapod.net/pypy/cffi/-/merge_requests/116.patch
# Python 3.12 compatibility
Patch:          https://foss.heptapod.net/pypy/cffi/-/commit/482f0af.patch
Patch:          https://foss.heptapod.net/pypy/cffi/-/commit/c3593e4.patch
Patch:          https://foss.heptapod.net/pypy/cffi/-/commit/87f514b.patch
Patch:          https://foss.heptapod.net/pypy/cffi/-/commit/69660bd.patch
Patch:          https://foss.heptapod.net/pypy/cffi/-/commit/814c55e.patch

BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  gcc

# For tests:
BuildRequires:  gcc-c++

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.

%package -n python3-cffi
Summary:        Foreign Function Interface for Python 3 to call C code
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pycparser

%description -n python3-cffi
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.

%package doc
Summary:        Documentation for CFFI
BuildArch:      noarch

%description doc
Documentation for CFFI, the Foreign Function Interface for Python.

%prep
%autosetup -p1 -n cffi-v%{general_version}%{?prerel}

%build
%py3_build

cd doc
make SPHINXBUILD=sphinx-build-3 html
rm build/html/.buildinfo

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest c/ testing/

%files -n python3-cffi
%doc README.md
%license LICENSE
%{python3_sitearch}/cffi/
%{python3_sitearch}/_cffi_backend.*.so
%{python3_sitearch}/cffi-%{general_version}%{?prerel}-py%{python3_version}.egg-info/

%files doc
%doc doc/build/html

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.15.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Miro Hrončok <mhroncok@redhat.com> - 1.15.1-3
- Fix build with pytest 7.2
- Fixes: rhbz#2142063

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Miro Hrončok <mhroncok@redhat.com> - 1.15.1-1
- Adjust tests for a last minute Python 3.11 change in the traceback format

* Mon Jul 11 2022 Lumír Balhar <lbalhar@redhat.com> - 1.15.1-0
- Update to 1.15.1
Resolves: rhbz#2102824

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.15.0-6
- Rebuilt for Python 3.11

* Wed Mar 30 2022 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-5
- Fix alignment issue on ppc64le
- Fixes: rhbz#2046865

* Wed Feb 02 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.15.0-4
- Backport patch to fix compatibility with Python 3.11
- Fixes: rhbz#2040165

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Tue Dec 21 2021 Lumír Balhar <lbalhar@redhat.com> - 1.15.0-1
- Update to 1.15.0
Resolves: rhbz#2013760

* Thu Oct 07 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.15.0~rc2-1
- Update to 1.15.0rc2
Resolves: rhbz#2007006

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Lumír Balhar <lbalhar@redhat.com> - 1.14.6-1
- Update to 1.14.6
Resolves: rhbz#1980622

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.14.5-2
- Rebuilt for Python 3.10

* Fri Feb 12 2021 Lumír Balhar <lbalhar@redhat.com> - 1.14.5-1
- Update to 1.14.5
Resolves: rhbz#1927933

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Joel Capitao <jcapitao@redhat.com> - 1.14.3-1
- Update to 1.14.3

* Tue Sep 08 2020 Lumír Balhar <lbalhar@redhat.com> - 1.14.2-1
- Update to 1.14.2 (#1869032)

* Fri Aug 14 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14.1-1
- Update to 1.14.1
- Fixes: rhbz#1860698
- Fixes: rhbz#1865276

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-2
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Lumír Balhar <lbalhar@redhat.com> - 1.14.0
- Update to 1.14.0 (#1800646)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Lumír Balhar <lbalhar@redhat.com> - 1.13.2-1
- Update to 1.13.2 (#1768219)

* Mon Oct 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.1-1
- Update to 1.13.1 (#1763767)

* Tue Oct 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.0-1
- Update to 1.13.0 (#1761757)

* Sun Oct 13 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-5
- Subpackage python2-cffi has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-3
- Reduce Python 2 build dependencies

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-1
- Update to 1.12.3 (#1701577)
- https://cffi.readthedocs.io/en/latest/whatsnew.html#v1-12-3

* Mon Jul 15 2019 Petr Viktorin <pviktori@redhat.com> - 1.12.2-2
- Remove unused build dependency on Cython
- Remove duplicate build dependency on pytest

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.2-1
- Update to 1.12.2 (#1677888)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.5-6
- Fix FTBFS (#1605627)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.5-4
- Rebuilt for Python 3.7

* Fri May 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.11.5-3
- Disable tests to fix mock-only FTBFS.

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.11.5-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Mar 02 2018 John Dulaney <jdulaney@Fedoraproject.org> - 1.11.2-1
- New release 1.11.5

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.11.2-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.11.2-1
- New release 1.11.0
- Fix %%check

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 1.11.0-2
- Cleanup spec file conditionals

* Sat Sep 23 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.11.0-1
- New release 1.11.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.10.0-1
- New release 1.10.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.9.1-1
- Update to latest upstream 1.9.1

* Fri Jan 6 2017 Orion Poplawski <orion@cora.nwra.com> - 1.8.3-4
- Modernize spec

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.8.3-3
- Rebuild for Python 3.6
- Disable test dependencies

* Thu Nov 03 2016 John Dulaney <jdulaney@Fedoraproject.org> - 1.8.3-2
- Re-disable check

* Sun Sep 18 2016 John Dulaney <jdulaney@Fedoraproject.org> - 1.8.3-1
- Update to 1.8.3
- Reenable check

* Wed Sep 07 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Tue Aug 09 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.7.0-3
- Record installed files

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 23 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Thu Apr 28 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6.0-3
- Switch Source0 to using pypi.io

* Thu Apr 28 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6.0-2
- Update Source0 URL to account for pypi change

* Thu Apr 21 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1329203)

* Mon Feb 15 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2 (#1299272)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.5.0-1
- Update to 1.5.0 (#1299272)

* Mon Jan 11 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.4.2-2
- Move python-cffi => python2-cffi

* Tue Dec 22 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2 (#1293504)

* Thu Dec 17 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.4.1-1
- Update to latest upstream release

* Fri Dec 11 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.3.1-1
- Update to latest upstream release

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1.1.2-4
- Rebuilt for Python3.5 rebuild

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.2-3
- Modernize spec file
- add missing source

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 16 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.1.2-2
- Update to 1.1.2
- Fix license

* Tue Aug 19 2014 Eric Smith <spacewar@gmail.com> 0.8.6-1
- Update to latest upstream.
- No python3 in el7.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 26 2014 Eric Smith <spacewar@gmail.com> 0.8.1-1
- Update to latest upstream.

* Tue Aug 13 2013 Eric Smith <spacewar@gmail.com> 0.6-5
- Add Requires of python{,3}-pycparser.

* Thu Jul 25 2013 Eric Smith <spacewar@gmail.com> 0.6-4
- Fix broken conditionals in spec (missing question marks), needed for el6.

* Tue Jul 23 2013 Eric Smith <spacewar@gmail.com> 0.6-3
- Add Python3 support.

* Mon Jul 22 2013 Eric Smith <spacewar@gmail.com> 0.6-2
- Better URL, and use version macro in Source0.

* Sun Jul 21 2013 Eric Smith <spacewar@gmail.com> 0.6-1
- initial version
