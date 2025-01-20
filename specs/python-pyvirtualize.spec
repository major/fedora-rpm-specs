%global srcname pyVirtualize
%global modname pyvirtualize

%global date    20191018
%global commit0 dc2d971cb1ff51b91f31b7390c0a6a3151003e1f

# FIXME epel7 Could not import extension sphinx.ext.githubpages (exception: No module named githubpages)
%if 0%{?fedora}
%global with_build_doc 1
%endif

%global desc A python interface to access and manage pyvmomi.\
\
pyVirtualize is build over pyvmomi, hence it has ability\
to perform all the operations what vSphere client is able to.\
\
pyVirtualize provides easy interfaces to:\
Connect to ESX, ESXi, Virtual Center and Virtual Server hosts.\
Query hosts, datacenters, resource pools, virtual machines\
and perform various operations over them.\
VMs operations: power, file, process, snapshot, admin, utilities\
\
And of course, you can use it to access all the API through python.

Name:           python-%{modname}
# pypi tells current version
Version:        0.10
Release:        21.%{date}git%(c=%commit0; echo ${c:0:7} )%{?dist}
Summary:        Another python frontend to access and manage pyvmomi

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/rocky1109/%{srcname}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{srcname}-%{commit0}.tar.gz

BuildArch:      noarch

%description
%desc

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-pyvmomi

%description -n python%{python3_pkgversion}-%{modname}
%desc

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}
Requires:       python%{python3_other_pkgversion}-pyvmomi

%description -n python%{python3_other_pkgversion}-%{modname}
%desc
%endif

%package doc
Summary:        Documentation files for %{srcname}
BuildRequires:  web-assets-devel
%if 0%{?fedora} > 38
BuildRequires:  python-sphinxcontrib-jquery 
BuildRequires:  js-jquery
%endif
Requires:       js-jquery
# some js files of documentation are licensed with BSD-2-Clause
License:        Apache-2.0 AND BSD-2-Clause

%description doc
This package installs %{summary}.


%prep
%autosetup -n %{srcname}-%{commit0}
# skip backported dependencies
sed -i /typing/d requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%{?python3_other_pkgversion: %py3_other_build}
%if 0%{?with_build_doc}
# drop useless files
rm -rfv docs/build/*
sphinx-build -d docs/build/doctrees docs/source docs/build/html
# drop useless build garbage
find docs/build/html -name '.*' -print -delete
%endif

%if 0%{?fedora} < 39
# unbundle jquery
rm -fv docs/build/html/_static/jquery*.js
ln -fs %{_jsdir}/jquery/3/jquery.js docs/build/html/_static
%endif

%install
%{?python3_other_pkgversion: %py3_other_install}
%pyproject_install


%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
# skip egg-info due to PEP 517/518
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{modname}
%license LICENSE
%doc README.md
%{python3_other_sitelib}/%{srcname}/
%{python3_other_sitelib}/%{srcname}-%{version}-py?.?.egg-info/
%endif

%files doc
%license LICENSE
%doc docs/build/html/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.10-20.20191018gitdc2d971
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.10-18.20191018gitdc2d971
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Raphael Groner <raphgro@fedoraproject.org> - 0.10-14.20191018gitdc2d971
- skip jquery dropped with sphinx 6 as in F39+ 

* Tue Apr 04 2023 Raphael Groner <raphgro-at-fedoraproject.org> - 0.10.13.20191018gitdc2d971
- use new python macros, generate buildrequires
- fix sphinx with unbundled jquery

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10-10.20191018gitdc2d971
- Rebuilt for pyparsing-3.0.9

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10-9.20191018gitdc2d971
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-8.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10-6.20191018gitdc2d971
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4.20191018gitdc2d971
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10-3.20191018gitdc2d971
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Raphael Groner <projects.rg@smart.ms> - 0.10-2.20191018gitdc2d971
- skip backported dependency of module typing

* Thu Apr 02 2020 Raphael Groner <projects.rg@smart.ms> - 0.10-1.20191018gitdc2d971
- use latest snapshot, rhbz#1770851
- improve support for python3 and dependencies, see upstream commits
- drop support for python2
- get rid of useless build contionals

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9.20181003git57d2307
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-8.20181003git57d2307
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-7.20181003git57d2307
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.9-6.20181003git57d2307
- drop brand
- group BR by python version and subpackage

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5.20181003git57d2307
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 02 2019 Raphael Groner <projects.rg@smart.ms> - 0.9-4.20181003git57d2307
- add more build macros to fix b0rken dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3.20181003git57d2307
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Raphael Groner <projects.rg@smart.ms> - 0.9-2.20181003git57d2307
- use current snapshot
- use python3 only in Fedora but still also python2 in EPEL
- introduce modname macro

* Tue Sep 04 2018 Raphael Groner <projects.rg@smart.ms> - 0.9-1.20180205git4b01f44
- initial

