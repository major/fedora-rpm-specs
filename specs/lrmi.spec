Name:           lrmi
Version:        0.10
Release:        36%{?dist}
Summary:        Library for calling real mode BIOS routines

License:        MIT
URL:            http://sourceforge.net/projects/lrmi/
Source0:        http://download.sourceforge.net/lrmi/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.9-build.patch
Patch1:         lrmi-0.10-newheaders.patch
BuildRequires:  kernel-headers
BuildRequires:  gcc
BuildRequires: make

ExclusiveArch:  %{ix86}
Provides:       lib%{name} = %{version}-%{release}

%description
LRMI is a library for calling real mode BIOS routines.

%package        devel
Summary:        Development files for LRMI
Requires:       %{name} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}

%description    devel
%{summary}.

%package     -n vbetest
Summary:        Utility for listing and testing VESA graphics modes

%description -n vbetest
%{summary}.


%prep
%setup -q
%patch -P0
%patch -P1 -p1 -b .new-headers


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" liblrmi.so vbetest


%install
rm -rf $RPM_BUILD_ROOT
make install \
  LIBDIR=$RPM_BUILD_ROOT%{_libdir} INCDIR=$RPM_BUILD_ROOT%{_includedir}
install -Dpm 755 vbetest $RPM_BUILD_ROOT%{_sbindir}/vbetest



%ldconfig_scriptlets


%files
%doc README
%{_libdir}/liblrmi.so.*

%files devel
%{_includedir}/lrmi.h
%{_includedir}/vbe.h
%{_libdir}/liblrmi.so

%files -n vbetest
%{_sbindir}/vbetest


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 0.10-22
- Fix FTBFS bug #1604742

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10-5
- fix compile against modern kernel headers
- add BR: kernel-headers

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 0.10-4
- Rebuild for gcc43

* Sun Aug 26 2007 Kevin Fenzi <kevin@tummy.com> - 0.10-3
- Rebuild for BuildID

* Sun Aug 27 2006 Kevin Fenzi <kevin@tummy.com> - 0.10-2
- Rebuild for fc6

* Sun Mar 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.10-1
- 0.10, asm patch applied upstream.

* Sun Dec  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9-2
- Fix build with new binutils.

* Wed Nov  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9-1
- 0.9, patches mostly applied/obsoleted upstream.
- Don't ship static libraries.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.8-2
- rebuilt

* Fri Jul 23 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8-0.fdr.1
- First build.
