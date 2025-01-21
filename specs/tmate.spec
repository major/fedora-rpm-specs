Name:           tmate
Version:        2.4.0
Release:        13%{?dist}

Summary:        Instant terminal sharing
License:        MIT
Url:            http://tmate.io

Source0:        https://github.com/tmate-io/tmate/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  ruby
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  libssh-devel >= 0.9.0
BuildRequires:  msgpack-devel >= 1.1.8

%description
Tmate is a fork of tmux providing an instant pairing solution.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc CHANGES FAQ README-tmux README.md
%license COPYING
%{_bindir}/tmate
%{_mandir}/man1/tmate.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 20:46:05 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.0-4
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Andreas Schneider <asn@redhat.com> - 2.4.0-1
- Update to version 2.4.0

* Wed Nov 06 2019 Andreas Schneider <asn@redhat.com> - 2.3.1-2
- Fix authentication problems with rsa-sha2 keys

* Mon Oct 14 2019 Andreas Schneider <asn@redhat.com> - 2.3.1-1
- Update to version 2.3.1 (#1761239)

* Thu Aug 01 2019 Andreas Schneider <asn@redhat.com> - 2.3.0-1
- Update to version 2.3.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Andreas Schneider <asn@redhat.com> - 2.2.1-8
- Rebuild to fix libevent dependency

* Tue Feb 20 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 2.2.1-7
- Rebuild following libevent update from 2.0 to 2.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 19 2016 Andreas Schneider <asn@redhat.com> - 2.2.1-2
- Rebuild against new msgpack version

* Wed Mar 30 2016 Andreas Schneider <asn@redhat.com> - 2.2.1-1
- Update to version 2.2.1
  * Reconnection implemented
  * Bug fixes in synchronizing the key bindings
  * Webhooks support added: https://github.com/tmate-io/tmate/wiki/Webhooks

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Andreas Schneider <asn@redhat.com> - 2.2.0-1
- Update to version 2.2.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 - Andreas Schneider <asn@redhat.com> - 1.8.9-3
- Add missing dist.

* Tue Apr 29 2014 - Andreas Schneider <asn@redhat.com> - 1.8.9-2
- Fixed 'make' calls.

* Fri Apr 25 2014 - Andreas Schneider <asn@redhat.com> - 1.8.9-1
- The big bang.
