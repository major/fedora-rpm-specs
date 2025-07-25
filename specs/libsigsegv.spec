Name:    libsigsegv
Version: 2.14
Release: 11%{?dist}
Summary: Library for handling page faults in user mode

License: GPL-2.0-or-later
URL:     https://www.gnu.org/software/libsigsegv/
Source0: http://ftp.gnu.org/gnu/libsigsegv/libsigsegv-%{version}.tar.gz
Patch0:  configure.patch

BuildRequires: automake libtool
BuildRequires: gcc
BuildRequires: make

%description
This is a library for handling page faults in user mode. A page fault
occurs when a program tries to access to a region of memory that is
currently not available. Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory
  - memory-mapped access to persistent databases
  - generational garbage collectors
  - stack overflow handlers
  - distributed shared memory

%package devel
Summary: Development libraries and header files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package static
Summary: Static libraries for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.


%prep
%autosetup -p1


%build
# for patch1, rpaths
autoreconf -ivf

%configure \
  --enable-shared \
  --disable-silent-rules \
  --enable-static

%make_build


%install
%make_install

# remove libtool archives
find %{buildroot} -type f -name "*.la" -delete


%check
make check


%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libsigsegv.so.2*

%files devel
%{_libdir}/libsigsegv.so
%{_includedir}/sigsegv.h

%files static
%{_libdir}/libsigsegv.a


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Lukáš Zaoral <lzaoral@redhat.com> - 2.14-6
- migrate to SPDX license format

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Rex Dieter <rdieter@fedoraproject.org> - 2.14-1
- 2.14

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.13-1
- Update to 2.13
- spec file cleanup

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 2.11-9
- Fix configure tests compromised by LTO

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11-4
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.11-1
- libsigsegv-2.11 (#1425639)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.10-11
- .spec cleanup, update URL, use %%license (#1418517)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Rex Dieter <rdieter@fedoraproject.org> 2.10-3
- drop multilib hacks altogether (haven't been used since 2.9-2)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Rex Dieter <rdieter@fedoraproject.org> 2.10-1
- libsigsegv-2.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.9-3
- drop multilib hacks (no longer needed)

* Sun Nov 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.9-2
- multilib wrapper header not installed on i686 (#657941)

* Sat Nov 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.9-1
- libsigsegv-2.9 (#593618)

* Tue Sep 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.6-6
- respin mystack patch

* Tue Sep 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.6-5
- libsigsegv allocates alternate stack on the main stack (#524795)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.6-3
- move libsigsegv.so.* to /lib (#512219, F-12+)
- %%doc: -ChangeLog, +COPYING

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Rex Dieter <rdieter@fedoraproject.org> 2.6-1
- libsigsegv-2.6 (#486090)

* Mon Sep 29 2008 Rex Dieter <rdieter@fedoraproject.org> 2.4-7
- multilib (sparc) fixes

* Fri Feb 22 2008 Rex Dieter <rdieter@fedoraproject.org> 2.4-6
- multiarch conflicts (#342391)
- -static subpkg

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4-5
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.4-4
- respin (ppc32)

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.4-3
- License: GPLv2+

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.4-2
- fc6 respin

* Thu Jul 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.4-1
- 2.4

* Fri Apr 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.3-1
- 2.3

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net> 
- fc5: gcc/glibc respin

* Thu Oct 06 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 2.2-1
- 2.2
- omit .la file(s)
- include (tiny) static lib

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.1
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Jul 22 2004 Rex Dieter <rexdieter at sf.net> 0:2.1-0.fdr.2
- add URL: tag
- make check

* Mon Apr 12 2004 Rex Dieter <rexdieter at sf.net> 0:2.1-0.fdr.1
- 2.1
- cleanup macro usage
- -devel: Requires: %%name

* Thu Oct 02 2003 Rex Dieter <rexdieter at sf.net> 0:2.0-0.fdr.1
- first try.

