Name:           websec
Version:        1.9.0
Release:        39%{?dist}
Summary:        Web Secretary - Web page monitoring software with highlighting

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/baruch/websec
Source0:        websec-1.9.0.tar.gz
# Patch0: newer GNU Make versions (3.82, maybe older as well) get confused by
# parts of the Makefile that are unused anyway, so remove them with this patch;
# upstream is dead afaics
Patch0:         %{name}-disable-htmldocs
# Patch1: Background in https://bugzilla.redhat.com/show_bug.cgi?id=1254288
# not send upstream, as its dead
Patch1:         %{name}-silence-unescaped-left-brace-warnings.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl-generators

# needed to send mail:
Requires:       /usr/sbin/sendmail
# needed for ssl:
Requires:       perl(IO::Socket::SSL)
Requires:       perl(LWP::Protocol::https)

%description
Web Secretary is a web page change monitoring software. It will detect changes
based on content analysis, making sure that it's not just HTML that changed,
but actual content. You can tell it what to ignore in the page (hit counters
and such), and it can mail you the document with the changes highlighted or 
load the highlighted page in a browser.


%prep
%setup -q
%patch -P0 -p1 -b .patch0
%patch -P1 -p1 -b .patch1


%build
make PREFIX=%{_prefix} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT .__doc
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

# proper permissions for man pages
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/man/man*/*

# temp doc dir 
mv $RPM_BUILD_ROOT%{_datadir}/doc/websec .__doc

# having the next two in the proper place would require proper dependencies,
# which is probably not worth the trouble as that would be bloat for most 
# users; so ship them as doc, that's better then not shipping them at all
mv $RPM_BUILD_ROOT%{_datadir}/vim/vim61 $RPM_BUILD_ROOT%{_datadir}/emacs/ \
   .__doc/
mkdir .__doc/scripts
cp rollback htmldiff .__doc/scripts/
chmod -x .__doc/scripts/*



%files
%doc COPYING HACKING NEWS TODO .__doc/*
%{_bindir}/*
%{_datadir}/man/man*/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.0-38
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.9.0-28
- Update project URL
- require perl(LWP::Protocol::https) (needed for https)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.9.0-19
- add patch to silence warnings "Unescaped left brace in regex is deprecated,
  passed through in regex" in perl 5.22  (#1254288)

* Wed Jul 01 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9.1-18
- Add dist-tag (RHBZ #1237192).

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-17.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-16.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-15.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.9.0-14.1
- Perl 5.18 rebuild

* Fri Mar 01 2013 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.9.0-13.1
- add /usr/bin/pod2man as BR (needed for F19 #914569)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.9.0-9.1
- Add a patch that removes some usused HTML procssing bit from the Makefile
  that seem to confuse newer make versions; fixes #660818 (FTBS)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 22 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.9.0-5
- Manually require perl(IO::Socket::SSL) to make https work

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Sun Apr 08 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.9.0-4
- rebuild

* Sun Apr 08 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.9.0-3
- remove the / add the end of the mv command

* Sat Apr 07 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.9.0-2
- Fixes found during review (#235573):
  - noarch automatically disables debuginfo
  - require /usr/sbin/sendmail instead of smtpdaemon

* Sat Apr 07 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.9.0-1
- Initial package
