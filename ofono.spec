Name:    ofono
Summary: Open Source Telephony
Version: 1.34
Release: 2%{?dist}

License: GPLv2
URL:     http://www.ofono.org/
Source0: https://git.kernel.org/pub/scm/network/ofono/ofono.git/snapshot/ofono-%{version}.tar.gz

BuildRequires: make
BuildRequires: libell-devel
BuildRequires: automake libtool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libudev) >= 145
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(mobile-broadband-provider-info)

BuildRequires: systemd-rpm-macros
BuildRequires: gcc
BuildRequires: m4

%description
oFono.org is a place to bring developers together around designing an
infrastructure for building mobile telephony (GSM/UMTS) applications.
oFono includes a high-level D-Bus API for use by telephony applications.
oFono also includes a low-level plug-in API for integrating with telephony
stacks, cellular modems and storage back-ends.

%package devel
Summary: Development files for oFono
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup


%build
if [ ! -f configure ]; then
./bootstrap
fi

%configure --enable-external-ell
%make_build


%install
%make_install
# create/own this
mkdir -p %{buildroot}%{_libdir}/ofono/plugins


%check
make check


%post
%systemd_post ofono.service

%preun
%systemd_preun ofono.service

%postun
%systemd_postun_with_restart ofono.service

%files
%doc ChangeLog AUTHORS README
%license COPYING
%{_sysconfdir}/dbus-1/system.d/ofono.conf
%dir %{_sysconfdir}/ofono/
%config(noreplace) %{_sysconfdir}/ofono/phonesim.conf
%{_sbindir}/ofonod
%{_unitdir}/ofono.service
%{_mandir}/man8/ofonod.8*
%dir %{_libdir}/ofono/
%dir %{_libdir}/ofono/plugins/

%files devel
%{_includedir}/ofono/
%{_libdir}/pkgconfig/ofono.pc


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.34-1
- Version 1.34

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 09 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.33-1
- Version bump to 1.33

* Sat Aug 07 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.32-1
- Build error fix and version bump
- Remove patch (upstream already has it)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.31-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Nikhil Jha <hi@nikhiljha.com> - 1.31-1
- Update to 1.31-1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.23-1
- 1.23
- use %%license %%make_build
- -devel: make base dep unarched, no point in making base multilib too

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.22-1
- 1.22

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Rex Dieter <rdieter@fedoraproject.org> 1.14-1
- first try (borrowed from obs)


