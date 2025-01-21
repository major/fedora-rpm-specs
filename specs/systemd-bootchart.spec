Name:           systemd-bootchart
Version:        235
Release:        2%{?dist}
Summary:        Boot performance graphing tool

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/systemd/systemd-bootchart
Source0:        https://github.com/systemd/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  gcc
BuildRequires:  systemd
BuildRequires:  pkgconfig(libsystemd) >= 221
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  docbook-style-xsl
%{?systemd_requires}

%description
This package provides a binary which can be started during boot early boot to
capture informations about processes and services launched during bootup.
Resource utilization and process information are collected during the boot
process and are later rendered in an SVG chart. The timings for each services
are displayed separately.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --disable-silent-rules
%make_build

%install
%make_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE.GPL2
%license LICENSE.LGPL2.1
%doc README
%config(noreplace) %{_sysconfdir}/systemd/bootchart.conf
%{_unitdir}/systemd-bootchart.service
%{_unitdir}/../%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/bootchart.conf.5*
%{_mandir}/man5/bootchart.conf.d.5*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 235-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 30 2024 Andrea Bolognani <abologna@redhat.com> - 235-1
- Update to v235 (RHBZ #2247564)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 234-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 234-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 234-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 234-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 29 2023 Dominique Martinet <asmadeus@codewreck.org> - 234-1
- Update to fix segfault in svg_ps_bars

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 233-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 233-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 233-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 233-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 233-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 233-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 233-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 233-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 233-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 233-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 233-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 233-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 233-1
- Update to 233

* Sun Sep 10 2017 Peter Robinson <pbrobinson@fedoraproject.org> 232-1
- new upstream 232 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 231-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 231-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 231-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 231-2
- Improve SPEC file thanks to suggestions during review

* Tue Sep 20 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 231-1
- Initial packaging
