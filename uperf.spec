Summary:        Network performance tool with modelling and replay support
Name:           uperf
Version:        1.0.7
Release:        10%{?dist}
License:        GPLv3
URL:            http://www.uperf.org/
Source0:        https://github.com/uperf/uperf/archive/%{version}.tar.gz
Patch1:         uperf-1.0.6-ssl-crash.patch
Patch2:         uperf-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
%description
Network performance tool that supports modelling and replay of various
networking patterns.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
find src -type f -print0 | xargs --null chmod 0644
find workloads -type f -print0 | xargs --null chmod 0644
chmod 0644 AUTHORS ChangeLog COPYING README

%build
# Prevent rebuilding of the configure script (for uperf-configure-c99.patch).
touch aclocal.m4 Makefile.in config.h.in configure
%configure           \
    --enable-cpc     \
    --enable-netstat \
    --enable-udp     \
    --enable-sctp    \
    --enable-ssl
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Move stuff to own subdir
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -p -m 0644 %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/%{name}
install -p -m 0644 {server,client}.pem %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/uperf
%{_datadir}/uperf

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 1.0.7-8
- Fix sendfilev configure glitch with C99 compilers

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.7-5
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.0.7-1
- 1.0.7

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.0.6-1
- 1.0.6

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.0.5-1
- 1.0.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.0.4-1
- 1.0.4

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-0.3.beta
- move workloads files

* Thu Mar 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-0.2.beta
- don't ship pem files

* Mon Feb  1 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-0.1.beta
- initial build
