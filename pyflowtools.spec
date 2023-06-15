%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif


Summary: An interface to OSU FlowTools
Name: pyflowtools
Version: 0.3.4.2
Release: 15%{?dist}
Source0: http://pyflowtools.googlecode.com/files/%{name}-%{version}.tar.gz
# No version specified.
License: GPL+
URL: http://pyflowtools.googlecode.com/
Requires: python3
BuildRequires: python3-devel zlib-devel flow-tools-devel gcc
Provides: python3-flowtools

%description
Python bindings to OSU Flow-Tools library

This is an interface which allows one to read flows stored by
OSU FlowTools into python program for further analysis.

%prep
%setup -q

%build
export libdirname=%{_lib}
%py3_build

%install
export libdirname=%{_lib}
%py3_install

%files
%doc COPYING CHANGES README example.py flowprint-full
%{python3_sitearch}/*

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.4.2-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.4.2-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.4.2-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.4.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jan 20 2019 Paul Komkoff <i@stingr.net> - 0.3.4.2-2
- Update to Python 3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.4.1-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Paul P. Komkoff Jr <i@stingr.net> - 0.3.4.1-1
- add exaddr_raw field.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 01 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.3.4-8
- Replace sitelib with sitearch. Otherwise fails to build from source

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.3.4-4
- new years rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.4-3
- Rebuild for Python 2.6

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.4-2
- fix license tag

* Fri Jul 18 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.3.4-1
- fix integer size-related bugs
- add some pydocs

* Wed Mar  5 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.3.3-1
- short bugfix release

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.2-2
- Autorebuild for GCC 4.3

* Thu Nov 29 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.3.2-1
- new upstream version

* Tue May 22 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.3-9
- rebuild

* Sun Dec 17 2006 Paul P. Komkoff Jr <i@stingr.net>
- rebuilt

* Fri Sep 15 2006 Paul P. Komkoff Jr <i@stingr.net>
- rebuilt

* Mon Feb 27 2006 Paul P Komkoff Jr <i@stingr.net> - 0.3-6
- Rebuild

* Fri Oct  7 2005 Paul P Komkoff Jr <i@stingr.net> - 0.3-5
- fix build on x86_64

* Thu Oct  6 2005 Paul P Komkoff Jr <i@stingr.net> - 0.3-4
- Use python sitelib instead of generated filelist - by
  Tom 'spot' Callaway
- Add dist tag

* Sun Sep 25 2005 Paul P Komkoff Jr <i@stingr.net> - 0.3-3
- fix BuildRoot

* Sun Sep 11 2005 Paul P Komkoff Jr <i@stingr.net> - 0.3-2
- Major bugfix update
- Submission to fedora extras

* Thu Jan  6 2005 Paul P Komkoff Jr <i@stingr.net>
- Updated to updated flow-tools-devel rpm

* Mon Sep  6 2004 Paul P Komkoff Jr <i@stingr.net>
- created RPM
- added fix to allow threads while reading flow
