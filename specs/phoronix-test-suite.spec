%global forgeurl https://github.com/phoronix-test-suite/phoronix-test-suite
%global commit   f977d6e270d5eb9eebfa26d3ca62385c00a547a6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date     20260826

Name:       phoronix-test-suite
Version:    10.8.6~%{date}git%{shortcommit}
Release:    %autorelease
Summary:    An Automated, Open-Source Testing Framework

License:    GPL-3.0-or-later
URL:        %{forgeurl}
Source0:    %{forgeurl}/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:    README.Fedora
BuildArch:  noarch

BuildRequires: desktop-file-utils
BuildRequires: systemd
BuildRequires: appstream

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
%autosetup -p1 -n %{name}-%{commit}
cp -p %{SOURCE1} documentation/

%build
# Nothing needed here

%install
export DESTDIR=%{buildroot}
./install-sh %{_prefix}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-launcher.desktop

# Fix AppStream validation warnings and missing OARS content rating
sed -i '/<content_rating/d' %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
sed -i '/<\/component>/i \  <url type="homepage">https://www.phoronix-test-suite.com/</url>' %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
sed -i '/<\/component>/i \  <developer_name>Phoronix Media</developer_name>' %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
sed -i '/<\/component>/i \  <content_rating type="oars-1.1"/>' %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

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
%{_datadir}/metainfo/com.phoronix_test_suite.phoronix_test_suite.metainfo.xml
%{_unitdir}/phoromatic-client.service
%{_unitdir}/phoromatic-server.service
%{_unitdir}/phoronix-result-server.service

%changelog
%autochangelog
