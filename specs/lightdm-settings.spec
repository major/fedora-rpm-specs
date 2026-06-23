Name:		lightdm-settings
Version:	2.1.1
Release:	2%{?dist}
Summary:	Configuration tool for the LightDM display manager

License:	GPL-3.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	make

Requires:	filesystem
Requires:	gtk3
Requires:	hicolor-icon-theme
Requires:	polkit
Requires:	python3-xapp
Requires:	python3-gobject
Requires:	python3-setproctitle
Requires:	slick-greeter

%description
This tool currently lets users configure slick-greeter.


%prep
%autosetup -p 1

%build
%make_build

%install
# No install-target in Makefile.
%{__cp} -pr .%{_prefix} %{buildroot}

# Set exec-permissions where needed.
%{__chmod} -c 0755 %{buildroot}%{_bindir}/%{name} \
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}

# Find localizations and build manifest.
%find_lang %{name}

%check
%{_bindir}/desktop-file-validate \
	%{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license debian/copyright COPYING
%doc debian/changelog README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/polkit-1/actions/org.x.%{name}.policy


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 09 2026 Leigh Scott <leigh123linux@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Sat Dec 13 2025 Leigh Scott <leigh123linux@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Sun Nov 30 2025 Leigh Scott <leigh123linux@gmail.com> - 2.0.9-1
- Update to 2.0.9

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Leigh Scott <leigh123linux@gmail.com> - 2.0.7-1
- Update to 2.0.7

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Tue Aug 20 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Wed Jun 05 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.2-1
- Update to 2.0.2 release

* Mon Dec 04 2023 Leigh Scott <leigh123linux@gmail.com> - 2.0.1-1
- Update to 2.0.1 release

* Thu Nov 30 2023 Leigh Scott <leigh123linux@gmail.com> - 2.0.0-1
- Update to 2.0.0 release
