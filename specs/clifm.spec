Name:           clifm
Version:        1.22
Release:        2%{?dist}
Summary:        Shell-like, command line terminal file manager

# source is pretty evently split between these
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
# misc/colors/ and plugins/ are GPL-3.0-only
# src/ are GPL-2.0-or-later


URL:            https://github.com/leo-arch/clifm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  libcap-devel
BuildRequires:  libacl-devel
BuildRequires:  file-devel
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
CliFM is a Command Line Interface File Manager: all input and interaction
is performed via commands. This is its main feature and strength.

Unlike most terminal file managers out there, indeed, CliFM replaces the
traditional TUI interface (also known as curses or text-menu based
interface) by a command-line interface (CLI), also known as REPL.

If working with the command-line, your workflow is not affected at all,
but just enriched with file management functionalities: automatic files
listing, files selection, bookmarks, tags, directory jumper, directory and
commands history, auto-cd and auto-open, bulk rename, TAB completion,
autosuggestions, and a trash system, among other features. In this sense,
CliFM is certainly a file manager, but also a shell extension.

Briefly put, with CliFM the command-line is always already there, never
hidden.


%prep
%autosetup
# just to be sure we use system lib
rm -f src/{printf*,qsort.h}


%build
%cmake
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/%{name}
%{_datadir}/applications/clifm.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 03 2024 Carl George <carlwgeorge@fedoraproject.org> - 1.22-1
- Update to version 1.22 rhbz#2304057

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Jonathan Wright <jonathan@almalinux.org> - 1.19-1
- update to 1.19 rhbz#2263600

* Mon Feb 12 2024 Jonathan Wright <jonathan@almalinux.org> - 1.17-1
- update to 1.17 rbhz#2263600

* Thu Feb 01 2024 Jonathan Wright <jonathan@almalinux.org> - 1.16-1
- Update to 1.16 rhbz#2257487

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.15-1
- Update to 1.15

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Jonathan Wright <jonathan@almalinux.org> - 1.10-1
- update to 1.10

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7-2
- adjust description per upstream request
- https://github.com/leo-arch/clifm/issues/154#issuecomment-1233102727

* Tue Aug 16 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7-1
- Initial package build
- rhbz#2118835
