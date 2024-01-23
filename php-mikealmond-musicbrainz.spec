Name:       php-mikealmond-musicbrainz
Version:    0.2.2
Release:    15%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    A PHP library to access MusicBrainz's Web Service v2
URL:        https://github.com/mikealmond/MusicBrainz
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: php-composer(fedora/autoloader)
BuildRequires: php-fedora-autoloader-devel
BuildRequires: phpunit 

Requires:   php(language) >= 5.3.8
Requires:   php-composer(fedora/autoloader)
Requires:   php-curl
Requires:   php-date
Requires:   php-filter
Requires:   php-json
Requires:   php-pcre
Requires:   php-spl

Provides:   php-composer(mikealmond/musicbrainz) = %{version}


%description
This PHP library that allows you to easily access the MusicBrainz Web
Service V2 API. Visit the MusicBrainz development page for more
information.

This project is a fork of https://github.com/chrisdawson/MusicBrainz and
takes some inspiration from the Python bindings.


%prep
%autosetup -n MusicBrainz-%{version}


%build
cat <<'AUTOLOAD' | tee src/MusicBrainz/autoload.php
<?php
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('MusicBrainz', __DIR__);
AUTOLOAD


%install
install -d -p -m 0755 %{buildroot}/%{_datadir}/php
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/MusicBrainz

cp -ar src/MusicBrainz/* %{buildroot}/%{_datadir}/php/MusicBrainz


%check
phpunit --no-coverage --bootstrap %{buildroot}/%{_datadir}/php/MusicBrainz/autoload.php


%files
%license LICENSE.md
%doc composer.json
%doc README.md
%{_datadir}/php/MusicBrainz


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2.2-1
- Initial release.
