%global author   splitbrain
%global project  slika
Name: php-%{author}-%{project}

Version: 1.0.5
Release: 3%{?dist}

Summary: Image handling library for PHP
License: MIT

URL: https://github.com/%{author}/%{project}

# The test cases work by editing some images and comparing the actual result
# to the expected one. The images are stored in Git-LFS and are not included
# in the code archives available on GitHub.
#
# The slika-get-archive.sh script is used to clone the repository,
# fetch the images and zip it all up.
Source0: %{project}-%{version}.zip
Source99: slika-get-archive.sh

BuildArch: noarch

%global with_tests 1

BuildRequires: php(language) >= 5.5.0
BuildRequires: php-fedora-autoloader-devel

%if 0%{with_tests}
BuildRequires: ImageMagick
BuildRequires: php-gd
BuildRequires: php-pcre
BuildRequires: phpunit8
%endif

Requires: php(language) >= 5.5.0
Requires: php-pcre

Requires: php-composer(fedora/autoloader)

Requires: (php-gd or ImageMagick)
Recommends: php-gd

Provides: php-composer(%{author}/%{project}) = %{version}

# Use a PSR-0 compatible directory hierarchy
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/slika


%description
Slika is a simple image handling library for PHP. It covers only
the bare basics you need when handling images: resizing, cropping, rotation.

It can use either PHP's libGD or a locally installed ImageMagick binary.

Autoloader: %{pkgdir}/autoload.php


%prep
%setup -q -n %{project}-%{version}

# Exclude the tests from the composer file
sed -e '/"splitbrain\\\\slika\\\\tests\\\\":/d' -i composer.json


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


%if 0%{with_tests}
%check
cat > ./bootstrap.php <<EOF
<?php
require '%{buildroot}%{pkgdir}/autoload.php';

require __DIR__ . '/tests/TestCase.php';
EOF

phpunit8 --verbose --bootstrap ./bootstrap.php
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%{pkgauthordir}/


%changelog
* Thu Oct 06 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.5-3
- Fix package being non-installable due to borked dependencies

* Wed Sep 28 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.5-2
- Add missing dependencies (as reported by phpcompatinfo)
- Make package directory hierarchy PSR-0 compatible

* Sat Sep 17 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.5-1
- Initial packaging
