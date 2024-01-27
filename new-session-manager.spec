Name:           new-session-manager
Version:        1.3.2
Release:        11%{?dist}
Summary:        Music production session manager

# Main program: GPL3+
# nsm.h: ISC
License:        GPLv3+ and ISC
URL:            https://github.com/linuxaudio/%{name}
Source0:        https://github.com/linuxaudio/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  liblo-devel
BuildRequires:  libXpm-devel
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  %{_bindir}/pathfix.py
BuildRequires:  %{_bindir}/find
Requires:       hicolor-icon-theme
Conflicts:      non-session-manager

%description
New Session Manager (NSM) is a tool to assist music production by grouping
standalone programs into sessions. Your workflow becomes easy to manage,
robust and fast by leveraging the full potential of cooperative applications.

You can create a session, or project, add programs to it and then use commands
to save, start/stop, hide/show all programs at once, or individually. At a
later date you can then re-open the session and continue where you left off.

All files belonging to the session will be saved in the same directory.

%prep
%autosetup

%build
%meson
%meson_build

%install 
%meson_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.linuxaudio.nsm-legacy-gui.desktop

%files
%license COPYING
%doc CHANGELOG
%doc README.md
%{_bindir}/nsmd
%{_bindir}/jackpatch
%{_bindir}/non-session-manager
%{_bindir}/nsm-legacy-gui
%{_bindir}/nsm-proxy
%{_bindir}/nsm-proxy-gui
%{_datadir}/applications/org.linuxaudio.nsm-legacy-gui.desktop

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.3.2-3
- Remove jack-audio-connection-kit from explicit Requires

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.3.2-1
- Initial build
