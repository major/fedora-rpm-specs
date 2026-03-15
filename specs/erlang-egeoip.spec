%global realname egeoip
%global git_commit 4efda2c2b5b0084d3e77b8f0bbdec78514706b34
%global git_date 20140111

Name:		erlang-%{realname}
Version:	1.1
Release:	%autorelease -s %{git_date}git%{sub %git_commit 0 7}
BuildArch:	noarch
Summary:	Erlang IP Geolocation module
License:	MIT
URL:		https://github.com/mochi/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
Patch1:		erlang-egeoip-0001-FIXME-an-old-DB-in-Fedora.patch
Patch2:		erlang-egeoip-0002-Fix-for-Rebar3.patch
BuildRequires:	GeoIP-GeoLite-data-extra
Requires:	GeoIP-GeoLite-data-extra
BuildSystem:	rebar3

%description
Erlang IP Geolocation module, currently supporting the MaxMind GeoLite City
Database.

%install -a
mkdir -p %{buildroot}%{erlang_appdir}/priv/
ln -s %{_datadir}/GeoIP/GeoIPCity.dat %{buildroot}%{erlang_appdir}/priv/GeoIPCity.dat
ln -s %{_datadir}/GeoIP/GeoLiteCity.dat %{buildroot}%{erlang_appdir}/priv/GeoLiteCity.dat
ln -s %{_datadir}/GeoIP/GeoLiteCountry.dat %{buildroot}%{erlang_appdir}/priv/GeoIP.dat

%files
%license LICENSE
%doc README
%{erlang_appdir}/

%changelog
%autochangelog
