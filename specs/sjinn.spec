Name:           sjinn
Version:        1.01
Release:        33%{?dist}
Summary:        Simple tool for sending & receiving data from RS-232 devices

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sjinn.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

# installer should use 0644 permissions for man page
# https://sourceforge.net/tracker/?func=detail&aid=3294964&group_id=26187&atid=386394
Patch0:         sjinn-install-args.patch

# Add DESTDIR as argument for install
# https://sourceforge.net/tracker/?func=detail&aid=3294967&group_id=26187&atid=386394
Patch1:         sjinn-install-DESTDIR.patch

# Uncompress man pages
# https://sourceforge.net/tracker/?func=detail&aid=3294981&group_id=26187&atid=386394
Patch2:         sjinn-uncompress-man-pages.patch

# Fix optstring for proper -r handling
# https://sourceforge.net/tracker/?func=detail&aid=3324235&group_id=26187&atid=386394
Patch3:         sjinn-optarg-r-fix.patch
Patch4: sjinn-configure-c99.patch


%description
S-Jinn is a free, lightweight, open-source Linux application written in
C. It is a simple command-line tool designed for sending & receiving
data from PC controlled TIA/EIA-232 (RS-232) test, measurement,
and control devices.

Depending on your application you may be able to use stty or
C-Kermit, but I believe you will find that S-Jinn is easier-to-use,
more intuitive, and more concise in the area of command-line and/or
scripted RS-232 data acquisition and control.

Popular Linux communications packages like Minicom will also
communicate with RS-232 devices, but they are better suited to modems,
computers, network devices, etc. They typically lack support for any
combination of UART communication settings required by many of the
RS-232 test, measurement, and control devices on the market.

Most communications packages also lack command-line support. Some
provide scripting languages, but S-Jinn frees you from
application-specific languages. S-Jinn simply directs the data to
STDOUT where you can display it, pipe it, and/or redirect it to
be processed by your favorite Unix shell and/or scripting language
regardless of whether you prefer Bash, Python, Perl, Expect, or you
name it.

Other S-Jinn features include the ability to:

    * Control RS-232 DTR and RTS lines from the command-line

    * Display DTR, RTS, CTS & DSR status

    * Send control characters (including the NULL character)

    * Send values in hex

    * Specify read length

    * Set programmable delay times for both send & read.

    * Support for virtually all baud rates, parity, and data lengths
      found in standard PC UARTS

    * Output Formatting: ASCII, hex, ASCII-over-hex, wrap text,
      truncate lines, suppress trailing line feeds


%prep
%setup -q -n %{name}
tar -xzf scripts.tar.gz
gunzip rs232.1.gz

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

# Fix some file permissions
chmod -x INSTALL COPYING README EXAMPLES FAQS ChangeLog Makefile \
        configure.in *.1 *.[ch] scripts/*

# Fix end-of-line encoding
sed -i 's/\r//' COPYING


%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}" prefix=%{_prefix}


%install
rm -rf %{buildroot}
make INSTALL="install -cDp" DESTDIR=%{buildroot} prefix=%{_prefix} \
        mandir=%{_mandir}/man1 install



%files
%{_bindir}/rs232
%{_bindir}/%{name}
%{_mandir}/man1/*
%license COPYING
%doc README EXAMPLES FAQS ChangeLog scripts


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.01-32
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 Florian Weimer <fweimer@redhat.com> - 1.01-28
- Port configure script to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 21 2018 John W. Linville <linville@redhat.com> - 1.01-18
- Add previously unnecessary BuildRequires for gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.01-16
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb  4 2015 John W. Linville <linville@redhat.com> - 1.01-10
- Use %%license instead of %%doc for file containing license information

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 John W. Linville <linville@redhat.com> - 1.01-3
- Fix optstring for proper -r handling

* Fri Apr 29 2011 John W. Linville <linville@redhat.com> - 1.01-2
- Remove executable bit from source files
- Add comments for patches, including upstream bug references
- Allow rpmbuild to handle man page compression
- Use non-macro sed invocation
- Decompress scripts tarball installed as doc
- Remove unneeded make arguments during install

* Mon Apr 18 2011 John W. Linville <linville@redhat.com> - 1.01-1
- Initial release for Fedora
