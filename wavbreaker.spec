Summary:	Tool for splitting .wav files
Name:		wavbreaker
Version: 	0.10
Release: 	30%{?dist}
License: 	GPLv2+
URL: 		http://wavbreaker.sourceforge.net
Source: 	http://downloads.sourceforge.net/wavbreaker/%{name}-%{version}.tar.gz
Patch:		wavbreaker-0.8-desktop-file.patch
Patch1:		wavbreaker-0.10-format-security.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	gtk2-devel, libxml2-devel, desktop-file-utils, alsa-lib-devel
BuildRequires:	gettext
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils

%description
This application's purpose in life is to take a wave file and break it 
up into multiple wave files. It makes a clean break at the correct 
position to burn the files to an audio cd without any dead air between 
the tracks. It will only read wave files, so use an appropriate tool to 
convert ogg, mp3, etc. files and then break them up.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install INSTALL="install -p"
%find_lang %{name}

desktop-file-install               \
        --dir %{buildroot}%{_datadir}/applications  \
        --add-category X-OutputGeneration           \
        --delete-original                           \
        %{buildroot}%{_datadir}/applications/wavbreaker.desktop

%files -f %{name}.lang
%{_bindir}/wav*
%{_datadir}/applications/wavbreaker.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/wavbreaker.png
%{_mandir}/man*/wav*
%doc ChangeLog CONTRIBUTORS NEWS AUTHORS COPYING README TODO

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10-19
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.10-12
- Fix FTBFS with -Werror=format-security (#1037382, #1107132)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.10-9
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.10-6
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.10-4
- Update desktop file according to F-12 FedoraStudio feature

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun 5 2008 Homer <dmaley at nc.rr.com> - 0.10-1
- move to latest upstream release

* Fri May 23 2008 Todd Zullinger <tmz@pobox.com> - 0.9-4
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-3
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Homer <dmaley at nc.rr.com> 0.9-2
- bump release for F8 -> F9 upgrade path

* Tue Nov 20 2007 Homer <dmaley at nc.rr.com> 0.9-1
- move to latest upstream release

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.8.1-4
- Rebuild for selinux ppc32 issue.

* Tue Aug 28 2007 Homer <dmaley at nc.rr.com> 0.8.1-3
- bump rev for F-8 mass rebuild

* Fri Jul 6 2007 Homer <dmaley at nc.rr.com> 0.8.1-2
- new version 0.8.1

* Sun May 13 2007 Homer <dmaley at nc.rr.com> 0.8-1
- new version 0.8

* Tue Oct 3 2006 Homer <dmaley at nc.rr.com> 0.7-6
- added wavbreaker-tooltips.patch

* Thu Jun 1 2006 Homer <dmaley at nc.rr.com> 0.7-5
- replaced wavbreaker-0.7-browsedir-set_current_folder.patch w/ 
  wavbreaker-0.7-browsedir-set_current_folder-v2.patch

* Tue May 30 2006 Homer <dmaley at nc.rr.com> 0.7-4
- added wavbreaker-0.7-browsedir-set_current_folder.patch

* Mon Apr 3 2006 Homer <dmaley at nc.rr.com> 0.7-3
- fixed %%doc

* Tue Mar 21 2006 Homer <dmaley at nc.rr.com> 0.7-2
- added %%doc

* Mon Feb 27 2006 Homer <dmaley at nc.rr.com> 0.7-1
- initial 0.7 build

* Mon Feb 20 2006 Homer <dmaley at nc.rr.com> 0.7a-1
- initial 0.7a build

* Mon Jan 25 2006 Homer <dmaley at nc.rr.com> 0.6.1-6
- default to ALSA

* Mon Dec 19 2005 Homer <dmaley at nc.rr.com> 0.6.1-5
- more .spec cleanup

* Fri Dec 9 2005 Homer <dmaley at nc.rr.com> 0.6.1-4
- continued .spec cleanup

* Wed Dec 7 2005 Homer <dmaley at nc.rr.com> 0.6.1-3
- cleaned up .spec based on Fedora Extras guidelines

* Mon Sep 12 2005 Homer <homerj at nc.rr.com> 0.6-homer.2
- fixed progress bar for save-as (wavbreaker-saveas-progress.patch)

* Thu Jun 2 2005 Homer <homerj at nc.rr.com> 0.6-homer.1
- rebuilt for 0.6.1 (bugfix release)

* Wed Jun 1 2005 Homer <homerj at nc.rr.com> 0.6-homer.1
- 0.6 released

* Wed May 23 2005 Homer <homerj at nc.rr.com> 0.6c-homer.2
- 0.6c (beta) release

* Wed May 19 2005 Homer <homerj at nc.rr.com> 0.6b-homer.3
- SPEC file clean-up

* Sat Feb 12 2005 Homer <homerj at nc.rr.com> 0.6b-homer.2
- appconfig.c: added remember-driver patch

* Tue Feb 8 2005 Homer <homerj at nc.rr.com> 0.6b-homer.1
- 0.6b (beta) release
- Makefile.am: added -lasound to wavbreaker_LDADD to fix compile error

* Fri Oct 29 2004 Homer <homerj at nc.rr.com> 0.5-homer.2
- attempted fix file closing bug (wavbreaker-fclose.patch)
- added BuildRequires for gtk2-devel

* Tue Jul 13 2004 Homer <homerj at nc.rr.com> 0.5-homer.1
- rebuilt for 0.5 release

* Thu Jul 1 2004 Homer <homerj at nc.rr.com> 0.4-homer.4
- actually fixed icon bug

* Thu Jul 1 2004 Homer <homerj at nc.rr.com> 0.4-homer.2
- (failed) attempt to fix icon bug

* Mon Jun 15 2004 Homer <homerj at nc.rr.com>
- initial build
