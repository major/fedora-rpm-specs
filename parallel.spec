Name:           parallel
Summary:        Shell tool for executing jobs in parallel
Version:        20221022
Release:        %autorelease

License:        GFDL and GPLv3+
URL:            https://www.gnu.org/software/parallel/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  perl-FileHandle
BuildRequires:  sed

%define __requires_exclude sh$

# Due to a naming conflict, both packages cannot be installed in parallel
# To prevent user confusion, GNU parallel is installed in a compatibility
# mode to be commandline compatible to moreutils' parallel.
# This mode can be turned off system wide or on a per-user base.
Conflicts:      moreutils-parallel

%description
GNU Parallel is a shell tool for executing jobs in parallel using one or more
machines. A job is typically a single command or a small script that has to be
run for each of the lines in the input. The typical input is a list of files, a
list of hosts, a list of users, or a list of tables.

If you use xargs today you will find GNU Parallel very easy to use. If you
write loops in shell, you will find GNU Parallel may be able to replace most of
the loops and make them run faster by running jobs in parallel. If you use ppss
or pexec you will find GNU Parallel will often make the command easier to read.

GNU Parallel also makes sure output from the commands is the same output as you
would get had you run the commands sequentially. This makes it possible to use
output from GNU Parallel as input for other programs.

GNU Parallel is command-line-compatible with moreutils' parallel, but offers
additional features.

%prep
%autosetup
# Replace shebang by replacing "env" by removing "env ".
# FIXME: this is quite a hack
sed -i '1s:/env :/:' src/env_parallel.*

%build
autoreconf -ivf
%configure
%make_build

%install
%make_install
rm -vrf %{buildroot}%{_pkgdocdir}

%files
%license LICENSES/GPL-3.0-or-later.txt LICENSES/GFDL-1.3-or-later.txt
%doc README NEWS
%{_bindir}/parallel
%{_bindir}/parcat
%{_bindir}/parset
%{_bindir}/parsort
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/parcat.1*
%{_mandir}/man1/parset.1*
%{_mandir}/man1/parsort.1*
%{_mandir}/man7/parallel*
%{_bindir}/env_parallel*
%{_mandir}/man1/env_parallel.1*
%{_bindir}/sem
%{_mandir}/man1/sem.1*
%{_bindir}/sql
%{_mandir}/man1/sql.1*
%{_bindir}/niceload
%{_mandir}/man1/niceload.1*
%{_datadir}/bash-completion/completions/parallel
%{_datadir}/zsh/site-functions/_parallel

%changelog
%autochangelog
