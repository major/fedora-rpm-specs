%global __requires_exclude perl\\(W3C::Validator::EventHandler\\)

Name:           w3c-markup-validator
Version:        1.3
Release:        30%{?dist}
Summary:        W3C Markup Validator

License:        W3C
URL:            http://validator.w3.org/
# Source0 created with Source99
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}-prepare-tarball.sh
# Not upstreamable
Patch0:         %{name}-1.2-config.patch
# Not upstreamable
Patch1:         %{name}-1.3-syspaths.patch
# Not upstreamable,
# https://www.redhat.com/archives/fedora-legal-list/2009-February/msg00015.html
Patch2:         %{name}-1.0-valid-icons.patch
# Not upstreamable,
# https://www.redhat.com/archives/fedora-legal-list/2009-February/msg00020.html
Patch3:         %{name}-1.3-iso-html.patch
Patch4:         %{name}-apache24.patch


BuildArch:      noarch
BuildRequires:  %{__perl}
BuildRequires:  perl-generators
Requires:       httpd
Requires:       %{name}-libs = %{version}
# Not autodetected
Requires:       perl(XML::LibXML) >= 1.70
# Optional
Recommends:       perl(HTML::Tidy)

%description
The W3C Markup Validator checks documents like HTML and XHTML for
conformance to W3C Recommendations and other standards.

%package        libs
Summary:        SGML and XML DTDs for the W3C Markup Validator
Requires:       sgml-common
Requires:       html401-dtds
Requires:       xhtml1-dtds >= 1.0-20020801.1

%description    libs
SGML and XML DTDs for the W3C Markup Validator.

%prep
%setup -q -n validator-%{version}

# Remove not needed stuff
rm -r htdocs/sgml-lib/REC-html401-19991224
rm -r htdocs/sgml-lib/REC-xhtml1-20020801
rm htdocs/images/markup_validation_service.psd

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

find . -type f -name "*.orig" -delete # patch backup files

mv htdocs/sgml-lib .

