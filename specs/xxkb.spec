Name:           xxkb
Version:        1.11.1
Release:        18%{?dist}
Summary:        Keyboard layout indicator and switcher

License:        Artistic-2.0
Url:            http://xxkb.sourceforge.net
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}-src.tar.gz
# Minimal changes in default config file to make xxkb works out of box on
# modern systems
Patch0:         %{name}-default-config.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)

%description
The xxkb program is a keyboard layout switcher and indicator. Unlike the
programs that reload keyboard maps and use their own hot-keys, xxkb is a simple
GUI for XKB (X KeyBoard extension) and just sends commands to and accepts events
from XKB. That means that it will work with the existing setup of your X Server
without any modifications.

%prep
%autosetup -p1

%build
xmkmf
sed -i "s|CCOPTIONS =|CCOPTIONS = %{build_cflags}|" Makefile
sed -i "s|EXTRA_LDOPTIONS =|EXTRA_LDOPTIONS = %{build_ldflags}|" Makefile
%make_build

%install
%make_install install.man

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/X11/app-defaults/XXkb
%{_mandir}/man1/xxkb.1x.*
%dir %{_prefix}/lib/X11
%{_prefix}/lib/X11/app-defaults

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.11.1-16
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11.1-5
- Initial package
