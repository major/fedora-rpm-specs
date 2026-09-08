Name:           bash-preexec
Version:        0.6.0
Release:        %autorelease
Summary:        preexec and precmd functions for Bash just like Zsh

License:        MIT
URL:            https://github.com/rcaloras/bash-preexec
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  bats
BuildArch:      noarch

# TODO: Remove this in the next release when it is made compatible
#  https://github.com/rcaloras/bash-preexec/pull/143
# The sh file has a note that the DEBUG and PROMPT_COMMAND variables should not be
# overwritten. Other implementations like ble.sh do not seem to have that limitation though :/
Provides:       bash(PROMPT_COMMAND)
Conflicts:      bash(PROMPT_COMMAND)
Provides:       bash(DEBUG)
Conflicts:      bash(DEBUG)

%global _description %{expand:
preexec and precmd hook functions for Bash 3.1+ in the style of Zsh. They aim to
emulate the behavior as described for}

%description %_description

%package        all-users
Summary:        bash-preexec init script for all users
Requires:       bash-preexec = %{version}-%{release}

# Note: This package should conflict with any other package that uses `PROMPT_COMMAND` or `DEBUG`
# (See General Usage section of bash-preexec.sh)

%description    all-users %_description

This package contains the init script to enable bash-preexec for all users.


%prep
%autosetup -p1


%install
install -Dpm 644 bash-preexec.sh %{buildroot}%{_libexecdir}/bash-preexec/bash-preexec.sh
# Backport import guards into the auto-import script
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/bash-preexec.sh <<EOF
# bash-preexec initialization script

# Skip non-bash shells.
[ -z "\${BASH_VERSION-}" ] && return

# Skip noninteractive shells.
[[ \$- != *i* ]] && return

source %{_libexecdir}/bash-preexec/bash-preexec.sh
EOF


%check
bats test

%files
%license LICENSE.md
%doc README.md
%dir %{_libexecdir}/bash-preexec
%{_libexecdir}/bash-preexec/bash-preexec.sh

%files all-users
%config(noreplace) %{_sysconfdir}/profile.d/bash-preexec.sh


%changelog
%autochangelog
