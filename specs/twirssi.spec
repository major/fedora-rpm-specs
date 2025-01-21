Name:           twirssi
Version:        2.6.4
Release:        18%{?dist}
Summary:        An Irssi script to interact with Twitter
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://twirssi.com/
Source0:        http://twirssi.com/%{name}-%{version}.pl
Source1:        https://raw.github.com/zigdon/twirssi/master/README
Source2:        https://raw.github.com/zigdon/twirssi/master/gpl-2.0.txt
BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       irssi
Requires:       perl(base)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Strptime)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Temp)
Requires:       perl(HTML::Entities)
Requires:       perl(HTTP::Date)
Requires:       perl(Irssi)
Requires:       perl(Irssi::Irc)
Requires:       perl(JSON::Any)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::Simple)  
Requires:       perl(Net::Twitter) >= 3.11009
Requires:       perl(WWW::Shorten)

# For Fedora < F20, which had versioned docdirs
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Twirssi allows you interact with Twitter and Identi.ca from Irssi. It can
handle tweets and direct messages (DMs), and supports multiple accounts on
either Twitter or Identi.ca.

%prep

%build

%install

install -d $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts
install -m 644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts/%{name}.pl
install -d $RPM_BUILD_ROOT%{_pkgdocdir}
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_pkgdocdir}
install -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%{_datarootdir}/irssi/scripts/%{name}.pl
%doc %{_pkgdocdir}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.4-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Julian C. Dunn <jdunn@aquezada.com> - 2.6.4-1
- Update to 2.6.4 (bz#1377132)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Julian C. Dunn <jdunn@aquezada.com> 2.6.3-1
- Update to 2.6.3 (bz#1054485)

* Sun Sep 15 2013 Julian C. Dunn <jdunn@aquezada.com> 2.6.2-1
- Update to 2.6.2 (bz#1008269)

* Sat Aug 24 2013 Julian C. Dunn <jdunn@aquezada.com> 2.6.0-4
- Update for unversioned docdir change (bz#993953)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.6.0-2
- Perl 5.18 rebuild

* Fri Jun 14 2013 Julian C. Dunn <jdunn@aquezada.com> 2.6.0-1
- Upgrade to 2.6.0 for Twitter 1.1 API

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-3
- Correct missed deps per bz#809948

* Wed Apr 04 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-2
- Changes per review in bz#808254

* Wed Feb 29 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-1
- Update to 2.5.1

* Mon Jul 05 2010 Julian C. Dunn <jdunn@aquezada.com> 2.4.3-1
- Initial import of 2.4.3
