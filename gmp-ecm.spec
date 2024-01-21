Name:           gmp-ecm
Version:        7.0.5
Release:        4%{?dist}
Summary:        Elliptic Curve Method for Integer Factorization
License:        GPL-3.0-or-later
URL:            https://gitlab.inria.fr/zimmerma/ecm
Source0:        %{url}/-/archive/git-%{version}/ecm-git-%{version}.tar.bz2

BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  make

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Programs and libraries employing elliptic curve method for factoring
integers (with GMP for arbitrary precision integers).


%package        devel
Summary:        Files useful for %{name} development
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}


%description    devel
The libraries and header files for using %{name} for development.


%package        libs
Summary:        Elliptic Curve Method library
License:        LGPL-3.0-or-later


%description    libs
The %{name} elliptic curve method library.


%prep
%autosetup -n ecm-git-%{version}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix non-UTF-8 encodings
for badfile in AUTHORS ; do
  iconv -f iso-8859-1 -t utf-8 -o $badfile.UTF-8 $badfile 
  touch -r $badfile $badfile.UTF-8
  mv $badfile.UTF-8 $badfile
done

# Fix the FSF's address
for badfile in `grep -FRl 'Fifth Floor' .`; do
  sed -e 's/Fifth Floor/Suite 500/' -e 's/02111-1307/02110-1335/' \
      -i.orig $badfile
  fixtimestamp $badfile
done

# Generate the configure script
autoreconf -fi .


%build
# Build an SSE2-enabled version for 32-bit x86, and a non-SSE2 version for all
# other arches, including x86_64; the assembly code containing SSE2
# instructions is 32-bit only.
%configure --disable-static --enable-shared --enable-openmp \
  --disable-gmp-cflags \
%ifarch %{ix86}
  --enable-sse2 \
%else
  --disable-sse2 \
%endif
  CFLAGS='%{build_cflags} -Wa,--noexecstack' \
  LDFLAGS='%{build_ldflags} -Wl,-z,noexecstack -lgmp -lgomp'

# Eliminate hardcoded rpaths; workaround libtool reordering -Wl,--as-needed
# after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build


%install
%make_install INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
pushd $RPM_BUILD_ROOT%{_bindir}
  mv ecm %{name}
popd
pushd $RPM_BUILD_ROOT%{_mandir}/man1
  for file in ecm.1*; do
    mv $file ${file/ecm/%{name}}
  done
popd


%check
export LD_LIBRARY_PATH=$PWD/.libs
make check


%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%files devel
%doc README.lib
%{_includedir}/ecm.h
%{_libdir}/libecm.so


%files libs
%doc AUTHORS ChangeLog NEWS TODO
%license COPYING.LIB
%{_libdir}/libecm.so.1
%{_libdir}/libecm.so.1.*


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Jerry James <loganjerry@gmail.com> - 7.0.5-1
- Version 7.0.5
- New URLs
- Convert License tags to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Jerry James <loganjerry@gmail.com> - 7.0.4-16
- New project and download URLs, and repacked tarball

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Jerry James <loganjerry@gmail.com> - 7.0.4-10
- Rebuild to fix "undefined symbol: __gmpn_add_nc"

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 7.0.4-7
- Do not do a special SSE2 build for 32-bit x86; that is default now

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 11 2016 Jerry James <loganjerry@gmail.com> - 7.0.4-1
- New upstream release
- Drop upstreamed patch

* Tue Aug 30 2016 Richard W.M. Jones <rjones@redhat.com> - 7.0.3-2
- Add proposed upstream fix for RHBZ#1367571.

* Mon Jul  4 2016 Jerry James <loganjerry@gmail.com> - 7.0.3-1
- New upstream release

* Tue Jun 28 2016 Jerry James <loganjerry@gmail.com> - 7.0.2-1
- New upstream release

* Wed May 25 2016 Jerry James <loganjerry@gmail.com> - 7.0.1-1
- New upstream release

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 7.0-1
- New upstream release
- Drop the -static subpackage; nothing needs it

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov  6 2015 Jerry James <loganjerry@gmail.com> - 6.4.4-7
- Rebuild to fix broken symbol issue (bz 1278522)
- Avoid unneeded library dependencies

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Jerry James <loganjerry@gmail.com> - 6.4.4-5
- Use license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar  4 2013 Jerry James <loganjerry@gmail.com> - 6.4.4-1
- New upstream release
- Drop all patches; all were from upstream subversion and are now applied
- Workaround for bz 759376 no longer necessary

* Sat Feb 23 2013 Jerry James <loganjerry@gmail.com> - 6.4.3-2
- Add -gmp51 patch to deal with changes in GMP 5.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Jerry James <loganjerry@gmail.com> - 6.4.3-1
- New upstream release
- Fix PPC64 build (bz 804330)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr  2 2012 Jerry James <loganjerry@gmail.com> - 6.4.2-1
- New upstream release

* Mon Mar 19 2012 Jerry James <loganjerry@gmail.com> - 6.4.1-2
- Fix elimination of hardcoded rpaths
- Mark -devel and -static as LGPLv3+ as well

* Mon Mar 19 2012 Jerry James <loganjerry@gmail.com> - 6.4.1-1
- New upstream release
- Split library and binaries into separate packages for licensing reasons
- Disable broken shellcmd feature

* Mon Jan 23 2012 Jerry James <loganjerry@gmail.com> - 6.4-1
- New upstream release

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 6.3-2
- Rebuild for GCC 4.7

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.3-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 6.3-1.1
- rebuild with new gmp

* Fri May 13 2011 Jerry James <loganjerry@gmail.com> - 6.3-1
- New upstream release
- Drop BuildRoot tag, clean script, and clean at start of install script
- Build an SSE2 version of the library for 32-bit x86
- Ensure the executable stack flag is not set on any ELF objects
- Various cleanups to fix rpmlint warnings
- Add check script

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 30 2009 Conrad Meyer <konrad@tylerc.org> - 6.2.3-1
- Bump to 6.2.3.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Conrad Meyer <konrad@tylerc.org> - 6.2.1-4
- Convert AUTHORS to utf-8 as well.
- Really bump release this time.

* Sat Nov 29 2008 Conrad Meyer <konrad@tylerc.org> - 6.2.1-3
- Add some %%docs.
- Add ldconfig (oops).
- Install binary and manpage under gmp-ecm, not ecm.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 6.2.1-2
- Change name.
- Split out a -static package and build shared libs for -devel.

* Wed Nov 26 2008 Conrad Meyer <konrad@tylerc.org> - 6.2.1-1
- Initial package.
