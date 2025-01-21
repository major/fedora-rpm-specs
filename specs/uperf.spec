Summary:       Network performance tool with modelling and replay support
Name:          uperf
Version:       1.0.8
Release:       6%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only
URL:           http://www.uperf.org/
Source0:       https://github.com/uperf/uperf/archive/v%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: lksctp-tools-devel
BuildRequires: make
BuildRequires: openssl-devel
%if 0%{?fedora} > 40
BuildRequires: openssl-devel-engine
%endif
%description
Network performance tool that supports modelling and replay of various
networking patterns.

%prep
%autosetup
chmod 0644 workloads/{tcp-change-cc.xml,sctp-over-udp.xml,tcp-freebsd-change-stack.xml}

%build
autoreconf --install
%configure           \
    --enable-cpc     \
    --enable-netstat \
    --enable-udp     \
    --enable-sctp    \
    --enable-ssl
%make_build

%install
%make_install

# Move stuff to own subdir
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -p -m 0644 %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/%{name}
install -p -m 0644 {server,client}.pem %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/uperf
%{_datadir}/uperf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.8-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Terje Rosten <terje.rosten@ntnu.no> - 1.0.8-3
- Fix build deps after openssl changes

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 10 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.0.8-1
- 1.0.8

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
