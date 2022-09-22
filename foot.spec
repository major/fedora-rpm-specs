Name:           foot
Version:        1.13.1
Release:        1%{?dist}
Summary:        Fast, lightweight and minimalistic Wayland terminal emulator

License:        MIT
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.58.0
BuildRequires:  desktop-file-utils
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(fcft) >= 3.0.1
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tllist) >= 1.0.4
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner) 
BuildRequires:  pkgconfig(xkbcommon)
# require *-static for header-only library
BuildRequires:  tllist-static

Recommends:     %{name}-terminfo
Requires:       (%{name}-terminfo = %{version}-%{release} if %{name}-terminfo)
# Optional dependency for bell = notify option
Recommends:     /usr/bin/notify-send
# Optional dependency for opening URLs
Recommends:     /usr/bin/xdg-open
Requires:       hicolor-icon-theme

%description
Fast, lightweight and minimalistic Wayland terminal emulator.
Features:
 * Fast
 * Lightweight, in dependencies, on-disk and in-memory
 * Wayland native
 * DE agnostic
 * Server/daemon mode
 * User configurable font fallback
 * On-the-fly font resize
 * On-the-fly DPI font size adjustment
 * Scrollback search
 * Keyboard driven URL detection
 * Color emoji support
 * IME (via text-input-v3)
 * Multi-seat
 * Synchronized Updates support
 * Sixel image support

%package        terminfo
Summary:        Terminfo files for %{name} terminal
BuildRequires:  /usr/bin/tic
Requires:       ncurses-base

%description    terminfo
%{summary}.


%prep
%autosetup -n %{name}


%build
%meson
%meson_build


%install
%meson_install
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}*.desktop


%post
%systemd_user_post %{name}-server@.{service,socket}

%preun
%systemd_user_preun %{name}-server@.{service,socket}


%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/xdg/%{name}/%{name}.ini
%{_bindir}/%{name}
%{_bindir}/%{name}client
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/bash-completion/completions/foot*
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/foot*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}client
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/CHANGELOG.md
%doc %{_docdir}/%{name}/README.md
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}client.1*
%{_mandir}/man5/%{name}.ini.5*
%{_mandir}/man7/%{name}-ctlseqs.7*
%{_userunitdir}/%{name}-server@.service
%{_userunitdir}/%{name}-server@.socket

%files terminfo
%license LICENSE
%dir %{_datadir}/terminfo/f
%{_datadir}/terminfo/f/%{name}
%{_datadir}/terminfo/f/%{name}-direct


%changelog
* Wed Aug 31 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.13.1-1
- Update to 1.13.1 (#2123078)

* Sun Aug 07 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 28 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.12.1-1
- Update to 1.12.1 (#2079544)

* Fri Apr 22 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0 (#2077953)
- Example config was moved to /etc/xdg/foot/foot.ini (upstream change)
- Install systemd unit files for foot --server

* Sat Feb 05 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0 (#2051005)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10.3-1
- Update to 1.10.3 (#2030411)

* Fri Dec 03 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10.2-1
- Update to 1.10.2

* Mon Nov 22 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#2025735)

* Sun Nov 14 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#2009965)

* Fri Oct 01 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.9.1-1
- Update to 1.9.1

* Fri Aug 27 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0
- Override custom terminfo dir with /usr/share/terminfo

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.2-2
- Add runtime dependency on fcft 2.4

* Sun Jul 18 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Fri Jul 02 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Fri Jun 25 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Apr 18 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Sun Mar 28 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sat Mar 20 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Wed Mar 10 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.6.4-1
- Initial import (#1912856)
