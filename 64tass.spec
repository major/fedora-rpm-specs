%global revision 3120

Name:		64tass
Version:	1.59.%{revision}
Release:	%autorelease
Summary:	6502 assembler
License:	LGPL-2.0-only AND LGPL-2.0-or-later AND GPL-2.0-or-later AND MIT
URL:		http://tass64.sourceforge.net/
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	w3m
Source0:	http://sourceforge.net/projects/tass64/files/source/%{name}-%{version}-src.zip

%description
64tass is a multi-pass optimizing macro assembler for the 65xx series of
processors. It supports the 6502, 65C02, R65C02, W65C02, 65CE02, 65816,
DTV, and 65EL02, using a syntax similar to that of Omicron TASS and TASM.

%prep
%autosetup -n %{name}-%{version}-src
rm README  # will be built

# be verbose during build
sed -i -e 's/.SILENT://' Makefile

%build
%make_build CFLAGS='%{build_cflags} -DREVISION="\""%{revision}"\""' LDFLAGS="%{build_ldflags}"

%install
# install binaries
install -d %{buildroot}%{_bindir}/
install -m 755 64tass %{buildroot}%{_bindir}/
# install man page
install -d %{buildroot}%{_mandir}/man1
install -m 644 64tass.1 %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc README.html
%license LICENSE-GPL-2.0
%license LICENSE-LGPL-2.0 LICENSE-LGPL-2.1
%license LICENSE-my_getopt

%changelog
%autochangelog
