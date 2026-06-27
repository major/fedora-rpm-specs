%global realname folsom

Name:		erlang-%{realname}
Version:	1.1.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang-based metrics system
License:	Apache-2.0
URL:		https://github.com/folsom-project/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-folsom-0001-Fix-generator-for-Erlang-27.patch
BuildRequires:	erlang-bear
BuildRequires:	erlang-meck
# For testing only
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-proper
BuildSystem:	rebar3

%description
Folsom is an Erlang based metrics system inspired by Coda Hale's metrics.
The metrics API's purpose is to collect realtime metrics from your Erlang
applications and publish them via Erlang APIs and output plugins. Folsom is not
a persistent store. There are 6 types of metrics: counters, gauges, histograms
and timers, histories, meter_readers and meters. Metrics can be created, read
and updated via the folsom_metrics module.

%prep -a
rm -f test/mochijson2.erl
rm -f test/mochinum.erl

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
