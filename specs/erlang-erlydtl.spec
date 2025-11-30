%global realname erlydtl

Name:		erlang-%{realname}
Version:	0.15.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang implementation of the Django Template Language
License:	MIT
URL:		https://github.com/erlydtl/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-erlydtl-0001-FIXME-disable-slex-for-now.patch
Provides:	ErlyDTL = %{version}-%{release}
BuildRequires:	erlang-gettext
BuildRequires:	erlang-rebar3

%description
ErlyDTL is an Erlang implementation of the Django Template Language. The
erlydtl module compiles Django Template source code into Erlang bytecode. The
compiled template has a "render" function that takes a list of variables and
returns a fully rendered document.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
cp -arv priv %{buildroot}/%{erlang_appdir}/

%check
# FIXME
#%%{erlang3_test -C rebar-tests.config}
#REBAR_CONFIG=./rebar-tests.config %%{erlang3_test}

%files
%license LICENSE
%doc CONTRIBUTING.md NEWS.md README.markdown README_I18N
%{erlang_appdir}/

%changelog
%autochangelog
