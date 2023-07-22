%global file_name com.github.hannesschulze.optimizer

Name:           optimizer
Version:        1.2.1
Release:        11%{?dist}
Summary:        Find out what's eating up your system resources

License:        GPLv3+
URL:            https://github.com/hannesschulze/optimizer/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-fallback-theme.patch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)

Requires:       hicolor-icon-theme

%description
Find out what's eating up your system resources and delete unnecessary files
from your disk.

%prep
%autosetup
# Quick fix for wrong location translate file
# https://github.com/hannesschulze/optimizer/pull/59/files
mv ru.po po/ru.po

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{file_name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{file_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{file_name}.desktop

%files -f %{file_name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{file_name}
%{_datadir}/applications/%{file_name}.desktop
%{_datadir}/glib-2.0/schemas/%{file_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{file_name}.svg
%{_metainfodir}/%{file_name}.appdata.xml

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-6
- Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Tue Apr 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.0-1
- Update to 1.2.0
- Enabled fallback theme which is better suits Adwaita GTK theme

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.1.0-3
- Rebuild with Meson fix for #1699099

* Wed Mar 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-2
- Initial Package
