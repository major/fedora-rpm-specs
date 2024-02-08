Name:           moreutils
Version:        0.68
Release:        %autorelease
Summary:        Additional unix utilities
License:        GPLv2
URL:            https://joeyh.name/code/moreutils/
Source0:        https://git.kitenet.net/index.cgi/moreutils.git/snapshot/moreutils-%{version}.tar.gz
# fixes docbook XSL path
Patch1:         0001-dont-overwrite-docbooxsl-path.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  docbook2X
BuildRequires:  docbook-dtds
BuildRequires:  libxml2
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  docbook-style-xsl
Requires:       perl(TimeDate)
Requires:       perl(Time::Duration)
Requires:       perl(Time::HiRes)
Requires:       perl(IPC::Run)
# These perl modules add functionality to the ts command, as they are added in eval'd code they are not
# picked up automatically by rpm.

%description
 This is a growing collection of the unix tools that nobody thought
 to write thirty years ago.

 So far, it includes the following utilities:
  - chronic: runs a command quietly, unless it fails
  - combine: combine the lines in two files using boolean operations
  - errno: look up errno names and descriptions
  - ifdata: get network interface info without parsing ifconfig output
  - ifne: run a program if the standard input is not empty
  - isutf8: check if a file or standard input is utf-8
  - lckdo: execute a program with a lock held
  - mispipe: pipe two commands, returning the exit status of the first
  - parallel: run multiple jobs at once (contained in moreutils-parallel
              sub package)
  - pee: tee standard input to pipes
  - sponge: soak up standard input and write to a file
  - ts: timestamp standard input
  - vidir: edit a directory in your text editor
  - vipe: insert a text editor into a pipe
  - zrun: automatically uncompress arguments to command

%package parallel
Summary:        Additional unix utility - parallel command
Requires:       %{name} = %{version}-%{release}
Conflicts:      parallel

%description parallel
 This is a growing collection of the unix tools that nobody thought
 to write thirty years ago.

 This is a sub package containing the parallel command only.

  - parallel: run multiple jobs at once


%prep
%autosetup -n %{name}-%{version}
# the required dtd's are not where this package expects them to be, let's fix that
DTDFILE=`xmlcatalog /usr/share/sgml/docbook/xmlcatalog "-//OASIS//DTD DocBook XML V4.4//EN" "-//OASIS//DTD DocBook XML V4.3//EN"|grep -v "No entry"|head -n1`
sed -r -i "s|/usr/share/xml/docbook/schema/dtd/4.4/docbookx.dtd|$DTDFILE|" *.docbook
# the docbook2x-man command is different in fedora, let's fix that too
sed -r -i "s|docbook2x-man|db2x_docbook2man|" Makefile
# a slightly different syntax is required here for the man pages to be built successfully
sed -r -i "s| rep=\"repeat\"||" *.docbook
# add path to pdf2man
sed -r -i "s|pod2man|/usr/bin/pod2man|" Makefile
# don't strip bins
sed -r -i "s|install -s|install|" Makefile

%build
%make_build

%check
make check

%install
%make_install

%files
%doc README COPYING
%{_mandir}/man1/chronic.1.gz
%{_mandir}/man1/combine.1.gz
%{_mandir}/man1/errno.1.gz
%{_mandir}/man1/ifdata.1.gz
%{_mandir}/man1/ifne.1.gz
%{_mandir}/man1/isutf8.1.gz
%{_mandir}/man1/lckdo.1.gz
%{_mandir}/man1/mispipe.1.gz
%{_mandir}/man1/pee.1.gz
%{_mandir}/man1/sponge.1.gz
%{_mandir}/man1/ts.1.gz
%{_mandir}/man1/vidir.1.gz
%{_mandir}/man1/vipe.1.gz
%{_mandir}/man1/zrun.1.gz
%{_bindir}/chronic
%{_bindir}/combine
%{_bindir}/errno
%{_bindir}/ifdata
%{_bindir}/ifne
%{_bindir}/isutf8
%{_bindir}/lckdo
%{_bindir}/mispipe
%{_bindir}/pee
%{_bindir}/sponge
%{_bindir}/ts
%{_bindir}/vidir
%{_bindir}/vipe
%{_bindir}/zrun

%files parallel
%doc README COPYING
%{_mandir}/man1/parallel.1.gz
%{_bindir}/parallel

%changelog
%autochangelog
