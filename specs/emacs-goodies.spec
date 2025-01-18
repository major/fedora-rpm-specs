%global pkg emacs-goodies
%global pkgname Emacs-goodies
%global goodies_dir %{buildroot}%{_emacs_sitelispdir}/goodies/
%global gnus_dir %{buildroot}%{_emacs_sitelispdir}/gnus-bonus/

Name:       %{pkg}
Version:    41.0
Release:    18%{?dist}
Summary:    Miscellaneous add on for Emacs

# Automatically converted from old format: GPLv2+ and GPLv3 - review is highly recommended.
License:    GPL-2.0-or-later AND GPL-3.0-only
URL:        http://packages.debian.org/sid/lisp/emacs-goodies-el
Source0:    http://snapshot.debian.org/archive/debian/20180913T085742Z/pool/main/e/emacs-goodies-el/emacs-goodies-el_41.0.tar.xz
#Patch which adjusts debian specific information to fedora in texi file
#Patch is irrelevant to upstream as it is specific to Fedora
Patch0:     emacs-goodies-el.texi.patch

BuildArch:  noarch
BuildRequires:  emacs texinfo
Requires:   emacs(bin) >= %{_emacs_version}

Obsoletes:  %{name}-el < 41.0-15
Provides:   %{name}-el = %{version}-%{release}

%description
This is %{pkgname} %{version} which provides numerous add on for GNU Emacs
and Gnus.

%prep
%setup -q -n %{pkg}-el-%{version}
%{__chmod} 644 COPYING-GPL-v3
%{__chmod} 644 COPYING-GPL-v2
%patch -P0 -p1

%build
%{__mkdir} -p elisp/%{pkg}-el/info
cd elisp/%{pkg}-el/
%{__chmod} +x %{pkg}-loaddefs.make
./%{pkg}-loaddefs.make
%{_emacs_bytecompile} *.el
makeinfo emacs-goodies-el.texi
iconv -f iso8859-1 -t utf-8 info/emacs-goodies > info/emacs-goodies.utf
%{__mv} info/emacs-goodies.utf info/emacs-goodies

%install
%{__rm} -rf %{buildroot}
%{__install} -pm 755 -d %{goodies_dir}
%{__install} -pm 755 -d %{buildroot}%{_emacs_sitestartdir}
%{__install} -pm 644 elisp/%{pkg}-el/%{pkg}-loaddefs.el %{buildroot}%{_emacs_sitestartdir}
%{__install} -pm 644 elisp/%{pkg}-el/*.elc %{goodies_dir}
%{__install} -pm 644 elisp/%{pkg}-el/*.el %{goodies_dir}
%{__install} -pm 755 -d %{buildroot}%{_infodir}/
%{__install} -pm 644 elisp/%{pkg}-el/info/%{pkg} %{buildroot}%{_infodir}/

%files
%doc COPYING-GPL-v2 COPYING-GPL-v3
%{_emacs_sitelispdir}/goodies/*.el
%{_emacs_sitelispdir}/goodies/*.elc
%{_emacs_sitestartdir}/emacs-goodies-loaddefs.el
%{_infodir}/%{pkg}.gz
%dir %{_emacs_sitelispdir}/goodies

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 41.0-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 15 2024 Tim Landscheidt <tim@tim-landscheidt.de> - 41.0-15
- Obsolete -el subpackage (#1234528)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 41.0-3
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Arun S A G <sagarun@fedoraproject.org> - 41.0-1
- New upstream release

* Mon Sep 10 2018 Arun S A G <sagarun@fedoraproject.org> - 40.1-2
- Fix some lint issues

* Mon Sep 10 2018 Arun S A G <sagarun@fedoraproject.org> - 40.1-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 35.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 35.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 35.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 35.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 35.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 18 2014 Arun S A G <sagarun AT gmail dot com> - 35.8-2
- Patch problems with ctypes.el Bug#833103

* Sat Dec 21 2013 Arun S A G <sagarun AT gmail dot com> - 35.8-1
- Update to latest upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 17 2011 Arun S.A.G <sagarun [AT] gmail dot com> - 35.0-1
- Updated to new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 13 2010 Arun S.A.G <sagarun [AT] gmail dot com> - 34.1-1
- Updated to emacs-goodies 34.1-1

* Sat May 29 2010 Arun S.A.G <sagarun [AT] gmail dot com> - 33.5-1
- Updated to emacs-goodies 33.5-1

* Sun May 16 2010 Arun S.A.G <sagarun [AT] gmail dot com> - 31.5-2
- Bumping version to match F12

* Fri Apr 2 2010 Arun S.A.G <sagarun [AT] gmail dot com> -  31.5-1
- Updated to version 31.5

* Sun Mar 14 2010 Jonathan G. underwood <jonathan.underwood@gmail.com>- 31.4-2
- Update spec file to comply with Emacs add-on packaging guidelines

* Wed Jan 13 2010 Arun SAG  <sagarun [AT] gmail dot com> - 31.4-1
- Removed patch1 as it is integrated into source by the upstream
- Made gnus to be autoloaded using source1
- Updated to version  31.4

* Wed Dec 16 2009 Arun SAG <sagarun [AT] gmail dot com> - 31.2-3
- License adjusted to GPLv2+ and GPLv3

* Mon Dec 14 2009 Arun SAG <sagarun [AT] gmail dot com> - 31.2-2
- Comment on  patches added

* Fri Dec 4 2009 Arun SAG <sagarun [AT] gmail dot com> - 31.2-1
- Updated to version 31.2-1

* Thu Nov 26 2009 Arun SAG <sagarun [AT] gmail dot com> - 31.1-1
- Updated to version 31.1-1

* Sun Nov 15 2009 Arun SAG <sagarun [AT] gmail dot com> - 30.11-1
- Updated to version 30.11-1

* Fri Oct 30 2009 Arun SAG <sagarun [AT] gmail dot com> - 30.8-2
- Upstream patches are applied

* Thu Oct 22 2009 Arun SAG <sagarun [AT] gmail dot com> - 30.8-1
- Updated to 30.8-1
- License corrected to GPLv2+

* Tue Sep 15 2009 Arun SAG <sagarun [AT] gmail dot com> - 30.5-1
- Initial release 30.5-1