# Localize configs.
%{__perl} -pi -e \
  's|/usr/local/validator\b|%{_datadir}/%{name}|' \
  htdocs/config/validator.conf httpd/conf/httpd.conf httpd/cgi-bin/*
%{__perl} -pi -e \
  's|\$Base/htdocs/sgml-lib|%{_datadir}/sgml/%{name}| ;
   s|\$Base/htdocs/config/tidy\.conf|%{_sysconfdir}/w3c/tidy.conf|' \
  htdocs/config/validator.conf
%{__perl} -pi -e \
  's|\$home/htdocs/sgml-lib/catalog\.xml|%{_datadir}/sgml/%{name}/catalog.xml|' \
  httpd/mod_perl/startup.pl

# Move config out of the way
mv htdocs/config __config


%build


%install
rm -rf $RPM_BUILD_ROOT

# Config files
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/w3c
install -pm 644 __config/* $RPM_BUILD_ROOT%{_sysconfdir}/w3c
install -Dpm 644 httpd/conf/httpd.conf \
  $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Scripts, HTML, etc.
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/httpd
cp -pR httpd/cgi-bin htdocs share $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pR httpd/mod_perl $RPM_BUILD_ROOT%{_datadir}/%{name}/httpd

# SGML library
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/sgml
cp -pR sgml-lib $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}
ln -s ../html/4.01 $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}/REC-html401-19991224
ln -s ../../xml/xhtml/1.0 \
  $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}/REC-xhtml1-20020801
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sgml
touch $RPM_BUILD_ROOT%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat


%post
[ $1 -eq 1 ] && systemctl reload httpd || :

%postun
%systemd_postun_with_restart httpd

%post libs
for catalog in sgml.soc xml.soc ; do
  install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/$catalog >/dev/null 2>&1 || :
done

%preun libs
for catalog in sgml.soc xml.soc ; do
  install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/$catalog >/dev/null 2>&1 || :
done


%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%dir %{_sysconfdir}/w3c/
%config(noreplace) %{_sysconfdir}/w3c/charset.cfg
%config(noreplace) %{_sysconfdir}/w3c/tidy.conf
# These are incompatible to some extent between releases, check noreplace
%config %{_sysconfdir}/w3c/types.conf
%config(noreplace) %{_sysconfdir}/w3c/validator.conf
%{_datadir}/%{name}/

%files libs
%ghost %config %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat
%{_datadir}/sgml/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 21 2022 Sérgio Basto <sergio@serjux.com> - 1.3-24
- Recommends perl(HTML::Tidy) instead Require

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Nathanael Noblet <nathanael@gnat.ca> - 1.3-20
- Adjust postun to use systemctl

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 19 2014 Nathanael Noblet <nathanael@gnat.ca> - 1.3-9
- Fix for bug #1109575 based off submitted patch

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Nathanael Noblet <nathanael@gnat.ca> - 1.3-7
- Rebuilt to fix perl dependencies bug #1057718

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.3-5
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Nils Philippsen <nils@redhat.com> - 1.3-3
- install missing httpd/mod_perl/startup.pl which prevented httpd from starting

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Nathanael Noblet <nathanael@gnat.ca> - 1.3-1
- New upstream release
- fixed syspath and iso-html patch for new release
- remove upstreamed perl warnings patch 

* Mon Jun 25 2012 Nathanael Noblet <nathanael@gnat.ca> - 1.2-5
- Removed non-needed hans patch as it has been packaged

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 15 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.2-3
- Filter unsatisfied perl(W3C::Validator::EventHandler) self-dependency.

* Sun Mar 13 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.2-2
- Apply upstream patch to avoid lc(undef) warnings with Perl >= 5.12.

* Wed Mar  9 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.2-1
- Update to 1.2.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.1-2
- Fix XML::LibXML catalog files setup (#657636).

* Tue Jul 13 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.1-1
- Update to 1.1.

* Fri Jun 18 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.0-1
- Update to 1.0, XML encoding fix applied upstream.

* Tue Mar  9 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.8.6-1
- Update to 0.8.6 + upstream XML encoding fix.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 29 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.8.5-1
- 0.8.5, override patch applied upstream.
- Drop content not acceptable in Fedora (some icons, ISO-HTML DTD).
- Refresh/reorganize patches.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.4-1
- 0.8.4 + upstream doctype override fix.
- types.conf and error log trash patches applied upstream.

* Thu Sep 11 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.3-2
- Upstream fix for server error log trashing.

* Tue Aug 12 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.3-1
- 0.8.3 + upstream types.conf fix; missing form enctype patch applied upstream.
- Drop disttag.

* Wed Mar 19 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.2-3
- Adjust to xhtml1-dtds >= 1.0-20020801 changes.
- Require (hint) perl(HTML::Tidy).

* Sun Oct 14 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.8.2-2
- Apply upstream fix for missing form enctype in reupload form.

* Thu Oct 11 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.8.2-1
- 0.8.2.

* Fri Aug 10 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.8.1-1
- 0.8.1.
- License: W3C
- Own the %%{_sysconfdir}/w3c directory.
- Patch to make some Encode::* modules that aren't packaged in Fedora yet
  optional.

* Tue Jun  5 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.8.0-0.1.b2
- 0.8.0b2.

* Sun May 27 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.8.0-0.1.b1
- 0.8.0b1.

* Wed Nov 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.4-1
- 0.7.4.

* Tue Oct 31 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.3-2
- Reference HTML 4.01 DTDs directly instead of making all system catalogs
  available - something in the catalogs breaks at least XHTML 1.0 (#213131).
- Use system XHTML 1.0 DTDs.

* Mon Oct 23 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.3-1
- 0.7.3, feedback and undebian patches applied upstream.
- Use "W3C License" as the License tag to appease rpmlint.

* Fri Sep 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.2-4
- Fix feedback view, remove references to Debian (#206617).

* Sat Aug 26 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.2-3
- Patch to allow use of system catalogs and DTDs, use system html401-dtds.
- Make config files noreplace again.
- Drop no longer needed Obsoletes.
- Allow FTP by default.

* Wed Mar 29 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.2-2
- Rebuild due to #187173, SELinux issues are being worked on in #182673.

* Mon Feb 20 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.2-1
- 0.7.2, Config::General compat patch applied upstream.

* Sun Jan 29 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7.1-1
- Require opensp >= 1.5, not openjade.
- Patch to work with Config::General 2.31.

* Sat Oct  8 2005 Ville Skyttä <ville.skytta@iki.fi>
- 0.7.1.

* Fri Sep 23 2005 Ville Skyttä <ville.skytta@iki.fi> - 0.7.0-1
- 0.7.0.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.6.7-2
- rebuilt

* Sun Jul 25 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.7-0.fdr.1
- Update to 0.6.7.

* Sat May 22 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.6-0.fdr.1
- Update to 0.6.6.
- Include local source/index.html in the package.

* Fri May  7 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.5-0.fdr.1
- Update to 0.6.5.

* Fri Apr 30 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.6.5-0.fdr.0.1.beta3
- Update to 0.6.5 beta 3.

* Sat Apr 24 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.6.5-0.fdr.0.1.beta2
- Apply fdr naming scheme.

* Sat Apr 24 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.5-0.beta2.2
- Make httpd reload its config after install, upgrade and erase.
- Fix a couple of paths for beta2.

* Sat Apr 17 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.5-0.beta2.1
- Update to 0.6.5 beta 2.

* Mon Apr  5 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.5-0.beta1.3
- The link checker is now available separately from CPAN.

* Mon Dec  1 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.5-0.beta1.2
- Cleanups.

* Fri Aug 29 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.5-0.beta1.1
- Update to 0.6.5 beta 1.

* Sat Aug 23 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.2-5w3c
- Requires openjade >= 0:1.3.2 (Red Hat packages OpenSP 1.5 there).

* Wed Jul 23 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.2-4w3c
- Include checklink manual page.
- Some spec file cleanups.

* Thu Jul 17 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.2-3w3c
- Requires perl(Net::IP).

* Fri Jul  4 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.2-2w3c
- Use aliasing instead of hardcoded docroot in httpd configuration.

* Mon Apr 21 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.6.2-1w3c
- Update to 0.6.2.
- Rename to w3c-markup-validator.
- Install our catalogs if %%{_bindir}/install-catalog is available.
- Add Epoch: 0.

* Sun Dec  1 2002 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-1w3c
- Update to 0.6.1.

* Fri Nov 29 2002 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-1w3c
- First release.
