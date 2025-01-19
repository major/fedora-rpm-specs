Summary:   Support files for bmake, the NetBSD make(1) tool
Name:      mk-files
Version:   20210321
Release:   11%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:   LicenseRef-Callaway-BSD
URL:       ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source0:   ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/mk-%{version}.tar.gz
BuildArch: noarch

%description
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.

%prep
%setup -q -n mk
sed -i.timestamp -e 's|cp_f=-f|cp_f=-pf|' install-mk
sed -i -e 's/BINMODE=555/BINMODE=755/' install-mk
sed -i -e 's/env python/python3/g' meta2deps.py

%build

%install
install -p -m 755 -d ${RPM_BUILD_ROOT}%{_datadir}/mk
env FORCE_BSD_MK={RPM_BUILD_ROOT}/nonexistent \
    SYS_MK_DIR=${RPM_BUILD_ROOT}/nonexistent \
    sh install-mk -v -m 644 ${RPM_BUILD_ROOT}%{_datadir}/mk

%files
%doc ChangeLog README
%license LICENSE
%dir %{_datadir}/mk
%{_datadir}/mk/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 20210321-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210321-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Timothée Floure <fnux@fedoraproject.org> - 20210321-1
- New upstream release shipping LICENSE
- Set meta2deps.py bang to python3 instead of python2

* Thu Mar 18 2021 Timothée Floure <fnux@fedoraproject.org> - 20200505-3
- Remove useless buildroot removal in install section
- Use -p flag with install to preserve timestamps

* Thu Dec 24 2020 Timothée Floure <fnux@fedoraproject.org> - 20200505-2
- Minor permission fixes

* Thu Dec 24 2020 Timothée Floure <fnux@fedoraproject.org> - 20200505-1
- New upstream release

* Sun Apr 19 2020 Timothée Floure <fnux@fedoraproject.org> - 20191111-2
- Fix Python shebang in meta2deps.py.

* Fri Feb 28 2020 Luis Bazan <lbazan@fedoraproject.org> - 20191111-1
- New upstream version

* Tue Feb 12 2019 Luis Bazan <lbazan@fedoraproject.org> - 20180528-3
- rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180528-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Luis Bazan <lbazan@fedoraproject.org> - 20180528-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170505-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170505-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Luis Bazan <lbazan@fedoraproject.org> - 20170505-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Robert Mayr <robyduck@fedoraproject.org> - 20151111-1
- New Upstream Version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140314-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140314-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 09 2014 Luis Bazan <lbazan@fedoraproject.org> - 20140314-1
- New Upstream Version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130401-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Luis Bazan <lbazan@fedoraproject.org> - 20130401-1
- New Upstream Version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Luis Bazan <lbazan@fedoraproject.org> - 20120808-1
- New Upstream Version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120420-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Luis Bazan <bazanluis20@gmail.com> - 20120420-1
- New Upstream version 20120420-1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Luis Bazan <bazanluis20@gmail.com> - 20111111-1
- New upstream version 20111111

* Thu Sep 29 2011 Luis Bazan <bazanluis20@gmail.com> - 20110808-1
- new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Stepan Kasal <skasal@redhat.com> - 20081111-1
- new upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070430-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 2 2008 Julio M. Merino Vidal <jmmv@NetBSD.org> - 20070430-1
- Initial release for Fedora.
