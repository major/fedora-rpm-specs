Name:           yersinia
Version:        0.8.2
Release:        19%{?dist}
Summary:        Network protocols tester and attacker

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.yersinia.net/
Source0:        https://github.com/tomac/yersinia/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         yersinia-format-strings.patch
Patch1:         yersinia-configure-c99-1.patch
Patch2:         yersinia-configure-c99-2.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  libnet-devel
BuildRequires:  gtk2-devel
BuildRequires:  ncurses-devel

%description
Yersinia is a network tool designed to take advantage of some weakeness
in different network protocols. It pretends to be a solid framework for
analyzing and testing the deployed networks and systems.

Currently, there are some network protocols implemented, but others are 
coming (tell us which one is your preferred). Attacks for the following
network protocols are implemented (but of course you are free for 
implementing new ones):

* Spanning Tree Protocol (STP)
* Cisco Discovery Protocol (CDP)
* Dynamic Trunking Protocol (DTP)
* Dynamic Host Configuration Protocol (DHCP)
* Hot Standby Router Protocol (HSRP)
* IEEE 802.1Q and IEEE 802.1X
* Inter-Switch Link Protocol (ISL)
* VLAN Trunking Protocol (VTP)

%prep
%autosetup -p1 -n %{name}-%{version}

# Don't override CFLAGS in configure* (RHBZ#1240089)
sed -i -e "s,^\(\s*CFLAGS=\".*\"\),:\1," configure*
# Avoid rerunning the autotools
touch -r aclocal.m4 acinclude.m4 configure*

# Convert to utf-8
for file in THANKS; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags} -fcommon"

%install
%make_install

%files
%doc AUTHORS ChangeLog FAQ README THANKS TODO
%license COPYING
%{_mandir}/man?/%{name}.*
%{_bindir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.2-18
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Florian Weimer <fweimer@redhat.com> - 0.8.2-13
- Port configure script to C99

* Sat Dec 10 2022 Florian Weimer <fweimer@redhat.com> - 0.8.2-12
- Apply upstream patch to fix FTBFS (#2113771)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-7
- Fix FTBFS (rhbz#1800287)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017  Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-1
- Update to latest upstream release 0.8.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 19 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.7.3-5
- Let configure honor CFLAGS (Fix F23FTBFS, RHBZ#1240089).
- Add %%license.
- Modernize spec.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 01 2013  Fabian Affolter <mail@fabian-affolter.ch> - 0.7.3-1
- Update to latest upstream release 0.7.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.1-9
- libnet rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.1-7
- Rebuild for new libpng

* Sun Oct 04 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.1-6
- Add --with-pcap-includes to fix build with libpcap 1.0

* Thu Sep 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-5
- Rebuild for new libpcap

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-2
- Added CFLAGS

* Tue Dec 23 2008 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Initial spec for Fedora
