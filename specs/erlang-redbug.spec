%global realname redbug

Name: erlang-%{realname}
Version: 2.0.10
Release: %autorelease
BuildArch: noarch
License: MIT
Summary: Erlang tracing debugger
URL: https://github.com/massemanet/redbug
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
redbug is a tool to interact with the Erlang trace facility. It is intended to
be run from the erlang shell, but it can also be run from an OS shell as an
escript (see below). It will instruct the Erlang VM to generate so-called
'trace messages' when certain events (such as a particular function being
called) occur. It uses a safe subset of the tracing functionality, and exits if
it feels overloaded, e.g. if it gets flooded by trace messages. It runs in the
background, collecting trace messages, until it reaches one of its termination
criteria (number of messages/file size or elapsed time).

The trace messages are either printed (i.e. human readable) to a file or to the
screen; or written to a trc file. Using a trc file puts less stress on the
system, but there is no way to count the messages (so the 'msgs' opt is
ignored), and the files can only be read by special tools (such as 'bread').
Printing and trc files cannot be combined. By default (i.e. if the 'file' opt
is not given), messages are printed.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
