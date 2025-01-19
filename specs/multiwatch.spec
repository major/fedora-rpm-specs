Name:           multiwatch
Version:        1.0.0
Release:        14%{?dist}
Summary:        Forks and watches multiple instances of a program in the same context
License:        MIT
URL:            https://redmine.lighttpd.net/projects/multiwatch/wiki
Source0:        https://download.lighttpd.net/multiwatch/releases-1.x/multiwatch-%{version}.tar.xz

# https://git.lighttpd.net/lighttpd/multiwatch/commit/bdd50b7910ebfd04f70e39cb688e3a4851505ac4.patch
Patch0:         multiwatch-1.0.0-fix_signal.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libev-devel


%description
Multiwatch forks multiple instance of one application and keeps them running.
It is made to be used with spawn-fcgi, so all forks share the same fastcgi
socket (no web server restart needed if you increase/decrease the number of
forks), and it is easier than setting up multiple daemontool supervised
instances.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc README
%{_bindir}/multiwatch
%{_mandir}/man1/multiwatch.1.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Xavier Bachelot <xavier@bachelot.org> - 1.0.0-3
- Fix spelling in %%description

* Thu Apr 23 2020 Xavier Bachelot <xavier@bachelot.org> - 1.0.0-2
- Add upstream patch to fix --signal behaviour

* Thu Dec 05 2019 Xavier Bachelot <xavier@bachelot.org> - 1.0.0-1
- Initial package
