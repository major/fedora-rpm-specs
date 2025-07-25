%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}


Name:           quilt
Version:        0.69
Release:        2%{?dist}
Summary:        Scripts for working with series of patches

License:        GPL-2.0-only
URL:            https://savannah.nongnu.org/projects/%{name}
Source:         https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  diffstat
BuildRequires:  gettext
BuildRequires:  gawk
BuildRequires:  p7zip
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  util-linux-ng
BuildRequires:  %{_sbindir}/sendmail

Requires:       bzip2
Requires:       coreutils
Requires:       diffstat
Requires:       diffutils
Requires:       gawk
Requires:       gzip
Requires:       p7zip
Requires:       procmail
Requires:       rpm-build
Requires:       sed
Requires:       tar
Requires:       util-linux-ng
Requires:       %{_sbindir}/sendmail

%description
These scripts allow one to manage a series of patches by keeping track of the
changes each patch makes. Patches can be applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts found at
http://www.zip.com.au/~akpm/linux/patches/


%prep
%autosetup -p1


%build
%configure                             \
  --docdir=%{_pkgdocdir}               \
  --with-diffstat=%{_bindir}/diffstat  \
  --with-sendmail=%{_sbindir}/sendmail \
;
%make_build


%install
%make_install BUILD_ROOT=%{buildroot}
%{find_lang} %{name}
mv %{buildroot}%{_pkgdocdir}/* .
rm -rf %{buildroot}%{_pkgdocdir}


%files -f %{name}.lang
%doc README README.MAIL quilt.pdf TODO
%license AUTHORS COPYING
%{_bindir}/guards
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/emacs/site-lisp/%{name}.el
%{_sysconfdir}/bash_completion.d
%config %{_sysconfdir}/%{name}.%{name}rc
%{_mandir}/man1/*.1*


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Apr 28 2025 Josh Boyer <jwboyer@fedoraproject.org> - 0.69-1
- Update to 0.69 release

* Sun Mar 16 2025 Richard Shaw <hobbes1069@gmail.com> - 0.68-3
- Add patches to deal with changes in RPM 4.20.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Björn Esser <besser82@fedoraproject.org> - 0.68-1
- Update to 0.68 release
  Fixes: rhbz#2271880

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 13 2023 Josh Boyer <jwboyer@fedoraproject.org> - 0.67-4
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Josh Boyer <jwboyer@fedoraproject.org> - 0.67-1
- New upstream release (RhBug 2054729)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Josh Boyer <jwboyer@fedoraproject.org> - 0.66-5
- Add BuildRequires on make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Björn Esser <besser82@fedoraproject.org> - 0.66-1
- Update to 0.66 release (rhbz 1693765)
- Modernize spec file
- Add some additional BuildRequires
- Add Requires: p7zip

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Josh Boyer <jwboyer@fedoraproject.org> - 0.65-1
- Update to the 0.65 release (rhbz 1393636)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Josh Boyer <jwboyer@fedoraproject.org> - 0.64-1
- Update to the 0.64 release (rbhz 1190801)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Josh Boyer <jwboyer@fedoraproject.org> - 0.63-1
- Update to 0.63 release (rhbz 1095660)

* Mon Dec 09 2013 Josh Boyer <jwboyer@fedoraproject.org> - 0.61-1
- Update to 0.61 release (rhbz 1039512)
- Add Requires for procmail (rhbz 1005053)

* Tue Aug 06 2013 Josh Boyer <jwboyer@redhat.com> - 0.60-6
- Adjust for unversioned docdir (rhbz 993926)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.60-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 01 2012 Josh Boyer <jwboyer@redhat.com> - 0.60-1
- Update to new upstream release.  Now noarch, yay.

* Mon Jan 30 2012 Josh Boyer <jwboyer@redhat.com> - 0.51-1
- Update to new upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Josh Boyer <jwboyer@redhat.com> - 0.50-3
- Fix quilt setup regression (rhbz #768787)

* Wed Dec 07 2011 Josh Boyer <jwboyer@redhat.com> - 0.50-2
- Fix regression in email address checking

* Tue Dec 06 2011 Josh Boyer <jwboyer@redhat.com> - 0.50-1
- Update to latest upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.48-1
- New upstream release
- Drop upstreamed patch
- Update spec to drop redundant buildroot items and clean section

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Josh Boyer <jwboyer@gmail.com> - 0.47-4
- Fix sendmail configure (bug 474136)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 - jwboyer@gmail.com - 0.47-2
- Fix 'quilt setup' for rpm 4.6 (bug 473557)

* Thu Aug 21 2008 - jwboyer@gmail.com 0.47-1
- Update to latest release

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.46-5
- Autorebuild for GCC 4.3

* Fri Sep 28 2007 - jwboyer@jdub.homelinux.org 0.46-4
- BR util-linux-ng for getopt

* Tue Aug 21 2007 - jwboyer@jdub.homelinux.org 0.46-3
- BR gawk

* Fri Aug 03 2007 - jwboyer@jdub.homelinux.org 0.46-2
- Update license field

* Fri Oct 20 2006 - jwboyer@jdub.homelinux.org 0.46-1
- Update to latest release

* Sun Aug 27 2006 - jwboyer@jdub.homelinux.org 0.45-2
- Bump and rebuild for FE6

* Mon Apr 24 2006 - jwboyer@jdub.homelinux.org 0.45-1
- Update to latest release

* Wed Feb 15 2006 - jwboyer@jdub.homelinux.org 0.44-1
- Update to latest release

* Thu Feb 2 2006 - jwboyer@jdub.homelinux.org 0.43-1
- Update to latest upstream
- Drop fix-debuginfo patch (upstream)

* Fri Oct 28 2005 - jwboyer@jdub.homelinux.org 0.42-2
- fix debuginfo package (bug 171917)

* Fri Jul 29 2005 - jwboyer@jdub.homelinux.org 0.42-1
- Update to latest upstream

* Mon Jun 6 2005 - jwboyer@jdub.homelinux.org 0.40-3
- Remove hardcoded dist tags
- Bump release

* Wed May 4 2005 - jwboyer@jdub.homelinux.org 0.40-2
- Bump release to fix dist tag usage

* Tue May 3 2005 - jwboyer@jdub.homelinux.org 0.40-1
- Update to 0.40
- Remove fix-man-page.patch as it's now upstream
- Fix release numbering for multiple distro version

* Fri Apr 22 2005 - jwboyer@jdub.homelinux.org 0.39-7
- Bump release to be higher than FC-3 branch

* Thu Apr 21 2005 - jwboyer@jdub.homelinux.org 0.39-5
- Add rpm-build requires back for setup function.  rpm-build needs patch and
  perl, so remove explict requires.

* Tue Apr 5 2005 - jwboyer@jdub.homelinux.org 0.39-4
- Remove some Requires.  coreutils needs grep and findutils. rpm-build isn't
  really needed.  gzip needs mktemp.
- Remove the Authors from the description to make it more Fedora like.
- Get rid of old character set warning in man page

* Sun Apr 3 2005 - jwboyer@jdub.homelinux.org 0.39-3
- Add dependency on perl for the graph, mail, and setup functions

* Fri Apr 1 2005 Toshio Kuratomi <toshio-tiki-lounge.com> 0.39-2
- Full URL for Source.
- Changed some of the entries in the %%files section to own more directories,
  add more docs, and mark config files as config.
- Add some BuildRequires, configure switches and Requires so various quilt
  commandline options work.

* Thu Mar 31 2005 - jwboyer@jdub.homelinux.org
- Adapt quilt spec file to Fedora Extras conventions
