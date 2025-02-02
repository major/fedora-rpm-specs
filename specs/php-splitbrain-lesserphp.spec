%global vendor   splitbrain
%global project  lesserphp

Name:    php-%{vendor}-%{project}
Version: 0.10.2
Release: 2%{?dist}

Summary: A compiler for LESS written in PHP
License: MIT OR GPL-3.0-only

URL:     https://github.com/%{vendor}/%{project}/
Source0: %{URL}archive/v%{version}/%{project}-%{version}.tar.gz

Patch0: %{name}--exlude-tests-from-autoloader.patch

BuildArch: noarch

%global with_tests 1

%if 0%{?with_tests}
BuildRequires: phpunit9
%endif

BuildRequires: php-fedora-autoloader-devel

Requires: php(language) >= 7.4.0
Requires: php-ctype
Requires: php-fileinfo
Requires: php-composer(fedora/autoloader)

# Composer
Provides: php-composer(%{vendor}/%{project}) = %{version}

# Use a PSR-0 compatible directory hierarchy
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkg_vendor_dir %{phpdir}/%{vendor}
%global pkg_project_dir %{pkg_vendor_dir}/%{project}


%description
LesserPHP is a compiler for LESS written in PHP. It is based on lessphp
by leafo. The original has been abandoned in 2014. The fork by MarcusSchwarz
has been mostly abandoned in 2021. There are other forks with dubious status.

This is an opinionated fork with the goal to modernize the code base enough
to be somewhat easier to maintain without completely rewriting it.
It is meant to be used as a stable base for DokuWiki.
This means features not needed for this goal are removed.

Autoloader: %{pkg_project_dir}/autoload.php


%prep
%autosetup -p1 -n %{project}-%{version}


%build
# Create autoloader
phpab \
	--template fedora \
	--output autoload.php \
	--basedir src/ \
	composer.json
cat autoload.php


%install
install -d -m 755 %{buildroot}%{pkg_vendor_dir}
cp -a src %{buildroot}%{pkg_project_dir}

cp autoload.php %{buildroot}%{pkg_project_dir}/autoload.php


%if 0%{with_tests}
%check
phpunit9 --verbose --bootstrap %{buildroot}%{pkg_project_dir}/autoload.php
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{pkg_vendor_dir}/


%changelog
* Thu Jan 30 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10.2-2
- Remove unnecessary Obsoletes
- Fix directory ownership

* Mon Jan 20 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10.2-1
- Update to v0.10.2

* Sun Sep 01 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10.0-1
- Initial packaging
