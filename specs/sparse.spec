Name: sparse

Version: 0.6.4

# either a rc? or %\{nil\}
%define rcver gce1a6720f69e

%if "x%{?rcver}" != "x"
%define build_ver       %{version}-%{rcver}
%define dotrc           .%{rcver}
%else
%define build_ver       %{version}
%define dotrc           %{nil}
%endif

Release: 4%{dotrc}%{?dist}.5
Summary:    A semantic parser of source files
License:    MIT
URL:        https://sparse.wiki.kernel.org
BuildRequires: make
BuildRequires: gcc
BuildRequires: libxml2-devel gtk2-devel
BuildRequires: sqlite-devel

Source0:    https://www.kernel.org/pub/software/devel/sparse/dist/sparse-%{build_ver}.tar.xz
Patch0:	    0001-linearize.c-fix-buffer-overrun-warning-from-fortify.patch

%description
Sparse is a semantic parser of source files: it's neither a compiler
(although it could be used as a front-end for one) nor is it a
preprocessor (although it contains as a part of it a preprocessing
phase).

It is meant to be a small - and simple - library.  Scanty and meager,
and partly because of that easy to use.  It has one mission in life:
create a semantic parse tree for some arbitrary user for further
analysis.  It's not a tokenizer, nor is it some generic context-free
parser.  In fact, context (semantics) is what it's all about - figuring
out not just what the grouping of tokens are, but what the _types_ are
that the grouping implies.

Sparse is primarily used in the development and debugging of the Linux kernel.

%prep
%autosetup -p1 -n sparse-%{build_ver}

%build
%define make_destdir \
make DESTDIR="%{buildroot}" PREFIX="%{_prefix}" \\\
     BINDIR="%{_bindir}" LIBDIR="%{_libdir}" \\\
     INCLUDEDIR="%{_includedir}" PKGCONFIGDIR="%{_libdir}/pkgconfig"

%make_destdir %{?_smp_mflags} CFLAGS="%{optflags}" HAVE_LLVM=no

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
%make_destdir install HAVE_LLVM=no

%check
make check HAVE_LLVM=no

%clean
rm -rf %{buildroot}
make clean

%files
%doc LICENSE README FAQ
%{_bindir}/sparse
%{_bindir}/semind
%{_bindir}/cgcc
%{_bindir}/c2xml
%{_bindir}/test-inspect
%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4.gce1a6720f69e.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Carlos Rodriguez-Fernandez <carlosrodrifernandez@gmail.com> - 0.6.4-4.gce1a6720f69e.4
- Migrated to SPDX license

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4.gce1a6720f69e.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4.gce1a6720f69e.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4.gce1a6720f69e.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Jeff Layton <jlayton@redhat.com> - 0.6.4-4.gce1a6720f69e
- Update to latest sparse git (commit ce1a6720f69e)
- Fix bogus snprintf length argument in linearize.c (bz2171731)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Jeff Layton <jlayton@redhat.com> - 0.6.4-3
- bump release to get around package version issue

* Wed Aug 10 2022 Jeff Layton <jlayton@redhat.com> - 0.6.4-2
- Add patch to address typeof() issues

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 07 2021 Jeff Layton <jlayton@redhat.com> - 0.6.4-1
- Update to 0.6.4 release

* Wed Sep 01 2021 Jeff Layton <jlayton@redhat.com> - 0.6.4.rc1-2
- Fix rpmlint warnings

* Wed Sep 01 2021 Jeff Layton <jlayton@redhat.com> - 0.6.4.rc1-1
- Update to 0.6.4-rc1 release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Jeff Layton <jlayton@redhat.com> - 0.6.3-1
- Update to 0.6.3 release

* Mon Aug 17 2020 Jeff Layton <jlayton@redhat.com> - 0.6.2-3
- Add some patches from upstream maint-v0.6.2 branch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Jeff Layton <jlayton@redhat.com> - 0.6.2-1
- Update to 0.6.2 release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Jeff Layton <jlayton@redhat.com> - 0.6.1-1
- Update to 0.6.1 release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Jeff Layton <jlayton@redhat.com> - 0.6.0-1
- Update to 0.6.0 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Jeff Layton <jlayton@redhat.com> - 0.5.2-1
-  Update to v0.5.2 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Jeff Layton <jlayton@redhat.com> - 0.5.1-2
- Rework CFLAGS handling patch

