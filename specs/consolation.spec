Name:		consolation
Version:	0.0.7
Release:	14%{?dist}
Summary:	Copy-paste for the Linux console

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://salsa.debian.org/consolation-team/consolation/
Source0:	https://salsa.debian.org/consolation-team/consolation/-/archive/consolation-%{version}/%{name}-consolation-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libinput-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:  pkgconfig(libinput) >= 1.5
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libevdev) >= 0.4
Requires:	systemd

%description
Consolation is a daemon that provide copy-paste and scrolling support to
the Linux console.

It is based on the libinput library and supports all pointer devices and
settings provided by this library,

Similar software include gpm and jamd.


%prep
%setup -q -n %{name}-consolation-%{version}


%build
autoreconf -fi
%configure
# Need to build the binary first, then the manual, otherwise the manual
# ends up butchered by the messed up make rules.
make %{?_smp_mflags} -C src consolation
make %{?_smp_mflags} consolation.8
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_unitdir}
install -pm644 consolation.service %{buildroot}%{_unitdir}


%systemd_post consolation.service
%systemd_preun consolation.service
%systemd_postun consolation.service


%files
%{_sbindir}/consolation
%{_mandir}/man8/consolation.8*
%{_unitdir}/consolation.service
%license LICENSE
%doc README AUTHORS ChangeLog


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.7-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.0.7-1
- Initial packaging
