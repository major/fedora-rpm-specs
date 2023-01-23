%global appname com.github.alecaddd.%{name}

Name:           taxi
Version:        2.0.1
Release:        4%{?dist}
Summary:        The FTP Client that drives you anywhere

License:        GPLv3+
URL:            https://github.com/Alecaddd/taxi
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)

Requires:       hicolor-icon-theme

%description
Taxi is a native Linux FTP client built in Vala and Gtk originally created by
Kiran John Hampal. It allows you to connect to a remote server with various
Protocols (FTP, SFT, etc.), and offers an handy double paned interface to
quickly transfer files and folders between your computer and the server.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{appname}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop


%files -f %{appname}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.appdata.xml


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.1-1
- build(update): 2.0.1

* Fri Aug 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-1
- build(update): 2.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 0.0.1-6
- Rebuilt for granite 6 soname bump.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.1-2
- Initial package
