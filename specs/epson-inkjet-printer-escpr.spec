# The lsb release used in the tarball name
%global lsb 1lsb3.2

Name:           epson-inkjet-printer-escpr
Summary:        Drivers for Epson inkjet printers
Epoch:          1
Version:        1.7.21
Release:        9.%{lsb}%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
# Search for something like XP-7100
URL:            http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
# Download address is garbled on web page
Source0:        https://download3.ebz.epson.net/dsc/f/03/00/13/77/93/e85dc2dc266e96fdc242bd95758bd88d1a51963e/epson-inkjet-printer-escpr-1.7.21-1lsb3.2.tar.gz
# Patch from Arch Linux
# https://aur.archlinux.org/packages/epson-inkjet-printer-escpr/
Patch1:         epson-inkjet-printer-escpr-filter.patch
Patch2:         implicit-function-declaration.patch

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  chrpath
BuildRequires:  libtool
BuildRequires:  cups-devel
BuildRequires:  libjpeg-devel
BuildRequires:  make

# All current Fedoras and modern RHEL
%if 0%{?fedora} || 0%{?rhel} >= 8
# For automatic detection of printer drivers
BuildRequires:  python3-cups
%else
# For automatic detection of printer drivers
BuildRequires:  python-cups
%endif
# For dir ownership
Requires:       cups-filesystem

%description
This package contains drivers for Epson Inkjet printers that use 
the New Generation Epson Printer Control Language.

For a detailed list of supported printers, please refer to
http://avasys.jp/english/linux_e/

%prep
%setup -q 
%patch -P1 -p1 -b .filter
%patch -P2 -p1 -b .implicit-function-declaration
# Fix permissions
find . -name \*.h -exec chmod 644 {} \;
find . -name \*.c -exec chmod 644 {} \;
for f in README README.ja COPYING AUTHORS NEWS; do
 chmod 644 $f
done

%build
autoreconf -i
%configure --disable-static --enable-shared --disable-rpath
# SMP make doesn't work
#make %{?_smp_mflags}
make

%install
make install DESTDIR=%{buildroot} CUPS_PPD_DIR=%{_datadir}/ppd/Epson
# Get rid of .la files
rm -f %{buildroot}%{_libdir}/*.la
# Compress ppd files
for ppd in %{buildroot}%{_datadir}/ppd/Epson/epson-inkjet-printer-escpr/*.ppd; do
 gzip $ppd
done
# Get rid of rpath
chrpath --delete %{buildroot}%{_cups_serverbin}/filter/epson-escpr
# Copy documentation
cp -a README README.ja COPYING AUTHORS NEWS ..

# Get rid of .so file, since no headers are installed.
rm %{buildroot}%{_libdir}/libescpr.so

%ldconfig_scriptlets

%files
%doc README README.ja COPYING AUTHORS NEWS
%{_cups_serverbin}/filter/epson-*
%{_datadir}/ppd/Epson/
%{_libdir}/libescpr.so.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.21-9.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.7.21-8.1lsb3.2
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.21-7.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.21-6.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.21-5.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.21-4.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.21-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Timm Bäder <tbaeder@redhat.com> - 1:1.7.21-2.1lsb3.2
- Fix an implicit function declaration
- https://fedoraproject.org/wiki/Toolchain/PortingToModernC

* Wed Sep 28 2022 Orion Poplawski <orion@nwra.com>  - 1:1.7.21-1.1lsb3.2
- Update to 1.7.21
- Update conditionals

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.18-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.7.18-1.1lsb3.2
- Update to 1.7.18.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.10-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.10-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.7.10-1.1lsb3.2
- Update to 1.7.10.

* Tue Mar 16 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.7.9-1.1lsb3.2
- Update to 1.7.9.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.7-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.7.7-1.1lsb3.2
- Update to 1.7.7.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.41-4.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.41-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.41-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.41-1.1lsb3.2
- Update to 1.6.41.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.30-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.30-1.1lsb3.2
- Update to 1.6.30.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.20-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.20-1.1lsb3.2
- Update to 1.6.20.

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:1.6.17-4.1lsb3.2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.17-3.1lsb3.2
- Added gcc buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.17-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.17-1.1lsb3.2
- Update to 1.6.17.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.13-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.13-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.13-1.1lsb3.2
- Update to 1.6.13.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.10-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.10-2.1lsb3.2
- Fix FTBFS in rawhide.
- Add patch that fixes crashes (BZ #1400346).

* Thu Nov 24 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.10-1.1lsb3.2
- Update to 1.6.10.

* Sun Apr 24 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.5.2-3.1lsb3.2
- Roll back to 1.5.2 due to serious bug in 1.6.x series.

* Sun Apr 24 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.6.5-1.1lsb3.2
- Update to 1.6.5.

* Thu Mar 31 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.6.4-1.1lsb3.2
- Make sure driver provides are autodetected (BZ #1323033).
- Update to 1.6.4.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.5.2-1.1lsb3.2
- Update to 1.5.2.

* Tue Aug 11 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.5.0-1.1lsb3.2
- Update to 1.5.0.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Orion Poplawski <orion@cora.nwra.com> - 1.4.3-1.1lsb3.2
- Update to 1.4.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.1-1.1lsb3.2
- Added BR: python-cups (BZ #1049528).
- Update to 1.3.1.

* Sun Nov 03 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.0-1.1lsb3.2
- Update to 1.3.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1.1lsb3.2
- Update to 1.2.3
- spec cleanup

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1-1.1lsb3.2
- Update to 1.1.1.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1lsb3.2
- Update to 1.1.0.

* Sun Aug 28 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.4-3.1lsb3.2
- No sense in shipping .so file without headers; dropped -devel.

* Wed Jul 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.4-2.1lsb3.2
- Get rid of rpath.

* Mon Jul 11 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.4-1.1lsb3.2
- First release.
