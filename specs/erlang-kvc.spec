%global realname kvc

Name:		erlang-%{realname}
Version:	1.7.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Key Value Coding for Erlang data structures
License:	MIT
URL:		https://github.com/etrepum/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-kvc-0001-Pass-source-files-through-epp-before-edoc-gen.patch
Patch:		erlang-kvc-0002-More-greedy-guard.patch
BuildSystem:	rebar3

%description
kvc supports Key Value Coding-like queries on common Erlang data structures. A
common use case for kvc is to quickly access one or more deep values in decoded
JSON, or some other nested data structure. It can also help with some aggregate
operations. It solves similar problems that you might want to use a tool like
XPath or jQuery for, but it is far simpler and strictly less powerful. It's
inspired by Apple's NSKeyValueCoding protocol from Objective-C.

%files
%license LICENSE
%doc CHANGES.md README.md
%{erlang_appdir}/

%changelog
%autochangelog
