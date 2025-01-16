%global gitdate         20230916
%global gittag          07e8df4ded6b586c0ce9eec0f9096690379749cb
%global shorttag        %(c=%{gittag}; echo ${c:0:7})
%global user            Macaulay2

Name:           mathic
Version:        1.0
Release:        30.%{gitdate}.git%{shorttag}%{?dist}
Summary:        Data structures for Groebner basis computations

License:        LGPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathic
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
BuildRequires:  pkgconfig(memtailor)

%description
Mathic is a C++ library of fast data structures designed for use in
Groebner basis computation.  This includes data structures for ordering
S-pairs, performing divisor queries and ordering polynomial terms during
polynomial reduction.

With Mathic you get to use highly optimized code with little effort so
that you can focus more of your time on whatever part of your Groebner
basis implementation that you are interested in.  The data structures
use templates to allow you to use them with whatever representation of
monomials/terms and coefficients that your code uses.  In fact the only
places where Mathic defines its own monomials/terms is in the test code
and example code.  Currently only dense representations of
terms/monomials are suitable since Mathic will frequently ask "what is
the exponent of variable number x in this term/monomial?".

%package devel
Summary:        Development files for mathic
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       memtailor-devel%{?_isa}

%description devel
Files for developing applications that use mathic.

%package tools
Summary:        Mathic-based tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Mathic-based tools.  Currently this contains:
- divsim: divisor query simulation
- pqsim: priority queue simulation

%prep
%autosetup -p0 -n %{user}-%{name}-%{shorttag}

%conf
# Upstream doesn't generate the configure script
autoreconf -fi .

%build
export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes GTEST_LIBS=-lgtest

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build
%make_build divsim pqsim

%install
%make_install

# We don't want the libtool archive
rm -f %{buildroot}%{_libdir}/lib%{name}.la

# Install the tools
mkdir -p %{buildroot}%{_bindir}
cp -p .libs/{divsim,pqsim} %{buildroot}%{_bindir}

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%files
%doc README.md
%license lgpl-2.1.txt
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/divsim
%{_bindir}/pqsim

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30.20230916.git07e8df4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29.20230916.git07e8df4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28.20230916.git07e8df4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 16 2023 Jerry James <loganjerry@gmail.com> - 1.0-27.20230916.git07e8df4
- Update to latest upstream snapshot

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26.20220426.git18ff8de
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25.20220426.git18ff8de
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.0-24.20220426.git18ff8de
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24.20220426.git18ff8de
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul  7 2022 Jerry James <loganjerry@gmail.com> - 1.0-23.20220426.git18ff8de
- Update to latest upstream snapshot
- Drop upstreamed -noreturn patch

* Thu Mar  3 2022 Jerry James <loganjerry@gmail.com> - 1.0-22.20220218.gitf52234d
- Update to latest upstream snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21.20210930.git68da8d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 1.0-20.20210930.git68da8d4
- Update to latest upstream snapshot
- Drop upstreamed -move patch

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19.20200709.gitcc52f46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.0-18.20200709.gitcc52f46
- Update to latest upstream snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17.20200526.git44095b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16.20200526.git44095b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  2 2020 Jerry James <loganjerry@gmail.com> - 1.0-15.20200526.git44095b8
- Update to latest upstream snapshot
- Add -move and -noreturn patches

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14.20181123.gite13b944
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13.20181123.gite13b944
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12.20181123.gite13b944
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Jerry James <loganjerry@gmail.com> - 1.0-11.20181123.gite13b944
- Update to latest upstream snapshot
- Add -tools subpackage for the new divsim and pqsim binaries

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20170606.git2f4a411
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.20170606.git2f4a411
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 1.0-8.20170606.git2f4a411
- Update to latest upstream snapshot

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.20160320.git558fff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6.20160320.git558fff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.20160320.git558fff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr  4 2016 Jerry James <loganjerry@gmail.com> - 1.0-4.20160320.git558fff0
- Update to latest upstream snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3.20150603.git18ff8ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jerry James <loganjerry@gmail.com> - 1.0-2.20150603.git18ff8ac
- Change to Macaulay2 repo
- Revert Macaulay2 patch to disable libtool (mathic-libtool.patch)
- Use a patch instead of sed for gtest manipulations (mathic-gtest.patch)

* Fri Nov 27 2015 Jerry James <loganjerry@gmail.com> - 1.0-1.20130827.git66b5d74
- Initial RPM
