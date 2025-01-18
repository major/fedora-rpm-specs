Summary:        Archiver for .arj files
Name:           arj
Version:        3.10.22
Release:        43%{?dist}
License:        GPL-2.0-or-later
URL:            https://arj.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# unarj.* from Debian
Source1:        unarj.sh
Source2:        unarj.1
Patch0:         arj-3.10.22-arches_align.patch
Patch1:         arj-3.10.22-no_remove_static_const.patch
Patch2:         arj-3.10.22-64_bit_clean.patch
Patch3:         arj-3.10.22-parallel_build.patch
Patch4:         arj-3.10.22-use_safe_strcpy.patch
Patch5:         arj-3.10.22-doc_refer_robert_k_jung.patch
Patch6:         arj-3.10.22-security_format.patch
Patch7:         arj-3.10.22-missing-protos.patch
Patch8:         arj-3.10.22-custom-printf.patch
# Filed into upstream bugtracker as https://sourceforge.net/tracker/?func=detail&aid=2853421&group_id=49820&atid=457566
Patch9:         arj-3.10.22-quotes.patch
Patch10:        arj-3.10.22-security-afl.patch
Patch11:        arj-3.10.22-security-traversal-dir.patch
Patch12:        arj-3.10.22-security-traversal-symlink.patch
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  make
Provides:       unarj = %{version}-%{release}
Obsoletes:      unarj < 3

%description
This package is an open source version of the arj archiver. It has
been created with the intent to preserve maximum compatibility and
retain the feature set of original ARJ archiver as provided by ARJ
Software, Inc.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1

pushd gnu
  autoconf
popd

%build
pushd gnu
  %configure
popd

# Disable binary strippings
%make_build ADD_LDFLAGS=""

%install
%make_install

install -D -p -m 644 resource/rearj.cfg.example $RPM_BUILD_ROOT%{_sysconfdir}/rearj.cfg
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/unarj
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/unarj.1

# remove the register remainders of arj's sharewares time
rm -f $RPM_BUILD_ROOT%{_bindir}/arj-register
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/arj-register.1*

%files
%license doc/COPYING
%doc ChangeLog* doc/rev_hist.txt
%config(noreplace) %{_sysconfdir}/rearj.cfg
%{_bindir}/*arj*
%{_libdir}/arj/
%{_mandir}/man1/*arj*.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.22-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 03 2015 Robert Scheck <robert@fedoraproject.org> 3.10.22-22
- Added patch from Debian to avoid free on invalid pointer due to a
  buffer overflow (#1196751, #1207180)
- Added patch from Debian for symlink directory traversal (#1178824)
- Added patch from Debian to fix the directory traversal via
  //multiple/leading/slash (#1178824)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 3.10.22-21
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 20 2013 Robert Scheck <robert@fedoraproject.org> 3.10.22-18
- Replaced compressed Debian patch file by regular patches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 3.10.22-12
- Re-enable parallel builds again now that quoting is fixed

* Sun Sep  6 2009 Milos Jakubicek <xjakub@fi.muni.cz> 3.10.22-11
- Fix FTBFS: added arj-3.10.22-quotes.patch

* Wed Aug 19 2009 Robert Scheck <robert@fedoraproject.org> 3.10.22-10
- Disabled the even with patches broken parallel builds again

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Robert Scheck <robert@fedoraproject.org> 3.10.22-8
- Added patch to disable the custom printf to avoid conflicting
  strnlen definition with glibc headers (thanks to Lubomir Rintel)

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 3.10.22-7
- Rebuild against gcc 4.4 and rpm 4.6

* Mon Sep 08 2008 Robert Scheck <robert@fedoraproject.org> 3.10.22-6
- Added patch to refer to original author in the manual page
- Added patch to support parallel builds in upstream Makefile

* Sat Aug 30 2008 Robert Scheck <robert@fedoraproject.org> 3.10.22-5
- Corrected from %%patch to %%patch0 to make rpm > 4.4 happy

* Mon Mar 31 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 3.10.22-4
- Fix missing prototype compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.10.22-3
- Autorebuild for GCC 4.3

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.10.22-2
- Update License tag for new Licensing Guidelines compliance

* Sat Sep  9 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.10.22-1
- initial FE submission based on a src.rpm by Ville Skyttä
