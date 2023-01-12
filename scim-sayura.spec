Name:		scim-sayura
Version:	0.3.0
Release:	32%{?dist}
Summary:	Sri Lankan input method for SCIM
License:	GPLv2
URL:		http://sinhala.sourceforge.net/
Source:		http://sinhala.sourceforge.net/files/%{name}-%{version}.tar.gz
Patch0:         scim-sayura-0.3.0-fix-constructor.patch
Patch1:         scim-sayura-aarch64.patch
Patch2: scim-sayura-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	scim-devel
Requires:	scim

%description
This package provides a Sinhala Trans input method for SCIM.


%prep
%setup -q 
%patch0 -p1 -b .fix-constructor
%patch1 -p1 -b .aarch64-support
%patch2 -p1

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%files
%doc README AUTHORS
%license COPYING
%{_libdir}/scim-1.0/*/IMEngine/sayura.so
%{_datadir}/scim/icons/scim-sayura.png


%changelog
* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 0.3.0-32
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-27
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Parag Nemade <pnemade AT fedoraproject.org> - 0.3.0-22
- Fix FTBFS(rh#1606314)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-14
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Pravin Satpute <psatpute AT redhat.com> - 0.3.0-10
- Resolves #926497 - aarch64 support

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 07 2010 Parag Nemade <paragn AT fedoraproject.org> - 0.3.0-5
- Fix FTBFS 
- Drop provides and obsoletes 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 11 2008 Pravin Satpute <psatpute@redhat.com> - 0.3.0-2
- convert scim-sinhala into scim-sayura

* Fri May 16 2008 Pravin Satpute <psatpute@redhat.com> - 0.3.0-1
- update to scim-sayura 0.3.0 from upstream
- upated spec file as per new tarball

* Mon Feb 11 2008 Pravin Satpute <psatpute@redhat.com> - 0.2.0-6
- Rebuild for gcc 4.3

* Tue Jan 08 2008 Pravin Satpute <psatpute@redhat.com> - 0.2.0-5
- removed preedit for unneccessary characters(#217065)
- modified scim-sinhala-preedit-217065.patch

* Fri Dec 14 2007 Pravin Satpute <psatpute@redhat.com> - 0.2.0-4
- implemented preedit in scim sinhala(#217065)

* Wed Aug 22 2007 Parag Nemade <pnemade@redhat.com> - 0.2.0-3
- rebuild against new rpm package
- update license tag

* Thu Sep 28 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-2
- add scim-sinhala-remove-timeout-206253.patch to remember previous key event
  for longer than a second (#206253)
- add scim-sinhala-help-text-206114.patch to add some keymap help (#206114)

* Mon Aug 28 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-1
- update to scim-sinhala-trans 0.2.0 from new upstream cvs
- no longer uses surrounding text (#200403)
- update url and spec file
- add scim-sinhala-trans-autogen-automake.patch to build with current automake

* Wed Jul 26 2006 Jens Petersen <petersen@redhat.com> - 0.1.0-3
- remove redundant po files

* Wed Jul 26 2006 Jens Petersen <petersen@redhat.com> - 0.1.0-2
- add .so suffix to IME module filename

* Wed Jul 26 2006 Jens Petersen <petersen@redhat.com> - 0.1.0-1
- package for Fedora

* Thu Sep  8 2005 Jens Petersen <petersen@redhat.com> - 0.0.0-0
- initial packaging
