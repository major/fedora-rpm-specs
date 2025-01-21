Name:           surfraw
Version:        2.3.0
Release:        15%{?dist}
Summary:        Shell Users Revolutionary Front Rage Against the Web
License:        LicenseRef-Fedora-Public-Domain
URL:            https://gitlab.com/surfraw/Surfraw
Source0:        http://surfraw.alioth.debian.org/dist/surfraw_%{version}.orig.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  gawk

# Surfraw searches for a text-mode broser at configuration time, not
# at runtime. This is something probably to be changed upstream. We
# could depend on 'text-www-browser', but then we are not sure that
# this resolves to the same package at build and install time. So, for
# now, we simply pick one.
%global text_browser elinks
BuildRequires:  %{text_browser}
BuildRequires:  perl-generators
Requires:       %{text_browser}
Requires:       gawk

# For calling the graphical browser, we can rely on xdg-open.
Requires:       xdg-utils


%description
Surfraw provides a fast unix command line interface to a variety of
popular WWW search engines and other artifacts of power. It reclaims
google, altavista, babelfish, dejanews, freshmeat, research index,
slashdot and many others from the false-prophet, pox-infested heathen
lands of html-forms, placing these wonders where they belong, deep in
unix heartland, as god loving extensions to the shell.

Surfraw abstracts the browser away from input. Doing so lets it get on
with what it's good at. Browsing. Interpretation of linguistic forms
is handed back to the shell, which is what it, and human beings are
good at. Combined with netscape-remote or incremental text browsers,
such as links (http://artax.karlin.mff.cuni.cz/~mikulas/links/), w3m
(http://www.w3m.org/), and screen(1) a Surfraw liberateur is capable
of navigating speeds that leave GUI tainted idolaters agape with fear
and wonder.


%prep
%setup -q


%build
%configure --with-elvidir=%{_libexecdir}/surfraw \
           --with-graphical-browser=xdg-open \
           --with-text-browser=%{text_browser} \
           --disable-opensearch
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%dir %{_sysconfdir}/xdg/surfraw
%config(noreplace) %{_sysconfdir}/xdg/surfraw/*
%{_bindir}/sr
%{_bindir}/surfraw
%{_bindir}/surfraw-update-path
%{_libexecdir}/surfraw
%{_mandir}/man1/*.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.0-1
- Update to 2.3.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.9-5
- Mark license with %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec  2 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.9-3
- Remove dependency on screen (rhbz#1159215).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.9-1
- Update to 2.2.9.
- Modernize spec file.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2.8-7
- Perl 5.18 rebuild

* Mon Feb 18 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.8-6
- Add BR for pod2man.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.8-2
- Rebuilt for trailing slash bug of rpm-4.9.1

* Thu Jul 21 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.8-1
- Update to 2.2.8.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 30 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.7-1
- Update to 2.2.7.

* Tue Dec 29 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.6-1
- Update to 2.2.6.
- Configuration is now in /etc/xdg/surfraw.

* Sun Sep 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.5-1
- Update to 2.2.5.
- New upstream, and new upstream URL.
- Elvi are now subcommands to the 'surfraw' command (or its 'sr'
  alias), avoids conflicts with other packages (bz 472623).
- Hard-code text browser to elinks, and graphical browser to xdg-open
  for now.
- Disable opensearch, needs perl(WWW::OpenSearch).
- Include manpages in the filelist.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 14 2007 Joe Rozner <livinded@deadbytes.net> 1.0.7-3
- Added BuildArch to build as noarch.
- Removed dependencies for browsers so that users will not need all three.

* Sat May 12 2007 Joe Rozner <livinded@deadbytes.net> 1.0.7-2
- Added dependencies for links, links, w3m, and screen.
- Fixed the license to be the correct one.

* Thu Mar 08 2007 Joe Rozner <livinded@deadbytes.net> 1.0.7-1
- Initial specfile created.
