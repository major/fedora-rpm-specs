%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10
%undefine _debugsource_packages
%endif

Name:           cloog
%global         tarball_name %{name}
Version:        0.18.4
Release:        21%{?dist}
Epoch:		1
Summary:        The Chunky Loop Generator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.cloog.org

# This tarball was retrieved directly from the Git source code
# repository of the Cloog project by doing:
#
#    git clone git://repo.or.cz/cloog.git -b cloog-%{version} cloog-%{version}
#    tar -cvf cloog-%{version}.tar.gz cloog-%{version}

Source0:        cloog-%{version}.tar.gz

BuildRequires:  isl-devel >= 0.15
BuildRequires:  gmp-devel >= 6.0.0
BuildRequires:  texinfo >= 4.12
BuildRequires:  texinfo-tex >= 4.12
BuildRequires:  libtool
BuildRequires:  make
Obsoletes: cloog-ppl < 0.18.3
Obsoletes: cloog-ppl-devel < 0.18.3

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package devel
Summary:        Development tools for the Chunky Loop Generator
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       isl-devel >= 0.15, gmp-devel >= 6.0.0

%description devel
The header files and dynamic shared libraries of the Chunky Loop Generator.

%prep
%setup -q -n %{tarball_name}-%{version}

%build
./autogen.sh
%configure \
    --with-isl=system \
    --with-isl-prefix=%{_prefix}

# Remove the cloog.info in the tarball
# to force the re-generation of a new one
test -f doc/cloog.info && rm doc/cloog.info

%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10
CLOOG_CFLAGS="-fPIE"
%endif

# Remove the -fomit-frame-pointer compile flag
# Use system libtool to disable standard rpath
make %{?_smp_mflags} AM_CFLAGS=${CLOOG_CFLAGS} LIBTOOL=%{_bindir}/libtool
make %{?_smp_mflags} AM_CFLAGS=${CLOOG_CFLAGS} LIBTOOL=%{_bindir}/libtool -C doc cloog.pdf

