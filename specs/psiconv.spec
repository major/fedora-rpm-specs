Name:		psiconv
Version:	0.9.8
Release:	47%{?dist}
Summary:	A conversion utility for Psion files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://software.frodo.looijaard.name/psiconv/
Source0:	http://software.frodo.looijaard.name/psiconv/files/%{name}-%{version}.tar.gz
Patch0:	psiconv-0.9.8-gcc10.patch
Patch1: psiconv-checkuid-stdlib.h
Patch2: psiconv-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	ImageMagick-devel
BuildRequires:	bc

%description
A conversion utility for the Psion files

%package devel
Summary:	Development files for psiconv
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Contains library and header files for psiconv

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_datadir}/%{name} _doc


%ldconfig_scriptlets


%files
%doc COPYING NEWS README TODO ChangeLog AUTHORS 
%dir %{_sysconfdir}/psiconv
%config %{_sysconfdir}/psiconv/psiconv.conf 
%config %{_sysconfdir}/psiconv/psiconv.conf.eg
%{_bindir}/psiconv
%{_mandir}/man1/psiconv.1.gz
%{_libdir}/libpsiconv.so.6
%{_libdir}/libpsiconv.so.6.4.2


%files devel
%doc _doc/*
%{_bindir}/psiconv-config
%{_mandir}/man1/psiconv-config.1.gz
%{_libdir}/libpsiconv.so
#%{_datadir}/psiconv/
%{_includedir}/psiconv/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.8-46
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.9.8-40
- Rebuild for ImageMagick 7

* Wed Dec  7 2022 Florian Weimer <fweimer@redhat.com> - 0.9.8-39
- Port to C99 (#2151481)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.8-36
- Rebuild against new ImageMagick

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Than Ngo <than@redhat.com> - 0.9.8-32
- Fixed FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.8-28
- Add BuildRequires: gcc-c++, fixes FTBFS (#1605513)

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 0.9.8-27
- Rebuild for new ImageMagick 6.9.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.8-25
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Kevin Fenzi <kevin@scrye.com> - 0.9.8-22
- Rebuild for new ImageMagick

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-15
- ImageMagick 6.8.8.10-3 rebuild.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Kevin Fenzi <kevin@scrye.com> - 0.9.8-13
- Rebuild for broken deps in rawhide

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Tom Callaway <spot@fedoraproject.org> - 0.9.8-10
- rebuild for new ImageMagick

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.9.8-7
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.8-6
- rebuild for new ImageMagick

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 14 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.9.8-4
- Rebuild for new ImageMagick soname

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.8-2
- Include unowned /etc/psiconv directory.
- Add missing defattr to -devel pkg.

* Wed Apr 16 2008 Huzaifa Sidhpurwala <huzaifas@fedoraproject.org> - 0.9.8-1
- Made changes to %%doc, license, added BR 

* Wed Apr 16 2008 Huzaifa Sidhpurwala <huzaifas@fedoraproject.org> - 0.9.8-0
- Initial Build
