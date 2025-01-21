Name:		winpdb
Version:	2.0.0
Release:	0.21.dev5%{?dist}
Summary:	An advanced python debugger
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://pypi.org/project/winpdb-reborn
Source0:	https://github.com/bluebird75/winpdb/archive/WINPDB_1_5_0.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
# Brings us to current git as of 20190815
Patch0:		winpdb-2.0.0dev5.patch
# https://github.com/bluebird75/winpdb/commit/3b720a6d98fbd8e9f282fa7e20677f55515da0c1
Patch1:		winpdb-colorterm-fix.patch
# https://github.com/bluebird75/winpdb/commit/047c35869e23d35188c9490cbbc87d574c77c939
Patch2:		winpdb-ensure-all-params-of-DES.new-are-set-to-byte.patch
BuildArch:	noarch
BuildRequires: 	python3-devel, desktop-file-utils
BuildRequires: 	python3-setuptools
Requires:	python3-crypto, python3-wxpython4
Provides:	winpdb-reborn = %{version}-%{release}

%description
Winpdb is an advanced python debugger, with support for smart breakpoints, 
multiple threads, namespace modification, embedded debugging, encrypted 
communication and speed of up to 20 times that of pdb.

%prep
%setup -q -n %{name}-WINPDB_1_5_0
%patch -P0 -p1 -b .dev5
%patch -P1 -p1 -b .colorterm-fix
%patch -P2 -p1 -b .bytes-fix
sed -i 's|/usr/bin/env python|/usr/bin/python3|g' rpdb2.py
sed -i 's|/usr/bin/env python|/usr/bin/python3|g' winpdb.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

desktop-file-install 		\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	%{SOURCE1}

chmod +x $RPM_BUILD_ROOT%{python3_sitelib}/rpdb2.py $RPM_BUILD_ROOT%{python3_sitelib}/winpdb.py

%files
%doc README.rst
%{_bindir}/*
%{python3_sitelib}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.21.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-0.20.dev5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.19.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-0.18.dev5
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.17.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.16.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.0-0.15.dev5
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.14.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.13.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-0.12.dev5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.11.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.10.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-0.9.dev5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.8.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.7.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-0.6.dev5
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.5.dev5
- add fixes from upstream
- remove unnecessary (and dead) dependency on wxPython-devel

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.4.dev5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-0.3.dev5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-0.2.dev5
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.1.dev5
- use winpdb-reborn sources, move to python3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Tom Callaway <spot@fedoraproject.org> - 1.4.8-20
- make explicit python2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Tom Callaway <spot@fedoraproject.org> - 1.4.8-18
- fix FTBFS

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.8-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Tom Callaway <spot@fedoraproject.org> - 1.4.8-9
- apply patch from debian for improved support with wxPython 3
- fix from upstream for breakpoints with commas (issue:19)

* Thu Dec  4 2014 Tom Callaway <spot@fedoraproject.org> - 1.4.8-8
- fix issue where winpdb doesn't launch in gnome-terminal properly anymore (bz1149030)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.4.8-5
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.8-1
- update to 1.4.8

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.6-1
- update to 1.4.6

* Wed Mar  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.4-4
- fix typo

* Wed Mar  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.4-3
- add icon, fix desktop file (bz 487870)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.4-1
- update to 1.4.4

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.4.2-2
- Rebuild for Python 2.6

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.2-1
- update to 1.4.2, source moved to google code

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.0-1
- update to 1.4.0

* Wed Apr 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.8-1
- update to 1.3.8

* Mon Mar 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.6-1
- update to 1.3.6

* Mon Jan 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.4-1.1
- bump to 1.3.4
- actually finish writing the changelog

* Tue Dec 11 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.2-1
- bump to 1.3.2

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.2-1
- bump to 1.2.2

* Mon Jul 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.4-1
- bump to 1.1.4

* Wed May 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.2-2
- fix desktop-file-utils usage in spec

* Mon May 14 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.2-1
- revisit for Fedora

* Sun Aug 28 2005 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-1
- initial build for Fedora Extras


