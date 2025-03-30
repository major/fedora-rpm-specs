%global realname proper

Name:       erlang-%{realname}
Version:    1.5.0
Release:    %autorelease
BuildArch:  noarch
License:    GPL-3.0-or-later
Summary:    A QuickCheck-inspired property-based testing tool for Erlang
URL:        https://github.com/proper-testing/%{realname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
PropEr (PROPerty-based testing tool for ERlang) is a QuickCheck-inspired
open-source property-based testing tool for Erlang.

%prep
%autosetup -p1 -n %{realname}-%{version}
sed -i -e "/covertool/d" ./rebar.config

%build
# The docs need to be built first: https://github.com/proper-testing/proper/issues/179
./scripts/make_doc
%{erlang3_compile}
# FIXME one particular test needs this
ln -s _build/default/lib/proper/ebin .

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license COPYING
%doc doc
%doc examples
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
