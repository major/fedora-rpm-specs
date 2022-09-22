Name:		seren
Version:	0.0.21
Release:	16%{?dist}
Summary:	Simple VoIP program to create conferences from the terminal
License:	GPLv3+
URL:		http://holdenc.altervista.org/seren/
Source:		http://holdenc.altervista.org/seren/downloads/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	alsa-lib-devel
BuildRequires:	opus-devel
BuildRequires:	ncurses-devel
BuildRequires:	gmp-devel

%description
Seren is a simple VoIP program based on the Opus codec that allows you 
to create a voice conference from the terminal, with up to 10 
participants, without having to register accounts, exchange emails, or 
add people to contact lists.
All you need to join an existing conference is the host name or IP 
address of one of the participants.
Seren creates a dynamic peer-to-peer network of equivalent nodes which 
exchange text and audio data using a UDP connection, and offers the 
user the ability to change the quality/bitrate on the fly, encrypt the 
traffic and record the calls.

%prep
%setup -q

%build
%configure --enable-default-pulse
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/seren
%{_mandir}/man1/seren.1.gz
%doc COPYING README BUGS TODO Changelog


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 02 2015 Francesco Frassinelli <fraph24@gmail.com> - 0.0.21-1
- Version bump

* Sun Sep 14 2014 Francesco Frassinelli <fraph24@gmail.com> - 0.0.20-1
- Version bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Francesco Frassinelli <fraph24@gmail.com> - 0.0.19-1
- Version bump

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Francesco Frassinelli <frafra@fedoraproject.org> - 0.0.18-1
- Version bump

* Sat Jan 18 2014 Francesco Frassinelli <frafra@fedoraproject.org> - 0.0.17-1
- Version bump

* Mon Jan 06 2014 Francesco Frassinelli <frafra@fedoraproject.org> - 0.0.16-1
- Initial build
