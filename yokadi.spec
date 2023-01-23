Name:           yokadi
Version:        1.2.0
Release:        6%{?dist}
Summary:        Command line oriented todo list system

License:        GPLv3+
URL:            https://yokadi.github.io
Source0:        %{url}/download/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       python3-sqlalchemy
Requires:       python3-dateutil

%description
Yokadi is a command-line oriented, SQLite powered, TODO list tool.
It helps you organize all the things you have to do and you must not
forget.It aims to be simple, intuitive and very efficient.

In Yokadi you manage projects, which contains tasks. At the minimum,
a task has a title, but it can also have a description, a due date,
an urgency or keywords. Keywords can be any word that help you to find
and sort your tasks.

%prep
%autosetup
sed -i -e '/^#!\//, 1d' {yokadi/yokadid.py,yokadi/createdemodb.py,yokadi/tests/tests.py}

%build
%py3_build

%install
%py3_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc NEWS README.md doc/*.md
%license LICENSE
%{_mandir}/man*/*.*
%{_bindir}/%{name}
%{_bindir}/yokadid
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info
%{_datadir}/icons/hicolor/*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.11

* Thu Mar 10 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-3
- Remove crypto support (closes rhbz#2061884)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Update to latest upstream release 1.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-16
- Rebuilt for Python 3.10

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-13
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-10
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.1-4
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to new upstream version 1.1.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Update to new upstream version 1.0.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 01 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Add desktop file
- Update license
- Update to new upstream version 0.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-8
- Spec file update

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.13.0-5
- Remove the python-sqlite2 dep as yokadi will work with sqlite3 from the stdlib

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-3
- Rebuild

* Mon May 16 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-2
- python-crypto added

* Sun Apr 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-1
- New requirement: pycrypto (not in Fedora at the moment)
- Update to new upstream version 0.13.0

* Wed Nov 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-2
- Add man pages

* Wed Nov 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to new upstream version 0.12.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Dec 23 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.2-1
- Update to new upstream version 0.11.2

* Fri Nov 20 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.1-1
- Update to new upstream version 0.11.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.0-2
- Change BR

* Mon Jul 13 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.0-1
- Initial spec for Fedora
