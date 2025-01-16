%global gitdate         20240205
%global gittag          4cd2bd1357107cf0c83661fdda66c94987de4608
%global shorttag        %(c=%{gittag}; echo ${c:0:7})
%global user            Macaulay2

Name:           mathicgb
Version:        1.0
Release:        40.%{gitdate}.git%{shorttag}%{?dist}
Summary:        Groebner basis computations

License:        GPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathicgb
VCS:            git:%{url}.git
Source:         %{url}/tarball/%{gittag}/%{user}-%{name}-%{shorttag}.tar.gz

# Upstream wants to download gtest and compile it in; we don't
Patch:          %{name}-gtest.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(mathic)
BuildRequires:  pkgconfig(tbb)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Mathicgb is a program for computing Groebner basis and signature
Groebner bases.  Mathicgb is based on the fast data structures from
mathic.

%package devel
Summary:        Development files for mathicgb
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Files for developing applications that use mathicgb.

%package libs
Summary:        Mathicgb libraries

%description libs
Library interface to mathicgb.

%prep
%autosetup -p0 -n %{user}-%{name}-%{shorttag}

%conf
# Fix end-of-line encoding
sed -i.orig 's/\r//' doc/description.txt
touch -r doc/description.txt.orig doc/description.txt
rm -f doc/description.txt.orig

# Remove spurious executable bit
chmod a-x src/test/gtestInclude.cpp

# Upstream doesn't generate the configure script
autoreconf -fi

%build
export GTEST_PATH=%{_prefix}
%configure --disable-static --enable-shared --with-gtest=yes

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
sed -i 's|g++$|& -Wl,--as-needed|' Makefile

%make_build

%install
%make_install

# We don't want the libtool archive
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%files
%doc README.md doc/description.txt doc/slides.pdf
%{_bindir}/mgb
%{_mandir}/man1/mgb.1*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%{_libdir}/lib%{name}.so.0*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-40.20240205.git4cd2bd1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jerry James <loganjerry@gmail.com> - 1.0-39.20240205.git4cd2bd1
- Update to latest upstream snapshot
- Stop building for 32-bit x86

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-38.20231121.git09ea46a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-37.20231121.git09ea46a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.0-36.20231121.git09ea46a
- Rebuilt for TBB 2021.11

* Fri Jan 12 2024 Jerry James <loganjerry@gmail.com> - 1.0-35.20231121.git09ea46a
- Update to latest upstream snapshot

* Thu Oct 26 2023 Jerry James <loganjerry@gmail.com> - 1.0-34.20230916.gitde9cc70
- Update to latest upstream snapshot

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-33.20220621.gitf3a05da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Jerry James <loganjerry@gmail.com> - 1.0-32.20220621.gitf3a05da
- Drop 32-bit ARM workaround

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-32.20220621.gitf3a05da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.0-31.20220621.gitf3a05da
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-31.20220621.gitf3a05da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul  7 2022 Jerry James <loganjerry@gmail.com> - 1.0-30.20220621.gitf3a05da
- Update to latest upstream snapshot
- Drop upstreamed -endian and -move patches
- Remove -fwrapv from the build flags

* Thu Mar  3 2022 Jerry James <loganjerry@gmail.com> - 1.0-29.20220225.gitdc73a8d
- Update to latest upstream snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28.20210930.git9ed59d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 1.0-27.20210930.git9ed59d9
- Update to latest upstream snapshot
- Drop upstreamed -gcc11 patch

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26.20210109.git4d23c24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.0-25.20210109.git4d23c24
- Update to latest upstream snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24.20200526.git0d70da7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 1.0-23.20200526.git0d70da7
- Fix missing #includes for gcc-11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22.20200526.git0d70da7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21.20200526.git0d70da7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 1.0-20.20200526.git0d70da7
- Update to latest upstream snapshot
- Add -gtest and -move patches

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19.20181123.git636952f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18.20181123.git636952f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17.20181123.git636952f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Jerry James <loganjerry@gmail.com> - 1.0-16.20181123.git636952f
- Update to latest upstream snapshot

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 1.0-15.20170606.gitbd634c8
- Rebuild for tbb 2019_U1
- Bundle gtest 1.6.0 to avoid incompatibility with gtest 1.8.0+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14.20170606.gitbd634c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13.20170606.gitbd634c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Jerry James <loganjerry@gmail.com> - 1.0-12-20170606.gitbd634c8
- Remove mgb dependency on gtest

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 1.0-11.20170606.gitbd634c8
- Update to latest upstream snapshot

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20170104.git068ed9d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.20170104.git068ed9d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.20170104.git068ed9d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Feb 22 2017 Jerry James <loganjerry@gmail.com> - 1.0-7.20170104.git068ed9d
- Update to latest upstream snapshot
- Add -endian patch to fix build failure on big endian architectures

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.20160202.gitbb268df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 1.0-6.20160202.gitbb268df
- Rebuild for tbb 2017

* Mon Apr  4 2016 Jerry James <loganjerry@gmail.com> - 1.0-5.20160202.gitbb268df
- Update to latest upstream snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.20150903.git427e61f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jerry James <loganjerry@gmail.com> - 1.0-3.20150903.git427e61f
- Change to Macaulay2 repo
- Reenable TBB support now that the i386 bug has been fixed
- Use a patch instead of sed for gtest manipulations (mathicgb-gtest.patch)

* Tue Dec  1 2015 Jerry James <loganjerry@gmail.com> - 1.0-2.20131006.gitc72c945
- Do not use TBB for now

* Tue Dec  1 2015 Jerry James <loganjerry@gmail.com> - 1.0-1.20131006.gitc72c945
- Initial RPM
