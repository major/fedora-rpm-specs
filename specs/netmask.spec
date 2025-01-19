Name:           netmask
Version:        2.4.4
Release:        15%{?dist}
Summary:        Utility for determining network masks

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/tlby/netmask
Source0:        https://github.com/tlby/netmask/archive/v%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc, automake, texinfo

%description
This is a handy tool for generating terse netmasks in several common
formats.  If you've ever maintained a firewall with more than a few
rules in it, you might use netmask to clean up and generalize sloppy
rules left by the network administrator before you.  It will also
convert netmasks from one format to another for the day you change
your firewall software.


%prep
%autosetup -a 0
./autogen  

%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%check
make check

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/netmask
%{_mandir}/man1/netmask.1*
%exclude %{_infodir}/dir
%{_infodir}/netmask.info*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.4-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.4.4-1
- Security bugfix buffer overflow reported at upstream 2019-01-30; updated sources

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.4.3-7
- Added gcc and texinfo to build requirements

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.4.3-1
- Update to 2.4.3

* Sat Oct  3 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.4.2-1
- Update to 2.4.2, specfile cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.3.12-9
- Ship COPYING as %%license where available

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jun  7 2014 Ville Skyttä <ville.skytta@iki.fi>
- Specfile cleanups

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 10 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.3.12-1
- Update to 2.3.12 (#590609), info dir entry patch applied upstream.

* Wed Mar 10 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.3.11-1
- Update to 2.3.11.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 16 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.3.10-1
- 2.3.10.

* Sat Feb  9 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.3.9-3
- Rebuild.

* Mon Aug  6 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.3.9-2
- License: GPLv2+

* Mon Mar 26 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.3.9-1
- 2.3.9.

* Wed Oct 11 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.3.8-1
- 2.3.8.

* Sat Sep  2 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.3.7-6
- Rebuild.

* Thu Feb 16 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.3.7-5
- Rebuild.

* Thu May 19 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.3.7-4
- Rebuild.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.3.7-3
- rebuilt

* Mon Jun 21 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:2.3.7-0.fdr.2
- Split install-info dep into post and preun.
- Run tests in the %%check section.
- Change URL.

* Sat Sep 27 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:2.3.7-0.fdr.1
- Update to 2.3.7.

* Tue Jul  8 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:2.3.6-0.fdr.1
- First build.
