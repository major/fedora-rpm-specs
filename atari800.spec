Name:          atari800
Version:       5.0.0
Release:       3%{?dist}
Summary:       An emulator of 8-bit Atari personal computers

License:       GPLv2+
URL:           https://atari800.github.io/
%global ver_ %(echo %{version} | tr . _)
Source0:       https://github.com/%{name}/%{name}/releases/download/ATARI800_%{ver_}/%{name}-%{version}-src.tgz
BuildRequires: gcc
BuildRequires: ncurses-devel, libX11-devel, SDL-devel
BuildRequires: libpng-devel, zlib-devel

%description
Atari800 is an emulator for the 800, 800XL, 130XE and 5200 models of
the Atari personal computer. It can be used on console, FrameBuffer or X11.
It features excellent compatibility, HIFI sound support, artifacting
emulation, precise cycle-exact ANTIC/GTIA emulation and more.


%prep
%autosetup


%build
%configure --docdir=%{_pkgdocdir}
%make_build


%install
%make_install


%files
%{_bindir}/atari800
%{_bindir}/cart
%{_mandir}/man1/atari800.1*
%license %{_pkgdocdir}/COPYING
%doc %{_pkgdocdir}/README.TXT
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/USAGE
%doc %{_pkgdocdir}/NEWS
%exclude %{_pkgdocdir}/INSTALL
%doc DOC/BUGS DOC/CREDITS DOC/ChangeLog DOC/FAQ DOC/HOWTO-*
%doc DOC/LPTjoy.txt DOC/TODO DOC/cart.txt DOC/coverage.txt DOC/pokeysnd.txt
%doc DOC/r_device.txt DOC/rdevice_faq.txt


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 28 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 5.0.0-1
- Update to upstream.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 04 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.2.0-2
- Updated description, source URL.
- Removed autoconf/automake and cleaning of RPM_BUILD_ROOT.
- Updated package doc directory to macro.
- Added configure --docdir parameter to allow build for epel7 too.

* Wed Feb 03 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.2.0-1
- Initial Fedora package.
