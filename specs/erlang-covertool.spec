%global realname covertool

Name: erlang-%{realname}
Version: 2.0.7
Release: %autorelease
BuildArch: noarch
License: BSD-2-Clause-Views
Summary: Tool to convert Erlang cover data files into Cobertura XML reports
URL: https://github.com/covertool/covertool
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
A simple tool to convert exported Erlang cover data sets into Cobertura XML
reports. The report could be then feed to the Jenkins Cobertura plug-in.

%prep
%autosetup -p1 -n %{realname}-%{version}
# FIXME this test was designed for rebar2, and it doesn't work with rebar3. We
# need to update it. The test is not critical, so we just disable it for now.
rm -f test/rebar_covertool_tests.erl

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
# We do not want to pull in Elixir as a dependency so we just ignore these
# messages. This function is called only if mix is used.
## ERROR: Cant find Elixir.Mix:raise/1 while processing '.../ebin/mix_covertool.beam'

# We do not ship rebar2, so these are valid messages. But these functions are
# called only if rebar2 is used.
## ERROR: Cant find rebar_app_utils:app_name/2 while processing '.../ebin/rebar_covertool.beam'
## ERROR: Cant find rebar_config:get_local/3 while processing '.../ebin/rebar_covertool.beam
%{erlang_appdir}

%changelog
%autochangelog
