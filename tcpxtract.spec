# Note: the same spec is used on all distro versions including EPEL,
# hence BuildRoot and related cleanup stays in.

Name:           tcpxtract
Version:        1.0.1
Release:        36%{?dist}
Summary:        Tool for extracting files from network traffic
License:        GPLv2+
URL:            http://tcpxtract.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# from AUR, who got it from Debian
Patch0:         01_fixmanpage.patch
# From AUR
Patch1:         02-fix_png_header_bytes.patch
# from AUR, who got it from Debian
Patch2:         fix-excessive-sync.patch
# From AUR, who got it from Debian/Ubuntu
Patch3:         tcpxtract-fix-segfault.patch
# From Debian
Patch4:         50_fix-spelling-binary.patch
# Clean up compile noise
Patch5:         tcpxtract-1.0.1-cleancompile.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  flex-static flex
BuildRequires:  autoconf
BuildRequires:  bison


%description
tcpxtract is a tool for extracting files from network traffic based on
file signatures.
tcpxtract features the following:
 * Supports 26 popular file formats out-of-the-box. New formats can be
 added by simply editing its config file.
 * With a quick conversion, you can use your old Foremost config file
 with tcpxtract.
 * Custom written search algorithm is lightning fast and very scalable.
 * Search algorithm searches across packet boundries for total coverage
 and forensic quality.
 * Uses libpcap, a popular, portable and stable library for network data
 capture
 * Can be used against a live network or a tcpdump formatted capture file.


%prep
%setup -q
%patch0 -p1 -b .manfix
%patch1 -p1 -b .pngfix
%patch2 -p1 -b .syncfix
%patch3 -p1 -b .segfaultfix
%patch4 -p1 -b .typofix
%patch5 -p1 -b .cleancompile
%{__sed} -i.path -e '/DEFAULT_CONFIG_FILE/s#/usr/local/etc#%{_sysconfdir}#' tcpxtract.c

%build
autoconf

%configure
export LDFLAGS="-lfl"
%make_build


%install
%make_install


%files
%doc COPYING AUTHORS
%{_mandir}/man1/tcpxtract.1*
%config(noreplace) %{_sysconfdir}/tcpxtract.conf
%{_bindir}/tcpxtract


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.0.1-27
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.1-25
- apply patches from Arch/Debian/Ubuntu
- cleanup compile to minimize warnings

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 30 2014 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 1.0.1-19
- EPEL7 needs the same BR as Fedora

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 1.0.1-17
- Remove dependency on perl-Carp ( perl package bug, #924938)
 
* Sat Mar 23 2013 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 1.0.1-17
- Use newer autoconf in order to support ARM64
 
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Manuel "lonely wolf" Wolfshant  <wolfy@fedoraproject.org> 1.0.1-11
- Fix FTBFS for Fedora > 12 ( flex libs are now in their own package)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 09 2008 Manuel "lonely wolf" Wolfshant  <wolfy@fedoraproject.org> 1.0.1-8.2
- rebuilt for gcc-4.3.0

* Tue Aug 22 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-8.1
- rebuilt

* Tue Aug 8 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-8
- license clarification

* Fri Mar 8 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-7
- removing unused patch from spec

* Thu Mar 8 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-6
- adapt buildrequires for EPEL-4

* Wed Mar 7 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-5
- remove superflous hard coded path from %%configure

* Sat Mar 3 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-4
- really keep timestamps

* Sat Mar 3 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-3
- replace patch with a sed in %%prep
- keep timestamps of default config and man pages

* Sat Mar 3 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-2
- Include a patch to fix the fact that the configuration file is ignored at
runtime, despite "--prefix" at %%configure time

* Fri Mar 2 2007 lonely wolf <wolfy@pcnet.ro> 1.0.1-1
- Initial rpm version starting from scratch
