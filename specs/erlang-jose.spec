%global srcname jose

Name:      erlang-%{srcname}
Version:   1.11.13
Release:   %autorelease
BuildArch: noarch
License:   MIT
Summary:   JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
URL:       https://github.com/potatosalad/%{name}
VCS:       git:%{url}.git
Source:	   %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:     erlang-jose-0001-Don-t-compare-zlib-output-byte-by-byte-in-rfc7520_5_.patch
BuildRequires: erlang-jiffy
BuildRequires: erlang-jsx
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3
BuildSystem: rebar3
BuildOption(check): -e

%description
%{summary}.

%prep -a
# Downloads its test vectors from the network
rm test/cavp_SUITE.erl
# A helper of cavp_SUITE which jose_SUITE uses too
mv test/cavp_SUITE_data/hex.erl test/

%files
%license LICENSE.md
%doc ALGORITHMS.md
%doc CHANGELOG.md
%doc examples
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
