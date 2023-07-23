Name:           python-ZEO
Version:        5.4.0
Release:        2%{?dist}
Summary:        Client-server storage implementation for ZODB

License:        ZPL-2.1
URL:            https://www.zodb.org/
Source0:        %pypi_source ZEO

BuildRequires:  gcc
BuildRequires:  python-ZODB-doc
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-persistent-doc
BuildRequires:  %{py3_dist cython}

%global common_desc                                                   \
ZEO is a client-server system for sharing a single storage among many \
clients.  When you use ZEO, the storage is opened in the ZEO server   \
process.  Client programs connect to this process using a ZEO         \
ClientStorage.  ZEO provides a consistent view of the database to all \
clients.  The ZEO client and server communicate using a custom RPC    \
protocol layered on top of TCP.

%description
%{common_desc}

%package        doc
Summary:        Documentation for ZEO
BuildArch:      noarch

%description    doc
Documentation for ZEO.

%package     -n python3-ZEO
Summary:        Client-server storage implementation for ZODB

%description -n python3-ZEO
%{common_desc}

%pyproject_extras_subpkg -n python3-ZEO msgpack uvloop

%prep
%autosetup -n ZEO-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -e "s|\('https://persistent\.readthedocs\.io/en/latest/', \)None|\1'%{_docdir}/python3-persistent-doc/objects.inv'|" \
    -e 's|\("https://zodb-docs\.readthedocs\.io/en/latest/", \)None|\1"%{_docdir}/python-ZODB-doc/html/objects.inv"|' \
    -i docs/conf.py

# Fedora has only msgpack 1.x.  Upstream only put the version restriction on
# to support Python 2, which we don't care about.
sed -i 's/msgpack < 1/msgpack/' setup.py

# Use mock from unittests
sed -i 's/import mock/from unittest &/' src/ZEO/asyncio/tests.py \
  src/ZEO/tests/test{ssl,ZEO,ZEOServer}.py
sed -i "/'mock'/d" setup.py

# Fix shebangs
%py3_shebang_fix src/ZEO

%generate_buildrequires
%pyproject_buildrequires -t -x msgpack,uvloop,docs

%build
cd src/ZEO/asyncio
cythonize -i *.pyx
cd -
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ZEO

# Because we built the Cython interface, we have to move everything from the
# noarch directory to the arch-specific directory.
if [ "%{python3_sitearch}" != "%{python3_sitelib}" ]; then
  mkdir -p %{buildroot}%{python3_sitearch}
  mv %{buildroot}%{python3_sitelib}/* %{buildroot}%{python3_sitearch}
  rm -fr %{buildroot}%{_prefix}/lib
  sed -i 's,%{python3_sitelib},%{python3_sitearch},g' ../python*
fi
cp -p src/ZEO/asyncio/*.so %{buildroot}%{python3_sitearch}/ZEO/asyncio

# Build documentation
%{py3_test_envvars} sphinx-build -b html -d docs/_build/doctrees docs \
  docs/_build/html
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

%check
%tox

%files -n python3-ZEO -f %{pyproject_files}
%doc CHANGES.html README.html
%license COPYRIGHT.txt
%{_bindir}/runzeo
%{_bindir}/zeo-nagios
%{_bindir}/zeoctl
%{_bindir}/zeopack
%{python3_sitearch}/ZEO/asyncio/_futures.cpython*
%{python3_sitearch}/ZEO/asyncio/_smp.cpython*

%files doc
%doc docs/_build/html

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 24 2023 Jerry James <loganjerry@gmail.com> - 5.4.0-1
- Dynamically generate BuildRequires

* Tue Jan 24 2023 Jerry James <loganjerry@gmail.com> - 5.4.0-1
- Version 5.4.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 5.3.0-3
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 5.3.0-2
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Jerry James <loganjerry@gmail.com> - 5.3.0-1
- Version 5.3.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug  9 2021 Jerry James <loganjerry@gmail.com> - 5.2.3-1
- Version 5.2.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.2.2-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Jerry James <loganjerry@gmail.com> - 5.2.2-2
- Remove unneeded mock BR
- Test with pytest

* Tue Aug 11 2020 Jerry James <loganjerry@gmail.com> - 5.2.2-1
- Version 5.2.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  9 2019 Jerry James <loganjerry@gmail.com> - 5.2.1-1
- New upstream release
- Drop redundant Requires
- Change msgpack name fix to version fix

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 5.2.0-4
- Drop python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-2
- Rebuilt for Python 3.7
- Don't BR trollius on python3

* Sat Apr  7 2018 Jerry James <loganjerry@gmail.com> - 5.2.0-1
- New upstream release

* Tue Mar 27 2018 Jerry James <loganjerry@gmail.com> - 5.1.2-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Dec 23 2017 Jerry James <loganjerry@gmail.com> - 5.1.1-1
- New upstream release

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 5.1.0-1
- New upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.0.4-2
- Rebuild for Python 3.6

* Sat Dec 10 2016 Jerry James <loganjerry@gmail.com> - 5.0.4-1
- New upstream release

* Tue Nov  1 2016 Jerry James <loganjerry@gmail.com> - 5.0.2-1
- New upstream release

* Tue Sep  6 2016 Jerry James <loganjerry@gmail.com> - 5.0.1-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul  4 2016 Jerry James <loganjerry@gmail.com> - 4.2.1-1
- New upstream release

* Fri Jun 17 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.1.0-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- New upstream release
- Name python 3 binaries according to policy
- Use license macro

* Thu Jun 12 2014 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Initial RPM
