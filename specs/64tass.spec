%global revision 3243

Name:           64tass
Version:        1.60.%{revision}
Release:        %autorelease
Summary:        Multi-pass optimizing macro assembler for the 65xx series of processors
# The main code is GPL-2.0-or-later
# Some parts are LGPL-2.0-only, LGPL-2.0-or-later, LGPL-2.1-or-later, and MIT
License:        GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://tass64.sourceforge.net/
Source0:        https://downloads.sourceforge.net/tass64/source/%{name}-%{version}-src.zip

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  unzip

%description
64tass is a multi-pass optimizing macro assembler for the 65xx series of
processors. It supports the 6502, 65C02, R65C02, W65C02, 65CE02, 65816,
DTV, and 65EL02, using a syntax similar to that of Omicron TASS and TASM.

%prep
%autosetup -n %{name}-%{version}-src

# be verbose during build
sed -i -e 's/.SILENT://' Makefile

%build
%make_build CFLAGS='%{build_cflags} -DREVISION="\""%{revision}"\""' LDFLAGS="%{build_ldflags}"

%install
install -D -p -m 755 64tass %{buildroot}%{_bindir}/64tass
install -D -p -m 644 64tass.1 %{buildroot}%{_mandir}/man1/64tass.1

%check
# Basic check to ensure the binary was built correctly and to silent rpmlint
./%{name} --version

%files
%license LICENSE-GPL-2.0
%license LICENSE-LGPL-2.0 LICENSE-LGPL-2.1
%license LICENSE-my_getopt
%doc README README.md README.html NEWS
%doc examples/ syntax/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
