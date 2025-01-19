%define _default_patch_fuzz 2
Summary: An interpreter for AGI games
Name: nagi
Version: 2.06
Release: 38%{?dist}
License: MIT
URL: http://www.agidev.com/projects/nagi/
Source0: http://www.agidev.com/dl_files/nagi/nagi_src_-_2002-11-14.tar.gz
Source1: nagi.sgml
Patch0: nagi-2.06-debian.patch 
Patch1: nagi-2.06-build_with_gcc-3.4.patch
Patch2:nagi-2.06-build_with_gcc-4.0.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: docbook-utils, SDL-devel, SDL-static
%description
NAGI is an interpreter for AGI games, such as the early Space Quest,
Leisure Suit Larry and King's Quest games.

%prep
%setup -qcn nagi

%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0

%build
export CFLAGS="$RPM_OPT_FLAGS -fcommon"
cd src
make -f Makefile.linux
docbook2man %{SOURCE1} 
cd ..
sed -i 's/\r//' license.txt
sed -i 's/\r//' readme.html

%install
mkdir -p %{buildroot}/%{_bindir}
install -Dp -m755 bin/nagi %{buildroot}/%{_bindir}/nagi
mkdir -p %{buildroot}%{_datadir}/nagi
install -Dp -m644 bin/*.nbf %{buildroot}%{_datadir}/nagi/
mkdir -p %{buildroot}%{_sysconfdir}/nagi
install -Dp -m644 bin/nagi.ini %{buildroot}%{_sysconfdir}/nagi/
install -Dp -m644 bin/standard.ini %{buildroot}%{_sysconfdir}/nagi/
mkdir -p %{buildroot}%{_mandir}/man1
install -Dp -m644 src/nagi.1 %{buildroot}%{_mandir}/man1

%files
%license license.txt
%doc readme.html
%{_bindir}/nagi 
%{_datadir}/nagi/
%config(noreplace) %{_sysconfdir}/nagi/
%{_mandir}/man1/nagi.1.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.06-33
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.06-26
- Fix FTBFS.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Jon Ciesla <limb@jcomserv.net> 2.06-6
- Patch fuzz workaround, will fix.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> 2.06-5
- GCC 4.3 rebuild.
- BR SDL-static.

* Tue Aug 21 2007 Jon Ciesla <limb@jcomserv.net> 2.06-4
- Rebuild for f8.

* Thu May 17 2007 Jon Ciesla <limb@jcomserv.net> 2.06-3
- Fixed RPM_OPT_FLAGS.
- Fixed build path issues.
- Preserved timestamps.

* Thu May 17 2007 Jon Ciesla <limb@jcomserv.net> 2.06-2
- Changed to literal sed.
- Cleaned up dir creation.
- Corrected patch names.

* Thu May 17 2007 Jon Ciesla <limb@jcomserv.net> 2.06-1
- Fixed license tag, version.

* Tue May 15 2007 Jon Ciesla <limb@jcomserv.net> 0.1-20021114
- Fixed dos2unix/sed, SDL-devel BR.

* Tue May 01 2007 Jon Ciesla <limb@jcomserv.net> 0.1-20021114
- Inital packaging.
