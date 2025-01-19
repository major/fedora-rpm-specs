# There's no svgalib in RHEL or on non-x86 platforms
%if 0%{?rhel} && 0%{?rhel} < 7
%ifarch %{ix86} x86_64
%bcond_without svgalib
%else
%bcond_with svgalib
%endif
%bcond_with svgalib
%endif

Name:           links
Version:        2.20.2
Release:        17%{?dist}
Epoch:          1
Summary:        Web browser running in both graphics and text mode
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://links.twibright.com/
Source0:        http://links.twibright.com/download/%{name}-%{version}.tar.bz2
Source1:        links.desktop
Patch0:         links-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gpm-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  autoconf automake
BuildRequires:  openssl-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libevent-devel
%if %with svgalib
BuildRequires:  svgalib-devel
%endif

Requires(preun): %{_sbindir}/alternatives
Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives
Requires(post): coreutils
Requires(postun): coreutils

Provides:       webclient


%description
Links is a web browser capable of running in either graphics or text mode.
It provides a pull-down menu system, renders complex pages, has partial HTML
4.0 support (including tables, frames and support for multiple character sets
and UTF-8), supports color and monochrome terminals and allows horizontal
scrolling.


%prep
%autosetup -p1


%build
iconv -f ISO-8859-1 -t UTF-8 AUTHORS >converted.AUTHORS
touch -r AUTHORS converted.AUTHORS
mv converted.AUTHORS AUTHORS

%configure --enable-graphics --with-ssl
make %{?_smp_mflags}


%install
make install DESTDIR=${RPM_BUILD_ROOT}
mv %{buildroot}/%{_bindir}/links $RPM_BUILD_ROOT/%{_bindir}/links2
mv %{buildroot}/%{_mandir}/man1/links.1 $RPM_BUILD_ROOT/%{_mandir}/man1/links2.1
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
install -D -p Links_logo.png %{buildroot}/%{_datadir}/pixmaps/links.png

# Alternatives cruft
touch %{buildroot}%{_bindir}/links
touch %{buildroot}%{_mandir}/man1/links.1.gz


%postun
[ $1 = 0 ] && exit 0
[ $(readlink %{_sysconfdir}/alternatives/links) = %{_bindir}/links2 ] &&
        %{_sbindir}/alternatives --set links %{_bindir}/links2
exit 0


%preun
[ $1 = 0 ] || exit 0
%{_sbindir}/alternatives --remove links %{_bindir}/links2


%post
%{_sbindir}/alternatives \
        --install %{_bindir}/links links %{_bindir}/links2 80 \
        --slave %{_mandir}/man1/links.1.gz links-man %{_mandir}/man1/links2.1.gz
[ $(readlink %{_sysconfdir}/alternatives/links) = %{_bindir}/links2 ] &&
        %{_sbindir}/alternatives --set links %{_bindir}/links2
exit 0


%files
%doc doc/* AUTHORS KEYS README COPYING
%{_bindir}/links2
%{_mandir}/man1/links2.1*
%{_datadir}/pixmaps/links.png
%{_datadir}/applications/links.desktop
%ghost %verify(not md5 size mtime) %{_bindir}/links
%ghost %verify(not md5 size mtime) %{_mandir}/man1/links.1.gz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1:2.20.2-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 1:2.20.2-11
- Fix C99 compatibility issues in configure script (#2167366)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:2.20.2-7
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 20:34:09 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.20.2-4
- Rebuilt for libevent 2.1.12

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Lubomir Rintel <lkundrak@v3.sk> - 1:2.20.2-1
- New release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Lubomir Rintel <lkundrak@v3.sk> - 1:2.17-1
- New release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Lubomir Rintel <lkundrak@v3.sk> - 1:2.14-1
- New release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:2.13-1
- New release

* Mon Apr 18 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:2.12-2
- Drop text mode browser provide

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:2.12-1
- New release
- Drop the SSL verification patch; upstream does it now

* Wed Jul 15 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:2.10-3
- Add libevent dependency

* Wed Jul 15 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:2.10-2
- Add RSVG dependency for SVG rendering

* Wed Jul 15 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:2.10-1
- Rebase to new release
- Drop the google patch -- upstream does a better job now

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:2.9-2
- Fix X11 and SVGALib backends

* Mon Jan 05 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:2.9-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1:2.8-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Mon Sep 23 2013 Ondrej Vasik <ovasik@redhat.com> - 1:2.8-1
- new upstream release 2.8 (#1010890)

* Fri Sep 13 2013 Ondrej Vasik <ovasik@redhat.com> - 1:2.7-1
- new upstream release 2.7 (#835427)
- remove IPv6 Fedora patch, supported upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1:2.6-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1:2.6-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Ondrej Vasik <ovasik@redhat.com> - 1:2.6-1
- rebase to latest upstream (#751354)
- apply IPv6 support patch
- removed nss patch(already included upstream)
- use openssl instead of nss again (nss upstream support has some
  header detection troubles)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1:2.2-14
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 27 2009 Ondrej Vasik <ovasik@redhat.com> - 1:2.2-12
- add Requires(post) and Requires(postun) for coreutils (readlink)
  (#540434)

* Sat Oct 17 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.2-11
- Do not display textareas hidden by CSS

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.2-9
- Add epoch to beat elinks obsoletes

* Mon Apr 13 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.2-8
- Enable SSL certificates verification

* Sun Apr 12 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.2-7
- removing unnecessary BuildConflicts

* Fri Apr 10 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.2-6
- Cosmetic fixes
- Ship license

* Fri Apr 03 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.2-5
- Add SSL/TLS support by the means of NSS
- Add web browser provides

* Thu Apr 02 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.2-4
- Do not silence make
- Use bundled icon, place it in pixmaps directory
- Adjust summary, description and style
- Remove useless configure parameters
- Include X11 support
- Adjust menu entry text
- Add alternatives support

* Mon Nov 10 2008 johnhford@gmail.com - 2.2-3
- Do not mutilate timestamps on AUTHORS
- Removed vendor from desktop-file-install
- No longer gzipping manpage

* Mon Nov 10 2008 John Ford <johnhford.gmail@com> 2.2-2
- Modified %%build to ensure shared libraries are used
- Added missing requirements (desktop-file-utils)
* Sat Nov 08 2008 John Ford <johnhford.gmail@com> 2.2-1
- Initial Submission

