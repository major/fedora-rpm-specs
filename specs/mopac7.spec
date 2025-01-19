Name:           mopac7
Summary:        Semi-empirical quantum mechanics suite
Version:        1.15
Release:        48%{?dist}
# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/554
# SPDX confirmed
License:        LicenseRef-Fedora-Public-Domain
URL:            http://sourceforge.net/projects/mopac7/
Source0:        http://bioinformatics.org/ghemical/download/current/mopac7-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-gfortran
BuildRequires:  libtool
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
MOPAC7 is a semi-empirical quantum-mechanics code written by James
J. P. Stewart and co-workers. The purpose of this project is to
maintain MOPAC7 as a stand-alone program as well as a library that
provides the functionality of MOPAC7 to other programs.

%package        libs
Summary:        Dynamic libraries from %{name}

%description    libs
Dynamic libraries from %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
perl -pi -e "s#-lg2c##g" libmopac7.pc.in

%build
autoreconf -fiv
# The f2c-generated sources are not compatible with C99.
%global build_type_safety_c 0
%set_build_flags
CFLAGS="$CFLAGS -std=gnu89"
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
# make install does not actually install the main binary
# chrpath --delete     fortran/.libs/%{name}
install -pDm0755 fortran/.libs/%{name} %{buildroot}%{_bindir}/%{name}
# install a convenience fortran wrapper for the main binary
sed "s;./fortran;%{_bindir};" run_mopac7 > %{buildroot}%{_bindir}/run_mopac7
chmod 755 %{buildroot}%{_bindir}/run_mopac7
# kill off the .la files
find %{buildroot}%{_libdir} -name *.la -delete -print
# kill off the makefiles in tests directory so we can use them as samples in %doc
find tests -name 'Makefile*' -delete -print

%ldconfig_scriptlets libs

%files
%doc tests
%{_bindir}/mopac7
%{_bindir}/run_mopac7

%files libs
%license COPYING
%{_libdir}/libmopac7.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/mopac7/
%{_libdir}/libmopac7.so
%{_libdir}/pkgconfig/libmopac7.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 10 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.15-46
- SPDX migration

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 1.15-43
- Set build_type_safety_c to 0 (#2159702)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 1.15-40
- Build in C89 mode (#2159702)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Jeff Law <law@redhat.com> - 1.15-35
- Re-enable LTO

* Fri Aug  7 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.15-34
- Disable lto for now

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-33
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.15-26
- F-28: rebuild for gfortran 8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.15-22
- F-26: rebuild againt gfortran 7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Christopher Meng <rpm@cicku.me> - 1.15-18
- NVR bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Carl Byington <carl@five-ten-sg.com> 1.15-15
- add autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Carl Byington <carl@five-ten-sg.com> 1.15-12
- Remove static from description of devel subpackage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 07 2010 Carl Byington <carl@five-ten-sg.com> 1.15-9
- Subpackage Licensing, main package requires -libs to get
  license files.

* Sat Jan 02 2010 Jussi Lehtola <jussi.lehtola@iki.fi> 1.15-8
- avoid use of chrpath.

* Wed Dec 23 2009 Carl Byington <carl@five-ten-sg.com> 1.15-7
- fedora review changes, remove rpath from binaries,
  --disable-rpath not enough, needs chrpath.
- move the %%doc files to -libs package.

* Wed Dec 23 2009 Carl Byington <carl@five-ten-sg.com> 1.15-6
- proper installation of the main binary rather than the
  libtool wrapper.
- fixup the fortran wrapper script to properly reference the
  installed binary.

* Wed Dec 23 2009 Carl Byington <carl@five-ten-sg.com> 1.15-5
- devel requires pkgconfig for EPEL
- build requires gcc-gfortran

* Wed Dec 23 2009 Carl Byington <carl@five-ten-sg.com> 1.15-4
- install -p to preserve timestamps
- explicit includedir name
- add pkgconfig for EPEL

* Sun Dec 20 2009 Carl Byington <carl@five-ten-sg.com> 1.15-3
- explicit names in %%files section rather than wildcards

* Wed Dec 02 2009 Carl Byington <carl@five-ten-sg.com> 1.15-2
- fix source url path
- remove static libraries

* Wed Nov 25 2009 Carl Byington <carl@five-ten-sg.com> 1.15-1
- convert to fedora compatible spec file

* Tue Aug 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.11-2mdv2007.0
- remove -lg2c from pkgconfig file

* Tue Aug 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.11-1mdv2007.0
- 1.11
- %%mkrel
- fix mixed-use-of-spaces-and-tabs

* Sun Dec 04 2005 Austin Acton <austin@mandriva.org> 1.10-1mdk
- New release 1.10

* Fri Aug 12 2005 Austin Acton <austin@mandrake.org> 1.00-1mdk
- initial package

