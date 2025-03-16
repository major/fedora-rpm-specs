%bcond check 1

Name:           xdg-terminal-exec
Version:        0.12.2
Release:        %autorelease
Summary:        Proposed XDG Default Terminal Execution Spec implementation

License:        GPL-3.0-or-later
URL:            https://github.com/Vladimir-csp/xdg-terminal-exec
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  scdoc
BuildRequires:  sed
%if %{with check}
BuildRequires:  bats
%endif

BuildArch:      noarch

%description
This package provides a reference shell-based implementation for a proposed XDG
Default Terminal Execution Specification. The proposal can be found at:

https://gitlab.freedesktop.org/terminal-wg/specifications/-/merge_requests/3

Please be advised that while this spec is in proposed state, backwards
compatibility is maintained as best effort and is not guaranteed.

%prep
%autosetup -p1

# Preserve timestamps on install
sed -i 's/install -Dm/install -Dpm/g' Makefile

%build
%make_build

%install
%make_install prefix="%{buildroot}%{_prefix}"

%if %{with check}
%check
make test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
