%global debug_package %{nil}

Summary: A filemanager similar to XTree
Name: ytree
Version: 2.04
Release: 3%{?dist}

License: GPLv2+
URL: https://www.han.de/~werner/ytree.html
Source0: https://www.han.de/~werner/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel >= 5.4
BuildRequires: readline-devel >= 4.3 

%description
A console based file manager in the tradition of Xtree.

%prep
%autosetup

%build
%make_build

%install
install -m644 -D -p ytree.1 $RPM_BUILD_ROOT/%{_mandir}/man1/ytree.1
install -m755 -D -p ytree $RPM_BUILD_ROOT/%{_bindir}/ytree

%files 
%doc CHANGES COPYING README THANKS ytree.conf
%doc %{_mandir}/man1/ytree.1.gz
%{_bindir}/ytree

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 30 2022 Filipe Rosset <rosset.filipe@gmail.com> - 2.04-1
- Update to 2.04 fixes rhbz#2020860

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.03-1
- Update to 2.03 fixes rhbz#1813702

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.01-1
- Update to 2.01 fixes rhbz#1756725 + spec cleanup and modernization

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.99pl1-9
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99pl1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.99pl1-2
- Rebuild for readline 7.x

* Fri Dec 02 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.99pl1-1
- Rebuilt new release 1.99pl1, fixes rhbz #1178453 and rhbz #1371310

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.97-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 22 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.97-1
- Bug fix release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.94-1
- New upstream release
  #  Adapted Makefile to respect environment CC and LDFLAGS 
  #  New "login to parent node" command ('p')
- Dropped the redundant buildroot items and clean section 

* Sun Aug 30 2009 Minto Joseph <mvaliyav at redhat.com> - 1.93-1
- Rebased to 1.93

* Thu May 28 2009 Minto Joseph <mvaliyav at redhat.com> - 1.92-3
- Cleaned up spec file

* Thu May 28 2009 Minto Joseph <mvaliyav at redhat.com> - 1.92-2
- Cleaned up spec file 

* Thu May 28 2009 Minto Joseph <mvaliyav at redhat.com> - 1.92-1
- initial package

