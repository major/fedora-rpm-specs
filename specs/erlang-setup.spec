%global realname setup

Name:		erlang-%{realname}
Version:	2.2.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Generic setup utility for Erlang-based systems
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-setup-0001-Don-t-escriptize.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar3

%description
While Erlang/OTP comes with many wonderful applications, including the Mnesia
DBMS, there is no standard or convention for installing a system. Erlang/OTP
provides tools for building a boot script, and rules for setting environment
variables, etc., and Mnesia offers an API for creating and modifying the
database schema.

However, with no convention for when these tools and API functions are called -
and by whom - application developers are left having to invent a lot of code
and scripts, not to mention meditate over chapters of Erlang/OTP documentation
in order to figure out how things fit together.

This utility offers a framework for initializing and configuring a system, with
a set of conventions allowing each component to provide callbacks for different
steps in the installation procedure.

The callbacks are defined through OTP application environment variables, which
can easily be overriden at install time.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc doc/ examples/ README.md
%{erlang_appdir}/

%changelog
%autochangelog
