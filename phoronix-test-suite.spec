Name:       phoronix-test-suite
Version:    10.8.4
Release:    %autorelease
Summary:    An Automated, Open-Source Testing Framework

License:    GPLv3+
URL:        http://%{name}.com/
Source0:    http://www.%{name}.com/releases/%{name}-%{version}.tar.gz
Source1:    README.Fedora
# Fix for CVE reported in https://github.com/phoronix-test-suite/phoronix-test-suite/issues/650
Patch0:     https://github.com/phoronix-test-suite/phoronix-test-suite/commit/d3880d9d3ba795138444da83f1153c3c3ac27640.diff#/CVE-2022-40704.diff
BuildArch:  noarch

BuildRequires: desktop-file-utils
BuildRequires: systemd
BuildRequires: libappstream-glib
BuildRequires: appdata-tools

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires: php-cli
Requires: php-xml
Requires: php-json
Requires: php-openssl
Requires: php-gd
Requires: php-sqlite3
Requires: php-posix
Requires: php-curl
Requires: hicolor-icon-theme


#These packages are not included anymore
#Packages required by tests. Use the following command to create this list:
#cat phoronix-test-suite/pts-core/external-test-dependencies/xml/fedora-packages.xml phoronix-test-suite/pts-core/external-test-dependencies/xml/generic-packages.xml| grep PackageName |sed -e 's/^.*<PackageName>\([^<]*\)<\/PackageName>.*$/\1/g' |xargs yum info|grep Name|sed -e 's/.*:\s\([^\s]*\)/\1/g'|grep -v devel$|sort|uniq|xargs
#Requires: autoconf automake bison blas cmake curl flex gcc gcc-c++ gcc-gfortran jam libcurl libtool make openmpi p7zip perl python scons tcl tcsh yasm

%description
The Phoronix Test Suite is the most comprehensive testing and benchmarking 
platform available for the Linux operating system. This software is designed to 
effectively carry out both qualitative and quantitative benchmarks in a clean, 
reproducible, and easy-to-use manner. The Phoronix Test Suite consists of a 
lightweight processing core (pts-core) with each benchmark consisting of an 
XML-based profile with related resource scripts. The process from the benchmark 
installation, to the actual benchmarking, to the parsing of important hardware 
and software components is heavily automated and completely repeatable, asking 
users only for confirmation of actions.

%prep
%autosetup -n %{name} -p1
cp -p %{SOURCE1} documentation/

%build
# Nothing needed here

%install
export DESTDIR=%{buildroot}
./install-sh %{_prefix}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-launcher.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%post
%systemd_post phoromatic-client.service
%systemd_post phoromatic-server.service
%systemd_post phoronix-result-server.service

%postun
%systemd_postun_with_restart phoromatic-client.service
%systemd_postun_with_restart phoromatic-server.service
%systemd_postun_with_restart phoronix-result-server.service

%preun
%systemd_preun phoromatic-client.service
%systemd_preun phoromatic-server.service
%systemd_preun phoronix-result-server.service

%files
%doc %{_datadir}/doc/%{name} 
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/phoronix-test-suite.png
%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-openbenchmarking.png
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_unitdir}/phoromatic-client.service
%{_unitdir}/phoromatic-server.service
%{_unitdir}/phoronix-result-server.service

%changelog
%autochangelog
