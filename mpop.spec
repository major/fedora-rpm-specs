Name:           mpop
Version:        1.4.10
Release:        7%{?dist}
Summary:        Client for receiving mail from POP3 mailboxes

License:        GPLv3+
URL:            https://marlam.de/mpop/
Source0:        https://marlam.de/mpop/releases/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  gnutls-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  gettext

%description
mpop is a small and fast POP3 client. Features include mail filtering,
delivery to mbox files, maildir folders or a mail delivery agent, a very
fast POP3 implementation, many authentication methods, good TLS/SSL
support, IPv6 support, and more.

%prep
%autosetup

%build
%configure --with-gnome-keyring
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS NOTES README THANKS
%doc doc/mpoprc.example
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.*
%{_bindir}/%{name}

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.10-1
- Update to new upstream release 1.4.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.4-7
- Update to latest upstream release 1.4.4

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.6-10
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6-7
- Fix BR

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6-2
- Update summary (rhbz#1399621)

* Thu Nov 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6-1
- Updated to new upstream version 1.2.6

* Thu Feb 04 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.4-1
- Updated to new upstream version 1.2.4 (rhbz#1179320)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.29-1
- Updated to new upstream version 1.0.29

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.28-1
- Updated to new upstream version 1.0.28

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.27-3
- Rebuild for libgsasl

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 05 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.27-1
- Update to new upstream version 1.0.27

* Sun Jan 08 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.26-1
- Update to new upstream version 1.0.26

* Tue Oct 25 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.25-1
- Update to new upstream version 1.0.25

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-3
- Rebuild (info)

* Wed Apr 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-2
- Remove obsolete doc entries

* Wed Apr 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-1
- Update to new upstream version 1.0.24

* Mon Mar 28 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.23-1
- Update to new upstream version 1.0.23

* Mon Jan 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.22-1
- Update to new upstream version 1.0.22

* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.21-1
- Update to new upstream version 1.0.21

* Thu Apr 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.20-1
- Update to new upstream version 1.0.20

* Mon Nov 16 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.19-1
- Update to new upstream version 1.0.19

* Mon Oct 12 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.18-1
- Update to new upstream version 1.0.18

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.17-1
- Update to new upstream version 1.0.17

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-3
- Add missing BR

* Sat Jan 10 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-2
- Fix files section, remove duplicates

* Mon Dec 29 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-1
- Initial package for Fedora
