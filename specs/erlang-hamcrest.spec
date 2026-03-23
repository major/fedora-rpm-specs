%global realname hamcrest
%global git_commit 0766ea004f7dd900c36b06aff14dbbac1d03b425
%global git_date 20181106

Name:		erlang-%{realname}
Version:	0.1.0
Release:	%autorelease -s %{git_date}git%{sub %git_commit 0 7}
BuildArch:	noarch
Summary:	A framework for writing matcher objects using declarative rules
License:	BSD-3-Clause
URL:		https://github.com/hyperthunk/%{realname}-erlang
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-proper
BuildSystem:	rebar3

%description
Hamcrest is a framework for writing matcher objects allowing 'match' rules to
be defined declaratively. There are a number of situations where matchers are
invaluable, such as UI validation, or data filtering, but it is in the area of
writing flexible tests that matchers are most commonly used.

%check
# FIXME requires proprietary library - QuickCheck

%files
%license LICENCE
%doc NOTES README.markdown
%{erlang_appdir}/

%changelog
%autochangelog
