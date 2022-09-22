%global __requires_exclude perl\\(.*[.]pl\\)|\/bin\/bash
%define _legacy_common_support 1

Name:           mlmmj
Version:        1.3.0
Release:        14%{?dist}
Summary:        A simple and slim mailing list manager inspired by ezmlm
License:        MIT
URL:            http://mlmmj.org/
Source0:        http://mlmmj.org/releases/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make

%description
Mlmmj(Mailing List Management Made Joyful) is a simple and slim mailing list 
manager (MLM) inspired by ezmlm. It works with many different Mail Transport 
Agents (MTAs) and is simple for a system adminstrator to install, configure 
and integrate with other software. As it uses very few resources, and requires
no daemons, it is ideal for installation on systems where resources are 
limited, such as Virtual Private Servers (VPSes).

Although it doesn't aim to include every feature possible, but focuses on 
staying mean and lean, and doing what it does do well, it does have a great 
set of features, including:

- Archive
- Custom headers / footer
- Fully automated bounce handling (similar to ezmlm)
- Complete requeueing functionality
- Moderation functionality
- Subject prefix
- Subscribers only posting
- Regular expression access control
- Functionality to retrieve old posts
- Web interface
- Digests
- No-mail subscription
- VERP support
- Delivery Status Notification (RFC1891) support
- Rich, customisable texts for automated operations

%prep
%setup -q

%build
%configure --enable-receive-strip
make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}
find contrib/ -type f -name *.pl -exec chmod -x {} ";"
find contrib/ -type f -name *.cgi -exec chmod -x {} ";"

%files
%{!?_licensedir:%global license %doc}
%license COPYING
%doc AUTHORS ChangeLog FAQ README* TODO TUNABLES UPGRADE
%doc contrib/web/
%{_bindir}/*
%{_mandir}/man1/mlmmj*.1*
%{_datadir}/%{name}/
%{_localstatedir}/spool/%{name}

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Denis Fateyev <denis@fateyev.com> - 1.3.0-9
- Add "legacy_common_support" build option

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Denis Fateyev <denis@fateyev.com> - 1.3.0-1
- Update to 1.3.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 02 2016 Denis Fateyev <denis@fateyev.com> - 1.2.19.0-1
- Update to 1.2.19.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Christopher Meng <rpm@cicku.me> - 1.2.18.1-1
- Update to 1.2.18.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 26 2013 Christopher Meng <rpm@cicku.me> - 1.2.18.0-2
- Filter out wrong dependencies.

* Fri Aug 09 2013 Christopher Meng <rpm@cicku.me> - 1.2.18.0-1
- Resubmit the package.
