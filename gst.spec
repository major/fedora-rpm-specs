%global uuid    com.leinardi.%{name}

Name:           gst
Version:        0.7.5
Release:        10%{?dist}
Summary:        System utility designed to stress and monitoring various hardware components

License:        GPLv3+
URL:            https://gitlab.com/leinardi/gst
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.45.1
BuildRequires:  python3-devel

BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.56.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30

Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       lm_sensors
Requires:       python3-gobject >= 3.38.0
Requires:       python3-humanfriendly >= 8.2
Requires:       python3-injector >= 0.18.4
Requires:       python3-matplotlib-gtk3 >= 3.1.1
Requires:       python3-peewee >= 3.14.4
Requires:       python3-psutil >= 5.8.0
Requires:       python3-pyxdg >= 0.27
Requires:       python3-pyyaml >= 5.4.1
Requires:       python3-requests >= 2.25.1
Requires:       python3-rx >= 3.1.1

Recommends:     dmidecode
Recommends:     stress-ng

%description
GST is a GTK system utility designed to stress and monitoring various hardware
components like CPU and RAM.

- Run different CPU and memory stress tests
- Run multi and single core benchmark
- Show Processor information (name, cores, threads, family, model, stepping,
  flags,bugs, etc)
- Show Processor's cache information
- Show Motherboard information (vendor, model, bios version, bios date, etc)
- Show RAM information (size, speed, rank, manufacturer, part number, etc)
- Show CPU usage (core %, user %, load avg, etc)
- Show Memory usage
- Show CPU's physical's core clock (current, min, max)
- Show Hardware monitor (info provided by sys/class/hwmon)


%prep
%autosetup
sed -e '/meson_post_install/d' -i meson.build


%build
%meson
%meson_build


%install
%meson_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2x/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING.txt
%doc CHANGELOG.md README.md RELEASING.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.7.5-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.5-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.5-3
- Rebuilt for Python 3.10

* Sat Apr 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.5-2
- build: Bump dependencies

* Mon Mar 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.5-1
- build(update): 0.7.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Mon Feb 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-1
- Update to 0.7.1

* Sun Feb 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jan 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-5
- Add dep 'lm_sensors'

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-3
- Add dep 'dmidecode'

* Mon Jan 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-2
- Add dep 'stress-ng'

* Sun Jan 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Sun Jan 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-5
- Initial package
