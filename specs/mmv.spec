Name:		mmv
Version:	2.10
Release:	%autorelease
Summary:	Move/copy/link multiple files

License:	GPL-3.0-or-later
URL:		https://github.com/rrthomas/mmv
Source0:	https://github.com/rrthomas/mmv/releases/download/v%{version}/mmv-%{version}.tar.gz
BuildRequires:	make gcc

%description
This is mmv, a program to move/copy/append/link multiple files
according to a set of wildcard patterns. This multiple action is
performed safely, i.e. without any unexpected deletion of files due to
collisions of target names with existing filenames or with other
target names. Furthermore, before doing anything, mmv attempts to
detect any errors that would result from the entire set of actions
specified and gives the user the choice of either aborting before
beginning, or proceeding by avoiding the offending parts.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/mmv
%{_bindir}/mcp
%{_bindir}/mln
%{_bindir}/mad
%{_mandir}/man1/*.1*

%changelog
%autochangelog

