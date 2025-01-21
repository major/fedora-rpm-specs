Name: steghide
Summary: A steganography program
Version: 0.5.1
Release: 51%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only

URL: http://steghide.sourceforge.net
Source: http://prdownloads.sourceforge.net/steghide/steghide-%{version}.tar.gz
Patch0: steghide-0.5.1-gcc41.patch
Patch2: steghide-0.5.1-mhash.patch
Patch3: steghide-0.5.1-gcc43.patch
# gcc7.0 compatibility fixes
Patch4: steghide-0.5.1-gcc70.patch
# Remove docs we don't want to be installed
Patch5: steghide-0.5.1-docs.patch
# Enable tests to search for libraries in current directory
Patch6: steghide-0.5.1-perltests.patch


BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: automake autoconf git
BuildRequires: gettext-devel, libtool
BuildRequires: libmcrypt-devel >= 2.5.8-2
BuildRequires: mhash-devel, libjpeg-devel, zlib-devel

# needed for tests
BuildRequires: perl-FileHandle

Requires: libmcrypt >= 2.5.8-2

%description
Steghide is a steganography program that is able to hide data in various kinds
of image- and audio-files. The color- respectivly sample-frequencies are not
changed thus making the embedding resistant against first-order statistical
tests. Features of steghide include compression and encryption of embedded
data,

embedding of a checksum to verify the integrity of the extracted data and
support for jpeg, bmp, wav and au files.

%prep
%autosetup -p 1 -S git

# Prevent configure from overriding CXXFLAGS
sed -i -e 's,^\(\s*CXXFLAGS="-O2 -Wall\),#\1,' configure.in
git commit -a -m "Prevent configure from overriding CXXFLAGS"

%build
aclocal
libtoolize --force
automake --add-missing
autoreconf
%configure
%make_build

%install
%make_install

%find_lang %name

%check
make check

%files -f %name.lang
%_pkgdocdir
%license COPYING
%{_bindir}/steghide
%{_mandir}/man1/steghide.1*

%Changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-50
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 David Kaufmann <astra@ionic.at> - 0.5.1-41
- add dependency to perl-FileHandle to fix test script

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-40
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Michal Ambroz <rebus _AT seznam.cz> - 0.5.1-34
- fix the perl tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5.1-30
- Add steghide-0.5.1-gcc70.patch (Fix F26FTBFS, RHBZ#1424475).
- Rework doc handling (Add steghide-0.5.1-docs.patch).
- Add %%license.
- Cleanup and modernize spec.
- Activate testsuite.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Michal Ambroz <rebus _AT seznam.cz> - 0.5.1-28
- rebuild for the newer gcc

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-25
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.5.1-21
- Try to fix aarch64 build issue (#926575)
- Disable 'make check' to solve a odd ccache related permission issue

* Mon Feb 18 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.5.1-20
- Rework aclocal/automake/autoreconf

* Sun Feb 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.5.1-9
- Rebuild for gcc-4.3

* Thu Jan 17 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.5.1-8
- Fix issues for compiling with gcc-4.3

* Tue Oct  9 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.5.1-7
- Add Req to libmcrypt >= 2.5.8-3 (#275641)

* Fri Aug 31 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.5.1-5
- Configuring belongs to the prep phase not build.

* Wed Aug  8 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.5.1-4
- Changing license tag

* Tue Apr 17 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.5.1-3
- Fix build problems on FC-7 (#235505)

* Sun Sep  3 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.5.1-2
- Rebuild for FC-6

* Tue Jul 11 2006 Jochen Schmitt <Jochen her-schmitt de> 0.5.1-1
- Initial RPM
