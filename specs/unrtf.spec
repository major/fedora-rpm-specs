Name:		unrtf
Summary:	RTF (Rich Text Format) to other formats converter
Version:	0.21.9
Release:	23%{?dist}

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/unrtf/unrtf.html
Source0:	ftp://ftp.gnu.org/gnu/unrtf/unrtf-%{version}.tar.gz

# http://hg.savannah.gnu.org/hgweb/unrtf/rev/3b16893a6406
Patch0001: 0001-Replace-all-instances-of-sprintf-with-snprintf-and-a.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	automake

%description
UnRTF is a command-line program written in C which converts documents in 
Rich Text Format (.rtf) to HTML, LaTeX, troff macros, and RTF itself. 
Converting to HTML, it supports a number of features of Rich Text Format:
    * Changes in the text's font, size, weight (bold), and slant (italic)
    * Underlines and strikethroughs
    * Partial support for text shadowing, outlining, embossing, or engraving
    * Capitalizations
    * Superscripts and subscripts
    * Expanded and condensed text
    * Changes in the foreground and background colors
    * Conversion of special characters to HTML entities 

%prep
%autosetup -p1

%build
# The ./configure command (specifically the symlinks in the ./config/
# directory) assume that automake is present in an "automake-1.13" directory.
# That is the case on EL7, but it's not the case in Fedora. That is why we
# regenerate the automake/autoconf bits by running the ./bootstrap script here.
./bootstrap
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make check

%files
%doc README ChangeLog COPYING AUTHORS NEWS
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.21.9-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.21.9-8
- Switch to %%autosetup
- Patch for CVE-2016-10091

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.21.9-1
- Upstream release 0.21.9 (RHBZ #1176987)
- Regenerate the automake/autoconf bits with ./bootstrap in order to eliminate
  the dependency on the automake-1.13 path.

* Wed Dec 17 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.21.7-1
- Upstream release 0.21.7 (RHBZ #1175241)

* Wed Dec 10 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.21.6-2
- Drop NEWS file (upstream didn't ship this in 0.21.6)

* Wed Dec 10 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.21.6-1
- Upstream release 0.21.6 (RHBZ #1172664)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.21.5-2
- don't alter conf file location (rhbz#1060513)

* Mon Apr 07 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.21.5-1
- Upstream release 0.21.5 (RHBZ #979619)
- Update URL for HTTPS
- Enable tests in %%check

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.21.4-1
- upstream release 0.21.4

* Thu Jan 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.21.2-1
- upstream release 0.21.2

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 07 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.21.1-1
- Bump up to the latest release
- Drop patches
- Update description
- License has changed from GPLv2+ to GPLv3+
- Update spec to match latest guidelines

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.20.2-4
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.20.2-3
- fix license tag
- rebuild for BuildID

* Sat Mar 03 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.20.2-2
- add patches from bugs 225188 and 225184

* Fri Sep 08 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.20.2-1
- version 0.20.2

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.19.9-1
- version 0.19.9

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.19.3-4
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 11 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 0.19.3-0.fdr.2
- Build with rpm opt flags.

* Thu May 13 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.19.3-0.fdr.1
- initial Fedora RPM (from Mandrake)

