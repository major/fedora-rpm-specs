%global pname   epgsearch
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

%global commit0  76d2b108bf17fde2a98e021c8bbfecb1a9a7e92e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20220201

# version we want build against
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-%{pname}
Version:        2.4.3
Release:        2%{?dist}
# Release:        0.12.%%{gitdate}git%%{shortcommit0}%%{?dist}
Summary:        Powerful schedules menu replacement plugin for VDR

License:        GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-epgsearch
Source0:        https://github.com/vdr-projects/vdr-plugin-epgsearch/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0:        %%url/archive/%%{commit0}/%%{name}-%%{commit0}.tar.gz#/%%{name}-%%{shortcommit0}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}-epgsearchonly.conf
Source3:        %{name}-conflictcheckonly.conf
Source4:        %{name}-quickepgsearch.conf
Source5:        %{name}-epgsearchmenu.conf
# Fedora specific, no need to send upstream
Patch0:         %{name}-2.4.0-fedora.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin provides a powerful replacement for VDR's default
schedules menu entry.  It looks like the standard schedules menu, but
adds several functions, such as additional commands for EPG entries,
reusable queries which can be used as dynamic "search timers" etc.

%prep
%setup -q -n vdr-plugin-%{pname}-%{version}
#%%setup -qn vdr-plugin-%{pname}-%%{commit0}
sed -e 's|__VARDIR__|%{vdr_vardir}|g' %{PATCH0} | %{__patch} -p1 --fuzz=0
for f in scripts/epgsearchcmds-french.conf conf/epgsearchcats.conf-tvm2vdr* ; do
    iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f ; mv $f.utf8 $f
done

