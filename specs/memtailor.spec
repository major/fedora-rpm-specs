# There have been no releases, so we use a git snapshot
%global gitdate         20230916
%global gittag          f785005b92a54463dbd5377ab80855a3d2a5f92d
%global shorttag        %(cut -b -7 <<< %{gittag})
%global user            Macaulay2

Name:           memtailor
Version:        1.0
Release:        27.%{gitdate}.git%{shorttag}%{?dist}
Summary:        C++ library of special-purpose memory allocators

License:        BSD-3-Clause
URL:            https://github.com/Macaulay2/memtailor
VCS:            git:%{url}.git
Source:         %{url}/tarball/%{gittag}/%{user}-%{name}-%{shorttag}.tar.gz

# Upstream wants to download gtest and compile it in; we don't
Patch:          %{name}-gtest.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)

%description
Memtailor is a C++ library of special purpose memory allocators.  It
currently offers an arena allocator and a memory pool.

The main motivation to use a memtailor allocator is better and more
predictable performance than you get with new/delete.  Sometimes a
memtailor allocator can also be more convenient due to the ability to
free many allocations at one time.

The Memtailor memory pool is useful if you need to do many allocations
of a fixed size.  For example a memory pool is well suited to allocate
the nodes in a linked list.

You can think of the Memtailor arena allocator as being similar to stack
allocation.  Both kinds of allocation are very fast and require you to
allocate/deallocate memory in last-in-first-out order.  Arena allocation
has the further benefits that it stays within the C++ standard, it will
not cause a stack overflow, you can have multiple arena allocators at
the same time and allocation is not tied to a function invocation.

%package devel
Summary:        Development files for memtailor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for developing applications that use memtailor.

%prep
%autosetup -p0 -n %{user}-%{name}-%{shorttag}

%conf
# Remove spurious executable bits
chmod a-x src/test/*.cpp

# Fix the URL in the pkgconfig file
sed -i 's/broune/Macaulay2/' build/autotools/memtailor.pc.in

# Upstream doesn't generate the configure script, and we have altered
# Makefile.am anyway.
autoreconf -fi

%build
export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build

%install
%make_install

# We don't want the libtool archive
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%check
LD_LIBRARY_PATH=$PWD/.libs make check

%files
%doc README.md
%license license.txt
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-27.20230916.gitf785005
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26.20230916.gitf785005
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25.20230916.gitf785005
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Jerry James <loganjerry@gmail.com> - 1.0-24.20230916.gitf785005
- Update to latest upstream snapshot
- Upstream now requires C++17

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23.20220104.git95dbac7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0-22.20220104.git95dbac7
- Build with C++17 instead of C++11, since gtest 0.13.0 requires C++14 or later
- Make BuildRequires on autoconf and automake explicit
- Run autoreconf in build instead of prep

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21.20220104.git95dbac7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.0-20.20220104.git95dbac7
- Fix URL in the pkgconfig file
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20.20220104.git95dbac7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar  3 2022 Jerry James <loganjerry@gmail.com> - 1.0-19.20220104.git95dbac7
- Update to latest upstream snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18.20210930.git123afe0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 1.0-17.20210930.git123afe0
- Update to latest upstream snapshot

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16.20200709.git777c5d2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.0-15.20200709.git777c5d2
- Update to latest upstream snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14.20200526.git1d13f96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13.20200526.git1d13f96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Jerry James <loganjerry@gmail.com> - 1.0-12.20200526.git1d13f96
- Update to latest upstream snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr  4 2016 Jerry James <loganjerry@gmail.com> - 1.0-3.20160311.gite85453b
- Update to latest upstream snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2.20140924.git7b48b98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jerry James <loganjerry@gmail.com> - 1.0-1.20140924.git7b48b98
- Change to Macaulay2 repo
- Revert Macaulay2 patch to disable libtool (memtailor-libtool.patch)
- Use a patch instead of sed for gtest manipulations (memtailor-gtest.patch)

* Fri Sep  4 2015 Jerry James <loganjerry@gmail.com> - 0-1.20130809.git722a30c
- Initial RPM
