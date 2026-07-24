Name:           xgrep
Version:        0.08
Release:        %autorelease
Summary:        A grep-like utility for XML files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.wohlberg.net/public/software/xml/xgrep/
Source0:        http://www.wohlberg.net/public/software/xml/xgrep/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  libxml2-devel
BuildRequires:  make

%description
XGrep provides facilities for searching content in XML files.  The
search is specified either as an XPath via the -x flag, or a custom
syntax including extended regular expressions via the -s flag.


%prep
%autosetup


%build
%configure
make depend
%make_build


%install
%make_install


%check


%files
%license GPL
%doc README ChangeLog NEWS
%{_bindir}/xgrep
%{_mandir}/man1/xgrep.1*


%changelog
%autochangelog
