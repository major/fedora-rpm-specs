Name:           mediawiki-SpecialInterwiki
Version:        0
Release:        0.27.20080913svn%{?dist}
Summary:        An extension to provide an interwiki management system

License:        GPLv2+
URL:            http://www.mediawiki.org/wiki/Extension:SpecialInterwiki
# http://svn.wikimedia.org/viewvc/mediawiki/trunk/extensions/Interwiki/SpecialInterwiki.php?revision=37451
Source0:        SpecialInterwiki.php
# http://svn.wikimedia.org/viewvc/mediawiki/trunk/extensions/Interwiki/SpecialInterwiki_body.php?revision=36822
Source1:        SpecialInterwiki_body.php
# http://svn.wikimedia.org/viewvc/mediawiki/trunk/extensions/Interwiki/SpecialInterwiki.i18n.php?revision=40706
Source2:        SpecialInterwiki.i18n.php
BuildArch:      noarch

Requires:       mediawiki >= 1.12

%description
Interwiki management extension allowing the viewing and management of InterWiki
links for Mediawiki preventing the need for direct database access.

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/SpecialInterwiki
install -cpm 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/SpecialInterwiki

echo 'To complete installation of %{name}, add the following line to LocalSettings.php:

  require_once "$IP/extensions/SpecialInterwiki/SpecialInterwiki.php";

for each MediaWiki instance you wish to install %{name} on.' > README.Fedora


%files
%{_datadir}/mediawiki/extensions/SpecialInterwiki
%doc README.Fedora

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 0-0.12.20080913svn
- Use special %%doc to install docs in order to honor %%{_docdir_fmt}.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0-0.6.20080913svn
- Fix unowned versioned documentation directory (#474674).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20080913svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep 13 2008 Nigel Jones <dev@nigelj.com> - 0-0.4.20080913svn
- Update to >= 1.12 version now that rawhide has an updated Mediawiki package
* Tue Jun 10 2008 Nigel Jones <dev@nigelj.com> - 0-0.3.20080606svn
- Do away with the prep section

* Fri Jun 06 2008 Nigel Jones <dev@nigelj.com> - 0-0.2.20080606svn
- Do away with the tarball

* Fri Jun 06 2008 Nigel Jones <dev@nigelj.com> - 0-0.1.20080606svn
- Initial package build.
