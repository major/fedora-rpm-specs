# Building the Enchant Voikko provider is disabled by default because it should
# be included in Enchant 1.4.
# Pass '--with enchant' on rpmbuild command-line to enable it.
%bcond_with enchant

Name:           tmispell-voikko
Version:        0.7.1
Release:        37%{?dist}
Summary:        An Ispell compatible front-end for spell-checking modules

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org/
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
# Keyring created by running
# gpg2 --export --export-options export-minimal "AC5D 65F1 0C85 96D7 E2DA E263 3D30 9B60 4AE3 942E" > gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
# See https://voikko.puimula.org/sources.html
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Patch0:         tmispell-voikko-0.7.1-glib-2.31-fix.patch
Patch1:         0001-redraw_minimenu-add-format-string.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libvoikko-devel ncurses-devel gettext glibmm24-devel
%if %{with enchant}
BuildRequires: enchant-devel
%endif

%description
Tmispell is an Ispell compatible front-end for spell-checking
modules. To do the actual spell-checking for Finnish language it uses
the spell-checking system Voikko.

%package -n 	enchant-voikko
Summary:        Voikko spellchecker support for Enchant


%description -n enchant-voikko
Voikko spellchecker support for Enchant.

# TODO: /usr/bin/ispell should be a symlink to /usr/bin/tmispell and the real
# ispell should be renamed to e.g. /usr/bin/ispell.real for KDE etc. to work.
# The other option would be to modify /usr/bin/ispell to call
# /usr/bin/tmispell when it's called with Finnish. If neither of these can be
# done, it's worth it to have /usr/bin/tmispell as a command line client for
# Voikko.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%if %{with enchant}
%configure --disable-dependency-tracking
%else
%configure --disable-dependency-tracking --disable-enchant
%endif

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%if %{with enchant}
# Remove static archive
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove the symlinks and move the library itself into a better name
rm $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so.1 \
   $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so
mv $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so.* \
   $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so
%endif
# Install the configuration file
sed -i -e 's/ispell.real/ispell/' tmispell.conf.example
install -Dpm 0644 tmispell.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/tmispell.conf
# Fake Finnish dictionary for ispell clients. Commented out for now.
# These won't actually work for KDE etc. unless the binary is in
# /usr/bin/ispell (or /usr/bin/ispell calls tmispell). These files should always 
# be installed into %{_prefix}/lib/ispell/ even though it's an rpmlint error
# because my testing shows that KDE recognizes them from there but not from 
# /usr/share.
#install -dm 755 %{buildroot}%{_prefix}/lib/ispell
#touch %{buildroot}%{_prefix}/lib/ispell/suomi.{hash,aff}
%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README README.fi
%config(noreplace) %{_sysconfdir}/tmispell.conf
%{_mandir}/man1/tmispell*
%{_mandir}/man5/tmispell*
%{_bindir}/tmispell
# Fake dictionary directory, commented out for now
#%{_prefix}/lib/ispell

%if %{with enchant}
%files -n enchant-voikko
%{_libdir}/enchant/libenchant_voikko.so
%endif


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-36
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Ville-Pekka Vainio <vpvainio@iki.fi> - 0.7.1-31
- Verify source file
- Redo sources file with sha512 hashes

* Tue Aug 02 2022 Ville-Pekka Vainio <vpvainio@iki.fi> - 0.7.1-30
- Add format string patch to fix build
- Use autosetup
- Update URLs

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.1-14
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> - 0.7.1-10
- Add aarch64 patch from rhbz #926641

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for c++ ABI breakage

* Sat Feb 04 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 0.7.1-6
- Add patch to fix build with glib 2.31

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7.1-1
- New upstream release
- Remove upstreamed GCC 4.4 patch
- This package is considered deprecated by upstream and will receive only
  bugfixes from now on. Enchant (with the Voikko provider) should be used
  instead.

* Wed Feb 04 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-2
- Fix build with GCC 4.4

* Wed May 14 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-1
- Bump release for the first Fedora build

* Tue May 13 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.8
- Remove the enchant-voikko-devel package and the static library, which were
  introduced in -0.6 

* Mon May 12 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.7
- Remove the Voikko provider library symlinks and move the library itself to 
  be libenchant_voikko.so

* Mon May 12 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.6
- Add defattr to enchant-voikko
- Don't package the symlink libenchant_voikko.so.1
- Use bcond_with
- Add the enchant-voikko-devel package, which contains libenchant_voikko.a

* Sun May 11 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.5
- Make building the enchant provider conditional, disabled by default
- Add --disable-dependency-tracking to configure
- Cleanup BuildRequires

* Tue Mar 25 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.4
- Don't build the enchant provider plugin, it should be shipped with enchant
  1.4

* Sun Feb 17 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.3
- Upstream released 0.7, only minor changes to the RCs

* Wed Feb 13 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.2.rc2
- New RC, uses ncursesw instead of ncurses, UTF-8 problems should be fixed
- Add doc files AUTHORS and COPYING

* Tue Feb 12 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.7-0.1.rc1
- New RC, use this because it removes the glibmm library that was shipped with
  the package and uses the one in the system

* Mon Nov 26 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.6.3-0.1
- Initial package
