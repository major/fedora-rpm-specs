Name:        iverilog
Version:     12.0
%define uver 12_0
Release:     %autorelease
Summary:     Icarus Verilog is a verilog compiler and simulator
License:     GPLv2
URL:         https://github.com/steveicarus/iverilog
Source0:     https://github.com/steveicarus/iverilog/archive/%{name}-%{uver}.tar.gz
# [PATCH] Fix compilation with -Werror=format-security
Patch1:      23e51ef7a8e8e4ba42208936e0a6a25901f58c65.patch

BuildRequires: autoconf
BuildRequires: bzip2-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: gperf
BuildRequires: gcc-c++
BuildRequires: readline-devel
BuildRequires: zlib-devel
BuildRequires: make

 
%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.
 
%prep
%autosetup -n %{name}-%{uver}
# Clean junks from tarball
find . -type f -name ".git" -exec rm '{}' \;
rm -rf `find . -type d -name "autom4te.cache" -exec echo '{}' \;`

%build
chmod +x autoconf.sh
sh autoconf.sh
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure

# use make, avoid use V=1 due https://github.com/steveicarus/iverilog/issues/262
make %{?_smp_mflags}

 
%install
%{__make}    prefix=%{buildroot}%{_prefix} \
             bindir=%{buildroot}%{_bindir} \
             libdir=%{buildroot}%{_libdir} \
             libdir64=%{buildroot}%{_libdir} \
             includedir=%{buildroot}%{_includedir} \
             mandir=%{buildroot}%{_mandir}  \
             vpidir=%{buildroot}%{_libdir}/ivl/ \
             INSTALL="install -p" \
install
 
%check
make check
 
 
%files
%doc BUGS.txt QUICK_START.txt
%doc ieee1364-notes.txt mingw.txt swift.txt netlist.txt
%doc t-dll.txt vpi.txt cadpli/cadpli.txt
%doc xilinx-hint.txt examples/
%doc va_math.txt tgt-fpga/fpga.txt extensions.txt glossary.txt attributes.txt
%license COPYING
%{_bindir}/*
%{_libdir}/ivl
%{_mandir}/man1/*
# headers for PLI: This is intended to be used by the user.
%{_includedir}/*.h
# RHBZ 480531
%{_libdir}/*.a
 
 
%changelog
%autochangelog
