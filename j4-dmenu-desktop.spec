Name:           j4-dmenu-desktop
Version:        2.18
Release:        8%{?dist}
Summary:        Generic menu for desktop managers
License:        GPLv3
URL:            https://github.com/enkore/j4-dmenu-desktop
Source0:        https://github.com/enkore/%{name}/archive/r%{version}/%{name}-%{version}.tar.gz
Patch0:         cmake-minimum-version.patch
BuildRequires:  cmake
BuildRequires:  catch-devel
BuildRequires:  gcc-c++

%description
%{name} is a replacement for i3-dmenu-desktop.
It's purpose is to find .desktop files and offer you a menu to start an
application using dmenu.  It should work just fine on about any desktop
environment.  You can also execute shell commands using it.

%prep
%autosetup -n %{name}-r%{version}

%build
%cmake -DWITH_GIT_CATCH=OFF -DCATCH_INCLUDE_DIR=/usr/include/catch2
%cmake_build

%install
%cmake_install
install -d %{buildroot}%{_mandir}/man1
cp %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 04 2021 Tobias Florek <tob@butter.sh> - 2.18-4
- remove CMAKE warning
- explicitly build-depend on gcc-c++

* Thu Jan 21 2021 Tobias Florek <me@ibotty.net> - 2.18-3
- packaging: fix archive name
- packaging: use cp instead of using cat and shell redirection

* Wed Jan 20 2021 Tobias Florek <me@ibotty.net> - 2.18-2
- packaging: use license macro for license
- packaging: do not gzip manpage

* Tue Nov 24 2020 Tobias Florek <me@ibotty.net> - 2.18-1
- bump version to 2.18
- use catch2 from fedor
- install man page
- update description

* Mon May 13 2019 Tobias Florek <me@ibotty.net> - 2.17-1
- bump version to 2.17

* Sat Jul 07 2018 Andrew DeMaria <lostonamountain@gmail.com> 2.16-2
- Update j4 dmenu (lostonamountain@gmail.com)
- Removed symlink (lostonamountain@gmail.com)
