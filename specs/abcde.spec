Name:           abcde
Version:        2.9.3
Release:        17%{?dist}
Summary:        A Better CD Encoder

# previously license field included Public Domain, but FOSSology scan of v2.9.3 did not 
# turn up any public domain dedications other than a reference in an old changelog entry
# to a public domain mention that has since been removed upstream.
License:        GPL-2.0-or-later
URL:            https://abcde.einval.com/
Source0:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz
Source1:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz.sign
# gpg2 --recv-key 0x587979573442684E
# gpg2 --export --export-options export-minimal 0x587979573442684E > 587979573442684E.gpg
Source2:        587979573442684E.gpg
Patch0:         %{name}-normalize.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1916974
Patch1:         https://bugzilla.redhat.com/attachment.cgi?id=1748056#/abcde-gnudb.patch

BuildArch:      noarch
BuildRequires:  %{_bindir}/gpgv2
BuildRequires:  make
BuildRequires:  perl-generators
Requires:       cd-discid
Requires:       %{_bindir}/hostname
Requires:       wget
Requires:       which
# cdparanoia, vorbis-tools for defaults
Requires:       cdparanoia
Requires:       vorbis-tools
# icedax for cd-text
Recommends:     icedax
Recommends:     flac
Suggests:       cd-discid
Suggests:       cdrdao
Suggests:       ImageMagick
Suggests:       lame
Suggests:       libcdio-paranoia
Suggests:       normalize
Suggests:       opus-tools
Suggests:       speex-tools
Suggests:       twolame
Suggests:       wavpack
Suggests:       vorbisgain
# eyeD3 is smaller than id3v2
Suggests:       %{_bindir}/eyeD3
Conflicts:      python-eyed3 < 0.7.0

%description
abcde is a front end command line utility (actually, a shell script)
that grabs audio tracks off a CD, encodes them to various formats, and
tags them, all in one go.


%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%autosetup
mv examples/cue2discid .
sed -i -e 's|bin/python\b|bin/python3|' cue2discid
chmod -c -x examples/musicbrainz-get-tracks


%build


%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}
rm -r $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version} # handled separately
install -pm 755 cue2discid $RPM_BUILD_ROOT%{_bindir}


%files
%license COPYING
%doc FAQ README changelog examples/
%config(noreplace) %{_sysconfdir}/abcde.conf
%{_bindir}/abcde
%{_bindir}/abcde-musicbrainz-tool
%{_bindir}/cddb-tool
%{_bindir}/cue2discid
%{_mandir}/man1/abcde.1*
%{_mandir}/man1/cddb-tool.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 16 2023 Jilayne Lovejoy <jlovejoy@redhat.com> - 2.9.3-12
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.9.3-7
- point to gnudb.org instead of the discontinued freedb.org (#1916974)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.9.3-3
- MusicBrainz lookup support for abcde (#1758816)
- use gpgverify macro
- add missing BR: perl-generators to generate perl dependencies
- add Requires: hostname which might be missing on minimal installs

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.9.3-1
- update to 2.9.3 (#1672604)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 04 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.9.2-1
- update to 2.9.2 (#1611854)
- fix version typo in Makefile

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.9.1-1
- update to 2.9.1 (#1553948)

* Fri Mar 09 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.9-1
- update to 2.9 (#1553139)
- rebase patches
- use autosetup macro

* Wed Feb 21 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.8.1-6
- add Suggests for twolame, now that's included in Fedora 27+ (#1534297)
- verify GPG signature for the source tarball

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.8.1-3
- set the default CDDBMETHOD to cddb, as perl MusicBrainz modules are
  not packaged
- add a weak dependency on lame, since mp3 encoding is now in Fedora 25+

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.8.1-1
- Update to 2.8.1

* Wed Jan 18 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.8-1
- Update to 2.8
- Add the supported additional tools packaged in Fedora to Suggests:

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-2
- Rebuild for Python 3.6

* Sun Apr 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.7.2-1
- Update to 2.7.2
- Use HTTPS for URLs

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct  4 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.7.1-1
- Update to 2.7.1

* Sun Jun 21 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.7-1
- Update to 2.7
- Use python3 in cue2discid
- Soften some dependencies

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov  9 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.6-1
- Update to 2.6
- Mark COPYING as %%license where applicable

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.5.4-4
- Fix eyeD3 tagging of entries without year info
- Fix bogus date in %%changelog

* Thu Aug  1 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.5.4-3
- Apply upstream + --comment fixes for eyeD3 >= 0.7.0 (#991163).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.5.4-1
- Update to 2.5.4.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.5.3-1
- Update to 2.5.3.

* Sun Apr 29 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.5.2-1
- Update to 2.5.2.

* Sun Apr 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.5.0-1
- Update to 2.5.0.
- Clean up specfile constructs no longer needed in Fedora or EL6+.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Dennis Gilmore <dennis@ausil.us> -2.4.2-3
- remove unsupported Requires(hint) from spec

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> -2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 30 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.4.2-1
- Update to 2.4.2 (#597723), track info patch applied upstream.

* Fri Apr  2 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.4.1-1
- Update to 2.4.1.

* Sun Oct 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.4.0-1
- Update to 2.4.0 (#529509).

* Wed Aug 12 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.8-1
- Update to 2.3.99.8 (#516886).

* Mon Jul 27 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.7-1
- Update to 2.3.99.7 (#513795); wget and usage patches applied upstream.
- Patch to improve CDDB track info handling.
- Update URL.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.99.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.99.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 10 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.6-7
- Patch to work around wget 1.11 regression (#441862).

* Sat Jan 19 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.6-6
- Include fixes from Ubuntu's 2.3.99.6-1ubuntu2: enables M4A and Speex
  tagging, fixes range code, and the -M option.
- Fix Speex comment tagging.
- Fix some usage message spelling errors.
- Drop disttag.

* Sat Sep 29 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.6-4
- Requires: which

* Mon Aug 13 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.6-3
- License: GPLv2+
- Add (empty) %%build section.

* Tue Aug 29 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.6-2
- Change vorbis-tools and flac dependencies to Requires(hint), drop
  speex dependency.

* Mon Aug  7 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.6-1
- 2.3.99.6.

* Wed Mar  1 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.5-1
- 2.3.99.5.

* Wed Dec 14 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99.2-1
- 2.3.99.2, config file fixes mostly applied upstream.

* Sat Dec 10 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.3.99-1
- 2.3.99, minor config file fixes.

* Mon Sep  5 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.3.4-1
- 2.3.4.

* Fri Aug 26 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.3.3-1
- 2.3.3.
- Reformat specfile.

* Sat Aug 20 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.3.2-1
- 2.3.2, vi and genre patches applied upstream.
- Convert man page to UTF-8.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.2.3-2
- rebuilt

* Thu Feb 10 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.2.3-1
- Update to 2.2.3.

* Mon Jan 17 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-2
- Add vorbis-tools, flac, cdparanoia, wget, and speex dependencies.
- Weed out some Debianisms from default external tool names.
- Include more docs.

* Fri Jan 14 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2.2.0

* Wed Apr 14 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2.1.19

* Tue May 21 2002 Nils Philippsen <nphilipp@redhat.com>
- version 2.0.3
- update rh, genre patches

* Wed Apr 25 2001 Nils Philippsen <nphilipp@redhat.com>
- version 1.9.9
- configuration now uses freedb.org per default, no need to patch
- various artist media can have a different output file name (than single
  artist ones)
- fix newlines with CR in parsing cddb genre

* Tue Jan 09 2001 Nils Philippsen <nphilipp@redhat.com>
- version 1.9.7
- initial build

