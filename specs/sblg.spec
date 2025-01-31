Name:           sblg
Version:        0.6.1
Release:        %{autorelease}
Summary:        Static blog utility
%global ver     %(v=%{version}; echo ${v//\./_})

License:        ISC
URL:            https://kristaps.bsd.lv/sblg/
VCS:            git:https://github.com/kristapsdz/sblg.git
Source:         https://github.com/kristapsdz/sblg/archive/VERSION_%{ver}/sblg-VERSION_%{ver}.tar.gz

BuildRequires:  gcc
BuildRequires:  expat-devel
BuildRequires:  make
BuildRequires:  valgrind

Recommends:  lowdown

%description
sblg is a utility for creating static blogs. It merges articles into templates
to generate static HTML files, Atom feeds, and JSON files. It's built for use
with make. No PHP, no database, just a simple UNIX tool for pulling data from
articles and populating templates. 

%package doc
BuildArch: noarch
Summary: Static blog utility


%description doc
Examples and documentation for sblg.

%prep
%autosetup -n sblg-VERSION_%{ver}


%build
# Does not use autotools, so passing fedora flags causes an error
./configure PREFIX=%{_prefix} MANDIR=%{_mandir} SHAREDIR=%{_docdir} LDFLAGS="${LDFLAGS}"
%make_build


%install
%make_install
# Ensure has correct permissions
chmod 755 %{buildroot}/%{_bindir}/sblg

%check
make regress
make valgrind

%files
%license LICENSE.md
%doc README.md
%{_bindir}/sblg
%{_mandir}/man1/sblg.1*

%files doc
%license LICENSE.md
%{_docdir}/sblg/

%changelog
%autochangelog
