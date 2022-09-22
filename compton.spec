%global ver 0.1
%global prever beta3

Name:		compton
Version:	%{ver}
Release:	0.12%{?prever:.%{prever}}%{?dist}
Summary:	A compositor for X11
License:	MIT
URL:		https://github.com/AxelSilverdew/compton
Source0: https://github.com/AxelSilverdew/compton/archive/v%{version}%{?prever:_%{prever}}.tar.gz#/%{name}-%{version}%{?prever:_%{prever}}.tar.gz
Source2:	https://raw.githubusercontent.com/AxelSilverdew/compton/master/media/icons/48x48/compton.png

BuildRequires : gcc
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xrender)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(libconfig) >= 1.4
BuildRequires : pcre-devel
BuildRequires : pkgconfig(libdrm)
BuildRequires : mesa-libGL-devel
BuildRequires : pkgconfig(dbus-1)
BuildRequires : asciidoc
BuildRequires : desktop-file-utils
BuildRequires : make
Requires : xprop
Requires : xwininfo
Requires : hicolor-icon-theme

%description
Compton is a compositor for X, and a fork of xcompmgr-dana.

%prep
%autosetup -n %{name}-%{version}%{?prever:_%{prever}}

%build
# Export the COMPTON_VERSION variable (you may also pass it to make directly)
export COMPTON_VERSION=%{version}-%{release}
export CFLAGS="$RPM_OPT_FLAGS"
%make_build
%make_build docs

%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps
install -pm 644 %{SOURCE2} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/compton.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/compton
%{_bindir}/compton-trans
%{_mandir}/man1/compton.1*
%{_mandir}/man1/compton-trans.1*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/compton.*



%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.12.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.11.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 0.1-0.8.beta3
- Require xprop and xwininfo not xorg-x11-utils

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.7.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.5.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 0.1-0.3.beta3
- Rebuild for new libconfig

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr  1 2018 AxelSilverdew <axeld@fedoraproject.org>
- Fixed a few last moment issues in the spec

* Fri Feb  9 2018 AxelSilverdew <axeld@fedoraproject.org>
- Removed post and postun scriptlets

* Tue Jan  9 2018 AxelSilverdew <axeld@fedoraproject.org>
- Made some edits to fit Fedora packaging guidelines better

* Sun Jan  7 2018 AxelSilverdew <axeld@fedoraproject.org>
- Initial Package Spec
