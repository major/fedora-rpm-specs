Name:       dontpanic   
Version:    1.02
Release:    19%{?dist}
Summary:    Very simple library and executable used in testing Alien::Base
# LICENSE:              GPL-1.0 text
# README.md:            GPL-1.0-or-later OR Artistic-1.0-Perl
## Unbunled
# aclocal.m4:           FSFULLRWD AND FSFULLR
# config/compile:       GPL-2.0-or-later WITH Autoconf-exception-generic
# config/config.guess:  GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config/config.sub:    GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config/depcomp:       GPL-2.0-or-later WITH Autoconf-exception-generic
# config/install-sh:    X11 AND LicenseRef-Fedora-Public-Domain
# config/ltmain.sh:     GPL-2.0-or-later WITH Libtool-exception AND
#                       GPL-3.0-or-later WITH Libtool-exception AND GPL-3.0-or-later
# config/missing:       GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:            FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# m4/libtool.m4:        FSFULLR AND GPL-2.0-or-later WITH Libtool-exception
#                       AND FSFUL
# m4/ltversion.m4:      FSFULLR
# m4/lt~obsolete.m4:    FSFULLR
# m4/ltoptions.m4:      FSFULLR
# m4/ltsugar.m4:        FSFULLR
# Makefile.in:          FSFULLRWD
# src/Makefile.in:      FSFULLRWD
License:    GPL-1.0-or-later OR Artistic-1.0-Perl    
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Libtool-exception AND GPL-3.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL AND LicenseRef-Fedora-Public-Domain
URL:        https://github.com/Perl5-Alien/%{name}/
Source0:    %{url}archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make    

%description
This software provides a very simple library and executable used in testing
Alien::Base.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
This package contains libraries and header files needed for developing
applications that use %{name}.

%prep
%setup -q
rm -r aclocal.m4 autogen.sh config configure Makefile.in m4/* src/Makefile.in
autoreconf -fi

%build
%configure --enable-shared --disable-static --disable-silent-rules
%{make_build}

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} check

%files
%license LICENSE
%doc Changes README.md
%{_bindir}/dontpanic
%{_libdir}/libdontpanic.so.0{,.*}

%files devel
%{_includedir}/libdontpanic.h
%{_libdir}/libdontpanic.so
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/dontpanic.pc

%changelog
* Thu Jul 03 2025 Petr Pisar <ppisar@redhat.com> - 1.02-19
- Declare a source license
- Unbundle autotools scripts

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.02-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 28 2021 Tim Landscheidt <tim@tim-landscheidt.de> - 1.02-8
- Update URL tag

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Petr Pisar <ppisar@redhat.com> - 1.01-2
- Update patch for disabled static linking

* Tue Sep 05 2017 Petr Pisar <ppisar@redhat.com> - 1.01-1
- 1.01 bump

* Fri Sep 01 2017 Petr Pisar <ppisar@redhat.com> - 1.00-1
- 1.00 packaged


