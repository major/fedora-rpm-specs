%global realname erlware_commons

Name:     erlang-%{realname}
Version:  1.8.1
Release:  %autorelease
Summary:  Extension to Erlang's standard library
License:  MIT
URL:      https://github.com/erlware/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
# The "color" tests does not play well with Fedora's build system - no tty in
# mock, so we disable it.
Patch:    erlang-erlware_commons-0001-Disable-color-test.patch
Patch:    erlang-erlware_commons-0002-Use-correct-version-instead-of-relying-to-git-one.patch
BuildArch:     noarch
BuildRequires: erlang-cf
BuildRequires: erlang-rebar3
# For tests only
BuildRequires: git-core

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
cp -arv priv/ %{buildroot}%{erlang_appdir}/

%check
%{erlang3_test}

%files
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
