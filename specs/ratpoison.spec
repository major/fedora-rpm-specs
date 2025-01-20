%global xsessiondir %{_datadir}/xsessions

Name:           ratpoison
Version:        1.4.9
Release:        28%{?dist}
Summary:        Minimalistic window manager
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/ratpoison/
Source0:        http://download.savannah.gnu.org/releases/ratpoison/ratpoison-%{version}.tar.xz
Source1:	%{name}.desktop
BuildRequires: make
BuildRequires:  gcc, texinfo
BuildRequires: libXft-devel, libX11-devel, perl-generators, readline-devel, libXt-devel, libXinerama-devel, libXtst-devel, libXi-devel, libXrandr-devel
BuildRequires:  emacs
Requires:       emacs-filesystem >= %{_emacs_version}

%description
Ratpoison is a simple window manager that relies solely on keyboard input as
opposed to keyboard and mouse input.

%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS -DHAVE_GETLINE"
%configure --disable-dependency-tracking
make %{?_smp_mflags}


%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{xsessiondir}
install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{xsessiondir}/
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/allwindows.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/clickframe.pl
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/genrpbindings
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpshowall.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpws
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/split.sh

%files
%{_bindir}/ratpoison
%{_bindir}/rpws
%doc %{_datadir}/doc/ratpoison/
%{_infodir}/ratpoison.info.*
%{_mandir}/man1/ratpoison.1.gz
%{_datadir}/ratpoison/
%{_datadir}/xsessions/ratpoison.desktop
%{_emacs_sitelispdir}/*.el

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.9-27
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Kevin Fenzi <kevin@scrye.com> - 1.4.9-17
- Fix FTBFS bug. Fixes rhbz#1865362

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.4.9-12
- Remove hardcoded gzip suffix from GNU info pages

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Kevin Fenzi <kevin@scrye.com> - 1.4.9-6
- Update to 1.4.9. Fixes bug #1438629

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4.8-5
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Kevin Fenzi <kevin@scrye.com> - 1.4.8-3
- Fix define vs global

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Kevin Fenzi <kevin@scrye.com> 1.4.8-1
- Update to 1.4.8. Fixes bug #1221160

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4.6-2
- Perl 5.18 rebuild

* Tue Jul 09 2013 Kevin Fenzi <kevin@scrye.com> 1.4.6-1
- Update to 1.4.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.5-1
- Update to 1.4.5

* Tue Jul 14 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.4-4
- Add libXi-devel to BuildRequires

* Tue Jun 16 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.4-3
- Rebuild again now that bug #505774 is fixed. 

* Fri Jun 12 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.4.4-2
- Build with $RPM_OPT_FLAGS.
- Disable autotools dependency tracking for cleaner build logs and possible
  slight build speedup.

* Thu May 14 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.4-1
- Update to 1.4.4
- Add libXft-devel to BuildRequires

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.1-2
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 John Berninger <john at ncphotography dot com> - 1.4.1-1
- rebuild for deps

* Fri Aug 31 2007 John Berninger <john at ncphotography dot com> - 1.4.1-0
- update to 1.4.1 - bz 269821

* Sun Sep 10 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-5
- Mass rebuild of FC/FE6

* Tue Apr 11 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-4
- BuildRequires fixes for FC-devel (FC-6)

* Sat Apr  8 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-3
- Permissions fixes

* Sat Apr  8 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-2
- install-info fixup
- BuildRequires fixup

* Fri Apr  7 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-1
- Bumped to 1.4.0-1 from 1.3.0-2
- Conditional BuildRequires for FC4-- versus FC5++
- Various fixes per bugzilla review

* Mon Mar 13 2006 John Berninger <johnw at berningeronline dot net> - 1.3.0-2
- Added ratpoison.desktop file

* Sun Feb 19 2006 John Berninger <johnw at berningeronline dot net> - 1.3.0-1
- Initial specfile build for FE(4)
