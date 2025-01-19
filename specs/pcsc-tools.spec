Name:           pcsc-tools
Version:        1.7.0
Release:        6%{?dist}
Summary:        Tools to be used with smart cards and PC/SC

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pcsc-tools.apdu.fr/
Source0:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2
Source1:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2.asc
Source2:        https://pcsc-tools.apdu.fr/smartcard_list.txt
Source3:        LICENCE

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  pcsc-lite-devel >= 1.2.9
BuildRequires:  perl-generators
BuildRequires:  gettext
Requires:       pcsc-lite

%description
The pcsc-tools package contains some useful tools for a PC/SC user:
pcsc_scan regularly scans connected PC/SC smart card readers and
prints detected events, ATR_analysis analyzes smart card ATRs (Anwser
To Reset), and scriptor sends commands to a smart card.

%package gscriptor
Summary:        GUI tool to send command to a smart card
Requires:       %{name} = %{version}-%{release}

%description gscriptor
The pcsc-tools-gscriptor package contains graphical tool gscriptor which
can send commands to a smart card. It has GTK user interface.


%prep
%setup -q
[ -f LICENCE ] || cp -a %{SOURCE3} LICENCE
cp -a %{SOURCE2} smartcard_list.txt


%build
%configure
make %{?_smp_mflags} CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --mode=644 \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications gscriptor.desktop
# TODO: icon
%find_lang %{name}

%files -f %{name}.lang
%license LICENCE
%doc Changelog README
%{_bindir}/ATR_analysis
%{_bindir}/pcsc_scan
%{_bindir}/scriptor
%{_datadir}/pcsc/
%{_mandir}/man1/ATR_analysis.1*
%{_mandir}/man1/pcsc_scan.1*
%{_mandir}/man1/scriptor.1*

%files gscriptor
%license LICENCE
%{_bindir}/gscriptor
%{_mandir}/man1/gscriptor.1*
%{_datadir}/applications/*gscriptor.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.0-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 08 2023 Jakub Jelen <jjelen@redhat.com> - 1.7.0-1
- New upstream release (#2242731)
- Add support for locale files

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Jakub Jelen <jjelen@redhat.com> - 1.6.2-1
- New upstream release (#2165783)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Jakub Jelen <jjelen@redhat.com> - 1.6.1-1
- New upstream release (#2156953)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 31 2022 Jakub Jelen <jjelen@redhat.com> - 1.6.0-1
- New upstream release (#2048150)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Jakub Jelen <jjelen@redhat.com> - 1.5.8-1
- New upstream release and updated smartcard list (#2020954)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tomáš Mráz <tmraz@redhat.com> - 1.5.7-1
- New upstream version 1.5.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Jakub Jelen <jjelen@redhat.com> - 1.5.4-1
- New upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep  5 2018 Tomáš Mráz <tmraz@redhat.com> - 1.5.3-1
- upgrade to the current upstream version 1.5.3
- move gscriptor to a subpackage (#1605277)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Tomáš Mráz <tmraz@redhat.com> - 1.5.2-1
- upgrade to the current upstream version 1.5.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 26 2016 Tomáš Mráz <tmraz@redhat.com> - 1.4.25-1
- upgrade to a latest upstream version
- include latest smartcard_list.txt (#1308753)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Tomáš Mráz <tmraz@redhat.com> - 1.4.23-1
- upgrade to a latest upstream version
- include latest smartcard_list.txt (#1183327)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4.17-7
- Perl 5.18 rebuild

* Fri Mar 01 2013 Jon Ciesla <limburgher@gmail.com> - 1.4.17-6
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep  7 2010 Tomas Mraz <tmraz@redhat.com> - 1.4.17-1
- upgrade to a latest upstream version

* Tue Apr 13 2010 Tomas Mraz <tmraz@redhat.com> - 1.4.16-1
- upgrade to a latest upstream version

* Tue Aug 11 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.15-1
- upgrade to a latest upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun  5 2008 Tomas Mraz <tmraz@redhat.com> - 1.4.14-1
- upgrade to a latest upstream version

* Sat Feb 16 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.4.12-1
- 1.4.12.

* Wed Aug 22 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.10-1
- 1.4.10, desktop entry patch applied upstream.

* Tue Aug  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.9-2
- License: GPLv2+

* Sat Jun 30 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.9-1
- 1.4.9.
- Drop Encoding key from desktop entry.

* Sun Nov 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.8-1
- 1.4.8.
- Drop X-Fedora desktop entry category.

* Sun Oct  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.7-1
- 1.4.7, Oct 8 smartcard_list.txt.

* Sat Sep  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.6-1
- 1.4.6, Aug 30 smartcard_list.txt.
- Drop pcsc-lite < 1.2.9 support.

* Mon May  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.5-1
- 1.4.5.

* Sat Mar 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.4-1
- 1.4.4.

* Thu Mar  9 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.3-1
- 1.4.3.
- Improve description.

* Wed Mar  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.2-1
- 1.4.2, desktop file, recent smartcard_list.txt, ATR_analysis message
  patch and smartcard_list.txt lookup path improvement included upstream.

* Mon Mar  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-3
- Update smartcard_list.txt to 20060305.
- Fix some ATR_analysis messages.

* Sat Feb 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-2
- Update smartcard_list.txt to 20060205.

* Tue Dec 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-1
- Update smartcard_list.txt to 20051127 and convert it to UTF-8.
- Improve summary and description.
- Add "Application" desktop entry category for legacy distros.
- Drop BR: sed.

* Sat Oct 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-0.2
- Update smartcard_list.txt to 20051011.
- Specfile cleanups.

* Wed Oct  5 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-0.1
- 1.4.1, patched to compile with pcsc-lite < 1.2.9-beta4.
- Move smartcard_list.txt to %%{_datadir}/pcsc.
- Add menu entry for gscriptor.

* Sat May 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.3-0.1
- Rebuild for FC4.

* Thu Jul  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.3-0.fdr.4
- Requires pcsc-lite (not too useful without the daemon).
- Update smartcard_list.txt to 1.72.

* Thu May 27 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.3-0.fdr.3
- Due to use of pkg-config, BuildRequires pcsc-lite-devel >= 1.2.0 (bug 1282).
- Update smartcard_list.txt to 1.71 (bug 1282).

* Wed May 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.3-0.fdr.2
- Patch to get PC/SC Lite CFLAGS and libs from pkg-config.
- Update smartcard_list (1.70).

* Fri Apr  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.3-0.fdr.1
- Update to 1.3.3.

* Tue Feb 10 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.2-0.fdr.2
- Update smartcard_list (1.64).

* Wed Dec 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.2-0.fdr.1
- Update to 1.3.2.

* Thu Oct 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.1-0.fdr.1
- Update to 1.3.1.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.0-0.fdr.4
- Own %%{_libdir}/pcsc.
- Spec cleanups.

* Sun Aug 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.0-0.fdr.3
- Updated smartcard_list.txt (1.43).

* Wed Aug 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.0-0.fdr.2
- Spec cleanups.

* Sun Jun  1 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.0-0.fdr.1
- Update to 1.3.0.

* Sun May 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.5-0.fdr.1
- Update to 1.2.5.

* Fri May 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.4-0.fdr.1
- First build.
