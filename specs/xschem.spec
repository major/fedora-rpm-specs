Name:           xschem
Version:        3.4.7
Release:        %autorelease
Summary:        Schematic capture and Netlisting EDA tool

License:        GPL-2.0-or-later
URL:            http://repo.hu/projects/xschem
Source0:        http://repo.hu/projects/xschem/releases/xschem-%{version}.tar.gz
Patch:          xschem-cairo-jpg-32bit.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
Recommends:     %{name}-doc = %{version}-%{release}
Requires:       tcl
Requires:       tk

%description
%{name} is a schematic capture program, it allows creation of hierarchical
representation of circuits with a top down approach. By focusing on
interfaces, hierarchy and instance properties, a complex system can be
described in terms of simpler building blocks. A VHDL or Verilog or Spice
netlist can be generated from the drawn schematic, allowing the simulation
of the circuit. Key feature of the program is its drawing engine written in C
and using directly the Xlib drawing primitives; this gives very good
speed performance, even on very big circuits. The user interface is
built with the Tcl-Tk toolkit, Tcl is also the extension language used.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.


%prep
%setup -q

# Fix wrong line encoding (CRLF to LF) of C files to apply patches cleanly
sed -i 's/\r$//' src/cairo_jpg.c

%patch -P 0 -p1

# Fix wrong line encoding (CRLF to LF)
sed -i 's/\r$//' src/make_sym_lcc.awk

# Remove shebang from non-executable script
sed -i '1{\@^#!/@d}' src/make_sym_lcc.awk

# Ensure LDFLAGS are passed when building rawtovcd to enable PIE/hardening
sed -i 's/rawtovcd rawtovcd.o/rawtovcd rawtovcd.o $(LDFLAGS)/' src/Makefile.in



%build
./"configure" --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}" \
    --prefix=%{_prefix} --symbols
%make_build


%install
%make_install


%files
%license LICENSE
%doc AUTHORS Changelog README
%{_bindir}/%{name}
%{_bindir}/rawtovcd
%{_datadir}/%{name}
%{_mandir}/man1/xschem.1*


%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/AUTHORS
%exclude %{_docdir}/%{name}/Changelog
%exclude %{_docdir}/%{name}/README



%changelog
%autochangelog
