%global realname mochiweb

Name:		erlang-%{realname}
Version:	3.3.0
Release:	%autorelease
BuildArch:	noarch
Summary:	An Erlang library for building lightweight HTTP servers
License:	MIT
URL:		https://github.com/mochi/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-xmerl
Provides:	%{realname} = %{version}-%{release}

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}
rm -f .gitignore ./examples/example_project/.gitignore

%build
%{erlang3_compile}

%install
%{erlang3_install}

# Additional skeleton files
cp -arv scripts %{buildroot}%{_erllibdir}/%{realname}-%{version}
cp -arv support %{buildroot}%{_erllibdir}/%{realname}-%{version}

%check
%{erlang3_test}

%files
%license LICENSE
%doc CHANGES.md README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
