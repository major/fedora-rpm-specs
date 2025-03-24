%global realname webmachine

Name:		erlang-%{realname}
Version:	1.12.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A REST-based system for building web applications
License:	Apache-2.0
URL:		https://github.com/webmachine/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-webmachine-0001-Enable-verbose-output-during-testing.patch
Patch:		erlang-webmachine-0002-FIXME-this-test-fails-constantly.patch
BuildRequires:	erlang-ibrowse
BuildRequires:	erlang-meck
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}
chmod 644 src/wmtrace_resource.erl
chmod -x priv/trace/wmtrace.css
chmod -x priv/trace/wmtrace.js

%build
%{erlang3_compile}

%install
%{erlang3_install}
# Additional resources
cp -arv priv %{buildroot}%{erlang_appdir}/

%check
%{erlang3_test}

%files
%license LICENSE
%doc docs/http-headers-status-v3.png README.md THANKS
%{erlang_appdir}/

%changelog
%autochangelog
