%global srcname p1_utils

Name:       erlang-%{srcname}
Version:    1.0.27
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    Erlang utility modules from ProcessOne
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
p1_utils is an application containing ProcessOne modules and tools that are
leveraged in other development projects.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
