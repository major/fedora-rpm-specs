Name:		consolation
Version:	0.0.7
Release:	7%{?dist}
Summary:	Copy-paste for the Linux console

License:	GPLv2+
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
