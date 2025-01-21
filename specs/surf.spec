Name:           surf
Version:        2.1
Release:        5%{?dist}
Summary:        Simple web browser
License:        MIT
URL:            http://surf.suckless.org/

Source0:        http://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.svg

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.1)
BuildRequires:  desktop-file-utils

Requires:       st
Requires:       dmenu
# https://bugzilla.redhat.com/show_bug.cgi?id=841348
Requires:       xprop
# https://bugzilla.redhat.com/show_bug.cgi?id=884296
Requires:       xterm
Requires:       wget, curl
# Appdata file needed later.

%description
surf is a simple web browser based on WebKit/GTK+.

%prep
%autosetup

# Adapt to Fedora FHS
# Also use correct webkit2gtk version
# Cf. https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
sed \
  -e 's|/usr/local|%{_prefix}|g' \
  -e 's|$(PREFIX)/lib|$(PREFIX)/%{_lib}|g' \
  -e 's|webkit2gtk-4.0|webkit2gtk-4.1|g' \
  -e 's|webkit2gtk-web-extension-4.0|webkit2gtk-web-extension-4.1|g' \
  -i config.mk

sed -i 's!^\(\t\+\)@!\1!' Makefile

%build
%set_build_flags
%make_build

%install
%make_install INSTALL="install -p"

desktop-file-install %{S:1} --dir=%{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -pm0644 %{S:2} %{buildroot}%{_datadir}/pixmaps/

%files
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/webext-%{name}.so
%{_mandir}/man*/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 2.1-2
- Add webkit2gtk-web-extension BR

* Sun Aug 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 2.1-1
- Update to latest upstream
- Adapt to use webkit2gtk-4.1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 2.0-10
- Require xprop not xorg-x11-utils

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Neal Gompa <ngompa13@gmail.com> - 2.0-6
- Add gcc BR to fix build in F29+ (rhbz#1606452)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Neal Gompa <ngompa13@gmail.com> - 2.0-1
- Update to latest upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3.gitda5290a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Neal Gompa <ngompa13@gmail.com> - 0.7-2.gitda5290a
- Switch to surf-webkit2 branch

* Sun Apr 17 2016 Neal Gompa <ngompa13@gmail.com> - 0.7-1
- Update to latest upstream
- Apply patch for GTK+3
- Switch to link to WebKitGTK+3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Simon Wesp <cassmodiah@fedoraproject.org> - 0.6-1
- New upstream release
- Thank you Sirko Kemter aka gnokii for the surf icon :)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 François Cami <fcami@fedoraproject.org> - 0.5-1
- New upstream release for surf
- Fix bz 884296 841348

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.1-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 05 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.1-2
- Rebuild against new version of webkitgtk

* Mon Jun 14 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.1-1
- New upstream release

* Mon May 31 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4-1
- New upstream release

* Tue Mar 23 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3-3
- Patch DSO

* Sun Jan 17 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3-2
- Output is verbose now

* Sun Jan 10 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3-1
- Initial package build
