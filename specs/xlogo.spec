Name:          xlogo
Version:       1.0.7
Release:       2%{?dist}
Summary:       Display the X11 logo

License:       MIT-open-group
URL:           https://www.x.org
Source0:       https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:       https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
# Upstream does not publish a GPG keyring, so create one for inclusion in
# the source RPM.  First import the public key then export it:
#
# gpg2 --keyserver hkp://keyserver.ubuntu.com --recv-keys CFDF148828C642A7
# gpg2 --export --export-options export-minimal CFDF148828C642A7 > gpgkey-CFDF148828C642A7.gpg
Source2:       gpgkey-CFDF148828C642A7.gpg

BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xorg-macros) >= 1.8
BuildRequires: gnupg2

Obsoletes:     xorg-x11-apps < 7.7-31

%description
xlogo displays a magnified snapshot of a portion of an X11 screen.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md ChangeLog
%{_bindir}/xlogo
%{_mandir}/man1/xlogo.1*
%{_datadir}/X11/app-defaults/XLogo
%{_datadir}/X11/app-defaults/XLogo-color

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 David Cantrell <dcantrell@redhat.com> - 1.0.7-1
- Upgrade to xlogo-1.0.7 (#2326145)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 David Cantrell <dcantrell@redhat.com> - 1.0.6-5
- spec file alignment

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 David Cantrell <dcantrell@redhat.com> - 1.0.6-1
- Upgrade to xlogo-1.0.6 (#2142321)
- Convert License tag to SPDX license identifier
- Use gpgverify in the prep block to verify the GPG signature on the
  source archive

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 David Cantrell <dcantrell@redhat.com> - 1.0.5-1
- Upgrade to xlogo-1.0.5 (#1957538)

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.4-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.4-1
- Split xlogo out from xorg-x11-apps into a separate package (#1933949)
