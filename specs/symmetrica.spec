%global gittag b24da56820651687cafb611809a4b1b0

Name:           symmetrica
Version:        3.1.0
Release:        1%{?dist}
Summary:        A Collection of Routines for Solving Symmetric Groups
# Note: they claim it's 'public domain' but then provide this:
# http://www.algorithm.uni-bayreuth.de/en/research/SYMMETRICA/copyright_engl.html
License:        ISC
URL:            https://gitlab.com/-/project/16178617
Source0:        %{url}/uploads/%{gittag}/%{name}-%{version}.tar.xz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make


%description
Symmetrica is a collection of routines, written in the programming
language C, through which the user can readily write his/her own
programs. Routines which manipulate many types of mathematical objects
are available.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p0

%build
%configure --disable-static --disable-silent-rules

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/*.la
rm doc/Makefile*


%check
cd src
make test
export LD_LIBRARY_PATH=$PWD/.libs
./test
cd -


%files
%doc README.md
%{_libdir}/lib%{name}.so.3*

%files devel
%doc doc
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Jan 13 2025 Carlos Rodriguez-Fernandez <carlosrodrifernandez@gmail.com> - 3.1.0-1
- Update to 3.1.0 (rhbz#2336496)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 3.0.1-9
- Stop building for 32-bit x86

* Wed Nov 22 2023 Florian Weimer <fweimer@redhat.com> - 3.0.1-9
- Fix C compatibility issue in symmetrica-attribute.patch

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 3.0.1-6
- Correct license from MIT to ISC (SPDX)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Jerry James <loganjerry@gmail.com> - 3.0.1-1
- Version 3.0.1
- New URLs
- Drop most of the patches
- Drop the unused -static subpackage
- Add a check script

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Jerry James <loganjerry@gmail.com> - 2.0-21
- Add -bruch patch to fix use-after-free problems in the bruch code
- Add -int32 patch to fix problems on 64-bit systems
- Add -rec01 patch to fix return values of rec01()
- Add -seq-point patch to fix undefined behavior
- Add -deref patch to fix a pointer to character comparison

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0-8
- Do not generate calls to undefined "local" functions.

* Tue May 8 2012 Jerry James <loganjerry@gmail.com> - 2.0-7
- Add patches to fix sagemath build problems, forwarded by pcpa
  <paulo.cesar.pereira.de.andrade@gmail.com>
- Drop unnecessary spec file elements (BuildRoot, clean script, etc.)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Conrad Meyer <konrad@tylerc.org> - 2.0-2
- Generate shared library as well as static library.

* Wed Oct 15 2008 Conrad Meyer <konrad@tylerc.org> - 2.0-1
- Initial package.
