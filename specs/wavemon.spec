%undefine _hardened_build

Name:           wavemon
Version:        0.9.6
Release:        3%{?dist}
Summary:        Ncurses-based monitoring application for wireless network devices

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/uoaerg/wavemon
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libpcap-devel
BuildRequires:  libnl3-devel
BuildRequires:  autoconf
BuildRequires:  automake

%description
wavemon is a wireless device monitoring application that allows you to
watch all important information like device configuration, encryption,
and power management parameters and network information at once.
Adaptive level bargraphs for link quality, signal/noise strength and
signal-to-noise ratio.  The customizeable "level alarm" feature that 
notices the user of changes in signal level strength audibly and/or
visually. wavemon is able to list of access points in range and shows
full-screen level histogram displaying signal/noise levels and SNR.

%prep
%autosetup
sed -e '/^CFLAGS=/d' -i configure.ac
sed -r 's|\?=|=|g' -i Makefile.in
autoreconf -fiv

%build
CFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"
CXXFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"

export CFLAGS
export CXXFLAGS

%configure
make %{?_smp_mflags}

%install
%make_install
# Delete wrong placed doc files
rm -rf %{buildroot}%{_datadir}/%{name}/*

%files
%doc README.md
%license LICENSE
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.6-2
- convert license to SPDX

* Thu Jul 18 2024 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.6-1
- Update to 0.9.6 fixes rhbz#2298082

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Update to latest upstream release 0.9.5 (closes #2247215)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 19 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Update to latest upstream release 0.9.4 (closes rhbz#2005629)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Update to latest upstream release 0.9.3 (#1910950)

* Wed Oct 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.2-1
- Update to latest upstream release 0.9.2 (#1891272)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to latest upstream release 0.9.1 (#1787835)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to latest upstream release 0.9.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-1
- Update to latest upstream release 0.8.2 (#1546530)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.1-6
- Fix FTBFS rawhide

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-3
- Fix FTBFS (#1424537)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-1
- Update to latest upstream release 0.8.1 (#1396756)

* Sun Nov 20 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-2
- Fix build failure

* Tue Nov 08 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update to latest upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 19 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.7.6-6
- Don't overwrite CFLAGS in configure* (Fix F23FTBFS, #1240046).
- Add %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 30 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.6-4
- Update requirements

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.6-1
- Update to new upstream 0.7.6

* Fri Jan 17 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-7
- Update spec file

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-3
- Update to match new guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-1
- Update to new upstream 0.7.5

* Sat Mar 24 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.4-1
- Update to new upstream 0.7.4

* Sat Feb 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.3-1
- Update to new upstream 0.7.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-3
- Rebuild (wireless-tools)

* Sat Mar 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-1
- Update to new upstream 0.7.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Update to new upstream 0.7.1

* Tue Nov 02 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Update to new upstream 0.7.0

* Wed Aug 18 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.11-1
- Update to new upstream 0.6.11

* Thu Nov 19 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.10-1
- Update to new upstream 0.6.10

* Thu Aug 06 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.7-1
- Update to new upstream 0.6.7

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.6-1
- Update to new upstream 0.6.6

* Mon May 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.5-1
- Update to new upstream 0.6.5

* Mon May 04 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-2
- Add optflags to make

* Sat May 02 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- Update install and prep section
- Update to new upstream version 0.6

* Wed Feb 25 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-1
- Initial package for Fedora
