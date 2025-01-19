Name:           m4ri
Version:        20200125
Release:        13%{?dist}
Summary:        Linear Algebra over F_2
License:        GPL-2.0-or-later
URL:            https://bitbucket.org/malb/m4ri
VCS:            git:%{url}.git
Source:         %{url}/downloads/%{name}-%{version}.tar.gz
# This patch will not be sent upstream, as it is Fedora-specific.
# Permanently disable SSE3 and SSSE3 detection.  Without this patch, the
# config file tends to be regenerated at inconvenient times.
Patch:          %{name}-no-sse3.patch
# Fix a format specifier.
Patch:          %{name}-printf.patch
# Remove an unnecessary direct library dependency from the pkgconfig file,
# and also cflags used to compile m4ri, but not needed by consumers of m4ri.
Patch:          %{name}-pkgconfig.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  make


%description
M4RI is a library for fast arithmetic with dense matrices over F_2.
The name M4RI comes from the first implemented algorithm: The "Method
of the Four Russians" inversion algorithm published by Gregory Bard.
M4RI is used by the Sage mathematics software and the BRiAl library.


%package        devel
# The content of the HTML documentation is GPL-2.0-or-later.  The other licenses
# are for files copied into the documentation by doxygen.
# bc_s.png: GPL-1.0-or-later
# bdwn.png: GPL-1.0-or-later
# closed.png: GPL-1.0-or-later
# doc.png: GPL-1.0-or-later
# doxygen.svg: GPL-1.0-or-later
# dynsections.js: MIT
# folderclosed.png: GPL-1.0-or-later
# folderopen.png: GPL-1.0-or-later
# jquery.js: MIT
# menu.js: MIT
# menudata.js: MIT
# nav_f.png: GPL-1.0-or-later
# nav_g.png: GPL-1.0-or-later
# nav_h.png: GPL-1.0-or-later
# open.png: GPL-1.0-or-later
# splitbar.png: GPL-1.0-or-later
# sync_off.png: GPL-1.0-or-later
# sync_on.png: GPL-1.0-or-later
# tab_a.png: GPL-1.0-or-later
# tab_b.png: GPL-1.0-or-later
# tab_h.png: GPL-1.0-or-later
# tab_s.png: GPL-1.0-or-later
# tabs.css: GPL-1.0-or-later
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(js-jquery)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static library files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static %{name} library.


%prep
%autosetup -p0

# Fix the version number in the documentation, and generate only HTML
sed -i 's/20140914/%{version}/;/GENERATE_LATEX/s/YES/NO/' m4ri/Doxyfile


%build
%configure --enable-openmp \
%ifarch %{ix86} x86_64
  --enable-sse2

sed -e 's/^#undef HAVE_MMX/#define HAVE_MMX/' \
    -e 's/^#undef HAVE_SSE$/#define HAVE_SSE/' \
    -e 's/^#undef HAVE_SSE2/#define HAVE_SSE2/' \
    -i m4ri/config.h
sed -e 's/^\(#define __M4RI_HAVE_SSE2[[:blank:]]*\)0/\11/' \
    -e 's/^\(#define __M4RI_SIMD_CFLAGS[[:blank:]]*\).*/\1" -mmmx -msse -msse2"/' \
    -i m4ri/m4ri_config.h
sed -i 's/^SIMD_CFLAGS =.*/SIMD_CFLAGS = -mmmx -msse -msse2/' Makefile
%else
  --disable-sse2
%endif

# Die, rpath, die!  Also workaround libtool reordering -Wl,--as-needed after
# all the libraries
sed -e "s|\(hardcode_libdir_flag_spec=\)'.*|\1|" \
    -e "s|\(runpath_var=\)LD_RUN_PATH|\1|" \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Build documentation
cd m4ri
doxygen
cd -


%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la


%check
make check LD_LIBRARY_PATH=$PWD/.libs


%files
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}-0.0.%{version}.so


%files devel
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files static
%{_libdir}/lib%{name}.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 20200125-7
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Jerry James <loganjerry@gmail.com> - 20200125-1
- Version 20200125
- Drop upstreamed -restrict patch

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 20200115-1
- Version 20200115
- Add -pkgconfig and -restrict patches

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 20140914-12
- SSE2 is now default for 32-bit x86

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140914-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 20140914-5
- Update URLs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140914-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Jerry James <loganjerry@gmail.com> - 20140914-3
- Remove more unnecessary CFLAGS from the pkgconfig file

* Tue Mar  3 2015 Jerry James <loganjerry@gmail.com> - 20140914-2
- Fix CFLAGS in pkgconfig file (bz 1196519)
- Note bundled jquery

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 20140914-1
- New upstream version
- Fix license handling

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Jerry James <loganjerry@gmail.com> - 20130416-2
- Rebuild for libpng 1.6

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 20130416-1
- New upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121224-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 31 2012 Jerry James <loganjerry@gmail.com> - 20121224-1
- New upstream version
- Installed headers no longer need an update

* Mon Dec 10 2012 Jerry James <loganjerry@gmail.com> - 20120613-1
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120415-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Jerry James <loganjerry@gmail.com> - 20120415-1
- New upstream version
- New approach to eliminating unnecessary direct shared library dependencies
- More robust way of updating installed headers
- Fix the tests

* Mon Jan 30 2012 Jerry James <loganjerry@gmail.com> - 20111203-1
- New upstream version
- Add libpng-devel BR

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 20111004-2
- Rebuild for GCC 4.7

* Mon Oct 10 2011 Jerry James <loganjerry@gmail.com> - 20111004-1
- New upstream version
- Install the pkgconfig file, but remove the libm requirement

* Thu Jul 21 2011 Jerry James <loganjerry@gmail.com> - 20110715-1
- New upstream version
- Preserve timestamps on modified header files

* Fri Jun 17 2011 Jerry James <loganjerry@gmail.com> - 20110613-1
- New upstream version
- Rebase no-sse3 patch
- Drop defattr

* Wed Apr 20 2011 Jerry James <loganjerry@gmail.com> - 20100817-1
- New upstream version
- Drop license clarification; fixed in the source
- Compile both SSE2 and non-SSE2 variants for i686
- Disable SSE3 and SSSE3 extensions
- Build doxygen documentation
- Drop BuildRoot tag, clean script, and clean at start of install script
- Add check script

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081028-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081028-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 7 2008 Conrad Meyer <konrad@tylerc.org> - 20081028-3
- Add ldconfig.
- Move static libraries to -static subpackage.

* Thu Nov 6 2008 Conrad Meyer <konrad@tylerc.org> - 20081028-2
- Move the header files to -devel subpackage.

* Wed Nov 5 2008 Conrad Meyer <konrad@tylerc.org> - 20081028-1
- Initial package.
