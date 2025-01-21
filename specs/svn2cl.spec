Name:           svn2cl
Version:        0.14
Release:        22%{?dist}
Summary:        Create a ChangeLog from a Subversion log

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://arthurdejong.org/svn2cl/
Source0:        http://arthurdejong.org/svn2cl/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       libxslt
Requires:       subversion
Provides:       subversion-svn2cl = 1.7.0
Obsoletes:      subversion-svn2cl < 1.7.0

%description
svn2cl is a simple XSL transformation and shell script wrapper for
generating a classic GNU-style ChangeLog from a subversion repository
log.  It is made from several change log -like scripts using common
XSLT constructs found in different places.


%prep
%setup -q
sed -i -e 's|^XSL="$dir/|XSL="%{_datadir}/svn2cl/|' svn2cl.sh


%build


%install
install -Dpm 755 svn2cl.sh $RPM_BUILD_ROOT%{_bindir}/svn2cl
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/svn2cl
install -pm 644 *.xsl $RPM_BUILD_ROOT%{_datadir}/svn2cl
install -Dpm 644 svn2cl.1 $RPM_BUILD_ROOT%{_mandir}/man1/svn2cl.1


%files
%doc ChangeLog NEWS README TODO authors.xml svn2html.css
%{_bindir}/svn2cl
%{_datadir}/svn2cl/
%{_mandir}/man1/svn2cl.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.14-1
- New upstream version
- BZ #1008425

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.13-2
- Provide subversion-svn2cl.

* Wed Oct 12 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.13-1
- Update to 0.13, obsolete subversion-svn2cl.
- Specfile cleanups.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.11-1
- 0.11.

* Sun Apr  6 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.10-1
- 0.10, drop disttag.

* Sun Apr  8 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9-1
- 0.9.

* Thu Oct 19 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.8-1
- 0.8.
- Add (empty) %%build section.

* Fri Sep 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7-2
- Rebuild.

* Fri Jun  2 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7-1
- 0.7.

* Fri Apr  7 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.6-1
- First FE build (#186632).

* Thu Mar 23 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.6-0.1
- First build.
