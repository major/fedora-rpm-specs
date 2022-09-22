Name:           tty-copy
Version:        0.2.2
Release:        %autorelease
Summary:        Copy content to system clipboard via TTY and terminal using ANSI OSC52 sequence

License:        MIT
URL:            https://github.com/jirutka/tty-copy
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoctor
BuildRequires:  gcc
BuildRequires:  make

%description
tty-copy is a utility for copying content to the system clipboard from
anywhere via a TTY and terminal using the ANSI OSC52 sequence. It works in any
terminal session, whether local, remote (e.g. SSH), or even nested therein.


%prep
%autosetup -p1


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{_prefix}


%check
# no test suite, so just smoke test it, as they do on CI
%{buildroot}%{_bindir}/tty-copy -V


%files
%license LICENSE
%doc README.adoc
%{_bindir}/tty-copy
%{_mandir}/man1/tty-copy.1*


%changelog
%autochangelog
