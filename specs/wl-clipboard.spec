Name:           wl-clipboard
Version:        2.2.1
Release:        4%{?dist}
Summary:        Command-line copy/paste utilities for Wayland

License:        GPL-3.0-or-later
URL:            https://github.com/bugaevc/wl-clipboard
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

Recommends:     xdg-utils
Recommends:     mailcap

%description
Command-line Wayland clipboard utilities, `wl-copy` and `wl-paste`,
that let you easily copy data between the clipboard and Unix pipes,
sockets, files and so on.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_mandir}/man1/wl-clipboard.1.*
%{_mandir}/man1/wl-copy.1.*
%{_mandir}/man1/wl-paste.1.*
%{_datadir}/bash-completion/completions/wl-*
%{_datadir}/fish/vendor_completions.d/wl-*
%{_datadir}/zsh/site-functions/_wl-*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 2.2.1-1
- new version (rhbz#2235567)

* Tue Jul 25 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 2.2.0-1
- new version 2.2.0 (rhbz#2225327)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 13 2023 Todd Zullinger <tmz@pobox.com> - 2.1.0-1
- update to 2.1.0 (rhbz#2066000)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 2.0.0-1
- Update to upstream v2.0.0 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.20181215git7e5103c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  9 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.0-0.1.20181215git7e5103c
- initial package (rhbz#1660440)