%install
%make_install INSTALL="%{__install} -p"
# GCC wants the library to be named libcloog.so, as it's what it uses
# at runtime.
rm %{buildroot}%{_libdir}/*/*.cmake
mkdir -p %{buildroot}%{_docdir}/cloog-%{version}
%{__install} -m0644 -p README LICENSE ChangeLog doc/cloog.pdf %{buildroot}%{_docdir}/cloog-%{version}

%files
%{_docdir}/cloog-%{version}/README
%license %{_docdir}/cloog-%{version}/LICENSE
%{_docdir}/cloog-%{version}/ChangeLog
%{_bindir}/cloog
%{_libdir}/libcloog-isl.so.*

%files devel
%{_includedir}/cloog
%{_libdir}/libcloog-isl.so
%{_libdir}/pkgconfig/cloog-isl.pc
%exclude %{_libdir}/libcloog-isl.a
%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%exclude %{_libdir}/libcloog-isl.la
%endif
%{_docdir}/cloog-%{version}/cloog.pdf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.18.4-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Pablo Greco <pgreco@centosproject.org> - 1:0.18.4-14
- Fix FTBFS in Fedora >= 36
- Fix warn about unversioned obsoletes

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 David Howells <dhowells@redhat.com> - 1:0.18.4-1
- Update to upstream cloog-0.18.4

* Mon Jan 12 2015 David Howells <dhowells@redhat.com> - 1:0.18.3-1
      	     	  Dodji Seketeli <dodji@seketeli.org>
- Update to upstream cloog-0.18.3
- Obsoletes the previous cloog-ppl package.
- Requires isl-devel.
- Ship the ChangeLog file.
- Ship the libcloog-isl.so* files.

* Tue May 06 2014 Adam Williamson <awilliam@redhat.com> - 1:0.15.11-8
- rebuild for new libppl

* Mon Dec  3 2012 Tom Callaway <spot@fedoraproject.org> - 1:0.15.11-5
- roll back to 0.15.11

* Mon Dec  3 2012 Tom Callaway <spot@fedoraproject.org> - 0.16.1-4
- undo hacks

* Mon Dec  3 2012 Tom Callaway <spot@fedoraproject.org> - 0.16.1-3
- put the hacky provides in the right place

* Mon Dec  3 2012 Tom Callaway <spot@fedoraproject.org> - 0.16.1-2
- hack to get the compilers built (will go away)

* Fri Nov 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.16.1-1
- update to 0.16.1

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15.11-2.1
- rebuild with new gmp without compat lib

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15.11-2
- rebuilt once again with new gmp

* Tue Oct 18 2011  <dodji@redhat.com> - 0.15.11-1
- Update to cloog 0.15.11

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 0.15.9-2.1
- rebuild with new gmp

* Sat Nov 20 2010  <dodji@redhat.com> - 0.15.9-1
- Long overdue update to upstream revision 0.15.9
- Upstream fixes:
  http://gcc.gnu.org/PR43012
  Memory leaks
  Use top_builddir, not undefined builddir
  Uninitialised configure variables
  Compilation with -Wc++-compat
  Import cloog_domain_scatter from cloog trunk.
- Remove unused git_revision macro.
- Upate download URL to ftp://gcc.gnu.org/pub/gcc/infrastructure

* Mon Mar 01 2010 Dodji Seketeli <dodji@redhat.com> - 0.15-7-1
- Add README and LICENSE file to package
- Escape '%%' character in the changelog

* Sat Aug 15 2009 Dodji Seketeli <dodji@redhat.com> - 0.15.7-1
- Update to new upstream version (0.15.7)
- Do not build from git snapshot anymore. Rather, got the tarball from
  ftp://gcc.gnu.org/pub/gcc/infrastructure/cloog-ppl-0.15.7.tar.gz
- The upstream tarball is named cloog-ppl, not cloog. Adjusted thusly.
- Use system libtool to disable standard rpath
- Do not try to touch the info file if it's not present. Closes #515929.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.10.gitb9d79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Dodji Seketeli <dodji@redhat.com> - 0.15-0.9.gitb9d79
- Update to new upstream git snapshot.
- Update some comments in the spec file.

* Thu Apr 09 2009 Dodji Seketeli <dodji@redhat.com> - 0.15-0.8.git1334c
- Update to new upstream git snapshot
- Drop the cloog.info patch as now upstreamed
- No need to add an argument to the --with-ppl
  configure switch anymore as new upstream fixed this

* Wed Apr 08 2009 Dodji Seketeli <dodji@redhat.org> - 0.15-0.7.gitad322
- Add BuildRequire texinfo needed to regenerate the cloog.info doc

* Wed Apr 08 2009 Dodji Seketeli <dodji@redhat.org> - 0.15-0.6.gitad322
- Remove the cloog.info that is in the tarball
  That forces the regeneration of a new cloog.info with
  suitable INFO_DIR_SECTION, so that install-info doesn't cry
  at install time.
- Slightly changed the patch to make install-info actually
  install the cloog information in the info directory file.
- Run install-info --delete in %%preun, not in %%postun,
  otherwise the info file is long gone with we try to
  run install-info --delete on it.

* Mon Apr 06 2009 Dodji Seketeli <dodji@redhat.org> - 0.15-0.5.gitad322
- Added patch to fix #492794
- Need to add an argument to the --with-ppl switch now.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.4.gitad322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Dodji Seketeli <dodji@redhat.org> 0.15-0.3.gitad322
- Updated to upstream git hash foo
- Generate cloog-ppl and cloog-ppl-devel packages instead of cloog and
  cloog-devel.

* Mon Dec 01 2008 Dodji Seketeli <dodji@redhat.com> 0.15-0.2.git57a0bc
- Updated to upstream git hash 57a0bcd97c08f44a983385ca0389eb624e66e3c7
- Remove the -fomit-frame-pointer compile flag

* Wed Sep 24 2008 Dodji Seketeli <dodji@redhat.com> 0.15-0.1.git95753
- Initial version from git hash 95753d83797fa9a389c0c07f7cf545e90d7867d7

