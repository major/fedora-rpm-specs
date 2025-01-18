Name:           gf2x
Version:        1.3.0
Release:        14%{?dist}
Summary:        Polynomial multiplication over the binary field

# GPL-3.0-or-later: the project as a whole
# LGPL-2.1-or-later: fft/gf2x-cantor-fft.h
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.inria.fr/gf2x/gf2x
VCS:            git:%{url}.git
Source:         %{url}/-/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.bz2
# Fix mismatched declarations and definitions
Patch:          %{name}-mismatched-decls.patch
# Change configure due to the Modern C initiative.  See
# https://fedoraproject.org/wiki/Changes/PortingToModernC
Patch:          %{name}-modern-c.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
Gf2x is a C/C++ software package containing routines for fast arithmetic
in GF(2)[x] (multiplication, squaring, GCD) and searching for
irreducible/primitive trinomials.

%package devel
Summary:        Headers and library files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and library files for developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%conf
# Fix the FSF's address
for badfile in `grep -FRl 'Fifth Floor' .`; do
  sed -e 's/Fifth Floor/Suite 500/' -e 's/02111-1307/02110-1335/' \
      -i.orig $badfile
  touch -r $badfile.orig $badfile
  rm -f $badfile.orig
done

# Generate the configure script
autoreconf -I config -fi .

%build
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Build the SSE2 version for x86, the native version for all other arches.
# Support for pclmul would be nice, but not all x86s support it.
%ifarch %{ix86} x86_64
%configure --disable-static --disable-hardware-specific-code --enable-sse2 \
  --disable-sse3 --disable-ssse3 --disable-sse41 --disable-pclmul \
  --disable-silent-rules --enable-fft-interface
# Workaround broken configure macros
sed -i.orig 's,/\* #undef \(GF2X_HAVE_SSE2_SUPPORT\) \*/,#define \1 1,' \
    gf2x/gf2x-config.h gf2x/gf2x-config-export.h
fixtimestamp gf2x/gf2x-config.h
fixtimestamp gf2x/gf2x-config-export.h
%else
# Workaround broken configure macros
sed -e "s/GF2X_SSE2_AVAILABLE_TRUE=$/&'#'/" \
    -e "/GF2X_SSE2_AVAILABLE_FALSE/s/'#'//" \
    -i configure
%configure --disable-static --disable-hardware-specific-code --disable-sse2 \
  --disable-sse3 --disable-ssse3 --disable-sse41 --disable-pclmul \
  --disable-silent-rules --enable-fft-interface
%endif

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build --eval='.SECONDARY:'

%install
%make_install INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
LD_LIBRARY_PATH=$PWD/.libs:$PWD/fft/.libs make check

%files
%doc AUTHORS BUGS NEWS README TODO
%license COPYING
%{_libdir}/lib%{name}.so.3
%{_libdir}/lib%{name}.so.3.*
%{_libdir}/lib%{name}-fft.so.3
%{_libdir}/lib%{name}-fft.so.3.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-fft.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Jerry James <loganjerry@gmail.com> - 1.3.0-8
- Convert License tag to SPDX
- Add patch to fix configure step for the Modern C initiative

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  8 2022 Jerry James <loganjerry@gmail.com> - 1.3.0-7
- New URLs
- Add -mismatched-decl patch to silence warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Version 1.3.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 1.2-4
- Drop SSE2 build for 32-bit x86, now default

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 1.2-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Jerry James <loganjerry@gmail.com> - 1.1-6
- Use license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug  3 2012 Jerry James <loganjerry@gmail.com> - 1.1-1
- New upstream release

* Fri May  4 2012 Jerry James <loganjerry@gmail.com> - 1.0-1
- Initial RPM
