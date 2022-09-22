Name:           grc
Version:        1.13
Release:        %autorelease
Summary:        Generic Colorizer

License:        GPLv2
URL:            http://korpus.juls.savba.sk/~garabik/software/grc.html
Source0:        https://github.com/garabik/grc/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  sed

%description
Generic Colorizer is yet another colorizer for beautifying your log files or
output of commands.

%prep
%autosetup -p1
# replace symlinks with plain files
rm COPYING CHANGES
cp debian/copyright COPYING
cp debian/changelog CHANGES
sed -i -e '/^#!\//, 1d' grc.fish grc.zsh
sed -i.bak -e 's/env python/python/' grc grcat
sed -i -e 's/cp -fv /cp -fvp /' install.sh

%build

%install
./install.sh "$RPM_BUILD_ROOT%{_prefix}" "$RPM_BUILD_ROOT"

%files
%doc CREDITS README.markdown TODO CHANGES Regexp.txt
%license COPYING
%{_bindir}/grc
%{_bindir}/grcat
%{_datadir}/grc/
%config(noreplace) %{_sysconfdir}/grc.conf
%config(noreplace) %{_sysconfdir}/grc.fish
%config(noreplace) %{_sysconfdir}/grc.zsh
%config(noreplace) %{_sysconfdir}/profile.d/grc.sh
%{_mandir}/man1/grc.1*
%{_mandir}/man1/grcat.1*

%changelog
%autochangelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.11.3-1
- Update to 1.11.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.11.1-2
- Remove unnecessary BR python2-devel

* Sat Feb 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Mon May 30 2011 Carl van Tonder <carl@supervacuo.com> 1.4-1.fc16
- New upstream release

* Mon Feb 15 2010 Carl van Tonder <carl@supervacuo.com> 1.3-1f12
- Simplify release and escape changelog

* Sat Feb 13 2010 Carl van Tonder <carl@supervacuo.com> 1.3-0.2f12
- Remove unnecessary patch and simplify %%install

* Thu Feb 11 2010 Carl van Tonder <carl@supervacuo.com> 1.3-0.1.f12.svac
- Initial Fedora package
