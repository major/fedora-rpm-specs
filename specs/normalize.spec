Summary:  Adjust the volume of audio files to a standard level
Name:     normalize
Version:  0.7.7
Release:  33%{?dist}
URL:      http://normalize.nongnu.org/
License:  GPL-2.0-or-later AND LGPL-2.1-or-later
Source0:  http://download.savannah.gnu.org/releases/normalize/normalize-%{version}.tar.gz
Source1:  http://download.savannah.gnu.org/releases/normalize/normalize-%{version}.tar.gz.sig
# https://pgp.mit.edu/pks/lookup?op=get&search=0xAFC8519A83FE7486
# https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x659d42b60f3b86ea4d37777eafc8519a83fe7486
Source2:  0xAFC8519A83FE7486.gpg
# fix audiofile detection
Patch0:   normalize-0.7.7-audiofile.patch
# fix configure regeneration with autoreconf
Patch1:   normalize-0.7.7-autoreconf.patch
# fix building without XMMS
Patch2:   normalize-0.7.7-no-xmms.patch
# fix building with GCC 15
Patch3:   normalize-0.7.7-gcc15.patch

BuildRequires:  audiofile-devel
BuildRequires:  flac
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  lame
BuildRequires:  libtool
BuildRequires:  libmad-devel
BuildRequires:  mpg123
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  vorbis-tools
# Explicit, because won't be detected automatically.
Requires:       flac
Requires:       lame
Requires:       mpg123
Requires:       vorbis-tools

%description
normalize is a tool for adjusting the volume of audio files to a
standard level. This is useful for things like creating mixed CDs
and mp3 collections, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%autosetup -p1
touch AUTHORS ChangeLog
autoreconf -fi
for i in THANKS doc/normalize-mp3.1; do
    iconv -f ISO-8859-1 -t UTF8 "$i" > "$i.UTF8"
    touch -r "$i" "$i.UTF8"
    mv "$i.UTF8" "$i"
done


%build
%configure --disable-xmms --with-audiofile --disable-static
%make_build


%install
%make_install

%find_lang %{name}

%check
make check

%files -f %{name}.lang
%license COPYING
%doc README NEWS THANKS TODO
%{_bindir}/normalize
%{_bindir}/normalize-mp3
%{_bindir}/normalize-ogg
%{_mandir}/man1/normalize.1.*
%{_mandir}/man1/normalize-mp3.1.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild
- fix building with GCC 15 (resolves rhbz#2340940) (Dominik Mierzejewski)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 16 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.7.7-28
- add mpg123 to dependencies (required for mp3 decoding)
- use SPDX license identifiers
- enable tests
- describe patches

* Thu Jul 21 2022 Dominik Mierzejewski <dominik@greysector.net> - 0.7.7-27
- fix build without xmms/gtk+/glib

* Wed May 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 0.7.7-26
- use a working Source URL
- verify source signature

* Sun Apr 17 2022 Dominik Mierzejewski <dominik@greysector.net> - 0.7.7-25
- drop xmms plugin (xmms is no longer built in Fedora 35+)
- drop audiofile version from BR, all distros have >= 0.2.2

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 23 2020 Leigh Scott <leigh123linux@gmail.com> - 0.7.7-22
- Revert mpg123 and use libmad

* Sun Aug 23 2020 Leigh Scott <leigh123linux@gmail.com> - 0.7.7-21
- Add mpg123
- Clean up spec file

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
- Drop madplay support
- Add BuildRequires: gcc

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.7.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.7.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Paul Howarth <paul@city-fan.org> - 0.7.7-13
- Perl 5.26 rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Paul Howarth <paul@city-fan.org> - 0.7.7-11
- BR: perl-generators for proper dependency generation
  (https://fedoraproject.org/wiki/Changes/Build_Root_Without_Perl)
- Use %%license

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Mar 25 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 0.7.7-9
- Fix FTBFS
- Modernize spec a bit
- Fix various rpmlint warnings

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7.7-8
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.7.7-5
- rebuild for new F11 features

* Mon Aug 04 2008 David Timms <iinet.net.au [AT] dtimms> 0.7.7-4
- mod BR: to libmad, del Requires: mad

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.7.7-3
- rebuild

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.7.7-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Sep 24 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.7.7-1
- Update to 0.7.7 (new upstream locations).

* Fri Apr  7 2006 Dams <anvil[AT]livna.org> - 0.7.6-11
- xmms package requires xmms-libs instead of xmms

* Mon Mar 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0.7.6-10
- Drop Epoch completely

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Fri Dec 31 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> 0:0.7.6-0.lvn.9
- fix x86_64 build; inside mach the integrated libtool does not work

* Thu May 20 2004 Dams <anvil[AT]livna.org> - 0:0.7.6-0.lvn.8
- xmms-config errors redirected to dev/null

* Sun May  4 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.7.6-0.fdr.7
- Use $RPM_BUILD_ROOT instead of %%{buildroot}.
- Fix spec file in accordance with bug #213 comments #14 and #15.

* Sun Apr 27 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Rename package normalize-xmms to xmms-normalize.
- Use explicit Epoch 1 for versioned audiofile, drop version
  requirement for xmms.

* Sat Apr 26 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Drop explicit Requires where possible.
- Update for split "mad" packages (bug #187).

* Fri Apr 25 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Update spec file according to Fedora package request bug #213.

* Sat Apr  5 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Depend on libmad-*.
- RHL9 build.

* Sun Apr 14 2002 Michael Schwendt <mschwendt[AT]users.sf.net>
- Initial RPM built for Red Hat Linux 7.2.
- Wants libaudiofile >= 0.2.2, but 0.2.1-2 seems to work.
  and passes tests, too.
- Descriptions taken from Chris Vaill's spec file.
