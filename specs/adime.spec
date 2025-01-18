Name:           adime
Version:        2.2.1
Release:        41%{?dist}
Summary:        Allegro Dialogs Made Easy
License:        zlib
URL:            http://adime.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         adime-2.2.1-so-fixes.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel texinfo
BuildRequires: make

%description
Adime is a portable add-on library for Allegro with functions for generating
Allegro dialogs in a very simple way. Its main purpose is to give as easy an
API as possible to people who want dialogs for editing many kinds of input
data.


%package devel
Summary: Development libraries and headers for adime
Requires: %{name} = %{version}-%{release}
Requires: allegro-devel

%description devel
The developmental files that must be installed in order to compile
applications which use adime.


%prep
%setup -q
%patch -P0 -p1 -z .so-fixes
./fix.sh unix
rm docs/txt/tmpfile.txt
mkdir docs/html docs/rtf


%build
make %{?_smp_mflags} lib docs \
  CFLAGS="-fPIC -DPIC $RPM_OPT_FLAGS" \
  CFLAGS_NO_OPTIMIZE="-fPIC -DPIC $RPM_OPT_FLAGS" \
  LFLAGS=-g


%install
make install install-man install-info \
  SYSTEM_DIR=$RPM_BUILD_ROOT/usr \
  SYSTEM_LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
  SYSTEM_MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
  SYSTEM_INFO_DIR=$RPM_BUILD_ROOT%{_infodir}
rm $RPM_BUILD_ROOT%{_infodir}/dir
ln -s libadime.so.0 $RPM_BUILD_ROOT%{_libdir}/libadime.so


%ldconfig_scriptlets

%files
%doc license.txt thanks.txt changes.txt
%{_libdir}/libadime.so.0

%files devel
%doc readme.txt docs/txt/*.txt docs/rtf docs/html
%{_includedir}/adime.h
%{_includedir}/adime
%{_libdir}/libadime.so
%{_mandir}/man3/*
%{_infodir}/adime.info.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 2.2.1-27
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 14 2013 Hans de Goede <hdegoede@redhat.com> - 2.2.1-16
- Fix Source0 URL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Hans de Goede <hdegoede@redhat.com> - 2.2.1-11
- Rebuilt for new allegro-4.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.1-7
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.1-6
- Rebuild for buildId

* Thu Aug  2 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.1-5
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.1-4
- FE6 Rebuild

* Sun Mar 12 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.1-3
- change license to "zlib License"
- modify adime-2.2.1-so-fixes.patch to strip -lalleg_unshareble from
  allegro-config --libs output instead of using a hardcoded allegro linkerflag

* Sun Mar 12 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.1-2
- add BR texinfo
- mkdir docs/html and docs/rtf during %%prep to make "make docs" happy, include
  the results in %%doc
- don't link liballeg_unsharable.a into our .so.0 file

* Sat Mar 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.1-1
- Initial Fedora Extras package
