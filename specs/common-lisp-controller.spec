Summary:      Common Lisp source and compiler manager
Name:         common-lisp-controller
Version:      7.4
Release:      30%{?dist}
URL:          https://alioth.debian.org/projects/clc
Source0:      http://ftp.de.debian.org/debian/pool/main/c/common-lisp-controller/common-lisp-controller_%{version}.tar.gz
Patch0:       common-lisp-controller-fedora.patch
License:      LLGPL
BuildArch:    noarch
Requires:     cl-asdf

%description
This package helps installing Common Lisp sources and compilers.
It creates a user-specific cache of compiled objects. When a library
or an implementation is upgraded, all compiled objects in the cache
are flushed. It also provides tools to recompile all libraries.

%prep 
%setup -q
%patch -P0 -p0 

%build
# Do nothing.

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/common-lisp
install -dm 755 $RPM_BUILD_ROOT%{_prefix}/sbin
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -dm 755 $RPM_BUILD_ROOT%{_sbindir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/man/man1
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/man/man3
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/man/man8
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/common-lisp
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/common-lisp/systems
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/common-lisp/source
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/common-lisp-controller
install -dm 755 $RPM_BUILD_ROOT%{_localstatedir}
install -dm 755 $RPM_BUILD_ROOT%{_localstatedir}/cache
install -dm 1777 $RPM_BUILD_ROOT%{_localstatedir}/cache/common-lisp-controller
# Not %{_libdir} because we really want /usr/lib even on 64-bit systems.
install -dm 755 $RPM_BUILD_ROOT/usr/lib/common-lisp
install -dm 755 $RPM_BUILD_ROOT/usr/lib/common-lisp/bin

for f in register-common-lisp-source unregister-common-lisp-source \
        register-common-lisp-implementation \
        unregister-common-lisp-implementation clc-update-customized-images; do
        install -m 755 $f $RPM_BUILD_ROOT%{_sbindir};
done;

for f in clc-register-user-package clc-unregister-user-package \
         clc-clbuild clc-lisp clc-slime; do
        install -m 755 $f $RPM_BUILD_ROOT%{_bindir};
done;

for f in common-lisp-controller.lisp post-sysdef-install.lisp; do
        install -m 644 $f $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/common-lisp-controller;
done;

install -m 644 lisp-config.lisp -p -D $RPM_BUILD_ROOT%{_sysconfdir}/lisp-config.lisp

gzip man/*
install -m 644 man/register-common-lisp-implementation.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8
install -m 644 man/clc-register-user-package.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 man/clc-clbuild.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 man/clc-lisp.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 man/clc-slime.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 man/common-lisp-controller.3.gz $RPM_BUILD_ROOT/%{_mandir}/man3

cd man
ln -s register-common-lisp-implementation.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/unregister-common-lisp-implementation.8.gz
ln -s register-common-lisp-implementation.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/register-common-lisp-source.8.gz
ln -s register-common-lisp-implementation.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/unregister-common-lisp-source.8.gz
ln -s register-common-lisp-implementation.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/clc-update-customized-images.8.gz
ln -s clc-register-user-package.1.gz  $RPM_BUILD_ROOT/%{_mandir}/man1/clc-unregister-user-package.1.gz
cd ..

# Think about it -- Rex
#triggerin -- sbcl
#/usr/sbin/register-common-lisp-implementation sbcl > /dev/null ||:

%files
%license debian/copyright
%doc DESIGN.txt
%dir %{_sysconfdir}/common-lisp
%dir /usr/lib/common-lisp
%dir /usr/lib/common-lisp/bin
%dir %{_localstatedir}/cache/common-lisp-controller
%config(noreplace) %{_sysconfdir}/lisp-config.lisp
%{_datadir}/common-lisp
%{_bindir}/clc-*
%{_sbindir}/clc-*
%{_sbindir}/register-*
%{_sbindir}/unregister-*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man8/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Anthony Green <green@redhat.com> - 7.4-17
- fix license handling

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.4-14
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  9 2010 Anthony Green <green@redhat.com> 7.4-2
- Fixed rhbz#642975: package creates /usr/lib64 on 32-bit system.

* Thu Nov  4 2010 Anthony Green <green@redhat.com> 7.4-1
- Upgrade.

* Thu Feb 18 2010 Rex Dieter <rdieter@fedoraproject.org>  6.20-2
- common-lisp-controller script problems (#499182)

* Sun Dec 27 2009 Anthony Green <green@redhat.com> 6.20-1
- Upgrade.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Anthony Green <green@redhat.com> 6.15-6
- Add new patch to allow for '+' in package names.

* Mon Sep 22 2008 Anthony Green <green@redhat.com> 6.15-5
- Own %%{_libdir}/common-lisp/bin.

* Sun Jul 13 2008 Anthony Green <green@redhat.com> 6.15-3
- Fix cache directory permissions.

* Mon Jul 07 2008 Anthony Green <green@redhat.com> 6.15-2
- Add debian/copyright and tweak description.

* Sun Jul 06 2008 Anthony Green <green@redhat.com> 6.15-1
- Upgrade.

* Thu Jan 03 2008 Anthony Green <green@redhat.com> 6.12-3
- Remove execute bit from lisp scripts and man pages.

* Sat Nov 11 2007 Anthony Green <green@redhat.com> 6.12-2
- Add cl-asdf dependency.

* Sat Sep 29 2007 Anthony Green <green@redhat.com> 6.12-1
- Created.
