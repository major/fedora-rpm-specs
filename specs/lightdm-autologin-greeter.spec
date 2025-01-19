Name:           lightdm-autologin-greeter
Version:        1.0
Release:        22%{?dist}
Summary:        Autologin greeter using LightDM

License:        MIT
URL:            https://github.com/spanezz/lightdm-autologin-greeter
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Source1:        %{name}.README.distro

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
Requires:       python3-gobject
%else
BuildRequires:  python2-devel
Requires:       pygobject3
%endif
Requires:       lightdm-gobject

# LightDM is required for this to be useful
Requires:       lightdm

# All LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

BuildArch:      noarch

%description
%{name} is a minimal greeter for LightDM that has
the same autologin behavior as nodm, but being based on LightDM,
it stays on top of modern display manager requirements.

The difference between LightDM's built-in autologin and this greeter,
is the behavior in case of 0-seconds autologin delay. When LightDM
automatically logs in with no delay, upon logout it will show the
login window again. The intent is that if the default user logged out,
they probably intend to log in again as a different user.

In the case of managing a kiosk-like setup, if the X session quits, then
the desired behavior is to just start it again.

LightDM with an autologin timeout of 1 or more seconds would work,
but one sees the login dialog window appear and disappear
on-screen at each system startup.

With this greeter, the X session starts right away, and is restarted
if it quits, without any flicker of a login dialog box.

If one is not setting up a kiosk-like setup, it's very likely that the
default autologin behavior of LightDM is the way to go, and that this
greeter is not needed.



%prep
%autosetup
# Install Source1 into source tree
cp %{S:1} README.distro

%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_prefix}

cp -a bin %{buildroot}%{_prefix}
cp -a share %{buildroot}%{_prefix}

%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i "s:#!/usr/bin/python:#!%{__python3}:" %{buildroot}%{_bindir}/%{name}
%else
sed -i "s:#!/usr/bin/python:#!%{__python2}:" %{buildroot}%{_bindir}/%{name}
%endif


%files
%license LICENSE
%doc README.md README.distro
%{_bindir}/%{name}
%{_datadir}/xgreeters/%{name}.desktop
%{_datadir}/lightdm/lightdm.conf.d/60-%{name}.conf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Neal Gompa <ngompa13@gmail.com> - 1.0-5
- Revert removing lightdm-greeter Provides

* Mon Aug 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0-4
- Remove provides lightdm-greeter as it is matched first on netinstall (rhbz #1481192)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Neal Gompa <ngompa13@gmail.com> - 1.0-2
- Rename distro readme file to README.distro on install

* Mon May 15 2017 Neal Gompa <ngompa13@gmail.com> - 1.0-1
- Update to 1.0

* Mon May 15 2017 Neal Gompa <ngompa13@gmail.com> - 0-0.git20170515.22021f3
- Initial packaging
