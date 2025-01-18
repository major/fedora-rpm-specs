%global __cmake_in_source_build 1

Summary: GUI client for Fwknop
Name: fwknop-gui
Version: 1.3.1
Release: 26%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://incomsystems.biz/fwknop-gui/
Source: %{url}/downloads/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++ make cmake
BuildRequires: fwknop-devel
BuildRequires: wxGTK-devel
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gpgme-devel
BuildRequires: pkgconfig(libqrencode)
BuildRequires: asciidoc

%description
Fwknop-gui is a cross platform gui that can save
and send knocks to a server running fwknopd.

%prep
%autosetup -n %{name}

%build
%cmake . -DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config-3.2
%make_build

%install
%make_install
install -p -m0644 -D %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fwknop-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/help.html
%doc %{_mandir}/man8/%{name}.8*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 1.3.1-19
- Rebuild with wxWidgets 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Jakub Jelen <jjelen@redhat.com> - 1.3.1-14
- Unbreak cmake build (#1863590)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 1.3.1-9
- Rebuilt (libqrencode.so.4)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3.1-2
- Rebuild for gpgme 1.18

* Mon Sep 05 2016 Jakub Jelen <jjelen@redhat.com> - 1.3.1-1
- New upstream release (fixing a bug in the QR code prompt)

* Wed Aug 10 2016 Jakub Jelen <jjelen@redhat.com> - 1.3-2
- Packaging tweaks

* Fri Aug 05 2016 Jakub Jelen <jjelen@redhat.com> - 1.3-1
- Initial release
