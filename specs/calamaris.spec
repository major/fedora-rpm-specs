%global __requires_exclude ^perl\\(ident\\)$

Summary:        Analyzer and report generator for web proxy servers like Squid
Name:           calamaris
Version:        2.99.4.8
Release:        2%{?dist}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later
URL:            https://cord.de/calamaris-english
Source0:        https://cord.de/files/calamaris/%{name}-%{version}.tar.gz
Patch0:         calamaris-2.99.4.7-use-lib.patch
BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       perl(NetAddr::IP)
# Test in %%check
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(GD::Graph)
BuildRequires:  perl(GD::Graph::bars)
BuildRequires:  perl(GD::Graph::colour)
BuildRequires:  perl(GD::Graph::utils)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(integer)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Time::Local)

%description
Calamaris is used to produce statistical output from web proxy servers
like Squid, NetCache, Inktomi Traffic Server, Oops! proxy server, Compaq
TaskSmart, Cisco Content Engines, iPlanet Proxy Server or related proxy
log files. The resulting output can be ASCII or HTML with or without
graphics and with or without frames. It is possible to cache calculated
data in a file to use them in later runs.

%prep
%setup -q
%patch -P0 -p1 -b .use-lib
for file in *.use-lib; do touch -c -r ${file} ${file%.use-lib}; done

%build

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
for file in *.pm; do
  install -D -p -m 0644 ${file} $RPM_BUILD_ROOT%{perl_vendorlib}/%{name}/${file}
done

# Convert files from ISO-8859-1 to UTF-8
for file in CONTRIBUTORS EXAMPLES; do
  iconv -f iso-8859-1 -t utf-8 -o ${file}.utf8 ${file}
  touch -c -r ${file} ${file}.utf8; mv -f ${file}.utf8 ${file}
done

%check
perl -c $RPM_BUILD_ROOT%{_bindir}/%{name}
echo '0 7 192.0.2.42 TCP_HIT/200 4711 GET http://example.net/ - NONE/- text/html' | \
  $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%license COPYRIGHT
%doc CHANGES CONTRIBUTORS EXAMPLES EXAMPLES.v3 README
%{_bindir}/%{name}
%{perl_vendorlib}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Robert Scheck <robert@fedoraproject.org> 2.99.4.8-1
- Upgrade to 2.99.4.8 (#2333752)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 Robert Scheck <robert@fedoraproject.org> 2.99.4.7-1
- Upgrade to 2.99.4.7 (#2035609)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Robert Scheck <robert@fedoraproject.org> 2.59-10
- Added patch to avoid warnings with perl >= 5.12 (#970990)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.59-8
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.59-2
- Rebuild against gcc 4.4 and rpm 4.6

* Thu Jul 24 2008 Robert Scheck <robert@fedoraproject.org> 2.59-1
- Upgrade to 2.59
- Initial spec file for Fedora and Red Hat Enterprise Linux
