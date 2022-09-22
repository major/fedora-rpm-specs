%global __provides_exclude_from %{_libexecdir}
%global __requires_exclude .*GSMUSSD.*

%global rev 25
Name:           gsm-ussd
Version:        0.4.0
Release:        0.32.%{rev}%{?dist}
Source:         http://linux.zum-quadrat.de/downloads/%{name}_%{version}-%{rev}.tar.gz
BuildArch:      noarch 
Summary:        USSD query tool

License:        GPLv2+ or LGPLv2+
Url:            http://iloapp.zum-quadrat.de/blog/linux?Home&category=2
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Expect)
%if 0%{?fedora} > 18
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
%endif
BuildRequires: make

# Makefile installs python scripts to lib dir. It's wrong.
# Patch serves to fix it.
Patch0:         %{name}-libexec.patch

# Fix incorrect syntaxis
Patch1:         %{name}-pod2man.patch

%description
gsm-ussd is a script to send USSD (Unstructured Supplementary
Services Data) queries to your broadband provider. USSD queries
are "phone numbers" like "*100#", which will result in a message
(NOT a SMS) with your current prepaid account balance.

You can use this program to query your own phone number,
replenish your prepaid account, query your free minutes left
and so on, depending on your GSM provider.

%prep
%setup -qn %{name}_%{version}-%{rev}
%patch0 -p1
%patch1 -p1

%build

%install
make PREFIX=$RPM_BUILD_ROOT/usr install install-doc
# Unset executable bit
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man1/* $RPM_BUILD_ROOT%{_mandir}/de/man1/*
chmod 644 $RPM_BUILD_ROOT%{_libexecdir}/%{name}/lib/GSMUSSD/*

# gsm-ussd has gui but it depends from KDE and Gnome.
# So I've droped it to prevent many dependencies.
rm $RPM_BUILD_ROOT%{_bindir}/xussd
rm $RPM_BUILD_ROOT%{_libexecdir}/%{name}/bin/xussd.sh
rm $RPM_BUILD_ROOT%{_mandir}/man1/xussd*
rm $RPM_BUILD_ROOT%{_mandir}/de/man1/xussd*

%files
%doc README LICENSE TODO docs/README.* docs/story.txt docs/ussd-sessions.txt
%doc %{_mandir}/man1/*
%doc %{_mandir}/de/man1/*
%{_libexecdir}/%{name}/
%{_bindir}/%{name}

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.32.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.31.25
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.30.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.29.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.28.25
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.27.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.26.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.25.25
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.24.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.23.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.22.25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.21.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.20.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.19.25
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.18.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.17.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.16.25
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.15.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.14.25
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.13.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.12.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.11.25
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-0.10.25
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.9.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.8.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.4.0-0.7.25
- Perl 5.18 rebuild

* Fri Feb 22 2013 Ivan Romanov <drizt@land.ru> - 0.4.0-0.6.25%{?dist}
- pod2man now in perl-podlators (#914057)
- added patch to fix incorrect syntaxis

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.5.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Ivan Romanov <drizt@land.ru> 0.4.0-0.4.25
- use %%global instead of %%define
- use %%name in patch

* Sun Oct 07 2012 Ivan Romanov <drizt@land.ru> 0.4.0-0.3.25
- dropped xussd
- unset executable flag for perl modules
- fixed License tag
- fixed Requires tag
- filter modules from Provides

* Sat Sep 22 2012 Ivan Romanov <drizt@land.ru> 0.4.0-0.2.25
- renamed lib-exec.patch -> gsm-ussd-libexec.patch
- dropped %%defattr
- corrected license
- use %%gloabal instead of %%define

* Sun Sep 16 2012 Ivan Romanov <drizt@land.ru> 0.4.0-0.1.25
- Initial version of package based on spec.tmpl from source tarball
