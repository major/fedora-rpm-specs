%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%(echo 'puts $tcl_version' | tclsh)}

Name:           tdom
Version:        0.8.2
Release:        40%{?dist}
Summary:        DOM parser for Tcl

# Most files MPL except for ./generic/xmlsimple.c and ./generic/domhtml.c
# which are LGPLV2+.
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.tdom.org
Source0:        http://www.tdom.org/files/tDOM-%{version}.tgz
Patch0:         tdom-0.8.2-noexpat.patch
Patch1:         tdom-0.8.2-tcl8.6.patch
Patch2:         tdom-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  tcl-devel expat-devel
Requires:       tcl(abi) = 8.6

%description
tDOM combines high performance XML data processing with easy and powerful Tcl
scripting functionality. tDOM should be one of the fastest ways to manipulate
XML with a scripting language and uses very little memory.

%package devel
Summary: Development files for compiling against tdom
Requires:       %{name} = %{version}-%{release} expat-devel
%description devel
Development header files for compiling against tdom.

%prep
%setup -q -n tDOM-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%configure --enable-threads
make %{?_smp_mflags}

rm -rf expat

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{name}%{version}/*.so %{buildroot}%{_libdir}
mv %{buildroot}%{_libdir}/%{name}%{version}/*.a %{buildroot}%{_libdir}
mv %{buildroot}%{_libdir}/%{name}%{version} %{buildroot}%{tcl_sitearch}

# Adjust some paths to reflect the new file locations
sed -i -e 's/file join $dir libtdom/file join $dir .. .. libtdom/' %{buildroot}%{tcl_sitearch}/%{name}%{version}/pkgIndex.tcl

sed -i -e "s#%{_libdir}/%{name}%{version}#%{_libdir}#" %{buildroot}%{_libdir}/tdomConfig.sh

%files
%doc README LICENSE CHANGES ChangeLog doc/*.html NPL-1_1Final.html
%{tcl_sitearch}/%{name}%{version}
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%{_mandir}/mann/*.gz

%files devel
%{_libdir}/%{name}Config.sh
# This static library is a 'stub' library that is used to assist with
# shared lib linking across library versions:  http://wiki.tcl.tk/285
%{_libdir}/*.a
%{_includedir}/*.h


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.2-39
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Florian Weimer <fweimer@redhat.com> - 0.8.2-34
- Remove implicit function declarations from configure script

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 0.8.2-19
- Real expat cutoff (foggot one line in prev commit :( ).

* Tue Jul 07 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 0.8.2-18
- Better expat cutoff.
- Spec cleanup: drom buildroot definition, clean section, defatr tag, buildroot clean in install section.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 0.8.2-14
- Fix for tcl-8.6.

* Fri May 30 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 0.8.2-13
- Changed requires to require tcl-8.6.

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 4 2008 Wart <wart at kobold.org> - 0.8.2-4
- Change installation directory for faster loading

* Sat Feb 9 2008 Wart <wart at kobold.org> - 0.8.2-3
- Rebuild for gcc 4.3

* Sun Sep 23 2007 Wart <wart at kobold.org> - 0.8.2-2
- Added missing linkage against -lexpat

* Sun Aug 26 2007 Wart <wart at kobold.org> - 0.8.2-1
- Update to 0.8.2
- Split into base and -devel packages
- License tag clarification

* Tue May 1 2007 Wart <wart at kobold.org> - 0.8.0-2
- Updated patch 1 to add $RPM_OPT_FLAGS to the compiler flags
- Add --enable-threads to match the configuration of the core Tcl package

* Sat Nov 25 2006 Wart <wart at kobold.org> - 0.8.0-1
- Initial package for Fedora
