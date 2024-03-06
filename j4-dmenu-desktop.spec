%define git_revision 7e3fd045482a8ea70619e422975b52feabc75175

Name:           j4-dmenu-desktop
Version:        2.19
Release:        0.1.20230912git%{?dist}
Summary:        Generic menu for desktop managers
License:        GPLv3
URL:            https://github.com/enkore/j4-dmenu-desktop
# Source0:        https://github.com/enkore/%%{name}/archive/r%%{version}/%%{name}-r%%{version}.tar.gz
Source0:        https://github.com/enkore/%{name}/archive/%{git_revision}/%{name}-%{git_revision}.tar.gz
BuildRequires:  cmake
BuildRequires:  catch1-devel
BuildRequires:  gcc-c++

%description
%{name} is a replacement for i3-dmenu-desktop.
It's purpose is to find .desktop files and offer you a menu to start an
application using dmenu.  It should work just fine on about any desktop
environment.  You can also execute shell commands using it.

%prep
# %%autosetup -n %%{name}-r%%{version}
%autosetup -n %{name}-%{git_revision}

%build
%cmake -DWITH_GIT_CATCH=OFF -DCATCH_INCLUDE_DIR=/usr/include/catch
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
* Fri Mar 01 2024 Tobias Florek <tob@butter.sh> - 2.19-0.1.20230912git
- Use catch1 explicitly
- use git snapshot

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
