Name:           fuse-emulator-utils
Version:        1.4.3
Release:        11%{?dist}
Summary:        Additional utils for the Fuse spectrum emulator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fuse-emulator.sourceforge.net
Source:         http://downloads.sourceforge.net/fuse-emulator/fuse-utils-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  audiofile-devel >= 0.2.3
BuildRequires:  glib2-devel
BuildRequires:  newt-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libspectrum-devel >= 1.4.3
BuildRequires:  zlib-devel
BuildRequires: make

%description
A collection of utilities for the Fuse ZX-Spectrum emulator


%prep
%setup -q -n fuse-utils-%{version}


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_mandir}/man1/*.1.gz
%{_bindir}/*
%doc AUTHORS COPYING README ChangeLog


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.3-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.3-1
- sync with latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.2-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.5-1
- new upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.1-1
- new upstream release

* Wed Oct 05 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.0-1
- new upstream release

* Sat Jun 11 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.0-3
- bump BR libspectrum version (thanks Sergio B)

* Wed Jun 08 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.0-2
- bump version for missing sources file

* Wed Jun 08 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.0-1
- update BR
- drop all patches (fixed upstream)
- update to latest upstream

* Thu Feb 18 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.1.1-8
- modernize specfile
- use upstream patch to fix extern declaration (fixes FTBFS)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 1.1.1-3
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Lucian Langa <cooly@gnome.eu.org> - 1.1.1-1
- new upstream release

* Thu May 23 2013 Lucian Langa <cooly@gnome.eu.org> - 1.1.0-1
- new upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 Lucian Langa <cooly@gnome.eu.org> - 1.0.0-5
- rebuilt with newer libaudiofile

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Lucian Langa <cooly@gnome.eu.org> - 1.0.0-1
- update patch0
- new upstream release

* Sat Feb 13 2010 Lucian Langa <cooly@gnome.eu.org> - 0.10.0.1-5
- update build requires

* Sat Feb 13 2010 Lucian Langa <cooly@gnome.eu.org> - 0.10.0.1-4
- fix implicit dso linking (#565062)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10.0.1-1
- new upstream package (package was missing files)

* Wed Dec 10 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10.0-2
- upstream released broken package (missing files)

* Fri Dec 05 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10.0-1
- new upstream 0.10.0 release

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9.0-3
fix for #458818

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.0-2
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.9.0-1
- Upgrade to 0.9.0
- Added several new BRs for the new version

* Tue Aug 21 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.0.1-2
- Release bump for F8 mass rebuild
- License change due to new guidelines

* Sat Jul 07 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.0.1-1
- Upgrade to 0.8.0.1
- Various cleanups to the SPEC including conforming to new guidelines

* Sat Sep 16 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.0-5
- rebuild

* Sun Jun 4 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.0-4
- Spec file fixes
- Added back in the 64 bit architecture

* Thu Feb 9 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.0-3
- Included ExcludeArch for x86_64 and ia64
- Fixed the package name correctly

* Fri Jan 13 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.0-2
- Renamed packed to fuse-emulator-utils

* Thu Sep 1 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.7.0-1.fc
- Initial build for FC
