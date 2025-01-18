Summary: Examines C/C++ source code for security flaws
Name: flawfinder
Version: 2.0.11
Release: 14%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL: http://www.dwheeler.com/flawfinder/

BuildArch: noarch
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Flawfinder scans through C/C++ source code,
identifying lines ("hits") with potential security flaws.
By default it reports hits sorted by severity, with the riskiest lines first.


%prep
%setup  -q
# Substitute the shebang to use python3
sed -i '1s@^#!/usr/bin/env python@#!/usr/bin/python3@' flawfinder


%build
make

%install
install -p -m755 -D flawfinder %{buildroot}%{_bindir}/flawfinder
install -p -m644 -D flawfinder.1 %{buildroot}%{_mandir}/man1/flawfinder.1

%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/flawfinder
%{_mandir}/man1/flawfinder.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.11-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.11-2
- explicitly BRs setuptools

* Sat Feb 29 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.11-1
- Update version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.8-1
- Update version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-2
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.6-1
- Update version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.5-2
- Fix shebang

* Fri Nov 17 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.5-1
- Update version

* Mon Oct 09 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.4-1
- Update version
- Use %%license tag
- Do not clean buildroot
- Use python3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.31-1
- New upstream release 1.31

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 14 2007 Jakub Hrozek <jhrozek@redhat.com> 1.27-3
- fix the dist tag
- fix build requires
- fix the Source URL to point to SF.net

* Sat Oct 13 2007 Jakub Hrozek <jhrozek@redhat.com> 1.27-2
- refactor the spec file to conform to the Fedora Guidelines

* Sat Feb 1 2003 Jose Pedro Oliveira <jpo@di.uminho.pt>
- changed build architecture to noarch
- replaced hardcoded directories by rpm macros
- removed several rpmlint warnings/errors

