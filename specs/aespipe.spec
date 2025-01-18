Summary:        AES-based encryption tool for tar/cpio and loop-aes imagemore
Name:           aespipe
Version:        2.4g
Release:        5%{?dist}
License:        GPL-2.0-or-later
URL:            http://loop-aes.sourceforge.net/
Source:         %{url}/aespipe/aespipe-v%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gpg
BuildRequires:  make
Requires:       gpg

%description
aespipe is an encryption tool that reads from standard input and
writes to standard output. It uses the AES (Rijndael) cipher.

It can be used as an encryption filter, to create and restore
encrypted tar/cpio backup archives and to read/write and convert
loop-AES compatible encrypted images.

aespipe can be used for non-destructive in-place encryption of
existing disk partitions for use with the loop-AES encrypted loop-back
kernel module.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%set_build_flags
%configure LDFLAGS="${CFLAGS}"

%global make_target %{nil}
%ifarch x86_64
%global make_target amd64
%endif
%ifarch %{ix86}
%global make_target x86
%endif
make %{?_smp_mflags} %{make_target}

%check
make tests

%install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/examples
cp -p ChangeLog README %{buildroot}%{_defaultdocdir}/%{name}
install -Dp -m0644 bz2aespipe %{buildroot}%{_defaultdocdir}/%{name}/examples
install -Dp -m0644 aespipe.1 %{buildroot}%{_mandir}/man1/aespipe.1
install -Dp -m0755 aespipe %{buildroot}%{_bindir}/aespipe


%files
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/*
%{_mandir}/man1/aespipe.1*
%{_bindir}/aespipe

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4g-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4g-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4g-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Jirka Hladky <hladky.jiri@gmail.com> - 2.4g-1
- Updated to version 2.4g. It sets -fno-strict-aliasing to WA RHEL-14046

* Wed Oct 18 2023 Jirka Hladky <hladky.jiri@gmail.com> - 2.4f-2
- WA got GCC bug https://issues.redhat.com/browse/RHEL-14046

* Sun Aug 09 2020 Jirka Hladky <hladky.jiri@gmail.com> - 2.4f-1
- Update to version 2.4f

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4e-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4e-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4e-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Jirka Hladky <hladky.jiri@gmail.com> - 2.4e-4
- Found the root cause with assembler linking - better patch

* Thu Aug 15 2019 Jirka Hladky <hladky.jiri@gmail.com> - 2.4e-3
- Imroved patch to solve the issues with assembler linking

* Wed Aug 14 2019 Jirka Hladky <hladky.jiri@gmail.com> - 2.4e-2
- Added patch to solve the issues with assembler linking

* Wed Aug 14 2019 Jirka Hladky <hladky.jiri@gmail.com> - 2.4e-1
- Update to version 2.4e

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 21 2015 Jirka Hladky <hladky.jiri@gmail.com> - 2.4d-2
- fixing build issue on F24

* Thu Aug 20 2015 Jirka Hladky <hladky.jiri@gmail.com> - 2.4d-1
- Update to version 2.4d

* Tue Jul 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.4c-10
- Add LDFLAGS=${CFLAGS} to %%configure (Fix F23FTBFS RHBZ#1239364).

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.4c-7
- Modernise spec, fixup scew with f20

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug  8 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.4c-5
- Use special %%doc to install docs (#993663).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4c-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul  3 2011 Jirka Hladky <jhladky@redhat.com> - 2.4c
  - Update to version 2.4c
* Sat Aug 28 2010 Jirka Hladky <jhladky@redhat.com> - 2.4b-3
  - Replaced global with define, see https://fedoraproject.org/wiki/Packaging/Guidelines#.25global_preferred_over_.25define
* Wed Aug 25 2010 Jirka Hladky <jhladky@redhat.com> - 2.4b-2
  - version 2.4b
  - cleaned up SPEC file
  - using MACROS everywhere
  - moved bz2aespipe into examples
* Fri Jan 22 2010 Dean Mander <knolderpoor@gmail.com> - 2.3e-4
  - added Requires:gpg
* Wed Dec 10 2008 Dean Mander <knolderpoor@gmail.com> - 2.3e-3
  - add make_target (to build on ppc)
  - add BuildRequires:gpg
  - add make tests
* Mon Nov 17 2008 Dean Mander <knolderpoor@gmail.com> - 2.3e-2
  - remove unneeded aclocal and autoconfig commands
  - corrected license to GPLv2+

* Tue Nov 11 2008 Dean Mander <knolderpoor@gmail.com> - 2.3e-1
  - bump to version 2.3e
  - set licence to GPL+ 
  - align to fedora standards

* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 2.3d-1 - +/
- Initial package. (using DAR)
