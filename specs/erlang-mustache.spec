%global realname mustache

Name:		erlang-%{realname}
Version:	0.1.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Mustache template engine for Erlang
License:	MIT
URL:		https://github.com/mojombo/%{realname}.erl
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-mustache-0001-Migrate-to-a-new-Meck.patch
BuildRequires:	erlang-meck
BuildSystem:	rebar3

%description
An Erlang port of Mustache for Ruby. Mustache is a framework-agnostic template
system that enforces separation of view logic from the template file. Indeed, it
is not even possible to embed logic in the template. This allows templates to be
reused across language boundaries and for other language independent uses.

%files
%license LICENSE
%doc examples/ README.md
%{erlang_appdir}/

%changelog
%autochangelog
