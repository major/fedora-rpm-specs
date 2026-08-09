%global realname emmap
%global git_commit f4a6f82d20a4ea08f723a033988b9a83bbcaf850
%global git_date 20230313

Name:		erlang-%{realname}
Version:	2.0.11
Release:	%autorelease -s %{git_date}git%{sub %git_commit 0 7}
Summary:	Erlang mmap interface
License:	Apache-2.0
URL:		https://github.com/saleyn/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
Patch1:		erlang-emmap-0001-Fix-for-i686.patch
Patch2:		erlang-emmap-0002-Enough-space-for-i686.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-rebar3-pc
BuildRequires:	gcc
BuildRequires:	gcc-c++

%description
This Erlang library provides a wrapper that allows you to memory map files into
the Erlang memory space.

%prep
%ifarch %{ix86}
%autosetup -p1 -n %{realname}-%{git_commit}
%else
%autosetup -N -n %{realname}-%{git_commit}
%endif

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
