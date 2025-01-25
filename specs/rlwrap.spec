Name:           rlwrap
Version:        0.46.1
Release:        %autorelease
Summary:        Wrapper for GNU readline

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/hanslub42/rlwrap
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-rpm-macros
BuildRequires:  readline-devel

%description
rlwrap is a 'readline wrapper' that uses the GNU readline library to
allow the editing of keyboard input for any other command. Input
history is remembered across invocations, separately for each command;
history completion and search work as in bash and completion word
lists can be specified on the command line.


%prep
%autosetup -p1


%build
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
# issues with rl_message function signature even though readline is not upgraded
# https://gcc.gnu.org/gcc-15/porting_to.html
# readline.c: In function ‘message_in_echo_area’:
# readline.c:192:5: error: too many arguments to function ‘rl_message’; expected 0, have 1
#   192 |     rl_message(message);
#       |     ^~~~~~~~~~ ~~~~~~~
# In file included from rlwrap.h:189,
#                  from readline.c:23:
# /usr/include/readline/readline.h:410:12: note: declared here
#   410 | extern int rl_message ();
#       |            ^~~~~~~~~~
# seems related to the switch to -std=gnu23 but not sure how:
# https://gcc.gnu.org/gcc-15/porting_to.html
# reported upstream in https://github.com/hanslub42/rlwrap/issues/195
export CFLAGS="%{optflags} -std=gnu17"
%endif

%configure
%make_build


%install
%make_install

# Fix shebangs to prevent bogus requirements
%{__sed} -r -i \
    -e 's|^#!.*perl$|#!%{__perl}|g' \
    -e 's|^#!.*python3$|#!%{__python3}|g' \
    $(find %{buildroot}%{_datadir}/%{name}/ -type f)


%check
make check


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/rlwrap
%{_mandir}/*/rlwrap.*
%{_mandir}/man3/RlwrapFilter.*
%{_datadir}/rlwrap



%changelog
%autochangelog