* Wed Oct 18 2017 Jeff Layton <jlayton@redhat.com> - 0.5.1-1
- Update to v0.5.1 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Jeff Layton <jlayton@redhat.com> - 0.5.0-10
- bring sparse up to the state of upstream git tree

* Mon Nov 14 2016 Kamil Dudka <kdudka@redhat.com> - 0.5.0-9
- avoid unnecessary build failure if llvm-devel is installed (bz# 1186794)

* Mon Nov 14 2016 Jeff Layton <jlayton@redhat.com> - 0.5.0-8
- Fix storage_modifiers handling of SForced (bz# 1109560)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Jeff Layton <jlayton@primarydata.com> - 0.5.0-4
- Fix handling of boolean sizes

* Sun Jun 15 2014 Jeff Layton <jlayton@primarydata.com> - 0.5.0-3
- Remove -fpic and -fPIC from CFLAGS. Seems to be causing weird effects with
  -O2. (bz# 1109560)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Jeff Layton <jlayton@redhat.com> - 0.5.0-1
- update to v0.5.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5.rc1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Jeff Layton <jlayton@redhat.com> - 0.4.5.rc1-2
- add test patch to silence warnings about __builtin_va_arg_pack() and
  __builtin_va_arg_pack_len()

* Tue Jul 09 2013 Jeff Layton <jlayton@redhat.com> - 0.4.5.rc1-1
- update to upstream rc1 release

* Thu Jun 27 2013 Jeff Layton <jlayton@redhat.com> - 0.4.4-6
- add built-in byte swap identifiers

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Jeff Layton <jlayton@redhat.com> - 0.4.4-2
- fix project URL in specfile (again) (bz#732529)

* Wed Nov 30 2011 Jeff Layton <jlayton@redhat.com> - 0.4.4-1
- update to new upstream release (bz#757482)

* Mon Aug 29 2011 Jeff Layton <jlayton@redhat.com> - 0.4.3-4
- fix project URL in specfile (bz#732529)

* Thu Jun 23 2011 Jeff Layton <jlayton@redhat.com> - 0.4.3-3
- fix build with gcc 4.6 (bz#716105)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Jeff Layton <jlayton@redhat.com> - 0.4.3-1
- Update to 0.4.3

* Sun Oct 18 2009 Jeff Layton <jlayton@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Tue Sep 29 2009 Jeff Layton <jlayton@redhat.com> - 0.4.2rc1-1
- Update to 0.4.2rc1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun  1 2008 Tom "spot" Callaway <tcallawa@redhat.com? - 0.4.1-3
- use fPIC on sparcv9/sparc64

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.1-2
- Autorebuild for GCC 4.3

* Tue Nov 13 2007 Roland McGrath <roland@redhat.com> - 0.4.1-1
- Upgrade to 0.4.1

* Thu Nov  1 2007 Roland McGrath <roland@redhat.com> - 0.4-2
- Upgrade to 0.4
- Install man pages, c2xml.
- Run make check in rpmbuild.

* Tue Aug 28 2007 Roland McGrath <roland@redhat.com> - 0.3-2
- Canonicalize License: tag.

* Thu May  3 2007 Roland McGrath <roland@redhat.com> - 0.3-1
- Upgrade to 0.3

* Tue Dec 05 2006 Matt Domsch <Matt_Domsch@dell.com> 0.2-1
- Upgrade to 0.2, add -devel package

* Thu Nov 09 2006 Matt Domsch <Matt_Domsch@dell.com> 0.1-1
- Upgrade to 0.1, no need for snapshots, yea!  New upstream maintainer.
- cgcc now installed

* Thu Oct 26 2006 Matt Domsch <Matt_Domsch@dell.com> 0-0.1.20061026git
- Initial packaging for Fedora Extras
