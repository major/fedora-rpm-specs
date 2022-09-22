Name:           classification-banner
Version:        1.7.0
Release:        16%{?dist}
Summary:        Displays Classification Banner for a Graphical Session

License:        GPLv2+
URL:            https://github.com/SecurityCentral/classification-banner
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3
Requires:       xrandr
Requires:       python3-gobject
Requires:       gtk3

%description
Classification Banner is a python script that will display the
classification level banner of a session with a variety of
configuration options on the primary screen.  This script can
help government and possibly private customers display a 
notification that sensitive material is being displayed - for 
example PII or SECRET Material being processed in a graphical
session. The script has been tested on a variety of graphical
environments such as GNOME2, GNOME3, KDE, twm, icewm, and Cinnamon.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

install -d -m755 %{buildroot}%{_datadir}/%{name}
install -d -m755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m755 %{buildroot}%{_sysconfdir}/xdg/autostart/

install -pm644 contrib/banner.conf %{buildroot}%{_sysconfdir}/%{name}/banner.conf
install -pm644 share/%{name}-screenshot.png %{buildroot}%{_datadir}/%{name}/%{name}-screenshot.png

desktop-file-install \
--dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
contrib/%{name}.desktop

%check
export DISPLAY=":0.0"
%{__python3} setup.py test

%files
%license LICENSE
%doc README.md AUTHOR Contributors.md
%{python3_sitelib}/classification_banner
%{python3_sitelib}/classification_banner-%{version}-py%{python3_version}.egg-info

%config(noreplace) %{_sysconfdir}/%{name}/banner.conf
%config(noreplace) %{_sysconfdir}/xdg/autostart/classification-banner.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}-screenshot.png

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.0-15
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.0-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 1.7.0-10
- Require xrandr not xorg-x11-server-utils

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-8
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Remove requirement of PyGTK2

* Tue Jan 8 2019 Gabe <redhatrises@gmail.com> - 1.7.0-1
- Remove usage of PyGTK2
- Use python3
- Various cleanups

* Thu Aug 9 2018 Gabe <redhatrises@gmail.com> - 1.6.7-1
- First package for EPEL
