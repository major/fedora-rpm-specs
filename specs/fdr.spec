Summary:	A daemon which enables ftrace probes and harvests the data
Name:		fdr
URL:		https://github.com/oracle/fdr.git
Version:	1.3
Release:	9%{?dist}
# Automatically converted from old format: UPL - review is highly recommended.
License:	UPL-1.0
Source0:	http://people.redhat.com/steved/fdr/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	sed
BuildRequires:	systemd-rpm-macros
Requires:	systemd

%description
The flight data recorder, a daemon which enables ftrace probes
and harvests the data

%prep
%autosetup

%build
sed -i -e "s:^CFLAGS.*:CFLAGS = %{optflags}:" Makefile
%make_build


%install
mkdir -p %{buildroot}/%{_sbindir}
install -m 755 fdrd %{buildroot}/%{_sbindir}

mkdir -p %{buildroot}%{_datadir}/fdr/samples
install -m 644 samples/nfs %{buildroot}/%{_datadir}/fdr/samples
install -m 644 samples/nfs.logrotate %{buildroot}/%{_datadir}/fdr/samples

mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service

mkdir -p %{buildroot}/%{_mandir}/man8
install -m 644 fdrd.man %{buildroot}/%{_mandir}/man8/fdrd.8

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_sbindir}/fdrd
%{_unitdir}/fdr.service
%{_datadir}/fdr/samples/nfs
%{_datadir}/fdr/samples/nfs.logrotate
%{_mandir}/man8/*
%doc README.md
%license LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Steve Dickson <steved@redhat.com>  1.3-0
- Initial commit
