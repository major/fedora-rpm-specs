Name:     scdoc
Version:  1.11.3
Release:  %autorelease
Summary:  Tool for generating roff manual pages

License:  MIT
URL:      https://git.sr.ht/~sircmpwn/%{name}
Source0:  %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: sed

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%autosetup -p1

# Disable static linking
sed -i '/-static/d' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
%if 0%{?el7}
%make_install PREFIX=%{_prefix} INSTALL="%{__install} -p"
%else
%make_install PREFIX=%{_prefix}
%endif

%check
make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
# Not shipped in a -devel package since scdoc is a development tool not
# installed in a user runtime.
%{_datarootdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
