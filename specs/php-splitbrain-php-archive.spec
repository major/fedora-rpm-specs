%global author   splitbrain
%global project  php-archive
Name: php-%{author}-%{project}

Version: 1.3.1
Release: 8%{?dist}

Summary: Pure-PHP implementation to read and write TAR and ZIP archives
License: MIT

URL: https://splitbrain.github.io/php-archive/
Source0: https://github.com/%{author}/%{project}/archive/%{version}/%{project}-%{version}.tar.gz

BuildArch: noarch

%global with_tests 1

BuildRequires: php(language) >= 7.1.0
BuildRequires: php-fedora-autoloader-devel

%if 0%{?with_tests}
BuildRequires: php-bz2
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-zip
BuildRequires: php-zlib

BuildRequires: php-composer(mikey179/vfsstream) >= 1.6
BuildRequires: phpunit8
%endif

Requires: php(language) >= 7.0.0
Requires: php-date
Requires: php-hash
Requires: php-pcre

Requires: php-composer(fedora/autoloader)

Recommends: php-bz2
Recommends: php-iconv
Recommends: php-mbstring
Recommends: php-zlib

Provides: php-composer(%{author}/%{project}) = %{version}

# Use a PSR-0 compatible directory name
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/PHPArchive


%description
PHPArchive allows to handle new ZIP and TAR archives without the need
for any special PHP extensions (gz and bzip are needed for compression).
It can create new files or extract existing ones.

To keep things simple, the modification (adding or removing files)
of existing archives is not supported.

Autoloader: %{pkgdir}/autoload.php


%prep
%setup -q -n %{project}-%{version}


%build
# Create autoloader
phpab \
	--template fedora \
	--output autoload.php \
	--basedir src/ \
	./composer.json
cat autoload.php


%install
install -d -m 755 %{buildroot}%{pkgauthordir}
cp -a src %{buildroot}%{pkgdir}

cp autoload.php %{buildroot}%{pkgdir}/autoload.php


%if 0%{?with_tests}
%check
# phpunit doesn't seem to accept multiple --boostrap files.
cat > bootstrap.php <<EOF
<?php
require '%{phpdir}/org/bovigo/vfs/autoload.php';
require '%{buildroot}%{pkgdir}/autoload.php';
EOF

phpunit8 --verbose --bootstrap ./bootstrap.php 
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%{pkgauthordir}/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3.1-2
- Add missing dependencies (as reported by phpcompatinfo)
- Make package directory hierarchy PSR-0 compatible

* Thu Sep 15 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3.1-1
- Initial packaging
