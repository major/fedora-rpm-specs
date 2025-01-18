Name:           dumb
Version:        0.9.3
Release:        44%{?dist}
Summary:        IT, XM, S3M and MOD player library
License:        zlib
URL:            http://dumb.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-autotools.tar.gz
Source2:        license-clarification.eml
Patch0:         dumb-0.9.3-CVE-2006-3668.patch
Patch1:         dumb-0.9.3-license-clarification.patch
Patch2:         dumb-0.9.3-weak-symbols.patch
Patch3:         dumb-configure-c99.patch
BuildRequires:  make gcc gcc-c++
BuildRequires:  allegro-devel

%description
IT, XM, S3M and MOD player library. Mainly targeted for use with the allegro
game programming library, but it can be used without allegro. Faithful to the
original trackers, especially IT.


%package devel
Summary: Development libraries and headers for dumb
Requires: %{name} = %{version}
Requires: allegro-devel

%description devel
The developmental files that must be installed in order to compile
applications which use dumb.


%prep
%setup -q -b 01
%patch -P0 -p1 -z .cve-2006-3668
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
cp %{SOURCE2} .


%build
%configure
# Remove useless /usr/lib64 rpath on 64bit archs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} LIBS=-lm


%install
%make_install
#clean out .la and static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
%doc release.txt readme.txt
%license licence.txt license-clarification.eml
%{_bindir}/dumb*
%{_libdir}/lib*-%{version}.so

%files devel
%doc docs/deprec.txt docs/dumb.txt docs/faq.txt docs/fnptr.txt docs/howto.txt docs/ptr.txt
%{_includedir}/*.h
%{_libdir}/libdumb.so
%{_libdir}/libaldmb.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Florian Weimer <fweimer@redhat.com> - 0.9.3-39
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Hans de Goede <hdegoede@redhat.com> - 0.9.3-35
- Remove rpath, fixing FTBFS (rhbz#1987430)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.9.3-28
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.3-17
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Wed May  1 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.3-16
- run autoreconf for aarch64 support (rhbz#925281)
- fix unresolved weak symbols in libaldmb

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Hans de Goede <hdegoede@redhat.com> - 0.9.3-12
- Rebuilt for new allegro-4.4

* Tue Mar 08 2011 Hans de Goede <hdegoede@redhat.com> - 0.9.3-11
- Fix unresolved symbols from libm in the libraries

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.3-7
- Autorebuild for GCC 4.3

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-6
- Clarify license after talking about it with upstream
- Include permission notice from upstream for license clarification
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-5
- FE6 Rebuild

* Thu Jul 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-4
- Fix CVE-2006-3668, thanks to Debian for the patch

* Wed Mar 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-3
- Add Requires: allegro-devel to -devel package

* Thu Mar 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-2
- Drop modplug.txt from %%doc and move release.txt and readme.txt from the
 -devel package to the main package (bz 185576).

* Fri Jan 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-1
- Initial Fedora Extras package
