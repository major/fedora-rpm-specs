Name:       light
Version:    1.2.2
Release:    7%{?dist}
Summary:    Control backlight controllers

License:    GPLv3
URL:        http://haikarainen.github.io/light/
Source0:    https://github.com/haikarainen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: help2man
BuildRequires: automake
BuildRequires: make


%description
Light is a program to control backlight controllers under GNU/Linux,
it is the successor of lightscript, which was a bash script
with the same purpose, and tries to maintain the same functionality.

Features

- Works excellent where other software have been proven unusable
  or problematic, thanks to how it operates internally
  and the fact that it does not rely on X.
- Can automatically figure out the best controller to use,
  making full use of underlying hardware.
- Possibility to set a minimum brightness value, as some controllers
  set the screen to be pitch black at a value of 0 (or higher).


%prep
%setup -q


%build
%global build_cflags %{optflags} -fcommon
./autogen.sh
%configure
%make_build


%install
%make_install


%post
# Make sure that all saved files have correct permissions
# after fixing RHBZ 1792875
if [ -e "%{_sysconfdir}/%{name}" ]; then
    chown -R :root %{_sysconfdir}/%{name}
fi


%files
%doc COPYING
%doc ChangeLog.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Jakub Kadlčík <jkadlcik@redhat.com> - 1.2.2-2
- Fix post hook for fresh installations where /etc/light
  does not exist yet

* Fri Mar 20 2020 Jakub Kadlčík <jkadlcik@redhat.com> - 1.2.2-1
- Upgrade to new upstream version light-1.2.2

* Wed Mar 18 2020 Jakub Kadlčík <jkadlcik@redhat.com> - 1.2.1-5
- Add post hook to set correct permissions for /etc/light

* Wed Mar 18 2020 Jakub Kadlčík <jkadlcik@redhat.com> - 1.2.1-4
- Fix RHBZ 1792875 - Escalation of Privileges via "light" SUID Binary

* Sun Feb 16 2020 Jakub Kadlčík <jkadlcik@redhat.com> - 1.2.1-3
- Explicitly use -fcommon to fix building for F32

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jakub Kadlcik <jkadlcik@redhat.com> - 1.2.1-1
- Upgrade to new upstream version light-1.2.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Jakub Kadlcik <jkadlcik@redhat.com> - 1.1.2-1
- Upgrade to new upstream version light-1.1

* Sun Jun 10 2018 Jakub Kadlcik <jkadlcik@redhat.com> - 1.1-1
- Upgrade to new upstream version light-1.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Jakub Kadlcik <frostyx@email.cz> 1.0-1
- initial package
