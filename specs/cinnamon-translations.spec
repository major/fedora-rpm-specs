%global _trans_version 2018.12.11

%global upstream_version 6.7.0-unstable

Name:           cinnamon-translations
Version:        6.7.0^unstable
Release:        2%{?dist}
Summary:        Translations for Cinnamon and Nemo

License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%{_trans_version}.tar.xz
BuildRequires:  gettext
BuildRequires:  make

BuildArch:      noarch

%description
Translations for Cinnamon, Nemo and Mintlocale.


%prep
%autosetup -a1 -p1 -n %{name}-%{upstream_version}


%build
%{make_build}
%{make_build} -C mint-translations


%install
# install mint translations for mintlocale
%{_bindir}/find mint-translations -not -name 'mintlocale.mo' -type f -delete
%{_bindir}/find . -name 'cinnamon-bluetooth.mo' -type f -delete
%{__cp} -pr mint-translations/%{_datadir}/linuxmint/locale .%{_datadir}
%{__cp} -pr .%{_prefix} %{buildroot}

%find_lang cinnamon
%find_lang mintlocale
%find_lang nemo
%find_lang nemo-extensions
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon

%files -f cinnamon.lang -f mintlocale.lang -f nemo.lang -f nemo-extensions.lang -f cinnamon-control-center.lang -f cinnamon-screensaver.lang -f cinnamon-session.lang -f cinnamon-settings-daemon.lang
%license COPYING


%changelog
* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0^unstable-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 09 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Sat Dec 13 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Leigh Scott <leigh123linux@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Tue Nov 26 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.2-2
- convert license to SPDX

* Sun Jul 21 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.2-1
- Update to 6.0.2 release

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-1
- Update to 6.0.0 release