chmod -x scripts/*

%build
%make_build AUTOCONFIG=0

%install
%make_install

install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
install -Dpm 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/epgsearchonly.conf
install -Dpm 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/conflictcheckonly.conf
install -Dpm 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/quickepgsearch.conf

install -pm 644 %{SOURCE5} \
  $RPM_BUILD_ROOT%{vdr_configdir}/plugins/epgsearch/epgsearchmenu.conf
rm $RPM_BUILD_ROOT%{vdr_configdir}/plugins/epgsearch/epgsearchcats.conf-* \
  $RPM_BUILD_ROOT%{vdr_configdir}/plugins/epgsearch/epgsearchupdmail-html.templ

install -dm 755 $RPM_BUILD_ROOT%{vdr_vardir}/epgsearch

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%license COPYING
%doc HISTORY conf/ scripts/
%lang(de) %doc HISTORY.DE
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/*.conf
%{_bindir}/createcats
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{_mandir}/man[145]/*.[145]*
%defattr(-,%{vdr_user},root,-)
%config(noreplace) %{vdr_configdir}/plugins/epgsearch/
%config(noreplace) %{vdr_vardir}/epgsearch/
%defattr(-,root,root,-)

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.3-1
- Rebuilt for new VDR API version 2.7.2
- Update to 2.4.3

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.2-0.14.20220201git76d2b10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.13.20220201git76d2b10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.12.20220201git76d2b10
- Rebuilt for new VDR API version 2.6.9

* Fri Jul 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.11.20220201git76d2b10
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.10.20220201git76d2b10
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.9.20220201git76d2b10
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.8.20220201git76d2b10
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.7.20220201git76d2b10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.6.20220201git76d2b10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.5.20220201git76d2b10
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.4.20220201git76d2b10
- Rebuilt for new VDR API version

* Thu Aug 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.3.20220201git76d2b10
- Update to new github address

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.2.20220201git76d2b10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-0.1.20220201git76d2b10
- Update for new git snapshot
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-4
- Rebuilt for new VDR API version

* Fri Dec 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-3
- Add %{name}-conflict_check.patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Mon Apr 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-18
- Rebuilt for new VDR API version

* Fri Feb 19 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-17
- Add %%{name}-conflictcheck.patch fixes (BZ#1930340)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-15
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-14
- Rebuilt for new VDR API version

* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 2.4.0-13
- Force C++14 as this code is not C++17 ready
- Avoid ordered pointer comparisons against zero

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Add patch menu_conflictcheck.patch to show device again in conflictcheck

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-8
- Fix setup line
- Spec file cleanup

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-7
- Rebuilt for new VDR API version

* Fri Apr 12 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-6
- Add Fix_possible_format_overflow_and_avoid_compiler_warning.patch

* Wed Apr 10 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-5
- Add replace_auto_ptr_with_unique_ptr.patch

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-3
- Rebuilt

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-0.14.beta5.5
- Update to vdr-2.4.0
- Adjust %%{name}-2.4.0-fedora.patch
- Remove unneeded patches

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.14.beta5.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.14.beta5.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.14.beta5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.14.beta5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb  6 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.14.beta5
- Apply upstream -std=c++11 and repeat summary check fixes

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.13.beta5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul  6 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.13.beta5
- Build with proper plugin build config, fixes LDFLAGS

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.12.beta5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-0.12.beta5.1
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.12.beta5
- Apply upstream fix for VDR >= 2.1.2
- Ship COPYING as %%license

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.11.beta5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.11.beta5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.11.beta5
- Rebuild

* Sat Mar 22 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.10.beta5
- Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.9.beta5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.9.beta5
- Update to 1.0.1.beta5.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.9.beta3
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.8.beta3
- Rebuild.

* Sun Mar 03 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.7.beta3
- Rebuild.

* Sun Feb 24 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.6.beta3
- Update to 1.0.1.beta3.

* Tue Feb 19 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.6.beta2
- Apply upstream patch for VDR >= 1.7.33.
- Fix bogus date in %%changelog.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.5.beta2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.5.beta2
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.4.beta2
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.3.beta2
- Rebuild.

* Wed Jun 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.2.beta2
- Rebuild.

* Tue Jun 12 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.1.beta2
- Update to 1.0.1.beta2.
- Drop SVDRP port migration scriptlet.

* Fri May 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-0.1.beta1
- Update to 1.0.1.beta1.

* Mon Mar 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-12
- Rebuild.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-11
- Rebuild.

* Tue Mar  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-10
- Apply upstream patch for VDR 1.7.25.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for c++ ABI breakage

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-8
- Rebuild.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-7
- Rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-5
- Rebuild.

* Thu Nov 17 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-4
- Rebuild.

* Mon Nov  7 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-3
- Set SVDRP port to 6419 in scripts and try to migrate config on upgrades
  if built for VDR >= 1.7.15.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-2
- Clean up specfile constructs no longer needed with Fedora or EL6+.

* Sun Sep 11 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-1
- Update to 1.0.0.

* Mon Sep  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.8.beta22
- Fix crash when editing searches.
- Clean up specfile to use macros from vdr-devel >= 1.6.0-41.
- Build with $RPM_LD_FLAGS.

* Wed Aug 31 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.7.beta22
- Update to 0.9.25.beta22.

* Tue May  3 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.7.beta21
- Install dummy epgsearchmenu.conf to auto-enable vdrsymbol-fonts icons.
- Drop %%defattr no longer needed with rpmbuild >= 4.4.

* Mon Feb 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.6.beta21
- Filter autogenerated plugin lib Provides (rpmbuild >= 4.9).

* Mon Feb 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.5.beta21
- Update to 0.9.25.beta21.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.25-0.5.beta20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.4.beta20
- Update to 0.9.25.beta20.

* Wed Jan  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.4.beta18
- Update to 0.9.25.beta18.
- Patch example scripts to match default Fedora config better.

* Sun Jun 20 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.4.beta17
- Update to 0.9.25.beta17; "long short text" patch applied upstream.

* Wed Mar 17 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.4.beta16
- Patch to fix max file name length overflow with long "short" texts.

* Mon Feb  1 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.3.beta16
- Update to 0.9.25.beta16; regexlib and Finnish patches applied upstream.

* Thu Oct 15 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.3.beta15
- Update to 0.9.25.beta15.
- Sendmail, regex includes and man section patches applied upstream.
- Point URL to English version of the project home page.

* Mon Aug  3 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.3.beta14
- Move many files that are not config ones but more like state data edited
  through the OSD from /etc to /var.
- Patch to use sendmail for sending mail by default.
- Require ISA qualified vdr(abi).
- Include sample config files in docs.
- Own config dir structure.

* Sun Jul 19 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.2.beta14
- Revert to using system regex, building with more than one regexp
  implementation makes no sense and pcre and tre seem to have more issues.
  Also patch to make builds with both pcre and tre less likely to happen.
- Patch to make sure correct regex headers are used and clean up unused ones.
- Patch to make path to sendmail executable settable at build time.
- Patch to fix embedded man page sections for non-section 5 man pages.
- Patch to improve some Finnish translations.

* Wed Jul 15 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.9.25-0.1.beta14
- Update to 0.9.25.beta14; gcc 4.3 patch no longer needed.
- Build with PCRE and TRE support.
- Use %%global instead of %%define.
- Specfile cleanups.

* Sun Sep 07 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.24-0.3
- Add gcc 4.3 patch from e-tobi

* Mon May 05 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.24-0.2
- New stable release

* Sun Apr 20 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.24-0.1.beta27
- New beta
- Handle VDR 1.6 style i18n
- Update license

* Wed Sep  5 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9.23-0.1
- 0.9.23.
- License: GPL+

* Sun May 27 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9.22-0.1
- 0.9.22.

* Sun Apr 29 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9.21-0.1
- 0.9.21.
- Include extra scripts in docs.

* Tue Jan 30 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9.20-0.1
- 0.9.20.

* Sun Jan  7 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9.19-0.2
- Rebuild for VDR 1.4.5.

* Sun Nov 19 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.9.19-0.1
- First build.
