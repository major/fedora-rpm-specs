%global srcname jose

Name:      erlang-%{srcname}
Version:   1.11.12
Release:   %autorelease
BuildArch: noarch
License:   MIT
Summary:   JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
URL:       https://github.com/potatosalad/%{name}
VCS:       git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-base64url
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3
BuildRequires: erlang-triq
Recommends: erlang-jiffy
Recommends: erlang-jsx

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# FIXME Not enough dependencies
#%%{erlang3_test}

%files
%license LICENSE.md
%doc ALGORITHMS.md
%doc CHANGELOG.md
%doc examples
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
