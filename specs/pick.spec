Name:           pick
Version:        4.0.0
Release:        %autorelease
Summary:        A fuzzy search tool for the command-line

# The entire source code is MIT except for
# compat-reallocarray.c and compat-strtonum.c files which are ISC
License:        MIT AND ISC
URL:            https://github.com/mptre/pick
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix discarded qualifier
Patch: fix-discarded-qualifiers.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

# nmh also provides /usr/bin/pick
Conflicts:      nmh

%description
The pick utility allows users to choose one option from a set of choices using
an interface with fuzzy search functionality. pick reads a list of choices on
stdin and outputs the selected choice on stdout. Therefore it is easily used
both in pipelines and subshells.

%prep
%autosetup

%build
export PREFIX=%{_prefix}
export MANDIR=%{_mandir}
export INSTALL_MAN="install -p -m 0644"
%configure
%make_build CFLAGS="%{build_cflags} -D_GNU_SOURCE"

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
