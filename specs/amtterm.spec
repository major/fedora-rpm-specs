Name:         amtterm
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:      GPL-2.0-or-later
Version:      1.6
Release:      24%{?dist}
Summary:      Serial-over-lan (sol) client for Intel AMT
URL:          http://www.kraxel.org/blog/linux/amtterm/
Source:       http://www.kraxel.org/releases/%{name}/%{name}-%{version}.tar.gz

Requires:     xdg-utils
Requires:     perl(SOAP::Lite)

BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: make

%description
Serial-over-lan (sol) client for Intel AMT.
Includes a terminal and a graphical (gtk) version.
Also comes with a perl script to gather informations
about and remotely control AMT managed computers.

%prep
%setup -q

%build
%{set_build_flags}
make prefix=/usr

%install
make prefix=/usr DESTDIR=%{buildroot} STRIP="" install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/gamt.desktop

%files
%doc COPYING
%{_bindir}/amtterm
%{_bindir}/amttool
%{_bindir}/gamt
%{_mandir}/man1/amtterm.1.gz
%{_mandir}/man1/amttool.1.gz
%{_mandir}/man1/gamt.1.gz
%{_mandir}/man7/amt-howto.7.gz
%{_datadir}/applications/gamt.desktop

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Gerd Hoffman <kraxel@redhat.com> - 1.6-12
- Add missing perl dependency for amttool.
- Resolves: rhbz#1869766

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Florian Weimer <fweimer@redhat.com> - 1.6-5
- Use %%{set_build_flags} to set both CFLAGS and LDFLAGS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Gerd Hoffman <kraxel@redhat.com> - 1.6-1
- Update to release 1.6.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Gerd Hoffmann <kraxel@redhat.com> - 1.4-1
- Update to release 1.4.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.3-6
- Perl 5.18 rebuild

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.3-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3-2
- Rebuild for new libpng

* Thu May 26 2011 Gerd Hoffmann <kraxel@redhat.com> - 1.3-1
- update to version 1.3

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Gerd Hoffmann <kraxel@redhat.com> - 1.2-1
- update to version 1.2
  * support special reboot commands (pxe, bios. ...).
  * gamt: gui tweaks, logging support.

* Thu Oct 30 2008 Gerd Hoffmann <kraxel@redhat.com> - 1.1-3
- update to version 1.1
  * handle BIOS-over-SOL.
  * some minor doc tweaks.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-2
- Autorebuild for GCC 4.3

* Fri Aug 31 2007 Gerd Hoffmann <kraxel@redhat.com> - 1.0-1
- update to version 1.0
  * more amttool improvements (network config).
- don't strip binaries (bug #269241).
* Fri Aug 24 2007 Gerd Hoffmann <kraxel@redhat.com> - 0.99-1
- update to version 0.99
  * add manual pages.
  * add desktop file.
  * improve amttool alot.
  * misc bug fixes.
- add amttool to the package description.
* Tue Aug 21 2007 Gerd Hoffmann <kraxel@redhat.com> - 0.5-1
- update to version 0.5
  * clarify license (GPLv2+).
  * keyboard tweaks.
  * cursor blink option.
- fix specfile bugs pointed out by review.
* Mon Aug 20 2007 Gerd Hoffmann <kraxel@redhat.com> - 0.4-1
- update to version 0.4
  * minur gui tweaks.
  * started tool to control machines.
* Thu Aug 16 2007 Gerd Hoffmann <kraxel@redhat.com> - 0.3-1
- update to version 0.3
  * gui improvements.
* Wed Aug 15 2007 Gerd Hoffmann <kraxel@redhat.com> - 0.2-1
- update to version 0.2
  * added gui (gtk) version.
  * some protocol fixups.
* Thu Aug 09 2007 Gerd Hoffmann <kraxel@redhat.com> - 0.1-1
- initial release
