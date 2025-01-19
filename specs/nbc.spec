Name:           nbc
Version:        1.2.1.r3
Release:        32%{?dist}
Summary:        Simple language and compiler to program the LEGO NXT brick
URL:            http://bricxcc.sourceforge.net/nbc/
# Automatically converted from old format: MPLv1.1 - review is highly recommended.
License:        LicenseRef-Callaway-MPLv1.1
Source0:        http://downloads.sourceforge.net/bricxcc/%{name}-%{version}.src.tgz

# This patch fixes the installation paths for the binary and manpage, 
# and adds a -g to the Pascal buildflags so a debuginfo package
# can be generated.  Not yet submitted upstream
Patch0:         %{name}-1.2.1.r3.fixinstall.patch

# Match fpc architectures
ExclusiveArch:  %{fpc_arches}
BuildRequires: make
BuildRequires:  glibc-devel
BuildRequires:  fpc
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  dos2unix

%description
Next Byte Codes (NBC) is a simple language with an assembly language
syntax that can be used to program LEGO's NXT programmable brick
(from the new LEGO Mindstorms NXT set).

Not Exactly C (NXC) is a high level language, similar to C, built on
top of the NBC compiler. It can also be used to program the NXT brick.
NXC is basically NQC (Not Quite C) for the NXT.

%prep
%setup -c -q
%patch -P0 -p0 -b .fixinstall

cd doc
for f in Readme Changelog; do
  dos2unix -n $f $f.tmp && \
  touch -r $f $f.tmp && \
  mv $f.tmp $f
done

%build
make

%install
make install DISTDIR=%{buildroot}

%files
%doc doc/Changelog doc/Readme
%{_bindir}/nbc
%{_mandir}/man1/nbc.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1.r3-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Rich Mattes <richmattes@gmail.com> - 1.2.1.r3-26
- Update BuildRequires and remove parallel make
- Resolves: rhbz#2113542

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.r3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.r3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.r3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.r3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.r3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.r3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.r3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.r3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Dan Horák <dan[at]danny.cz> - 1.2.1.r3-4
- fpc not available on s390(x)

* Tue Mar 01 2011 Rich Mattes <richmattes@gmail.com> - 1.2.1.r3-3
- Patch build system so it doesn't gzip manpage
- Preserve manpage timestamp
- Preserve timestamps in dos2unix call
- Add smp_mflags

* Sun Jan 09 2011 Rich Mattes <richmattes@gmail.com> - 1.2.1.r3-2
- Fixed manpage installation
- Added -g to build flags to generate debuginfo
- Fixed typos in specfile

* Thu Dec 30 2010 Martin Langhoff <martin@laptop.org> - 1.2.1.r3-1
- Initial package

