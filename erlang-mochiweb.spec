%global realname mochiweb
%global upstream mochi


Name:		erlang-%{realname}
Version:	3.1.2
Release:	%autorelease
BuildArch:	noarch
Summary:	An Erlang library for building lightweight HTTP servers
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-xmerl
Provides:	%{realname} = %{version}-%{release}


%description
An Erlang library for building lightweight HTTP servers.


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
