Name:           tcpjunk
Version:        2.9.03
Release:        28%{?dist}
Summary:        TCP protocols testing tool

License:        GPLv2+
URL:            http://code.google.com/p/tcpjunk/
Source0:        http://tcpjunk.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         tcpjunk-2.9.03-add-libcrypto.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  gtksourceview2-devel
BuildRequires:  pkgconfig

BuildRequires:  desktop-file-utils

%description
TCPJunk is a TCP protocols manipulation and hacking utility that can
be used in different ways. Similar to netcat, TCPJunk can be used as
a client or server, but instead of stdin, it uses a 'Session file' as
the data to send or receive. TCPJunk can be used as a general testing
tool, a traffic generator or a fuzzer, for protocols such as HTTP,
SMTP, POP3, IMAP, FTP and others.

%prep
%setup -q
%patch0 -p1
# Cleanup the sources
rm -rf .anjuta autom4te.cache *.bak Optimized $(find -name .cvsignore)

%build
%configure
make %{?_smp_mflags}  CFLAGS="${RPM_OPT_FLAGS} -fcommon"

%install
make install DESTDIR=%{buildroot} \
    manpagedir=%{_mandir}/man1 INSTALL="install -p"
desktop-file-install                                    \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -rf %{buildroot}/usr/doc/%{name}

%files
%doc AUTHORS ChangeLog TODO.tasks
%license COPYING
%{_mandir}/man*/%{name}*.gz
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.9.03-26
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.03-22
- Fix FTBFS (rhbz#1800185)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 28 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.9.03-12
- Add tcpjunk-2.9.03-add-libcrypto.patch (Fix F23FTBFS, RHBZ#1240060).
- Add %%license.
- Cleanup the sources.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.03-8
- Updated spec file
- Fixed FTBFS (#992783)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.9.03-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 06 2010 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.03-1
- Updated to new upstream version 2.9.03

* Sun Feb 21 2010 Fabian Affolter <mail@fabian-affolter.ch> - 2.8.21-1
- Updated to new upstream version 2.8.21

* Wed Oct 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.8.01-1
- Updated to new upstream version 2.8.01

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.7.01-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.01-1
- Updated to new upsteram version 2.7.01

* Mon Jul 06 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.92-1
- Updated to new upsteram version 2.6.92

* Sat Jun 13 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.87-1
- Updated to new upsteram version 2.6.87

* Mon Apr 20 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.660-1
- Updated to new upsteram version 2.660

* Tue Mar 10 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.649-2
- Changed license

* Sun Feb 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.649-1
- Updated to new upstream version 2.649
- .desktop file and icon are now in the source
- Added the doc files and configure

* Sun Feb 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 2.643-1
- Initial spec for Fedora

