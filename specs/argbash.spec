Name: argbash
Version: 2.11.0
Release: %autorelease
Summary: Bash argument parsing code generator
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://argbash.dev
Source0: https://github.com/matejak/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: autoconf
BuildRequires: coreutils
BuildRequires: make
BuildRequires: bash
BuildRequires: bash-completion
BuildRequires: python%{python3_pkgversion}-docutils
BuildRequires: ShellCheck

Requires: autoconf
Requires: bash
Requires: coreutils
Requires: grep
Requires: sed

%if !0%{?rhel} || 0%{?rhel} > 7
Recommends: bash-completion
%endif

# Submitted upstream: https://github.com/matejak/argbash/pull/177


%description
Argbash helps your shell scripts to accept arguments.
You declare what arguments you want your script to accept and Argbash
generates the shell code that parses them from the command-line and exposes
passed values as shell variables.

Help message is also generated, and helpful error messages are dispatched
if the script is called with arguments that conflict with the interface.

%prep
%autosetup -p1

%build

%install
cd resources && \
    ROOT=%{buildroot} \
    PREFIX=%{_prefix} \
    PREFIXED_LIBDIR=%{_datarootdir} \
    SYSCONFDIR=%{_sysconfdir} \
    INSTALL_COMPLETION=yes \
    BASH_COMPLETION_DIRECTORY=%{_datarootdir}/bash-completion/completions \
    make install

%check
cd resources && %{make_build} check

%files
%license LICENSE
%doc README.md ChangeLog
%{_mandir}/man1/argbash*

%{_bindir}/argbash
%{_bindir}/argbash-1to2
%{_bindir}/argbash-init
%{_datarootdir}/argbash/
%{_datarootdir}/bash-completion/completions/argbash

%changelog
%autochangelog
